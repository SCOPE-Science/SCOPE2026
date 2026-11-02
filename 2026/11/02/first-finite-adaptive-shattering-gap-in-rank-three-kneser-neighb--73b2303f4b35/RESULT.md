# First finite adaptive-shattering gap in rank-three Kneser neighborhoods

## Finding
For every integer \(3\le n\le11\), let \(\operatorname{KG}(n,3)\) have the three-element subsets of \([n]\) as vertices, with edges joining disjoint triples. Let \(\mathcal N_n=\{N(Y):Y\in\binom{[n]}3\}\) be its open-neighborhood concept family, queried by membership of a triple. The exact ordinary (deterministic, realizable) Littlestone dimensions are
\[
\left(\operatorname{Ldim}(\mathcal N_n)\right)_{n=3}^{11}=(0,0,0,1,2,3,4,5,6).
\]
In particular, \(\operatorname{Ldim}(\mathcal N_{10})=5\) and \(\operatorname{Ldim}(\mathcal N_{11})=6\). A previously established finite static shattering classification gives corresponding VC dimensions \(4\) and \(5\), respectively, so the adaptive dimension exceeds the static dimension in both cases; ten is the first order exhibiting such a gap within this fixed-rank family. The previously established VC classification is not a new theorem here.

## Assumptions and scope
Every vertex and query is exactly a three-element subset. A positive answer means disjointness (not intersection, closed neighborhoods or Johnson adjacency). Repeated queries are allowed but do not increase the dimension. A depth-\(d\) shattered tree is a full binary query tree of depth \(d\) such that every answer sequence is realized by at least one hypothesis. All statements here are finite, for \(3\le n\le11\). No dimension assertion for \(n\ge12\) is made.

## Proof
Write \(E_n=\binom{[n]}3\). Enumerate its elements lexicographically as \(e_0,\ldots,e_{m-1}\), where \(m=\binom n3\). For every query \(q\in E_n\), define its exact positive mask \(Q_q=\{i:e_i\cap q=\varnothing\}\). A version space is an arbitrary nonempty subset \(S\subseteq\{0,\ldots,m-1\}\). Define the Boolean recurrence
\[
F(S,0)=[S\ne\varnothing],\qquad
F(S,d)=\bigvee_{q\in E_n}\bigl(F(S\cap Q_q,d-1)\wedge F(S\setminus Q_q,d-1)\bigr)
\quad(d\ge1).
\]
This recurrence is equivalent to the definition of a complete depth-\(d\) shattered binary tree: the root queries some \(q\), and its two children must shatter depth \(d-1\) on their actual remaining version spaces. Both directions follow by induction on \(d\). In particular a no-instance of \(F(E_n,d+1)\) is an exhaustive upper-bound proof, provided that every root query and every recursively possible version space is examined. The supplementary code enumerates **all** \(\binom n3\) root queries at every reached state; memoization identifies only exactly equal pairs \((S,d)\). It discards branches if \(|S|<2^d\), which is a rigorous necessary condition because distinct binary leaves require distinct witnesses. It also discards queries if either side has fewer than \(2^{d-1}\) hypotheses. These are mathematically necessary prunings and do not omit a successful tree.

For each \(n=3,\ldots,11\), the standard-library verifier evaluates both \(F(E_n,d_n)\) and \(F(E_n,d_n+1)\) with \(d_n=\max(0,n-5)\). Every former value is true and every latter false. For each positive case it extracts a full explicit query tree into `trees.json`, containing a distinct concrete hypothesis at every leaf. The independent tree checker walks all answer paths and checks every query answer directly by triple disjointness. Thus the lower bound is separately certified by concrete witnesses, and the upper bound by exhaustive recurrence. The special small orders have \(n<6\), hence no two disjoint triples: every hypothesis has the same all-zero behavior, so dimension zero also follows immediately. For the higher orders the exact calculation proves the asserted values, not a heuristic pattern or infinite extrapolation.

The claimed first adaptive/static gap is a comparison with an already-established static result (the VC sequence for \(n=3,\ldots,11\) is \((0,0,0,1,2,3,4,4,5)\)); it is not inferred from the adaptive calculations alone.

## Verification
Run `python3 verify.py` beside `trees.json` using Python 3 standard library. The program recomputes the exact dimension bounds from the definition and compares every newly constructed witness tree with the independently stored certificate. Every leaf verifies its whole answer path. `output.txt` records the complete nine-order pass; the central cases are 120 hypotheses and dimension five at \(n=10\), 165 hypotheses and dimension six at \(n=11\). There are 31 and 63 internal queries and 32 and 64 leaf witnesses in their respective complete trees. Exact enumeration proves only the stated finite cases.

## Relationship to prior work
Adler, Benediktsson and Macpherson [1] prove static VC-dimension bounds for open neighborhoods in Johnson and Hamming graphs, not the adaptive dimensions of Kneser disjointness graphs. Disjointness of fixed-cardinality sets is also a well-established subject in combinatorial communication complexity [2]; its communication lower bounds do not determine these exact mistake-tree ranks. A separate earlier static classification of rank-three Kneser neighborhoods gives the VC comparison above, and an earlier online classification of **rank-two** Kneser neighborhoods gives \(\operatorname{Ldim}(\operatorname{KG}(n,2))=\min\{4,n-3\}\). Neither implies the finite rank-three adaptive recurrence outcomes. No authorship or publication priority is claimed for those earlier results.

## Limitations
The theorem has a finite, reproducible exact-exhaustion proof, not a closed all-order formula. Runtime and memory usage can depend strongly on implementation but do not change the finite enumeration's mathematical completeness. The VC comparison is contextual prior mathematical work, not independently re-proved here. The search of accessible literature and research records does not rule out an unindexed equivalent prior calculation, particularly under online set-disjointness or thicket terminology. No independent external scientific audit has occurred.

## References
1. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1, publicly posted July 31, 2020, https://arxiv.org/abs/2007.16042.
2. A. Bhattacharya et al., *Disjointness through the Lens of VC Dimension: Sparsity and Beyond*, arXiv:2006.13712v1, publicly posted June 24, 2020, https://arxiv.org/abs/2006.13712.
