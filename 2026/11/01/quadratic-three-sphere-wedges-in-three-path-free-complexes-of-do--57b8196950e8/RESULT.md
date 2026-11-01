# Quadratic three-sphere wedges in three-path-free complexes of double brooms

## Finding

For integers \(a,c\ge 1\), let \(B_{a,c}\) be the tree with a four-vertex spine \(u-v-w-z\), with exactly \(a\) extra leaves adjacent to \(u\) and exactly \(c\) extra leaves adjacent to \(z\), and no additional edges. Let \(\operatorname{Ind}_2(G)\) denote the simplicial complex of vertex subsets inducing connected components of at most two vertices. Then there is an integral homotopy equivalence
\[
\boxed{\operatorname{Ind}_2(B_{a,c})\simeq\bigvee^{ac-1}S^3.}
\]
In particular the complex is contractible precisely when \(a=c=1\); otherwise its only nonzero reduced integral homology is \(\widetilde H_3\cong\mathbb Z^{ac-1}\). The wedge multiplicity depends quadratically on the sizes of the two leaf classes. For example, \(\operatorname{Ind}_2(B_{2,2})\simeq\bigvee^3S^3\) and \(\operatorname{Ind}_2(B_{3,3})\simeq\bigvee^8S^3\).

## Assumptions and scope

Every graph is finite, simple and undirected. The selected spine vertices are four **distinct** vertices. The sets of pendant leaves \(A=\{a_1,\ldots,a_a\}\) and \(C=\{c_1,\ldots,c_c\}\) are disjoint from one another and the spine. The parameter \(2\) is fixed: this is the three-path-free complex, since for a tree an induced component has at least three vertices if and only if its selected vertex set contains a path on three vertices. The notation \(\bigvee^0S^3\) means a point (contractibility), not an empty simplicial complex. There is no restriction on the parity or relative sizes of \(a,c\).

Write \(\Delta_J\) for the full simplex on vertex set \(J\), \(\operatorname{skel}_0\Delta_J\) for its zero-skeleton, and \(K*L\) for simplicial join. Standard geometric realizations and their homotopy types are understood.

## Proof

**1. The star calculation.** Let \(S_k\), for \(k\ge1\), be a star with central vertex \(x\) and leaf set \(J\) of cardinality \(k\). Directly from the definition,
\[
\operatorname{Ind}_2(S_k)=\Delta_J\ \cup\ \bigl(x*\operatorname{skel}_0\Delta_J\bigr),
\qquad
\Delta_J\cap \bigl(x*\operatorname{skel}_0\Delta_J\bigr)=\operatorname{skel}_0\Delta_J.
\]
Each of the two pieces is contractible and the intersection consists of \(k\) isolated vertices. The homotopy-pushout (equivalently, the graph obtained by collapsing the two contractible pieces) gives
\[
\operatorname{Ind}_2(S_k)\simeq\bigvee^{k-1}S^1.
\]
This includes \(k=1\), when the complex is a simplex and is contractible.

**2. Delete the left inner spine vertex.** Set \(K=\operatorname{Ind}_2(B_{a,c})\) and \(D=K\setminus v\). Deleting \(v\) from the tree leaves the two disjoint stars \(S_a\) centered at \(u\) and \(S_{c+1}\) centered at \(z\), the latter having \(w\) as its additional leaf. The higher-independence construction sends disjoint unions of graphs to joins, so
\[
D=\operatorname{Ind}_2(S_a)*\operatorname{Ind}_2(S_{c+1})
\simeq\bigvee^{(a-1)c}S^3.
\]
Indeed, the join of connected circle wedges is a suspension of their smash product, hence a wedge of three-spheres. If \(a=1\), the first factor is contractible and so is \(D\). In all cases \(D\) is connected and \(\pi_2(D)=0\).

**3. Compute the link exactly.** Let \(L=\operatorname{lk}_K(v)\). An allowed face of the link cannot contain any of the pairs \(\{u,a_i\}\), \(\{u,w\}\), or \(\{w,z\}\), because each pair together with \(v\) would complete a forbidden three-vertex path. All other forbidden triples are already handled by membership in \(D\).

Define the complexes on the right leaf class
\[
Q=\Delta_{\{w\}\cup C}\ \cup\ \bigl(z*\operatorname{skel}_0\Delta_C\bigr),
\qquad
R=\Delta_C\ \cup\ \bigl(z*\operatorname{skel}_0\Delta_C\bigr)
=\operatorname{Ind}_2(S_c).
\]
If \(u\) is absent, all leaves in \(A\) are free and the remaining allowable faces form \(Q\); if \(u\) is present, both \(w\) and all the \(A\)-leaves must be absent, leaving exactly \(R\). Thus, as **equalities of subcomplexes**,
\[
L=(\Delta_A*Q)\ \cup\ (u*R),
\qquad
(\Delta_A*Q)\cap(u*R)=R.
\]
The nonempty \(A\) makes \(\Delta_A*Q\) a cone, and \(u*R\) is another cone. The two inclusions of \(R\) are simplicial cofibrations. Their homotopy pushout is the suspension of \(R\); by step 1,
\[
L\simeq\Sigma R\simeq\bigvee^{c-1}S^2.
\]
For \(c=1\), this says \(L\) is contractible, which also follows directly from the union-of-cones description.

**4. Split the attaching map.** The standard deletion-link decomposition is
\[
K=D\ \cup_L\ (v*L),
\]
with the second term a cone. The attaching inclusion \(L\to D\) is nullhomotopic because \(L\) is a wedge of two-spheres or contractible, whereas \(D\) is a wedge of three-spheres or contractible and hence is two-connected. The homotopy cofiber therefore splits:
\[
K\simeq D\vee\Sigma L
\simeq \bigvee^{(a-1)c}S^3\vee\bigvee^{c-1}S^3
\simeq\bigvee^{ac-1}S^3.
\]
This proof is integral and works uniformly for every \(a,c\ge1\). In particular, no finite enumeration or field-coefficient calculation is used to conclude the homotopy equivalence. \(\square\)

## Verification

The standalone standard-library program `verify.py` generates the graph independently from its edge list and enumerates forbidden three-vertex paths. It constructs all faces of the original complex, its deletion at \(v\), and its link at \(v\); computes exact mod-two boundary ranks; and checks reduced Euler characteristics. The checked values agree with \(\widetilde\beta_3(K)=ac-1\), \(\widetilde\beta_3(D)=(a-1)c\), and \(\widetilde\beta_2(L)=c-1\) for 21 parameter pairs including the complete grid \(1\le a,c\le4\). These are reproducible finite consistency checks, **not** a proof for arbitrary parameters or a substitute for integral attaching-map control, which is supplied above.

Run with `python3 verify.py` from a directory containing the provided file; no third-party libraries are needed.

## Relationship to prior work

Sawant [1], first publicly available on 2026-05-24, establishes vertex decomposability of all higher-independence complexes of trees and identifies three-path-free complexes with the \(r=2\) case. That general result guarantees shellability but does not determine the sphere dimension and multiplicity for these double brooms. The earlier work of Abdelmalek and collaborators [2] establishes vertex decomposability for caterpillar graphs, again without this exact homotopy count. Deshpande and Singh [3] give exact homotopy types for fully whiskered graphs, paths, cycles, complete multipartite graphs, and perfect-branching trees. The present trees have two nonleaf spine vertices \(v,w\) without pendant neighbors and therefore are **not fully whiskered**; the case \(a=c=1\) is already a path and is not claimed as novel in isolation. The new result is the uniform two-parameter formula and its null-attaching-map proof.

## Limitations

Only the fixed threshold \(r=2\) and the length-four spine with leaves at both endpoints are treated. Nothing here claims exact homotopy types for arbitrary trees or other thresholds, or describes equivariant homology representations of the leaf-permutation action. Similar formulas may occur in unindexed literature; the literature comparison is necessarily non-exhaustive. The finite checker verifies mod-two homology for specified small parameters, not integral homotopy or infinitely many cases. Independent validation has not been performed.

## References

[1] R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1 (first public 2026-05-24). https://arxiv.org/abs/2605.25150

[2] F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (2021). https://arxiv.org/abs/2106.10863

[3] P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (2020). https://arxiv.org/abs/2001.05448
