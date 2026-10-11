# Nonattainment of the three-dimensional point-symmetric Minkowski-chirality bound

## Finding

Let \(K\subset\mathbb R^3\) be a point-symmetric convex body. For either nontrivial reflection dimension
\[
j\in\{1,2\},
\]
its Minkowski chirality satisfies
\[
\boxed{\alpha_j(K)<\sqrt3.}
\]

Thus the universal estimate
\[
\alpha_j(K)\le\sqrt3
\]
for point-symmetric three-dimensional bodies is never attained.

The mechanism is already visible on parallelotopes. Let
\[
P=A[-1,1]^3
\]
be origin-symmetric and write a singular-value decomposition
\[
A=QDR^{\mathsf T}.
\]
The John ellipsoid is \(A B_2^3\). For each \(i\in\{1,2,3\}\), reflect in the principal plane of this ellipsoid perpendicular to \(Qe_i\). The exact containment factor for that particular reflection is
\[
\boxed{
\left\|I-2v_i v_i^{\mathsf T}\right\|_{\infty\to\infty},
\qquad
v_i=Re_i.
}
\]
It is always at most \(\sqrt3\).

Equality for one such principal reflection is rigid: up to permutation, the squared coordinates of its unit normal \(v_i\) must be either
\[
\left(
\frac{3+\sqrt3}{6},
\frac{3-\sqrt3}{12},
\frac{3-\sqrt3}{12}
\right)
\]
or
\[
\left(
\frac{3-\sqrt3}{6},
\frac{3+\sqrt3}{12},
\frac{3+\sqrt3}{12}
\right).
\]
No orthonormal basis of \(\mathbb R^3\) consists entirely of vectors of these equality types. Consequently at least one principal John-plane reflection of every parallelotope has containment factor strictly below \(\sqrt3\), and hence
\[
\alpha_2(P)<\sqrt3.
\]

The equality \(\alpha_1(P)=\alpha_2(P)\) for point-symmetric bodies then gives
\[
\alpha_1(P)<\sqrt3.
\]
Polarity transfers the same strict inequalities to all three-dimensional cross-polytopes.

Finally, the three-dimensional equality classification for the Banach--Mazur distance to the Euclidean ball says that a symmetric body with
\[
d_{\mathrm{BM}}(K,B_2^3)=\sqrt3
\]
must be a parallelotope or a cross-polytope. Since Minkowski chirality is bounded above by that Banach--Mazur distance, equality
\[
\alpha_j(K)=\sqrt3
\]
would force \(K\) into one of those two classes, which have just been excluded.

## Assumptions and scope

Minkowski chirality is used in the normalization of Caragea, von Dichter, Gottwald, Grundbacher, Jahn, and Runge. For a convex body \(K\), \(\alpha_j(K)\) is the infimum of the relative circumradius
\[
R(K,\Phi_U(K))
\]
over affine \(j\)-flats \(U\), where \(\Phi_U\) is reflection in \(U\).

Point symmetry allows translation of \(K\) so that its center is the origin without changing the chirality. For origin-symmetric bodies, a translation of the reflected container cannot improve the relative circumradius: if
\[
K\subset t+\lambda C
\]
with \(K=-K\) and \(C=-C\), then applying support functions in directions \(u\) and \(-u\) gives
\[
h_K(u)\le\lambda h_C(u)-|t\cdot u|\le\lambda h_C(u),
\]
so already
\[
K\subset\lambda C.
\]

The theorem is a strict nonattainment statement. It does not claim that the supremum of \(\alpha_j\) over point-symmetric three-dimensional bodies is smaller than \(\sqrt3\). In particular, no dimension-three uniform gap is proved.

## Proof

Translate first so that the parallelotope is
\[
P=A[-1,1]^3
\]
with \(A\) invertible, and take
\[
A=QDR^{\mathsf T}
\]
with \(Q,R\) orthogonal and \(D\) positive diagonal.

The John ellipsoid of the cube is \(B_2^3\), so affine equivariance gives
\[
\mathcal E_J(P)=A B_2^3.
\]
Its principal axes are the columns \(Qe_i\).

Fix \(i\). Reflection in the principal plane perpendicular to \(Qe_i\) has matrix
\[
\Phi_i=Q S_iQ^{\mathsf T},
\qquad
S_i=I-2e_ie_i^{\mathsf T}.
\]
Because \(D\) commutes with \(S_i\),
\[
A^{-1}\Phi_i A
=
R D^{-1}S_iD R^{\mathsf T}
=
R S_iR^{\mathsf T}.
\]
Put
\[
v_i=Re_i.
\]
Then
\[
R S_iR^{\mathsf T}
=
I-2v_iv_i^{\mathsf T}.
\]

Let
\[
C=[-1,1]^3.
\]
Since both \(P\) and \(\Phi_i(P)\) are origin-symmetric, the preceding support-function observation removes translations from the relative circumradius. Applying \(A^{-1}\) therefore gives
\[
R(P,\Phi_i(P))
=
\inf\{\lambda:C\subset\lambda M_iC\},
\qquad
M_i=I-2v_iv_i^{\mathsf T}.
\]
The reflection matrix satisfies
\[
M_i^{-1}=M_i,
\]
hence
\[
R(P,\Phi_i(P))
=
\|M_i\|_{\infty\to\infty}.
\]

Every row of the orthogonal matrix \(M_i\) has Euclidean norm \(1\). Cauchy--Schwarz yields
\[
\|M_i\|_{\infty\to\infty}
=
\max_r\sum_s |(M_i)_{rs}|
\le\sqrt3.
\]

We now classify equality. Suppose
\[
\|I-2vv^{\mathsf T}\|_{\infty\to\infty}=\sqrt3
\]
for a unit vector \(v\). Some row has both Euclidean norm \(1\) and \(\ell_1\)-norm \(\sqrt3\), so all three absolute entries of that row equal
\[
\frac1{\sqrt3}.
\]
If its index is \(r\), put
\[
t=v_r^2
\]
and let the other two squared coordinates be \(s_1,s_2\). Equality of the two off-diagonal magnitudes gives
\[
s_1=s_2=s.
\]
The unit-vector condition and either off-diagonal equation are
\[
t+2s=1,
\qquad
4ts=\frac13.
\]
Therefore
\[
6t^2-6t+1=0,
\]
so
\[
t=\frac{3\pm\sqrt3}{6},
\qquad
s=\frac{3\mp\sqrt3}{12}.
\]
This is exactly the two equality types in the Finding.

It remains to show that three orthonormal equality-type vectors cannot exist. Write
\[
a^2=\frac{3+\sqrt3}{6},
\qquad
b^2=\frac{3-\sqrt3}{12},
\]
and
\[
c^2=\frac{3-\sqrt3}{6},
\qquad
d^2=\frac{3+\sqrt3}{12}.
\]
Call a vector of squared-coordinate type
\[
(a^2,b^2,b^2)
\]
type \(A\), and one of type
\[
(c^2,d^2,d^2)
\]
type \(B\), allowing arbitrary coordinate permutations and signs.

Two type-\(A\) vectors cannot be orthogonal. If their distinguished coordinates coincide, the magnitude \(a^2\) is larger than the sum \(2b^2\); if the distinguished coordinates differ, the two \(ab\) terms either cancel, leaving a nonzero \(b^2\), or add with magnitude larger than \(b^2\). The same argument applies to two type-\(B\) vectors after exchanging the roles forced by their values.

For an \(A\)-vector and a \(B\)-vector with different distinguished coordinates, the largest product is
\[
ad,
\]
and one checks
\[
ad>bc+bd,
\]
so they cannot be orthogonal. Thus an orthogonal equality-type pair must have the same distinguished coordinate. In that case
\[
ac=\frac1{\sqrt6},
\qquad
bd=\frac1{2\sqrt6},
\]
so orthogonality is possible exactly by cancelling the distinguished-coordinate contribution against the two equal remaining contributions.

For every such orthogonal pair, the two nondistinguished sign products agree. Their cross product therefore has zero distinguished coordinate. Since the pair is orthonormal, the cross product is a unit vector; symmetry of the two remaining coordinates gives squared-coordinate pattern
\[
(0,1/2,1/2)
\]
up to permutation. This is neither equality type \(A\) nor equality type \(B\). Hence an orthonormal equality-type triple is impossible.

The three vectors
\[
v_1,v_2,v_3
\]
are the columns of the orthogonal matrix \(R\), hence form an orthonormal basis. Therefore not all three principal-plane factors can equal \(\sqrt3\). At least one satisfies
\[
R(P,\Phi_i(P))<\sqrt3.
\]
Since \(\alpha_2(P)\) is the infimum over all planes,
\[
\alpha_2(P)<\sqrt3.
\]

For every point-symmetric body in dimension three, the source proves
\[
\alpha_1=\alpha_2.
\]
Thus
\[
\alpha_1(P)<\sqrt3
\]
as well.

If \(C\) is a cross-polytope, translate it to the origin. Its polar is a parallelotope. The source proves, for origin-symmetric bodies,
\[
\alpha_j(C)=\alpha_j(C^\circ),
\]
so cross-polytopes also have strict chirality below \(\sqrt3\).

Now let \(K\) be any point-symmetric convex body in \(\mathbb R^3\). The source gives
\[
\alpha_j(K)\le d_{\mathrm{BM}}(K,B_2^3)\le\sqrt3.
\]
If equality held in the first displayed theorem, then necessarily
\[
d_{\mathrm{BM}}(K,B_2^3)=\sqrt3.
\]
Grundbacher--Kobos classify the three-dimensional equality cases: \(K\) must be affinely equivalent to a parallelotope or a cross-polytope. Those classes have already been excluded. Therefore
\[
\alpha_j(K)<\sqrt3
\]
for \(j=1,2\).

## Verification

The proof is analytic except for elementary radical comparisons in the equality-type lemma.

The bundled checker reconstructs all \(48\) signed and permuted equality-type unit vectors exactly over algebraic numbers. It confirms that there are \(48\) orthogonal unordered pairs, that every equality-type vector has exactly two equality-type orthogonal partners, and that the orthogonality graph has no triangle. It further checks that every orthogonal equality-type pair consists of one type \(A\) and one type \(B\) with the same distinguished coordinate, and that its cross product has squared-coordinate multiset
\[
\{0,1/2,1/2\}.
\]

This finite check is exhaustive only after the analytic equality classification has reduced the problem to those \(48\) vectors. The infinite geometric theorem does not follow from numerical sampling.

The primary paper was inspected at its definition of Minkowski chirality, its general Banach--Mazur upper bound, the polarity and complementary-dimension identities, and its open-problem discussion identifying parallelotopes and cross-polytopes as the only possible three-dimensional equality classes. The supporting Banach--Mazur paper was inspected at its three-dimensional equality classification.

## Relationship to prior work

Caragea, von Dichter, Gottwald, Grundbacher, Jahn, and Runge prove
\[
\alpha_j(K)\le d_{\mathrm{BM}}(K,B_2^n)
\]
and, for point-symmetric \(K\),
\[
\alpha_j(K)=\alpha_{n-j}(K).
\]
For origin-symmetric \(K\), they also prove polarity invariance
\[
\alpha_j(K)=\alpha_j(K^\circ).
\]

Their open-problem section specializes these facts to dimension three. It states that
\[
\alpha_j(K)\le\sqrt3
\]
for \(j=1,2\), observes that the only possible equality bodies are parallelotopes and cross-polytopes, and explicitly says that deciding attainment reduces to checking one chirality on either one of those classes.

Grundbacher--Kobos provide the needed Banach--Mazur equality classification: in dimension three, parallelotopes and cross-polytopes are the only symmetric bodies at Banach--Mazur distance \(\sqrt3\) from the Euclidean ball.

The present result performs the missing class calculation and shows that neither candidate class actually attains the chirality bound. Targeted searches for Minkowski-chirality nonattainment, the three-dimensional \(\sqrt3\) equality question, principal-axis reflection factors of parallelotopes, and equivalent cross-polytope formulations found no prior statement of this conclusion.

## Limitations

Strict pointwise nonattainment does not imply a uniform quantitative gap. The theorem leaves open whether
\[
\sup\{\alpha_j(K):K\subset\mathbb R^3\text{ point-symmetric}\}
\]
is equal to \(\sqrt3\) or is strictly smaller.

The argument is dimension-specific. Its key final obstruction is that three equality-type vectors cannot form an orthonormal basis in \(\mathbb R^3\). No claim is made about analogous principal-axis configurations in higher dimension.

The proof uses the published three-dimensional Banach--Mazur equality classification as an input. It does not reprove that classification.

## References

1. Andrei Caragea, Katherina von Dichter, Kurt Klement Gottwald, Florian Grundbacher, Thomas Jahn, and Mia Runge, *Minkowski chirality: a measure of reflectional asymmetry of convex bodies*, arXiv:2504.13013v1, 17 April 2025; Journal of Mathematical Analysis and Applications 557 (2026), 130287.
2. Florian Grundbacher and Tomasz Kobos, *On certain extremal Banach--Mazur distances and Ader's characterization of distance ellipsoids*, arXiv:2407.08829v1, 11 July 2024; Mathematika 72 (2026), e70062.
