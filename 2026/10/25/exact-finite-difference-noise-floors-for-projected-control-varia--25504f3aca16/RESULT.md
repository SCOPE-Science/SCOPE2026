# Exact finite-difference noise floors for projected control-variate Gaussian descent

## Finding

A control variate can remove gradient-estimation variance while leaving a sharp finite-difference noise floor. On a quadratic with a known gradient subspace, keeping a full ambient Gaussian probing direction introduces an avoidable cubic dependence on ambient dimension even though the unknown gradient has fixed dimension.

**Theorem (exact second moments and probe-support separation).** Fix integers \(d\ge 2\) and \(1\le k<d\); put \(q=d-k\). Let \(P\) be any rank-\(k\) orthogonal projector on \(\mathbb R^d\), and let \(f(x)=\tfrac12\|x\|_2^2\). At every step use the exact reference gradient \(m(x)=Px\), a constant stepsize \(\alpha>0\), and one-sided finite-difference radius \(\tau>0\). Independently resample standard Gaussian probes at each step. Compare

\[
G_F(x,u)=Px+\frac{f(x+\tau u)-f(x)-\tau\langle Px,u\rangle}{\tau}\,u,
\qquad u\sim N(0,I_d),
\]

with

\[
G_R(x,v)=Px+\frac{f(x+\tau v)-f(x)-\tau\langle Px,v\rangle}{\tau}\,v,
\qquad v=(I-P)z,\quad z\sim N(0,I_d).
\]

Set \(x_{n+1}^{F}=x_n^{F}-\alpha G_F(x_n^{F},u_n)\) and \(x_{n+1}^{R}=x_n^{R}-\alpha G_R(x_n^{R},v_n)\), with any deterministic finite \(x_0\). Then both schemes have bounded mean-square trajectories for every initial point **exactly** when

\[
0<\alpha<\frac2{q+2}.
\]

On this interval, their exact limiting second moments exist, do not depend on \(x_0\), and satisfy

\[
\lim_{n\to\infty}\mathbb E\|x_n^F\|^2
=\frac{\alpha\tau^2(d+2)(d+4)[2d-\alpha(d+k)]}
{4(2-\alpha)[2-\alpha(q+2)]}=:F_{d,k},
\]

\[
\lim_{n\to\infty}\mathbb E\|x_n^R\|^2
=\frac{\alpha\tau^2 q(q+2)(q+4)}{4[2-\alpha(q+2)]}=:R_q.
\]

In particular \(F_{d,k}>R_q>0\) whenever \(1\le k<d\), and

\[
\frac{F_{d,k}}{R_q}
=\frac{(d+2)(d+4)[2d-\alpha(d+k)]}
{q(q+2)(q+4)(2-\alpha)}.
\]

If \(q\) and \(\alpha\in(0,2/(q+2))\) are held fixed while \(d\to\infty\), then

\[
\frac{F_{d,d-q}}{R_q}
\sim \frac{2(1-\alpha)}{q(q+2)(q+4)(2-\alpha)}d^3.
\]

Thus restricting Gaussian probes to the unknown gradient subspace preserves the exact mean-square contraction factor while removing a cubically increasing one-sided finite-difference noise penalty. This theorem applies to the named estimators and not to every method using directional hints.

## Assumptions and scope

The setting is finite-dimensional Euclidean space in exact real arithmetic. The same \(P\), \(\tau>0\), and \(\alpha>0\) are used at every iteration. The exact projected-gradient reference \(Px\) is available without error. The random probes are independent of the iterates' past and independent across iterations, and all objective values are exact. Both methods require one additional evaluation at the perturbed point, reusing \(f(x)\); sampling in the complement does not require extra objective evaluations. All expectations integrate the Gaussian sampling randomness.

The full-space estimator is the Gaussian control-variate estimator introduced by Ryabchenko, Qian and Mou [1], specialized to the exact-projection oracle. The residual-only estimator is the comparison construction analyzed here. Both estimate \(\nabla f(x)=x\) without bias **on this quadratic**. The comparison is made at equal finite-difference radius; the same parameter \(\tau\) need not represent equal expected perturbation norms in the two probe supports. The objective does not satisfy the source's globally bounded-gradient hypothesis, so this is an exact quadratic model of the estimator, not a claim about that paper's theorem on its stated function class.

## Proof

Choose an orthonormal basis adapted to \(P\), and write \(x=(a,b)\in\mathbb R^k\oplus\mathbb R^q\). Similarly write \(u=(s,w)\), where \(s\sim N(0,I_k)\) and \(w\sim N(0,I_q)\) are independent. On the quadratic,

\[
G_F(x,u)=(a,0)+\left(\langle b,w\rangle+\frac{\tau}{2}\|u\|^2\right)u.
\]

For residual-only probes \(v=(0,w)\), the same identity holds with \(u\) replaced by \(v\) and \(\|u\|^2\) replaced by \(\|w\|^2\). Gaussian odd-moment cancellation gives conditional unbiasedness, so

\[
\mathbb E[x_{n+1}\mid x_n]=(1-\alpha)x_n
\]

for either scheme. For a \(j\)-dimensional standard Gaussian \(g\), radial chi-square moments and rotational invariance give

\[
\mathbb E[(\langle b,g\rangle)^2\|g\|^2]=(j+2)\|b\|^2,
\qquad
\mathbb E[\|g\|^6]=j(j+2)(j+4).
\]

More specifically, independence of \(s,w\) gives \(\mathbb E[(\langle b,w\rangle)^2\|s\|^2]=k\|b\|^2\) and

\[
\mathbb E[\|u\|^4\|s\|^2]=k(d+2)(d+4),\qquad
\mathbb E[\|u\|^4\|w\|^2]=q(d+2)(d+4).
\]

All terms involving the product of the linear residual and the quadratic finite-difference remainder vanish by Gaussian parity. Define \(A_n=\mathbb E\|Px_n\|^2\), \(B_n=\mathbb E\|(I-P)x_n\|^2\), and

\[
s=(1-\alpha)^2,\quad r=1-2\alpha+(q+2)\alpha^2,
\quad C_j=\frac{\tau^2(j+2)(j+4)}4.
\]

A direct expansion of the two updates and the preceding moments gives **exactly at every iteration**

\[
\begin{aligned}
B_{n+1}^{F}&=rB_n^{F}+\alpha^2q C_d,\\
A_{n+1}^{F}&=sA_n^{F}+\alpha^2 k(B_n^{F}+C_d),\\
B_{n+1}^{R}&=rB_n^{R}+\alpha^2q C_q,\\
A_{n+1}^{R}&=sA_n^{R}.
\end{aligned}
\]

Because \(q\ge1\), \(r\ge0\) and \(r<1\) is equivalent to \(0<\alpha<2/(q+2)\); this implies \(s<1\). At \(r=1\), the strictly positive term \(\alpha^2qC_j\) makes \(B_n\) grow linearly. At \(r>1\), the same term causes exponential growth. Hence the open stability interval is necessary and sufficient for mean-square boundedness of all deterministic starts; no finite-iteration experiment enters this argument.

Inside that interval, the recurrences are affine contractions. Their fixed points are

\[
B_\infty^F=\frac{\alpha q C_d}{2-\alpha(q+2)},\qquad
A_\infty^F=\frac{\alpha k(B_\infty^F+C_d)}{2-\alpha},
\]

\[
B_\infty^R=\frac{\alpha q C_q}{2-\alpha(q+2)},\qquad A_\infty^R=0.
\]

Summing the first two entries and substituting \(q=d-k\) yields the claimed expression for \(F_{d,k}\). The other expression is immediate. Since \(d>q\), \(C_d>C_q\) and \(A_\infty^F>0\), strict dominance follows. Dividing the formulas proves the exact ratio; with fixed \(q\), the numerator's factor \(2d-\alpha(d+k)=2(1-\alpha)d+\alpha q\), and the other factors are quadratic in \(d\). This proves the stated cubic asymptotic, completing the proof.

## Verification

The accompanying standalone `check.py` uses exact symbolic Gaussian-Wick polynomial integration to verify all four one-step moment recurrences for three distinct small \((d,k)\) configurations with rational data. It checks the closed-form fixed points and strict gap for every pair \(2\le d\le17\), \(1\le k<d\), at a representative stable step. A separate Monte Carlo diagnostic uses 20,000 independent trajectories over 180 steps for \(d=5\), \(k=3\), \(\alpha=0.19\), \(\tau=0.13\). Formula-predicted second moments are \(0.1910805382\) (full) and \(0.03107419355\) (restricted); a seeded execution gave \(0.1874676646\) and \(0.0308233340\), respectively. Reproduce with `python check.py` and Python packages `numpy`, `sympy`. These finite checks are corroboration; the proof above establishes the universal assertions.

## Relationship to prior work

Ryabchenko, Qian and Mou [1, §3.1, Lemma 3.3 and Appendix C] introduce the one-sided Gaussian control-variate estimator and bound its squared error by a residual-direction term plus a smoothing term of cubic dimension order. Their exact projection benchmark is the origin of \(G_F\). They do not provide the stationary error formulas above or an equal-query complement-probe comparison for this quadratic.

Chayti, Mirrokni and Jaggi [2, §§2–3 and Appendices B–D] study partial-gradient access with a different residual-tracking recursion and central-difference probes. In particular their contraction lemma already contains the standard Gaussian coefficient \(q+2\) in the residual dimension and the associated stepsize interval; **neither this factor nor the idea of using a known gradient component is claimed new here**. Their central differences remove the one-sided quadratic remainder in the present model, but require a different oracle scheme. The new assertion assessed here is the joint exact one-sided finite-\(\tau\) stationary error law and its full-versus-complement probe-support separation.

## Limitations

This is a fixed-stepsize, fixed-projector, exact-reference quadratic statement. Its objective is not globally Lipschitz and therefore lies outside the global-gradient-bound hypothesis in [1]. The restricted estimator is unbiased on this quadratic; for a general nonquadratic objective and finite \(\tau\), it estimates a different smoothed gradient from the full isotropic estimator. If probe energy rather than \(\tau\) is normalized equally, the numerical ratio changes; the theorem makes no optimality claim under such a different normalization. No claim is made about adaptive directional hints, noisy projected references, objective noise, arbitrary anisotropic Hessians, finite-precision arithmetic or central/antithetic finite differences. The existence of an exactly matching result in older or unindexed variance-reduction literature cannot be ruled out solely by the comparisons described.

## References

[1] A. Ryabchenko, J. Qian, W. Mou, *Adaptively Incorporating Directional Hints into Zeroth-Order Optimization*, arXiv:2609.08277v1 (first posted 2026-09-08), https://arxiv.org/html/2609.08277v1 .

[2] E. M. Chayti, A. Mirrokni, M. Jaggi, *Partially Informed Stochastic Optimization via Zeroth-Order Residual Tracking*, arXiv:2610.13871v1 (first posted 2026-10-09), https://arxiv.org/html/2610.13871v1 .
