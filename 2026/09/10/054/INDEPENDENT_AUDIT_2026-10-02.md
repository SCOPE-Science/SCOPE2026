# Independent mathematical audit

## correctness

PASS

I independently reran all 6,084 fundamental quadratic twists with squarefree absolute parameter at most 5,000 in installed PARI/GP 2.15.4, using E=ellinit([0,-1,1,-10,-20]), D=quaddisc(±d) and R=ellrank(elltwist(E,D)). PARI's documented 2-Selmer upper bound is R[2]+R[3] here, because base/twist 2-torsion is zero. The rerun returned total 6084, sum of Selmer sizes 12136, maximum upper bound 3, and histogram [2106,3011,932,35,0,0], exactly the frozen CSV. A second full sweep independently collected the nine twists with certified rank lower bound three: -206,-1007,1393,1766,-1799,2362,2878,-4399,4582; root-number parity disagreements were zero. Thus no rank-four twist appears in this finite range, conditional on the trusted PARI descent implementation; the result does not assert an infinite no-rank-four theorem.

## originality

PASS

General results on average Selmer sizes and rank distribution do not supply this exact finite 11a1 quadratic-twist table. Resultary's exact match was the audited SCOPE record. No inspected primary source or database supplies the 6084-row T=5000 census, histogram or nine rank-three certificates; best-of-knowledge residual database risk is stated.

## value

PASS

The canonical conductor-11 curve's quadratic twist family is a natural arithmetic testbed; an exhaustive bounded 2-Selmer/rank dataset with full denominator, histogram and nine rank-three certificates is a useful reproducibility benchmark. The result is explicitly finite and does not overstate average-distribution or infinite-rank implications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
