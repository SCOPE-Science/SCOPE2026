# Rank, regularity and idempotents in the Margolis–Rhodes monoid of a star

## Finding

Let \(m\ge3\), and let \(K_{1,m}\) be the labeled star with center \(c\) and leaf set \(L\), \(|L|=m\). Let \(M=\operatorname{MR}(K_{1,m})\) be the monoid of partial functions \(f:V\rightharpoonup V\) such that, for every singleton vertex and every edge \(X\) of the target graph, the full inverse image \(f^{-1}(X)\) is empty, a singleton, or an edge of the source star. The empty map belongs to \(M\).

Write \(\operatorname{rk}(f)=|\operatorname{im} f|\). For integers \(a,b\ge0\), define the partial-injection polynomial
\[
F_{a,b}(t)=\sum_{j=0}^{\min(a,b)}\binom aj(b)_{\underline j}t^j,\qquad (b)_{\underline j}=b(b-1)\cdots(b-j+1),\quad (b)_{\underline 0}=1,
\]
and write \(F_a(t)=F_{a,a}(t)\). Define the complete rank census, idempotent census and nonregular census by
\[
P_m(t)=\sum_{f\in M}t^{\operatorname{rk}(f)},\qquad
E_m(t)=\sum_{\substack{f\in M\\f^2=f}}t^{\operatorname{rk}(f)},\qquad
N_m(t)=\sum_{\substack{f\in M\\f\text{ is not regular}}}t^{\operatorname{rk}(f)}.
\]
Here regular means that some \(g\in M\) satisfies \(fgf=f\).

**Theorem.** For every integer \(m\ge3\),
\[
\boxed{P_m(t)=F_{m,m+1}(t)+2mt+tF_m(t)+m^2t^2+m^2tF_{m-1}(t),}
\]
\[
\boxed{E_m(t)=(1+t)^{m+1}+mt\bigl(1+(1+t)^{m-1}\bigr),}
\]
\[
\boxed{N_m(t)=\sum_{r=2}^{m}\binom mr\binom m{r-1}r!\,t^r.}
\]
The nonregular elements are *exactly* the injective partial functions \(f\) whose image consists of at least two leaves and whose domain contains the center. Thus the regular rank enumerator is \(P_m(t)-N_m(t)\), and the total number of idempotents is \(2^{m+1}+m(1+2^{m-1})\). These identities hold also for \(m=1,2\), where the star is a complete graph or a path; novelty is asserted only for the branching family \(m\ge3\).

## Assumptions and scope

All functions are partial maps with the convention that the inverse image of a target set consists only of points in the domain. Products are compositions of partial maps; the chosen left/right convention does not affect idempotency or regularity. The source and target star are the same labeled graph. Each element is counted as a distinct partial function, not modulo automorphisms. The variable \(t\) records the cardinality of the image. No assumptions about coefficient fields are involved.

The convention on continuity is *inverse-image simplex continuity*: it is not ordinary graph-homomorphism continuity. In particular, a one-to-one map may send an edge to two nonadjacent leaves and still be continuous.

## Proof

**1. Fiber decomposition.** For a continuous \(f\), the inverse image of any singleton has cardinality at most two. If it has two elements, those elements must form an edge of the source star. Distinct fibers are disjoint, and any two edges in a star meet at the center. Consequently at most one fiber has cardinality two. If such a double fiber exists, it is \(\{c,u\}\) for one leaf \(u\). If its image is the center, no further image vertex is possible: the inverse image of the edge joining the center to any additional image leaf would contain at least three vertices. If the double fiber has image a leaf \(v\), any other image points must be leaves distinct from \(v\), because the center is adjacent to \(v\). The remaining source vertices are leaves, and an arbitrary injection from a subset of them to the remaining target leaves is continuous. Conversely all these maps meet the vertex- and edge-preimage conditions. This gives \(mt\) maps in the first double-fiber case and \(m^2tF_{m-1}(t)\) in the second: choose \(u\), choose \(v\), then a partial injection from the \(m-1\) unused source leaves to the \(m-1\) other target leaves.

**2. Injective maps.** If \(c\notin\operatorname{im}f\), every partial injection to \(L\) is continuous, with rank enumerator \(F_{m,m+1}(t)\). If \(\operatorname{im}f=\{c\}\), there are \(m+1\) singleton maps. Otherwise the image comprises \(c\) and \(s\ge1\) leaves. Each target edge from \(c\) to an image leaf must have a source edge as inverse image. If the unique preimage of \(c\) is \(c\), the preimages of the \(s\) other image vertices are distinct leaves, contributing \(\binom ms(m)_{\underline s}\) maps of rank \(s+1\). If the preimage of \(c\) is a leaf, the preimage of *every* image leaf must be \(c\), so necessarily \(s=1\); there are \(m^2\) such exceptional maps of rank two. Thus the remaining injective rank enumerator is
\[
(m+1)t+t(F_m(t)-1)+m^2t^2.
\]
Adding this to Step 1 yields \(P_m(t)\), because \((m+1)+m-1=2m\).

**3. Idempotents.** For any partial transformation, \(f^2=f\) exactly when every element of its image lies in its domain and is fixed. Every injective idempotent is a partial identity, contributing \((1+t)^{m+1}\). In the double-fiber case \(\{c,u\}\), the image of the double fiber must be one of \(c,u\) so that it is fixed. If it is \(c\), no further image is possible: for each \(u\) there is exactly one rank-one idempotent. If it is \(u\), any subset of the other \(m-1\) leaves may be fixed additionally, giving \(mt(1+t)^{m-1}\). This yields the stated \(E_m(t)\). Notice that mapping \(\{c,u\}\) to a *different* leaf is not idempotent, because that image leaf would not belong to the double fiber and would have to be fixed separately, contradicting its double fiber.

**4. Regularity.** If \(fgf=f\), restricting \(g\) to \(\operatorname{im}f\) gives a continuous section of \(f\) (for every image point, it chooses one preimage). Conversely any continuous section \(g\) gives \(fgf=f\). Restrictions of continuous partial maps remain continuous, so the criterion is exact.

Every map with a double fiber is regular. For a single-image map choose either point of its nonempty fiber as the section. For a double fiber mapped to a leaf, choose the leaf \(u\) of the paired source edge as the preimage of its image point; all other source preimages are leaves. The section is a partial injection from leaves to leaves and is therefore continuous.

For an injective \(f\), its section is uniquely its partial inverse. Both \(f\) and its inverse are continuous if and only if the induced graphs on domain and image are isomorphic under \(f\): the inverse-image condition for two distinct image vertices is exactly preservation of target edges, and applying it to \(f^{-1}\) gives preservation of source edges. A continuous injection from the star whose image contains \(c\) is such an isomorphism, by the cases in Step 2: if the image has at least two leaves, the center must be fixed, while a two-vertex edge may have its endpoints swapped. If the image lies in \(L\), it is independent, so an isomorphism occurs exactly when the domain is also independent. For image size at least two, a source subset of the star is independent exactly when it does not contain \(c\). Thus nonregular maps are precisely the asserted injections with image contained in \(L\), rank \(r\ge2\), and source domain containing \(c\).

Choose the target image of size \(r\) in \(\binom mr\) ways, the other \(r-1\) source domain leaves in \(\binom m{r-1}\) ways, and the bijection in \(r!\) ways. This proves \(N_m(t)\), completing the theorem.

## Verification

The standalone `verify.py` uses *the defining simplex-preimage condition*, rather than the case split in the proof, to enumerate every partial map on \(m+1\) labeled vertices. It checks each predicted coefficient of \(P_m\) and \(E_m\) for \(1\le m\le6\). For \(1\le m\le5\) it checks regularity independently by enumerating all sections and testing whether a section is continuous. The exhaustive results are:

| \(m\) | \(|M|\) | \(\#\{f^2=f\}\) | \(\#\{f\text{ regular}\}\) |
|---:|---:|---:|---:|
| 1 | 9 | 6 | 9 |
| 2 | 36 | 14 | 32 |
| 3 | 185 | 31 | 149 |
| 4 | 1278 | 68 | 990 |
| 5 | 10857 | 149 | 8357 |
| 6 | 106664 | 326 | not exhaustively checked |

All checked coefficients agree with the three formulas. The finite checks are corroboration, not a proof for unbounded \(m\); that proof is in the preceding case analysis.

## Relationship to prior work

Margolis and Rhodes (2021) define continuous partial functions on graphs using full inverse images of simplices and prove the general fiber structure. Margolis and Rhodes (2026, arXiv:2609.39370, first public version September 30, 2026) develop the monoid further, including explicit enumerations for paths and cycles, and a general characterization of singular and injective parts (their Section 3.4). The present theorem is a specialization to the *first branching tree family*, with full rank enumeration, explicit regularity obstruction, nonregular rank census, and idempotent rank census. The general structural lemma is antecedent knowledge; it is not claimed as new. The cases \(m=1,2\) overlap familiar complete-graph and path behavior and are stated only as boundary checks.

The general fiber decomposition alone does not state the three formulas or identify which labeled star maps fail regularity. A differently indexed enumeration may exist, particularly in work on translational hulls or degree-two transformation semigroups; no absolute priority claim is made.

## Limitations

The theorem applies to stars only, not arbitrary trees. It counts labeled maps rather than isomorphism or conjugacy classes. It determines element regularity and image rank, not the detailed Green-class multiplication table or Krohn–Rhodes complexity.

## References

1. S. Margolis and J. Rhodes, *The Margolis–Rhodes Monoid of a Graph*, arXiv:2609.39370 (first public version 2026-09-30), https://arxiv.org/abs/2609.39370 .
2. S. Margolis and J. Rhodes, *Degree 2 transformation semigroups as continuous maps on graphs: Foundations and structure*, International Journal of Algebra and Computation **31** (2021), 1065–1091, doi:10.1142/S0218196721400051 .
