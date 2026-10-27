"""Independent exact checks for low-support binary three-deck reconstruction."""
from itertools import combinations, product
from math import comb
from collections import defaultdict


def deck3(word):
    one=[0,0]; two=[0]*4; three=[0]*8
    for ch in word:
        b=int(ch)
        for a in range(4):
            three[2*a+b]+=two[a]
        for a in range(2):
            two[2*a+b]+=one[a]
        one[b]+=1
    return tuple(three)


def encode_from_zero_prefixes(z,m):
    previous=0
    out=[]
    for value in z:
        assert previous <= value <= m
        out.append('0'*(value-previous)+'1')
        previous=value
    out.append('0'*(m-previous))
    return ''.join(out)


def mul(a,b):
    x,y=a;u,v=b
    return x*u-5*y*v,x*v+y*u


def powers(k):
    for j in range(k+1):
        p=(1,0)
        for _ in range(j):p=mul(p,(1,1))
        for _ in range(k-j):p=mul(p,(1,-1))
        yield p


def constructed(k):
    q=6**k
    B=4*q
    m=5*B
    for x,y in powers(k):
        assert x*x+5*y*y==q
        assert (x-y)%2==0
        v=((x-y)//2,(3*y-x)//2,(-x-3*y)//2,(x+y)//2)
        assert sum(v)==0 and sum((i+1)*v[i] for i in range(4))==0
        assert sum(t*t for t in v)==q
        z=tuple((i+1)*B+v[i] for i in range(4))
        assert 0<=z[0]<z[1]<z[2]<z[3]<=m
        yield z,m



def moment_formula(z,m):
    r=len(z)
    s0=sum(z)
    s1=sum((i+1)*value for i,value in enumerate(z))
    s2=sum(value*value for value in z)
    return (comb(m,3),(s2-s0)//2,m*s0-s2,
            r*s0-s1,
            (r*m*(m-1)-2*m*s0+s2+s0)//2,
            2*s1-(r+1)*s0,comb(r,2)*m-s1+s0,comb(r,3))


def naive_deck3(w):
    result=[0]*8
    for i in range(len(w)):
        for j in range(i+1,len(w)):
            for k in range(j+1,len(w)):
                result[4*int(w[i])+2*int(w[j])+int(w[k])]+=1
    return tuple(result)

def main():
    count=0
    for n in range(3,13):
        for r in range(0,min(4,n)+1):
            for ones in combinations(range(n),r):
                arr=['0']*n
                for j in ones:arr[j]='1'
                w=''.join(arr)
                z=tuple(i-j for j,i in enumerate(ones))
                observed=deck3(w)
                assert observed==moment_formula(z,n-r), (n,r,w,observed,moment_formula(z,n-r))
                if n<=9:assert observed==naive_deck3(w)
                count+=1
    print('independent moment formula verified for',count,'words with at most four ones through length twelve')
    for k in range(1,6):
        pairs=list(constructed(k))
        assert len(set(z for z,m in pairs))==k+1
        decks={deck3(encode_from_zero_prefixes(z,m)) for z,m in pairs}
        assert len(decks)==1
        print('construction k=',k,'length=',len(encode_from_zero_prefixes(*pairs[0])), 'distinct=',len(pairs),'deck-identical=True')
    for n in range(3,15):
        for r in range(0,min(3,n)+1):
            fiber=defaultdict(int)
            for ones in combinations(range(n),r):
                arr=['0']*n
                for j in ones:arr[j]='1'
                fiber[deck3(arr)]+=1
            maximum=max(fiber.values())
            assert maximum <= (2 if r==3 else 1), (n,r,maximum)
        print('exhaustive small-support length=',n,'passed')

if __name__=='__main__':main()
