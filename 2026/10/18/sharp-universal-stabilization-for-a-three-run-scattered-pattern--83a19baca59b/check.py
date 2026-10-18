from math import comb
from itertools import product
from collections import defaultdict

def calc_poly(s,t,k):
    d=s+t-1
    terms=[]
    for A in range(s+t,s+t+k):
        weights=[comb(i,s)*comb(A-i,t) for i in range(s,A-t+1)]
        states={(0,0):1}
        for wt in weights:
            nex=defaultdict(int)
            for (freq,number),cnt in states.items():
                for j in range((k-freq)//wt+1):
                    nex[(freq+j*wt,number+j)]+=cnt
            states=nex
        for (freq,h),cnt in states.items():
            if freq==k: terms.append((A+h,cnt))
    return terms,d

def cbin(x,d):
    prod=1
    for i in range(d): prod*=x-i
    return prod//__import__('math').factorial(d)

def count_p(w,p):
    a=[1]+[0]*len(p)
    for x in w:
        for i in range(len(p)-1,-1,-1):
            if x==p[i]: a[i+1]+=a[i]
    return a[-1]

def do():
    counts=0
    sharp=0
    for s in range(1,4):
      for t in range(1,4):
       for k in range(1,7):
        terms,d=calc_poly(s,t,k)
        assert terms
        assert max(b for b,_ in terms)==s+t+k
        for n in range(0,13):
            direct=sum(count_p(w,'0'*s+'1'+'0'*t)==k for w in map(''.join,product('01',repeat=n)))
            exact=sum(cnt*comb(n-base+d,d) for base,cnt in terms if n>=base)
            assert exact==direct,(s,t,k,n,direct,exact)
            if n>=k+1:
                polynomial=sum(cnt*cbin(n-base+d,d) for base,cnt in terms)
                assert polynomial==direct,(s,t,k,n,direct,polynomial)
            counts+=1
        at_k=sum(cnt*cbin(k-base+d,d) for base,cnt in terms)
        directk=sum(count_p(w,'0'*s+'1'+'0'*t)==k for w in map(''.join,product('01',repeat=k)))
        delta=at_k-directk
        expected=(-1)**d*sum(cnt for base,cnt in terms if base==s+t+k)
        assert delta==expected and delta!=0,(s,t,k,delta,expected)
        sharp+=1
    print('PASS, exact enumerations',counts,'sharp threshold assertions',sharp)
    for s,t,k in [(1,1,1),(1,1,3),(2,3,3),(3,2,5)]:
        terms,d=calc_poly(s,t,k)
        print((s,t,k),'degree',d,'terms',len(terms),'leading numerator',sum(c for _,c in terms),'sharp discrepancy',(-1)**d*sum(c for b,c in terms if b==s+t+k))
if __name__=='__main__':do()
