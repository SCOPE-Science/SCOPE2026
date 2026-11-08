# Independent mathematical audit

## correctness

PASS

A zero multiplier followed by a zero multiplier makes the state exactly (0,0) forever; the first waiting pair occurs a.s. and first-step conditioning gives mean waiting time (1+r)/r^2. For integer k>=1 the binomial expansion closes k+1 nonnegative mixed moments into B_k(M,w), with strong-connectedness and an aperiodic loop giving primitivity for M,w>0; Perron–Frobenius gives an asymptotic positive multiple of rho(B_k)^t. The Perron root is strictly increasing in M, vanishes at M=0 and is <1 at M=1 by geometric absorption, so unique M_k>1. Determinants yield M1=1/w and M2=(sqrt(1+8/w)-1)/2. Lyapunov moment comparison gives M_{k+1}<=M_k; an all-retained run has growth root R_M>1 for each M>1 and forces M_k->1. Fresh independent numeric threshold checks at w=1/2 and orders 1..6 give approx 2,1.56155,1.38513,1.28735,1.22701,1.18691; finite checks not infinite proof.

## originality

PASS

Random-coefficient AR moment spectral criteria are longstanding; the k=2 criterion is already in general small-gain theory. The exact threshold sequence for every integer order and critical positive limit together with almost-sure finite-time extinction is not stated in inspected accessible older work. Feigin–Tweedie 1985 remains a real material priority risk because full text could not be read: authorized institutional attempt returned VPN disconnected. The absence alone is not automatic FAIL, and we do not present generalized moment-matrix machinery as new.

## value

PASS

One natural model can terminate exactly after finite time on every sample path while high moments diverge; the theorem determines exactly which multipliers do this at all orders, with computable matrices of size k+1 and thresholds decreasing to the sharp barrier 1. The distinction between pathwise reliability and moment risk is mathematically nontrivial and potentially useful in stochastic feedback, without claiming a general random-control law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
