# Certified central-section profile of the $l_4^5$ ball: six enclosed volumes with $21.8\%$ diagonal-vs-coordinate gap

## Context

Let $K_0=B_4^5=\\{x\\in\\mathbb R^5:\\sum|x_i|^4\\le 1\\}$, the canonical smooth
symmetric interpolant between cube and Euclidean ball in dimension $5$,
the first open Mahler dimension above the resolved $n=3$ case.
Quantitative stability for the Mahler volume product and the Bourgain
slicing program after the Klartag–Lehec resolution is the recognized
frontier; explicit directional section profiles of $K_0$ calibrate any
future stability constant. General Koldobsky Fourier identities give the
toolkit but no certified $B_4^5$ numbers; Mahler/KLS/slicing tables record
only extremal bodies (cube, ball, simplex, Hanner) and universal bounds.

## Definitions

For unit $\\theta$, $S(\\theta)=|K_0\\cap\\theta^\\perp|_4$ is the
$4$-volume of the central hyperplane section. Fix in order:
$t_1=e_1$, $t_2=(e_1+e_2)/\\sqrt2$, $t_3=(e_1+e_2+e_3)/\\sqrt3$,
$t_4=(e_1+e_2+e_3+e_4)/2$, $t_5=d=(1,1,1,1,1)/\\sqrt5$,
$t_6=(3e_1+e_2+e_3+e_4+e_5)/\\sqrt{13}$.
Put $c_0=\\int_{\\mathbb R}e^{-y^4}dy=2\\Gamma(5/4)$,
$\\psi(v)=\\Gamma(5/4)^{-1}\\int_0^\\infty\\cos(vy)e^{-y^4}dy$,
$F_a(t)=\\prod_{j=1}^5\\psi(a_jt)$.

## Result (headline claim)

The exact values $S(t_i)$ lie in:

| $i$ | direction | interval $I_i$ | width |
|---|---|---|---|
| 1 | $e_1$ | $[10.799515629,10.799517629]$ | $2.0\\times10^{-9}$ |
| 2 | $(11)/\\sqrt2$ | $[12.842488,12.843236]$ | $7.5\\times10^{-4}$ |
| 3 | $(111)/\\sqrt3$ | $[12.938968,12.939703]$ | $7.4\\times10^{-4}$ |
| 4 | $(1111)/2$ | $[13.080006,13.080741]$ | $7.4\\times10^{-4}$ |
| 5 | diagonal $d$ | $[13.151640,13.152375]$ | $7.4\\times10^{-4}$ |
| 6 | $(31111)/\\sqrt{13}$ | $[12.325403,12.326138]$ | $7.4\\times10^{-4}$ |

Every width is $\\le 10^{-3}$. Moreover
$\\min I_5/\\max I_1=13.151640/10.799518=1.217799\\ge 1.05$,
the maximum over the six directions is attained at the diagonal $t_5$
(lower end $13.151640$ exceeds next largest upper end $13.080741$ by
$0.0709$) and the minimum at $t_1=e_1$ (upper end $10.799518$ below next
smallest lower end $12.325403$ by $1.5259$).

## Proof / evidence

Koldobsky Fourier-cosine identity (Lemma H-K: Koldobsky, *Fourier Analysis
in Convex Geometry*, AMS vol. 105 (2005), Ch. 2 Thm 2.1 p. 27, Eq. (2.4)
p. 28; $l_p$ specialization Ch. 4 Lemma 4.2/Cor. 4.3), specialized via
$f(x)=\\exp(-\\|x\\|_4^4)$ and the Fourier slice theorem to
$S(a)=(c_0^5/\\pi)\\int_0^\\infty F_a(t)\\,dt$.
Enclosure: composite Simpson on $[0,4]$ ($4800$ panels) for $\\psi,\\psi'$
tables on $[0,65]$ at step $0.05$ with explicit fourth-derivative sup
majorants ($E_0=1.72\\times10^{-7}$, $E_1=7.12\\times10^{-7}$); cubic
Hermite interpolation ($\\varepsilon_h=1.87\\times10^{-7}$ with
$D_4=\\sup|\\psi^{(4)}|=1/4$); composite Simpson on $[0,60]$ ($6000$
panels, error $\\sim10^{-8}$); polynomial-majorant tails
$|\\psi(v)|\\le\\min(1,C_2/v^2,C_4/v^4)$, $C_2=8.2$, $C_4=1100$
(worst $6.2\\times10^{-6}$); propagation $\\le3.67\\times10^{-4}$;
plus quantified floating-point allowance $10^{-7}$; total half-width
$\\le3.74\\times10^{-4}$. The $e_1$ case is exact by geometry
($x_1=0$ slice is $B_4^4$, so $S(e_1)=c_0^4=10.799516629\\ldots$),
quadrature cross-check $6.3\\times10^{-14}$.

## Limitations

The full $D(K)+E(K)\\ge\\kappa T(K)$ rigidity with $\\kappa>0.01$ is NOT
proved; only the fallback six-interval table is claimed. Error bounds are
analytic majorants plus a quantified $10^{-7}$ rounding allowance, not
bit-verified interval arithmetic; margins (ratio excess $0.168$, width
headroom $25\\%$, $e_1$ check $6\\times10^{-14}$) exceed the allowance by
orders of magnitude. H-K citation is as above with $p=4,n=5$
specialization derived in the record.

## Reproducibility

Stdlib-only `output/artifacts/verify_sections.py` (~1 s);
committed output `output/artifacts/verify_log.txt`. Auditor re-executed
and reproduced the log exactly.

## References

- A. Koldobsky, *Fourier Analysis in Convex Geometry*, AMS Surveys and
  Monographs vol. 105 (2005), Ch. 2 Thm 2.1, Eq. (2.4); Ch. 4 Lemma 4.2/Cor. 4.3.
- H. König, On maximal hyperplane sections of the unit ball of $l_p$ for
  $p>2$, arXiv:2409.06432.
- A. Giannopoulos, A. Koldobsky, A. Zvavitch, Inequalities for sections
  and projections of convex bodies, arXiv:2302.04347.
- Admission triage: 3D Mahler resolution arXiv:2605.09334; slicing via
  small-ball estimates arXiv:2501.06854; $L^p$-polarity arXiv:2304.14363.
