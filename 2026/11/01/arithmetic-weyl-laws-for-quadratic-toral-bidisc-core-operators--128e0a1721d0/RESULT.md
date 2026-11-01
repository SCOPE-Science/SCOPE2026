# Arithmetic Weyl laws for quadratic toral bidisc core operators

## Finding
For each \(0<\theta<\pi\), define the homogeneous quadratic polynomial
\[
p_\theta(z,w)=z^2-2\cos(\theta)zw+w^2
\]
and the principal Hardy-bidisc submodule \(\mathcal M_\theta=[p_\theta]\subset H^2(\mathbb D^2)\). Let \(R_z,R_w\) be its two restricted coordinate shifts. If \(P_z=I-R_zR_z^*\) denotes the wandering-space projection, set the self-adjoint core operator
\[
C_\theta=P_z-R_wP_zR_w^*.
\]
Write \(s_1(C_\theta)\ge s_2(C_\theta)\ge\dots\ge0\) for its singular values, with multiplicity, including zeros if appropriate.

The **decreasing-rearrangement Weyl coefficient** exists and satisfies
\[
\boxed{\lim_{N\to\infty}N s_N(C_\theta)=\Lambda(\theta)}
\]
with the complete arithmetic classification
\[
\boxed{\Lambda(\theta)=
\begin{cases}
8/\pi,&\theta/\pi\notin\mathbb Q,\\[2pt]
\dfrac4q\csc\!\bigl(\dfrac\pi{2q}\bigr),&\theta/\pi=p/q\ \text{reduced},\quad q\ge3\ \text{odd},\\[4pt]
\dfrac4q\cot\!\bigl(\dfrac\pi{2q}\bigr),&\theta/\pi=p/q\ \text{reduced},\quad q\ge2\ \text{even}.
\end{cases}}
\]
In particular, \(2\le\Lambda(\theta)\le8/3\) sharply. Equality at the lower endpoint holds **only** for \(\theta=\pi/2\); equality at the upper endpoint holds **only** for \(\theta=\pi/3\) and \(\theta=2\pi/3\). The irrational-angle value \(8/\pi\) lies strictly between the endpoints. Every rational angle is a discontinuity point of this coefficient as a function of \(\theta\), whereas every irrational angle is a continuity point.

As direct spectral consequences, \(C_\theta\in\mathcal S_{1,\infty}\setminus\mathcal S_1\), \(C_\theta\in\mathcal S_r\) for every \(r>1\), and
\[
\boxed{\lim_{N\to\infty}\frac{1}{\log N}\sum_{j=1}^{N}s_j(C_\theta)=\Lambda(\theta).}
\]
The same limits hold for every generalized logarithmic limit of these normalized partial sums.

## Assumptions and scope
All Hilbert spaces are complex. The Hardy-bidisc space has its usual monomial orthonormal basis. The polynomial has exactly two distinct simple zeros on the unit circle: \(e^{i\theta}\) and \(e^{-i\theta}\). Thus \(0<\theta<\pi\) is essential; coalescing endpoints are excluded. The normalization of the core and the OPUC Verblunsky sequence agrees with Lu and Zu, Theorems 2.3 and 3.4 [1]. The result is a statement about the **principal submodule core**, not the quotient-module cross-commutator or a different compression.

## Proof
**1. Established spectral dictionary.** Let \(q_\theta(\zeta)=p_\theta(\zeta,1)=(\zeta-e^{i\theta})(\zeta-e^{-i\theta})\) and let \(\alpha_n\) be the Verblunsky coefficients for the probability measure proportional to \(|q_\theta(e^{it})|^2dt\) on the unit circle. By [1, Theorem 3.4], the nonzero signed spectrum of \(C_\theta\), counted with multiplicity, is \(1\) and \(\pm|\alpha_n|\) for \(n\ge0\). In particular, its nonzero singular values are \(1\) and **two copies** of each \(|\alpha_n|\). Both the dictionary and the multiplicity are prior results.

**2. Two Fisher–Hartwig singularities.** The weight has simple toral zeros of squared modulus, so it meets [2, Theorem 3] with two Fisher–Hartwig exponents equal to \(1\) and constant analytic background. The normalized interior/exterior Szegő factors can be taken as \(D_i(z)=q_\theta(z)\) and \(D_e(z)=z^2/q_\theta(z)\), since \(q_\theta(0)=1\) and \(q_\theta\) is reciprocal. Their scattering product is \(\mathcal S(z)=z^2\). The singularity phases in [2, Eq. (39)] are consequently \(\vartheta_a=-a^2\), for \(a=e^{\pm i\theta}\). Substituting into [2, Eq. (15)] gives
\[
\alpha_n=\frac{e^{-i(n+3)\theta}+e^{i(n+3)\theta}}{n}+O_\theta(n^{-2})
=\frac{2\cos((n+3)\theta)}{n}+O_\theta(n^{-2}). \tag{1}
\]
Here \(O_\theta\) fixes \(\theta\); uniformity as the two roots merge is not asserted. Replacing the denominator \(n\) by \(n+1\) changes only the stated error order.

**3. Rearranged spectral counting, beyond coefficient asymptotics.** Put \(b_n=2|\cos((n+3)\theta)|/n\) for \(n\ge1\). Equation (1) yields \(\bigl||\alpha_n|-b_n\bigr|\le K_\theta n^{-2}\) after discarding finitely many indices (only the first finitely many indices are separately ignored). For \(t>0\), denote by \(N_C(t)\) the number of singular values of \(C_\theta\) strictly larger than \(t\). Then
\[
N_C(t)=2\#\{n\ge1:|\alpha_n|>t\}+O(1).
\]
Fix \(\gamma=3/4\). Indices below \(t^{-\gamma}\) contribute at most \(O(t^{-\gamma})\) to the counting function, hence contribute \(o(1)\) after multiplication by \(t\). Above this threshold, the error \(K_\theta n^{-2}\) is at most \(K_\theta t^{3/2}=o(t)\). The remaining count is therefore sandwiched between counts of
\(tn<2|\cos((n+3)\theta)|\pm o(1)\), with \(n\le(2+o(1))/t\).

Partition the interval \([0,2]\) for \(u=tn\) into finitely many short bins. On each bin, periodicity (when \(\theta/\pi\) is rational) or uniform distribution of the irrational rotation \(n\theta\bmod\pi\) (when it is irrational) computes the asymptotic fraction satisfying the cosine threshold; exceptional angular boundary points have zero Haar measure in the irrational case, while the finitely many exceptional threshold levels in the rational case have zero measure in the final integration over the level. Refine the bins, using the bounded integrand, to obtain
\[
\lim_{t\downarrow0}tN_C(t)
=2\int_0^2\nu_\theta\{v:2|\cos v|>u\}\,du
=4\int|\cos v|\,d\nu_\theta(v), \tag{2}
\]
where \(\nu_\theta\) is normalized Lebesgue measure on \([0,\pi)\) for irrational \(\theta/\pi\) and uniform measure on the \(q\)-point orbit for reduced rational \(p/q\). The right side is strictly positive. The standard equivalence between a monotone counting law \(N_C(t)\sim L/t\) and decreasing singular values \(s_N\sim L/N\) now yields the asserted **pointwise** Weyl coefficient, not just a Cesàro law.

**4. Exact arithmetic averages.** For irrational \(\theta/\pi\), \(\int_0^\pi|\cos v|\,dv/\pi=2/\pi\). For reduced rational \(p/q\), multiplication by \(p\) permutes the absolute cosine orbit, giving
\[
\int|\cos v|\,d\nu_\theta(v)=\frac1q\sum_{r=0}^{q-1}|\cos(\pi r/q)|.
\]
Splitting at the cosine sign change and summing geometric progressions gives exactly \(q^{-1}\csc(\pi/(2q))\) for odd \(q\), and \(q^{-1}\cot(\pi/(2q))\) for even \(q\). Let \(x=\pi/(2q)\). For odd \(q\), \(x/\sin x\) increases strictly with \(x>0\) on \((0,\pi/6]\), so its largest eligible value is at \(q=3\). For even \(q\), \(x\cot x\) decreases strictly with \(x\) on \((0,\pi/4]\), so its smallest eligible value is at \(q=2\). Both sequences approach \(1\) as \(q\to\infty\), one from above and the other from below. Hence the sharp global bounds and unique extremizers follow. Rational values differ from \(8/\pi\), and rationals and irrationals are dense; denominator growth proves continuity at irrational points. Finally \(s_N\sim\Lambda/N\) gives the Schatten and logarithmic statements by comparison with harmonic sums.

## Verification
The accompanying standard-library-only Python program checks 1,153 finite identities: exact rational Toeplitz Gram solves yielding initial Verblunsky coefficients at three angles, agreement with the cited leading Fisher–Hartwig phase, trigonometric orbit identities for denominators through 100, and coprime-numerator invariance for denominators through 54. These are supplementary local checks, **not** a substitute for the infinite-dimensional OPUC theorem, its large-index asymptotics, or the rearrangement proof. Run `python3 verify.py` after extracting this document and `verify.py` from the same package.

## Relationship to prior work
Lu and Zu [1] established the full core-eigenvalue/Verblunsky dictionary and trace-ideal criterion for any homogeneous principal generator, including this quadratic. Martínez-Finkelshtein, McLaughlin and Saff [2] established the general multi-point Fisher–Hartwig Verblunsky expansion used in (1). Neither underlying theorem, by itself, states the **decreasing-order singular-value limit** or the discontinuous **sharp arithmetic phase extremizers** for the present two-root core family. The contribution asserted here is the combined Weyl-counting theorem and its all-angle exact arithmetic classification, **not** the already-known spectral dictionary or the OPUC expansion. The two established theorems are strong inputs; potential anticipation as an implicit special consequence remains a publication-priority limitation.

## Limitations
The angle is fixed and lies strictly between \(0\) and \(\pi\); no uniform two-root-coalescence asymptotics are obtained. The coefficient is a first-order spectral invariant only: the remainder in \(s_N\) is not quantified, and lower-order oscillations need not vanish. The result does not determine arbitrary finite products, more than two distinct toral factors, general nonhomogeneous modules, or the quotient cross-commutator. The literature comparison is a best-knowledge priority assessment, not proof of global originality. Independent scientific validation has not been performed.

## References
[1] Y. Lu and C. Zu, *Verblunsky coefficients, CMV matrices and numerical invariants of homogeneous bidisc submodules*, arXiv:2608.18456, version 1 publicly posted August 19, 2026; Theorems 2.3 and 3.4.

[2] A. Martínez-Finkelshtein, K. T.-R. McLaughlin and E. B. Saff, *Asymptotics of orthogonal polynomials with respect to an analytic weight with algebraic singularities on the circle*, arXiv:math/0605715, Theorem 3, Eqs. (15), (32), (39).
