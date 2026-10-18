#!/usr/bin/env python3
"""Independent finite checks for nested spin-flip stability counts and their disorder covariance."""
from fractions import Fraction
from itertools import product, permutations
from math import factorial
from random import Random


def energy(spins, weights):
    return -sum(weights[j]*spins[j]*spins[(j+1)%len(spins)] for j in range(len(spins)))


def number_of_stable_spins(weights, order):
    n=len(weights)
    count=0
    for state in product((-1,1),repeat=n):
        e=energy(state,weights)
        stable=True
        for i in range(n):
            for length in range(1,order+1):
                flip=list(state)
                for j in range(length):
                    flip[(i+j)%n]*=-1
                if energy(flip,weights)<=e:
                    stable=False
                    break
            if not stable:
                break
        if stable: count+=1
    return count


def number_of_weak_bonds(weights,order):
    n=len(weights)
    return sum(all(weights[i]<weights[(i+d)%n] for d in range(-order,order+1) if d) for i in range(n))


def exact_joint_probability(r,s,d):
    site_list=sorted(set(range(-r,r+1))|set(range(d-s,d+s+1)))
    place={j:i for i,j in enumerate(site_list)}
    good=0
    for rank in permutations(range(len(site_list))):
        if (all(rank[place[0]]<rank[place[k]] for k in range(-r,r+1) if k)
          and all(rank[place[d]]<rank[place[k]] for k in range(d-s,d+s+1) if k!=d)):
            good+=1
    return Fraction(good,factorial(len(site_list)))


def per_site_cov(r,s):
    a=Fraction(1,2*r+1); b=Fraction(1,2*s+1)
    out=Fraction(0)
    for d in range(r+s+1):
        p=exact_joint_probability(r,s,d)
        out+=(1 if d==0 else 2)*(p-a*b)
    return out


def full_cov_at_length(n):
    e1=e2=e11=e22=e12=0
    for w in permutations(range(1,n+1)):
        a=number_of_weak_bonds(w,1); b=number_of_weak_bonds(w,2)
        e1+=a;e2+=b;e11+=a*a;e22+=b*b;e12+=a*b
    fac=factorial(n)
    a=Fraction(e1,fac);b=Fraction(e2,fac)
    return (Fraction(e11,fac)-a*a,Fraction(e22,fac)-b*b,Fraction(e12,fac)-a*b)


def main():
    rng=Random(20261014)
    trials=0
    for n in range(5,11):
        for _ in range(12):
            w=list(range(1,n+1))
            rng.shuffle(w)
            for k in (1,2):
                expected=2**number_of_weak_bonds(w,k)
                actual=number_of_stable_spins(w,k)
                assert actual==expected,(n,w,k,actual,expected)
                trials+=1
    values={
        (1,2,2):Fraction(1,18),
        (1,2,3):Fraction(8,105),
        (2,2,3):Fraction(1,20),
        (2,2,4):Fraction(2,45),
    }
    for key,p in values.items():assert exact_joint_probability(*key)==p,key
    exact=(per_site_cov(1,1),per_site_cov(2,2),per_site_cov(1,2))
    assert exact==(Fraction(2,45),Fraction(13,450),Fraction(-1,315)),exact
    computed=full_cov_at_length(9)
    assert computed==tuple(9*x for x in exact),(computed,exact)
    print(f'PASS: {trials} direct Hamiltonian enumeration comparisons')
    print('PASS: four critical finite-window order probabilities')
    print('PASS: 3 exact covariance constants')
    print('PASS: complete 9! cyclic-order disorder covariance enumeration')
    print('covariance per bond:',tuple(str(x) for x in exact))

if __name__=='__main__':main()
