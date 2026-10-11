# Center alignment for Lp-optimal matching of centrally symmetric convex bodies
## Finding
Let \(d\ge2\) and \(2<p<\infty\). For convex bodies \(K,L\subset\mathbb R^d\), define
\[
\rho_p(K,L)
=
\left(
\int_{S^{d-1}}
|h_K(u)-h_L(u)|^p\,d\sigma(u)
\right)^{1/p},
\]
where \(h_K\) is the support function and \(\sigma\) is normalized spherical measure.

Suppose \(A\) and \(B\) are centrally symmetric convex bodies with centers \(a\) and \(b\). For every orthogonal map \(Q\in O(d)\), the function
\[
t\longmapsto \rho_p(QA+t,B)
\]
has the unique minimizer
\[
t=b-Qa.
\tag{1}
\]
Consequently, every Euclidean isometry
\[
f(x)=Qx+t
\]
that is globally \(\rho_p\)-optimal for matching \(A\) to \(B\) satisfies
\[
f(a)=b.
\tag{2}
\]
Therefore the center-of-symmetry map is a Euclidean-isometry-equivariant selector associated with \(\rho_p\) on the full isometry-invariant class of centrally symmetric convex bodies.

## Assumptions and scope
A convex body is a compact convex set with nonempty interior. A centrally symmetric convex body has a unique center \(c\) such that
\[
K-c=-(K-c).
\]
The support function is
\[
h_K(u)=\max_{x\in K}x\cdot u.
\]

The theorem concerns \(2<p<\infty\), matching the unresolved exponent range in the motivating 2009 selector problem. The proof itself uses only strict convexity of
\[
x\longmapsto |x|^p,
\]
so the translation statement also holds for \(1<p<\infty\); no originality claim is made here for the already classical \(p=2\) selector case.

The theorem does not assert uniqueness of the optimal orthogonal map \(Q\). It asserts that once \(Q\) is fixed, the optimal translation is unique, and hence every globally optimal Euclidean isometry aligns the two symmetry centers.

## Proof
Translate both bodies to their symmetry centers:
\[
A_0=A-a,
\qquad
B_0=B-b.
\]
Then
\[
A_0=-A_0,
\qquad
B_0=-B_0.
\]
For every centrally symmetric body centered at the origin, the support function is even:
\[
h_{A_0}(-u)=h_{A_0}(u),
\qquad
h_{B_0}(-u)=h_{B_0}(u).
\]
Orthogonal images preserve origin symmetry, so for fixed \(Q\in O(d)\),
\[
g(u):=h_{QA_0}(u)-h_{B_0}(u)
\]
is an even function on \(S^{d-1}\).

For a translation \(t\in\mathbb R^d\), set
\[
z=Qa+t-b.
\]
The translation rule for support functions gives
\[
h_{QA+t}(u)-h_B(u)
=
g(u)+z\cdot u.
\]
Hence
\[
\rho_p(QA+t,B)^p
=
\int_{S^{d-1}}
|g(u)+z\cdot u|^p\,d\sigma(u).
\tag{3}
\]

Pair the integrand at \(u\) and \(-u\). Because \(g\) is even and
\[
z\cdot(-u)=-z\cdot u,
\]
equation (3) equals
\[
\frac12
\int_{S^{d-1}}
\left(
|g(u)+z\cdot u|^p
+
|g(u)-z\cdot u|^p
\right)
d\sigma(u).
\tag{4}
\]

For real \(r,s\), strict convexity of
\[
\phi(x)=|x|^p
\]
gives
\[
\frac{\phi(r+s)+\phi(r-s)}2
\ge
\phi(r),
\tag{5}
\]
with equality if and only if
\[
s=0.
\]
Applying (5) pointwise to (4) yields
\[
\rho_p(QA+t,B)^p
\ge
\int_{S^{d-1}}|g(u)|^p\,d\sigma(u).
\tag{6}
\]

If \(z\ne0\), then
\[
z\cdot u=0
\]
only on a great \((d-2)\)-sphere, which has spherical measure zero. Thus (5) is strict for almost every \(u\), and (6) is strict. Equality holds exactly when
\[
z=0,
\]
which is equivalent to (1).

Now let \(f(x)=Qx+t\) be globally optimal among Euclidean isometric copies of \(A\). If
\[
t\ne b-Qa,
\]
then keeping the same \(Q\) and replacing only \(t\) by \(b-Qa\) strictly decreases the \(\rho_p\)-distance, contradicting global optimality. Therefore (2) holds.

Finally, the map sending a centrally symmetric convex body to its symmetry center selects a point of the body and commutes with every Euclidean isometry. Equation (2) is exactly the required association property on this class.

## Verification
The proof is analytic and has no finite-enumeration step. Its only nonlinear ingredient is strict convexity of
\[
|x|^p.
\]
The supplied `verify.py` checks the paired inequality on deterministic grids for several nonintegral exponents \(p>2\), verifies the exact quartic identity
\[
(r+s)^4+(r-s)^4-2r^4
=
12r^2s^2+2s^4,
\]
and independently performs deterministic circular quadrature for an even support-function difference perturbed by nonzero linear translation modes.

Those computations are regression checks only. The continuum theorem follows from equations (3)--(6) and the fact that a nonzero linear functional vanishes on a spherical set of measure zero.

## Relationship to prior work
Herburt and Moszyńska define the \(L_p\) support-function metrics, study optimal Euclidean isometries, and prove existence of an optimal isometry for every pair for the relevant \(L_p\) metrics. Their paper recalls Arnold's \(p=2\) result: for an \(L_2\)-optimal isometry, the Steiner points coincide.

The accompanying 2009 open-problem session asks whether, for \(p>2\), there is an isometry-equivariant selector associated with \(\rho_p\). The theorem here gives an affirmative answer on the natural isometry-invariant subclass of all centrally symmetric convex bodies: the selector is simply the symmetry center. More strongly, it identifies the unique optimal translation for every fixed relative orientation.

The closest primary paper was inspected in full around the metric definition, associated-selector definition, the \(p=2\) result, and its optimal-isometry existence theorem. It does not state the center-alignment theorem for centrally symmetric bodies. Targeted searches under center-of-symmetry, optimal-translation, support-function \(L_p\), and associated-selector formulations did not locate an implication-equivalent published statement.

## Limitations
This does not solve the 2009 selector problem on all convex bodies. Central symmetry is essential to the parity argument because it makes the centered support functions even.

The theorem does not claim a unique optimal rotation or a unique globally optimal isometry; different orthogonal maps may give the same minimum value. It only proves that their translation component is forced by center alignment.

The \(p=2\) case is already covered by the classical Steiner-point result and is not claimed as new. No statement is made for the Hausdorff metric or for \(p=1\), where strict convexity is unavailable.

Because the argument is short and structural, an equivalent observation may exist in unindexed approximation-theory or convex-geometry literature under different terminology. The closest primary sources and the main equivalent formulations were checked, but that historical residual risk remains.

## References
1. I. Herburt and M. Moszyńska, *Optimal isometries for a pair of compact convex subsets of \(\mathbb R^n\)*, Banach Center Publications 84 (2009), 111--120. DOI: 10.4064/bc84-0-7.
2. *Open Problem Session*, Banach Center Publications 84 (2009), 217--222, Problem 13.
3. R. Arnold, *Zur \(L_2\)-Bestapproximation eines konvexen Körpers durch einen bewegten konvexen Körper*, Monatshefte für Mathematik 108 (1989), 277--293.
