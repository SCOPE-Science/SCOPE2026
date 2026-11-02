# Sharp symmetry-fiber zero transition for the quadratic B-spline Zak transform

## Finding

Let \(B_3=B_1*B_1*B_1\), where \(B_1\) is the indicator of \([-1/2,1/2]\). Use the scaled Zak transform
\[
Z_\lambda B_3(x,\nu)=\sqrt{\lambda}\sum_{k\in\mathbb Z}B_3(\lambda(x-k))e^{2\pi i k\nu}.
\]
For every real \(1/3<\lambda<1\), consider the symmetry fiber \(\nu\mapsto Z_\lambda B_3(1/2,\nu)\) on \(0\le\nu<1\). Set
\[
\lambda_*=\frac{99-2\sqrt{42}}{247}=0.3483340834137\ldots.
\]
Then this fiber has **exactly three distinct real-frequency zeros modulo one** when \(1/3<\lambda<\lambda_*\), namely \(\nu=1/2\) and a conjugate pair \(\nu_\lambda,1-\nu_\lambda\), with \(1/3<\nu_\lambda<1/2\). It has **exactly one distinct real-frequency zero modulo one**, \(\nu=1/2\), when \(\lambda_*\le\lambda<1\).

For \(1/3<\lambda<\lambda_*\), the extra frequency is determined exactly: \(\nu_\lambda=\pi^{-1}\arccos\sqrt{y_\lambda}\), where \(y_\lambda\) is the unique root in \((0,1)\) of
\[
P_\lambda(y)=8(7\lambda-3)^2y^3-12(53\lambda^2-44\lambda+9)y^2
 +3(95\lambda^2-76\lambda+15)y-\frac{247\lambda^2-198\lambda+39}{8}.
\]
The extra zeros coalesce with \(1/2\) at the exact transition. The central zero has multiplicity three at \(\lambda=\lambda_*\); the same multiplicity also occurs at \(\lambda=1/2\), without an additional distinct frequency. The assertion concerns **only this symmetry fiber**, not the two-dimensional Zak zero set or the Gabor frame set.

## Assumptions and scope

The order-three spline \(B_3\) is the *quadratic*, centered cardinal B-spline, explicitly
\[
B_3(t)=\begin{cases}3/4-t^2,&|t|\le1/2,\\(3/2-|t|)^2/2,&1/2<|t|<3/2,\\0,&|t|\ge3/2.\end{cases}
\]
The restriction \(\lambda>1/3\) is natural: then only the first four pairs of spline samples can contribute to the Zak symmetry fiber; at \(\lambda=1/3\), an integer-reciprocal aliasing configuration occurs. The result is for all **real**, not merely rational, scales in \((1/3,1)\). All equalities at internal knot values are interpreted using the continuous spline.

## Proof

Write \(\vartheta=\pi\nu\), \(y=\cos^2\vartheta\), and \(a_j(\lambda)=B_3(\lambda(j+1/2))\). Pairing the terms with indices \(-j\) and \(j+1\) yields the exact identity
\[
Z_\lambda B_3(1/2,\nu)=2\sqrt\lambda e^{\pi i\nu}\sum_{j=0}^3a_j(\lambda)\cos((2j+1)\vartheta),
\]
with any absent terms understood as zero. The sum always contains the factor \(\cos\vartheta\), hence \(\nu=1/2\) is a zero. Since \(\cos(\pi\nu)=0\) exactly at this frequency modulo one, every *additional* zero is determined by a real root \(0<y\le1\) of the remaining polynomial. The value \(y=1\) corresponds to \(\nu=0\).

**Four contributing pairs: \(1/3<\lambda<3/7\).** Here
\[
(a_0,a_1,a_2,a_3)=\left(\frac{3-\lambda^2}{4},\frac{(3-3\lambda)^2}{8},\frac{(3-5\lambda)^2}{8},\frac{(3-7\lambda)^2}{8}\right).
\]
Using \(\cos(3\vartheta)/\cos\vartheta=4y-3\), \(\cos(5\vartheta)/\cos\vartheta=16y^2-20y+5\), and \(\cos(7\vartheta)/\cos\vartheta=64y^3-112y^2+56y-7\), the remaining factor is exactly \(P_\lambda(y)\) displayed above. Its discriminant in \(y\) is
\[
81(3\lambda-1)^4D(\lambda),\qquad
D(\lambda)=48621\lambda^4-95084\lambda^3+67662\lambda^2-20844\lambda+2349.
\]
This discriminant is strictly negative for all \(1/3<\lambda<3/7\), by an exact sign certificate. Put \(\lambda=1/3+(2/21)t\) with \(0\le t\le1\). In the degree-four Bernstein basis \(\binom4k t^k(1-t)^{4-k}\), the five coefficients of \(D\) are, in order,
\[
-\frac{64}{27},\quad-\frac{1472}{189},\quad-\frac{832}{147},\quad-\frac{864}{343},\quad-\frac{2160}{2401}.
\]
Thus \(P_\lambda\) has precisely **one distinct real root on the entire real line** for these \(\lambda\). Moreover
\[
P_\lambda(1)=\frac{3(27\lambda^2-30\lambda+11)}8>0,
\qquad
P_\lambda(1/4)=\frac{3(3\lambda-1)^2}{4}>0,
\qquad
P_\lambda(0)=-\frac{247\lambda^2-198\lambda+39}{8}.
\]
The quadratic in the first inequality has negative discriminant. The second value is negative on \((1/3,\lambda_*)\), zero at \(\lambda_*\), and positive on \((\lambda_*,3/7)\). Because the cubic has positive leading coefficient and one real root, that root lies in \((0,1)\) precisely for \(1/3<\lambda<\lambda_*\). At \(\lambda_*\) it equals zero, which produces no new *distinct* frequency. In fact \(P_{\lambda_*}'(0)=(594-12\sqrt{42})/3211>0\), proving a cubic-order central zero. By continuity, \(y_\lambda\to1/4\) as \(\lambda\downarrow1/3\), since \(P_{1/3}(y)=(4y-1)^3/18\); hence \(\nu_\lambda\to1/3\). Likewise \(y_\lambda\to0\) as \(\lambda\uparrow\lambda_*\), so \(\nu_\lambda\to1/2\).

**Three contributing pairs: \(3/7\le\lambda<3/5\).** Now \(a_3=0\), and the quotient by \(\cos\vartheta\) becomes
\[
Q_\lambda(y)=2(5\lambda-3)^2y^2-2(29\lambda^2-33\lambda+9)y+3(2\lambda-1)^2.
\]
Its discriminant is \(4E(\lambda)\), where
\[
E(\lambda)=241\lambda^4-594\lambda^3+525\lambda^2-198\lambda+27.
\]
On \([3/7,23/50]\), \(E<0\): its Bernstein coefficients after the affine substitution \(\lambda=3/7+(23/50-3/7)t\) are
\[
-\frac{135}{2401},\quad-\frac{1773}{34300},\quad-\frac{10469}{245000},\quad-\frac{53811}{1750000},\quad-\frac{105719}{6250000}.
\]
Since the quadratic's leading coefficient is strictly positive, \(Q_\lambda(y)>0\) for all real \(y\) on this subinterval. On \([23/50,3/5)\), its coefficients of \(y^2\) and \(y\) are strictly positive: the latter follows from \(29\lambda^2-33\lambda+9<0\), because this convex quadratic is negative at both endpoints. Its constant term is nonnegative, with equality only at \(\lambda=1/2\). Hence \(Q_\lambda(y)>0\) for all \(y>0\) throughout this entire second scale range. At \(\lambda=1/2\), \(Q_\lambda(0)=0\) and \(Q_\lambda'(0)>0\), so the central frequency alone has multiplicity three.

**Two contributing pairs: \(3/5\le\lambda<1\).** The quotient becomes
\[
L_\lambda(y)=\frac{9(1-\lambda)^2}{2}y+\frac{-29\lambda^2+54\lambda-21}{8}.
\]
Both terms are nonnegative for \(0\le y\le1\), and the constant is strictly positive for \(3/5\le\lambda<1\): the concave quadratic numerator is positive at both endpoints of that interval. Therefore no extra frequency occurs here either. Together the three cases establish the zero count and both stated multiplicities.

## Verification

Run `python CHECK.py` with SymPy and NumPy installed. The code checks the sample-reduction coefficients, cubic and quadratic discriminants, the two exact Bernstein sign certificates, both degeneracy identities, positivity endpoint identities, and supplementary numerical zero counts. It reports `CHECK_OK 41` in the tested environment. The proof above uses **exact universal symbolic certificates** for all real scale parameters; the sampled zero counts are supplementary and are not used in the proof.

## Relationship to prior work

Hasannasab and Lemvig (arXiv:2609.13116, first posted 2026-09-11) give a full zero-set classification for the hat spline, describe higher-order splines for scales above one, and examine palindromic polynomials along the \(x=1/2\) symmetry line for smaller scales. Their Section 6 includes an order-three illustrative example with a restricted reciprocal-scale condition, but the accessible text does not state this complete interval-wide transition or the critical value \(\lambda_*\). The displayed equations for that example were not fully recoverable from the available rendering, leaving a specific comparison risk. Lemvig (arXiv:2601.07642) proves Gabor frame obstructions for general B-splines, not this real-frequency zero-count phase diagram. Stangl and Frederick (arXiv:2609.00481) study the **order-two hat spline**, not the order-three quadratic spline. An earlier related investigation of the **different fiber** \(x=0\) for reciprocal scale \(2<b<8/3\) does not imply the present \(x=1/2\) zero count on \(1/3<\lambda<1\). The result concerns a symmetry fiber, not a full two-dimensional or frame-set classification.

## Limitations

The classification does not treat \(0<\lambda\le1/3\), any fiber \(x\ne1/2\), higher spline orders, or whether an identified zero causes a Gabor-frame failure. Its originality assessment is provisional without an independent literature audit; the unavailable displayed formulas in the most closely related Section 6 are a material residual comparison risk. No numerical check can replace the exact sign certificates.

## References

1. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116 (first public version 2026-09-11), https://arxiv.org/abs/2609.13116.
2. J. Lemvig, *A new family of hyperbolic slits in the Gabor frame set of B-spline generators*, arXiv:2601.07642 (first public version 2026-01-12), https://arxiv.org/abs/2601.07642.
3. A. Stangl and C. Frederick, *The frameset of the second-order B-Spline along ab=1/q*, arXiv:2609.00481 (first public version 2026-08-31), https://arxiv.org/abs/2609.00481.
