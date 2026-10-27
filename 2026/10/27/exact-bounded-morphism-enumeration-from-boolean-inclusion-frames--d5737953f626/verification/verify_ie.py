from itertools import combinations

def ideals(n):
    a=[0,1]
    for j in range(n):
        m=1<<(j)
        a=[x|(y<<m) for x in a for y in a if x&y==y]
    return a

def count(n):
    ideals_n=ideals(n);N=1<<n;full=(1<<N)-1
    ans=0
    for I in ideals_n:
        if I==0 or I==full: continue
        zeros=[a for a in range(N) if I>>a&1]
        maxima=[a for a in zeros if not any((a != (a|(1<<j))) and (I>>(a|(1<<j))&1) for j in range(n))]
        for choices in range(1<<len(maxima)):
            U=0
            for z,a in enumerate(maxima):
                if choices>>z&1:
                    for j in range(n):
                        b=a|(1<<j)
                        if b==a:continue
                        U |= sum(1<<x for x in range(N) if b&x==b)
            Q=full & ~(I|U)
            d=0
            vals=[a for a in range(N) if Q>>a&1]
            for bits in range(1<<len(vals)):
                S=sum(1<<v for z,v in enumerate(vals) if bits>>z&1)
                if all(not (S>>a&1) or all(not(Q>>b&1) or (S>>b&1) for b in range(N) if (b&a)==b) for a in vals):
                    d+=1
            ans+= (-1 if choices.bit_count()%2 else 1)*d
        ans-=1
    return ans
if __name__=='__main__':
    for n in range(1,4):print('n',n,'IE',count(n))
