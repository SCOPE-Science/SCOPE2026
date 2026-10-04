#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict, Counter
import math

def longest_zero(bits):
    L=cur=0
    for b in bits:
        if b:
            cur=0
        else:
            cur+=1
            if cur>L:
                L=cur
    return L

def run():
    bitstrings_checked=0
    covariance_checks=0
    influence_checks=0
    stochastic_order_checks=0
    bound_checks=0

    for n in range(1,17):
        total=1<<n
        sumS=sumL=sumSL=0
        byS=defaultdict(Counter)
        total_decrement=0

        for mask in range(total):
            bits=[(mask>>i)&1 for i in range(n)]
            S=sum(bits)
            L=longest_zero(bits)
            sumS+=S
            sumL+=L
            sumSL+=S*L
            byS[S][L]+=1

            dec=0
            for i,b in enumerate(bits):
                if b==0:
                    changed=bits.copy()
                    changed[i]=1
                    dec += L-longest_zero(changed)
            total_decrement+=dec
            bitstrings_checked+=1

        ES=Fraction(sumS,total)
        EL=Fraction(sumL,total)
        cov=Fraction(sumSL,total)-ES*EL
        via_influence=-Fraction(total_decrement,2*total)
        assert cov==via_influence
        assert cov<0
        covariance_checks+=1
        influence_checks+=1

        m=math.ceil(math.log2(n)) if n>1 else 0
        assert -cov <= Fraction(m*m+4*m+6,8)
        bound_checks+=1

        for s in range(n):
            a=byS[s]
            b=byS[s+1]
            na=sum(a.values())
            nb=sum(b.values())
            maxL=max(max(a),max(b))
            strict=False
            for t in range(maxL+1):
                ta=Fraction(sum(v for ell,v in a.items() if ell>=t),na)
                tb=Fraction(sum(v for ell,v in b.items() if ell>=t),nb)
                assert ta>=tb
                strict |= ta>tb
            assert strict
            stochastic_order_checks+=1

    print(
        "VERIFY_OK "
        f"bitstrings_checked={bitstrings_checked} "
        f"covariance_checks={covariance_checks} "
        f"influence_checks={influence_checks} "
        f"stochastic_order_checks={stochastic_order_checks} "
        f"bound_checks={bound_checks}"
    )

if __name__=="__main__":
    run()
