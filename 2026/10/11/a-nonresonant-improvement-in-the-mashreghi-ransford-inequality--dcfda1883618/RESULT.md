# A nonresonant improvement in the Mashreghi–Ransford inequality

## Finding

For a complex sequence \((a_n)_{n\geq0}\), define its two binomial transforms by
\[
b_n=\sum_{k=0}^n\binom nk a_k,
\qquad
c_n=\sum_{k=0}^n\binom nk(-1)^{n-k}a_k.
\]
Fix \(\beta>1\), put \(\alpha=\sqrt{\beta^2-1}\), and suppose \(b_n,c_n=O(\beta^n)\). If
\[
\frac{\arccos(1/\beta)}{\pi}\notin\mathbb Q,
\]
then
\[
\limsup_{n\to\infty}\frac{|a_n|}{\alpha^n}
\leq
K_{\mathrm{irr}}
\left(\limsup_{n\to\infty}\frac{|b_n|}{\beta^n}\right)^{1/2}
\left(\limsup_{n\to\infty}\frac{|c_n|}{\beta^n}\right)^{1/2},
\qquad
K_{\mathrm{irr}}=\frac4\pi\left(2\cos\frac\pi9-1\right)
=1.1196680646257\ldots<\frac2{\sqrt3}.
\]
Thus a strict improvement on the sharp *uniform-in-parameter* constant holds at every parameter whose associated angle is irrational relative to \(\pi\). No claim is made that this is the best fixed-parameter constant.

## Assumptions and scope

All limits superior are taken over nonnegative integers tending to infinity. The bounded-transforms assumption ensures the displayed right-hand factors are finite. Their vanishing is permitted. The parameter \(\beta\) is fixed before taking limits. Define
\[
\phi=\arccos(1/\beta)\in(0,\pi/2),\qquad
p=\sin\phi=\alpha/\beta,\qquad q=\cos\phi=1/\beta.
\]
The irrational-angle hypothesis is essential for the complete Poisson angular equidistribution used below; the theorem does not cover rational \(\phi/\pi\), even with large denominators. The method concerns growth of binomial transforms and entire exponential generating functions (MSC2020 30D15).

## Proof

**Step 1: normalization and the zero cases.** The uniform Mashreghi–Ransford estimate in Bouthat [1, Theorem 1.1] gives finiteness of the normalized coefficient limsup and proves the claimed inequality whenever either right-hand limsup vanishes. To handle complex sequences, choose a subsequence along which the normalized moduli of \(a_n\) approach their limsup, and pass to a further subsequence with convergent arguments. Rotation followed by the real part produces a real sequence with the same normalized limsup and whose transformed limsups do not exceed the original two. It therefore suffices to handle real \(a_n\) and positive
\[
B=\limsup|b_n|/\beta^n,\qquad C=\limsup|c_n|/\beta^n.
\]
Set \(x_n=a_n/\alpha^n\), \(y_n=b_n/\beta^n\), \(z_n=(-1)^nc_n/\beta^n\), and define the exponential generating functions
\[
F(w)=\sum_{n\ge0}x_nw^n/n!,\qquad
G(w)=\sum_{n\ge0}y_nw^n/n!,\qquad
H(w)=\sum_{n\ge0}z_nw^n/n!.
\]
These are entire of finite exponential type; by the binomial theorem,
\[
G(w)=e^{qw}F(pw),\qquad H(w)=e^{qw}F(-pw),
\]
and hence
\[
e^{-2qw}G(w)=H(-w),\qquad e^{-2qw}H(w)=G(-w).
\]
The real coefficients imply conjugation symmetry.

**Step 2: a nonresonant angular lemma.** Let \((s_n)\) be any bounded real sequence, let \(L=\limsup|s_n|\), and set \(E(w)=\sum_{n\ge0}s_nw^n/n!\). Assume \(\phi/\pi\notin\mathbb Q\) and
\[
e^{-t}E(te^{3i\phi})\longrightarrow0
\qquad(t\longrightarrow\infty).
\]
We prove
\[
\limsup_{t\to\infty}e^{-t}|E(te^{i\phi})|
\le J L,\qquad
J=\frac2\pi\left(2\cos\frac\pi9-1\right).
\]
Set
\[
\lambda=\frac1{3-4\sin^2(\pi/9)}>0,
\quad
g(\vartheta)=\cos\vartheta+\lambda\cos(3\vartheta),
\quad
w_{t,n}=e^{-t}t^n/n!.
\]
For every integer \(k\ne0\),
\[
\sum_{n\ge0}w_{t,n}e^{ikn\phi}
=\exp\{t(e^{ik\phi}-1)\}\longrightarrow0,
\]
since \(k\phi\notin2\pi\mathbb Z\). By approximation of the continuous periodic function \(|g|\) by trigonometric polynomials,
\[
\sup_{\vartheta\in\mathbb R}
\left|\sum_{n\ge0}w_{t,n}|g(n\phi+\vartheta)|
-\frac1{2\pi}\int_0^{2\pi}|g(u)|\,du\right|\longrightarrow0.
\]
Uniformity in \(\vartheta\) follows because each nonzero Fourier mode has modulus bounded by \(\exp(t(\cos(k\phi)-1))\), independently of its translated phase.

Choose \(\vartheta=\vartheta_t\) so that
\[
e^{-t}|E(te^{i\phi})|
=\operatorname{Re}\bigl(e^{i\vartheta}e^{-t}E(te^{i\phi})\bigr).
\]
Adding the vanishing third-harmonic contribution gives
\[
e^{-t}|E(te^{i\phi})|
=\sum_{n\ge0}w_{t,n}s_n g(n\phi+\vartheta)
-\lambda\operatorname{Re}\bigl(e^{3i\vartheta}e^{-t}E(te^{3i\phi})\bigr).
\]
For every \(\varepsilon>0\), \(|s_n|\le L+\varepsilon\) outside a finite set; the Poisson weight of this finite set tends to zero. The angular limit above therefore bounds the limsup by \((L+\varepsilon)(2\pi)^{-1}\int|g|\). Let \(\varepsilon\downarrow0\).

To evaluate the integral exactly, factor
\[
g(u)=\cos u\,(1-3\lambda+4\lambda\cos^2u).
\]
Its unique sign change on \((0,\pi/2)\) is at \(u_0=7\pi/18\), because \(\cos u_0=\sin(\pi/9)\). As
\[
\int_0^u g(v)\,dv=\sin u+(\lambda/3)\sin3u,
\qquad\sin(3u_0)=-1/2,
\]
quarter-circle symmetry yields
\[
\frac1{2\pi}\int_0^{2\pi}|g(u)|\,du
=\frac2\pi\int_0^{\pi/2}|g(u)|\,du
=\frac2\pi\bigl(2\sin u_0-1\bigr)
=J.
\]
This is an exact identity, not a quadrature estimate. Conjugation proves the same inequality on the negative first-harmonic ray.

**Step 3: transfer to the binomial transforms.** By the normalization identities, \(|G(w)|\) and \(|H(w)|\) are bounded by \(Me^{|w|}\); their exponential partners \(e^{-2qw}G(w)=H(-w)\) and \(e^{-2qw}H(w)=G(-w)\) obey the same bound. Bouthat [1, Lemma 4.2] proves from these two entire-function bounds, using the Phragmén–Lindelöf theorem on sectors of opening less than \(\pi\), that
\[
e^{-t}G(te^{\pm3i\phi})\to0,
\qquad e^{-t}H(te^{\pm3i\phi})\to0.
\]
The lemma just proved, with coefficient limsups \(B\) and \(C\), improves [1, equation (15)] to
\[
\limsup_{t\to\infty}e^{-t}|G(te^{\pm i\phi})|\le JB,
\qquad
\limsup_{t\to\infty}e^{-t}|H(te^{\pm i\phi})|\le JC.
\]

**Step 4: interpolation and the two saddle points.** Set
\[
\delta=\pi/2-\phi\in(0,\pi/2),
\qquad \Psi(w)=e^{-pw}F(-ipw).
\]
The exact identities [1, equation (17)] are
\[
\Psi(te^{i\delta})=e^{-t}G(te^{-i\phi}),
\qquad
\Psi(te^{-i\delta})=e^{-t}H(te^{i\phi}).
\]
Apply the two-constants Phragmén–Lindelöf principle [1, Lemma 5.1] to \(\Psi\) in \(|\arg w|<\delta\). On each fixed closed smaller angular sector it gives the asymptotic upper bound
\[
\limsup_{r\to\infty}|\Psi(re^{i\theta})|
\le (JB)^{(\delta+\theta)/(2\delta)}
(JC)^{(\delta-\theta)/(2\delta)}.
\]
This conclusion is uniform for \(\theta\) on compact subintervals. Writing \(\eta_n=\arcsin(n^{-1/4})\), choosing \(r=n/p\), and letting \(|\theta|\le\eta_n\), one obtains
\[
\sup_{|\theta|\le\eta_n}
 e^{-n\cos\theta}|F(-ine^{i\theta})|
\le J\sqrt{BC}+o(1).
\]
Real coefficients make \(|F(ine^{-i\theta})|=|F(-ine^{i\theta})|\). Bouthat [1, Lemma 3.2] shows that the remaining arcs of the Cauchy coefficient integral are negligible, while the two neighborhoods of the saddle points contribute at most their normalized sum. It follows that
\[
\limsup_{n\to\infty}|x_n|\le 2J\sqrt{BC}
=\frac4\pi\left(2\cos\frac\pi9-1\right)\sqrt{BC}.
\]
Undoing normalization and the real-part reduction completes the proof. Finally, one may use \(\pi>3.14\), \(\sqrt3<1.74\), and the Taylor bound \(\cos(\pi/9)<0.94\) to obtain \(2J<4(0.88)/3.14<2/1.74<2/\sqrt3\).

## Verification

The companion program `check_angular.py` checks: the sign-changing angle and coefficient of the trigonometric combination; its normalized absolute integral against independent midpoint quadrature; the strict separation from the known uniform constant; uniform-phase Poisson finite-parameter tests at three radii for one irrational angle; and binomial-transform normalization on a finite test sequence. The infinite theorem uses the exact Poisson Fourier transform, trigonometric-polynomial approximation, and the cited analytic lemmas; no finite computation or sampled integral is treated as an infinite proof.

## Relationship to prior work

Bouthat [1] proves the optimal universal constant \(2/\sqrt3\) and an angular auxiliary bound \(1/\sqrt3\) that applies to every \(\phi\in(0,\pi/2)\). The new argument replaces the auxiliary Cauchy–Schwarz estimate by an exact absolute first-plus-third harmonic average, using complete Poisson angular equidistribution for irrational \(\phi/\pi\). The rest of the analytic transfer remains applicable without change. At the sharp universal witness \(\beta=2\), one has \(\phi/\pi=1/3\), so the irrational-angle estimate is not applicable.

The published note *Arithmetic resonance lower bounds for fixed-parameter Mashreghi–Ransford constants* records lower bounds from a two-pole witness, which equal one for irrational angles; a lower bound does not imply the new strict upper bound. Earlier Mashreghi–Ransford [2] proves a universal constant two. None of these results implies the stated strict nonresonant upper improvement.

## Limitations

The result does not identify the optimal fixed-parameter constant, does not assert that \(K_{\mathrm{irr}}\) is sharp, and does not address rational-angle parameters. There is no uniform convergence rate in \(\phi\): angles approaching a rational resonance may require increasingly large radii before the Poisson distribution equidistributes. The 2005 primary article was not available for full-text examination during preparation; it is known here through the bibliographic record and the full 2026 analysis. Equivalent unindexed literature cannot be excluded by search alone.

## References

1. L. Bouthat, *The sharp constant in the Mashreghi–Ransford inequality*, arXiv:2609.08852v1, first posted 8 September 2026, https://arxiv.org/pdf/2609.08852 . In particular, Sections 2–5 and Lemmas 3.2, 4.2, 5.1.
2. J. Mashreghi and T. Ransford, *Binomial sums and functions of exponential type*, Bulletin of the London Mathematical Society 37 (2005), 15–24, DOI:10.1112/S0024609304003625.
3. *Arithmetic resonance lower bounds for fixed-parameter Mashreghi–Ransford constants*, publicly accessible mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-arithmetic-resonance-lower-bounds-for-fixed-parameter-mashreghi--cc17fb4139fb .
