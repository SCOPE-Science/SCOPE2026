# Linear Kohn collapse rate on worm blow-ups: explicit O(δ) upper bound

## Context

The Diederich–Fornæss worm domains in $\mathbb{C}^2$ are the central examples
of smooth bounded pseudoconvex domains with pathological $\bar\partial$-Neumann
behaviour: Barrett showed failure of Sobolev regularity of the Bergman
projection and Christ established global irregularity of the
$\bar\partial$-Neumann problem. A quantitative form of degeneracy is the rate at
which the lowest Kohn eigenvalue collapses under anisotropic blow-up at a point
of the critical Levi-flat annulus. The admitted target asks: for the worm
$W_\pi$ blown up by the Levi-adapted dilation $D_\delta$, does
$\lambda_1(\delta)=\inf\mathrm{spec}\,\Box_\delta$ satisfy
$\lambda_1(\delta)\le C\delta$ for explicit $C,\delta_0$, with a tabulated
Rayleigh-quotient ledger, or does a rigorous slower-collapse lower bound hold?

## Definitions

Standard smooth worm representative (Diederich–Fornæss/Barrett):
$$\rho(z)=|z_1+e^{i\pi L}|^2-1+\eta(L),\qquad L=\log|z_2|^2,$$
with smooth cutoff $\eta\ge 0$, $\eta\equiv 0$ for $|L|\le 1/2$.
Put $p_0=(0,1)$ on the critical annulus and the global anisotropic dilation
$$D_\delta(z_1,z_2)=\left(\frac{z_1}{\delta},\frac{z_2-1}{\sqrt\delta}\right),
\qquad \Omega_\delta=D_\delta(W_\pi),$$
normal weight $1$, tangential weight $1/2$.
Let $\Box_\delta$ be the $\bar\partial$-Neumann Kohn Laplacian on $(0,1)$-forms
on $\Omega_\delta$ with Euclidean metric and
$\lambda_1(\delta)=\inf\mathrm{spec}\,\Box_\delta$.
For $0\ne u\in\mathrm{Dom}(\bar\partial)\cap\mathrm{Dom}(\bar\partial^*)$,
$Q_\delta(u)=(\|\bar\partial u\|^2+\|\bar\partial^*u\|^2)/\|u\|^2$ and
$\lambda_1(\delta)\le Q_\delta(u)$.

## Result

**Theorem.** With $C=6144/5=1228.8$ and $\delta_0=1$,
$$\lambda_1(\delta)\le C\,\delta\qquad\text{for }0<\delta\le 1.$$
More precisely, there is an explicit quasimode family $u_\delta$ compactly
supported strictly inside $\Omega_\delta$ with exact quotient
$Q_\delta(u_\delta)=\delta^2 A+\delta B\le C\delta$,
$A=B=3072/5$.

Ledger: $\delta=1: \le 1228.8$; $10^{-1}: \le 122.88$;
$10^{-2}: \le 12.288$; $10^{-3}: \le 1.2288$;
$10^{-4}: \le 0.12288$; $10^{-6}: \le 0.0012288$.

## Proof / evidence

Fix $\psi(\zeta)=(1-|\zeta|^2)^3_+$ on $\mathbb{C}^2$, supported in the closed
unit ball, $C_c^2$ (smooth inside; smoothable at the rim without changing the
bound, or approximable in $H^1$). With $q=(-1/2,1)$, $r=1/16$ set
$a(z)=\psi((z-q)/r)$ and $\alpha=a\,d\bar z_2$.

Inclusion lemma: $\overline{B(q,r)}\subset W_\pi$ with margin
$\rho\le -0.03$. Indeed for $z$ in the ball, $|z_2-1|\le 1/16$ gives
$|L|\le 2/15<1/2$ so $\eta(L)=0$; with $\theta=\pi L$,
$|e^{i\theta}-1|\le|\theta|\le 2\pi/15<0.42$, and
$|z_1+e^{i\theta}|\le 1/16+1/2+0.42=0.9825<1$ (numerically $0.9680<1$ with
exact logs). Hence $\mathrm{supp}\,\alpha\Subset W_\pi$.

Push forward by the biholomorphism $D_\delta$:
$u_\delta=(D_\delta^{-1})^*\alpha=\varphi_\delta\,d\bar w_2$,
$\varphi_\delta(w)=\sqrt\delta\,a(\delta w_1,1+\sqrt\delta\,w_2)$,
smooth and compactly supported strictly inside $\Omega_\delta$, hence in
$\mathrm{Dom}(\Box_\delta)$. With $dV_w=\delta^{-3}dV_z$,
$\|u_\delta\|^2=\delta^{-2}\|a\|^2$,
$\|\bar\partial u_\delta\|^2=\|\partial_{\bar z_1}a\|^2$,
$\|\bar\partial^*u_\delta\|^2=\delta^{-1}\|\partial_{z_2}a\|^2$.
Thus with $\delta$-independent $A,B$,
$Q_\delta(u_\delta)=\delta^2 A+\delta B$.

Constants by Beta integrals: on the unit ball in $\mathbb{C}^2$,
$dV=2\pi^2 r_d^3 dr_d$,
$\|\psi\|^2=\pi^2B(2,7)=\pi^2/56$,
$\|\partial_{\bar\zeta_j}\psi\|^2=\frac92\pi^2B(3,5)=3\pi^2/70$,
since $\partial_{\bar\zeta_j}\psi=-3(1-r_d^2)^2\zeta_j$ and each
$|\zeta_j|^2$ carries half of $r_d^2$; $B(2,7)=1/56$, $B(3,5)=1/105$
exactly, ratio $12/5$. Scaling by $1/r^2$ with $r=1/16$ gives
$A=B=(12/5)/r^2=3072/5$. Hence for $\delta\le 1$,
$Q_\delta=\delta^2A+\delta B\le (A+B)\delta=(6144/5)\delta$.
The variational principle yields $\lambda_1(\delta)\le Q_\delta$.
All rational identities and the ledger are machine-checked in
`artifacts/ledger.py`. The Levi-flat structure at $p_0$ is unused: upper
bounds only need interior trial forms.

## Limitations

Proves only the linear upper-bound (collapse) alternative; no sharpness and no
lower bound (disproof direction) is claimed. Uses one standard smooth worm
representative with $\eta$ vanishing near $L=0$ and the stated global
anisotropic dilation, and the standard variational principle for the
$\bar\partial$-Neumann Kohn Laplacian. The constant $6144/5$ is explicit but
not claimed optimal.

## Reproducibility

Run `python3 artifacts/ledger.py`: checks $C=24/(5r^2)=6144/5$,
$B(2,7)=1/56$, $B(3,5)=1/105$, $A=B=3072/5$, the interior-ball bounds
$|L|\le 0.1291<1$, $|z_1+e^{i\theta}|\le 0.9680<1$, and prints the ledger.

## References

Diederich–Fornæss worm domains; Barrett, Sobolev irregularity on worms;
Christ, Global $C^1$ irregularity of the $\bar\partial$-Neumann problem for
worm domains; Fu–Straube compactness and Property (P) theory; standard
$\bar\partial$-Neumann $L^2$ theory (Kohn, Catlin); Beta function identities
$B(2,7)=1/56$, $B(3,5)=1/105$.
