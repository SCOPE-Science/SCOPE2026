from collections import Counter,defaultdict
from itertools import permutations,product
from math import factorial,comb

def all_words(A,B,r):
    symbols=['a']*A+['b']*B+['c'+str(i) for i in range(r)]
    # multiset permutations using recursion
    cnt=Counter(symbols)
    def rec(prefix,remain):
        if not remain:
            yield tuple(prefix);return
        for k in tuple(cnt):
            if cnt[k]:
                cnt[k]-=1;prefix.append(k)
                yield from rec(prefix,remain-1)
                prefix.pop();cnt[k]+=1
    yield from rec([],len(symbols))

def deck(w,alphabet):
    ix={v:i for i,v in enumerate(alphabet)}
    out=[0]*(len(alphabet)**2)
    for i in range(len(w)):
      for j in range(i+1,len(w)):
        out[ix[w[i]]*len(alphabet)+ix[w[j]]]+=1
    return tuple(out)

def formula(A,B,r):
    return factorial(r)*comb(A+r,r)*comb(B+r,r)*(r+1+A*B)//(r+1)

def gauss(a,b):
    poly=Counter()
    for w in all_words(a,b,0):
        x=sum(w[i]=='a' and w[j]=='b' for i in range(len(w)) for j in range(i+1,len(w)))
        poly[x]+=1
    return dict(poly)

def convolution(p,q):
    z=Counter()
    for i,ci in p.items():
        for j,cj in q.items():z[i+j]+=ci*cj
    return dict(z)

def compositions(n,k):
    if k==1:yield (n,);return
    for i in range(n+1):
        for rest in compositions(n-i,k-1):yield (i,)+rest

def expected_fibers(A,B,r):
    out=[]
    for ap in compositions(A,r+1):
        for bp in compositions(B,r+1):
            p={0:1}
            for a,b in zip(ap,bp):p=convolution(p,gauss(a,b))
            out.extend(p.values())
    return sorted(out*r_factorial(r))

def r_factorial(r):return factorial(r)

if __name__=='__main__':
    c=0
    g=0
    for r in range(4):
      for A in range(1,4):
       for B in range(1,4):
        if (A+B+r)>9:continue
        alphabet=['a','b']+['c'+str(i) for i in range(r)]
        hist=Counter(deck(w,alphabet) for w in all_words(A,B,r))
        exact=formula(A,B,r)
        assert len(hist)==exact,('deck count mismatch',r,A,B,len(hist),exact)
        expect=expected_fibers(A,B,r)
        assert sorted(hist.values())==expect,('fiber mismatch',r,A,B)
        c+=1;g+=sum(hist.values())
    print('PASS: checked',c,'exact-class and complete-multiplicity cases; total examined words',g)
    print('examples: (A,B,r)=(2,2,1) ->',formula(2,2,1),'distinct decks; (3,3,2) ->',formula(3,3,2))
