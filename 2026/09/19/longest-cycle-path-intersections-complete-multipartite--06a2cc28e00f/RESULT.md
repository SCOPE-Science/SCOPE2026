# Exact intersections of longest cycles and paths in complete multipartite graphs

## Result

Let
\[
G=K_{n_1,\ldots,n_r},\qquad r\ge 2,
\]
be a connected complete multipartite graph. Put
\[
n=\sum_i n_i,\qquad M=\max_i n_i,\qquad q=n-M.
\]
Then the vertex-connectivity of \(G\) is
\[
\kappa(G)=q.
\]

The longest-cycle and longest-path vertex sets admit an exact description depending only on \(M\) and \(q\).

### Longest cycles

Assume \(q\ge 2\), so \(G\) is 2-connected and contains a cycle.

If \(M\le q\), then \(G\) is Hamiltonian. Hence every longest cycle is spanning, the intersection of all longest cycles is \(V(G)\), and any two longest cycles intersect in all \(n\) vertices.

Suppose instead that \(M>q\). Then the largest part \(B\) is unique. Write
\[
O=V(G)\setminus B,\qquad |B|=M,\qquad |O|=q.
\]
The circumference is \(2q\), and the collection of vertex sets of longest cycles is exactly
\[
\mathcal V_C(G)=
\left\{\,O\cup A:A\in\binom{B}{q}\,\right\}.
\]
Consequently,
\[
\bigcap_{X\in\mathcal V_C(G)}X=O,
\qquad
|\mathcal V_C(G)|=\binom{M}{q},
\]
and the complete pairwise intersection spectrum is
\[
\left\{|X\cap Y|:X,Y\in\mathcal V_C(G)\right\}
=
\left\{
q+t:
\max(0,2q-M)\le t\le q
\right\}.
\]
In particular, the minimum possible intersection of two longest cycles is
\[
\boxed{
\iota_C(G)=
\begin{cases}
n,&M\le q,\\[1mm]
q+\max(0,2q-M),&M>q.
\end{cases}}
\]
Since \(\kappa(G)=q\), every complete multipartite graph satisfies Smith's conjectured lower bound
\[
\iota_C(G)\ge \kappa(G),
\]
and in the non-Hamiltonian regime equality holds exactly when
\[
M\ge 2q.
\]
Equivalently, equality holds exactly when \(n\ge3\kappa(G)\). Thus the usual complete-bipartite sharpness construction is part of a larger complete-multipartite equality family.

### Longest paths

For every connected \(G\) above, let \(\mathcal V_P(G)\) be the collection of vertex sets of longest paths.

If \(M\le q+1\), then \(G\) has a Hamiltonian path, so
\[
\mathcal V_P(G)=\{V(G)\}.
\]

If \(M>q+1\), then \(B\) is again the unique largest part and
\[
\mathcal V_P(G)=
\left\{\,O\cup A:A\in\binom{B}{q+1}\,\right\}.
\]
Thus the longest paths have \(2q+1\) vertices,
\[
\bigcap_{X\in\mathcal V_P(G)}X=O,
\qquad
|\mathcal V_P(G)|=\binom{M}{q+1},
\]
and
\[
\left\{|X\cap Y|:X,Y\in\mathcal V_P(G)\right\}
=
\left\{
q+t:
\max(0,2q+2-M)\le t\le q+1
\right\}.
\]
Therefore the minimum possible intersection of two longest paths is
\[
\boxed{
\iota_P(G)=
\begin{cases}
n,&M\le q+1,\\[1mm]
q+\max(0,2q+2-M),&M>q+1.
\end{cases}}
\]
Hence complete multipartite graphs also satisfy Hippchen's conjectured bound
\[
\iota_P(G)\ge\kappa(G).
\]
In the non-traceable regime, equality holds exactly when
\[
M\ge2q+2,
\]
equivalently \(n\ge3\kappa(G)+2\).

The statements about the common core are stronger than the pairwise inequalities: in every non-Hamiltonian complete multipartite graph all longest cycles contain the same minimum vertex cut \(O\), and in every non-traceable complete multipartite graph all longest paths contain the same minimum vertex cut \(O\).

## Proof

First, \(\delta(G)=n-M=q\). Deleting fewer than \(q\) vertices cannot leave vertices from only one part, because deleting all vertices outside any part requires at least \(q\) deletions. Hence no set of fewer than \(q\) vertices disconnects \(G\), while the standard bound \(\kappa(G)\le\delta(G)\) gives
\[
\kappa(G)=q.
\]

Fix a largest part \(B\), with complement \(O\).

For any cycle \(C\), no two consecutive vertices can lie in \(B\). Hence
\[
|V(C)\cap B|\le |V(C)\cap O|\le q.
\]
If \(M>q\), this gives \(|C|\le2q\). Conversely, for any \(q\)-subset
\[
A=\{a_1,\ldots,a_q\}\subseteq B
\]
and any ordering \(O=\{o_1,\ldots,o_q\}\), the alternating sequence
\[
a_1o_1a_2o_2\cdots a_qo_qa_1
\]
is a cycle. Thus the circumference is \(2q\). Equality in the upper bound forces a longest cycle to contain all \(q\) vertices of \(O\) and exactly \(q\) vertices of \(B\), proving the asserted description of \(\mathcal V_C(G)\).

If \(M\le q\), then
\[
\delta(G)=q\ge n/2,
\]
so Dirac's theorem gives a Hamiltonian cycle. This establishes the cycle dichotomy.

For paths, the same adjacency obstruction gives
\[
|V(P)\cap B|\le |V(P)\cap O|+1.
\]
Thus if \(M>q+1\), every path has at most \(2q+1\) vertices. For every \((q+1)\)-subset
\[
A=\{a_1,\ldots,a_{q+1}\}\subseteq B,
\]
the sequence
\[
a_1o_1a_2o_2\cdots a_qo_qa_{q+1}
\]
is a path, so the upper bound is attained; equality forces all vertices of \(O\) and exactly \(q+1\) vertices of \(B\).

If \(M\le q\), a Hamiltonian cycle gives a Hamiltonian path (with the trivial \(K_2\) case immediate). If \(M=q+1\), the preceding alternating path using all of \(B\) and all of \(O\) is Hamiltonian. Hence \(G\) is traceable exactly when \(M\le q+1\).

It remains to compute intersections. Two \(k\)-subsets of an \(M\)-set can have intersection size exactly \(t\) if and only if
\[
\max(0,2k-M)\le t\le k.
\]
Indeed, the lower bound is inclusion-exclusion, and every integer in this interval is realized by choosing \(t\) common elements and disjoint complements of size \(k-t\). Applying this with \(k=q\) for longest cycles and \(k=q+1\) for longest paths gives the displayed spectra and minimum-intersection formulas.

Finally, because \(M>q\) (respectively \(M>q+1\)) in the non-spanning regimes, the intersection of all \(q\)-subsets (respectively all \((q+1)\)-subsets) of \(B\) is empty. Hence the common core is exactly \(O\), whose size is \(q=\kappa(G)\).

## Context and originality

Smith's conjecture asks whether any two longest cycles in every \(k\)-connected graph share at least \(k\) vertices. Ma, Ning and Zhao (2026) proved the first linear general bound, \(k/600\). Their introduction notes that the conjectured constant is sharp for \(K_{k,n-k}\) when \(n\ge3k\): two longest cycles can choose disjoint \(k\)-subsets of the larger bipartition class and then meet exactly in the smaller class.

The theorem above identifies the full mechanism inside all complete multipartite graphs. It determines every possible longest-cycle and longest-path vertex set, the intersection of all such sets, the full pairwise intersection spectrum, and exactly when the Smith and Hippchen lower bounds are attained.

Gutiérrez and Valqui (2024) relate Smith's and Hippchen's conjectures and establish dense-regime bounds for both. A full-text search of their arXiv version did not return "multipartite" or "bipartite". The 2013 survey by Shabbir, C. T. Zamfirescu and T. I. Zamfirescu was also inspected in full text; a search did not return "multipartite". Exact and synonymous searches for complete multipartite longest-cycle/longest-path intersection formulas did not locate the classification above.

Accordingly, originality is claimed only **to the best of our knowledge**. The main residual risk is older or class-specific literature using different terminology. Two especially relevant sources were not fully inspected: Thomas Hippchen's 2008 thesis *Intersections of Longest Paths and Cycles*, which introduced the path conjecture, and Haidong Wu's 2026 article *Intersection of cycles and paths in k-connected graphs* (Discrete Applied Mathematics 378, 226--233). Available bibliographic records and abstracts/snippets did not indicate a complete-multipartite classification, but their full texts were not inspected. Philip Kains's 2023 dissertation *On Intersections of Long Cycles and Paths in k-Connected Graphs* was available at the abstract level; its downloadable full text could not be inspected. These access limitations leave residual originality uncertainty but no concrete evidence of prior coverage.

## Verification

A standalone verifier enumerates every connected complete multipartite isomorphism type of order \(2\) through \(9\), constructs the graph from its adjacency relation, and uses exact subset dynamic programming to determine which vertex subsets support Hamiltonian paths or cycles. It then derives the longest-path and longest-cycle vertex-set families directly from the definition and compares:

- maximum path/cycle order;
- the complete pairwise intersection spectrum;
- the common core in each non-spanning regime; and
- the number of distinct longest-object vertex sets.

The executed verification covered 87 graph types, 166 longest-object checks, and 44 non-spanning core/count checks, with no discrepancy. This finite verification supports but does not replace the proof.

## References

1. J. Ma, B. Ning, Z. Zhao, *Longest cycles intersect linearly in highly connected graphs*, arXiv:2609.20724 (2026). https://arxiv.org/abs/2609.20724
2. J. Gutiérrez, C. Valqui, *On two conjectures about the intersection of longest paths and cycles*, Discrete Mathematics 347 (2024), 114148; arXiv:2310.03849. https://arxiv.org/abs/2310.03849
3. A. Shabbir, C. T. Zamfirescu, T. I. Zamfirescu, *Intersecting longest paths and longest cycles: A survey*, Electronic Journal of Graph Theory and Applications 1 (2013), 56--76. https://doi.org/10.5614/ejgta.2013.1.1.6
4. H. Wu, *Intersection of cycles and paths in k-connected graphs*, Discrete Applied Mathematics 378 (2026), 226--233. https://doi.org/10.1016/j.dam.2025.07.013
5. P. Kains, *On Intersections of Long Cycles and Paths in k-Connected Graphs*, Ph.D. dissertation, University of Mississippi (2023). https://egrove.olemiss.edu/etd/2690/
6. T. Hippchen, *Intersections of Longest Paths and Cycles*, Ph.D. thesis, Georgia State University (2008).
