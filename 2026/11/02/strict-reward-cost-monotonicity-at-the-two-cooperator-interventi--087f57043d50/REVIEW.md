# Independent mathematical audit

## correctness

PASS

PASS. Re-derived the absorbing birth-death scale Green kernel for state 1, with the Fermi update and the self-loop factor h_j. Exact expected cost E=N^2 theta B(r) where r=R exp(-beta theta), R=exp(-beta delta)>1, T=sum_{k=0}^{N-3}R^k, and B=(1+r)(A(1+rT)+CT)/(1+r+Tr^2), A=1/(N-1), C=1/(N-2). Differentiation yields Bprime=(AT-2CT^2r-(A+C)T^2r^2)/D^2. If Bprime>0 it forces r<1/(2T), Bprime/B<1/(1+r), and r log(R/r)<1 (since T>=1+R>2), proving the derivative positive at every theta>=0; the boundary theta=0 follows directly. Independently solved absorbing rational chains for 85 (N,R,r) configurations N=4..8 with exact agreement. The fixation-ratio optimization is a corollary and does not cover other initial states.

## originality

PASS

PASS, qualified best-of-knowledge. The 2024 Duong–Durbac–Han article analyzes Fermi reward costs and proves an analytical t=1 case, while threshold-dependent higher cases were treated numerically. The exact all-N threshold-two positivity proof for initial single cooperator is not furnished by their stated theorems. Strict scope prevents extrapolation to initial-state mixtures or t>=3.

## value

PASS

PASS. Exact all-N monotonicity for the first unsolved two-cooperator threshold settles the choice of least-cost reward in a natural absorbing evolutionary-game model with institution costs. The threshold-1 case alone does not decide it, and the proof supplies a nontrivial Green-kernel derivative inequality rather than a numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
