# Exact integer-oversampling Poisson Gabor bounds and optimal redundancy-two width

## Finding
For the even Poisson window \(g_w(t)=1/(t^2+w^2)\), the optimal frame bounds on every integer-oversampled rectangular lattice have closed hyperbolic formulas. Fix any integer \(q\ge 2\), any \(w>0\), and the Gabor family
\[
\mathcal G_{q,w}=\{e^{2\pi i mt/q}g_w(t-n):m,n\in\mathbb Z\}\subset L^2(\mathbb R).
\]
Writing \(c=2\pi w\) and \(R_q(c)=\sinh(c)/\sinh(c/q)\), its **sharp** lower and upper frame bounds are respectively
\[
A_q(w)=\left(\frac{\pi}{w}\right)^2\frac{R_q(c)-q}{2\cosh^2(c/2)},\qquad
B_q(w)=\left(\frac{\pi}{w}\right)^2\frac{R_q(c)\cosh(c/q)+q}{2\sinh^2(c/2)}.
\]
The entire spectrum of the frame operator is \([A_q(w),B_q(w)]\), and \(A_q(w)>0\). Both frame constants are optimal, not merely estimates.

Within this same sharp frame-bound profile, the redundancy-two condition number \(\kappa_2(w)=B_2(w)/A_2(w)\) has a **unique** global minimizer over \(w>0\):
\[
w_*=\frac2\pi\operatorname{arcosh}\sqrt{y_*},\quad
4y_*^4-10y_*^3+4y_*^2+y_*-1=0,\quad y_*>1.
\]
The displayed polynomial has exactly one real root above \(1\). Numerically \(w_*=0.551291516054163\ldots\) and \(\kappa_2(w_*)=5.62088237421534\ldots\).

## Assumptions and scope
The real line has Lebesgue measure, and \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i t\xi}\,dt\). The atoms use integer translations and modulations spaced \(1/q\), with **no** \(L^2\)-normalization of \(g_w\). Here \(q\) is an integer at least \(2\), and \(w\) is an arbitrary positive real number. Optimality means that the constants cannot be improved in
\[
 A_q(w)\|f\|_2^2\le\sum_{m,n\in\mathbb Z}|\langle f,e^{2\pi i mt/q}g_w(t-n)\rangle|^2
 \le B_q(w)\|f\|_2^2\quad(f\in L^2(\mathbb R)).
\]
No claim is made about nonintegral oversampling, irregular lattices, or optimality among different window profiles. The optimizing \(w_*\) concerns only the condition number for \(q=2\).

## Proof
**1. Scalar diagonalization.** Introduce the unitary Zak transform
\[
 Zf(x,\omega)=\sum_{k\in\mathbb Z}f(x+k)e^{-2\pi i k\omega},\qquad (x,\omega)\in[0,1]^2.
\]
For \(m=j+q\ell\), where \(0\le j<q\) and \(\ell\in\mathbb Z\), the Zak transform of an atom equals
\[
 e^{2\pi i(j/q+\ell)x}e^{-2\pi i n(\omega-j/q)} Zg_w(x,\omega-j/q).
\]
Parseval for the orthonormal torus Fourier basis as \((\ell,n)\) varies shows that the entire frame quadratic form is
\[
\int_{[0,1]^2}|Zf(x,\omega)|^2 F_{q,w}(x,\omega)\,dx\,d\omega,\qquad
F_{q,w}(x,\omega)=\sum_{j=0}^{q-1}|Zg_w(x,\omega+j/q)|^2.
\]
Consequently the sharp bounds are the essential infimum and supremum of the continuous periodic function \(F_{q,w}\). Its range is an interval because the two-dimensional torus is connected, so it also gives the full frame-operator spectrum.

**2. Exact Zak transform.** The Fourier transform of the window is \(\widehat g_w(\xi)=(\pi/w)e^{-2\pi w|\xi|}\). Put \(r=e^{-c}\), \(\theta=2\pi x\), and \(v\in[0,1)\). Splitting the Fourier-side geometric series into nonnegative and negative indices gives the exact identity
\[
 Zg_w(x,v)=\frac{2\pi r}{w}\,
 \frac{e^{iv\theta}\big[\sinh(c(1-v))+e^{-i\theta}\sinh(cv)\big]}
 {1-2r\cos\theta+r^2}.
\]
The formula extends continuously by periodicity and quasi-periodicity at the sides of a Zak fundamental cell.

**3. The extremal spatial fibers.** Write \(a=\sinh(c(1-v))\) and \(b=\sinh(cv)\). Both are nonnegative. With \(t=\cos\theta\), each term of \(F_{q,w}\) is a positive constant times
\[
 H(t)=\frac{a^2+b^2+2ab t}{(1-2rt+r^2)^2},\qquad -1\le t\le1.
\]
A direct derivative gives
\[
 H'(t)=\frac{2ab(1-2rt+r^2)+4r(a^2+b^2+2ab t)}{(1-2rt+r^2)^3}>0.
\]
Indeed the denominator is positive, \(a,b\) cannot vanish simultaneously, and \(a^2+b^2+2ab t\ge(a-b)^2\ge0\); at the only possible zero of the latter, the \(2ab\) term is strictly positive. Thus the sum \(F_{q,w}\) is strictly increasing in \(\cos(2\pi x)\). Its global minimum is attained along \(x=1/2\), and its global maximum along \(x=0\), modulo integer shifts.

**4. The extremal frequency fibers.** The preceding Zak identity simplifies at these two spatial values. For \(0\le\omega\le1/q\), abbreviate \(v_j=\omega+j/q\). Then
\[
F_{q,w}(1/2,\omega)=\left(\frac\pi w\right)^2\frac{\sum_{j=0}^{q-1}\sinh^2(c(1/2-v_j))}{\cosh^2(c/2)},
\]
\[
F_{q,w}(0,\omega)=\left(\frac\pi w\right)^2\frac{\sum_{j=0}^{q-1}\cosh^2(c(1/2-v_j))}{\sinh^2(c/2)}.
\]
The finite geometric sum gives the exact hyperbolic identity
\[
\sum_{j=0}^{q-1}\cosh\big(c(1-2\omega-2j/q)\big)
=\frac{\sinh c}{\sinh(c/q)}\cosh\big(c(1/q-2\omega)\big).
\]
Therefore, using \(\cosh^2 u=(\cosh2u+1)/2\) and \(\sinh^2 u=(\cosh2u-1)/2\),
\[
 F_{q,w}(1/2,\omega)=\left(\frac\pi w\right)^2
 \frac{R_q(c)\cosh(c(1/q-2\omega))-q}{2\cosh^2(c/2)},
\]
\[
 F_{q,w}(0,\omega)=\left(\frac\pi w\right)^2
 \frac{R_q(c)\cosh(c(1/q-2\omega))+q}{2\sinh^2(c/2)}.
\]
The first expression has its unique minimum in that frequency cell at \(\omega=1/(2q)\); the second has its maxima at \(\omega=0,1/q\). These substitutions give precisely \(A_q(w)\) and \(B_q(w)\). The inequality \(R_q(c)>q\) follows from the strict increase of \(\sinh u/u\) on positive \(u\), so \(A_q(w)>0\). Since \(F_{q,w}\) is continuous and extremal at these fibers, the constants are sharp.

**5. Unique optimal Poisson width at redundancy two.** Set \(y=\cosh^2(\pi w/2)>1\). Elementary use of \(\sinh(c)/\sinh(c/2)=2\cosh(c/2)\) yields
\[
 \kappa_2(w)=\frac{(2y-1)^2\big((2y-1)^2+1\big)}{8y(y-1)^2}.
\]
Differentiation with respect to \(y\) gives
\[
 \frac{d\kappa_2}{dy}=\frac{(2y-1)(4y^4-10y^3+4y^2+y-1)}{4y^2(y-1)^3}.
\]
Putting \(y=1+t\), the quartic becomes \(4t^4+6t^3-2t^2-5t-2\). Its coefficient sequence has exactly one sign change, so Descartes' rule of signs gives at most one positive root. Its value at zero is negative and its leading term is positive; hence it has exactly one positive root. The condition number diverges as \(y\downarrow1\) and as \(y\to\infty\). Thus this root is the unique global minimizer and gives the asserted width.

## Verification
The accompanying standalone Python program `checks/check_poisson_bounds.py` performs 951 deterministic supplementary assertions. These include 12 parameter combinations \((q,w)\), direct checks of both fiber extrema, 900 random torus-point inequalities, nine comparisons against independently truncated time-domain Zak series, and six strict comparisons around the uniquely optimized redundancy-two width. Executing `python3 checks/check_poisson_bounds.py` prints `POISSON_FRAME_CHECKS_OK 951`. Finite computations are not a substitute for steps 1–5, which prove the infinite-dimensional result.

## Relationship to prior work
Belov and Semenov's 2026 work establishes a general frame-property criterion for time-frequency shifts of this Poisson kernel on semi-regular sets. A previous exact calculation for **two half-staggered translation cosets with integer modulations** already gives the \(q=2\) sharp constants of this paper: the unitary dilation \(f(t)\mapsto2^{-1/2}f(t/2)\) sends that lattice to unit translations and half-integer modulations, and sends \(g_{w/2}\) to \(2\sqrt2\,g_w\). Consequently its bounds divided by \(8\) agree with the \(q=2\) formulas above. **The frame-bound novelty here is the all-integer family \(q\ge3\)** and its exact global extrema; the redundancy-two width optimizer is a distinct explicit corollary of those bounds and is not claimed to make the known redundancy-two bounds new. The general frame criterion does not furnish the \(q\ge3\) formulas. Belov, Kulikov and Lyubarskii analyze the different, single-pole Cauchy window. Kloos and Stöckler study Zak-transform methods and frame criteria for totally positive windows and exponential splines. The generic integer-oversampling frame-bound representation goes back at least to Janssen; this result claims the Poisson-specific evaluations, not that general representation.

## Limitations
The sharp formulas require integer redundancy \(q\ge2\), integer translations, and the specific non-normalized Poisson profile; general nonrectangular lattice optimization is not addressed. The historical novelty comparison is limited by unavailable full text of Janssen's 1996 paper; possible implicit previous coverage remains a risk. Independent mathematical validation has not been performed.

## References
- Y. Belov and A. V. Semenov, *Irregular Gabor Frames for the Poisson Kernel*, first publicly available 2026-10-21, arXiv:2610.30037, https://arxiv.org/abs/2610.30037.
- Y. Belov, A. Kulikov and Y. Lyubarskii, *Gabor frame operator for the Cauchy kernel*, arXiv:2212.08915, https://arxiv.org/abs/2212.08915.
- T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359, https://arxiv.org/abs/1311.7359.
- A. J. E. M. Janssen, *Some Weyl–Heisenberg frame bound calculations*, *Indagationes Mathematicae* **7** (1996), 165–183, https://doi.org/10.1016/0019-3577(96)85088-9.
