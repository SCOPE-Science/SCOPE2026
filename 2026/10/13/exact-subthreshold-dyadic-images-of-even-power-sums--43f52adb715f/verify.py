#!/usr/bin/env python3
"""Finite consistency checks for subthreshold dyadic modular Waring images.
The source of validity for arbitrary parameters is the accompanying proof.
"""

def parameters(k):
    assert k>=6 and k%2==0
    s=0
    z=k
    while z%2==0:
        z//=2
        s+=1
    return s,s+2,1<<(s+2)

def predicted(k,t,a):
    s,h,q=parameters(k)
    assert 1<=t<q and a>=1
    M=1<<a
    if a<=h:
        return {i%M for i in range(t+1)}
    outer={r for r in range(M) if 1<=r%q<=t}
    if a<=k:
        inner={0}
    else:
        inner={(1<<k)*r for r in predicted(k,t,a-k)}
    assert not (outer&inner)
    return outer|inner

def actual(k,t,a):
    M=1<<a
    pows={pow(x,k,M) for x in range(M)}
    states={0}
    for _ in range(t):
        states={(x+y)%M for x in states for y in pows}
    return states

def main():
    cases=0
    plan={6:([1,2,3,7],12),8:([1,2,3,7,15,31],12),10:([1,2,5,7],12),12:([1,3,7,15],12),14:([1,2,7],11),16:([1,5,16,31,63],12),20:([1,2,3,15],11),24:([1,3,15,31],11),32:([1,3,31,63,127],11)}
    for k,(ts,amax) in plan.items():
        s,h,q=parameters(k)
        for t in ts:
            for a in range(1,amax+1):
                got=actual(k,t,a)
                expected=predicted(k,t,a)
                assert got==expected,(k,t,a,len(got),len(expected),sorted(got^expected)[:10])
                if a<=h:
                    cardinal=min(1<<a,t+1)
                elif a<=k:
                    cardinal=t*(1<<(a-h))+1
                else:
                    cardinal=t*(1<<(a-h))+len(predicted(k,t,a-k))
                assert len(got)==cardinal,(k,t,a,len(got),cardinal)
                cases+=1
    print('VERIFY_OK')
    print('exponents=6,8,10,12,14,16,20,24,32')
    print('exact_image_and_cardinality_checks='+str(cases))
    print('moduli_powers=2^1_to_2^12')
    print('method=brute_force_power_residues_and_iterated_sumsets')
    print('limitation=finite_consistency_checks_not_an_infinite_proof')

if __name__=='__main__':
    main()
