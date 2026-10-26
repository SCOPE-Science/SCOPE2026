# Newton-polygon strata of a symmetric genus-five Howe family in characteristic three

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\). For \((b,c)\) in
\[
U=\{(b,c)\in\mathbb A^2_k:c\ne0,\ c\ne b^2,\ (c-1)^2+b^2\ne0\},
\]
let \(H_{b,c}\) be the smooth projective normalization of the fiber product over \(\mathbb P^1_x\) of the elliptic covers
\[
E_0:u^2=x^4+1,\qquad E_{b,c}:v^2=x^4+bx^2+c.
\]
Then \(H_{b,c}\) is a geometrically connected genus-five curve, and its Jacobian has precisely three possible Newton polygons. The \(3\)-rank, \(a\)-number and slopes (with multiplicities) are:

| Parameter condition in \(U\) | \(3\)-rank | \(a\)-number | Newton slopes |
|---|---:|---:|---|
| \(b\ne0,\ c\ne-1\) | 4 | 1 | \(0^{[4]},(1/2)^{[2]},1^{[4]}\) |
| Exactly one of \(b=0,\ c=-1\) | 3 | 2 | \(0^{[3]},(1/2)^{[4]},1^{[3]}\) |
| \(b=0,\ c=-1\) | 2 | 3 | \(0^{[2]},(1/2)^{[6]},1^{[2]}\) |

In particular, the non-generic rank locus is the reduced transverse union of two affine line sections \(\{b=0\}\cap U\) and \(\{c=-1\}\cap U\), with exactly one intersection point. No Jacobian in this family is ordinary, and none has \(3\)-rank below two.

For \(q=3^m\) and each integer \(m\ge1\), count **ordered equation parameters** \((b,c)\in U(\mathbb F_q)\), not isomorphism classes. Put \(\epsilon_m=0\) for odd \(m\), and \(\epsilon_m=2\) for even \(m\). The numbers of parameters in ranks \(2,3,4\), respectively, are
\[
1,\qquad 2q-\epsilon_m-4,\qquad
\begin{cases}(q-1)(q-3)&m\text{ odd},\\q^2-6q+11&m\text{ even}.\end{cases}
\]
The total is \(q^2-2q\) for odd \(m\), and \(q^2-4q+6\) for even \(m\).

## Assumptions and scope

All geometric smoothness statements are over \(\overline{\mathbb F}_3\); the finite-field counts concern parameters rational over \(\mathbb F_{3^m}\) subject to geometric smoothness. The first elliptic double cover is fixed and supersingular; the second is an even quartic with unit leading coefficient. These equations define a natural coordinate-marked subfamily of the genus-five generalized Howe construction, invariant under the common base involution \(x\mapsto-x\). Distinct parameters are counted separately even when their abstract curves are isomorphic. The claim does not concern the full genus-five moduli space.

## Proof

**Smoothness and genus.** The derivative of \(x^4+bx^2+c\) is \(x^3-bx\) in characteristic three; it has a repeated root precisely when \(c=0\) or \(c=b^2\). The first quartic is separable. A common root of the two quartics would give \(t=x^2\), \(t^2=-1\), and \(bt+c-1=0\); eliminating \(t\) gives \((c-1)^2+b^2=0\), and conversely this equation yields a common geometric root. Thus the conditions defining \(U\) are exactly the separability and disjoint-branch conditions.

Consequently the two degree-two extensions of \(k(x)\) are independent, and the compositum is a connected \((\mathbb Z/2)^2\)-Galois cover of \(\mathbb P^1\) of degree four. Each of its eight distinct branch points contributes two to the Riemann–Hurwitz ramification term. Therefore \(2g(H_{b,c})-2=-8+16=8\) and \(g(H_{b,c})=5\). The third nontrivial involution quotient is the genus-three hyperelliptic curve
\[
G_{b,c}:w^2=(x^4+1)(x^4+bx^2+c).
\]

**Prime-to-three Jacobian decomposition.** The quotient maps for the three nontrivial characters of \((\mathbb Z/2)^2\) induce an isogeny of degree a power of two between \(J(H_{b,c})\) and \(E_0\times E_{b,c}\times J(G_{b,c})\). This follows either from the standard Klein-four quotient decomposition or from its idempotent correspondences after inverting two. Since three does not divide the isogeny degree, it identifies the \(3\)-divisible groups and hence preserves Newton slopes, total \(3\)-rank and total \(a\)-number.

**Cartier–Manin computation.** For a hyperelliptic equation \(y^2=f(x)\) in characteristic three, with genus \(g\) and \(f\) squarefree, a Hasse–Witt/Cartier–Manin matrix (up to the standard transpose/twist convention) has entries \([x^{3i-j}]f(x)\) for \(1\le i,j\le g\). The exponent \((3-1)/2\) is one. The coefficient of \(x^2\) in \(x^4+1\) is zero, so \(E_0\) is supersingular. The coefficient of \(x^2\) in \(x^4+bx^2+c\) is \(b\), so \(E_{b,c}\) is ordinary if and only if \(b\ne0\). Expanding the genus-three polynomial gives
\[
x^8+bx^6+(c+1)x^4+bx^2+c,
\]
and its matrix is
\[
M_G=\begin{pmatrix}b&0&c\\0&c+1&0\\1&0&b\end{pmatrix}.
\]
The \(2\)-by-\(2\) block \(\left(\begin{smallmatrix}b&c\\1&b\end{smallmatrix}\right)\) has determinant \(b^2-c\ne0\) throughout \(U\). It is therefore invertible under all Frobenius twists and iterations. The remaining one-dimensional block is \(c+1\), so the **stable** Hasse–Witt rank of \(G_{b,c}\) is three when \(c\ne-1\), and two when \(c=-1\). The matrix rank is the same, giving \(a(G_{b,c})=0\) or one. Adding the invariants of the three factors proves the asserted \(3\)-ranks and \(a\)-numbers. For a genus-three abelian variety of \(3\)-rank two, its remaining two Newton slopes are necessarily both \(1/2\); the slopes of the elliptic factors are ordinary or supersingular as above. This proves the three stated Newton polygons.

**Exact finite-field census.** Define \(A=\{c=0\}\), \(B=\{c=b^2\}\), and \(D=\{(c-1)^2+b^2=0\}\) inside \(\mathbb F_q^2\). The first two have \(q\) rational points and \(|A\cap B|=1\). If \(m\) is odd, \(-1\) is nonsquare and \(|D|=1\); if \(m\) is even, \(D\) is a pair of rational lines and \(|D|=2q-1\). In either case \(|A\cap D|=|B\cap D|=\epsilon_m\), with empty triple intersection. Inclusion–exclusion yields the asserted \(|U(\mathbb F_q)|\). The line \(b=0\) contributes \(q-2\) smooth parameters, while \(c=-1\) contributes \(q-\epsilon_m\); they meet at the unique smooth parameter \((0,-1)\). Thus rank two has one parameter, rank three has \((q-3)+(q-\epsilon_m-1)=2q-\epsilon_m-4\), and subtraction gives the rank-four count. All formulae hold for every \(m\ge1\).

## Verification

The supplied standalone `verify.py` independently enumerates all parameters over \(\mathbb F_3\), \(\mathbb F_9\), \(\mathbb F_{27}\), and \(\mathbb F_{81}\). It determines geometric smoothness through polynomial gcds, not by directly applying the claimed forbidden-parameter equations; it constructs the actual quotient polynomials and their Hasse matrices, computes stable Frobenius ranks by iteration, and compares to the symbolic predictions. Execute `python3 verify.py`. The expected rank counts \((N_2,N_3,N_4)\) are \((1,2,0)\), \((1,12,38)\), \((1,50,624)\), and \((1,156,6086)\), respectively. The program terminates with `VERIFY_OK`. These finite checks corroborate but do not replace the preceding proof for all \(m\).

## Relationship to prior work

Moriya and Kudo's 2023 genus-five Howe paper supplies the general fiber-product framework and a plane sextic model for its complementary quotient presentation, rather than a characteristic-three rank census. Kudo's companion 2024 paper constructs sextic models for the disjoint-elliptic-branch type but works in characteristic zero or at least five and classifies sextic singularities, not this arithmetic stratification. Later work by Kawakita treats Serre-bound point counts and by Ohashi treats superspecial constructions, principally in larger characteristic. None of the inspected relevant primary results gives the two transverse characteristic-three rank divisors and the uniform odd/even extension-degree parameter counts stated here. Previous arithmetic stratifications for other genus-three or genus-four families do not imply this genus-five fiber-product result. The decomposition theorem itself and the elementary Hasse–Witt recipe are standard prior tools, not asserted as new.

## Limitations

The result is a complete classification only for the stated fixed-coordinate two-parameter subfamily, not for all genus-five Howe curves, all curves with extra involutions, or abstract isomorphism classes. It does not classify the full Ekedahl–Oort type beyond the listed invariants, nor compute individual zeta functions. Literature coverage may be incomplete, especially older unindexed explicit arithmetic calculations. The numerical verifier establishes only its four finite-field cases.

## References

1. T. Moriya and M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, I*, arXiv:2310.15993v1 (first public 2023-10-24), https://arxiv.org/html/2310.15993v1.
2. M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760 (first public 2024-01-01), https://arxiv.org/abs/2401.00760.
3. M. Q. Kawakita, *Generalised Howe curves of genus five attaining the Serre bound*, arXiv:2412.03071 (2024), https://arxiv.org/abs/2412.03071.
4. R. Ohashi, *Superspecial generalized Howe curves of genus 4, 5, and 6 with completely decomposable Jacobians*, arXiv:2604.18074 (2026), https://arxiv.org/abs/2604.18074.
