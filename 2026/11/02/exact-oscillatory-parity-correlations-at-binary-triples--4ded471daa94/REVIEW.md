# Independent mathematical audit

## correctness

PASS

For all integers r>=0, digitwise 3b_j+c_j=y_j+2c_(j+1) with c∈{0,1,2} and terminal digit parity tau(c_r) yields C_r=e M^r v, where M=[[1,1,0],[-1,0,-1],[0,1,1]], e=[1,0,0], v=[1,-1,-1]. Exact resolvent is (1-2z+3z²)/((1-z)(1-z+2z²)); eigenvalues 1,(1±i√7)/2 give C_r=1-(2/√7)Im(((1+i√7)/2)^r), correct for r=0,1,2. Marginal N-matrix yields U_r with classical 3^(r/2) scale, and the four joint parity cells (2^r+bU_r+abC_r)/4 for r>=1. Irrationality of eigenangle follows from 1/√2 not an algebraic integer, giving infinite positive/negative subsequences of 2^(r/2). Independent symbolic resolvent and direct bit-popcount enumeration through r=13 agreed. Infinite oscillation follows analytic density not finite sample.

## originality

PASS

Shallit and classical Newman/Coquet analyze marginal tau(3n) but not mixed tau(n)tau(3n). Baake–Coons study correlations with fixed additive offsets; 3n-n=2n is a varying offset. An accessible 2011 paper on rarefied weighted Thue–Morse studies weights derived from digits of 3n+j, not directly this exact dyadic mixed parity, though an implicit reduction remains a risk.

## value

PASS

The exact two-coordinate joint sign distribution resolves a natural multiplication-by-three digit-correlation question; its oscillating scale 2^(r/2), distinct from marginal 3^(r/2), is substantive structure beyond simply computing the first few automaton states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
