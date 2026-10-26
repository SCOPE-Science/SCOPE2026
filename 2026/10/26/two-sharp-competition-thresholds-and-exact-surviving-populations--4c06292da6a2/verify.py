"""Exact finite-domain checks for a competitive biomass sign-update map on cycles.

No external Python packages are required. This checks bounded cases only;
the accompanying mathematical argument covers every permitted cycle size.
"""
from fractions import Fraction
from itertools import product


def step(state, alpha):
    n = len(state)
    ans = []
    for i, z in enumerate(state):
        if not z:
            ans.append(0)
            continue
        bracket = 2 - z - alpha * (state[(i-1)%n]+state[(i+1)%n]) / 2
        ans.append(z + (1 if bracket > 0 else -1 if bracket < 0 else 0))
    return tuple(ans)


def run(n, alpha, bits):
    init = tuple(1+x for x in bits)
    x = tuple(bits)
    dim = tuple(x[i] and x[(i+1)%n] and not x[(i-1)%n] and not x[(i+2)%n] for i in range(n))
    dimer_sites = {i for i, a in enumerate(dim) if a} | {(i+1)%n for i,a in enumerate(dim) if a}
    # This set records the initial two-site runs, not simply adjacent survivors.
    predicted_t2=[]
    predicted_t3=[]
    for i in range(n):
        neigh = x[(i-1)%n]+x[(i+1)%n]
        if alpha < 2:
            t2 = 2 if x[i] and neigh < 2 else 0
        elif alpha == 2:
            t2 = (2-neigh) if x[i] else 0
        else:
            t2 = 2 if x[i] and neigh == 0 else 0
        t3 = (1 if i in dimer_sites else 2) if x[i] and neigh<2 and alpha<=2 else t2
        predicted_t2.append(t2)
        predicted_t3.append(t3)
    t1=step(init,alpha)
    t2=step(t1,alpha)
    t3=step(t2,alpha)
    t4=step(t3,alpha)
    t5=step(t4,alpha)
    assert t1 == tuple(x), (n,alpha,bits,'t1')
    assert t2 == tuple(predicted_t2), (n,alpha,bits,'t2',t2,predicted_t2)
    assert t3 == tuple(predicted_t3), (n,alpha,bits,'t3',t3,predicted_t3)
    assert t4 == (t2 if alpha < 2 else t3), (n,alpha,bits,'t4')
    assert t5 == (t3 if alpha < 2 else t3), (n,alpha,bits,'t5')
    return len([z for z in t3 if z>0]), len(dimer_sites), sum(t3), sum(t2), int(t2!=t3)


def main():
    checked=0
    alpha_cases=(Fraction(5,4),Fraction(3,2),Fraction(7,4),Fraction(2,1),Fraction(9,4),Fraction(5,2),Fraction(4,1))
    for n in range(4,11):
        for alpha in alpha_cases:
            occup=osc=biomass=biomass2=cycles=0
            for x in product((0,1), repeat=n):
                a,b,c,d,e=run(n,alpha,x)
                occup+=a;osc+=b;biomass+=c;biomass2+=d;cycles+=e
                checked+=1
            total=2**n
            assert Fraction(occup,n*total)==(Fraction(3,8) if alpha<=2 else Fraction(1,8))
            if alpha<=2:
                assert Fraction(osc,n*total)==Fraction(1,8)
            if alpha<2:
                assert Fraction(biomass,n*total)==Fraction(5,8)
                assert Fraction(biomass2,n*total)==Fraction(3,4)
            elif alpha==2:
                assert Fraction(biomass,n*total)==Fraction(5,8)
                assert Fraction(biomass2,n*total)==Fraction(1,2)
            else:
                assert Fraction(biomass,n*total)==Fraction(1,4)
                assert cycles==0
    print('PASS',checked,'exact initial-state/parameter classifications on cycles of sizes 4..10.')
    print('Including finite-size survival and dimer densities, biomass means, temporal periods.')

if __name__=='__main__':
    main()
