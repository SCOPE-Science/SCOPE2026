# Independent mathematical audit

## correctness

PASS

For exactly specified 2-stage 2-step scheme with scalar frozen decay x in [0,4], stages give companion A(t) with t=T2(1-x/2)=1-2x+x^2/2, A(t)=[[3(1+t)/5,-t/5],[1,0]]. P=[[1,-1/3],[-1/3,1/5]] has determinant 4/45>0. Direct matrix algebra gives A(-1)^T P A(-1)=P/5 and P-A(1)^T P A(1)=(4/25)[[1,-1],[-1,1]], and convexity of squared P norm in A(t) gives the uniform factor 1-x(4-x)/5. Endpoint spectral radius squared 1/5 forces coefficient <=1/5; equality and A(1) fixed vector (1,1) force Q proportional to P. Quadratic Jury conditions make frozen strict Schur interval (-2,1), while D22=(5-t^2)/25 and det D=32(1-t)(t+2)/1125 show SAME P nonexpansive for -2<=t<=1. Summed x(4-x)=infinity implies energy->0. Smooth-order-two Taylor expansion does not assert discontinuous-rate convergence order or noncommuting operator stability.

## originality

PASS

Qualified best-of-knowledge PASS: Moisa–Faleichik formulate these stabilized two-step methods and frozen scalar stability, but the inspected source does not give this sharp, unique common switching quadratic. Different variable-step BDF estimates are not implications.

## value

PASS

A single sharp and unique explicit quadratic Lyapunov certificate guarantees arbitrary switching stability, which scalar frozen root-stability alone cannot guarantee. The full Schur interval and exact energy loss sharpen a natural low-stage stabilized integrator instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
