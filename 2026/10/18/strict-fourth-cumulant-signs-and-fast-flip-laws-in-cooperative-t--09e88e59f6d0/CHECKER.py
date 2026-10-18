#!/usr/bin/env python3
"""Exact fourth-cumulant checks for linearly filtered symmetric telegraph forces.

Requirements: Python 3 and SymPy. All equalities tested over rational numbers.
"""
from itertools import product
from math import comb
import sympy as sp


def filtered_fourth_cumulant(eigenvalues, coefficients, flipping_rate):
    """Independent integration of the ordered four-time telegraph cumulant."""
    rate = sp.sympify(flipping_rate)
    ans = sp.S.Zero
    for idx in product(range(len(eigenvalues)), repeat=4):
        a, b, c, d = [eigenvalues[i] for i in idx]
        prefactor = sp.prod(coefficients[i] for i in idx)
        denominator = ((a+b+c+d)*(b+c+d+2*rate)*
                       (c+d+4*rate)*(d+2*rate))
        ans += prefactor/denominator
    return sp.factor(-48*ans)


def filtered_variance(eigenvalues, coefficients, flipping_rate):
    """Independent integration of the two-time telegraph covariance."""
    rate = sp.sympify(flipping_rate)
    ans = sp.S.Zero
    for i, j in product(range(len(eigenvalues)), repeat=2):
        a, b = eigenvalues[i], eigenvalues[j]
        ans += (coefficients[i]*coefficients[j]*
                (1/(a+2*rate)+1/(b+2*rate))/(a+b))
    return sp.factor(ans)


def generator_moments(matrix, input_vector, rate, maximum_degree=4):
    """Solve polynomial moment balance of dot X=AX+b sigma with flip rate."""
    A = sp.Matrix(matrix)
    n = A.rows
    drive = sp.Matrix(input_vector)
    assert A.cols == n and drive.rows == n
    moments = {(tuple([0]*n),0): sp.S.One,
               (tuple([0]*n),1): sp.S.Zero}
    for degree in range(1, maximum_degree+1):
        def multi_indices(dim, size):
            if dim == 1:
                yield (size,)
            else:
                for t in range(size+1):
                    for tail in multi_indices(dim-1, size-t):
                        yield (t,)+tail
        keys = [(alpha,e) for alpha in multi_indices(n,degree)
                for e in (0,1)]
        unknown = sp.symbols('u0:'+str(len(keys)))
        fresh = dict(zip(keys,unknown))
        def get(alpha,e):
            key = (tuple(alpha),e)
            return fresh[key] if key in fresh else moments[key]
        equations = []
        for alpha,e in keys:
            expr = -2*rate*e*get(alpha,e)
            for i in range(n):
                if not alpha[i]:
                    continue
                beta=list(alpha)
                beta[i]-=1
                for j in range(n):
                    gamma=beta.copy()
                    gamma[j]+=1
                    expr += alpha[i]*A[i,j]*get(gamma,e)
                expr += alpha[i]*drive[i]*get(beta,1-e)
            equations.append(expr)
        mat,rhs=sp.linear_eq_to_matrix(equations,unknown)
        solved=mat.inv()*rhs
        moments.update({key:sp.factor(val) for key,val in zip(keys,solved)})
    return moments


def readout_cumulant(moments, readout):
    assert len(readout)==2
    c0,c1=readout
    var=sum(comb(2,i)*c0**i*c1**(2-i)*
            moments[((i,2-i),0)] for i in range(3))
    fourth=sum(comb(4,i)*c0**i*c1**(4-i)*
               moments[((i,4-i),0)] for i in range(5))
    return sp.factor(var),sp.factor(fourth-3*var**2)


def check():
    q=sp.Rational
    z=sp.symbols('z', positive=True)
    eigenvalues=[sp.S.One,sp.S(3)]
    positive_response=[q(1,2),q(-1,2)]  # (exp(-t)-exp(-3t))/2 is positive at t>0
    exact_variance=(z+2)/(6*(2*z+1)*(2*z+3))
    exact_cumulant=-(8*z**4+116*z**3+646*z**2+1655*z+1400)/(
      20*(2*z+1)**2*(2*z+3)**2*(2*z+5)*(2*z+7)*(2*z+9))
    assertions=0
    def verify(predicate, description):
        nonlocal assertions
        assert bool(predicate),description
        assertions+=1
    verify(sp.cancel(filtered_variance(eigenvalues,positive_response,z)-exact_variance)==0,
           'exact analytic two-site variance')
    verify(sp.cancel(filtered_fourth_cumulant(eigenvalues,positive_response,z)-exact_cumulant)==0,
           'exact analytic two-site fourth cumulant')
    verify(sp.limit(z**3*exact_cumulant,z,sp.oo)==-q(1,320),
           'sharp inverse-cubic fourth cumulant')
    verify(sp.limit(z*exact_variance,z,sp.oo)==q(1,24),
           'sharp inverse-linear variance')
    verify(sp.limit(z*exact_cumulant/exact_variance**2,z,sp.oo)==-q(9,5),
           'sharp inverse-linear excess kurtosis')
    verify(sp.limit(exact_cumulant,z,0)==-q(2,81),
           'static-telegraph cumulant endpoint')
    verify(sp.integrate(((sp.exp(-z)-sp.exp(-3*z))/2)**2,
                        (z,0,sp.oo))==q(1,24), 'response L2')
    verify(sp.integrate(((sp.exp(-z)-sp.exp(-3*z))/2)**4,
                        (z,0,sp.oo))==q(1,960), 'response L4')
    for rate in [q(1,4),sp.S.One,sp.S(2),sp.S(10)]:
        generator=generator_moments([[-2,1],[1,-2]],[1,0],rate)
        var,k4=readout_cumulant(generator,[0,1])
        verify(var==exact_variance.subs(z,rate),'generator vs integral variance')
        verify(k4==exact_cumulant.subs(z,rate),'generator vs integral fourth cumulant')
        verify(k4<0,'strict negative fourth cumulant at test rate')
    signed=[sp.S.One,sp.S(-3)]  # exp(-t)-3 exp(-3t), sign-changing
    rate=q(1,10)
    signed_kernel=filtered_fourth_cumulant(eigenvalues,signed,rate)
    verify(signed_kernel==q(10825,918528), 'exact positive signed-response fourth cumulant')
    gen_signed=generator_moments([[-1,0],[0,-3]],[1,1],rate)
    var_signed, k4_signed=readout_cumulant(gen_signed,[1,-3])
    verify(k4_signed==signed_kernel,'signed-response independent generator check')
    verify(k4_signed>0 and var_signed>0,'signed-response positivity is real')
    for rate in [q(1,5),sp.S.One,sp.S(5)]:
        # A single oscillator with unit stiffness and unit active force.
        one=filtered_fourth_cumulant([sp.S.One],[sp.S.One],rate)
        verify(one==-6/((1+2*rate)**2*(3+2*rate)),
               'single-site independent beta-law check')
    print('PASS: %d independent exact-rational or symbolic assertions' % assertions)
    print('two-site variance:',exact_variance)
    print('two-site fourth cumulant:',exact_cumulant)
    print('positive signed-response fourth cumulant:',signed_kernel)


if __name__=='__main__':
    check()
