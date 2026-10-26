from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import comb

def fano():
    return sorted({tuple(sorted(((a+i)%7 for a in (0,1,3)))) for i in range(7)})

def affine9():
    vec=[(x,y) for x in range(3) for y in range(3)]
    no={p:i for i,p in enumerate(vec)}
    return sorted({tuple(sorted(no[((x+j*dx)%3,(y+j*dy)%3)] for j in range(3)))
                   for x,y in vec for dx,dy in [(1,0),(0,1),(1,1),(1,2)]})

def bose15():
    blocks=[tuple(sorted((3*x,3*x+1,3*x+2))) for x in range(5)]
    for x,y in combinations(range(5),2):
        for i in range(3):
            blocks.append(tuple(sorted((3*x+i,3*y+i,3*((3*(x+y))%5)+(i+1)%3))))
    return sorted(blocks)

def pg15():
    return sorted({tuple(sorted((x-1,y-1,(x^y)-1))) for x,y in combinations(range(1,16),2)})

def validate(v, blocks):
    c=Counter(pair for block in blocks for pair in combinations(block,2))
    assert len(blocks)==v*(v-1)//6
    assert len(c)==comb(v,2) and set(c.values())=={1}

def histogram(v,blocks,k):
    ss=[set(x) for x in blocks]
    return Counter(sum(s.issubset(W) for s in ss) for W in map(set,combinations(range(v),k)))

def expected(v,k):
    b=v*(v-1)//6
    if k==3:
        n1=b
        return {0:comb(v,k)-n1,1:n1}
    if k==4:
        n1=b*(v-3)
        return {0:comb(v,k)-n1,1:n1}
    if k==5:
        n2=v*(v-1)*(v-3)//8
        n1=v*(v-1)*(v-3)*(v-7)//12
        return {0:comb(v,k)-n1-n2,1:n1,2:n2}

if __name__=='__main__':
    for name,v,fn in [('fano',7,fano),('affine',9,affine9),('Bose',15,bose15),('PG',15,pg15)]:
        B=fn(); validate(v,B)
        for k in [3,4,5]:
            got=histogram(v,B,k)
            exp=expected(v,k)
            assert all(got.get(i,0)==j for i,j in exp.items()),(name,k,got,exp)
            assert sum(got.values())==comb(v,k)
            # independently compute PAV scores and confirm induced-block criterion
            if k in [3,4,5]:
                for W in combinations(range(v),k):
                    s=sum([Fraction(0),Fraction(1),Fraction(3,2),Fraction(11,6)][len(set(W).intersection(T))] for T in B)
                    tau=sum(set(T).issubset(W) for T in B)
                    formula=Fraction(k*(v-1),2)-Fraction(comb(k,2),2)+Fraction(tau,3)
                    assert s==formula,(name,k,W,s,formula)
            print(name,v,k,sorted(got.items()))
        print('six-set spectrum',name,sorted(histogram(v,B,6).items()))
