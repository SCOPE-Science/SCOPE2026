"""Finite arithmetic checks for exact single-field Gibbs sign-transition formulas.
Run: python3 verify_reversal.py. Requires only the Python standard library.
These numerical checks corroborate, but do not establish, the all-size theorem.
"""
import math
import random
import itertools


def cov_spin_ij(n, energies, h, i=0, j=1, k=2):
    # energies maps spin configuration tuple to unnormalized log-weight with h_k=0.
    z = 0.0
    m_i = m_j = m_ij = 0.0
    for s, base in energies.items():
        w = math.exp(base + h*s[k]); z += w
        m_i += w*s[i]; m_j += w*s[j]; m_ij += w*s[i]*s[j]
    return m_ij/z - m_i*m_j/z**2


def three_spin_potential(a,b,c,d,h1,h2):
    return {(x,y,t):a*x*y+b*x*t+c*y*t+d*x*y*t+h1*x+h2*y for x,y,t in itertools.product((-1,1),repeat=3)}


def three_spin_quadratic(a,b,c,d):
    e = math.exp
    return (e(4*a+2*d)-e(-2*d),2*(e(4*a)*math.cosh(2*(b+c))-math.cosh(2*(b-c))),e(4*a-2*d)-e(2*d))


def conditioned_tables(n, energies, i=0,j=1,k=2):
    out={-1:{(x,y):0.0 for x in (-1,1) for y in (-1,1)},1:{(x,y):0.0 for x in (-1,1) for y in (-1,1)}}
    for s,b in energies.items():out[s[k]][(s[i],s[j])]+=math.exp(b)
    return out


def q_from_tables(tab,z):
    w={xy:z*tab[1][xy]+tab[-1][xy] for xy in [(1,1),(-1,-1),(1,-1),(-1,1)]}
    return w[(1,1)]*w[(-1,-1)]-w[(1,-1)]*w[(-1,1)]


def sign(x,eps=1.e-11):
    if x>eps:return 1
    if x < -eps:return -1
    return 0


def main():
    rng = random.Random(20261024)
    checks = 0
    for _ in range(320):
        a,b,c,d=[rng.uniform(-1.1,1.1) for _ in range(4)]
        h1,h2=[rng.uniform(-2.5,2.5) for _ in range(2)]
        E=three_spin_potential(a,b,c,d,h1,h2)
        tab=conditioned_tables(3,E)
        aa,bb,cc=three_spin_quadratic(a,b,c,d)
        for h in [-2.,-0.6,0.,0.7,1.9]:
            cv=cov_spin_ij(3,E,h)
            z=math.exp(2*h)
            q=aa*z*z+bb*z+cc
            assert sign(cv)==sign(q,1.e-9), (a,b,c,d,h,cv,q)
            assert sign(cv)==sign(q_from_tables(tab,z),1.e-9)
            checks+=2
    # arbitrary higher-order spin interactions for N=4,5,6
    for n in (4,5,6):
        for _ in range(65):
            E={s:rng.uniform(-1.4,1.4) for s in itertools.product((-1,1),repeat=n)}
            tab=conditioned_tables(n,E)
            for h in (-3.,-1.1,-0.1,0.6,2.1):
                cv=cov_spin_ij(n,E,h)
                q=q_from_tables(tab,math.exp(2*h))
                assert sign(cv)==sign(q,1.e-9),(n,h,cv,q)
                checks+=1
    # two reversals with positive conditional pair interactions
    a=math.log(2)/4;b=math.log(2);c=-math.log(2);d=0.
    aa,bb,cc=three_spin_quadratic(a,b,c,d)
    assert abs(aa-1)<1.e-12 and abs(bb+193/16)<1.e-12 and abs(cc-1)<1.e-12
    z_plus=(193+15*math.sqrt(161))/32
    z_minus=(193-15*math.sqrt(161))/32
    assert abs(z_plus*z_minus-1)<1.e-12
    critical=math.log(z_plus)/2
    E=three_spin_potential(a,b,c,d,0.4,-0.9)
    assert cov_spin_ij(3,E,-critical-0.3)>0
    assert cov_spin_ij(3,E,0)<0
    assert cov_spin_ij(3,E,critical+0.3)>0
    for h in (-critical,critical):assert abs(cov_spin_ij(3,E,h)) < 1e-12
    checks+=8
    # unique reversal when the three-body coefficient dominates direct coupling
    for d in (-1.0,1.0):
        E=three_spin_potential(.1,.5,-.7,d,1.0,-1.1)
        c1=cov_spin_ij(3,E,-10);c2=cov_spin_ij(3,E,10)
        assert c1*c2<0
        checks+=1
    # zero all-field pair association: a=d=0 and b=0 (arbitrary c).
    E=three_spin_potential(0,0,-1.3,0,1.1,-.8)
    for h in (-4,0,4):assert abs(cov_spin_ij(3,E,h))<1.e-12;checks+=1
    print('PASS',checks,'finite arithmetic assertions')

if __name__=='__main__':main()
