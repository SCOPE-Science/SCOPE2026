# Independent mathematical audit

## correctness

PASS

For binary F2^3 complementary subspaces F1=<e1>,F2=<e2,e3> with uniformly sampled labeled generator columns (with replacement), G4=(e1,e1,e2,e3) has E1=2 and E2=6 by geometric and two-coupon waiting times. For any rank-3 length-5 matrix H, m=#columns exactly e1 is at most 3. If m=0, no one-draw recovery and identical first-two draws with probability 1/5 give E1>=11/5>2. If m=1, among four other columns at most four unordered complementary-type pairs sum e1, yielding E1>=1+4/5+8/25=53/25>2. If m=2, unique complementary pair gives E1=25/12; no pair with three-body sum gives 9/4; or else E1=5/2: all >2. If m=3, other u,v must be linearly independent with e1, so E1=5/3, and recovering two-dimensional F2 forces both unique u and v coupon positions, giving E2>=5(1+1/2)=15/2. Equality at (e1,e1,e1,e2,e3). Independent complete exhaustive implementation enumerated 476 full-rank F2^3 multisets of length five including zero columns, and exact absorbing-subspace DP confirmed only 12 with E1<=2, each E1=5/3 and min E2=15/2. Hence no five-column matrix Pareto dominates (2,6); finite enumeration is exhaustive for this exact problem, not a claim for all field sizes or n.

## originality

PASS

Best-of-knowledge PASS: direct counterexample to Conjecture 2 (one-step weak Pareto inclusion when a file has dimension at least two) of Bar-Lev 2026, in fixed field F2 and file sizes (1,2). The same paper already exhibits nonmonotonicity when both files have dimension one; that prior example does not imply the dimension-three mixed-file obstruction because additional mixed columns could dominate. The hyperbolic conjecture dim1/E1+dim2/E2<=1 is distinct and not contradicted, likewise Resultary one-mixed-column hyperbolic bound. Primary Bar-Lev revised 2026 preprint Conjecture 2 and Remark 10 were read in full.

## value

PASS

A concrete sharp obstruction refutes a natural explicit length monotonicity conjecture and identifies the exact Pareto barrier at the smallest mixed-dimension binary layout. The proof closes all rank-three five-column codes rather than merely presenting a near miss. A small finite theorem is valuable because it overturns a universal conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
