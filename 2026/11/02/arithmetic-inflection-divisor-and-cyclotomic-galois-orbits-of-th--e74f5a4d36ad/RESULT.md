# Arithmetic inflection divisor and cyclotomic Galois orbits of the 48-automorphism quartic

## Finding

Consider the smooth plane quartic
\[
 C:\quad X^4+Y^4+XZ^3=0
\]
over \(\mathbb Q\), with its integral equation reduced to any field of characteristic \(p>3\). Its geometric inflection divisor, obtained by intersecting \(C\) with its Hessian, has exactly twenty distinct supports: four hyperflexes of multiplicity two and sixteen ordinary flexes of multiplicity one. All of these points are rational over \(\mathbb Q(\zeta_{24})\); that cyclotomic field is their exact joint splitting field, and their six absolute-Galois orbits have sizes
\[
1,1,2,4,4,8.
\]
For every prime power \(q=p^s\) with \(p>3\), the number \(N(q)\) of distinct rational flex points of the reduced curve is
\[
 N(q)=2+2\mathbf1_{q\equiv1\pmod3}+4\mathbf1_{q\equiv1\pmod8}
       +4\mathbf1_{q\equiv1\text{ or }5\pmod{24}}+8\mathbf1_{q\equiv1\pmod{24}}.
\]
Equivalently, for residues \(q\equiv1,5,7,11,13,17,19,23\pmod{24}\), the respective counts are \(20,6,4,2,4,6,4,2\). Every geometric flex point is rational over \(\mathbb F_{p^2}\), for every \(p>3\).

## Assumptions and scope

Work over \(\mathbb Q\), or over a finite field \(\mathbb F_q\) with \(\operatorname{char}\mathbb F_q=p>3\); geometric assertions use an algebraic closure. Flex supports are distinct geometric points of contact order at least three with their unique tangent line; a hyperflex has contact order four. In characteristic \(p>3\), the usual Hessian intersection detects the flex divisor. The point-count formula counts each rational support once, not with its Hessian intersection multiplicity. Let \(\zeta_{24}\) be a chosen primitive twenty-fourth root of unity, \(\zeta_3=\zeta_{24}^8\), \(\zeta_8=\zeta_{24}^3\), and choose \(\sqrt3=\zeta_{24}^2+\zeta_{24}^{-2}\).

## Proof

**1. Smoothness and the complete Hessian intersection.** For \(F=X^4+Y^4+XZ^3\), its first derivatives are
\[
 F_X=4X^3+Z^3,\quad F_Y=4Y^3,\quad F_Z=3XZ^2.
\]
In characteristic other than two or three these have no simultaneous projective zero on \(F=0\); thus \(C\) is smooth. The determinant of the second-derivative matrix is the exact identity
\[
 \det(\partial_i\partial_j F)=108Y^2 Z(8X^3-Z^3).
\]
At \(Y=0\) and \(Z=1\), the curve equation is \(X^4+X=0\), with simple roots \(0,-1,-\zeta_3,-\zeta_3^2\). This gives exactly four hyperflex supports
\[
 [0:0:1],\quad [-\zeta_3^j:0:1]\quad(j=0,1,2).
\]
Indeed the tangent there is \(X=X_0Z\), and substitution in \(F\) gives \(Y^4\), so tangent contact is four and the Hessian vanishing order on the smooth curve is two.

At \(Z=0\), the four points are \([1:\zeta_8^{1+2k}:0]\) for \(k=0,1,2,3\). They have simple Hessian intersection: the Hessian factor \(Z\) has simple zero on the curve, since \(F_Y\ne0\). In the chart \(X=1\), the tangent line \(Y=\zeta_8^{1+2k}X\) has contact three because its substitution gives \(Z^3\).

At \(8X^3=Z^3\), \(Z=1\) and \(X=\zeta_3^j/2\) for \(j=0,1,2\). The quartic equation reduces to \(Y^4=-9\zeta_3^j/16\), giving four distinct nonzero values of \(Y\) for each \(j\). Their precise coordinates are
\[
 P_{j,k}=\left[\frac{\zeta_3^j}{2}:\frac{\sqrt3}{2}\zeta_{24}^{3+2j+6k}:1\right],
 \qquad j=0,1,2,\quad k=0,1,2,3.
\]
Since \(F_Y\ne0\), \(X-X_0\) is a local uniformizer; the factor \(8X^3-1\) vanishes simply because its derivative \(24X_0^2\ne0\). These twelve Hessian intersections are simple and hence are ordinary flexes of contact three. The exhaustive weighted count is \(4\cdot2+4+12=24=4\cdot6\), the Bézout intersection degree, with no common component. Thus there are no other geometric flexes, including in characteristic \(p>3\).

**2. Exact splitting field and Galois orbits.** Every displayed point belongs to \(K=\mathbb Q(\zeta_{24})\). The four infinity flex coordinates generate \(\mathbb Q(\zeta_8)\) collectively; the nonrational hyperflex coordinates generate \(\mathbb Q(\zeta_3)\) collectively. Their compositum is \(K\), so the common flex-point splitting field is exactly \(K\). Its Galois group is the eight-element group \((\mathbb Z/24\mathbb Z)^\times\). Its action fixes \([0:0:1]\) and \([-1:0:1]\), exchanges the two other hyperflexes, acts transitively on the four infinity flexes, and splits the twelve affine ordinary flexes into an orbit of four (\(j=0\)) and an orbit of eight (\(j=1,2\)). To verify these last claims explicitly, write the affine point as \(P(j,e)\), where \(Y=(\sqrt3/2)\zeta_{24}^e\) and \(e\equiv3+2j\pmod6\). For a unit \(a\pmod{24}\), set \(\epsilon(a)=12\) when \(a\equiv5,7\pmod{12}\) and \(\epsilon(a)=0\) otherwise. Then
\[
 \sigma_a:P(j,e)\longmapsto P(aj\bmod3,\,ae+\epsilon(a)\bmod24).
\]
This immediately gives orbit sizes four and eight. In particular the four-point affine orbit is fixed pointwise precisely by \(a=1,5\pmod{24}\), and the eight-point affine orbit has trivial stabilizer.

**3. Rational flex counts over finite fields.** The same explicit integral-coefficient equations and étale root-of-unity descriptions remain valid in characteristic \(p>3\), because \(24\) is invertible. Geometric Frobenius acts on the cyclotomic labels as \(\sigma_q\), so rational points are the fixed points of this permutation. The two rational hyperflexes persist over every \(\mathbb F_q\); the remaining two hyperflexes are rational iff \(q\equiv1\pmod3\). The four infinity flexes are rational iff \(q\equiv1\pmod8\). The four-point affine orbit contributes four rational points iff \(q\equiv1,5\pmod{24}\), and the eight-point orbit contributes eight iff \(q\equiv1\pmod{24}\). This proves the displayed formula for all prime powers. Every prime \(p>3\) satisfies \(p^2\equiv1\pmod{24}\), proving the uniform quadratic splitting assertion. The rational hyperflex count is \(2+2\mathbf1_{q\equiv1\pmod3}\).

## Verification

Run the standalone `verify_c48_flex.py` with Python 3 and SymPy. It computes the Hessian over the integers and checks the affine substitution, the explicit eight-element Galois permutation actions and orbit sizes, and the rational-support formula by direct enumeration in 23 prime fields from characteristic five to ninety-seven. It additionally enumerates all rational flex supports over quadratic extensions of characteristics five, seven and eleven using independently implemented finite-field arithmetic. Expected final output: `C48_FULL_HESSIAN_GALOIS_ORBITS_PRIME_AND_QUADRATIC_EXTENSION_COUNTS_PASS`. The general statement is proved in the preceding paragraphs; these finite tests are supplementary, not an exhaustive argument over all finite fields.

## Relationship to prior work

M. Janasz, *On symmetric plane quartic curves* (arXiv:2406.07015v1, first public 2024-06-11), Section 3, studies exactly the complex curve \(X^4+Y^4+XZ^3=0\) and obtains four hyperosculating lines and a dual curve with sixteen ordinary cusps, twenty-four nodes and four \(E_6\) singularities. Thus the geometric occurrence of four hyperflexes and sixteen ordinary flexes is already implicit in prior results; it is **not** claimed as an independent discovery. The present assertion instead supplies explicit complete flex coordinates, exact cyclotomic splitting field, arithmetic Galois orbit decomposition and the uniform finite-field fixed-point formula, including the degree-two splitting bound.

M. Janasz, P. Pokora and M. Zieliński, *On arrangements of smooth plane quartics and their bitangents* (arXiv:2308.16514v2), investigate bitangent arrangements, notably the Klein, Dyck and Komiya–Kuribayashi quartics, rather than this arithmetic inflection action. Broad literature and mathematical-record searches did not identify a theorem implying the arithmetic assertions above. This is a best-knowledge priority assessment, not a proof that no unindexed equivalent result exists.

## Limitations

The theorem does not compute the full bitangent Galois representation, Jacobian torsion, or the zeta function of \(C\). Characteristic two and three are excluded because the smoothness/Hessian analysis changes. The arithmetic data concern the particular rational equation displayed; they are not asserted for arbitrary nontrivial twists of the same geometric curve. Exact novelty in earlier unindexed literature remains a residual priority risk, and no independent mathematical audit has been performed.

## References

1. M. Janasz, *On symmetric plane quartic curves*, arXiv:2406.07015v1 (2024-06-11). Full text: https://arxiv.org/html/2406.07015v1 .
2. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514v2 (initial public version 2023-08-31). Full text: https://arxiv.org/html/2308.16514v2 .
