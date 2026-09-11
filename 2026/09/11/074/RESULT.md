# Short-time weighted-L1 to L2 enlargement is false: infinite operator norm for cutoff hard-sphere torus dynamics

## Context
Enlargement from a small hypocoercive Hilbert space to large physical
$L^1$-type spaces is the recognized bottleneck for constructive Boltzmann
stability on the torus. Abstract Gualdani–Mischler–Mouhot factorization
proves enlargement with symbolic weights, powers and constants. The admitted
target fixed a concrete ledger: with $E=L^1_v(\langle v\rangle^{12}dv)
L^\infty_x$ on $\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3$ and
$H=L^2_{x,v}(dx\,dv)$, the cutoff hard-sphere linearized semigroup
$S(t)=\exp(t(L-v\cdot\nabla_x))$ about the global Maxwellian $\mu$ was
conjectured to satisfy $\|S(t)(I-\Pi)\|_{E\to H}\le 60\,t^{-5/2}$ for
$0<t\le 1$, where $\Pi$ is the global hydrodynamic projection.

## Definitions
$B=|v-v_*|$ with normalized cutoff, $\mu=(2\pi)^{-3/2}e^{-|v|^2/2}$,
$\nu(v)=\int |v-w|\mu(w)\,dw$, $L=-\nu+K$,
$Kf=Q^+(f,\mu)+Q^+(\mu,f)-Q^-(f,\mu)$.
$B_0=-v\cdot\nabla_x-\nu$ generates
$S_{B_0}(t)f(x,v)=e^{-\nu(v)t}f(x-vt,v)$, a contraction $C_0$-semigroup on
both $E$ and $H$. $K\in\mathcal B(E)$ by Grad/Povzner weighted-$L^1$ bounds
and $K:E\to H$ is bounded via Alonso–Carneiro–Gamba Young estimates for the
two gain terms and the pointwise bound
$|Q^-(f,\mu)|\le\mu\langle\cdot\rangle\|f\|_{L^1_1}$ with
$\mu\langle\cdot\rangle\in L^2_v$. Bounded perturbation gives
$S(t)\in\mathcal B(E)$ with $\sup_{s\le 1}\|S(s)\|_{E\to E}<\infty$.
No positivity, no $K\in\mathcal B(H)$, no $S\in\mathcal B(H)$ is used.
$\Pi f=\sum_{j=0}^4 a_j(f)\phi_j\mu$ with
$\phi\in\{1,v_i,(|v|^2-3)/\sqrt6\}$ and $a_j=\iint f\phi_j$.

## Result
For every $t>0$,
$\|S(t)(I-\Pi)\|_{E\to H}=+\infty$.
In particular $\|S(t)(I-\Pi)\|_{E\to H}\le 60\,t^{-5/2}$ on $(0,1]$ is false,
and no finite $(C,\alpha)$ envelope $\le C t^{-\alpha}$ holds. The violation
persists on smooth data.

## Proof / evidence
Witnesses are $x$-homogeneous velocity-ball indicators
$\psi_\varepsilon(v)=c_\varepsilon\mathbf 1_{\{|v|\le\varepsilon\}}$,
$0<\varepsilon\le 1$, $c_\varepsilon^{-1}=\int_{|v|\le\varepsilon}
\langle v\rangle^{12}dv$, so $\|\psi_\varepsilon\|_E=1$. Since
$\langle v\rangle^{12}\le 64$ on $B_1$,
$c_\varepsilon\ge 1/(64\cdot\frac{4\pi}{3}\varepsilon^3)$ and
$\|\psi_\varepsilon\|_H=(2\pi)^{3/2}c_\varepsilon
(\frac{4\pi}{3}\varepsilon^3)^{1/2}\ge c_H\varepsilon^{-3/2}$ with
$c_H=(2\pi)^{3/2}/(64\sqrt{4\pi/3})\approx 0.12024\ge 0.12$.
Transport acts trivially on homogeneous data:
$S_{B_0}(t)\psi_\varepsilon=e^{-\nu(v)t}\psi_\varepsilon$, and on
$|v|\le 1$, $\nu(v)\le |v|+\sqrt{8/\pi}\le\bar\nu:=2.6$, so
$\|S_{B_0}(t)\psi_\varepsilon\|_H\ge e^{-\bar\nu t}c_H\varepsilon^{-3/2}$.
Duhamel in $\mathcal B(E)$ gives
$S(t)\psi_\varepsilon-S_{B_0}(t)\psi_\varepsilon
=\int_0^t S_{B_0}(t-s)KS(s)\psi_\varepsilon\,ds$, hence
$\|S(t)\psi_\varepsilon-S_{B_0}(t)\psi_\varepsilon\|_H
\le t\|K\|_{E\to H}e^{\|K\|_{E\to E}t}=:B(t)<\infty$ uniformly in
$\varepsilon$, using $H$-contractivity of $S_{B_0}$.
Projection weights $m_j=\sup|\phi_j|\langle v\rangle^{-12}$ are exact:
$m_0=1$, $m_1=11^{-1/2}(12/11)^{-6}\approx 0.1789$,
$m_4=\sqrt{3/2}\approx 1.2247$. Exact Gaussian moments give
$\|\Pi\|_{E\to H}\lesssim 1374.2$ and $\|\Pi\|_{E\to E}<\infty$, so
$\|S(t)\Pi\psi_\varepsilon\|_H\le C_\Pi^H
+t\|K\|_{E\to H}e^{\|K\|t}C_\Pi^E=:C'(t)<\infty$ uniformly in $\varepsilon$,
via the Schwartz range of $\Pi$. With $g_\varepsilon=(I-\Pi)\psi_\varepsilon
\ne 0$ (compact support versus analytic Gaussian combination),
$\|S(t)g_\varepsilon\|_H\ge e^{-\bar\nu t}c_H\varepsilon^{-3/2}
-B(t)-C'(t)\to+\infty$ as $\varepsilon\to 0$ at fixed $t>0$.
$v$-mollifications $\psi_{\varepsilon,k}\to\psi_\varepsilon$ in $E$ and $H$
inherit the lower bound by $H$-contractivity of $S_{B_0}$ and $E\to H$
continuity of the remainder, and normalization by
$\|g_{\varepsilon,k}\|_E\to\|g_\varepsilon\|_E\in(0,1+C_\Pi^E]$ keeps ratios
unbounded. Thus the envelope fails on smooth data. Any $A$–$B$ splitting
bound must control the bare transport-loss term which preserves
$v$-concentration; the smoothing piece enters only convolved
$\varepsilon$-uniform remainders and cannot cancel the peak. This is
qualitatively sharp: Fokker–Planck $\Delta_v$ diffuses the peak, cutoff
Boltzmann transport does not.

## Limitations
Gain-operator finiteness $\|K\|_{E\to E}<\infty$ and $\|K\|_{E\to H}<\infty$
is cited to standard theory (Grad 1963, Alonso–Carneiro–Gamba Young,
Mouhot–Strain, Gualdani–Mischler–Mouhot memoir hal-00495786) rather than
re-proved with numeric values. The disproof is qualitative (infinite norm)
and does not identify a weaker true envelope or the optimal weight threshold
at which boundedness would resume.

## Reproducibility
Deterministic stdlib script `output/artifacts/disproof_ledger.py` certifies
$c_H\ge 0.12$, $\bar\nu\le 2.6$, exact $m_j$, $\|\Pi\|_{E\to H}\le 1374.2$,
$\|\Pi\|_{E\to E}<\infty$ via exact-integer/closed-form Gamma sums, and
$\varepsilon$-thresholds defeating any finite remainder cap $R$ up to
$10^9$. Full proof in `output/DRAFT.md` analogue (this file).

## References
- Gualdani–Mischler–Mouhot, Factorization for non-symmetric operators and
  exponential H-theorem, arXiv:1006.5523 / https://hal.science/hal-00495786v1/file/spectreFP21.pdf.
- Alexandre–Morimoto–Ukai-type inhomogeneous non-cutoff regularization;
  sharp non-cutoff regularization arXiv:2305.02861 (broader smoothing,
  different norms/regime).
- Grad 1963 weighted-$L^1$ bounds; Alonso–Carneiro–Gamba Young inequality
  for $Q^+$; Mouhot–Strain splitting theory.
