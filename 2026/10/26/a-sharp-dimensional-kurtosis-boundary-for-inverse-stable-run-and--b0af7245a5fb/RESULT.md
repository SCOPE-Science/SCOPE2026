# A sharp dimensional kurtosis boundary for inverse-stable run-and-tumble transport

## Finding
For each integer \(d\geq1\), a time-fractional isotropic run-and-tumble flight has an exact critical fractional order \(\nu_d\in(0,1)\), uniquely defined by
\[
\frac{\Gamma(1+4\nu_d)}{\Gamma(1+2\nu_d)^2}=\frac{6d}{d+2}.
\]
For \(\nu_d<\nu<1\), the excess kurtosis of **every fixed unit-direction projection** is negative at all sufficiently small positive times, positive at all sufficiently large times, and therefore crosses zero at least once at a finite time. The threshold is independent of the particle speed and reorientation rate. It is strictly increasing in dimension, with \(\nu_1=1/2\), \(\nu_2=0.693572909926\ldots\), and
\[
\nu_d=1-\frac{6}{7d}+O(d^{-2})\qquad(d\to\infty).
\]
For \(0<\nu<\nu_d\), the kurtosis is positive in **both** limiting time regimes; no claim about its sign at all intervening times is made. At the equality order the short-time limit vanishes, without any claim of an all-time sign law.

## Assumptions and scope
Choose an integer dimension \(d\geq1\), speed \(v>0\), collision intensity \(\alpha>0\), and fractional order \(0<\nu<1\). The operational-time motion begins at the origin with uniform unit-sphere direction \(U_0\). It obeys
\[
X(u)=v\int_0^u U_q\,dq,
\]
where \(U_q\in\mathbb S^{d-1}\) is independently redrawn uniformly at each event of a rate-\(\alpha\) Poisson process, also independently of \(U_0\). In dimension one this convention has actual sign reversals at rate \(\alpha/2\), rather than \(\alpha\). Let \(S_\nu(u)\) be an independent strictly \(\nu\)-stable subordinator normalized by \(\mathbb E[e^{-sS_\nu(u)}]=e^{-us^\nu}\), and define its inverse clock \(E_\nu(t)=\inf\{u>0:S_\nu(u)>t\}\). For any deterministic unit vector \(e\), set \(Z_t=e\cdot X(E_\nu(t))\). Define \(M_j(t)=\mathbb E[Z_t^j]\) and the excess kurtosis
\[
K_{d,\nu}(t)=\frac{M_4(t)}{M_2(t)^2}-3,\qquad t>0.
\]
The variance is positive at every positive time, and odd moments vanish by directional symmetry. No finite-speed assertion is made about the physical-time-changed motion.

## Proof
**Step 1 (operational moments).** By isotropy we may take \(e\) along the first coordinate. Write \(Y=e\cdot U\). Uniform-sphere moments are
\[
\mu_2=\mathbb E[Y^2]=\frac1d,\qquad
\mu_4=\mathbb E[Y^4]=\frac{3}{d(d+2)}.
\]
The Markov generator acting on a polynomial \(f(x,y)\) is \(\mathcal Lf=v y\partial_x f+\alpha(\mathbb E_{Y'}f(x,Y')-f(x,y))\). With \(m_{p,q}(u)=\mathbb E[(e\cdot X(u))^pY_u^q]\), differentiation gives
\[
m'_{p,q}=pv\,m_{p-1,q+1}-\alpha m_{p,q}+\alpha\mu_qm_{p,0},
\]
where the last two terms cancel for \(q=0\) and \(m_{0,q}=\mu_q\). Solving the triangular moment system in the operational-time Laplace variable \(w>0\) gives the **exact** second- and fourth-moment transforms
\[
\widehat M^{\mathrm{op}}_2(w)=\frac{2v^2\mu_2}{w^2(w+\alpha)},\qquad
\widehat M^{\mathrm{op}}_4(w)=
\frac{24v^4(\mu_4w+\alpha\mu_2^2)}{w^3(w+\alpha)^3}.
\]
The full generator computation is reproduced independently in `check.py`.

**Step 2 (fractional subordination and exact transforms).** The inverse stable clock has density kernel \(q_\nu(u,t)\) with
\[
\int_0^\infty e^{-st}q_\nu(u,t)\,dt=s^{\nu-1}e^{-us^\nu}.
\]
Independence implies the physical-time moments have exact Laplace transforms
\[
\widehat M_2(s)=\frac{2v^2\mu_2}{s^{\nu+1}(s^\nu+\alpha)},\qquad
\widehat M_4(s)=\frac{24v^4(\mu_4s^\nu+\alpha\mu_2^2)}{s^{2\nu+1}(s^\nu+\alpha)^3}.
\]
These formulas hold for every \(s>0\) and every permitted parameter choice.

**Step 3 (two time regimes without an unproved Tauberian inference).** By stable scaling, \(E_\nu(t)\) equals \(t^\nu E_\nu(1)\) in distribution, and, for each nonnegative integer \(j\),
\[
\mathbb E[E_\nu(t)^j]=\frac{j!\,t^{j\nu}}{\Gamma(1+j\nu)}.
\]
At operational time \(u\downarrow0\), absence of a collision to first order gives \(\mathbb E[(e\cdot X(u))^2]\sim v^2\mu_2u^2\) and \(\mathbb E[(e\cdot X(u))^4]\sim v^4\mu_4u^4\). The bound \(|e\cdot X(u)|\le vu\) and the finite inverse-clock moments justify dominated convergence after time change. Consequently,
\[
M_2(t)\sim\frac{2v^2\mu_2t^{2\nu}}{\Gamma(1+2\nu)},\qquad
M_4(t)\sim\frac{24v^4\mu_4t^{4\nu}}{\Gamma(1+4\nu)}\quad(t\downarrow0).
\]
In the opposite regime, inverse Laplace transformation of the rational operational transforms yields
\[
M^{\mathrm{op}}_2(u)=\frac{2v^2\mu_2}{\alpha}u+O(1),\qquad
M^{\mathrm{op}}_4(u)=\frac{12v^4\mu_2^2}{\alpha^2}u^2+O(u+1).
\]
The same expressions have polynomial global upper bounds, so stable-clock scaling and dominated convergence give
\[
M_2(t)\sim\frac{2v^2\mu_2}{\alpha\Gamma(1+\nu)}t^\nu,\qquad
M_4(t)\sim\frac{24v^4\mu_2^2}{\alpha^2\Gamma(1+2\nu)}t^{2\nu}\quad(t\to\infty).
\]
It follows that
\[
\boxed{\lim_{t\downarrow0}K_{d,\nu}(t)=\frac{18d}{d+2}\frac{\Gamma(1+2\nu)^2}{\Gamma(1+4\nu)}-3},
\]
while
\[
\boxed{\lim_{t\to\infty}K_{d,\nu}(t)=6\frac{\Gamma(1+\nu)^2}{\Gamma(1+2\nu)}-3>0}.
\]
The strict inequality uses strict monotonicity of \(\Gamma(1+2\nu)/\Gamma(1+\nu)^2\), which rises from one to two as \(\nu\) rises from zero to one; this follows on differentiating its logarithm and using strict increase of the digamma function.

**Step 4 (sharp threshold and crossings).** Set \(F(\nu)=\Gamma(1+4\nu)/\Gamma(1+2\nu)^2\). The logarithmic derivative is
\[
\frac{F'(\nu)}{F(\nu)}=4\big[\psi(1+4\nu)-\psi(1+2\nu)\big]>0.
\]
Further, \(F(0)=1\) and \(F(1)=6\), while \(6d/(d+2)\in(1,6)\). Thus exactly one critical order exists, and the short-time excess has the sign of \(6d/(d+2)-F(\nu)\). Since the long-time limit is strictly positive, the opposite initial and final signs for \(\nu>\nu_d\), together with continuity of \(M_2,M_4\) and \(M_2>0\), force at least one positive finite-time zero by the intermediate value theorem. Neither uniqueness nor monotonicity of the time profile is assumed.

Strict increase of \(d\mapsto\nu_d\) follows because \(6d/(d+2)\) increases with dimension. At \(d=1\), \(F(1/2)=2\), so \(\nu_1=1/2\) exactly. Finally, \(F'(1)=14\) and \(6d/(d+2)=6-12/d+O(d^{-2})\). Taylor expansion of the implicit equation gives \(\nu_d=1-6/(7d)+O(d^{-2})\).

## Verification
Run `python check.py` with Python 3, SymPy, and mpmath. The standalone script rebuilds the polynomial-generator Laplace recursion, symbolically checks both exact transforms and their operational-time leading coefficients, numerically solves the unique critical-order equation for six dimensions, verifies limiting positivity for five orders, and independently inverts the physical-time Laplace formulas at selected short and long times. It passes all explicit assertions. For example, \(d=1,\nu=0.7\) gives excess kurtosis approximately \(-0.9869694\) at \(t=0.02\) and \(0.8999257\) at \(t=200\) when \(v=\alpha=1\). Numerical examples are auxiliary; all parameter-uniform conclusions come from the proof.

## Relationship to prior work
Angelani, De Gregorio, Garra, and Iafrate (2024), arXiv:2404.15941, formulate the same uniform-reorientation finite-velocity random flight and its inverse-stable time change, including its mean-square displacement. Their Sections 2–4 and 6 and appendices provide the underlying process, kinetic generator, and inverse-stable kernel; the above fourth-projection-moment and dimension-by-dimension kurtosis threshold are not stated there. Masoliver's (2021) review discusses fractional telegraphic models in several dimensions, including general distance-moment asymptotic representations; its corresponding higher-dimensional telegrapher models are not automatically identical to the uniform-sphere Poisson-redirection model here. D'Ovidio, Orsingher, and Toaldo (2012), arXiv:1206.2511, establish other time-changed telegraph equations, but the exact dimension-dependent gamma-ratio threshold is not identified in the inspected accessible text. The present claim is the sharp **sign classification of the short-time projection excess**, combined with strictly positive long-time excess and therefore finite-time reversal—not the existence of inverse-stable subordination or the generic anomalous-diffusion exponents.

## Limitations
The theorem requires independent inverse-stable timing, independent uniform-direction Poisson refreshments, a fixed finite spatial dimension, and the stated no-drift unconfined model. It does not assert a unique crossing, global positivity below threshold, a sign at the equality order, thermodynamic transitions, finite-sample estimability, or generality beyond the specified process. General Fourier–Laplace representations in earlier literature may permit retrospective derivation of the moments, so a broader scholarly priority search remains necessary; no independent validation has been performed.

## References
1. L. Angelani, A. De Gregorio, R. Garra, F. Iafrate, *Anomalous random flights and time-fractional run-and-tumble equations*, arXiv:2404.15941v1 (first posted 24 April 2024), https://arxiv.org/abs/2404.15941 .
2. J. Masoliver, *Telegraphic Transport Processes and Their Fractional Generalization: A Review and Some Extensions*, Entropy 23 (2021), 364, https://doi.org/10.3390/e23030364 .
3. M. D'Ovidio, E. Orsingher, B. Toaldo, *Time-changed processes governed by space-time fractional telegraph equations*, arXiv:1206.2511 (2012), https://arxiv.org/abs/1206.2511 .
4. E. Orsingher, L. Beghin, *Time-fractional telegraph equations and telegraph processes with Brownian time*, Probab. Theory Relat. Fields 128 (2004), 141–160, https://doi.org/10.1007/s00440-003-0309-8 .
