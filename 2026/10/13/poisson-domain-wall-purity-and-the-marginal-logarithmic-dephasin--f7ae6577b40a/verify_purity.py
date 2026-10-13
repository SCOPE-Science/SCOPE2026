"""Finite-matrix and one-wall checks for a power-law pair-dephasing channel.

Run with Python 3.9+ (standard library only). No data files are required.
"""
from itertools import product
from math import exp, fsum, isclose, log, sqrt


def rates(n, alpha, p):
    if alpha == float('inf'):
        return [0.0] + [p] + [0.0] * (n - 2)
    return [0.0] + [p * (n**(alpha-1) if alpha < 1 else 1) / r**alpha
                    for r in range(1, n)]


def domain_walls(word):
    return sum(word[i] != word[i+1] for i in range(len(word)-1))


def mps_probability(n, g):
    # Direct multiplication of the exact 2x2 source MPS tensors and boundary vectors.
    # The explicit matrices are checked against the domain-wall Born law.
    assert g > 0
    m0=((0.,0.),(1.,1.))
    m1=((1.,g),(0.,0.))
    L=(1/sqrt(g),1.)
    R=(sqrt(g),1.)
    amplitudes=[]
    for x in product((0,1),repeat=n):
        v=L
        for bit in x:
            m=m1 if bit else m0
            v=(v[0]*m[0][0]+v[1]*m[1][0],
               v[0]*m[0][1]+v[1]*m[1][1])
        amplitudes.append(v[0]*R[0]+v[1]*R[1])
    norm=sum(a*a for a in amplitudes)
    return [a*a/norm for a in amplitudes]


def direct_channel_purity(n, g, alpha, p):
    words=list(product((0,1),repeat=n))
    q=[g**domain_walls(x)/(2*(1+g)**(n-1)) for x in words]
    amps=[sqrt(v) for v in q]
    rho=[[a*b for b in amps] for a in amps]
    d=len(words)
    for i in range(n):
        for j in range(i+1,n):
            rate=rates(n,alpha,p)[j-i]
            for x in range(d):
                s=words[x][i]^words[x][j]
                for y in range(d):
                    if s != (words[y][i]^words[y][j]):
                        rho[x][y]*=1-2*rate
    return fsum(v*v for row in rho for v in row)


def exact_wall_formula(n,g,alpha,p):
    # Marginal law of U=X xor Y: U_1 fair, independent bond flips with
    # probability 2g/(1+g)^2. No density matrix is used here.
    h=2*g/(1+g)**2
    probs=rates(n,alpha,p)
    total=0.
    for u in product((0,1),repeat=n):
        k=domain_walls(u)
        val=(h**k)*((1-h)**(n-1-k))/2
        for r in range(1,n):
            crossing=sum(u[i]!=u[i+r] for i in range(n-r))
            val*=abs(1-2*probs[r])**(2*crossing)
        total+=val
    return total


def one_step_crossings(n,k,r):
    # A domain wall lies between sites k and k+1, 1 <= k < n.
    return max(0,min(k,n-r)-max(1,k-r+1)+1)


def single_wall_weight(n,k,alpha,p):
    terms=[]
    for r,prob in enumerate(rates(n,alpha,p)[1:],1):
        crossings=one_step_crossings(n,k,r)
        if not crossings:continue
        x=abs(1-2*prob)
        if x==0:return 0.
        terms.append(2*crossings*log(x))
    return exp(fsum(terms))


def wall_factor_infinite(alpha,p,cutoff):
    if alpha<=2:return 0.
    terms=[]
    for r in range(1,cutoff+1):
        x=abs(1-2*p/r**alpha)
        if x==0:return 0.
        terms.append(2*r*log(x))
    return exp(fsum(terms))


def main():
    checks=0
    for n in range(2,7):
        for g in (.08,.37,1.):
            q=mps_probability(n,g)
            for x,v in zip(product((0,1),repeat=n),q):
                formula=g**domain_walls(x)/(2*(1+g)**(n-1))
                assert abs(v-formula)<1e-12,(n,g,x,v,formula)
                checks+=1
    for n in range(2,7):
        for g in (0.,.17,.7):
            for alpha in (0.,.6,1.5,2.,3.,float('inf')):
                for p in (.15,.5,.85):
                    lhs=direct_channel_purity(n,g,alpha,p)
                    rhs=exact_wall_formula(n,g,alpha,p)
                    assert abs(lhs-rhs)<2e-12,(n,g,alpha,p,lhs,rhs)
                    checks+=1
                    h=2*g/(1+g)**2
                    if alpha==float('inf'):
                        expected=(1-4*p*(1-p)*h)**(n-1)
                        assert abs(lhs-expected)<2e-12
                        checks+=1
                    if p==.5 and alpha>1:
                        expected=(1-h)**(n-1)
                        assert abs(lhs-expected)<2e-12
                        checks+=1
    for alpha in (2.5,3.,4.):
        for p in (.2,.8):
            q=wall_factor_infinite(alpha,p,100000)
            errors=[abs(single_wall_weight(n,n//2,alpha,p)-q)
                    for n in (100,1000,10000)]
            assert errors[-1]<errors[0],(alpha,p,errors)
            checks+=3
    for c in (.3,1.1):
        q=exp(-4*c)
        errors=[abs(single_wall_weight(n,n//2,2.,c/log(n))-q)
                for n in (100,1000,10000)]
        assert errors[-1]<errors[0],(c,errors)
        checks+=3
    # Exact one-wall crossing multiplicities, independent site-pair enumeration.
    for n in range(2,25):
        for k in range(1,n):
            u=(0,)*k+(1,)*(n-k)
            for r in range(1,n):
                direct=sum(u[i]!=u[i+r] for i in range(n-r))
                assert direct==one_step_crossings(n,k,r)
                checks+=1
    print('VERIFY_OK',checks,'MPS amplitudes, quantum-channel matrices, Markov-wall sums, and boundary products')

if __name__=='__main__':main()
