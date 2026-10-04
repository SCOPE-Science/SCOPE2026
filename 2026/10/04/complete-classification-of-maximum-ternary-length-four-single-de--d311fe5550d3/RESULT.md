# Complete classification of maximum ternary length-four single-deletion codes
## Finding
Let \(Q=\{0,1,2\}\). For \(w\in Q^4\), let \(D_1(w)\) denote the set of distinct length-three words obtained by deleting one coordinate. A one-deletion-correcting code is a set \(C\subseteq Q^4\) such that \(D_1(u)\cap D_1(v)=\varnothing\) for all distinct \(u,v\in C\).

The maximum size is \(11\), and exactly six labeled maximum codes exist. Define
\[
K=\{aaaa:a\in Q\}\cup\{aabb:a,b\in Q,\ a\ne b\}
\]
and
\[
R=\{abca:\{a,b,c\}=Q\}.
\]
The set \(K\) has nine words. The deletion-compatibility graph on the six words of \(R\) is a six-cycle, and every maximum code is \(K\) together with one edge of that cycle. The six allowed unordered pairs are
\[
\{0120,1021\},\ \{0120,2102\},\ \{0210,1201\},\ \{0210,2012\},\ \{1021,2012\},\ \{1201,2102\}.
\]
Hence there are exactly six labeled maximum codes. Under global permutations of the three alphabet symbols together with optional reversal of coordinate order, all six lie in one orbit of size \(6\); the stabilizer has order \(2\).

## Assumptions and scope
The alphabet symbols are labeled \(0,1,2\), coordinate order is significant, and deletion removes exactly one coordinate while preserving the relative order of the remaining symbols. The labeled count treats two subsets of \(Q^4\) as distinct unless they are literally equal. The equivalence statement uses only channel symmetries that preserve the ordered deletion operation: a single global alphabet permutation and optional reversal.

This is a finite classification for ternary words of length four. It does not claim an analogous classification for other alphabet sizes or word lengths. Each maximum code found here has deletion-shadow union of size \(23\), so these maximum codes are not perfect deletion codes in the sense of covering all \(27\) length-three received words.

## Proof
Associate to every word \(w\in Q^4\) its deletion shadow \(D_1(w)\), represented exactly as a bit mask on the \(27\) ternary length-three words. Form the compatibility graph on the \(81\) words of \(Q^4\), joining two words precisely when their deletion shadows are disjoint. One-deletion-correcting codes are exactly cliques in this graph.

The embedded verifier uses a direct ordered recursion for a prescribed clique size. At each step it chooses the least remaining candidate, recurses only on later candidates compatible with that word, and prunes only when fewer candidates remain than the number still needed. Thus each target-size subset is considered exactly once and every prune is a cardinality impossibility, not a heuristic. Exhaustive search finds no clique of size \(12\) and exactly six cliques of size \(11\). Since an explicit size-
\(11\) clique exists and any larger clique would contain a size-
\(12\) clique, the maximum is exactly \(11\).

Taking the intersection of the six enumerated maxima gives exactly \(K\). Their two-word remainders lie in \(R\). Direct comparison of the six deletion masks in \(R\) gives exactly the six compatible pairs displayed above; every vertex has degree two, so this compatibility graph is a six-cycle. Finally, the verifier applies all \(6\) global alphabet permutations and both coordinate orientations. The orbit of one maximum code is exactly the complete six-code list, and exactly two of the \(12\) group elements stabilize the representative.

## Verification
Run `python3 artifacts/verify.py` beside `artifacts/max_codes.json`. The verifier reconstructs the \(81\) words and all deletion shadows from definitions, independently enumerates target-size cliques, checks the six-code data file, checks the six-cycle description, and traverses the full symmetry group. The recorded replay is:

`VERIFY_OK maximum=11 labeled_maxima=6 orbits=1 orbit_size=6 stabilizer=2 nodes11=668442 nodes12=485745`

The target-
\(11\) recursion makes \(668442\) calls and returns six solutions; the target-
\(12\) recursion makes \(485745\) calls and returns none. These counts are reproducibility diagnostics; correctness rests on the exhaustive recursion and direct shadow checks implemented in the supplied source, not on the numbers alone.

## Relationship to prior work
Kim, Lee, and Oh study length-four single-deletion codes and explicitly note that their sharp even-alphabet bound is not sharp for odd alphabet size; their construction theory therefore does not settle the ternary extremal classification. Kulkarni and Kiyavash formulate deletion coding as a hypergraph matching problem. Their numerical table gives, for ternary length four, a fractional-matching upper bound of \(12\) and a best listed Tenengolts construction of size \(8\), rather than an exact extremal classification.

Wang and Ji prove existence of perfect \(T^*(3,4,v)\) codes for all alphabet sizes. That statement is not an implication of the present classification: a perfect code covers every length-three received word exactly once, whereas each maximum code classified here covers exactly \(23\) of the \(27\) possible received words. A 2011 thesis on ternary one-deletion codes was also checked through indexed material; it discusses perfect-code background and constructive search methods, but a complete machine-readable copy was not available for inspection, so an unindexed prior enumeration remains a residual literature risk.

## Limitations
The proof is finite and computer-assisted. It classifies only \(Q^4\) for \(Q=\{0,1,2\}\). No claim is made about a closed formula or extremal structure for general odd alphabet size. Literature searches cannot prove absence from all unpublished or poorly indexed sources; the principal residual originality risk is an inaccessible or unindexed small-parameter enumeration, especially in older ternary-code work.

## References
1. H. K. Kim, J. Y. Lee, D. Y. Oh, “Optimal codes in deletion and insertion metric,” arXiv:0810.3729, first submitted 2008-10-21; replaced by arXiv:1003.4057.
2. H. K. Kim, J. Y. Lee, D. Y. Oh, “Construction of optimal codes in deletion and insertion metric,” arXiv:1003.4057.
3. A. A. Kulkarni, N. Kiyavash, “Non-asymptotic Upper Bounds for Deletion Correcting Codes,” arXiv:1211.3128.
4. J. Wang, L. Ji, “Existence of \(T^*(3,4,v)\)-codes,” Journal of Combinatorial Designs 13 (2005), 42–53, DOI:10.1002/jcd.20031.
5. Z. Li, “Construction of 1-Deletion-Correcting Ternary Codes,” M.Sc. thesis, Brock University, 2011.
