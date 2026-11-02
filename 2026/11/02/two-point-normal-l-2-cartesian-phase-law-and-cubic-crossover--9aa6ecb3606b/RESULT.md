# Two-point normal \(L^2\)-Cartesian phase law and cubic crossover

## Finding
For a nonzero operator \(T\) on a complex Hilbert space, define its \(L^2\)-Cartesian numerical radius by
\[
\omega_{\mathrm{C},2}(T)^2
=\frac1{2\pi}\int_0^{2\pi}
\left\|\operatorname{Re}(e^{-i\theta}T)\right\|^2\,d\theta.
\]
The following exact two-spectral-value profile holds. Let \(P,Q\) be nonzero orthogonal projections with \(PQ=0\), let \(a,b\in\mathbb C\) satisfy \(0<|b|<|a|\), and set
\[
T=aP+bQ,\qquad M=|a|,\qquad r=|b|/|a|\in(0,1).
\]
Let \(\beta\in[0,\pi/2]\) be the shortest angular distance between the projective eigenvalue phases \(\arg(a)\) and \(\arg(b)\) modulo \(\pi\). Put \(A=(1-r^2)/2>0\). Then
\[
\boxed{
\frac{\omega_{\mathrm{C},2}(T)^2}{M^2}
=\frac12+\frac{r\sin\beta-A\arctan(r\sin\beta/A)}{\pi}.
}\tag{1}
\]
This formula applies in arbitrary Hilbert-space dimension and is independent of the nonzero multiplicities of the two spectral values; an additional zero spectral subspace is allowed.

At fixed \(r\), the right-hand side is strictly increasing as \(\beta\) runs from \(0\) to \(\pi/2\). Thus the sharp phase bounds and equality classes are
\[
\boxed{
\frac12\ \le\ \frac{\omega_{\mathrm{C},2}(T)^2}{M^2}
\ \le\ \frac12+\frac{r-(1-r^2)\arctan r}{\pi}.
}\tag{2}
\]
Equality on the left occurs exactly for collinear spectral phases, and equality on the right exactly for projectively orthogonal phases.

The phase excess also satisfies a **globally sharp two-sided cubic modulus**. Writing
\[
D_r(\beta)=\omega_{\mathrm{C},2}(T)^2/M^2-1/2,
\quad
C_-(r)=\frac{r-(1-r^2)\arctan r}{\pi},
\quad
C_+(r)=\frac{4r^3}{3\pi(1-r^2)^2},
\]
we have
\[
\boxed{C_-(r)\sin^3\beta\ \le\ D_r(\beta)\ \le\ C_+(r)\sin^3\beta.}\tag{3}
\]
The lower coefficient cannot be increased (equality at \(\beta=\pi/2\)); the upper coefficient cannot be decreased (its ratio is attained in the limit \(\beta\downarrow0\)). Both inequalities are strict whenever \(0<\beta<\pi/2\). At \(\beta=0\) both sides vanish.

The angular turn-on is cubic at every fixed unequal modulus ratio:
\[
\boxed{
\frac{\omega_{\mathrm{C},2}(T)^2}{M^2}-\frac12
=\frac{4r^3}{3\pi(1-r^2)^2}\,\beta^3
+O_r(\beta^5)
\qquad(\beta\downarrow0).
}\tag{4}
\]
At the equal-modulus boundary the scaling changes. If \(r=1-\varepsilon\), \(\beta=\varepsilon t\), and \(t\ge0\) is fixed, then
\[
\boxed{
\lim_{\varepsilon\downarrow0}
\frac{\omega_{\mathrm{C},2}(T)^2/M^2-1/2}{\varepsilon}
=\frac{t-\arctan t}{\pi}.
}\tag{5}
\]
The convergence in (5) is uniform for \(t\) in compact subsets of \([0,\infty)\). The crossover interpolates between a cubic small-angle response and the linear response of equal-modulus spectra.

## Assumptions and scope
All operators and projections act on a complex Hilbert space, finite or infinite dimensional. \(P\) and \(Q\) are nonzero orthogonal self-adjoint idempotents and satisfy \(PQ=QP=0\); they need not have finite rank or sum to the identity. Both coefficients are nonzero with \(0<|b|<|a|\). The ratio \(r\) is the smaller-to-larger eigenvalue modulus and \(M\) is the larger modulus. A projective angle is measured modulo \(\pi\) because rotating an eigenvalue by \(\pi\) does not change the absolute real-part response. This uniquely defines \(\beta\in[0,\pi/2]\). Formula (5) concerns a family of such operators with prescribed ratios and angles, not an operator-norm limit on a fixed Hilbert space.

## Proof
**Spectral reduction and phase symmetry.** Orthogonality of \(P,Q\) gives
\[
\|\operatorname{Re}(e^{-i\theta}T)\|^2
=M^2\max\{\cos^2\theta,\ r^2\cos^2(\theta-\beta)\}
\]
after a harmless rotation of the angular integration variable, reversal of orientation, and a shift of either phase by \(\pi\). The zero subspace contributes only an eigenvalue zero. Thus write
\[
F_r(\beta)=\frac1{2\pi}\int_0^{2\pi}
\max\{\cos^2\theta,r^2\cos^2(\theta-\beta)\}\,d\theta.
\]
Using \(\max(u,v)=(u+v+|u-v|)/2\) and the mean \(1/2\) of each squared cosine,
\[
F_r(\beta)=\frac{1+r^2}{4}+
\frac12\cdot\frac1{2\pi}\int_0^{2\pi}
|\cos^2\theta-r^2\cos^2(\theta-\beta)|\,d\theta.
\]

**Absolute sinusoid integral.** The expression inside the absolute value has the form \(A+R\cos(2\theta-\gamma)\) for some real phase \(\gamma\), where
\[
A=\frac{1-r^2}{2},\qquad
R^2=A^2+r^2\sin^2\beta.
\]
For any \(0\le A\le R\), direct splitting at the two zeros of \(A+R\cos u\) gives
\[
\frac1{2\pi}\int_0^{2\pi}|A+R\cos u|\,du
=\frac2\pi\bigl(\sqrt{R^2-A^2}+A\arcsin(A/R)\bigr).
\]
Since \(A>0\), use \(\sqrt{R^2-A^2}=r\sin\beta\) and
\(\arcsin(A/R)=\pi/2-\arctan(r\sin\beta/A)\) for \(0\le\beta\le\pi/2\). The constant terms reduce to \(1/2\), proving (1).

**Sharpness and equality.** Set \(s=\sin\beta\) and regard the right-hand side of (1) as a function of \(s\in[0,1]\). Differentiation yields
\[
\frac{dF_r}{ds}=
\frac{r^3s^2}{\pi(A^2+r^2s^2)}>0\qquad(0<s\le1).
\]
The minimum is therefore attained only at \(s=0\) and the maximum only at \(s=1\). At \(s=1\), the identity \(\arctan(2r/(1-r^2))=2\arctan r\), valid for \(0<r<1\), gives the right-hand coefficient in (2). Any two nonzero orthogonal projections and appropriately phased nonzero scalars realize both equality cases. Thus the inequalities are sharp and the phase conditions are necessary.

**Sharp global cubic modulus.** The identity
\[
x-\arctan x = \int_0^x\frac{t^2}{1+t^2}\,dt
=x^3\int_0^1\frac{u^2}{1+x^2u^2}\,du
\]
shows that \( (x-\arctan x)/x^3\) is positive and strictly decreasing for \(x>0\), with limit \(1/3\) at zero. Consequently, \(D_r(\beta)/\sin^3\beta\) is strictly decreasing as \(\sin\beta\) increases from zero to one. Its endpoint values are exactly \(C_+(r)\) and \(C_-(r)\); thus (3) holds with both best constants and strictness in the interior.

**Cubic law.** For fixed \(r<1\), set \(x=r\sin\beta/A\). Then
\[
F_r(\beta)-\tfrac12=\frac A\pi(x-\arctan x).
\]
Taylor's theorem gives \(x-\arctan x=x^3/3+O(x^5)\) and \(\sin\beta=\beta+O(\beta^3)\). Hence
\[
F_r(\beta)-\tfrac12
=\frac{r^3}{3\pi A^2}\beta^3+O_r(\beta^5)
=\frac{4r^3}{3\pi(1-r^2)^2}\beta^3+O_r(\beta^5),
\]
which is (4).

**Crossover.** Let \(r=1-\varepsilon\) and \(\beta=\varepsilon t\) with \(t\) in a fixed compact subset of \([0,\infty)\). Uniformly there,
\[
A/\varepsilon\longrightarrow1,
\qquad r\sin(\varepsilon t)/\varepsilon\longrightarrow t,
\qquad r\sin(\varepsilon t)/A\longrightarrow t.
\]
Substitute these three limits into (1), using uniform continuity of \(\arctan\) on compact sets, to obtain (5). For exactly equal moduli, the limit of (1) as \(r\uparrow1\) is \(1/2+\sin\beta/\pi\), showing the advertised linear boundary response. This boundary specialization is recorded for comparison, not asserted as new.

## Verification
A standard-library-only checker, `verify_two_point.py`, evaluates the defining angular integral by midpoint quadrature for six unequal modulus ratios and thirteen phase angles each. It also checks the strict phase ordering, sharp orthogonal-phase formula, cubic coefficients, and compact-scale crossover. It passed 909 finite consistency assertions, including the strict global cubic coefficient bounds. All infinite and asymptotic assertions follow from the analytic argument above, not from numerical quadrature. No dependence on matrices from unrelated results is required.

## Relationship to prior work
Audeh, Kittaneh, Moradi, and Sahoo introduced the angular \(L^2\)-Cartesian numerical radius, proved the global comparison \(\omega(T)/\sqrt2\le\omega_{\mathrm C,2}(T)\le\omega(T)\), and computed the equal-modulus example \(\operatorname{diag}(1,i)\) in their Remark 19. Their published results do not state the unequal-modulus two-point profile, its sharp constrained phase bounds, or the cubic-to-linear crossover.

A published cubic stability theorem for the same angular radius already computes the orthogonal-phase value \(C_-(r)\) for a four-eigenvalue example with spectrum \(\{1,-1,ir,-ir\}\); that example has the **same angular norm** as \(\operatorname{diag}(1,ir)\). Thus the orthogonal-phase endpoint value is **not claimed as independently new**. Its theorem controls a global distance to phase-self-adjoint operators but does not give the interior two-phase profile, the best global phase coefficients in (3), or the double-scaling limit in (5).

The published *Exact projective spectral-gap formula and optimal finite spectra for the \(L^2\)-Cartesian radius of unitaries* treats spectra confined to one circle (equal eigenvalue moduli); its angular gap identity therefore supplies the boundary specialization but does not determine (1) for \(0<r<1\). The published *Exact rank-one overlap profile for the \(L^2\)-Cartesian numerical radius* concerns rank-one, generally nonnormal operators; it does not imply the two-nonzero-eigenvalue normal formula. General numerical-radius inequalities and earlier two-by-two numerical-range formulas constrain suprema, rather than the angular \(L^2\) average studied here. The exact elementary integration of the interior two-spectral-value family may nonetheless have appeared in older support-function or trigonometric-envelope literature under another name.

## Limitations
The result applies only to normal operators with two nonzero spectral values of unequal moduli (and a possible zero subspace), not to arbitrary normal spectra or nonnormal operators. It does not claim that this class maximizes the angular radius among all operators with fixed norm and second singular value. The equal-modulus boundary law is established elsewhere and is used solely to describe the crossover. A novelty search cannot certify publication priority; an old equivalent scalar integral formula might exist under different terminology. The checker is supplementary and independent mathematical auditing has not been performed.

## References
1. W. Audeh, F. Kittaneh, H. R. Moradi, S. Sahoo, *The \(L^2\)-Cartesian Numerical Radii of Hilbert Space Operators*, arXiv:2610.04844v2, 2026; first public version 2026-10-04, https://arxiv.org/html/2610.04844v2 .
2. *Exact projective spectral-gap formula and optimal finite spectra for the \(L^2\)-Cartesian radius of unitaries*, published-finding corpus published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-projective-spectral-gap-formula-and-optimal-finite-spectra--f6644dc86b39 .
3. *Cubic operator-norm stability for the \(L^2\)-Cartesian numerical radius*, published-finding corpus published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-cubic-operator-norm-stability-for-the-l-2-cartesian-numerical-ra--ffd07fee0727 .
4. *Exact rank-one overlap profile for the \(L^2\)-Cartesian numerical radius*, published-finding corpus published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-rank-one-overlap-profile-for-the-l-2-cartesian-numerical-r--846b702b24b7 .
5. L. Z. Gevorgyan, *On the numerical radii of \(2\times2\) complex matrices*, arXiv:1401.4794, 2014, https://arxiv.org/abs/1401.4794 .
