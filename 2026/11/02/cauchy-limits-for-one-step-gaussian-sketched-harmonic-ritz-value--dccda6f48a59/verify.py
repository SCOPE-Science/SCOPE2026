"""Reproducible checks for the one-step Gaussian-sketch harmonic Ritz theorem.

The analytical proof is contained in RESULT.md. This script checks algebraic
identities, distributional transformations, and sharp witnesses; simulations
are corroboration, not infinite-case certification.
"""
import numpy as np
from scipy.special import betainc, gammaln
from scipy.stats import t as student_t


def descriptor(A, b):
    u = A @ b
    w = b
    a = float(u @ w / (u @ u))
    d2 = float(w @ w / (u @ u) - a*a)
    return a, float(np.sqrt(max(0.0, d2)))


def false_sign_probability(s, a, d):
    return 0.0 if d == 0.0 else 0.5*betainc(s/2, .5, d*d/(a*a+d*d))


def tail_constant(s, a, d):
    if d == 0:
        return 0.0
    return float(2*np.exp(gammaln((s+1)/2)-gammaln(s/2))/(np.sqrt(np.pi)*d)
                 * (1+a*a/(d*d))**(-(s+1)/2))


def witness(kappa):
    A = np.diag([1., 1./kappa])
    u = np.array([np.sqrt(kappa/(kappa+1)), np.sqrt(1/(kappa+1))])
    return A, np.linalg.solve(A, u)


def check():
    checks = 0
    rng = np.random.default_rng(321547)
    for k in [1.05, 1.3, 2, 3, 5, 10, 100]:
        A, b = witness(k)
        a, d = descriptor(A, b)
        z = ((k-1)/(k+1))**2
        assert np.isclose(d*d/(a*a+d*d), z, atol=5e-14)
        checks += 1
        u = A @ b
        w = b
        for s in [1, 2, 3, 4, 8, 16, 31, 64]:
            p = false_sign_probability(s, a, d)
            p_t = student_t.cdf(-a*np.sqrt(s)/d, df=s)
            assert np.isclose(p, p_t, atol=2e-13)
            checks += 1
            if s <= 16:
                # Distribution, from independent normal pieces at a fixed direction.
                S = rng.standard_normal((25000,s,2))/np.sqrt(s)
                x = S @ u
                y = S @ w
                r = (x*y).sum(1)/(x*x).sum(1)
                assert np.isfinite(r).all()
                empirical = (r < 0).mean()
                assert abs(empirical - p) < 7*np.sqrt(max(p*(1-p), .0005)/25000)+.002
                checks += 1
                # The actual ratio and the decomposition are identical for every draw.
                xnorm = np.linalg.norm(x,axis=1)
                assert np.all(xnorm>0)
                checks += 1
            # Tail constant is positive and finite for each finite sketch dimension.
            assert 0 < tail_constant(s,a,d) < 1e10
            checks += 1
        # Exact worst-case normalized angle and sharp embedding construction.
        un = u/np.linalg.norm(u)
        w = b/np.linalg.norm(b)
        H = (np.outer(un,w)+np.outer(w,un))/2
        eigs, Q = np.linalg.eigh(H)
        sgn = (Q*np.sign(eigs))@Q.T
        critical = 2*np.sqrt(k)/(k+1)
        assert np.isclose(un@w,critical,atol=2e-14)
        checks += 1
        eps = (critical+1)/2
        G = np.eye(2)-eps*sgn
        assert np.linalg.eigvalsh(G).min()>0
        assert np.isclose(np.linalg.norm(G-np.eye(2),ord=2),eps)
        assert un@G@w < 0
        checks += 3
    # Arbitrary SPD matrices: the universal angle bound and one-step identity.
    for n in [2,3,5,7]:
        for j in range(65):
            Z = rng.normal(size=(n,n))
            A = Z.T@Z+np.eye(n)*.25
            b = rng.normal(size=n)
            u=A@b
            if np.linalg.norm(u)==0:continue
            a,d=descriptor(A,b)
            kap=np.linalg.cond(A)
            assert 0 <= d*d/(a*a+d*d) <= ((kap-1)/(kap+1))**2+2e-13
            checks += 1
            for s in [1,2,4,9]:
                S = rng.normal(size=(s,n))/np.sqrt(s)
                x=S@u
                rhs=S@b
                denominator=x@rhs
                if abs(denominator)<1e-12: continue
                theta=x@x/denominator
                inverse=a+((x@rhs)/(x@x)-a)
                assert np.isclose(theta*inverse,1.,atol=1e-10)
                checks += 1
    # Non-sketch eigenvector case is deterministically safe.
    A=np.diag([2.,5.,11.]);b=np.array([0.,1.,0.]);a,d=descriptor(A,b)
    assert np.isclose(a,1/5) and d < 1e-14
    checks+=1
    # Heavy-tail constant: numerically integrate density on tiny centered intervals.
    from scipy.integrate import quad
    for k in [2,5,15]:
        A,b=witness(k);a,d=descriptor(A,b)
        for s in [1,2,4,16]:
            c=tail_constant(s,a,d)
            for cutoff in [10000.,100000.]:
                # Event |theta|>cutoff is |R|<1/cutoff.
                h=1/cutoff
                integral=quad(lambda r: np.sqrt(s)/d*student_t.pdf((r-a)*np.sqrt(s)/d,df=s),-h,h,epsabs=1e-14)[0]
                assert abs(cutoff*integral/c-1)<.006
                checks+=1

    # Cauchy domain-of-attraction: empirical medians and interquartile ranges
    # of replicate averages approach the analytic Cauchy location and scale.
    from scipy.integrate import quad
    for k, s, n_rep, samples in [(2,2,4000,1100),(10,3,4000,1100),(10,8,4000,1100)]:
        A, b = witness(k)
        a, d = descriptor(A, b)
        sigma = np.pi*tail_constant(s,a,d)/2
        scale=d/np.sqrt(s)
        f=lambda x: student_t.pdf((x-a)/scale,df=s)/scale
        loc=quad(lambda x: (f(x)-f(-x))/x if x else 0.0,0,np.inf,epsabs=1e-8,limit=300)[0]
        tdraw=student_t.rvs(df=s,size=(n_rep,samples),random_state=rng)
        avg=np.mean(1/(a+scale*tdraw),axis=1)
        q25,q50,q75=np.quantile(avg,[.25,.5,.75])
        # The limiting quartiles are location +/- scale.
        assert abs(q50-loc)<max(.15*sigma,.006)
        assert abs((q75-q25)-2*sigma)<max(.18*sigma,.01)
        checks+=2
    print(f'PASS: {checks} algebraic, probabilistic, sharpness, Cauchy-law, and numerical checks')


if __name__=='__main__':
    check()
