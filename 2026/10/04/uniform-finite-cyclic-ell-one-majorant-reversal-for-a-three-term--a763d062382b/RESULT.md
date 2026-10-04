# Uniform finite-cyclic ell-one majorant reversal for a three-term arithmetic progression
## Finding
Let \(N\ge3\), let \(d\in\mathbb Z_N\), and suppose the character
\[
\chi_d(x)=e^{2\pi i dx/N}
\]
has order \(L=N/\gcd(N,d)\ge3\). Equip \(\mathbb Z_N\) with normalized counting measure and define
\[
F_+(x)=1+\chi_d(x)+\chi_{2d}(x),\qquad
F_-(x)=1+\chi_d(x)-\chi_{2d}(x).
\]
Then
\[
\lVert F_-\rVert_1>\lVert F_+\rVert_1
\]
for every such \(N,d\). More precisely, when \(L=3\), the two norms are \(1\) and \(5/3\); when \(L=4\), they are \(3/2\) and \((1+\sqrt5)/2\). For every \(L\ge5\),
\[
\lVert F_+\rVert_1\le\frac{25}{16},\qquad
\lVert F_-\rVert_1\ge\frac{1+\sqrt5}{2},
\]
and consequently
\[
\lVert F_-\rVert_1-\lVert F_+\rVert_1\ge\frac{8\sqrt5-17}{16}>0.
\]
Thus the simplest three-term arithmetic-progression idempotent exhibits a Hardy--Littlewood majorant reversal on every nondegenerate finite cyclic quotient, with a modulus-independent gap once the quotient order is at least five.

## Assumptions and scope
The norm is the normalized \(\ell^1\) norm
\[
\lVert f\rVert_1=\frac1N\sum_{x\in\mathbb Z_N}\lvert f(x)\rvert.
\]
The hypothesis \(L\ge3\) is exactly the nondegeneracy condition that the three characters \(1,\chi_d,\chi_{2d}\) are distinct. No assertion is made here for more general three-frequency sets, other exponents, or arbitrary coefficient magnitudes.

## Proof
Multiplication by a character does not change absolute value. The map \(x\mapsto\chi_d(x)\) takes every \(L\)-th root of unity exactly \(N/L\) times, so both normalized norms depend only on \(L\). Write
\[
z_k=e^{2\pi i k/L},\qquad \theta_k=\frac{2\pi k}{L}.
\]
For the all-positive sum,
\[
\lvert1+z_k+z_k^2\rvert=\lvert1+2\cos\theta_k\rvert.
\]
Put \(x=1+2\cos\theta\), so \(-1\le x\le3\), and define
\[
q(x)=\frac{15}{32}+\frac{9}{16}x^2-\frac1{32}x^4.
\]
For \(0\le x\le3\),
\[
32\bigl(q(x)-x\bigr)=(3-x)(x-1)^2(x+5)\ge0,
\]
while for \(-1\le x\le0\),
\[
32\bigl(q(x)+x\bigr)=(5-x)(x+1)^2(x+3)\ge0.
\]
Hence \(q(x)\ge\lvert x\rvert\) throughout \([-1,3]\).

For \(L\ge5\), root-of-unity orthogonality sees no alias among frequencies of absolute value at most four. Since \(x=1+z+z^{-1}\), the constant coefficients of \(x^2\) and \(x^4\) are respectively \(3\) and \(19\). Therefore
\[
\frac1L\sum_{k=0}^{L-1}x_k^2=3,\qquad
\frac1L\sum_{k=0}^{L-1}x_k^4=19,
\]
and
\[
\lVert F_+\rVert_1\le\frac1L\sum_{k=0}^{L-1}q(x_k)
=\frac{15}{32}+\frac{27}{16}-\frac{19}{32}
=\frac{25}{16}.
\]

For the signed sum, multiplication by \(z_k^{-1}\) gives
\[
\lvert1+z_k-z_k^2\rvert
=\lvert1-2i\sin\theta_k\rvert
=\sqrt{1+4\sin^2\theta_k}.
\]
The function \(u\mapsto\sqrt{1+4u}\) is concave on \([0,1]\), so it lies above its endpoint chord:
\[
\sqrt{1+4u}\ge1+(\sqrt5-1)u.
\]
For every \(L\ge3\), root-of-unity orthogonality gives
\[
\frac1L\sum_{k=0}^{L-1}\sin^2\theta_k=\frac12.
\]
Thus
\[
\lVert F_-\rVert_1\ge1+\frac{\sqrt5-1}{2}=\frac{1+\sqrt5}{2}.
\]
For \(L\ge5\), comparison with \(25/16\) yields the stated gap because \(8\sqrt5>17\).

The two remaining quotient orders are direct. For \(L=3\), the magnitudes of \(1+z+z^2\) are \(3,0,0\), whereas those of \(1+z-z^2\) are \(1,2,2\), giving \(1<5/3\). For \(L=4\), the corresponding averages are \(3/2\) and \((1+\sqrt5)/2\).

## Verification
The bundled verifier checks the two polynomial factorizations with exact integer arithmetic, reconstructs the constant coefficients \(3\) and \(19\) by Laurent-polynomial convolution, verifies the special cases \(L=3,4\), and numerically stress-tests every quotient order \(5\le L\le1000\). These computations corroborate the proof; the theorem itself follows from the identities and inequalities above for all \(L\).

## Relationship to prior work
Krenedits proved the continuous-circle three-term majorant reversal for \(1+e_1\pm e_2\) at every \(0<p<2\), hence in particular at \(p=1\). That continuous result does not imply a comparison of every finite root-of-unity average: a discrete average can reverse inequalities that hold after integration. Krenedits also reports that Mockenhaupt's 1996 thesis contains a discrete uniform inequality in a different regime, connected to \(1+e_1\pm e_3\) for exponents between two and four; the cited description does not cover the present exponent-one, consecutive-frequency statement.

Bonami and Révész explicitly place \(L^1\) idempotent questions on finite cyclic groups and study concentration on \(\mathbb Z/q\mathbb Z\). Their finite-group results concern concentration constants and Littlewood-type lower bounds rather than the signed-versus-positive three-term comparison proved here. The present theorem therefore isolates an exact finite-cyclic persistence phenomenon at the smallest nontrivial three-frequency arithmetic progression.

## Limitations
The result is specific to exponent one and to a three-term arithmetic progression with equal coefficient magnitudes. The uniform constants \(25/16\) and \((1+\sqrt5)/2\) are certificates, not claimed to equal the two norms for \(L\ge5\). The original full text of Mockenhaupt's 1996 Habilitationsschrift was not available for direct inspection; the comparison with its Example 3.4 uses Krenedits' detailed secondary description, which places that example in a different exponent and frequency regime.

## References
1. A. Bonami and Sz. Gy. Révész, *Concentration of the integral norm of idempotents*, arXiv:0811.4576v1, first public 2008-11-27. Primary MSC 42A05.
2. S. Krenedits, *Three-term idempotent counterexamples in the Hardy--Littlewood majorant problem*, arXiv:1006.0409v1, first public 2010-06-02. Primary MSC 42A05.
3. G. Mockenhaupt, *Bounds in Lebesgue Spaces of Oscillatory Integral Operators*, Habilitationsschrift, Universität-Gesamthochschule-Siegen, 1996; comparison to Example 3.4 is based on the description in Krenedits' paper.
