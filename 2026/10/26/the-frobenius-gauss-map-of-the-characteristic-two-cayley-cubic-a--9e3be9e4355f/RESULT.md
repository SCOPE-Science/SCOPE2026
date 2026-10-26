# The Frobenius Gauss map of the characteristic-two Cayley cubic and the Fano seven-point net

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). For the cubic surface
\[
X=V(F)\subset\mathbb P^3_k,\qquad
F=x_0x_1x_2+x_0x_1x_3+x_0x_2x_3+x_1x_2x_3,
\]
the point \(o=[1:1:1:1]\) is smooth, yet **every tangent plane at a smooth point of \(X\) contains \(o\)**. The reduced projective dual is exactly the plane
\[
X^\vee=\{[a_0:a_1:a_2:a_3]\in(\mathbb P^3_k)^\vee:\ a_0+a_1+a_2+a_3=0\}.
\]
The rational Gauss map \(\gamma:X\dashrightarrow X^\vee\) is generically purely inseparable of degree \(4\), of exponent one: under the displayed coordinates on the dual plane, its function field is exactly \(k(X)^2\subset k(X)\). Equivalently the Gauss map is a rational birational reparametrization of relative Frobenius on \(X\).

More precisely, \(\gamma=\psi\circ\pi_o\) rationally, where projection \(\pi_o:X\dashrightarrow\mathbb P^2\) from \(o\) and the planar map \(\psi:\mathbb P^2\dashrightarrow\mathbb P^2\) are **both purely inseparable of degree \(2\)**. The latter is the complete cubic linear system through the seven \(\mathbb F_2\)-rational points of \(\mathbb P^2\); blowing up these seven reduced points resolves \(\psi\) to the basepoint-free anticanonical map of degree \(2\). Thus the exceptional inseparability has a geometric explanation through the Fano plane configuration.

## Assumptions and scope
The field \(k\) is algebraically closed of characteristic exactly \(2\), hence perfect. The scheme \(X\) is defined by the displayed homogeneous cubic \(F\); the dual variety always means the reduced closure of tangent hyperplanes to its smooth locus. Degrees refer to finite extensions of function fields at generic points, not to numbers of geometric points in fibers. The projections and Gauss maps are rational maps, so no extension over their indeterminacy loci is asserted. \(\mathbb F_2\subset k\) is the prime subfield.

## Proof
**1. The strange point and the projection.** A direct derivative calculation in characteristic two yields
\[
\sum_{i=0}^3\partial F/\partial x_i=0.
\]
Thus every tangent plane to \(X\) passes through \(o\). At \(o\), each \(\partial F/\partial x_i=1\), so \(o\) is smooth. Set
\[
U=x_0+x_3,\quad V=x_1+x_3,\quad T=x_2+x_3,\quad W=x_3,
\]
which is an invertible projective coordinate transformation. Then
\[
F=UVT+W^2S,\qquad S=U+V+T.
\]
In these coordinates \(o=[0:0:0:1]\), and \(\pi_o\) is given by \([U:V:T]\). On \(U=1\), with \(y=V/U\), \(z=T/U\), and \(w=W/U\), the cubic equation is
\[
w^2=\frac{yz}{1+y+z}.
\]
The right-hand side is not a square in \(k(y,z)\): at the prime divisor \(y=0\) its valuation is one. It follows that \(F\) is irreducible and that \(\pi_o\) is generically purely inseparable of degree \(2\), with
\[
k(X)=k(y,z,w),\qquad[k(X):k(y,z)]=2.
\]

**2. The seven-point cubic net.** The derivatives of \(F\) with respect to \((U,V,T,W)\) are
\[
\bigl(VT+W^2,\ UT+W^2,\ UV+W^2,\ 0\bigr).
\]
Multiplying the first three derivatives by \(S\), and reducing modulo the equation \(F=0\), gives respectively
\[
G_1=VT(V+T),\quad G_2=UT(U+T),\quad G_3=UV(U+V).
\]
Hence on the dense open set \(S\ne0\), the Gauss map is the composite of projection and
\[
\psi([U:V:T])=[G_1:G_2:G_3].
\]
The common zeros of the three cubics are precisely the seven points \(\mathbb P^2(\mathbb F_2)\): if all three coordinates are nonzero they are equal; if one vanishes, the other two are equal or one also vanishes. In the local affine chart about each of these seven points, the linear parts of the three cubics span the two-dimensional cotangent space, so all base points are simple and there are no embedded or infinitely near base points. The seven point-evaluation conditions on ten plane cubic monomials are independent: their evaluation matrix has rank \(7\) over \(\mathbb F_2\). Thus \(G_1,G_2,G_3\) are a basis for the complete three-dimensional space of cubics through these points.

Let \(B\) be the blow-up of this seven-point scheme and \(E_i\) the exceptional divisors. The strict-transform linear system is
\[
\left|3H-\sum_{i=1}^7E_i\right|=|-K_B|,
\]
which is basepoint-free and has self-intersection \(9-7=2\). Its image is a surface, as verified directly by the function-field calculation below, so the induced morphism to \(\mathbb P^2\) has generic degree \(2\). In particular every line containing three Fano points is contracted, since its strict transform intersects \(-K_B\) in \(3-3=0\). No assertion that these seven points are in del Pezzo general position is made.

**3. The exact function-field computation.** Work where \(U=1\), \(G_2\ne0\), \(S\ne0\) and set target coordinates
\[
r=\frac{G_1}{G_2}=\frac{yz(y+z)}{z(1+z)},\qquad
 t=\frac{G_3}{G_2}=\frac{y(1+y)}{z(1+z)}.
\]
The exact polynomial identity \(G_1=yG_2+zG_3\) gives \(y=r+tz\). Substitution in the second displayed fraction yields
\[
z^2=\frac{r(r+1)}{t(t+1)},\qquad
y^2=\frac{r(r+t)}{1+t}.
\]
The surface equation and the same cubic identities also yield
\[
w^2=\frac r{1+t}.
\]
These are identities in \(k(X)\), on dense rational-function charts; clearing their denominators gives ordinary characteristic-two polynomial identities (checked in the included exact-arithmetic script). Put \(K=k(r,t)\). Since \(k(y,z)=K(z)\) and \(z^2\in K\), the extension \(k(y,z)/K\) is algebraic, so \(K\) has transcendence degree two: \(r,t\) are algebraically independent. Thus \(r(r+1)/(t(t+1))\) is nonsquare in \(K\) (valuation one at \(r=0\)), we have \([k(y,z):K]=2\), purely inseparable. Combining with step 1 gives
\[
[k(X):K]=4\quad\text{and the extension is purely inseparable.}
\]
The three square formulas show \(k(X)^2\subseteq K\). Because \(k\) is perfect and \(k(X)\) has transcendence degree \(2\), the standard \(p\)-basis degree formula gives \([k(X):k(X)^2]=2^2=4\). Hence equality \(K=k(X)^2\) follows by the tower law. This proves the exponent-one Frobenius statement, and shows that \(r,t\) are algebraically independent, so the reduced dual fills the indicated plane. All assertions follow. \(\square\)

## Verification
Run \(\texttt{python verify.py}\) with Python 3 and SymPy. The standalone script checks (over \(\mathbb F_2\)) the coordinate substitution, four derivatives, cubic-net identities, rank seven of the cubic evaluation matrix, first-order rank two at each of the seven base points, and all three cleared-denominator square identities. Its expected two lines begin \(\texttt{VERIFY_OK}\). The argument that a rational function with an odd prime-divisor valuation is nonsquare and the \(p\)-basis degree calculation are general mathematical proofs, **not** inferred from finite-field enumeration.

## Relationship to prior work
Heath-Brown [1] uses precisely the displayed elementary-symmetric Cayley cubic to study rational points over \(\mathbb Q\), not characteristic-two Gauss maps. Catanese and Ceresa [2, Proposition 2] compute the classical four-nodal cubic's dual **Steiner quartic**, under characteristic-zero hypotheses and the characteristic-zero duality formulas; its equation and conclusions are not the present characteristic-two linear dual. Catanese [3, §8] discusses the same cubic and its four complex nodes and covering constructions but not the asserted characteristic-two Gauss-field equality. Kadyrsizova and coauthors [4] analyze characteristic-two cubic surfaces through \(F\)-singularities, not the claimed polar factorization. These statements are **not** presented as exhaustive proof of uniqueness: older or differently named modular treatments of the strange surface may contain equivalent calculations.

## Limitations
The theorem concerns the reduced dual and generic rational Gauss map; it does not compute a potentially nonreduced scheme structure on a discriminant or classify all rational-map exceptional fibers. Its comparison with the classical dual quartic is a characteristic-dependent contrast, not a claim of a flat family of dual varieties. The characteristic-two seven-point net is highly special and does not behave as seven general points. The source examination and targeted searches cannot exclude an unidentified pre-existing equivalent theorem. Independent verification is not claimed.

## References
[1] D. R. Heath-Brown, *The Density of Rational Points on Cayley's Cubic Surface*, arXiv:math/0210333v1, publicly submitted 21 October 2002; https://arxiv.org/pdf/math/0210333.

[2] F. Catanese and G. Ceresa, *Constructing Sextic Surfaces with a Given Number of Nodes*, Journal of Pure and Applied Algebra 23 (1982), 1–12, especially §1 and Proposition 2; https://www.mathe8.uni-bayreuth.de/de/team/prof-fabrizio-catanese-old/pdf/012.pdf.

[3] F. Catanese, *Kummer Quartic Surfaces, Strict Self-Duality, and More*, arXiv:2101.10501, especially §8; https://arxiv.org/pdf/2101.10501.

[4] Z. Kadyrsizova et al., *Cubic Surfaces of Characteristic Two*, arXiv:2007.12018; https://arxiv.org/pdf/2007.12018.
