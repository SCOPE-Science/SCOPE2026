# Optimality certificates for three length-six limited-permutation covers
## Finding
In the radius-one limited permutation channel on length-six words, let \(X_\lambda\) be a concrete multiset class of type \(\lambda\), and let \(\kappa(\lambda)\) be the minimum number of channel balls with centers in \(X_\lambda\) whose union covers \(X_\lambda\). Then
\[
\kappa((2,2,2))=9,\qquad \kappa((3,1,1,1))=15,\qquad \kappa((2,2,1,1))=17.
\]
These values hold for every concrete class of the indicated type, not only for the canonical labelings used in the certificates.

## Assumptions and scope
A radius-one channel action is any set of pairwise-disjoint adjacent transpositions. Equivalently, choose a matching \(S\) in the path on six coordinates and swap coordinates \(i\) and \(i+1\) for every \(i\in S\). There are exactly thirteen such matchings. The channel preserves symbol multiplicities, so each concrete multiset class is closed under every channel ball.

For a fixed type, the canonical classes used here are the permutations of \(001122\), \(000123\), and \(001123\), respectively. Any relabeling of alphabet symbols is a bijection that commutes with coordinate swaps, so the covering number depends only on the type.

## Proof
The upper bounds are given by explicit center sets in `certificates.json`. The verifier enumerates the full canonical class and all thirteen legal swap matchings, then checks that the displayed \(9\), \(15\), and \(17\) balls cover all \(90\), \(120\), and \(180\) words, respectively.

For the lower bounds, `certificates.json` also gives a nonnegative weight \(w(y)\) on words of each canonical class. For every possible center \(c\), the exact certificate satisfies
\[
\sum_{y\in B(c)}w(y)\le 1.
\]
If \(C\) is any ball cover, then
\[
|C|\ge \sum_{c\in C}\sum_{y\in B(c)}w(y)\ge \sum_{y\in X_\lambda}w(y).
\]
The three total weights are exactly \(9\), \(15\), and \(17\). Hence no smaller cover exists, and the explicit covers are optimal.

All weights are in \(\{0,1/2,1\}\). Thus the lower bounds are exact rational fractional-packing certificates and do not depend on numerical optimization.

## Verification
Run `python3 verify.py` in the directory containing `verify.py` and `certificates.json`. The script uses only the Python standard library. It independently regenerates each multiset class, enumerates all thirteen disjoint-adjacent-swap patterns, verifies every upper-cover inclusion, parses the rational dual weights with `fractions.Fraction`, checks every one of the \(90\), \(120\), and \(180\) possible center inequalities, and checks the exact total weight. A successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Ben Shimon and Lev Zabokritskiy introduced the relevant length-six finite covering refinement in arXiv:2607.19566v1. Their Table 3 gives replacement covers of sizes \(9\), \(15\), \(17\), \(32\), and \(60\) for five multiset types. The text immediately following the table explicitly states that no optimality of any replacement size is claimed. The present result closes that optimality gap for the three types \((2,2,2)\), \((3,1,1,1)\), and \((2,2,1,1)\).

The earlier work of Langberg, Schwartz, and Yaakobi develops the \(\ell_\infty\)-limited permutation channel and general coding bounds, including special attention to radius one, but does not determine these three concrete length-six multiset-class covering numbers.

## Limitations
No optimality claim is made here for the source paper's remaining length-six replacement sizes \(32\) for type \((2,1,1,1,1)\) or \(60\) for the all-distinct type. The result concerns covering numbers inside fixed concrete multiset classes; it does not by itself prove a globally optimal value of \(K_q(6;1)\) for any alphabet size.

## References
1. Noam Ben Shimon and Aryeh Lev Zabokritskiy, “Extinction Depth and q-ary Error-Correcting Codes for the Limited Permutation Channel,” arXiv:2607.19566v1, first posted 2026-07-21. Section 5.1 and Table 3.
2. Michael Langberg, Moshe Schwartz, and Eitan Yaakobi, “Coding for the \(\ell_\infty\)-Limited Permutation Channel,” IEEE Transactions on Information Theory 63(12), 2017, DOI:10.1109/TIT.2017.2762676.
