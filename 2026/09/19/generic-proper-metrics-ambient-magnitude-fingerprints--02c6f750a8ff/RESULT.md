# Generic proper algebraically independent metrics have ambiently unique magnitude fingerprints

## Statement

Let \(X\) be a strongly zero-dimensional locally compact Polish space, and let
\(\operatorname{Met}_{\mathrm{pr}}(X)\) denote its proper compatible metrics, equipped with the
uniform topology induced by
\[
D_X(d,e)=\sup_{x,y\in X}|d(x,y)-e(x,y)|.
\]
Let \(\mathcal A(X)\) be the compatible metrics whose positive distances, indexed by
distinct unordered pairs \(\{x,y\}\), are algebraically independent over \(\mathbb Q\).

Then
\[
\boxed{\mathcal A(X)\cap\operatorname{Met}_{\mathrm{pr}}(X)
\text{ is a dense }G_\delta\text{ subset of }\operatorname{Met}_{\mathrm{pr}}(X).}
\]

Moreover, every \(d\in\mathcal A(X)\) has the following ambient hereditary rigidity
property. If \(A\subset X\) has at least three points and
\(f:A\to X\) is distance-preserving, then
\[
\boxed{f(x)=x\quad\text{for every }x\in A.}
\]
For a two-point set, every distance-preserving image is the same unordered pair
(the two points may be interchanged).

Consequently, for every \(d\in\mathcal A(X)\):

1. the multiset of pairwise distances of any finite subset \(F\subset X\), \(|F|\ge2\),
   determines \(F\) as an actual subset of the ambient space, not merely up to
   abstract isometry;
2. the magnitude function of \(F\) determines \(F\) as an actual ambient subset;
   equivalently, if finite \(A,B\subset X\) with \(|A|,|B|\ge2\) have the same
   magnitude function (on a common sufficiently-large-scale tail), then \(A=B\).

Thus a generic proper compatible metric on such an \(X\) gives every nontrivial finite
point cloud an ambiently unique magnitude fingerprint.

## Context

Ishiki introduced \(\mathcal A(X)\) and proved two results used here:

- on every strongly zero-dimensional metrizable \(X\) of cardinality at most the
  continuum, every compatible metric can be uniformly approximated by a member of
  \(\mathcal A(X)\);
- for every \(\sigma\)-compact metrizable \(X\), \(\mathcal A(X)\) is \(G_\delta\) in
  \(\operatorname{Met}(X)\), and is dense when \(X\) is strongly zero-dimensional.

The same paper separately proves that rigid proper metrics are relatively \(G_\delta\)
among proper metrics on locally compact Polish spaces. It does not state the stronger
genericity of *algebraically independent proper* metrics.

Ishiki also observes, using O'Hara's theorem, that every finite subspace of a metric in
\(\mathcal A(X)\) is reconstructible from its magnitude function up to isometry.
O'Hara's theorem says that a finite metric space whose edge lengths are rationally
independent is determined by its magnitude function. The contribution here is the
proper-metric transfer and the upgrade from abstract finite-space reconstruction to
ambient reconstruction simultaneously for all finite subsets.

## Proof

### 1. Properness is invariant under finite uniform perturbation

Suppose \(d,e\in\operatorname{Met}(X)\) and
\[
D_X(d,e)\le C<\infty.
\]
If \(d\) is proper, then \(e\) is proper.

Indeed, for every \(x\in X\) and \(R>0\),
\[
\overline B_e(x,R)\subseteq \overline B_d(x,R+C).
\]
The set on the right is compact. Because \(d\) and \(e\) induce the same topology,
\(\overline B_e(x,R)\) is closed in \(X\), hence is a closed subset of that compact
\(d\)-ball and is compact.

By symmetry, properness is constant on every finite-\(D_X\) equivalence class
\[
[d]_{\mathrm{bd}}=\{e\in\operatorname{Met}(X):D_X(d,e)<\infty\}.
\]
Since the uniform topology is induced by \(\min\{1,D_X\}\), each such class is clopen.
Therefore \(\operatorname{Met}_{\mathrm{pr}}(X)\) itself is a union of clopen
finite-\(D_X\) classes.

### 2. Algebraically independent proper metrics are generic

A locally compact Polish space is \(\sigma\)-compact. Hence Ishiki's \(G_\delta\)
theorem gives that \(\mathcal A(X)\) is \(G_\delta\) in \(\operatorname{Met}(X)\).

Fix \(d\in\operatorname{Met}_{\mathrm{pr}}(X)\) and \(\varepsilon>0\). Ishiki's
approximation theorem gives \(e\in\mathcal A(X)\) with
\[
D_X(d,e)<\varepsilon.
\]
The preceding lemma makes \(e\) proper. Thus
\(\mathcal A(X)\cap\operatorname{Met}_{\mathrm{pr}}(X)\) is dense in the proper-metric
subspace. Its relative \(G_\delta\) property follows by intersection. This proves the
first boxed assertion.

The same argument shows a slightly more local statement: inside every finite-\(D_X\)
component of \(\operatorname{Met}(X)\), algebraically independent metrics form a dense
\(G_\delta\).

### 3. Algebraic independence forces ambient hereditary rigidity

For \(d\in\mathcal A(X)\), two distinct unordered pairs cannot have the same distance:
otherwise
\[
T_1-T_2=0
\]
would be a nonzero rational polynomial relation between two distinct positive distances.
Hence
\[
\{x,y\}\longmapsto d(x,y)
\]
is injective on \([X]^2\).

Let \(A\subset X\), \(|A|\ge3\), and let \(f:A\to X\) preserve all distances.
For distinct \(x,y\in A\),
\[
d(x,y)=d(f(x),f(y))
\]
forces
\[
\{f(x),f(y)\}=\{x,y\}.
\]
Choose distinct \(y,z\in A\setminus\{x\}\). Then
\[
\{f(x)\}
=
\{f(x),f(y)\}\cap\{f(x),f(z)\}
=
\{x,y\}\cap\{x,z\}
=
\{x\}.
\]
So \(f(x)=x\). Since \(x\) was arbitrary, \(f\) is the inclusion.

If \(A=\{x,y\}\), the same pair-injectivity gives
\(\{f(x),f(y)\}=\{x,y\}\), proving setwise rigidity.

### 4. The distance multiset already determines the ambient finite subset

Let finite \(A,B\subset X\) have at least two points and suppose their multisets of
pairwise distances agree. Pair-injectivity converts equality of distance values into
equality of the corresponding unordered ambient pairs. Hence
\[
[A]^2=[B]^2.
\]
The vertex set of the complete graph \([A]^2\) is \(A\), and similarly for \(B\), so
\(A=B\).

### 5. Magnitude becomes an ambient fingerprint

For a nonempty finite metric space \(F\), write
\[
Z_F(t)=\bigl(e^{-t d(x,y)}\bigr)_{x,y\in F},
\qquad
M_F(t)=\sum_{x,y\in F}(Z_F(t)^{-1})_{xy},
\]
for sufficiently large \(t\), where the matrix is invertible.

O'Hara proved that rational independence of all edge lengths lets the magnitude function
recover the finite metric space up to isometry. Algebraic independence implies rational
linear independence, so this applies to every finite \(F\subset(X,d)\).

Suppose \(A,B\subset X\), \(|A|,|B|\ge2\), have identical magnitude functions. O'Hara's
theorem gives an isometry \(A\to B\). If the common cardinality is at least three,
ambient hereditary rigidity forces that isometry to be the inclusion and therefore
\(A=B\). If the common cardinality is two, pair-injectivity forces the unique edge to
be the same ambient unordered pair, again giving \(A=B\).

Singletons must be excluded: every one-point metric space has the same magnitude
function \(M(t)=1\).

## Further geometric consequences

Algebraic independence also forbids every nontrivial linear distance identity. In
particular, for three distinct points every triangle inequality is strict: an equality
such as
\[
d(x,z)=d(x,y)+d(y,z)
\]
would be a rational polynomial relation among three distinct pair distances. Hence these
metrics have no nontrivial metric-segment triples.

Likewise, no four-point subset is a tree metric. The four-point condition for an
additive tree metric forces equality between two of
\[
d_{12}+d_{34},\qquad d_{13}+d_{24},\qquad d_{14}+d_{23},
\]
again contradicting algebraic independence.

## Limitations

The generic proper-metric statement uses strong zero-dimensionality; it does not extend
to arbitrary locally compact Polish spaces. The magnitude conclusion is injective, not
stable: no quantitative inverse estimate is proved for recovering a point cloud from a
perturbed magnitude function. Singleton subsets cannot be distinguished by magnitude.
No claim is made that the properness lemma, Ishiki's approximation and \(G_\delta\)
theorems, or O'Hara's finite-space reconstruction theorem are new individually.

The primary metric-construction source is very recent. The originality claim therefore
concerns the proper genericity theorem, ambient hereditary rigidity formulation, and
ambient magnitude-fingerprint consequence, to the best of our knowledge.

## References

1. Yoshito Ishiki, *Algebraically independent distances and rigid metrics*,
   arXiv:2609.19773 (2026).
2. Jun O'Hara, *Magnitude function determines generic finite metric spaces*,
   Discrete Analysis 2025:13, DOI 10.19086/da.143788; arXiv:2401.00786.
