# Uniform quadratic small-skew law and extremizer rigidity in real \(L_4\)

## Finding
Let \(X=L_4(\Omega,\mu;\mathbb R)\) have dimension at least two. For \(1\le t<\infty\) and \(\tau\ge0\) write
\[
S_{X,t}(\tau)=\inf_{\|x\|_4=\|y\|_4=1}
\left(\frac{\|x+\tau y\|_4^t+\|\tau x-y\|_4^t}{2}\right)^{1/t},
\]
and for \(t=\infty\) replace the mean by the maximum of the two norms.
There are absolute constants \(\tau_0>0\) and \(K<\infty\), independent of the measure space and of \(1\le t\le\infty\), such that
\[
\boxed{\left|S_{X,t}(\tau)-1+\frac{\tau}{2\sqrt2}-\frac{9\tau^2}{16}\right|\le K\tau^3\quad(0\le\tau\le\tau_0).}
\]
Thus both the first and second small-skew coefficients are exactly **independent of the outer power-mean exponent**, including the maximum-norm endpoint. This is an asymptotic statement, not equality of the entire functions \(S_{X,t}\) for different exponents.

For all unit \(x,y\in X\), an exact stability identity holds:
\[
\boxed{\left\|x^2-y^2+\sqrt2\,xy\right\|_2^2
=2+2\sqrt2\int xy(x^2-y^2)\,d\mu.}
\]
Consequently, the antisymmetric normalized-duality pairing has the sharp value
\[
\inf_{\|x\|_4=\|y\|_4=1}\int xy(x^2-y^2)\,d\mu=-\frac1{\sqrt2}.
\]
Equality holds precisely when \(x^2-y^2+\sqrt2xy=0\) almost everywhere. Where \(y\ne0\), the ratio \(x/y\) then takes only the two values \(r_\pm=(-\sqrt2\pm\sqrt6)/2\), and the fractions of the \(y^4\)-mass on \(r_+\) and \(r_-\) are respectively \((2+\sqrt3)/4\) and \((2-\sqrt3)/4\). Both fractions are positive.

There is also a quantitative almost-minimizer conclusion: for any \(t=t(\tau)\in[1,\infty]\), if unit pairs satisfy
\[
\mathcal M_{t(\tau)}\bigl(\|x_\tau+\tau y_\tau\|_4,\|\tau x_\tau-y_\tau\|_4\bigr)
\le S_{X,t(\tau)}(\tau)+O(\tau^3),
\]
then \(\|x_\tau^2-y_\tau^2+\sqrt2x_\tau y_\tau\|_2=O(\tau)\). The constants in this conclusion depend only on the constant implicit in the displayed near-optimality assumption, not on \(t\).

## Assumptions and scope
All scalars are **real**; the pointwise products and powers are real functions. The measure space is arbitrary subject to \(\dim L_4\ge2\), equivalently there exist two disjointly supported unit functions. Only \(\tau\downarrow0\) is under consideration; no full-parameter minimization formula and no complex-space extension is asserted. The normalized power mean \(\mathcal M_t(a,b)\) is \(((a^t+b^t)/2)^{1/t}\) for finite \(t\), and \(\max(a,b)\) for the endpoint. Every error term can be bounded by one numerical constant for all \(t\ge1\) and all such measure spaces.

## Proof
**1. Exact antisymmetric-duality identity and equality cases.** For unit \(x,y\) set
\[
C=\int x^3y,\qquad E=\int xy^3,\qquad D=\int x^2y^2,
\qquad F=C-E,
\qquad R=x^2-y^2+\sqrt2xy.
\]
Hölder gives \(|C|,|E|,D\le1\). Direct expansion and \(\int x^4=\int y^4=1\) show
\[
\|R\|_2^2=\int[x^4+y^4+2\sqrt2xy(x^2-y^2)]=2+2\sqrt2 F.
\]
Hence \(F\ge-1/\sqrt2\), with equality exactly when \(R=0\). On the nonzero common support of an equality pair, \(r=x/y\) obeys \(r^2+\sqrt2r-1=0\). Also \(y=0\) forces \(x=0\). The identities \(\int x^4=\int y^4=1\) and \(r_\pm^4=7\mp4\sqrt3\) uniquely determine the two \(y^4\)-masses as stated. Such equality pairs do exist: choose disjointly supported unit functions \(f,g\); choose \(a,b>0\) satisfying
\[
a^4+b^4=1,\quad a^2b^2=\tfrac14,\quad a^2>b^2,
\]
and put \(x=af+bg\), \(y=-bf+ag\). Then both have unit \(L_4\) norm, \(F=-1/\sqrt2\), \(C=-E=-1/(2\sqrt2)\), and \(D=1/2\).

**2. Uniform second-order Taylor formula.** By direct polynomial expansion,
\[
\begin{aligned}
\|x+\tau y\|_4^4&=1+4\tau C+6\tau^2D+4\tau^3E+\tau^4,\\
\|\tau x-y\|_4^4&=1-4\tau E+6\tau^2D-4\tau^3C+\tau^4.
\end{aligned}
\]
For \(0\le\tau\le1/8\), the corresponding fourth roots are bounded below by \(1-\tau\) and the polynomial coefficients are uniformly bounded by Hölder. Taylor's theorem applied to the fourth root therefore gives, with an absolute remainder bound \(K_0\tau^3\),
\[
\frac{\|x+\tau y\|_4+\|\tau x-y\|_4}{2}
=1+\frac\tau2F+\tau^2B+O(\tau^3),
\qquad B=\frac32D-\frac34(C^2+E^2).
\]
At an equality pair from part 1, \(B=9/16\).

**3. Stability of the second-order coefficient.** Write \(r=\|R\|_2\) and \(Z=C+E\). From the exact identity,
\[
F=-\frac1{\sqrt2}+\frac{r^2}{2\sqrt2}.
\]
The pointwise products give
\[
\langle R,xy\rangle=F+\sqrt2D,
\qquad \langle R,x^2+y^2\rangle=\sqrt2Z.
\]
The same expansion with \(-\sqrt2xy\) gives \(F\le1/\sqrt2\), so \(0\le r\le2\). As \(\|xy\|_2\le1\), and \(\|x^2+y^2\|_2\le2\), these identities imply
\[
|D-\tfrac12|\le r/\sqrt2+r^2/4,
\qquad |Z|\le\sqrt2r,
\qquad |F^2-\tfrac12|\le r^2/2.
\]
Since \(C^2+E^2=(F^2+Z^2)/2\), we obtain the simple global bound \(|B-9/16|\le4r\) (using \(r\le2\)). Therefore the arithmetic mean of the output norms is bounded below by
\[
1-\frac\tau{2\sqrt2}+\frac{9\tau^2}{16}
+\frac{\tau r^2}{4\sqrt2}-4\tau^2r-K_0\tau^3.
\]
Completing the square, \(r^2/(4\sqrt2)-4\tau r\ge-16\sqrt2\tau^2\), yields a lower estimate with an absolute error of order \(\tau^3\), uniformly over all unit pairs.

**4. Upper bound simultaneously for all power means.** Use the two-support equality pair in part 1. The two transformed vectors have the same \(L_4\) norm, and their common fourth power is exactly
\[
(a-\tau b)^4+(b+\tau a)^4
=1-\sqrt2\tau+3\tau^2+\sqrt2\tau^3+\tau^4.
\]
Every power mean, even the maximum, therefore equals the fourth root of this polynomial on that pair, with expansion
\[
1-\frac\tau{2\sqrt2}+\frac{9\tau^2}{16}+O(\tau^3).
\]
For every nonnegative two-vector and all \(t\ge1\), the power mean dominates the arithmetic mean. The uniform lower bound in part 3 and the common upper trial now sandwich **every** \(S_{X,t}(\tau)\) between the same second-order expression with absolute \(O(\tau^3)\) remainder, establishing the theorem.

**5. Near-minimizer rigidity.** Under the stated \(O(\tau^3)\) near-optimality hypothesis, combine the lower bound before completing the square with the explicit upper trial to obtain
\[
\frac{r^2}{4\sqrt2}-4\tau r\le K_1\tau^2
\]
for a constant independent of \(t\). Its positive quadratic root forces \(r\le K_2\tau\), proving the quantitative conclusion.

## Verification
All analytic steps are self-contained and dimension-free. The quartic expansions were checked algebraically against their two-atom specialization; the squared-weight equalities \(a^4+b^4=1\), \(a^2b^2=1/4\), and \((a^2-b^2)^2=1/2\) yield the coefficients \(-\sqrt2\), \(3\), and \(+\sqrt2\) in the explicit trial polynomial. The fourth-root Taylor coefficient is \(3/4-3/16=9/16\). Uniformity across the outer exponent is proved by a power-mean sandwich rather than numerical optimization. Finite numerical checks in low-dimensional \(\ell_4\) were supplementary; no finite computation is used to infer the infinite-dimensional assertion.

## Relationship to prior work
Xu and Liu, *Skew Schäffer Type Constants* (first posted October 2, 2026), define the invariant and compute the exact real \(L_p\) profile **when the outer power exponent equals the ambient exponent**. For differing exponents their Corollary 3.6 and subsequent comparisons provide inequalities; these do not determine the first two coefficients uniformly for all \(1\le t\le\infty\), nor the exact antisymmetric-duality stability identity or almost-minimizer rigidity established here. Their formula covers \(t=4\); in fact, because the exact minimizing two-support pair there has equal output norms, power-mean monotonicity implies **the entire \(t\ge4\) range** already follows from their theorem. The genuinely new sharp lower bound is for \(1\le t<4\), together with the explicit deficit identity and quantitative rigidity.

The published exact small-skew slope on Banaś–Frączek planes concerns a different, nonsmooth norm and only the quadratic outer mean. The exact skew geometric mean constant of real \(\ell_4\) is instead **supremal** and does not determine the infimal cross-power onset. The known endpoint profile on a regular hexagonal Banach plane concerns a different norm and an all-parameter maximum mean. The distinctions are about mathematical implications, not merely titles or parameter values.

## Limitations
The result is a sharp two-term **local** expansion, not an all-parameter formula, and does not assert that minimizing pairs exist for every positive \(\tau\). The equality classification is for the antisymmetric first-variation functional, not for every finite-\(\tau\) minimizer. The proof uses real pointwise fourth powers; extending it to complex \(L_4\), other ambient exponents, or third-order uniform asymptotics requires separate work. Literature comparisons cannot certify absolute priority, particularly for equivalent formulations in older geometry-of-Banach-spaces literature. No independent audit has been performed.

## References
1. Y. Xu and Q. Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1, publicly posted 2026-10-02, https://arxiv.org/html/2610.03050v1.
2. Q. Ni, Q. Liu, and Y. Zhou, *Some aspects of new skew geometric constants in Banach spaces*, Mathematical Inequalities & Applications 28 (2025), 327–342, DOI:10.7153/mia-2025-28-22. Different supremal invariant.
3. Related published real Banaś–Frączek small-skew and regular-hexagon endpoint studies, both publicly available from October 11, 2026. Different Banach norms and outer parameter regimes.
