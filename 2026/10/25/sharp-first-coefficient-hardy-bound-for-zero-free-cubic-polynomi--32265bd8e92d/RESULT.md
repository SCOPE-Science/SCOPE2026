# Sharp first-coefficient Hardy bound for zero-free cubic polynomials

## Finding

Let \(p(z)=a_0+a_1z+a_2z^2+a_3z^3\) be a nonzero complex polynomial of degree at most three, with **no zeros in the open unit disk**. In the classical Hardy norm
\[
\|p\|_{H^2}^2=\frac{1}{2\pi}\int_0^{2\pi}|p(e^{it})|^2\,dt=\sum_{j=0}^{3}|a_j|^2,
\]
the exact coefficient inequality is
\[
\boxed{\quad |a_1|^2\le\frac7{10}\|p\|_{H^2}^2.\quad}
\]
Equivalently,
\[
3|a_1|^2\le7\bigl(|a_0|^2+|a_2|^2+|a_3|^2\bigr).
\]
Equality for a nonzero polynomial holds **exactly** for
\[
\boxed{\quad p(z)=C\,(1+\eta z)^2(1-\eta z/4),
\qquad C\in\mathbb C\setminus\{0\},\quad |\eta|=1.\quad}
\]
In particular, two zeros of every extremizer lie together on the unit circle, while its third zero lies at four times their radial distance on the opposite ray. The closed-boundary zeros are allowed by the open-disk zero-free assumption.

## Assumptions and scope

The domain of nonvanishing is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), not its closure. The polynomial may have degree less than three; its missing coefficients are zero. Every nonzero such polynomial has \(a_0\ne0\), and it factors as
\[
p(z)=a_0\prod_{j=1}^3(1+x_jz),\qquad |x_j|\le1,
\]
where some \(x_j\) may vanish. All three complex factor parameters are arbitrary, with no assumption that they are real or have aligned phases. The Fourier normalization in the finding is part of the statement.

## Proof

**1. Reduce to a three-root inequality.** Set \(e_1=x_1+x_2+x_3\), \(e_2=x_1x_2+x_1x_3+x_2x_3\), and \(e_3=x_1x_2x_3\). Since \(a_j=a_0e_j\) for \(j=1,2,3\), it is enough to establish
\[
F:=7(1+|e_2|^2+|e_3|^2)-3|e_1|^2\ge0.
\]
Write \(x_j=r_je^{i\theta_j}\), with \(0\le r_j\le1\) (the phase at zero is arbitrary). Put
\[
F_0=7\left(1+\sum_{i<j}r_i^2r_j^2+r_1^2r_2^2r_3^2\right)-3\sum_{j=1}^3r_j^2.
\]
Expansion of the two elementary symmetric functions yields the exact identity
\[
F=F_0+2\sum_{i<j}r_ir_j(7r_k^2-3)\cos(\theta_i-\theta_j),
\]
where \(k\) is the unique index outside \(\{i,j\}\). Consequently,
\[
F\ge F_*=F_0-2\sum_{i<j}r_ir_j|7r_k^2-3|.
\]
Thus it suffices to prove a symmetric real inequality on the closed unit cube.

**2. Exact positive Bernstein certificates in three sign regions.** Call a radius *high* if \(r_j\ge\sqrt{3/7}\) and *low* otherwise. Since \(13/20<\sqrt{3/7}<2/3\), a low coordinate belongs to \([0,2/3]\), and a high coordinate belongs to \([13/20,1]\). In each fixed sign region, remove the absolute values in \(F_*\). If there are exactly zero, one, or three high coordinates, the resulting polynomial is nonnegative on its slightly larger rational box. In fact its degree-four tensor-product Bernstein coefficients are **strictly positive**. Exact lower bounds on all those coefficients, respectively, are
\[
\begin{array}{c|c|c}
\text{number of high radii}&\text{rational product box}&\text{smallest degree-four Bernstein coefficient}\\\hline
0 &[0,2/3]^3&247/81\\
1 &[13/20,1]\times[0,2/3]^2&344/729\\
3 &[13/20,1]^3&2
\end{array}
\]
The unshown permutations are equivalent by symmetry. These entries are not samples of the function: they are coefficients in an exact nonnegative partition-of-unity basis and thus certify strict positivity throughout the relevant boxes. The standalone `verify.py` constructs every coefficient using integer binomial coefficients and rational arithmetic.

**3. The two-high region and its unique equality point.** By symmetry write \(r_1=a\), \(r_2=b\), and \(r_3=c\), where \(a,b\ge\sqrt{3/7}\) and \(c\le\sqrt{3/7}\). Here the sign pattern is compatible with phases \(0,0,\pi\), and the lower bound is the following real quadratic in \(c\):
\[
F_*=7\left(1+(ab-c(a+b))^2+a^2b^2c^2\right)-3(a+b-c)^2
=A c^2+2Bc+C,
\]
where
\[
\begin{aligned}
A&=7((a+b)^2+a^2b^2)-3,\\
B&=(a+b)(3-7ab),\\
C&=7(1+a^2b^2)-3(a+b)^2.
\end{aligned}
\]
Since \(a,b\ge13/20\), we have \(A\ge883/100>0\). Define the discriminant complement \(D=AC-B^2\). Substituting \(u=1-a\), \(v=1-b\), both in \([0,7/20]\), yields an exact polynomial of bidegree at most four:
\[
D=(7((a+b)^2+a^2b^2)-3)(7(1+a^2b^2)-3(a+b)^2)
-(a+b)^2(3-7ab)^2.
\]
All \(9\times9\) tensor-product degree-eight Bernstein coefficients of \(D\) on \([0,7/20]^2\) are nonnegative. Exactly one coefficient vanishes: the corner coefficient indexed by \((0,0)\); all eighty others are strictly positive. Hence \(D\ge0\), with equality only at \(u=v=0\), i.e. \(a=b=1\). It follows that
\[
F_*=A\left(c+\frac BA\right)^2+\frac DA\ge0.
\]
At \(a=b=1\) the quadratic reduces to \(F_*=32(c-1/4)^2\). Consequently \(F_*=0\) precisely when the radii are a permutation of \((1,1,1/4)\).

**4. Recover phases and the sharp constant.** In the equality case all three pair-coupling coefficients in Step 1 are nonzero. Equality in the estimate \(\cos(\theta_i-\theta_j)\ge-1\) after multiplying by each signed coefficient requires the two unit-modulus factors to have equal phases and the one-quarter factor to have the opposite phase. Thus \((x_1,x_2,x_3)\), up to permutation, equals \((\eta,\eta,-\eta/4)\), \(|\eta|=1\). This gives exactly the extremizing polynomials in the finding.

For \(p(z)=(1+z)^2(1-z/4)\), the coefficients are \((1,7/4,1/2,-1/4)\), so \(\|p\|_{H^2}^2=35/8\) and \(|a_1|^2=49/16\). Their quotient is \(7/10\). Finally, \(F\ge0\) rearranges to \(3|a_1|^2\le7(\|p\|_{H^2}^2-|a_1|^2)\), giving the claimed \(7/10\) constant. No numerical approximation is used in the proof.

## Verification

The standalone `verify.py` uses only the Python standard library, with exact `Fraction` arithmetic. Run `python verify.py`. The checker expands the relevant multivariate polynomials, converts their monomials to tensor Bernstein coefficients on the stated rational boxes, asserts their nonnegativity and their exact count of zeros, and independently checks the normalized extremizer. A successful execution prints `CHECK_OK` and the four certificate lines with minimum coefficients \(247/81\), \(344/729\), \(2\), and \(0\), the last with exactly one zero.

The polynomial-to-Bernstein conversion follows from the identity
\[
t^j=\sum_{i=j}^{n}\frac{\binom{i}{j}}{\binom{n}{j}}\binom ni t^i(1-t)^{n-i}
\qquad(0\le j\le n,\ 0\le t\le1),
\]
applied after affine substitution on each coordinate. Hence the finite checks establish explicit exact polynomial identities and coefficient inequalities that cover the entire continuous cubes; they are not point-grid experiments.

## Relationship to prior work

Krushkal's July 2026 preprint and September 2026 study of polynomial-coefficient evaluation supply a general structural comparison between coefficients of zero-free polynomials and states its new explicit degree theory for degrees at least five. The work distinguishes degrees below five as requiring additional analysis; it does not give the numerical sharp first Hardy coefficient \(\sqrt{7/10}\) or classify the cubic extremizer by root locations. Earlier work on the Hummel–Scheinberg–Zalcman problem supplies the global Hardy-space coefficient bound \(\sqrt{2/e}\), which is strictly weaker for cubic polynomials and therefore does not imply the exact finite-degree constant.

The present statement is only about degree at most three, the first Taylor coefficient, the coefficient Euclidean/Hardy \(H^2\) norm, and zero-freeness in the open disk. General results for univalent functions, arbitrary degrees, other coefficient indices, and other norms do not automatically imply it. The present proof is a direct finite-degree sharp inequality with complete equality classification.

## Limitations

No claim is made for degrees four or higher, other coefficients, other \(H^p\) exponents, zero-free disks of different radii without rescaling, or zero-free polynomials in several variables. The boundary-double-root maximizer does not satisfy zero-freeness on the *closed* unit disk; for strictly zero-free closed-disk polynomials the same constant is the supremum obtained by radial approximation, but it is not attained. Historical-priority uncertainty persists because the earlier coefficient-extremal literature is extensive, and some relevant full texts could not be inspected in their entirety. No independent mathematical audit has been performed.

## References

1. S. L. Krushkal, *A General Theorem on Sharp Evaluation of Polynomial Coefficients*, **Axioms** 15 (2026), 699, published 19 September 2026. DOI: `10.3390/axioms15090699`. See Theorems 1–2 and Section 5.
2. S. L. Krushkal, *A new method for evaluation of polynomial coefficients*, arXiv:2607.20870, first submitted 23 July 2026. This is the earliest verified publicly available source in the motivating line. Abstract and bibliographic record inspected; its complete preprint was not accessible during this comparison.
3. S. L. Krushkal, *Two Coefficient Conjectures for Nonvanishing Hardy Functions, I*, **Journal of Mathematical Sciences** 268 (2022), 199–221. DOI: `10.1007/s10958-022-06192-1`.
4. J. A. Hummel, S. Scheinberg, L. Zalcman, *A coefficient problem for bounded nonvanishing functions*, **Journal d'Analyse Mathématique** 31 (1977), 169–190.
