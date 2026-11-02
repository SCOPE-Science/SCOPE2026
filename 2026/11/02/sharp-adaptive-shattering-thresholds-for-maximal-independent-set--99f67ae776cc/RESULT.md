# Sharp adaptive-shattering thresholds for maximal independent sets of degree-two graphs

## Finding
Let \(G\) be a finite simple graph and let \(\mathcal M(G)\) consist of its inclusion-maximal independent vertex sets. Regard \(\mathcal M(G)\) as a Boolean concept class with vertex-membership queries. Write \(v(G)=\operatorname{VCdim}\mathcal M(G)\) and \(\ell(G)=\operatorname{Ldim}\mathcal M(G)\), where Littlestone dimension uses complete binary mistake trees.

**Theorem (sharp connected and componentwise thresholds).** Every finite graph of maximum degree at most two and order at most nine satisfies \(v(G)=\ell(G)\). On exactly ten vertices, the **only** graph of maximum degree at most two, up to isomorphism, with \(v(G)<\ell(G)\) is the ten-vertex path \(P_{10}\), for which
\[
(v(P_{10}),\ell(P_{10}))=(3,4).
\]
Every cycle \(C_n\) with \(3\le n\le12\) has equal dimensions; the first strict cyclic gap is
\[
(v(C_{13}),\ell(C_{13}))=(4,5).
\]
Moreover, for every integer \(s\ge1\), the disjoint union of \(s\) ten-vertex paths has
\[
\operatorname{VCdim}\mathcal M(sP_{10})=3s,\qquad
\operatorname{Ldim}\mathcal M(sP_{10})=4s.
\]
In particular, the difference is unbounded even within graphs of maximum degree two. The connected-path and cycle threshold assertions are exact finite classifications, not extrapolations to larger connected graphs.

## Assumptions and scope
A graph is finite, loopless, undirected, and has no parallel edges. A vertex set is *independent* if it contains no edge, and *maximal independent* if no additional vertex can be adjoined while preserving independence; maximal does **not** mean maximum cardinality. A support \(S\subseteq V(G)\) is VC-shattered if \(\{I\cap S:I\in\mathcal M(G)\}=2^S\). A complete depth-\(d\) binary query tree is Littlestone-shattered if each branch of \(d\) prescribed binary membership outcomes is realized by some \(I\in\mathcal M(G)\); queries may depend on previous answers. Graph \(P_n\) has vertices \(0,\ldots,n-1\) and consecutive edges; \(C_n\) adds edge \(\{0,n-1\}\), defined for \(n\ge3\). Isolated vertices are allowed as components of general graphs. The empty graph has both dimensions zero.

## Proof
**1. Complete finite test.** A maximal independent set of an \(n\)-vertex graph is exactly an independent subset dominating all vertices. Thus the following exhaustive predicate, checked on each integer \(0\le b<2^n\), generates **all and only** concepts: no edge has both endpoints in \(b\), and each vertex outside \(b\) has a neighbor inside \(b\). This is a complete search, rather than sampling. Given the resulting finite hypothesis family \(H\), every \(S\subseteq V\) is VC-shattered precisely when the set of bit projections \(\{h\mathbin{\&}S:h\in H\}\) has \(2^{|S|}\) elements. Exhausting all \(S\) therefore computes exact VC dimension.

For Littlestone dimension, define \(R(H,U)\), where \(U\) is the available set of as-yet-unqueried vertices. Its value is zero if no vertex \(x\in U\) has both nonempty restrictions \(H_{x=0}\) and \(H_{x=1}\); otherwise
\[
R(H,U)=1+\max_{\substack{x\in U\\H_{x=0},H_{x=1}\ne\varnothing}}
\min\bigl(R(H_{x=0},U\setminus\{x\}),R(H_{x=1},U\setminus\{x\})\bigr).
\]
This is exact by induction on \(|U|\): a complete shattered tree has some first query, and both branches must support the remaining height; conversely, two such subtrees graft together. No repeated query along a branch is needed in a shattered tree. The finite calculation of \(R(H,V)\) is exhaustive, without statistical inference. `verify.py` implements both exhaustive procedures; `independent_check.py` independently constructs concepts by recursive independent-set generation and tests depth feasibility as a Boolean predicate.

Their complete exact values through thirteen vertices are:

| \(n\) | \(|\mathcal M(P_n)|\) | \(v(P_n)\) | \(\ell(P_n)\) | \(|\mathcal M(C_n)|\) | \(v(C_n)\) | \(\ell(C_n)\) |
|---:|---:|---:|---:|---:|---:|---:|
|1|1|0|0|—|—|—|
|2|2|1|1|—|—|—|
|3|2|1|1|3|1|1|
|4|3|1|1|2|1|1|
|5|4|2|2|5|2|2|
|6|5|2|2|5|2|2|
|7|7|2|2|7|2|2|
|8|9|3|3|10|3|3|
|9|12|3|3|12|3|3|
|10|16|3|4|17|3|3|
|11|21|4|4|22|4|4|
|12|28|4|4|29|4|4|
|13|37|4|5|39|4|5|

In `certificate.json`, the shattered VC supports of the exceptional path and cycle are respectively \(\{0,3,6\}\) and \(\{0,2,5,8\}\). It contains complete depth-four and depth-five adaptive query trees with respectively sixteen and thirty-two distinct maximal-independent-set leaf witnesses. Each witness is checked for the complete answer history leading to its leaf. The two upper bounds are independently immediate from concept counts: \(|\mathcal M(P_{10})|=16<32\) and \(|\mathcal M(C_{13})|=39<64\), whereas depth five and depth six respectively would require at least thirty-two and sixty-four distinct witnesses. The finite search also excludes every larger VC support, as well as a depth-four tree on \(C_{10}\).

**2. Degree-two reduction.** Every finite connected graph of maximum degree at most two is a path, an isolated vertex, or a cycle. The table proves equality on each component of order at most nine. On ten vertices the only connected possibilities are \(P_{10}\) and \(C_{10}\); the table identifies exactly the former as a gap. Any disconnected ten-vertex graph has components of smaller order.

**3. Product additivity.** If \(G\) and \(H\) are vertex-disjoint, then \(\mathcal M(G\sqcup H)=\mathcal M(G)\times\mathcal M(H)\) on disjoint query sets. VC dimension adds because a support is shattered by the product exactly when its projections are separately shattered. Littlestone dimension adds: concatenating complete adaptive shattered trees gives the lower bound, and the deterministic realizable mistake-bound characterization gives the upper bound by running the two optimal online learners independently, each paying at most its own dimension. Therefore both dimensions add over components. Applying this to the ten-vertex path yields the infinite-family formulas.

## Verification
The fully standalone artifacts `verify.py`, `independent_check.py`, and `certificate.json` were executed together under Python 3.10 or newer (standard library only). Running `python3 verify.py` and `python3 independent_check.py` in the directory containing the certificate reproduces `verification_output.txt`. Both programs independently obtain the exact twenty-four path/cycle rows; the first also checks every vertex-support projection and replays both explicit adaptive trees. Its recurrence searches all possible next queries and both outcomes. The second computes exact depth feasibility using a distinct representation of hypotheses and an independent Boolean recursion. The first reports `ALL_DEGREE_TWO_ADAPTIVE_GAP_CHECKS_PASS 24`; the second reports `INDEPENDENT_DEGREE_TWO_CROSSCHECK_PASS 24`.

## Relationship to prior work
Malliaris and Moran [1] develop the model-theoretic interpretation of Littlestone dimension through special trees, with a general theory of stable incidence classes. Their general results do not determine the present graph-specific thresholds. Palmer and Patkós [2] analyze numbers of maximal independent sets and give the recurrence for cycle counts; knowing concept cardinalities supplies only logarithmic upper bounds and does not establish the exact online dimensions or the first gap. Liu, Shangguan, Skokan, and Xu [3, Lemma 2.20] bound the VC dimension of the maximal-independent-set incidence system using bipartite induced matchings; that is a nonadaptive upper bound and does not settle the adaptive parameters. Related finite-forest results determine VC dimensions and an earlier eight-vertex branching example; they do not imply the sharp maximum-degree-two boundary or the first cyclic boundary. Distinct graph cover-free families on paths and cycles also do not identify the same incidence concept class.

## Limitations
The exact connected-graph classification is proved only through thirteen vertices, and no formula for the Littlestone dimension of all longer paths or cycles is asserted. The all-orders statement is solely the disjoint-union amplification. The novelty comparison covers identified literature and accessible research records, not an exhaustive priority determination. Computations are finite exhaustive proofs of the stated finite ranges because the algorithms are explicit and terminating over those ranges; their execution does not certify any larger unspecified range. Independent external scientific audit has not been performed.

## References
[1] M. Malliaris and S. Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569; first posted 2021-08-12. Inspected full accessible HTML of later version, especially §1.3 and §5.

[2] C. Palmer and B. Patkós, *On the number of maximal independent sets: From Moon–Moser to Hujter–Tuza*, arXiv:2205.04082; first posted 2022-05-09. Inspected full accessible HTML, especially §§1–2.

[3] H. Liu, C. Shangguan, J. Skokan, and Z. Xu, *Beyond chromatic threshold via the (p,q)-theorem, and a sharp blow-up phenomenon*, arXiv:2403.17910; first posted 2024-03-26. Inspected full accessible HTML, especially §2.4, Lemma 2.20.
