"""Independent exact checks of the finite two-sample rank-statistic identities.
Run: python3 verify.py. Uses only Python standard library.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def check(a,b):
    n=a+b; h=F(a*b,n*n)
    vals=[]
    for chosen in combinations(range(n),a):
        word=[int(i in chosen) for i in range(n)]
        runs=1+sum(word[i]!=word[i+1] for i in range(n-1))
        cumulative=0; t=F(0)
        for i in range(n-1):
            cumulative+=word[i]; s=F(cumulative)-F(a*(i+1),n)
            t+=s*s
        vals.append((runs,t))
    count=len(vals)
    assert count==comb(n,a)
    e=lambda fn:sum(map(fn,vals),F())/count
    er=e(lambda z:z[0]); et=e(lambda z:z[1])
    vr=e(lambda z:z[0]**2)-er**2
    vt=e(lambda z:z[1]**2)-et**2
    cov=e(lambda z:z[0]*z[1])-er*et
    assert er==1+2*n*h
    assert et==n*h*(n+1)/6
    assert vr==2*n*h*(2*n*h-1)/(n-1)
    assert vt==n*n*h*(n+1)*(4*(n+1)*h-3)/180
    assert cov==-n*h*(2*n*h-1)/3
    assert 6*cov==-(n-1)*vr
    if n>=3:
        assert cov<0
    return count,6

def main():
    cases=0; nwords=0; assertions=0
    for n in range(2,12):
        for a in range(1,n):
            ncases,na=check(a,n-a)
            cases+=1;nwords+=ncases;assertions+=na
    print('PASSED: %d fixed-composition cases; %d binary words; %d exact moment assertions' % (cases,nwords,assertions))
if __name__=='__main__':main()
