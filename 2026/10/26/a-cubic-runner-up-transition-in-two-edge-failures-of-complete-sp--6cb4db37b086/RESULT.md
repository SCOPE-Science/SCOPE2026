# A cubic runner-up transition in two-edge failures of complete split networks

## Finding
Let \(p\ge3\) and \(q\ge2\) be integers, and let \(G=K_p\vee\overline{K_q}\) be the unweighted complete split graph with clique \(X\) of size \(p\) and independent part \(Y\) of size \(q\). For each unordered pair of distinct existing edges \(F\), define the resistance vulnerability
\[
\Delta(F)=\operatorname{Kf}(G-F)-\operatorname{Kf}(G),
\qquad
\operatorname{Kf}(H)=\sum_{\{u,v\}\subset V(H)}R_H(u,v),
\]
where \(R_H\) is the unit-conductance effective resistance.

**Worst pair.** The unique failure pattern maximizing \(\Delta\) is two cross-edges with a common endpoint in \(Y\) and different endpoints in \(X\). It has exactly \(q\binom p2\) realizations, and the common maximal damage is
\[
\Delta_{\max}=
\frac{2(2p^2+2pq-3p+q^2-q)}{p(p-2)(p+q-1)}.
\]

**Runner-up, including all equality cases.** Put
\[
R_p=p^3-3p^2+p+1.
\]
If \(2\le q\le R_p\), the strictly second-largest damage is attained precisely by two cross-edges sharing an endpoint in \(X\) (\(p\binom q2\) pairs). If \(q\ge R_p+1\), it is attained precisely by two disjoint cross-edges (\(2\binom p2\binom q2\) pairs). In either regime all other failure patterns have strictly smaller damage, and there is no integer-parameter tie for second place.

Thus a disjoint two-link failure overtakes an incident failure as the network's independent part grows past an explicit cubic threshold. For \(p=3\), this switch occurs between \(q=4\) and \(q=5\); for \(p=4\), between \(q=21\) and \(q=22\).

## Assumptions and scope
All graphs are finite, undirected, simple, and have unit edge conductance. The two deleted edges must be **distinct** and **present before deletion**. The graph remains connected after any such deletion: removing at most one clique edge leaves the clique connected, while removing two clique edges leaves every cross-edge intact; every vertex in \(Y\) retains at least \(p-2\ge1\) incident cross-edges. Effective resistances and the Kirchhoff index are therefore finite for every permitted pair.

Set \(N=p+q\), and write \(J\) for the all-ones matrix. The intact graph has Laplacian eigenvalues \(0\) (once), \(p\) (multiplicity \(q-1\)), and \(N\) (multiplicity \(p\)), giving
\[
\operatorname{Kf}(G)=p+\frac{N(q-1)}p.
\]
Every existing edge is either a clique edge (type \(XX\)) or a cross-edge (type \(XY\)). There are exactly seven automorphism orbits of unordered two-edge failures, one of which requires \(p\ge4\). Their representatives and exact damage formulas appear in `COMPARISONS.md`.

## Proof
**1. Spectral inverse and rank-two deletion.** On the constant-free subspace, the orthogonal projection onto vectors supported on \(Y\) with coordinate sum zero is
\[
P_Y=\operatorname{diag}(0_X,I_Y-J_Y/q).
\]
Consequently, with \(L\) the intact Laplacian,
\[
L^+=\frac1N(I-J/N)+\left(\frac1p-\frac1N\right)P_Y,
\quad
(L^+)^2=\frac1{N^2}(I-J/N)+\left(\frac1{p^2}-\frac1{N^2}\right)P_Y.
\]
For oriented incidence vectors \(b,c\) of the two deleted edges, form \(B=[b,c]\), \(K=B^{\mathsf T}L^+B\), and \(S=B^{\mathsf T}(L^+)^2B\). Since the deleted graph is connected, \(I_2-K\) is positive definite. The Woodbury identity restricted to the constant-free subspace gives the **exact** formula
\[
\Delta(\{b,c\})=N\operatorname{tr}[(I_2-K)^{-1}S].
\]
Writing \(r_b=b^{\mathsf T}L^+b\), \(r_c=c^{\mathsf T}L^+c\), \(s_b=b^{\mathsf T}(L^+)^2b\), \(s_c=c^{\mathsf T}(L^+)^2c\), \(k=b^{\mathsf T}L^+c\), \(t=b^{\mathsf T}(L^+)^2c\), this equals
\[
N\frac{(1-r_c)s_b+(1-r_b)s_c+2kt}{(1-r_b)(1-r_c)-k^2}.
\]
All denominators are strictly positive because they are Gram-deletion determinants for connected graphs.

**2. Complete orbit reduction.** The automorphism group \(S_p\times S_q\) permutes the labels inside \(X\) and \(Y\) independently. Two cross-edges may share their \(Y\) endpoint (orbit \(A\)), share their \(X\) endpoint (\(B\)), or be disjoint (\(C\)). A clique edge and a cross-edge either meet (\(D\)) or are disjoint (\(E\)). Two clique edges either meet (\(F\)) or are disjoint (\(G\)); \(G\) requires \(p\ge4\). There are no other orbits.

For any oriented edges \(b,c\), put \(b_Y\) and \(c_Y\) for their restrictions to \(Y\). The spectral formulas give, for \(j=1,2\),
\[
b^{\mathsf T}(L^+)^jc
=\frac{b^{\mathsf T}c}{N^j}+
\left(\frac1{p^j}-\frac1{N^j}\right)
\left(b_Y^{\mathsf T}c_Y-\frac{(\mathbf1^{\mathsf T}b_Y)(\mathbf1^{\mathsf T}c_Y)}q\right).
\]
Substituting orbit representatives into the rank-two formula gives the seven rational damage values reproduced in `COMPARISONS.md`. In particular, the \(A\), \(B\), and \(C\) formulas there are exact for all stated \(p,q\).

**3. Strict extremality and the runner-up reduction.** Explicit subtraction shows that
\[
\Delta_A>\Delta_B,\qquad \Delta_A>\Delta_C,
\qquad \Delta_B>\max\{\Delta_D,\Delta_E,\Delta_F,\Delta_G\},
\]
where the last comparison with \(G\) is omitted when that orbit does not exist. These are **strict** for all permitted parameters. The positive-denominator polynomial comparisons, including expanded coefficient certificates after substituting \(u=p-3\ge0\), \(v=q-2\ge0\), are given in `COMPARISONS.md`. Thus \(A\) is always the unique maximizing orbit and second place can belong only to \(B\) or \(C\).

**4. The cubic integer boundary.** Define
\[
H=p^2+pq-2p-q=(p-2)p+(p-1)q>0.
\]
Exact subtraction gives
\[
\Delta_B-\Delta_C
=\frac{2\left[-q^2+(p^2(p-3)+2)q+p^2(p-2)^2\right]}
{(p-1)(N-2)H(H+2)}.
\]
The denominator is positive. The bracket is a concave quadratic in \(q\), with exactly one positive root since its constant term is positive and its leading coefficient is negative. At \(q=R_p\) it equals \(1\); at \(q=R_p+1\) it equals \(-p(p-1)(p-2)\). Since \(R_p\ge4\) for \(p\ge3\), the root lies strictly between those two consecutive integers, with the claimed signs at every integer \(q\ge2\). This proves the runner-up classification with no ties.

**5. Exact counts.** Type \(A\) chooses one vertex of \(Y\) and two of its \(p\) neighbors: \(q\binom p2\). Type \(B\) chooses one vertex of \(X\) and two vertices of \(Y\): \(p\binom q2\). Type \(C\) chooses two vertices from each class, and then one of their two cross-matchings: \(2\binom p2\binom q2\). These are distinct unordered edge pairs; no symmetry quotient is applied to the counts.

## Verification
The standalone file `verify.py` checks the seven symbolic orbit expressions, the strict-comparison polynomial certificates, and the integer transition identities using exact rational and polynomial arithmetic. It also constructs integer Laplacians independently and matches the direct inverse-based Kirchhoff-index increases with the rank-two formulas for 80 orbit-parameter cases (\(3\le p\le5\), \(2\le q\le5\)). Four small labelled families independently verify exhaustion of the stated seven structural orbits. Run `python verify.py` after installing `sympy` as specified in `requirements.txt`. The proof for unbounded \(p,q\) is analytical; these finite checks corroborate rather than replace it.

## Relationship to prior work
Yang (2014) studies Kirchhoff-index bounds in terms of independence and clique number and uses a complete split join in a fixed-independence extremal comparison. This motivates studying the fragility of the same network class, but its bounds do not determine the two-edge deletion ordering. Xu, Das and Zhang (2016) rank connected graphs and analyze deleting a bounded number of edges from a complete graph; their theorem subsumes certain special small-deletion patterns, including the worst-case \(q=2\) shape when their hypotheses hold, but not the stated all-parameter runner-up transition. General edge-defect formulas for complete-graph deletions (Tamura, 2026) imply computability of each fixed configuration, but do not themselves give the sharp complete-split failure ordering and cubic integer threshold.

Ge, Liao and Zhang (2024) study resistance distances and a Moon-type spanning-tree formula for weighted complete split graphs. Its title is directly relevant to the objects, but the complete article was not obtainable for comparison. The unresolved possibility of a specialized prior classification is explicitly retained as an originality limitation.

## Limitations
The theorem applies only to unit-conductance complete split graphs, **exactly two** simultaneously removed existing edges, integer \(p\ge3\), \(q\ge2\), and the Kirchhoff-index objective. It makes no claim for nonunit weights, more than two failures, disconnected post-failure graphs, or other network performance measures. A general rank-two formula is not by itself a novel result. The claimed contribution is the explicit nontrivial extremal classification and the sharp runner-up switching law. Independent mathematical assessment has not been performed, and a potentially relevant inaccessible paper leaves residual originality risk.

## References
1. Y. Yang, *Some Bounds for the Kirchhoff Index of Graphs*, Abstract and Applied Analysis (2014), Article 794781, first published 10 July 2014, DOI 10.1155/2014/794781. https://doi.org/10.1155/2014/794781
2. K. Xu, K. Ch. Das, X.-D. Zhang, *Ordering connected graphs by their Kirchhoff indices*, International Journal of Computer Mathematics (2016), arXiv:1602.07039 (first public preprint 21 February 2016). https://arxiv.org/abs/1602.07039
3. J. Ge, Y. Liao, B. Zhang, *Resistance distances and the Moon-type formula of a vertex-weighted complete split graph*, Discrete Applied Mathematics 359 (2024), 10–15, DOI 10.1016/j.dam.2024.07.040. https://doi.org/10.1016/j.dam.2024.07.040
4. S. Tamura, *Edge-defect matrices and stability of the Kirchhoff index for complete graphs with deleted edges*, arXiv:2608.05924 (2026). https://arxiv.org/abs/2608.05924
