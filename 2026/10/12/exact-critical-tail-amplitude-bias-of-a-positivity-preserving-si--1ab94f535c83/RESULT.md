# Exact critical-tail amplitude bias of a positivity-preserving SIR balanced implicit method

## Finding

At the exact deterministic SIR invasion threshold, the constant-step balanced implicit method (BIM) in Schurz and Tosun (2026, equations (12)–(13)) preserves the extinction equilibrium but changes the universal critical infected-population amplitude. In the noise-free specialization with \(k=\alpha+\gamma+\mu=\beta K\), every admissible initial state with \(I_0>0\) and every fixed \(h>0\) satisfies
\[
\lim_{n\to\infty}nhI_n=\frac{\mu(1+kh)}{\beta k},
\qquad
\lim_{t\to\infty}tI(t)=\frac{\mu}{\beta k}.
\]
Here \(t=nh\) is physical time, \(I_n\) is the BIM infected coordinate, and \(I(t)\) is the infected coordinate of the original continuous model with the same initial state. The **exact critical-tail amplitude ratio** is \(1+kh\), independent of initial conditions. Consequently, all-step positivity, invariance, and fixed-finite-time convergence do not ensure reproduction of the leading critical relaxation amplitude at a fixed positive step.

## Assumptions and scope

Let \(K,\alpha,\gamma,\mu,\beta,h\) be strictly positive constants, set \(k=\alpha+\gamma+\mu\), and assume the exact threshold \(\beta K=k\). Set the noise intensities \(F_1\equiv F_2\equiv0\), which is permitted by the source's diffusion-function conditions. Start at arbitrary \(S_0>0\), \(I_0>0\), \(R_0>0\) with \(S_0+I_0+R_0\le K\). No limit in population size or step size is taken; \(h\) remains fixed while \(n\to\infty\).

The continuous system is
\[
\dot S=-\beta SI+\mu(K-S),\quad
\dot I=(\beta S-k)I,\quad
\dot R=\alpha I-\mu R.
\]
The source BIM (12)–(13), when both noise coefficients vanish and the mesh is constant, is the exactly defined recurrence
\[
(S_{n+1},I_{n+1},R_{n+1})=(S_n,I_n,R_n)+\tau_n\bigl(-\beta S_nI_n+\mu(K-S_n),\;(\beta S_n-k)I_n,\;\alpha I_n-\mu R_n\bigr),
\quad \tau_n=\frac h{1+h(k+\beta I_n)}.
\]

## Proof

**1. Invariance and extinction for the discrete scheme.** Put \(x_n=K-S_n\) and \(N_n=S_n+I_n+R_n\). At criticality the recurrence becomes
\[
I_{n+1}=I_n(1-\beta\tau_nx_n),\qquad
x_{n+1}=(1-\mu\tau_n)x_n+\beta\tau_nS_nI_n,\qquad
R_{n+1}=(1-\mu\tau_n)R_n+\alpha\tau_nI_n.
\]
Its susceptible coordinate can also be written
\[
S_{n+1}=\frac{S_n(1+h(k-\mu))+h\mu K}{1+h(k+\beta I_n)}>0,
\]
while the infected numerator is \(I_n[1+h\beta(S_n+I_n)]>0\) and the removed numerator is \(R_n[1+h(k+\beta I_n-\mu)]+h\alpha I_n>0\). These formulas use only \(k>\mu\). Moreover
\[
N_{n+1}=N_n+\tau_n[\mu(K-N_n)-\gamma I_n],
\]
and \(0<\mu\tau_n<1\), proving inductively \(0<S_n\), \(0<I_n\), \(0<R_n\), and \(N_n\le K\) for every \(n\). Hence \(x_n=K-S_n\ge I_n+R_n>I_n\). We also have \(I_{n+1}<I_n\) and \(I_{n+1}>0\). Since \(0<I_n\le K\), the effective step satisfies
\[
\tau_n\ge\frac h{1+h(k+\beta K)}>0.
\]
Were \(I_n\to\ell>0\), then for all sufficiently large \(n\) the above infected recurrence would contract by at least a fixed factor strictly smaller than one, contradiction. Thus \(I_n\to0\). The stable scalar recurrence for \(x_n\), with \(\tau_n\to\tau_*=h/(1+kh)\), bounded \(S_n\), and forcing \(\beta\tau_nS_nI_n\to0\), implies \(x_n\to0\). Consequently \(S_n\to K\), and the analogous stable recurrence gives \(R_n\to0\).

**2. Discrete critical amplitude.** The strictly positive ratio \(r_n=x_n/I_n\) satisfies exactly
\[
r_{n+1}=\frac{(1-\mu\tau_n)r_n+\beta\tau_nS_n}{1-\beta\tau_nx_n}.
\]
The affine coefficient converges to \(1-\mu\tau_*\in(0,1)\), and its forcing converges to \(\beta\tau_*K\). The elementary contractive affine-recursion lemma therefore gives \(r_n\to\beta K/\mu=k/\mu\). (For completeness, subtract the limiting fixed point, choose a coefficient bound \(q<1\) eventually, and bound the error by \(q\) times its predecessor plus a forcing tending to zero.) The reciprocal infected increment has the exact identity
\[
\frac1{I_{n+1}}-\frac1{I_n}=
\frac{\beta\tau_n r_n}{1-\beta\tau_nx_n}
\longrightarrow\frac{\beta k}{\mu}\tau_*.
\]
Cesàro summation thus yields \((nI_n)^{-1}\to\beta k\tau_*/\mu\), equivalently \(nhI_n\to\mu(1+kh)/(\beta k)\).

**3. Continuous critical amplitude.** With \(x(t)=K-S(t)\) and \(r(t)=x(t)/I(t)\), positivity and the invariant simplex follow from the vector field's boundary conditions and \(N'=\mu(K-N)-\gamma I\). At criticality \(I'=-\beta xI\le-\beta I^2\), so \(I(t)\to0\). The forced stable equation \(x'=-\mu x+\beta SI\) gives \(x(t)\to0\), so \(S(t)\to K\). Direct differentiation yields \(r'=\beta S-(\mu-\beta x)r\). For all sufficiently large \(t\), \(\mu-\beta x(t)>\mu/2\), and standard variation of constants gives \(r(t)\to\beta K/\mu=k/\mu\). Finally \((1/I)'=\beta r\to\beta k/\mu\). Integrating and dividing by \(t\) proves \(tI(t)\to\mu/(\beta k)\).

## Verification

The included independent arithmetic recurrence checker `verify.py` checks exact-rational invariance and reciprocal-increment identities for an admissible parameter instance, and numerically examines the critical asymptotics over up to \(10^6\) time steps. In that instance \(K=\mu=\alpha=\gamma=1\), \(\beta=3\), \(h=1/4\), and \((S_0,I_0,R_0)=(7/10,1/5,1/10)\). The theorem predicts \(\lim nI_n=7/9\), \(\lim nhI_n=7/36\), and the continuous physical-time coefficient \(1/9\), a ratio of \(7/4\). Finite computations illustrate, but do not prove, the asymptotic quantifiers. The analytic proof above supplies the infinite-time argument.

## Relationship to prior work

Schurz and Tosun (2026) establish unconditional invariant-domain preservation and finite-horizon convergence for their BIM and provide sub-/supercritical SIR examples. Their paper states the recurrence and the critical reproduction number, but its theorems do not quantify the leading algebraic relaxation amplitude at equality. The result here specializes their recurrence to the permitted zero-noise case, derives an exact \(h\)-dependent infinite-horizon coefficient, and compares it with the continuous flow. It is not a counterexample to their fixed-horizon convergence theorem, nor does it assert anything about stochastic fluctuations at nonzero diffusion. Other positive numerical SIR schemes and stochastic SIS linearizations use different update maps and do not imply this specific coefficient without an additional calculation.

## Limitations

The theorem treats the deterministic zero-noise specialization and the exact threshold only. It does not address weakly nonzero stochastic forcing, arbitrary nonuniform time meshes, endemic persistence, noncritical rates, or epidemiological data. The direct coefficient follows from the published numerical equations as written; no independent scientific audit or empirical validation has been performed. Possible unindexed earlier analysis of this same amplitude remains a literature risk.

## References

1. H. Schurz and K. Tosun, “Numerical Analysis of BIMs for Stochastic SIR and SIS Models with Variable Contact Diffusion Rates,” *Journal of Mathematical Biology* 92, article 88 (first online 2026-05-14). DOI: 10.1007/s00285-026-02392-4. Full open-access source: https://link.springer.com/article/10.1007/s00285-026-02392-4.
2. H. Zhou, Y. Hu, and J. Zhao, “Explicit-implicit methods for stochastic susceptible-infected-recovered model,” *Numerical Algorithms* 100 (2025), 1199–1238 (first online 2024-11-27). DOI: 10.1007/s11075-024-01986-7. Different scheme and stochastic model.
3. H. Schurz and K. Tosun, “Stochastic asymptotic stability of SIR model with variable diffusion rates,” *Journal of Dynamics and Differential Equations* 27 (2015), 69–82. DOI: 10.1007/s10884-014-9415-9. SDE stability rather than numerical critical-tail bias.
