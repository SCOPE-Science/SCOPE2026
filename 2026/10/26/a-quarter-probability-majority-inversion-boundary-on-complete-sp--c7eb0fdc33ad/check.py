"""Exact independent checks for one-round local-majority voting on a complete split graph."""
from math import comb
from fractions import Fraction
from itertools import product

def predicted(c,l):
    n=c+l
    if n%2!=1 or c<2 or l<1:
        raise ValueError('requires c>=2, l>=1 and odd n')
    if l<c: return Fraction(0,1)
    s=sum(comb(c,x)*sum(comb(l,y) for y in range(max(0,n//2+1-x),l+1))
          for x in range((c-2)//2+1))
    return Fraction(2*s,2**n)

def direct_one(bits,c,l):
    n=c+l
    out=[]
    for i in range(n):
        neighbors=range(n) if i<c else [*range(c),i]
        positives=sum(bits[j] for j in neighbors)
        if 2*positives>len(neighbors): out.append(1)
        elif 2*positives<len(neighbors): out.append(0)
        else: out.append(bits[i])
    return int(sum(out)>n//2)

if __name__=='__main__':
    count=0
    for c in range(2,8):
        for l in range(1,10):
            n=c+l
            if n%2==0 or n>16: continue
            disag=0
            for bits in product((0,1),repeat=n):
                before=int(sum(bits)>n//2)
                after=direct_one(bits,c,l)
                disag+=(before!=after)
            want=predicted(c,l)*2**n
            assert disag==want,(c,l,disag,want)
            count+=2**n
            print(f'c={c}, l={l}, inversion={disag}/{2**n}', flush=True)
    print(f'PASS: {count} exact initial profiles, formula agrees with direct vertex-by-vertex voting')
    for c in [2,4,6,10,20,40,80,160]:
        print('boundary',c,str(predicted(c,c-1)),str(predicted(c,c+1)),float(predicted(c,c+1)))
