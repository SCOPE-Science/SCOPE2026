# The 42 determinantal classes of the Fermat quartic over \(\mathbb F_5\)

## Finding
Let \(k=\mathbb F_5\) and \(C\subset\mathbb P^2_k\) be the smooth Fermat plane quartic
\[C:X^4+Y^4+Z^4=0.\]
Up to left-right equivalence over \(k\), \(C\) has exactly **42** linear \(4\times4\) determinantal representations, of which **16** equivalence classes admit a symmetric representative and the remaining **26** do not. For the symmetric count, equivalence means congruence up to a nonzero scalar, \(M\sim c P M P^{\mathsf T}\), with \(c\in k^\times\) and \(P\in\mathrm{GL}_4(k)\). The underlying algebraic invariants are
\[
\#J(C)(k)=64,\qquad J(C)(k)\cong\mathbb Z/4\mathbb Z\oplus(\mathbb Z/2\mathbb Z)^4,
\qquad\#J(C)[2](k)=32.
\]
The arithmetic odd theta characteristics (geometric bitangents) have Frobenius cycle type \(1^{16}2^6\), and precisely \(16\) even theta characteristics are \(k\)-rational. The \(16\) rational odd theta characteristics are effective; the \(16\) rational even ones are non-effective. The distinct effective rational degree-two divisor classes number \(22\); the other \(42\) classes give the determinantal representations.

## Assumptions and scope
A linear determinantal representation is a triple \((M_X,M_Y,M_Z)\) of matrices over \(k\) such that \(\det(XM_X+YM_Y+ZM_Z)\) is a nonzero scalar multiple of the equation of \(C\). Two such triples are equivalent when \(M'_i=PM_iQ\) with \(P,Q\in\mathrm{GL}_4(k)\). Symmetric means all three matrices are symmetric, with symmetric equivalence by projective congruence as above. These are representations of this fixed plane model, not quotients by coordinate automorphisms. All divisor classes and theta characteristics are over \(k\). The characteristic is exactly five, so the étale \(2\)-torsion pairing and classical theta parity apply.

## Proof
**1. Curve counts and Jacobian order.** The gradient \((4X^3,4Y^3,4Z^3)\) is nowhere zero on the projective curve. The smooth nonhyperelliptic genus is three. Exact finite-field enumeration, including the points at infinity, gives
\[
(\#C(k),\#C(\mathbb F_{25}),\#C(\mathbb F_{125}))=(0,44,192).
\]
The supplied checker performs complete enumeration using polynomial-basis arithmetic in \(\mathbb F_5\), \(\mathbb F_5[t]/(t^2+2)\), and \(\mathbb F_5[t]/(t^3+t+1)\); both extension polynomials are irreducible. In each field it counts affine pairs satisfying \(u^4+v^4=-1\) and points at infinity satisfying \(u^4=-1\). These are finite exhaustive sums, not asymptotic sampling. Newton identities and the Weil functional equation for a genus-three curve determine its zeta numerator as
\[
L_C(T)=1-6T+27T^2-68T^3+135T^4-150T^5+125T^6=(1-2T+5T^2)^3.
\]
Hence \(\#J(C)(k)=L_C(1)=64\).

**2. Bitangent and theta arithmetic.** Over characteristic five, the identity
\[
(A+B)^4+A^4+B^4=2(A^2+AB+B^2)^2
\]
shows that the sixteen distinct lines \(X+aY+bZ=0\) for \(a,b\in k^\times\) are ordinary bitangents: each \(a^4=b^4=1\). Another twelve distinct bitangents are the three coordinate-pair families \(X=\zeta Y\), \(Y=\zeta Z\), \(Z=\zeta X\), where \(\zeta^4=-1\). For example, on \(X=\zeta Y\) the quartic restricts to \(Z^4\), making the line a hyperflex. All four roots of \(\zeta^4=-1\) lie in \(\mathbb F_{25}\) and satisfy \(\zeta^5=-\zeta\); there are no roots in \(k\). By the classical theorem identifying the 28 distinct geometric bitangents of a smooth nonhyperelliptic plane quartic in characteristic other than two with its 28 odd theta characteristics, the exhibited families exhaust them. Thus Frobenius has \(16\) fixed odd theta characteristics and six transpositions.

Choose one of the fixed odd theta characteristics \(\theta_0\). Write \(V=J(C)[2](\bar k)\cong\mathbb F_2^6\), equipped with its nondegenerate alternating Weil pairing \(\langle\ ,\ \rangle\). Theta parity defines a quadratic refinement \(q_0:V\to\mathbb F_2\) whose zero vectors correspond exactly to the odd theta characteristics, with polarization \(\langle\ ,\ \rangle\). Because \(\theta_0\) is defined over \(k\), Frobenius preserves \(q_0\). If \(K=V^{\mathrm{Frob}}\), then \(\#\{v\in K:q_0(v)=0\}=16\). Therefore \(\dim K\ge4\). If \(\dim K=4\), all sixteen elements of \(K\) have \(q_0=0\), so polarization vanishes on this four-dimensional subspace. This contradicts the maximal totally isotropic dimension three of a six-dimensional symplectic vector space. If \(\dim K=6\), all 28 odd theta characteristics are fixed, contradicting the six observed transpositions. Thus \(\dim K=5\), and \(\#J(C)[2](k)=32\). The group \(J(C)(k)\) has order \(2^6\) and exactly \(2^5\) elements killed by two, so its five invariant factors have exponents \((2,1,1,1,1)\), proving the displayed group isomorphism. Among the thirty-two rational theta characteristics, sixteen are odd, hence sixteen are even. Every even theta characteristic on a nonhyperelliptic genus-three curve is non-effective, since an effective even theta would have at least two sections and yield a degree-two morphism to \(\mathbb P^1\).

**3. Effective degree-two classes and determinantal representations.** Because \(C(k)=\varnothing\), the effective divisors of degree two defined over \(k\) are precisely the Frobenius-conjugate pairs of points in \(C(\mathbb F_{25})\). There are \(44/2=22\) such divisors. Distinct effective degree-two divisors cannot be linearly equivalent on a nonhyperelliptic curve: otherwise they yield a \(g^1_2\). An exhibited bitangent provides a rational line bundle of degree two, so \(\mathrm{Pic}^2(C)(k)\) is a trivial torsor under \(J(C)(k)\) and has 64 elements; over a finite field the distinction between rational Picard-scheme points and line bundles causes no Brauer obstruction. The 42 remaining classes are non-effective. The standard line-bundle correspondence identifies these with left-right equivalence classes of linear \(4\times4\) determinantal representations. Under the symmetric version of the correspondence (and projective congruence), the sixteen non-effective rational even theta characteristics give precisely sixteen symmetric classes. Hence there are \(42-16=26\) other classes.

## Verification
Run `python3 verify.py` using only the Python standard library. It tests the extension polynomials' irreducibility, all affine/projective field counts over sizes \(5,25,125\), Newton identities, order 64, the 22/42 counting arithmetic, all sixteen ordinary bitangent square identities, and consistency of the quadratic-form Frobenius fixed-point census in dimension six. The last test illustrates the quadratic symplectic deduction; its specific model is not claimed to be a separately constructed geometric Galois representation. The script prints `VERIFY_OK`. The underlying 28-bitangent/theta and determinantal correspondences are classical mathematical theorems rather than independently formalized code lemmas.

## Relationship to prior work
Meagher–Top give the elliptic-factor isogeny and twist arithmetic for Fermat quartics, supporting the zeta numerator independently. Plaumann–Sturmfels–Vinzant treat classical quartic bitangents and symmetric determinantal constructions. Ishitsuka–Ito–Ohshita (2018, 2021) establish detailed \(4\)-torsion/Galois arithmetic for the rational Fermat quartic and its positive-coefficient twist over the rationals, including existence and local-global questions about determinantal representations. Their rational-number-field conclusions are not finite-field counts of inequivalent representations over \(\mathbb F_5\). Previously recorded computations include the sixteen rational bitangents and the geometric bitangent arrangements; these components are credited, not independently claimed. The contribution assessed here is the exact finite-field determinantal-class division \(42=16+26\), together with the finite-Jacobian invariant factors and the supporting theta fixed-space argument.

## Limitations
No actual representative \(4\times4\) matrices for all forty-two classes are constructed, and the classification is up to the specified equivalence, not up to automorphisms of the plane. The finite Jacobian group statement is specific to \(k=\mathbb F_5\), not all finite extensions. Independent mathematical validation and complete historical priority verification have not been performed. Explicit global \(4\)-torsion data in the later work of Ishitsuka–Ito–Ohshita may imply parts of the arithmetic conclusions after reduction and twisting; the precise extent of this possible implication is a remaining originality risk.

## References
1. Stephen Meagher and Jaap Top, *Twists of genus three curves over finite fields*, Finite Fields Appl. 16 (2010), 347–368, DOI 10.1016/j.ffa.2010.06.001, lawful full text https://home.mathematik.uni-freiburg.de/arithgeom/TwistsGenThreeCurve.pdf.
2. Daniel Plaumann, Bernd Sturmfels, Cynthia Vinzant, *Quartic Curves and Their Bitangents*, arXiv:1008.4104 (initial submission 2010-08-24), https://arxiv.org/html/1008.4104.
3. Yasuhiro Ishitsuka, Tetsushi Ito, Tatsuya Ohshita, *Explicit calculation of the mod 4 Galois representation associated with the Fermat quartic*, arXiv:1804.07109, https://arxiv.org/html/1804.07109.
4. Yasuhiro Ishitsuka, Tetsushi Ito, Tatsuya Ohshita, *The arithmetic of a twist of the Fermat quartic*, arXiv:2107.05902, Sections 2 and 7, https://arxiv.org/abs/2107.05902.
