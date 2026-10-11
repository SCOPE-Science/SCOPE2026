# Minkowski centers of complete-graph spanning-tree polytopes and the exceptional six-vertex cut

## Finding
For every integer \(n\ge 3\), let \(E\) be the edge set of the complete graph \(K_n\), and write \(P_n\subset\mathbb R^E\) for the convex hull of the incidence vectors of its spanning trees. Define the Minkowski asymmetry \(s(P)=\min_{c\in P}\min\{r\ge1: -(P-c)\subseteq r(P-c)\}\). Then
\[
s(P_n)=n-1.
\]
The full set \(\mathcal M(P_n)\) of minimizing centers is exactly the set of vectors
\[
 c_e=\frac{1+z_e}{n}\quad(e\in E),
\]
where \(z\) is a nonnegative weighting of \(K_n\) whose weighted degree at every vertex is \(n-1\). For \(n\ge4\), the only further conditions are
\[
 0\le z_e\le n-2\quad(e\in E),
\]
**except when \(n=6\)**: in that case the additional conditions
\[
 z(\delta(S))\ge1\qquad(S\subseteq[n],\ |S|=3)
\]
are necessary and sufficient. Here \(\delta(S)\) denotes the edges with precisely one endpoint in \(S\), and \(z(F)=\sum_{e\in F}z_e\). For \(n=3\) the center is uniquely \(c_e=2/3\) for each of the three edges. For all \(n\ge3\),
\[
 \dim\operatorname{aff}\mathcal M(P_n)=\binom n2-n=\frac{n(n-3)}2.
\]
In particular, \(n=4\) gives a two-dimensional hexagonal minimizing-center locus. The six-vertex exceptional cut is essential, whereas the corresponding cut constraints for \(n\ge7\) follow from nonnegativity alone.

## Assumptions and scope
All graphs are finite, simple, complete, and undirected. The ambient norm is irrelevant to Minkowski asymmetry because the containment definition is affine-invariant. All polytopes and their centers are understood in the affine hull \(x(E)=n-1\). The center parameter \(c\) is required to belong to \(P_n\); this follows automatically from the displayed minimum-asymmetry inequalities. The statement covers every integer \(n\ge3\), without numerical cutoff, and addresses ordinary Minkowski asymmetry rather than Euclidean circumradius or John ellipsoids.

The standard spanning-tree/graphic-matroid base-polytope theorem states
\[
P_n=\{x\in\mathbb R^E:\ x(E)=n-1,\ x_e\ge0\ (e\in E),\ x(E(S))\le |S|-1\ (\varnothing\ne S\subsetneq[n])\},
\]
where \(E(S)\) consists of edges with both endpoints in \(S\). Subsets of size one contribute only trivial upper inequalities.

## Proof
**1. Convert reflection containment into sharp linear inequalities.** For \(r\ge1\), inclusion \(-(P_n-c)\subseteq r(P_n-c)\) is equivalent to membership
\[
 y=\frac{(r+1)c-x}{r}\in P_n\quad\text{for every }x\in P_n.
\]
Every spanning tree has exactly \(n-1\) edges, so the affine-sum equality holds automatically when \(c(E)=n-1\). For every edge \(e\), the maximum of \(x_e\) over spanning trees is \(1\). For every proper nonempty vertex set \(S\), the minimum of \(x(E(S))\) is \(0\): take a star centered outside \(S\). Consequently the displayed spanning-tree inequalities for all \(y\) are **equivalent**, without loss of quantifiers, to
\[
 (r+1)c_e\ge1\quad(e\in E),\qquad
 (r+1)c(E(S))\le r(|S|-1)\quad(2\le |S|\le n-1),
\]
together with \(c(E)=n-1\). Conversely these inequalities imply the membership of every reflected point \(y\) in \(P_n\). They also imply \(c\in P_n\) when \(r\ge1\), because they give \(c\ge0\), and the upper bounds on \(c(E(S))\) are no larger than the original ones.

**2. Optimal asymmetry and forced vertex degrees.** Set \(S=[n]\setminus\{v\}\) in the second inequality. Summing the resulting \(n\) bounds gives
\[
 (n-2)(n-1)\le \frac{nr}{r+1}(n-2),
\]
because each edge lies in exactly \(n-2\) of the co-singleton induced edge sets, and \(c(E)=n-1\). Since \(n\ge3\), this forces \(r\ge n-1\). At \(r=n-1\), the uniform vector \(c_e=2/n\) obeys the edge bounds and all subset bounds: for \(s=|S|\), one has \(c(E(S))=s(s-1)/n\le(n-1)(s-1)/n\). Therefore \(s(P_n)=n-1\).

At this minimum, equality in the sum of the co-singleton bounds forces equality in **each** such bound. Hence every minimizing center satisfies
\[
 c(\delta(v))=\frac{2(n-1)}n\qquad(v\in[n]).
\]
Putting \(z_e=nc_e-1\), the edge bounds say \(z_e\ge0\), and the vertex-degree equalities say \(z(\delta(v))=n-1\). Conversely those degree equalities imply the affine-sum equality \(c(E)=n-1\).

**3. Exact cut constraints.** Fix a subset \(S\) of cardinality \(s\). In the \(z\)-coordinates, the upper induced-edge inequality at \(r=n-1\) says
\[
 z(E(S))\le(n-1)(s-1)-\binom{s}{2}.
\]
Since \(z\) is \((n-1)\)-regular, the exact double-counting identity
\[
 z(\delta(S))=s(n-1)-2z(E(S))
\]
turns this into
\[
 z(\delta(S))\ge F_n(s),\qquad F_n(s)=s^2-ns+2n-2.
\]
This is a necessary-and-sufficient reformulation for all proper \(S\) with \(s\ge2\). For \(s=n-1\), both sides equal \(n-1\), so the constraint is automatic. For \(s=2\), the cut inequality is equivalent to \(z_e\le n-2\) on the single induced edge. The \(s=n-2\) case is the identical two-edge-complement constraint. For \(n=4,5\), there are no further nonautomatic subset sizes. For \(n=6\), only \(s=3\) remains, with \(F_6(3)=1\).

For \(n\ge7\) and \(3\le s\le n-3\), the convex quadratic \(F_n(s)\) has its maximum on that integer interval at an endpoint, giving
\[
 F_n(s)\le F_n(3)=F_n(n-3)=7-n\le0.
\]
Because \(z\ge0\), each such cut is automatic. The advertised classifications follow; for \(n=3\) the degree equations alone determine \(z_e=1\), hence \(c_e=2/3\).

**4. Affine dimension.** For every \(n\ge4\), the uniform weighting \(z_e=1\) is strictly positive and lies strictly below each edge cap \(n-2\). In the exceptional \(n=6\) case, each three-vertex cut has uniform weight \(9>1\); therefore it too is strict. The only equations in the affine hull of the center locus are the \(n\) weighted-degree equalities. They are linearly independent for \(n\ge3\): if \(\lambda_u+\lambda_v=0\) on every edge, applying this to any triangle gives three zero coefficients, and completeness gives all remaining coefficients zero. The incidence matrix thus has row rank \(n\), and \(\dim\operatorname{aff}\mathcal M(P_n)=\binom n2-n\). When \(n=3\), this is zero and the unique center computed above realizes it.

**5. Sharpness of the exceptional cut.** For \(n=6\), partition the vertices into two triples and put weight \(5/2\) on the edges internal to each triple, zero elsewhere. Every vertex has weighted degree \(5\), and every edge respects the cap \(4\), yet the cut of either triple has weight zero, violating its required lower bound \(1\). To see failure in the original polytope, take a spanning star rooted outside one triple. Its reflected point at \(r=5\) has induced-edge total \(21/10>2\) on that triple, violating the spanning-tree inequality. In contrast, for \(n=7\), split the vertices into groups of three and four, put weights \(3\) and \(2\), respectively, on their internal edges and zero on cross edges. Each vertex has weighted degree \(6\), every edge is below cap \(5\), and by the previous proof this weighting is a minimizing center despite its zero triple cut. Thus the cutoff at six vertices is sharp.

## Verification
The accompanying `verify.py` is a standalone Python standard-library checker. It enumerates all \(n^{n-2}\) labeled spanning trees for each \(n=3,4,5,6,7\) using Prüfer sequences. For uniform centers, and for a degree-preserving four-cycle perturbation whenever \(n\ge4\), it checks **every** reflected tree against **every** nontrivial spanning-tree subset inequality using integer arithmetic. This yields \(36{,}491\) reflected trees and \(4{,}151{,}797\) subset-inequality checks. It additionally verifies the exact six-vertex obstruction, the seven-vertex disconnected center, the stated quadratic cutoff for \(7\le n\le199\), and unsigned incidence rank for \(3\le n\le10\) using exact rational elimination. It prints `VERIFICATION_OK` on success. These finite calculations are corroboration only; all-\(n\) claims follow from the proof above.

## Relationship to prior work
Pineda-Villavicencio and Schröter study reconstructibility, basis exchange, and combinatorial structure of matroid base polytopes, including graphic matroids; they do not establish Minkowski center loci or the graph-cut transition obtained here. Chaourar investigates facets of spanning-tree polytopes and their graphical interpretation, underpinning the known polyhedral inequalities used as a starting point. The classical spanning-tree inequalities and the general notion of Minkowski asymmetry are prior knowledge, **not** new contributions. The new claim is the **complete minimizing-center locus for the complete-graph spanning-tree polytope**, the exact affine dimension, and the essential six-vertex triple-cut boundary. This differs from Minkowski centers of a matroid *independence polytope*: passing to a fixed-rank base face does not preserve minimizing centers.

## Limitations
The theorem is restricted to complete graphs, not arbitrary graphical matroids or arbitrary edge-weighted spanning-tree polytopes. It concerns affine Minkowski asymmetry, not Euclidean John ellipsoids, volumes, or stability under perturbations. The comparison with accessible literature and indexed mathematical records supports a tentative originality assessment but does not constitute independent priority certification; equivalent prior formulations under other geometric or optimization terminology remain a residual risk. All finite computations are tests, not proofs of infinite statements. No independent audit has been performed.

## References
1. G. Pineda-Villavicencio and B. Schröter, *Reconstructibility of matroid polytopes*, arXiv:2010.10227, first public preprint 2020-10-20; SIAM Journal on Discrete Mathematics 36 (2022), 490–508. Primary MSC2020: 52B11. https://arxiv.org/abs/2010.10227
2. B. Chaourar, *The facets of the spanning trees polytope*, arXiv:1903.07292 (first publicly available 2019-03-18), https://arxiv.org/abs/1903.07292
3. Classical graphic-matroid base-polytope / spanning-tree inequalities due to Edmonds, as discussed in the references above.
