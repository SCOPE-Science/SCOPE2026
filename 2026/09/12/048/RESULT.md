# Disproof of the limiting-centered quantitative deformed sparse-edge Tracy–Widow rate

## Context

The target asks whether the largest eigenvalue of a sparse deformed Wigner matrix
$X=H+A$ satisfies a quantitative Tracy–Widom limit about the fixed limiting
free-convolution edge $E_+$ with an explicit polynomial rate $N^{-c}$, uniformly
over the admissible sparsity, deformation, and regularity parameters. The known
positive input is Lee–Schnelli edge universality for deformed Wigner matrices,
which centers at the finite-$N$ edge $E_{+,N}$ determined by the empirical
deformation law. The question is whether the limiting center $E_+$ may be
substituted while retaining a polynomial rate under only weak convergence
$\nu_N\to\nu$.

## Definitions

Fix $\delta=1/4$, $a=1/2$, $s_-=1/4$, $s_+=2$.
Let $H_{ij}=\xi_{ij}/\sqrt N$ with i.i.d. Rademacher atoms ($\pm1$), hence
mean-zero, variance-one, bounded/subexponential, and take $p=1$ (dense subcase,
admissible since $Np=N\ge N^{1/3+\delta}=N^{7/12}$).
Let $A_N=\mathrm{diag}$ with $r_N$ entries $+a$ and $N-r_N$ entries $-a$, where
on the subsequence $N_k=(2m)^4$ ($m=3,4,\dots$),
$r_k=N_k/2+N_k^{3/4}/2$ and $\alpha_{N_k}:=r_k/N_k=1/2+N_k^{-1/4}/2$;
off the subsequence $r_N=\lfloor N/2\rfloor$.
Then $\alpha_N\to1/2$ so
$\nu_N=\alpha_N\delta_{+a}+(1-\alpha_N)\delta_{-a}\to
\nu=(\delta_{-a}+\delta_{+a})/2$ weakly.
For $\nu_\alpha=\alpha\delta_{+a}+(1-\alpha)\delta_{-a}$ the Pastur equation is
$m=\alpha/(a-z-m)+(1-\alpha)/(-a-z-m)$.
With $\zeta=z+m$,
$\Phi_\alpha(\zeta)=\zeta+\alpha/(\zeta-a)+(1-\alpha)/(\zeta+a)$ for $\zeta>a$,
$h(s,\alpha)=\alpha/(s-a)^2+(1-\alpha)/(s+a)^2$,
$\Phi_\alpha'(\zeta)=1-h(\zeta,\alpha)$.
The upper edge is $E(\alpha)=\Phi_\alpha(u(\alpha))$ where $u(\alpha)>a$ is the
unique root of $h(\cdot,\alpha)=1$.
The limiting edge is $E_+=E(1/2)$; the finite-$N$ edge is $E_{+,N}=E(\alpha_N)$.
Since $\Phi_\alpha'(u(\alpha))=0$,
$E'(\alpha)=\partial_\alpha\Phi(u(\alpha))
=1/(u-a)-1/(u+a)=2a/(u^2-a^2)=1/(u^2-1/4)$ at $a=1/2$.
Let $\mu_1$ be the largest eigenvalue of $X_N=H_N+A_N$, $\gamma>0$ the fixed
limiting curvature, and $F_1$ the GOE Tracy–Widow law.

## Result

With the above admissible tuple, no pair $(c,N_0)$ with $c>0$ satisfies
$\sup_s|\mathbb P(\gamma^{2/3}N^{2/3}(\mu_1-E_+)\le s)-F_1(s)|\le N^{-c}$
for all $N\ge N_0$.
In fact along $N_k\to\infty$ the left side stays $\ge1/2$: the rescaled
statistic diverges to $+\infty$ in probability because the finite-$N$ edge
drifts by $\gg N^{-2/3}$. Precisely,
$b_{N_k}:=E_{+,N_k}-E_+\ge0.317\,N_k^{-1/4}$, so
$\gamma^{2/3}N_k^{2/3}b_{N_k}\ge\mathrm{const}\cdot N_k^{5/12}\to\infty$.

## Proof / evidence

Exact rational enclosures (machine-checked with `Fraction`, no floating-point
logic, status ALL_OK): $h_{1/2}(1.2)>1$ and $h_{3/5}(1.35)<1$ with $h$
decreasing in $s$ and increasing in $\alpha$ force
$u(\alpha)\in(1.2,1.35)$ for $\alpha\in[1/2,3/5]$, and
$u_0:=u(1/2)\in(1.27,1.272)$.
Hence $E'(\alpha)=1/(u^2-1/4)\ge1/(1.35^2-1/4)=400/629>0.635$ uniformly, and
$E'(1/2)=\sqrt3-1\approx0.732$.
By the mean value theorem on the subsequence,
$b_{N_k}\ge0.635\cdot\frac12N_k^{-1/4}\ge0.317N_k^{-1/4}$.
Uniform square-root regularity holds:
$1.62\le\Phi''\le4$ on the enclosure, and at $\alpha=1/2$,
$2.17\le\Phi''(u_0)\le2.371$, so the limiting edge ($E_+\approx2.2018$,
$u_0\approx1.2712$, slope $\approx0.92$, TW scale $\approx1.06/0.94$) is regular
with data in $[1/4,2]$; a Jensen plus monotonicity argument gives
single-interval support with square-root edges.
Under this uniform regular-edge control, Lee–Schnelli (arXiv:1407.8015) gives
rigidity about the finite-$N$ quantile: for every $\varepsilon>0$, $D>0$,
$\mathbb P(|\mu_1-E_{+,N}|>N^{-2/3+\varepsilon})\le N^{-D}$ eventually; with
$\varepsilon=1/12$, $D=2$,
$\mathbb P(|\mu_1-E_{+,N}|\ge N^{-7/12})\le N^{-2}$.
Writing the limiting-centered event as
$\{\mu_1-E_{+,N}\le\gamma^{-2/3}N^{-2/3}s-b_N\}$,
for fixed $s$ eventually the right side is $\le-b_{N_k}/2$, and
$b_{N_k}/2\ge0.158N_k^{-1/4}\ge N_k^{-7/12}$ for $N\ge253$.
Thus $\mathbb P(\gamma^{2/3}N_k^{2/3}(\mu_1-E_+)\le s)\le N_k^{-2}\to0$ for every
fixed $s$, while $F_1(s)\to1$; picking $s_0$ with $F_1(s_0)\ge3/4$ gives
$\sup_s|\mathbb P_{N_k}(s)-F_1(s)|\ge1/2$ eventually, contradicting any $N^{-c}$.

## Limitations

The disproof refutes only the limiting-centered quantitative rate as stated;
it does not refute qualitative Tracy–Widom universality with finite-$N$
centering $E_{+,N}$ and slope $\gamma_N$ (the Lee–Schnelli theorem).
The rigidity step is a cited theorem applied under verified uniform regularity,
not re-proved; $F_1(s)\to1$ is used as known.
The counterexample uses the dense ($p=1$) subcase, so it says nothing new about
genuinely sparse-only mechanisms.
A quantitative hypothesis such as $|\alpha_N-1/2|=O(N^{-2/3-\omega})$ would
restore a chance for the limiting-centered rate.

## Reproducibility

Run `python3 output/artifacts/verify_edge_bias.py`; all exact rational checks
must print PASS and final ALL_OK. The proof otherwise uses only the quoted
fractions, the cited rigidity bound, and the $F_1$ tail.

## References

- J. O. Lee, K. Schnelli, Edge universality for deformed Wigner matrices,
  arXiv:1407.8015; Rev. Math. Phys. 27 (2015).
- J. O. Lee, K. Schnelli, Extremal eigenvalues and eigenvectors of deformed
  Wigner matrices, arXiv:1310.7057.
- K. Schnelli, Y. Xu, Convergence rate to Tracy–Widom laws for Wigner
  matrices, Commun. Math. Phys. 393 (2022); EJP 2023 refinements.
