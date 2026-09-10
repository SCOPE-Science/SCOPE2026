# Certified Hawking-mass anchor at r=10 for extreme-mass-ratio Brill–Lindquist data (1, 0.01, d=3)

## Context
Time-symmetric vacuum Brill–Lindquist (BL) data with bare masses
$(m_1,m_2)=(1,0.01)$ and puncture separation $d=3$ is the canonical
scalar-flat axisymmetric perturbation of Schwarzschild with ADM mass
$m_{\mathrm{ADM}}=1.01$. Explicit finite-radius quasi-local mass anchors
on such data scope horizon searches and initialize inverse-mean-curvature-flow
(Geroch) arguments. No prior source states a Hawking-mass interval or
outer-untrapped certificate for this cell at a fixed asymptotic anchor sphere.

## Definitions
On $\mathbb{R}^3\setminus\{p_1,p_2\}$ with
$p_1=(0,0,+3/2)$, $p_2=(0,0,-3/2)$ ($d=3$):
$$g=\psi^4\,\delta,\qquad
\psi(x)=1+\frac{m_1}{2r_1}+\frac{m_2}{2r_2},\quad r_i=|x-p_i|,$$
so $R(g)=0$ and $m_{\mathrm{ADM}}=m_1+m_2=1.01$.
Let $S_{r=10}=\{|x|=10\}$ with outward unit normal.
Time symmetry ($K\equiv 0$) gives $\theta^+=H_g$ (physical mean curvature).
Hawking mass:
$$m_H(S)=\sqrt{\frac{A}{16\pi}}\left(1-\frac{1}{16\pi}\int_S H_g^2\,dA_g\right).$$
By axisymmetry put $c=\cos t\in[-1,1]$, $R=10$:
$$q_1=102.25-30c=r_1^2,\quad q_2=102.25+30c=r_2^2,$$
$$\psi=1+\frac{1}{2r_1}+\frac{0.01}{2r_2},\qquad
\frac{d\psi}{dr}=-\left[\frac{10-1.5c}{2r_1^3}
+\frac{0.01\,(10+1.5c)}{2r_2^3}\right],$$
$$H_g=\psi^{-2}\frac{2}{R}+4\psi^{-3}\frac{d\psi}{dr},$$
$$A=2\pi R^2\int_{-1}^{1}\psi^4\,dc,\quad
I=2\pi R^2\int_{-1}^{1}H_g^2\psi^4\,dc,\quad
m_H=\sqrt{\frac{A}{16\pi}}\left(1-\frac{I}{16\pi}\right).$$

## Result
For the above data, the coordinate sphere $S_{r=10}$ satisfies:
- (a) $S_{r=10}$ is strictly outer-untrapped:
  $\min_{S_{r=10}}\theta^+=\min H_g\ge 0.10$ (certified $\ge 0.1548055$);
- (b) $m_H(S_{r=10})\in[0.96,1.06]$ (certified $m_H\in[1.00568,1.01022]$).

Corollary (by citation, existence-conditional): if a connected outermost
(outer-minimizing) MOTS $\Sigma_{\mathrm{out}}$ enclosed by $S_{r=10}$ exists,
then by the cited Riemannian Penrose inequality (Huisken–Ilmanen, JDG 2001,
Main Theorem; $R(g)=0$, weak-IMCF Geroch monotonicity from the outermost
horizon, enclosure by the certified outer-untrapped $S_{r=10}$):
$$A(\Sigma_{\mathrm{out}})\le 16\pi\,m_{\mathrm{ADM}}^2
=16\pi(1.01)^2\approx 51.28\le 16\pi(1.06)^2\approx 56.48.$$
No bound on arbitrary non-outermost enclosed MOTS is claimed.

## Proof / Evidence
$[-1,1]$ in $c$ is partitioned into $N=400$ equal panels (width $1/200$,
exact in $\mathbb{Q}$). On each panel
$(q_1,q_2,\psi,d\psi/dr,H_g,\psi^4,H_g^2\psi^4)$ are evaluated with exact
rational (`Fraction`) interval arithmetic; square roots via rigorous
floor/ceil integer enclosures; $\pi\in[3.141592653589793,3.141592653589794]$.
Summing panelwise $h\cdot[\inf,\sup]$ brackets both integrals. Output:
$$\min H_g\ge 0.1548055\ge 0.10,$$
$$J_1=\int\psi^4\,dc\in[2.43571,2.43608],\quad
J_2=\int H^2\psi^4\,dc\in[0.0653545,0.0654192],$$
$$A\in[1530.40,1530.63],\quad I/(16\pi)\in[0.81693,0.81774],$$
$$m_H\in[1.00568,1.01022]\subset[0.96,1.06].$$
Margins: $0.055$ on $\theta^+$, $\ge 0.045$ on each side of $m_H$.
Pointwise values ($H=0.15483$ north pole, $0.16455$ equator, $0.16994$ south
pole) agree with direct evaluation. The interval certificate proves (a)–(b);
the area cap is quoted from Huisken–Ilmanen, not derived from the computation
(the certified $m_H(S)\le 1.01022$ is not used for the cap; the cap is stated
at the weaker quoted ADM level).

## Limitations
- Proves only the single-sphere anchor (a)–(b); the full outermost
  pin/gap/eigenvalue target is not claimed.
- Area corollary is conditional on outermost-MOTS existence and cited; it is
  not an interval-computed bound and does not apply to non-outermost MOTS.
- No minimizing-hull (ALY) or Wang–Liu–Yau comparison is invoked.

## Reproducibility
`python3 output/artifacts/certify_fallback.py` (stdlib only, with
`output/artifacts/interval.py`) prints `PASS_a: True`, `PASS_b: True` and the
intervals above. Independent float check `inputs/artifacts/anchor.py` gives
$A\approx1530.52$, $m_H\approx1.00795$ inside the certified intervals.

## References
- Huisken–Ilmanen, The Inverse Mean Curvature Flow and the Riemannian Penrose
  Inequality, JDG 2001 (cited area-cap tool).
- Brill–Lindquist, Interaction Energy in Geometrostatics, Phys. Rev. 1963
  (data family).
- Andersson–Mars–Simon, Stability of MOTS and existence of MOTTs (framework,
  no cell numbers); Alaee–Lesourd–Yau, localized Penrose (abstract criteria,
  no cell numbers); Thornburg, horizon finders review (no mass certificate).
