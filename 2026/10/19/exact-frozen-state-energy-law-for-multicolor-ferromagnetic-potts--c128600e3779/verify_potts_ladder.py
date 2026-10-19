#!/usr/bin/env python3
"""Finite independent checks for the Potts ladder frozen-state theorem."""
from itertools import product

def predicted(q,n):
    # Polynomial in wall fugacity via integer coefficients, b=-(q-1)u or b=u.
    # P_n(b) recurrence P_n=P_{n-1}-bP_{n-2}.
    def powsign(coeff):
        x=[2]; y=[1]
        if n==0: return x
        if n==1: return y
        for j in range(2,n+1):
            z=[0]*((j//2)+1)
            for k,v in enumerate(y): z[k]+=v
            for k,v in enumerate(x): z[k+1]-=coeff*v
            x,y=y,z
        return y
    x=powsign(-(q-1)); y=powsign(1)
    t=[a+(q-1)*b for a,b in zip(x+[0]*(max(len(x),len(y))-len(x)),y+[0]*(max(len(x),len(y))-len(y)))]
    t[0]+=q*(q-1)
    return t

def brute(q,n):
    hist=[0]*(n+1)
    energy_hist=[0]*(3*n+1)
    count=0
    for configuration in product(range(q),repeat=2*n):
        # Index (row,rung) -> row*n+rung
        good=True
        for row in (0,1):
            for i in range(n):
                k=row*n+i
                neighbours=(configuration[row*n+(i-1)%n],configuration[row*n+(i+1)%n],configuration[(1-row)*n+i])
                original=sum(x==configuration[k] for x in neighbours)
                # Independently calculate every energy difference from actual local Hamiltonian.
                for color in range(q):
                    if color!=configuration[k] and original<=sum(x==color for x in neighbours):
                        good=False;break
                if not good: break
            if not good: break
        if good:
            count+=1
            walls=sum(configuration[i]!=configuration[(i+1)%n] for i in range(n))
            assert walls==sum(configuration[n+i]!=configuration[n+(i+1)%n] for i in range(n)), 'Unexpected mixed-rung stable state'
            hist[walls]+=1
            same_rung=all(configuration[i]==configuration[n+i] for i in range(n))
            if not same_rung:
                # A second direct check of the geometric classification.
                assert len(set(configuration[:n]))==1
                assert len(set(configuration[n:]))==1
                assert configuration[0]!=configuration[n]
            else:
                assert all(configuration[i]==configuration[(i-1)%n] or
                           configuration[i]==configuration[(i+1)%n] for i in range(n))
            # Independent energy count from actual distinct undirected edges.
            disagree=sum(configuration[i]!=configuration[n+i] for i in range(n))
            disagree+=sum(configuration[i]!=configuration[(i+1)%n] for i in range(n))
            disagree+=sum(configuration[n+i]!=configuration[n+(i+1)%n] for i in range(n))
            energy_hist[disagree]+=1
    return hist, energy_hist, count

def main():
    cases=[(q,n) for q in (2,3,4) for n in range(3,6)] + [(3,6),(5,3),(5,4)]
    tests=0;configs=0
    for q,n in cases:
        expected=predicted(q,n)
        observed,energy_observed,total=brute(q,n)
        energy_expected=[0]*(3*n+1)
        for k,value in enumerate(expected):
            if k==0:
                energy_expected[0]+=value-q*(q-1)
                energy_expected[n]+=q*(q-1)
            else: energy_expected[2*k]+=value
        assert energy_observed==energy_expected,(q,n,energy_observed,energy_expected)
        assert observed[:len(expected)]==expected,(q,n,observed,expected)
        assert all(x==0 for x in observed[len(expected):]),(q,n,observed)
        assert total==sum(expected)
        configs+=q**(2*n)
        tests+=1
        print(f'q={q} n={n}: frozen={total} histogram={observed}')
    # Test exact matrix trace via independent direct transition construction.
    for q in range(2,7):
        states=list(product(range(q),repeat=2))
        lookup={s:i for i,s in enumerate(states)}
        T=[[0]*len(states) for _ in states]
        for i,(a,b) in enumerate(states):
            for c in range(q):
                if a!=b and b!=c: continue
                T[i][lookup[(b,c)]]=1
        powers=[[int(i==j) for j in range(len(states))] for i in range(len(states))]
        for n in range(1,9):
            powers=[[sum(powers[i][k]*T[k][j] for k in range(len(states))) for j in range(len(states))] for i in range(len(states))]
            trace=sum(powers[i][i] for i in range(len(states)))
            assert trace==sum(predicted(q,n))-q*(q-1),(q,n,trace)
            tests+=1
    print('VERIFY_OK: cases',tests,'independently scanned configurations',configs)
if __name__=='__main__': main()
