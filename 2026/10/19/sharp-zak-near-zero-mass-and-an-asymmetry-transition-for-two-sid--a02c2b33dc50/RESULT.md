# Sharp Zak near-zero mass and an asymmetry transition for two-sided exponential windows

## Finding
For every pair of positive decay rates \(a,b>0\), let
\[
g_{a,b}(t)=\begin{cases}e^{at},&t<0,\\e^{-bt},&t\geq0,\end{cases}
\qquad h_{a,b}=\left(\frac{2ab}{a+b}\right)^{1/2}g_{a,b}.
\]
The function \(h_{a,b}\) has unit \(L^2(\mathbb R)\)-norm. On the unit Zak cell define
\[
Z_{a,b}(x,\omega)=\sum_{k\in\mathbb Z}h_{a,b}(x-k)e^{2\pi i k\omega},
\quad (x,\omega)\in[0,1)^2,
\]
and let \(P_{a,b}(\varepsilon)\) be the area of the set where \(|Z_{a,b}|<\varepsilon\). Then the exact small-value law is
\[
\boxed{P_{a,b}(\varepsilon)=\mathcal C(a,b)\varepsilon^2+o(\varepsilon^2)},
\qquad \varepsilon\downarrow0,
\]
with the positive **sharp** coefficient
\[
\boxed{\mathcal C(a,b)=\frac{[2\cosh(a/2)]^{1+2b/(a+b)}[2\cosh(b/2)]^{1+2a/(a+b)}}{8ab\sinh((a+b)/2)}.}
\]
Here the Zak transform has just one simple zero in the cell; the coefficient is the local reciprocal Jacobian area factor at that zero.

There is an exact symmetry-breaking threshold for this normalized low-value statistic under a fixed total decay rate. Let \(q_*\) be the unique positive solution of
\[
\boxed{2q\tanh q-2q^2\operatorname{sech}^2q=1},
\qquad s_*=4q_*=4.592010397216724\ldots.
\]
For each fixed \(s=a+b\), the balanced choice \(a=b=s/2\) is a strict local minimizer of \(\mathcal C\) when \(0<s<s_*\), and a strict local maximizer when \(s>s_*\). At equality the quadratic variation vanishes; no strict-extremum assertion is needed at equality. For \(s>s_*\), all global minimizers of \(\mathcal C\) are asymmetric, and at least one reflection-related pair of global minimizers exists.

The *global* large-total-decay design problem has a sharp limiting answer. Let \(\alpha_*\) be the unique positive solution of
\[
\boxed{\alpha_*(2e^{\alpha_*}-1)=e^{\alpha_*}+1},
\qquad \alpha_*=0.888367907619767\ldots.
\]
As \(s\to\infty\),
\[
\boxed{\inf_{a+b=s\atop a,b>0}\mathcal C(a,b)\sim
\frac{(1+e^{\alpha_*})^3}{4\alpha_*e^{\alpha_*}}\,\frac1s
=\frac{4.675803184305343\ldots}{s}.}
\]
For **every** choice of global minimizers with total rate \(s\), their smaller decay rate converges to \(\alpha_*\) as \(s\to\infty\). The result concerns the Zak near-zero area, not the exact optimal Gabor frame bound at an oversampled lattice.

## Assumptions and scope
All parameters \(a,b,s\) are real and strictly positive; the spatial Zak period and frequency Zak period are both one. The area measure on the cell is ordinary two-dimensional Lebesgue measure in \((x,\omega)\). The normalization of \(h_{a,b}\) is essential for comparing different decay splits. The limiting small-value law fixes \(a,b\) before letting \(\varepsilon\to0\). The subsequent design limits fix \(s\), optimize over positive splits, and finally let \(s\to\infty\), in that order. Statements of simplicity refer to the real two-dimensional Jacobian of the complex-valued Zak transform.

## Proof
**1. Exact Zak transform and unique zero.** Put \(u=e^{-a}\), \(v=e^{-b}\), and \(z=e^{2\pi i\omega}\). Summing the two geometric tails of the unnormalized Zak series gives, for \(0\le x<1\),
\[
Zg_{a,b}(x,\omega)=\frac{e^{-bx}}{1-vz^{-1}}+
\frac{e^{ax}uz}{1-uz}.
\]
The denominator factors do not vanish when \(|z|=1\). Multiplying them out produces the real-affine numerator
\[
P_x+Q_xz,\qquad
P_x=e^{-bx}-uv e^{ax},\quad Q_x=u(e^{ax}-e^{-bx}).
\]
For \(0<x<1\), both \(P_x,Q_x\) are positive, and
\[
\frac{Q_x}{P_x}=\frac{u(e^{(a+b)x}-1)}{1-uv e^{(a+b)x}}
\]
is strictly increasing from zero to infinity. At \(x=0\), \(Q_x=0\), so no zero occurs there. Hence \(P_x+Q_xz=0\) with \(|z|=1\) precisely when \(z=-1\) and \(P_x=Q_x\). This gives the **unique** zero
\[
(x_0,\omega_0)=\left(\frac{\log(1+e^a)-\log(1+e^{-b})}{a+b},\frac12\right),
\qquad 0<x_0<1.
\]

**2. Jacobian and small-value area.** Introduce positive numbers
\[
A=\frac{e^{-bx_0}}{1+v}=\frac{ue^{ax_0}}{1+u},
\qquad \beta=\frac{1-uv}{(1+u)(1+v)}.
\]
Termwise differentiation of the convergent geometric expressions at the zero yields
\[
\partial_x Zg_{a,b}(x_0,\tfrac12)=-(a+b)A,
\quad
\partial_\omega Zg_{a,b}(x_0,\tfrac12)=-2\pi i\beta A.
\]
The two derivative columns are nonzero and orthogonal as real vectors. Since \(\|g_{a,b}\|_2^2=(a+b)/(2ab)\), the magnitude of the real Jacobian determinant for the normalized Zak map is
\[
\boxed{J(a,b)=4\pi ab\beta A^2>0.}
\]
The inverse-function theorem maps a sufficiently small neighborhood of the isolated zero diffeomorphically onto a neighborhood of zero in \(\mathbb C\); the rest of the compact quasi-periodic Zak cell has modulus bounded away from zero. Consequently, changing variables in the complex disk of radius \(\varepsilon\) gives
\[
P_{a,b}(\varepsilon)=\frac{\pi\varepsilon^2}{J(a,b)}+o(\varepsilon^2)
=\frac{\varepsilon^2}{4ab\beta A^2}+o(\varepsilon^2).
\]
Writing \(H=2\cosh(a/2)\), \(K=2\cosh(b/2)\) and \(s=a+b\), elementary simplification yields
\[
A=H^{-b/s}K^{-a/s},\qquad
\beta=\frac{2\sinh(s/2)}{HK}.
\]
Substitution establishes the displayed closed form for \(\mathcal C=\pi/J\).

**3. Exactly one local stability switch.** Keep \(s>0\) fixed, write \(a=s/2+\delta\), \(b=s/2-\delta\), and set \(q=s/4\). Taylor expansion of the explicit positive coefficient around \(\delta=0\) gives
\[
\log\mathcal C(s/2+\delta,s/2-\delta)
=\log\mathcal C(s/2,s/2)-\frac{\mathcal H(q)}{4q^2}\delta^2+O_s(\delta^4),
\]
where
\[
\mathcal H(q)=2q\tanh q-2q^2\operatorname{sech}^2q-1.
\]
Its derivative is
\[
\mathcal H'(q)=2\left(\tanh q-q\operatorname{sech}^2q
+2q^2\operatorname{sech}^2q\tanh q\right)>0
\]
for \(q>0\): the first difference is positive since \(\sinh q\cosh q>q\). Furthermore \(\mathcal H(0+)=-1\) and \(\mathcal H(q)\to\infty\). This proves existence and uniqueness of \(q_*\) and the strict local minimum/maximum assertion on either side of \(s_*\). For fixed \(s\), the coefficient \(\mathcal C\) tends to infinity as either rate tends to zero and is continuous in the interior, so global minimizers exist. If \(s>s_*\), the balanced split is a strict local maximum, hence no global minimizer is balanced; symmetry under swapping the rates supplies a distinct minimizing pair.

**4. Sharp large-rate optimum.** For each \(s\), take a global minimizer and denote its smaller decay rate by \(a_s\le s/2\). The estimates \(0<A,\beta\le1\), \(ab\le as\), and \(A\le[2\cosh(a/2)]^{-1/2}\le e^{-a/4}\) when \(a\le b\) show
\[
s\mathcal C(a,s-a)\ge\frac1{4a},
\qquad s\mathcal C(a,s-a)\ge\frac{e^{a/2}}{4a}.
\]
These inequalities force the minimizing smaller rates to remain bounded away from zero and infinity as \(s\to\infty\), provided a bounded comparison value exists. Such a comparison is obtained by holding any \(a>0\) fixed and letting \(b=s-a\to\infty\). The exact formulas from Step 2 then show, uniformly for \(a\) in every compact subinterval of \((0,\infty)\),
\[
s\mathcal C(a,s-a)\longrightarrow
F(a):=\frac{(1+e^a)^3}{4ae^a}.
\]
The derivative of \(\log F\) vanishes exactly when
\[
a(2e^a-1)=e^a+1.
\]
The left-minus-right side is negative at zero and has strictly positive derivative \((1+2a)e^a-1\) for \(a>0\), so there is exactly one stationary point. Since \(F(a)\to\infty\) at zero and infinity, that point \(\alpha_*\) is the unique global minimizer. Compactness and locally uniform convergence now show that *every* sequence of smaller rates from global minimizers converges to \(\alpha_*\), and the minimum coefficient has the sharp stated asymptotic.

## Verification
The standalone standard-library program `verify_zak.py` independently compares the geometric closed form against finite Zak sums, checks the real Jacobian by centered finite differences, checks the hyperbolic coefficient formula, and evaluates small-Zak sublevel area by radial quadrature. It also tests both sides of the exact local transition and the large-rate asymptotic. Run with `python3 verify_zak.py`; the accompanying `verification_output.txt` records one executed run. These finite checks do not establish uniqueness for all parameters or the limiting theorem: Steps 1–4 are the proofs of those unrestricted statements.

## Relationship to prior work
Kloos and Stöckler (arXiv:1311.7359v1, particularly Section 3 and Corollary 3.5) establish the one-zero Zak property for totally positive finite-type windows and study related Gabor frame bounds. Janssen (2003, Sections 1–2) treats critical-density Zak normalization and the **even** two-sided exponential. De Dios Pont, Gröchenig, Liehr, Shafkulovska and Taylor (arXiv:2608.04992v1, Sections 2 and 5) establish a general qualitative frame-set and shifted-sampling theory. A separate exact translated-grid sampling result for asymmetric two-sided exponentials gives sharp sampling constants and an unstable spatial shift, together with the same elementary Zak rational symbol. These works furnish the known zero and sampling structure; none of their inspected statements supplies the \(L^2\)-normalized **two-dimensional small-value-area coefficient**, its exact unique fixed-sum local stability switch, or the limiting **global** rate-design law. The rational symbol and basic one-zero property are not claimed to be new. The new assertion is the quantitative and optimized near-zero geometry.

## Limitations
This concerns the **unit-period Zak cell** and a two-piece exponential family, with \(L^2\) normalization, not arbitrary totally positive windows. The small-value-area expansion is for fixed positive rates, not uniform in the rates near boundary degeneration. The local transition does not assert that the balanced split is globally optimal below the threshold or classify all global minimizers at finite total rate; at equality only the vanishing second variation is asserted. The statistic \(\mathcal C\) is not itself a frame lower bound. Additional unindexed literature might contain a mathematically equivalent optimized local-symbol asymptotic; bibliographic priority is therefore subject to further external review.

## References
1. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359v1, first public preprint 2013-11-28, https://arxiv.org/abs/1311.7359.
2. A. J. E. M. Janssen, *On generating tight Gabor frames at critical density*, Journal of Fourier Analysis and Applications 9 (2003), 175–214, https://pure.tue.nl/ws/files/3079889/Metis235352.pdf.
3. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, and M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992v1, first public preprint 2026-08-05, https://arxiv.org/html/2608.04992v1.
4. *Sharp shifted sampling bounds and two tight phases for asymmetric two-sided exponentials*, publicly archived mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-shifted-sampling-bounds-and-two-tight-phases-for-asymmetri--acaeec402fe4.
