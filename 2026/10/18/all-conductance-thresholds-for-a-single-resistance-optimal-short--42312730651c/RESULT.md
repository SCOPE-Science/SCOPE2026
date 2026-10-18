# All conductance thresholds for a single resistance-optimal shortcut on a path

## Finding

**Complete finite-conductance phase diagram.** For every integer \(n\ge4\), let \(P_n\) be the unit-conductance path on vertices \(0,1,\ldots,n-1\). Insert exactly one additional edge joining nonadjacent vertices with prescribed finite conductance \(w>0\). Minimize the Kirchhoff index \(\operatorname{Kf}\), the sum of effective resistances over unordered vertex pairs, over all possible positions of the new edge.

Put \(K=\lfloor(n-1)/8\rfloor\). For each integer \(0\le k\le K\), define the centered shortcut \(e_k=\{k,n-1-k\}\). For \(0\le k<K\), define the positive rational threshold
\[
\tau_k=\frac{12(k+1)(n-2k-2)}{(n-2k-1)(n-2k-3)(n-8k-8)}.
\]
These thresholds are strictly increasing. With \(\tau_{-1}=0\) and \(\tau_K=+\infty\), the **unique** global minimizer for \(\tau_{k-1}<w<\tau_k\) is \(e_k\), for every \(0\le k\le K\). At \(w=\tau_k\), exactly \(e_k\) and \(e_{k+1}\) attain the minimum; no third shortcut ties. In particular, no off-center shortcut can be globally optimal. There are exactly \(\lfloor(n-1)/8\rfloor\) positive-conductance phase transitions, without skipped centered configurations.

The first new transition occurs at \(n=9\). For \(n=17\), the maximizing shortcut moves from \(\{0,16\}\) to \(\{1,15\}\) at \(w=5/56\), then to \(\{2,14\}\) at \(w=13/7\). For \(4\le n\le8\), the endpoint shortcut remains uniquely optimal at every finite \(w>0\).

## Assumptions and scope

Path-edge conductances stay exactly one; the added edge is a nonedge of the original path and has fixed conductance \(w>0\), independent of its selected endpoints. No other edge additions, deletions, or reallocations are permitted. The Kirchhoff index counts each unordered pair once. The minimization is over all \(\binom n2-(n-1)\) permissible unordered pairs. The theorem concerns finite positive \(w\), not the formal infinite-conductance quotient limit. The underlying optimization is unchanged if \(\operatorname{Kf}\) is divided by \(n\) to use \(\operatorname{tr}(L^+)\).

## Proof

**1. Exact improvement under one edge.** Fix \(0\le i<j\le n-1\) with span \(\ell=j-i\ge2\), and set \(b=\mathbf e_i-\mathbf e_j\). For the path Laplacian \(L\), the path effective resistance between these vertices is \(b^{\mathsf T}L^+b=\ell\). The voltage vector \(L^+b\), up to an additive constant and sign, has coordinates \(v_r=\min\{\ell,\max\{0,r-i\}\}\). Rank-one inversion on the orthogonal complement of constants gives
\[
\operatorname{Kf}(P_n)-\operatorname{Kf}(P_n+wbb^{\mathsf T})
=\frac{w}{1+w\ell}\left[n\sum_{r=0}^{n-1}v_r^2-\left(\sum_{r=0}^{n-1}v_r\right)^2\right].
\]
Writing \(q=n-1-j\) and \(p=i\) (left and right exterior tail lengths), the bracket simplifies exactly to
\[
A(i,\ell)=\frac{n\ell(3n\ell-2\ell^2+2)}{12}-\frac{\ell^2(p-q)^2}{4}.
\]
Also \(\operatorname{Kf}(P_n)=(n^3-n)/6\). Therefore minimizing \(\operatorname{Kf}\) is equivalent to maximizing \(wA(i,\ell)/(1+w\ell)\).

**2. Unbalanced tails can never win.** Fix \(\ell\). Since \(p+q=n-1-\ell\), the numerator is maximal for the most balanced pair of tails. Set \(A_0(\ell)=n\ell(3n\ell-2\ell^2+2)/12\) and let \(\varepsilon_\ell\in\{0,1\}\) be the parity of \(n-1-\ell\). The fixed-span maximum is \(A_\ell=A_0(\ell)-\varepsilon_\ell\ell^2/4\). Whenever \(\varepsilon_\ell=1\) and \(3\le\ell\le n-2\), neighboring spans have balanced tails and obey the exact identity
\[
A_{\ell-1}+A_{\ell+1}-2A_\ell=\frac{(n-\ell)^2}{2}>0.
\]
As \(1+w\ell\) is the arithmetic mean of \(1+w(\ell-1)\) and \(1+w(\ell+1)\), the ratio at \(\ell\) is strictly below the larger neighboring ratio. If \(n\) is even and \(\ell=2\) has odd tail imbalance, the span-three centered chord wins because \(A_3>A_2\) and \(A_3/3>A_2/2\) for every \(n\ge4\). Thus every global optimum has \(\varepsilon_\ell=0\), with an exactly centered chord \(\{k,n-1-k\}\); any nonmaximal placement at its span is strictly dominated. The candidates have \(\ell=n-1-2k\), \(k\ge0\), \(\ell\ge2\).

**3. Consecutive centered chords.** Define for real \(x>0\)
\[
F_w(x)=\frac{w A_0(x)}{1+wx},\qquad A_0(x)=\frac{nx(3nx-2x^2+2)}{12}.
\]
Direct polynomial subtraction gives
\[
A_0(x)-A_0(x-2)=n(x-1)(n+1-x),
\]
\[
xA_0(x-2)-(x-2)A_0(x)=\frac{nx(x-2)(4x-3n-4)}{6}.
\]
For every valid centered span \(x\ge3\), the first difference is positive. Hence \(F_w(x)=F_w(x-2)\) at a positive finite \(w\) precisely when \(4x>3n+4\), and then the crossing weight is
\[
w=\frac{6(x-1)(n+1-x)}{x(x-2)(4x-3n-4)}.
\]
Substituting \(x=n-1-2k\) yields exactly \(\tau_k\) in the finding. The longer of the two chords wins strictly below this threshold and the shorter wins strictly above. There is no positive crossing if \(4x\le3n+4\). Thus positive consecutive crossings occur exactly for \(k=0,\ldots,K-1\).

**4. No skipping and no shorter global competitor.** Direct differentiation yields
\[
F'_w(x)=\frac{nw\,[2+6x(n-x)+wx^2(3n-4x)]}{12(1+wx)^2},
\]
\[
F''_w(x)=-\frac{nw\,[2w^2x^3+6wx^2+6x-3n+2w]}{6(1+wx)^3}.
\]
For every \(w>0\), \(F'_w(x)>0\) on \(0<x\le3n/4\), while \(F''_w(x)<0\) on \(x\ge n/2\). All centered spans \(\ell_k=n-1-2k\), \(0\le k\le K\), lie in the latter strict-concavity interval. At a crossing of \(\ell_k\) and \(\ell_{k+1}\), strict concavity forces \(F_w(\ell_{k+1})>F_w(\ell_{k+2})\) whenever \(k+2\le K\). Since the comparison of successive spans switches sign only once, this forces \(\tau_k<\tau_{k+1}\). Consequently, among \(e_0,\ldots,e_K\), precisely the claimed one or adjacent two maximize, with no intermediate configuration skipped.

For the last admitted span \(\ell_K\), the condition \(n\le8(K+1)\) gives \(4\ell_K\le3n+4\), so \(F_w(\ell_K)>F_w(\ell_K-2)\) for all \(w>0\) whenever the shorter centered span exists. Moreover \(\ell_K-2\le3n/4\); strict increase of \(F_w\) up to \(3n/4\) excludes every still-shorter centered chord. Together with Step 2 this excludes all remaining nonedges. Therefore the described list is complete, and the equality cases are exactly the claimed pairs. \(\square\)

## Verification

The reproducible symbolic/rational script `verify.py` (Python 3.11 or later and SymPy 1.13) verifies the exact polynomial difference identities, the centered-tail amplitude and the parity-imbalance identity. It exhaustively evaluates the actual Kirchhoff-improvement scores for all nonadjacent endpoint pairs for every \(4\le n\le32\), testing positive rational conductances both away from and exactly at the predicted thresholds; it also checks direct exact Laplacian inverses for \(4\le n\le9\). Its recorded result is `VERIFY_OK 67122 exact symbolic, rational placement, tie, and direct-matrix checks`. Finite enumeration is corroborative and does not prove the assertion for unbounded \(n\); the preceding analytical argument does.

## Relationship to prior work

Rank-one pseudoinverse updates and minimizing total effective resistance are established tools in network design [1,2]. General single- or multi-edge resistance-robustness insertion algorithms [3] do not give these path-specific all-conductance transition thresholds. Classical Kirchhoff-index extremal results for all unicyclic graphs [4] vary the whole topology rather than hold all path edges fixed and optimize a prescribed-weight shortcut. Earlier path-specific analysis already establishes the exact gain formula, the first endpoint-to-one-step-inward transition, and a fixed-weight large-path limit; those facts are **not** claimed as new here. The contribution is the complete sequence of **all** finite-\(n\) thresholds, strict ordering, exclusion of every noncentered optimizer, unique/no-skipping equality classification, and exact number of transitions.

## Limitations

The theorem addresses one inserted edge with a fixed strictly positive finite conductance on a unit-conductance path only. It does not treat optimal simultaneous edge additions, optimizing the edge conductance itself under a budget, heterogeneous path weights, spectral-gap objectives, or any claim that a generic graph admits similarly simple thresholds. The literature comparison is not a proof of global historical novelty; equivalent specialized results may exist outside inspected materials. Independent mathematical audit has not been performed.

## References

[1] A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66; earlier 2006 proceedings version. DOI: 10.1137/050645452. Accessible proceedings PDF: https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf.

[2] T. H. Summers, I. Shames, J. Lygeros, F. Dörfler, *Topology Design for Optimal Network Coherence*, arXiv:1411.4884v1 (18 November 2014). https://arxiv.org/pdf/1411.4884.

[3] M. Predari, L. Berner, R. Kooij, H. Meyerhenke, *Greedy Optimization of Resistance-based Graph Robustness with Global and Local Edge Insertions*, Social Network Analysis and Mining 13 (2023), article 130. DOI: 10.1007/s13278-023-01137-1. https://link.springer.com/article/10.1007/s13278-023-01137-1.

[4] Y. Yang, X. Jiang, *Unicyclic Graphs with Extremal Kirchhoff Index*, MATCH Communications in Mathematical and in Computer Chemistry 60 (2008), 107–120. https://match.pmf.kg.ac.rs/electronic_versions/Match60/n1/match60n1_107-120.pdf.
