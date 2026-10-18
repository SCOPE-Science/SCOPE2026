# Independent mathematical audit

## correctness

PASS

Cr_n has closed neighborhoods of size n. Summing their >=k inequalities proves W>=2k. In equality all are tight, and paired labels obey x_i-y_i=c, (n-2)c=0, hence x_i=y_i=z_i with sum z_i=k. The given integer-count vector constructions include a value 3 (or a 2) to defend all relevant labels and attain W=2k unless n+k=5; exactly (3,2) and (4,1) fail the requisite rescue. A paired shore-difference parity analysis rules out W=2k+1 for those cases; vectors (-1,1,3) and (-1,-1,1,3) duplicated attain 2k+2. Exhaustively checked every f in {-1,1,2,3}^{2n} for n=3,4,5 and all 3n admissible k with an independent C++ implementation. No finite test is used for the all-n assertion.

## originality

PASS

Henning–Volkmann analyze the same k-domination invariant on complete bipartite K_{p,p}, obtaining 2k+2 for a range of p,k, but removing a perfect matching changes every vertex neighborhood and the exact value. No implication from the K_{p,p} theorem to the matching-deleted graph follows. Published crown-graph Roman domination entries use different labels/conditions.

## value

PASS

The full n,k phase classification gives the exact feasibility range and shows a striking near-universal attainment of the regular-graph double-counting lower bound, with only two sharp small exceptions. Crowns are a fundamental regular bipartite test family for domination parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
