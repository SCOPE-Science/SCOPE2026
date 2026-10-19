# Sharp convex amplitude chamber for maximal Cauchy-wavelet zeros of positive pulse trains

## Finding
For an arbitrary finite train of separated positive rectangular pulses, the analytic first-order Cauchy-wavelet transform has at most \(n-1\) zeros in the upper half-plane, counted with their complex-analytic multiplicities. The amplitudes attaining this maximum form an explicitly characterized, nonempty, open **convex cone**. Its boundary is characterized by the creation of real multiple zeros. For two pulses, the resulting amplitude-versus-gap transition has a closed-form sharp threshold.

Let \(I_j=[a_j,b_j]\), \(\ell_j=b_j-a_j>0\), and define
\[
F_w(z)=\int_{\mathbb R}\frac{\sum_{j=1}^n w_j\mathbf 1_{I_j}(t)}{(z-t)^2}\,dt
=\sum_{j=1}^n\frac{w_j\ell_j}{(z-a_j)(z-b_j)}.
\]
For each \(k\), set
\[
\Phi_k(x;w)=\sum_{j\ne k}w_j\frac{\ell_j}{\ell_k}\,
\frac{(x-a_k)(b_k-x)}{(x-a_j)(x-b_j)}\qquad(a_k\le x\le b_k).
\]
The chamber \(\mathcal C\) is the set of positive amplitude vectors satisfying
\[
  w_k>\max_{x\in[a_k,b_k]}\Phi_k(x;w)\quad\text{for every }k.
\]
Then the total upper-half-plane zero multiplicity of \(F_w\) equals \(n-1\) **if and only if** \(w\in\mathcal C\). All equal-weight vectors are in \(\mathcal C\).

For \(n=2\), write the interval lengths as \(\ell_1,\ell_2\), their intervening gap as \(g=a_2-b_1\), and their amplitude ratio as \(r=w_1/w_2\). The exact condition becomes
\[
 \boxed{g(g+\ell_1+\ell_2)>\ell_1\ell_2\sinh^2\!\left(\tfrac12\log r\right)}.
\]
It yields one simple upper-half-plane zero in the strict regime, one double **real** zero at equality, and two distinct real zeros in the reverse regime. Thus the sharp contrast tolerated by a given pulse separation is exact.

## Assumptions and scope
Fix \(n\ge1\), \(a_1<b_1<a_2<b_2<\cdots<a_n<b_n\) real, and \(w_j>0\). The function \(f(t)=\sum_jw_j\mathbf 1_{[a_j,b_j]}(t)\) lies in \(L^2(\mathbb R)\). Zeros are those of the holomorphic factor \(F_w\) for \(\operatorname{Im}z>0\), and are counted with multiplicity. This factor differs only by a nowhere-zero scale-dependent multiplier from the continuous transform using the first-order analytic Cauchy wavelet with positive-frequency profile proportional to \(\omega e^{-2\pi\omega}\). The present theorem does not count any zeros on the lower half-plane independently; they are complex conjugates of those above.

## Proof
**1. Degree and noncancellation.** Integrating each pulse gives the displayed rational expression. With \(D(z)=\prod_j(z-a_j)(z-b_j)\), the numerator \(P_w=D F_w\) has degree exactly \(2n-2\), since its leading coefficient is \(\sum_j w_j\ell_j>0\). At each endpoint \(a_k\) or \(b_k\), only the \(k\)-th term of \(P_w\) survives, and it is nonzero because intervals are disjoint and all weights are positive. Consequently no pole cancels, and all finite zeros of \(F_w\) are precisely those of this real-coefficient polynomial. The upper-half-plane zero multiplicity cannot exceed half the total polynomial degree, namely \(n-1\).

**2. Real-axis signs and the exact amplitude chamber.** For real \(x\) outside the union of all the intervals, each denominator \((x-a_j)(x-b_j)\) is strictly positive; therefore \(F_w(x)>0\). Within \((a_k,b_k)\), the \(k\)-th summand is negative and all other summands are positive. Multiplication by the strictly positive quantity \((x-a_k)(b_k-x)/\ell_k\) yields the equivalence
\[
 F_w(x)<0\quad\Longleftrightarrow\quad w_k>\Phi_k(x;w).
\]
As \(x\) approaches either endpoint from *inside* its interval, \(F_w(x)\to-\infty\), because the own-pulse term dominates. Since each \(\Phi_k\) extends continuously to the closed interval and vanishes at both endpoints, \(F_w\) has no real zeros exactly when all chamber inequalities hold. Indeed, if any inequality fails, \(F_w\) is nonnegative at some interior point and negative at the interval endpoints, producing at least one real zero, including the tangential equality case. Conversely, strict inequalities make \(F_w\) negative throughout each interval and positive elsewhere. The real-coefficient polynomial \(P_w\) has no real root exactly in \(\mathcal C\), which by conjugate pairing is equivalent to attaining \(n-1\) upper-half-plane zeros counted with multiplicity.

For every fixed \(k,x\) the inequality \(w_k>\Phi_k(x;w)\) is a strict homogeneous **linear** inequality in the amplitude vector. Their intersection with the positive orthant is therefore a convex cone; compactness of the intervals and strictness of the finitely many maximum inequalities make it open.

**3. Nonemptiness.** Put \(w_j=c>0\) for all \(j\), and define
\[
 R(z)=\prod_{j=1}^n\frac{z-a_j}{z-b_j}.
\]
The zeros and poles strictly interlace on the real line. Its partial fractions are \(R(z)=1+\sum_j\rho_j/(z-b_j)\), where
\[
\rho_j=(b_j-a_j)\prod_{m\ne j}\frac{b_j-a_m}{b_j-b_m}>0.
\]
Each factor in the product is positive by the interval order. Therefore \(R'(x)=-\sum_j\rho_j/(x-b_j)^2<0\) on the real line away from poles. Since \(R(x)<0\) on every \((a_k,b_k)\), the identity
\[
\frac{F_{(c,\ldots,c)}(x)}{c}=-\frac{R'(x)}{R(x)}
\]
shows strict negativity there. Thus equal positive amplitudes lie inside \(\mathcal C\) and the cone is nonempty.

**4. Boundary degeneracy.** Let \(w\) have positive entries and lie on the relative boundary of \(\mathcal C\) within the positive orthant. At least one inequality has equality: for some \(k\) and some interior maximizer \(x_*\in(a_k,b_k)\), \(w_k=\Phi_k(x_*;w)\). The function \(w_k-\Phi_k(x;w)\) has a local minimum of zero there, so it and its first derivative vanish. The sign identity in Step 2 then yields \(F_w(x_*)=F_w'(x_*)=0\). Thus the transition passes through a multiple real zero. No assertion of generic multiplicity exactly two is needed for arbitrary \(n\).

**5. Exact two-pulse threshold and root locations.** Let \(m_j=(a_j+b_j)/2\), \(\delta=m_2-m_1=g+(\ell_1+\ell_2)/2\), \(A=w_1\ell_1\), \(B=w_2\ell_2\), and \(C=A+B\). The numerator is the quadratic
\[
P_w(z)=A\big((z-m_2)^2-\ell_2^2/4\big)
+B\big((z-m_1)^2-\ell_1^2/4\big).
\]
Completing the square gives \(P_w(z)=C((z-M)^2+Y^2)\), where
\[
M=\frac{A m_2+B m_1}{C},\qquad
Y^2=\frac{AB\delta^2}{C^2}-\frac{A\ell_2^2+B\ell_1^2}{4C}.
\]
A simple algebraic rearrangement shows \(Y^2>0\) precisely when
\[
4\delta^2>\ell_1^2+\ell_2^2+(r+r^{-1})\ell_1\ell_2,
\]
which is exactly the strict gap/contrast inequality in the Finding. For \(Y^2>0\), the roots are \(M\pm i\sqrt{Y^2}\); for \(Y^2=0\), they coalesce in a double real root; for \(Y^2<0\), they are distinct real roots \(M\pm\sqrt{-Y^2}\). The transition is exact for every positive gap, positive pulse widths, and positive weights. This completes the proof.

## Verification
The accompanying `checker.py` performs **96 exact-rational test cases**. These include numerator degrees, endpoint noncancellation, independent rational transform evaluations for up to five pulses, positive partial-fraction residues and upper-half-plane root counts in equal-height examples, and algebraic-discriminant/root checks of the two-pulse transition over four geometries and seven weight ratios each. The saved `checker_output.txt` contains the actual run result. All symbolic and finite checks passed. These checks corroborate the proof but cannot replace the argument for arbitrary \(n\) or continuously varying weights.

## Relationship to prior work
Mallat and Waldspurger (first public version 2014) develop the analytic Cauchy-wavelet transform as a holomorphic object and analyze phase retrieval and stability; that framework supplies the wavelet setting, not the present positive pulse-train amplitude chamber. Abakumov, Baranov, and Belov (2013) treat localization of zeros in spaces of Cauchy transforms of discrete measures, with a distinct zero-localization problem. Classical results about critical points of rational functions give additional nearby theory and are a residual priority risk: the equal-amplitude product formula in Step 3 is an interlacing argument of classical type. The proposed contribution here is the **sharp parameter-space characterization for all positive amplitudes**, the convexity/nonemptiness theorem, and its exact two-pulse contrast boundary. No assertion of universal publication priority is made.

## Limitations
Strict disjointness of the intervals and positivity of all amplitudes are essential hypotheses; touching or overlapping intervals are not covered. The chamber's defining maxima generally require a one-variable optimization on each interval; no closed-form general \(n\)-parameter boundary is claimed. Multiplicity \(n-1\) is counted with multiplicity and does not imply all upper zeros are distinct for \(n\ge3\). The arbitrary-size boundary yields a real zero of multiplicity at least two, not necessarily exactly two. These are ideal rectangular signals with exact data, not robust noise guarantees. An older rational-function zero-locus theorem may contain an equivalent characterization; the available searches do not certify absolute novelty.

## References
1. S. Mallat and I. Waldspurger, *Phase retrieval for the Cauchy wavelet transform*, initial arXiv submission 2014-04-04, https://arxiv.org/abs/1404.1183 .
2. E. Abakumov, A. Baranov, and Y. Belov, *Localization of zeros for Cauchy transforms*, initial arXiv submission 2013-12-23, https://arxiv.org/abs/1312.6706 .
3. J. L. Walsh, *The Location of Critical Points of Analytic and Harmonic Functions*, classical monograph on rational-function critical points; contextual rather than a claimed source for the new chamber criterion.
