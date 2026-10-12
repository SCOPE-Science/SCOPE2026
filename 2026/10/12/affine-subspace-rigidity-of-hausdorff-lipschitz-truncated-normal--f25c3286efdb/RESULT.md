# Affine-subspace rigidity of Hausdorff-Lipschitz truncated normal cones
## Finding

Let \(C\subset\mathbb R^p\) be a nonempty closed convex set and fix \(r>0\). For \(y\in C\), define
\[
T_r(y)=N_C(y)\cap B_r,
\]
where \(N_C(y)\) is the convex normal cone and \(B_r\) is the closed Euclidean ball of radius \(r\) centered at the origin.

Then the following are equivalent:

1. \(T_r\) is Hausdorff-Lipschitz on \(C\).
2. \(T_r\) is Hausdorff-continuous on \(C\).
3. \(C\) is an affine subspace.

In fact, if \(C\) is not affine, then at every relative-boundary point \(\bar y\in\operatorname{relbd}C\) there is a sequence \(y_k\in\operatorname{ri}C\) with \(y_k\to\bar y\) such that
\[
d_H\!\left(T_r(\bar y),T_r(y_k)\right)\ge r
\]
for every \(k\). Thus the discontinuity has a fixed jump of at least \(r\), independent of how close \(y_k\) is to \(\bar y\).

This gives a complete convex-set classification of the general-set normal truncation used in equation (3) of the recent inexact linearized ADMM analysis. Under that form of the normal mapping, the paper's Hausdorff-Lipschitz Assumption 2 holds for a closed convex constraint set exactly when the set is affine. Therefore intervals, boxes, bounded polyhedra, Euclidean balls, simplices, and every other non-affine closed convex set violate that assumption.

The result concerns the paper's general-set form (3). Its separate manifold form (4), which bounds multiplier vectors before applying a smooth constraint Jacobian, is a different set-valued map and is not ruled out by this theorem.

## Assumptions and scope

The set \(C\) is nonempty, closed, and convex in finite-dimensional Euclidean space. No full dimensionality, smoothness, compactness, polyhedrality, or nonempty ambient interior is assumed.

Let
\[
A=\operatorname{aff}C=a+L,
\]
where \(L\) is the direction space of the affine hull. Relative interior and relative boundary are always taken with respect to \(A\).

The normal cone is the standard convex-analysis normal cone
\[
N_C(y)=\{u\in\mathbb R^p:\langle u,z-y\rangle\le0\ \text{for all }z\in C\}.
\]
For a closed convex set this agrees with the limiting normal cone used in the source.

The theorem does not address arbitrary nonconvex sets. It also does not identify form (4) with form (3): for a smooth equality manifold, the source uses a bounded multiplier ball in form (4), rather than intersecting the ambient normal cone itself with \(B_r\).

## Proof

Assume first that \(C\) is an affine subspace. Write
\[
C=a+L.
\]
Then for every \(y\in C\),
\[
N_C(y)=L^\perp.
\]
Hence
\[
T_r(y)=L^\perp\cap B_r
\]
is independent of \(y\). The map is therefore Hausdorff-Lipschitz with exact modulus \(0\).

Conversely, suppose that \(C\) is not affine. Then
\[
C\ne\operatorname{aff}C,
\]
so \(\operatorname{relbd}C\) is nonempty. Fix
\[
\bar y\in\operatorname{relbd}C.
\]

By the supporting-hyperplane theorem applied inside the affine hull \(a+L\), there exists a nonzero vector \(u\in L\) such that
\[
\langle u,z-\bar y\rangle\le0
\]
for every \(z\in C\). Normalize \(u\) so that
\[
\|u\|=1.
\]
Then
\[
u\in N_C(\bar y),
\]
and therefore
\[
ru\in T_r(\bar y).
\]

Relative interior is dense in a nonempty convex set, so choose any sequence
\[
y_k\in\operatorname{ri}C,
\qquad
y_k\to\bar y.
\]
At every relative-interior point,
\[
N_C(y_k)=L^\perp.
\]
Indeed, all feasible first-order directions inside \(L\) occur locally in both signs, so a normal vector can have no component in \(L\), while every vector in \(L^\perp\) is automatically normal to the whole affine hull.

Consequently,
\[
T_r(y_k)=L^\perp\cap B_r.
\]
Because \(u\in L\) and \(L\perp L^\perp\),
\[
\operatorname{dist}\!\left(ru,L^\perp\cap B_r\right)=r.
\]
Since \(ru\in T_r(\bar y)\), the definition of Hausdorff distance gives
\[
d_H\!\left(T_r(\bar y),T_r(y_k)\right)\ge r
\]
for every \(k\).

But
\[
\|y_k-\bar y\|\to0.
\]
Therefore \(T_r\) is not Hausdorff-continuous at \(\bar y\), and a fortiori cannot satisfy any finite Hausdorff-Lipschitz bound on \(C\).

This proves all three equivalences and the quantitative jump statement.

For the application to the recent ADMM analysis, its equation (3) is precisely the map
\[
y\longmapsto N_Y(y)\cap B_r
\]
for a general closed set \(Y\), and Assumption 2 requires a global Hausdorff-Lipschitz estimate for that map. Specializing to closed convex \(Y\) and applying the theorem shows that form (3) satisfies Assumption 2 exactly for affine subspaces.

## Verification

The proof is analytic and does not depend on finite enumeration or numerical experimentation.

The standalone script `artifacts/verify_boundary_examples.py` checks three canonical exact examples:

- the interval \([0,1]\), whose truncated normal cone jumps by exactly \(r\) between any interior point and the endpoint \(0\);
- the Euclidean unit disk, whose truncated normal cone jumps by exactly \(r\) from interior points to a boundary point;
- an affine line in \(\mathbb R^2\), whose truncated normal cone is constant.

These examples are consistency checks only. The arbitrary-dimensional theorem follows from the affine-hull and supporting-hyperplane argument above.

## Relationship to prior work

El Bourkhissi and Necoara introduce two bounded normal mappings. Their general-set form (3) truncates the normal cone directly,
\[
N_Y(y)\cap B_r,
\]
and their Assumption 2 requires this map to be globally Lipschitz in Hausdorff distance. They separately introduce form (4) for smooth equality manifolds by bounding the multiplier vector before applying the Jacobian. Their Lemma 2 gives positive examples, including affine subspaces and spheres, but does not characterize which convex sets satisfy form (3). The paper also explicitly notes that its \(Y\)-projection subproblem is strongly convex when \(Y\) is convex.

Recent work of Ma and Sun studies local Aubin properties and strong regularity for generalized equations involving normal cone maps over broad convex sets. That theory concerns localized solution mappings and uses only the standard outer semicontinuity of the convex normal cone; it does not assert symmetric Hausdorff continuity of the entire bounded normal-cone value \(N_C(y)\cap B_r\).

Thinh, Qin, and Yao study coderivatives and the Aubin property relative to a set for normal-cone mappings to polyhedra. Their discussion explicitly distinguishes interior points, where the normal cone can collapse to zero in the full-dimensional case, from boundary points. Their Aubin property is a localized graphical inclusion around a selected graph point, not the global symmetric Hausdorff-Lipschitz condition imposed on the full truncated values here.

Targeted searches for Hausdorff continuity, truncated normal cones, affine-subspace characterizations, normal-cone Aubin properties, and the primary paper's Assumption 2 did not locate a published statement that gives the exact equivalence above or applies it to the source convergence hypothesis.

## Limitations

The classification is specific to the direct truncation
\[
N_C(y)\cap B_r
\]
with a fixed positive radius. It does not say that normal-cone based algorithms cannot handle non-affine convex constraints; standard projection, resolvent, and localized graphical regularity theories do handle such sets under different hypotheses.

The result does not invalidate a convergence theorem conditional on Assumption 2. It identifies the exact convex-set scope of one of the two normal-map constructions allowed by that assumption.

The proof uses standard convex-geometric facts about relative interiors and supporting hyperplanes. Its value is the complete scope classification and its direct consequence for the recent algorithmic hypothesis, not the introduction of a new normal-cone definition.

## References

1. L. El Bourkhissi, I. Necoara, *Convergence rates for an inexact linearized ADMM for nonsmooth nonconvex optimization with nonlinear equality constraints*, Computational Optimization and Applications 93, 689--727, 2026. DOI: 10.1007/s10589-025-00737-1. Earliest public preprint: arXiv:2503.01060v1, 2 March 2025.
2. J. Ma, D. Sun, *The Aubin Property for Generalized Equations over \(C^2\)-cone Reducible Sets*, arXiv:2509.14194v5, 2026.
3. V. D. Thinh, X. Qin, J.-C. Yao, *Coderivatives with respect to a set of the normal cone mappings and their applications*, arXiv:2312.15834v1, 2023.
