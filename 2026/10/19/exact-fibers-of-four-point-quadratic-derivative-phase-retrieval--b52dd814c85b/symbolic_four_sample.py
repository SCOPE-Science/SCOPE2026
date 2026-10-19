#!/usr/bin/env python3
"""Symbolic verification of the four-point Fourier measurement identity."""
import sympy as sp
A,B,C,Ab,Bb,Cb=sp.symbols('A B C Ab Bb Cb')
points=[1,sp.I,-1,-sp.I]
F=[];D=[]
for z in points:
 p=A+B*z+C*z*z
 pc=Ab+Bb/z+Cb/z**2
 d=B+2*C*z
 dc=Bb+2*Cb/z
 F.append(sp.expand(p*pc));D.append(sp.expand(d*dc))
y=[sp.expand(sum(F[j]*points[j]**(-k) for j in range(4))/4) for k in range(3)]
w=[sp.expand(sum(D[j]*points[j]**(-k) for j in range(4))/4) for k in range(2)]
expecty=[A*Ab+B*Bb+C*Cb,B*Ab+C*Bb,C*Ab+A*Cb]
expectw=[B*Bb+4*C*Cb,2*C*Bb]
for a,b in zip(y+w,expecty+expectw):assert sp.expand(a-b)==0
print('PASS: all five independent Fourier-intensity invariants are exact polynomial identities.')
