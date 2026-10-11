# Exact Minkowski asymmetry and unique center of simplex-sum stellohedra

## Finding

For every integer \(k\ge 1\), label the vertices of the star \(K_{1,k}\) by a hub \(0\) and leaves \(1,\ldots,k\). Write \(\Delta_T=\operatorname{conv}\{e_i:i\in T\}\subset\mathbb R^{k+1}\). The translated standard simplex-sum realization of its graph associahedron is

\[
S_k=\sum_{\varnothing\ne A\subseteq[k]}\Delta_{\{0\}\cup A},
\qquad x(\{0,\ldots,k\})=2^k-1.
\]

Define Minkowski asymmetry for a full-dimensional convex body in its affine hull by

\[
s(K)=\min_{c,\,s\ge1}\{s:-(K-c)\subseteq s(K-c)\}.
\]

Then the exact asymmetry of this \(k\)-dimensional stellohedron is

\[
\boxed{s(S_k)=\frac{k2^{k-1}}{2^k-1}=\frac{k}{2-2^{1-k}}.}
\]

The minimizing Minkowski center is unique, and its coordinates are

\[
\boxed{c_1=\cdots=c_k=\frac{2^k-1}{k+2-2^{1-k}},\qquad
c_0=(2-2^{1-k})c_1.}
\]

In particular, \(s(S_1)=1\), \(s(S_2)=4/3\), \(s(S_3)=12/7\), and the exact dimension-dependent expansion is

\[
\boxed{s(S_k)=\frac{k}{2}+\frac{k}{2(2^k-1)},\qquad
\lim_{k\to\infty}\frac{s(S_k)}k=\frac12.}
\]

The location of the unique center is nonuniform for every \(k\ge2\): the hub coordinate is precisely \(2-2^{1-k}\) times each leaf coordinate. The claims concern the stated Minkowski-sum realization; they are affine-invariant under translations and invertible affine transformations, but not claims about all inequivalent realizations sharing the same face lattice.

## Assumptions and scope

All sums are ordinary Minkowski sums. The ambient affine hyperplane carries no preferred Euclidean metric because the invariant here is affine. For \(k=1\) there is a segment; for \(k\ge2\) the polytope has dimension \(k\), since it contains the full simplex \(\Delta_{\{0,\ldots,k\}}\) as a Minkowski summand. Every summand is a simplex that includes the hub and at least one leaf. Adding the omitted singleton simplices translates \(S_k\) by the all-ones vector, giving the customary sum over all connected vertex sets of the star; thus both conventions have the same asymmetry.

For \(T\subseteq\{0,\ldots,k\}\), write \(x(T)=\sum_{i\in T}x_i\), \(L(T)=\min_{x\in S_k}x(T)\), and \(U(T)=\max_{x\in S_k}x(T)\).

## Proof

**1. An exact subset-inequality description.** For a Minkowski sum \(P=\sum_{J\in\mathcal J}\Delta_J\), define \(z(T)=|\{J\in\mathcal J:J\subseteq T\}|\) (counting repeated summands). Then

\[
P=\{x:x(E)=|\mathcal J|,\quad x(T)\ge z(T)\text{ for all }T\subseteq E\}.
\]

To verify sufficiency without assuming a facet classification, take an arbitrary linear functional, order its coordinate weights nondecreasingly, and write it as a constant multiple of \(x(E)\) plus a nonnegative linear combination of tail-set sums. The displayed inequalities give the same lower support bound as the original Minkowski sum, because each simplex independently minimizes at a vertex of minimum weight. This holds for every linear functional, hence the two compact convex sets coincide. Upper subset bounds follow by complementation: \(U(T)=|\mathcal J|-L(E\setminus T)\).

For \(S_k\), let \(N=2^k-1\). If \(A\subseteq[k]\) contains \(a\) leaves and not the hub, no summand is wholly contained in \(A\), while precisely \(2^k-2^{k-a}\) summands intersect \(A\). Therefore

\[
L(A)=0,\qquad U(A)=F_k(a):=2^k-2^{k-a}\quad(0\le a\le k).
\]

The bounds for hub-containing sets are exactly the complementary bounds because every point has coordinate sum \(N\).

**2. Containment criterion.** Fix \(s\ge1\) and a proposed center \(c\) with \(c(E)=N\). The reflected-and-contracted map is \(R_{s,c}(x)=((s+1)c-x)/s\). Using the preceding complete subset description, \(R_{s,c}(S_k)\subseteq S_k\) if and only if, for every subset \(T\),

\[
sL(T)+U(T)\le(s+1)c(T)\le sU(T)+L(T).
\]

It suffices to check leaf-only subsets since taking complements exchanges the two bounds. For a leaf-only subset \(A\) of size \(a\), the criterion becomes

\[
F_k(a)\le(s+1)c(A)\le sF_k(a).
\]

**3. Sharp lower bound for every possible center.** Apply the left inequality to all \(k\) singletons. Since \(F_k(1)=2^{k-1}\),

\[
(s+1)\sum_{i=1}^kc_i\ge k2^{k-1}.
\]

Apply the right inequality to the complete leaf set \([k]\); since \(F_k(k)=2^k-1\),

\[
(s+1)\sum_{i=1}^kc_i\le s(2^k-1).
\]

Combining yields \(s\ge s_*:=k2^{k-1}/(2^k-1)\). At equality, every singleton lower bound must be an equality because the sum upper bound is sharp. Therefore every minimizing center, if it exists, must have

\[
c_i=\frac{2^{k-1}}{1+s_*}\quad(1\le i\le k),\qquad
c_0=N-\sum_{i=1}^kc_i.
\]

**4. Feasibility and uniqueness.** Set the coordinates as just displayed. The sequence \(F_k(a)\) is strictly concave in the integer variable \(a\): for \(1\le a\le k\), its increment is \(F_k(a)-F_k(a-1)=2^{k-a}\), decreasing with \(a\). Hence the averages \(F_k(a)/a\) decrease from \(2^{k-1}\) at \(a=1\) to \((2^k-1)/k\) at \(a=k\). In particular,

\[
F_k(a)\le a2^{k-1}= (1+s_*)c(A)
\le s_*F_k(a)
\]

for every nonempty leaf subset \(A\) of cardinality \(a\). The empty set is automatic. All complement inequalities therefore hold, and the containment criterion proves \(R_{s_*,c}(S_k)\subseteq S_k\). The lower bound is attained and the coordinate equalities from Step 3 force uniqueness. Substituting the formula for \(s_*\) gives the displayed center and asymptotic identities.

## Verification

The supplied standard-library verifier, `verify.py`, performs exact-rational subset inequalities for \(k=1,\ldots,6\), enumerates every coordinate-order greedy vertex for those dimensions, and checks every reflected greedy vertex against all subset bounds. It reports 5,912 greedy coordinate orders and 252 center subset tests, with all reflected subset checks passing. A separate numerical linear-programming formulation, with independent center variables and subset constraints, agreed with the exact optimum for \(k=2,\ldots,7\). Finite checks are supplementary; Steps 1–4 prove the statement for all integers \(k\ge1\).

Run `python verify.py` with Python 3.9 or later. No external Python dependencies are needed for the provided exact checks.

## Relationship to prior work

Padrol, Pilaud and Poullot describe the general simplex-sum graph-associahedron realization and its deformation cone, including stellohedra (arXiv:2109.09200, Theorem 2.2 and Section 2). Cardinal, Pournin and Valencia-Pabon examine graph-associahedron one-skeleton diameters and recover the stellohedron graph diameter as a special case of their complete-split-graph result (arXiv:2106.16130, Theorem 8). Neither inspected treatment asserts the affine Minkowski asymmetry of the displayed realization or its minimizing center.

Generic convex-body symmetry and linear-programming methods explain how to compute asymmetry from a finite inequality system, but do not themselves provide the stated closed formula or uniqueness proof. The earlier Euclidean inradius of this same realization is a distinct, metric-dependent invariant and neither implies nor is implied by the reflection-containment factor calculated here. The two-inequality lower certificate and whole-family matching construction are the additional statements assessed here.

## Limitations

The result concerns the specified unweighted simplex-sum realization, up to affine equivalence. Other graph-associahedron realizations can have the same face lattice but different affine asymmetry. The proof does not classify weighted simplex sums, arbitrary graph associahedra, or Minkowski centers of those families. The literature comparison cannot rule out earlier equivalent statements formulated under alternate terminology; an independent literature audit has not been performed.

## References

1. A. Padrol, V. Pilaud and G. Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200, first posted September 19, 2021; specifically the introduction, Theorem 2.2 and Section 2 on simplex-sum realizations.
2. J. Cardinal, L. Pournin and M. Valencia-Pabon, *Diameter estimates for graph associahedra*, arXiv:2106.16130, first posted June 30, 2021; specifically the introduction, star examples and Theorem 8 on one-skeleton diameter.
3. A. Postnikov, *Permutohedra, associahedra, and beyond*, International Mathematics Research Notices (2009), the generalized-permutahedron and building-set foundations cited by the above works.
