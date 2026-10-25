"""Exact finite checks for excursion-size likelihood-ratio ordering and bridge occupation variance."""
from math import comb
from fractions import Fraction
from itertools import combinations


def cat(j):
    return comb(2*j,j)//(j+1)


def Z(n,k):
    if k==0: return 1 if n==0 else 0
    if n<k or n<0: return 0
    return k*comb(2*n-k,n-k)//(2*n-k)


def q(n,k,l):
    if not (1<=k<=n and 1<=l<=n-k+1):return Fraction(0)
    return Fraction(k*l*cat(l-1)*Z(n-l,k-1),n*Z(n,k))


def independent_occupation(n):
    total={};length_mass={};A_mass={}
    for positive in combinations(range(2*n),n):
        posset=set(positive)
        s=0;last=0;k=0;A=0;lengths=[]
        for j in range(2*n):
            s+=1 if j in posset else -1
            if s==0:
                length=(j+1-last)//2
                sign=1 if last in posset else -1
                lengths.append(length)
                if sign==1:A+=length
                last=j+1;k+=1
        assert s==0 and sum(lengths)==n
        total[k]=total.get(k,0)+1
        A_mass[k,A]=A_mass.get((k,A),0)+1
        for l in lengths:
            length_mass[k,l]=length_mass.get((k,l),0)+l
    return total,length_mass,A_mass


def test():
    assertions=0
    for n in range(1,10):
        tot,lmass,amass=independent_occupation(n)
        assert sum(tot.values())==comb(2*n,n); assertions+=1
        for k in range(1,n+1):
            assert tot[k]==(2**k)*Z(n,k);assertions+=1
            assert sum(lmass.get((k,l),0) for l in range(1,n+1))==n*tot[k]; assertions+=1
            assert sum(q(n,k,l) for l in range(1,n+1))==1;assertions+=1
            for l in range(1,n+1):
                assert Fraction(lmass.get((k,l),0),n*tot[k])==q(n,k,l);assertions+=1
            assert Fraction(sum(a*amass.get((k,a),0) for a in range(n+1)),tot[k])==Fraction(n,2);assertions+=1
            var=Fraction(sum((2*a-n)**2 *amass.get((k,a),0) for a in range(n+1)),4*tot[k])
            formula=Fraction(n,4)*sum(l*q(n,k,l) for l in range(1,n+1))
            assert var==formula;assertions+=1
    for n in range(2,51):
        for k in range(1,n):
            prev=[q(n,k,l) for l in range(1,n+1)]
            nex=[q(n,k+1,l) for l in range(1,n+1)]
            assert sum(prev)==sum(nex)==1;assertions+=1
            assert sum(l*nex[l-1] for l in range(1,n+1))<sum(l*prev[l-1] for l in range(1,n+1));assertions+=1
            for l in range(1,n):
                assert nex[l]*prev[l-1]<=nex[l-1]*prev[l];assertions+=1
    print('PASS assertions',assertions)
    for n in (4,8,12):
        print('n',n,'Var(A|K=k) initial',Fraction(n,4)*sum(l*q(n,1,l) for l in range(1,n+1)), 'terminal',Fraction(n,4)*sum(l*q(n,n,l) for l in range(1,n+1)))

if __name__=='__main__':test()
