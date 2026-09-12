# Certified Lovasz theta defect for the hash-pinned Exoo Ramsey(4,6;35) core G35

## Context

The classical Ramsey number R(4,6) is known to exceed 35: Geoffrey Exoo found 37 edge-colorings of K_35 with no K_4 in the first color and no K_6 in the second color (Electronic Journal of Combinatorics 19(1):P66, 2012), raising the lower bound from 35 to 36. Brendan McKay hosts these as the graph6 file `r46_35some.g6` (37 graphs, explicitly an incomplete sample). The admitted target asks, for the hash-pinned first-listed graph G35 of that file, whether the Lovasz theta number satisfies theta(G35) < 6 with an exact rational SDP-dual certificate, or theta(G35) >= 6 with an exact primal witness.

## Definitions

Let G be a graph on n vertices. The Lovasz theta number in primal form is theta(G) = max{ <J,B> : tr B = 1, B_{ij} = 0 for every edge ij of G, B positive semidefinite }, where J is the all-ones matrix and <J,B> = sum_{i,j} B_{ij}. Any feasible B gives the lower bound theta(G) >= <J,B> by weak duality. The sandwich theorem states alpha(G) <= theta(G). A Ramsey(4,6;35) graph has n = 35, clique number omega <= 3, and independence number alpha <= 5.

## Object

G35 is the first line of McKay's `r46_35some.g6`: graph6 string `b@QWoq@_`KHKQcHQFVeGwiSrCbNV_?ZTGMTWDT{ol[LCS]uPj@kGVFqgiYXaaXWXM[oIQQPDQycEoesbPpTMikPC]wDWWW~@SRKw_` (truncated display; full string in artifacts), sha256 `0627d6bc4d82fd75292ec17b2483aa255c056438de5723f34e6e674f6dfbb484`, n = 35, 248 edges, degrees 12..15. Exact branch-and-bound verification gives omega(G35) = 3 (witness triangle [0,5,15]) and alpha(G35) = 5 (witness independent set [0,1,2,6,7]); exhaustive search confirms K4-freeness and no independent set of size 6. Hence G35 is a genuine Ramsey(4,6;35) graph and theta(G35) >= 5.

## Result

For the hash-pinned G35, theta(G35) >= 754549/100000 = 7.54549 >= 6, witnessed by an exact rational primal-feasible matrix B. Consequently the theta(G35) < 6 alternative is false and the certified theta-defect branch of the target holds. Any SDP-dual-feasible M must have largest eigenvalue at least 7.54549. Numerics (primal ADMM ~7.68, dual eigenvalue optimization ~7.78) suggest the true theta lies around 7.6-7.8, well above 6; the Hoffman eigenvalue bound 9.34 is too weak to decide.

## Proof / evidence

The file `output/artifacts/theta_defect_certificate.json` contains B_entries (35x35 exact rational matrix as per-entry strings), L_entries and pivots (exact LDL factorization B = L D L^T). Verification over the rationals confirms: (1) B is symmetric; (2) trace is exactly 1; (3) B_{ij} = 0 on all 248 edge positions; (4) LDL reconstruction holds entrywise over Q with all 35 pivots strictly positive (minimum pivot ~8.5e-4), proving B is positive definite over Q; (5) <J,B> = 754549/100000 = 7.54549 >= 6. Weak duality lifts this to theta(G35) >= 7.54549 > 6. An independent audit script re-verified all 1225 entries from the two JSON files alone and passed. Construction: decode graph6, exact clique/independence branch-and-bound, scaled ADMM float SDP, then exactization (zero edge entries, trace renormalization, 0.98/0.02 mixing with I/35, rounding to multiples of 1/200000, exact diagonal trace fix, exact Fraction LDL). Float phases are heuristics only; the final claim rests solely on exact rational arithmetic.

## Limitations

The certificate proves the lower bound theta(G35) >= 7.54549, not the exact value of theta(G35). The float SDP phases used pure-Python Jacobi eigensolvers with no external SDP library. Graph identity rests on fetching McKay's public file and pinning its first line by sha256; a re-download reproduces it. No claim is made about the other 36 graphs in the file or about R(4,6) itself.

## Reproducibility

Inputs `G35_adj.json` (adjacency matrix + graph6) and `theta_defect_certificate.json` (B, L, pivots, objective) plus the audit script suffice: check sha256, symmetry, trace, edge zeros, LDL identity B = LDL^T over Q, pivot positivity, and the objective sum. All checks use exact rational arithmetic (Python Fractions) and run in seconds.

## References

- G. Exoo, On the Ramsey number R(4,6), Electron. J. Combin. 19(1) (2012), P66. doi:10.37236/2102.
- B. McKay, Ramsey Graphs combinatorial data, https://users.cecs.anu.edu.au/~bdm/data/ramsey.html (file r46_35some.g6).
- L. Lovasz, On the Shannon capacity of a graph, IEEE Trans. Inform. Theory 25 (1979), 1-7 (theta function and sandwich theorem).
