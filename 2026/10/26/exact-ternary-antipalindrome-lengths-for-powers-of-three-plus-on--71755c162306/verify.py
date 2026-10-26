#!/usr/bin/env python3
"""Exact independent finite check of ternary antipalindrome-summand theorem."""
def antipalindromes(maxlen):
    out=[]
    for length in range(1,maxlen+1):
        half=(length+1)//2
        for t in range(3**half):
            z=t; hi=[]
            for _ in range(half):
                hi.append(z%3); z//=3
            if not hi[0] or (length%2 and hi[-1]!=1):
                continue
            digits=hi+[2-hi[length-1-j] for j in range(half,length)]
            value=0
            for d in digits:
                value=3*value+d
            out.append(value)
    return sorted(set(out))

def isanti(z):
    if z<=0:return False
    a=[]
    while z:
        a.append(z%3);z//=3
    return all(a[j]+a[-1-j]==2 for j in range(len(a)))

def main():
    for n in range(1,15):
        target=3**n+1
        a=antipalindromes(n+1)
        aset=set(a)
        pairs=[(x,target-x) for x in a if x<=target-x and target-x in aset]
        wanted=[]
        if n==2:wanted=[(4,6)]
        if n>=6 and n%2==0:
            b=3**(n-3)+1+2*sum(3**(2*j) for j in range(1,n//2-1))
            wanted=[(b,target-b)]
        assert pairs==wanted, (n,pairs,wanted)
        if n==1:
            assert isanti(target)
        else:
            assert not isanti(target)
        if n>=3:
            u=(5*3**(n-2)-3)//2
            v=3**n-u
            assert u+v+1==target and all(isanti(x) for x in (1,u,v)), n
        print('n=%d: pairs=%d, triple=%s' %(n,len(pairs),n>=3))
    print('VERIFIED')

if __name__=='__main__':main()
