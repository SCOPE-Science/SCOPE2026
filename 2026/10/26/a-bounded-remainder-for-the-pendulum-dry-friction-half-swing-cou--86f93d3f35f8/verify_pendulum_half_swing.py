#!/usr/bin/env python3
"""Numerical sanity check only; the asymptotic proof is analytic."""
import math

def simpson(f, a, b, n=200000):
    h=(b-a)/n
    total=f(a)+f(b)
    for i in range(1,n):
        total+=(4 if i%2 else 2)*f(a+i*h)
    return total*h/3

def integrand(x):
    return 0.5 if x==0.0 else math.sin(x)/(2*x)

def next_state(x, eps):
    lo,hi=0.0,x
    for _ in range(70):
        z=(lo+hi)/2
        g=math.cos(z)-math.cos(x)-eps*(x+z)
        if g>0: lo=z
        else: hi=z
    return (lo+hi)/2

def count(eps):
    x=math.pi; k=0
    while x>=6*eps:
        x=next_state(x,eps); k+=1
    return k,x

def main():
    d=simpson(integrand,0.0,math.pi)
    print(f"D_approx={d:.12f}")
    print("epsilon,K,D/epsilon,K-D/epsilon,terminal_X/epsilon")
    for eps in (1e-2,5e-3,1e-3,5e-4):
        k,x=count(eps)
        print(f"{eps:.1e},{k},{d/eps:.8f},{k-d/eps:.8f},{x/eps:.8f}")

if __name__=="__main__":
    main()
