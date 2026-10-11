# Clique joins suspend Lovász neighborhood complexes
## Finding
Let \(H\) be a finite nonempty simple graph with no isolated vertices, let \(r\ge 1\), and write \(K_r\vee H\) for the graph join. Then
\[
\mathcal N(K_r\vee H)\simeq\Sigma^r\mathcal N(H).
\]
In particular, for \(n,m\ge2\), define \(J_{r,n,m}=K_r\vee(nK_m)\). Then
\[
\mathcal N(J_{r,n,m})\simeq
\left(\bigvee^n S^{m+r-2}\right)\vee
\left(\bigvee^{n-1}S^r\right).
\]
For \(r=1,m=2\), this says that the friendship graph with \(n\) triangles has neighborhood complex \(\bigvee^{2n-1}S^1\).

## Assumptions and scope
The neighborhood complex \(\mathcal N(G)\) is the simplicial complex whose vertices are the non-isolated vertices of \(G\) and whose simplices are finite vertex sets having a common neighbor. Graphs here are finite and simple. The hypothesis that \(H\) has no isolated vertices keeps the vertex set of \(\mathcal N(H)\) equal to \(V(H)\) and is used in the exact complex decomposition below. The conclusion is a homotopy equivalence; no simple-homotopy equivalence is asserted.

## Proof
It is enough first to adjoin one universal vertex. Let \(c\) be the new vertex of \(C(H)=K_1\vee H\), put \(V=V(H)\), and let \(\Delta(V)\) be the full simplex on \(V\). A simplex of \(\mathcal N(C(H))\) with common neighbor \(c\) is precisely a face of \(\Delta(V)\). If its common neighbor is a vertex \(v\in V\), the simplex is contained in \(\{c\}\cup N_H(v)\), hence is a face of the simplicial cone \(c*\mathcal N(H)\). Conversely, every face of either of those two subcomplexes has the displayed common neighbor. Therefore there is an equality of simplicial complexes
\[
\mathcal N(C(H))=\Delta(V)\cup\bigl(c*\mathcal N(H)\bigr),
\qquad
\Delta(V)\cap\bigl(c*\mathcal N(H)\bigr)=\mathcal N(H).
\]
Both pieces are contractible, and their intersection inclusions are simplicial cofibrations. Hence this union is the homotopy pushout of two maps from \(\mathcal N(H)\) to contractible spaces. Replacing the two contractible targets by points gives the standard homotopy pushout model for the unreduced suspension, so
\[
\mathcal N(K_1\vee H)\simeq\Sigma\mathcal N(H).
\]
Now build \(K_r\vee H\) by adjoining \(r\) universal vertices successively. After the first step the graph has no isolated vertices, so the one-vertex argument iterates and gives
\[
\mathcal N(K_r\vee H)\simeq\Sigma^r\mathcal N(H).
\]

For the explicit family, a simplex of \(\mathcal N(nK_m)\) lies in a single component, while \(\mathcal N(K_m)=\partial\Delta^{m-1}\cong S^{m-2}\). Thus
\[
\mathcal N(nK_m)=\bigsqcup_{i=1}^n S^{m-2}.
\]
For nonempty spaces, \(\Sigma(X\sqcup Y)\simeq\Sigma X\vee\Sigma Y\vee S^1\). Applying this decomposition to the \(n\) components and then suspending \(r-1\) further times yields
\[
\Sigma^r\left(\bigsqcup_{i=1}^n S^{m-2}\right)
\simeq
\left(\bigvee^n S^{m+r-2}\right)\vee
\left(\bigvee^{n-1}S^r\right),
\]
as claimed.

## Verification
The proof above is symbolic and applies to every graph in the stated domain. The accompanying checker is only an independent finite consistency test, not a substitute for that proof. It reconstructs the neighborhood complex from the common-neighbor definition, verifies the exact one-universal-vertex decomposition on a cycle, a path, and a disconnected graph, and computes mod-two simplicial homology for ten members of the family \(K_r\vee(nK_m)\) with \(1\le r\le3\), \(2\le n\le3\), and \(2\le m\le4\). Its packaged replay prints `VERIFY_OK`.

## Relationship to prior work
Matsushita defines the neighborhood complex in the same common-neighbor form and studies its fundamental group; the paper's first public arXiv version is dated 2012-10-10 and its published metadata lists primary MSC 55Q05. The inspected paper does not state a universal-vertex, graph-join, or windmill suspension formula. Dochtermann develops structural properties of Hom complexes for categorical products, exponentials, coproducts, and graph foldings. Those operations do not imply the graph-join identity proved here. Focused searches under graph-cone, universal-vertex, graph-join, windmill, friendship-graph, and \(\operatorname{Hom}(K_2,-)\) formulations did not locate an equivalent or stronger statement. The strongest residual originality risk is that this elementary structural identity may exist as unindexed folklore or inside literature using box-complex terminology.

## Limitations
No claim is made for an original graph \(H\) with isolated vertices, for closed-neighborhood complexes, or for stronger equivariant or simple-homotopy equivalences. Finite computations in the checker cover only the listed examples and do not establish the all-parameter theorem; the proof does. The literature search cannot exclude an equivalent result hidden under terminology not indexed by the sources checked.

## References
1. T. Matsushita, *Fundamental Groups of Neighborhood Complexes*, arXiv:1210.2803v1, first posted 2012-10-10; J. Math. Sci. Univ. Tokyo 24 (2017), 321–353. Primary MSC 55Q05.
2. A. Dochtermann, *Hom complexes and homotopy theory in the category of graphs*, European J. Combin. 30 (2009), 490–509, DOI 10.1016/j.ejc.2008.04.009.
