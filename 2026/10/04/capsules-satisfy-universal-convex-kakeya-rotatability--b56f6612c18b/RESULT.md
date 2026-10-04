# Capsules satisfy universal convex Kakeya rotatability

## Finding

Let \(d\ge2\), let \(T\subset\mathbb R^d\) be compact, and let
\[
S_r=T+rB_2^d,
\qquad r\ge0,
\]
where \(B_2^d\) is the Euclidean unit ball.

Say that \(T\) has the universal convex Kakeya rotatability property if, for every compact convex \(T\)-Kakeya set \(C\), any two \(T\)-copies in \(C\) can be continuously rotated into each other.

Then Euclidean ball thickening preserves this property:

\[
\boxed{
T\text{ universally rotatable}
\quad\Longrightarrow\quad
T+rB_2^d\text{ universally rotatable}.
}
\]

In particular, let \(L\) be any nondegenerate line segment and let \(r>0\). The capsule
\[
S=L+rB_2^d
\]
has the universal convex Kakeya rotatability property.

Thus, for every \(d\ge3\), capsules give a family of compact convex sets \(S\subset\mathbb R^d\) that are neither segments nor balls and for which every convex \(S\)-Kakeya body allows any two \(S\)-copies to be continuously rotated into one another. This answers Question 5.2 of Janzer affirmatively.

## Assumptions and scope

For \(A,B\subset\mathbb R^d\), their Minkowski sum is
\[
A+B=\{a+b:a\in A,\ b\in B\}.
\]

For a compact convex set \(K\) and \(r\ge0\), define its Euclidean inner parallel body
\[
K\ominus rB_2^d
=
\{x\in\mathbb R^d:x+rB_2^d\subset K\}.
\]
Equivalently,
\[
K\ominus rB_2^d
=
\bigcap_{b\in rB_2^d}(K-b),
\]
so it is compact and convex whenever it is nonempty.

Following Janzer, \(K\) is \(S\)-Kakeya if for every \(\rho\in\operatorname{SO}(d)\) there exists \(w\in\mathbb R^d\) with
\[
\rho S+w\subset K.
\]
Two \(S\)-copies can be rotated into each other within \(K\) when their rotation and translation parameters can be joined by continuous paths while preserving containment.

The conclusion concerns this path-connectivity property, not Janzer's stronger problem of continuously selecting one copy simultaneously for every orientation.

## Proof

Let
\[
S_r=T+rB_2^d
\]
and let \(K\) be a compact convex \(S_r\)-Kakeya set. Put
\[
C=K\ominus rB_2^d.
\]

The key point is the exact placement equivalence
\[
\boxed{
\rho S_r+w\subset K
\quad\Longleftrightarrow\quad
\rho T+w\subset C
}
\]
for every
\[
\rho\in\operatorname{SO}(d),
\qquad
w\in\mathbb R^d.
\]

Indeed, Euclidean rotations preserve the ball, so
\[
\rho S_r+w
=
\rho T+w+rB_2^d.
\]
By the definition of erosion,
\[
\rho T+w+rB_2^d\subset K
\]
holds exactly when every point \(x\in\rho T+w\) satisfies
\[
x+rB_2^d\subset K,
\]
which is exactly
\[
\rho T+w\subset K\ominus rB_2^d=C.
\]

Because \(K\) is \(S_r\)-Kakeya, the equivalence shows that \(C\) is \(T\)-Kakeya. In particular \(C\) is nonempty.

Now suppose
\[
\rho_0S_r+w_0\subset K,
\qquad
\rho_1S_r+w_1\subset K.
\]
The same equivalence gives
\[
\rho_0T+w_0\subset C,
\qquad
\rho_1T+w_1\subset C.
\]

Assume \(T\) has the universal convex Kakeya rotatability property. Then there are continuous maps
\[
\gamma:[0,1]\to\operatorname{SO}(d),
\qquad
\delta:[0,1]\to\mathbb R^d
\]
with the prescribed endpoints and
\[
\gamma(t)T+\delta(t)\subset C
\]
for every \(t\in[0,1]\).

Applying the placement equivalence again,
\[
\gamma(t)S_r+\delta(t)\subset K
\]
for every \(t\). Thus \(S_r\) inherits universal rotatability.

For the capsule consequence, take \(T=L\), a nondegenerate segment. Janzer's Theorem 1.2 proves the universal rotatability property for unit segments in every dimension \(d\ge2\). Any other positive segment length follows by a Euclidean similarity: scale the host and the segment by the reciprocal of the segment length, apply the unit-segment theorem, and scale the path back.

Therefore
\[
L+rB_2^d
\]
is universally rotatable for every \(r>0\).

Finally, when \(r>0\) and \(L\) is nondegenerate, the capsule is not a segment because it has positive width in every direction. It is not a ball because its width in the direction of \(L\) is
\[
\operatorname{length}(L)+2r,
\]
whereas its width in every direction orthogonal to \(L\) is
\[
2r.
\]
Hence the capsule is a nontrivial example of precisely the type requested in Janzer's Question 5.2.

## Verification

The proof is set-theoretic and does not depend on a numerical computation.

The packaged `verify.py` checks the central erosion equivalence independently on many randomly generated polyhedral halfspace systems in dimensions \(2\) through \(5\). For a halfspace
\[
\langle a,x\rangle\le b,
\]
a capsule placement is contained precisely when the segment support value plus
\[
r\lVert a\rVert
\]
is at most \(b\); erosion replaces \(b\) by
\[
b-r\lVert a\rVert,
\]
so the two tests coincide.

It also checks the elementary width distinction showing that a nondegenerate positive-radius capsule is neither a segment nor a ball.

The replay output is:

`VERIFY_OK capsule Kakeya erosion reduction`

These finite checks are consistency tests only. The theorem itself follows from the exact erosion identity and Janzer's segment theorem.

## Relationship to prior work

Janzer defines \(S\)-Kakeya containment and the path notion used here, proves in Theorem 1.2 that any two unit segments can be rotated into each other inside every compact convex Kakeya body in every dimension \(d\ge2\), and proves that the analogous statement fails for general bodies in dimensions at least four.

In the concluding section, Janzer asks whether there are compact convex sets other than segments and balls, in dimensions \(d\ge3\), for which the positive path property always holds. Capsules provide such a family.

Bae, Cabello, Cheong, Choi, Stehn, and Yoon prove a planar reverse-Kakeya theorem for arbitrary convex shapes. That planar result does not answer Janzer's higher-dimensional Question 5.2, which specifically asks for \(d\ge3\).

Targeted searches using the terms `S-Kakeya`, capsule, spherocylinder, stadium, Minkowski sum, inner parallel body, outer parallel body, and Janzer's Question 5.2 did not locate a prior statement of the ball-thickening inheritance lemma or the capsule consequence.

## Limitations

The argument depends on the thickening summand being a Euclidean ball, or more generally a compact set invariant under every rotation under consideration. For an anisotropic thickening body \(Q\), one has
\[
\rho(T+Q)=\rho T+\rho Q,
\]
so a single fixed erosion of \(K\) no longer gives the same reduction unless \(Q\) is rotation-invariant.

The result establishes Janzer's path-connectivity property. It does not establish the stronger existence of a continuous global choice of one placement for every orientation.

The literature search found no equivalent capsule statement, but differently phrased or unindexed prior observations remain a residual originality risk.

## References

B. Janzer, “Rotation Inside Convex Kakeya Sets,” arXiv:2209.09728, first submitted 2022-09-20; Discrete & Computational Geometry 73 (2025), 149–176, DOI 10.1007/s00454-024-00639-9.

S. W. Bae, S. Cabello, O. Cheong, Y. Choi, F. Stehn, and S. D. Yoon, “The Reverse Kakeya Problem,” 34th International Symposium on Computational Geometry (SoCG 2018), Article 6, DOI 10.4230/LIPIcs.SoCG.2018.6; later Advances in Geometry 21 (2021), 75–84, DOI 10.1515/advgeom-2020-0030.
