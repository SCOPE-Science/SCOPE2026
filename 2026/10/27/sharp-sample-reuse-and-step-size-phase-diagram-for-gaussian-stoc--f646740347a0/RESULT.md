# Sharp sample-reuse and step-size phase diagram for Gaussian stochastic extragradient on a bilinear saddle

## Finding

The elementary bilinear saddle \(\min_x\max_y axy\) exhibits an exact transition between instability and mean-square contraction when its two stochastic extragradient calls reuse a controlled fraction of Gaussian samples. This gives an exact cost-versus-correlation benchmark rather than an upper bound.

Set \(D_\rho=a^2+(2\rho-1)v\) and \(H_\rho=a^4+(2+4\rho)a^2v+(1+2\rho^2)v^2\). For every integer \(n\ge0\),

\[
\mathbb E\|z_n\|_2^2=q_\rho(\eta)^n\|z_0\|_2^2,\qquad q_\rho(\eta)=1-\eta^2D_\rho+\eta^4H_\rho.
\]

For any nonzero deterministic initial state, mean-square convergence is equivalent to

\[
D_\rho>0,\qquad 0<\eta^2<\frac{D_\rho}{H_\rho}.
\]

When \(D_\rho\le0\), no positive constant equal stepsize yields mean-square contraction. In particular, at \(\rho=0\) and \(v\ge a^2\) all positive constant steps fail, whereas at \(\rho=1\) sufficiently small positive steps always work. For \(v>a^2\), the exact strict noise-correlation threshold for existence of a stable positive step is \(\rho>(1-a^2/v)/2\), tending to \(1/2\) when \(v/a^2\) diverges.

At any fixed \(\eta>0\), the unique minimizer of the mean-square factor over \(\rho\in[0,1]\) is

\[
\rho_* = \operatorname{clip}_{[0,1]}\!\left(\frac{1/(2\eta^2)-a^2}{v}\right).
\]

Full reuse is optimal when \(\eta^2\le 1/[2(a^2+v)]\); an interior fraction of reuse is optimal when \(1/[2(a^2+v)]<\eta^2<1/(2a^2)\); independent calls are optimal when \(\eta^2\ge1/(2a^2)\). These statements compare the numerical factor, not automatically the existence of convergence at a prescribed large stepsize. At \(a=1\), \(v=1/10\), \(\eta^2=12/25\), the strictly best fraction is \(\rho_*=5/12\), with \(q_{5/12}=26437/31250\), strictly below \(q_0=13231/15625\) and \(q_1=13243/15625\); all three factors are below one.

## Assumptions and scope

Let \(a>0\) and \(J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\). The population operator \(F(z)=aJz\) is the simultaneous gradient and negative-gradient operator for \(\min_x\max_y axy\); it is monotone and has its unique zero at the origin. At each iteration, draw a pair \((W_1,W_2)\) with a bivariate normal law, both components having mean \(a\), marginal variance \(v>0\), and covariance \(\rho v\), \(0\le\rho\le1\). Pairs at distinct iterations are mutually independent and independent of the deterministic initial state. Either oracle returns \(W_iJz\), which is unbiased for \(F(z)\); every realization is a skew-symmetric monotone linear operator. All operations take place in exact real arithmetic. The same positive \(\eta\) is used for both calls:

\[
\widetilde z_n=z_n-\eta W_{1,n}Jz_n,\qquad z_{n+1}=z_n-\eta W_{2,n}J\widetilde z_n.
\]

At \(\rho=1\), the centered Gaussian multipliers coincide almost surely; at \(\rho=0\), they are independent. The result concerns mean-square last-iterate behavior, not almost-sure convergence and not a restricted-gap performance guarantee.

A concrete sampling interpretation is available: construct two minibatches of \(B\ge1\) independent Gaussian coefficient observations, each with mean \(a\) and variance \(\tau^2>0\), sharing exactly \(k\in\{0,\ldots,B\}\) observations and otherwise independent. Take the average in each minibatch and redraw all observations independently at each iteration. Then \(v=\tau^2/B\) and \(\rho=k/B\). A positive stable stepsize exists precisely when

\[
B^2a^2+(2k-B)\tau^2>0,
\]

with the step ceiling above after this substitution. In particular, reusing at least half of the minibatch guarantees the *existence* of a stable step for any finite positive \(a,\tau\), although the permitted step can become arbitrarily small.

## Proof

**First, an exact rotation identity.** Since \(J^T=-J\), \(J^2=-I\), and \(\langle z,Jz\rangle=0\), direct substitution yields

\[
z_{n+1}=\big[(1-\eta^2W_{1,n}W_{2,n})I-\eta W_{2,n}J\big]z_n.
\]

Therefore, for every deterministic pair of sampled coefficients,

\[
\|z_{n+1}\|_2^2=\big[(1-\eta^2W_{1,n}W_{2,n})^2+\eta^2W_{2,n}^2\big]\|z_n\|_2^2.
\]

**Second, fourth moments.** Write \(W_i=a+\xi_i\), where \(\mathbb E\xi_i^2=v\) and \(\mathbb E\xi_1\xi_2=\rho v\). The Gaussian fourth-moment pairing formula gives

\[
\mathbb E[W_1W_2]=a^2+\rho v,\quad
\mathbb E W_2^2=a^2+v,\quad
\mathbb E[W_1^2W_2^2]=a^4+(2+4\rho)a^2v+(1+2\rho^2)v^2.
\]

Taking the expectation of the scalar norm multiplier conditionally on \(z_n\) gives \(\mathbb E[\|z_{n+1}\|_2^2\mid z_n]=q_\rho(\eta)\|z_n\|_2^2\). Independence across iterations and induction prove the displayed exact identity for all \(n\ge0\).

**Third, the sharp stability frontier.** The strictly positive fourth moment \(H_\rho=\mathbb E[W_1^2W_2^2]\) satisfies

\[
q_\rho(\eta)-1=\eta^2(H_\rho\eta^2-D_\rho).
\]

This is negative precisely for the stated strict conditions. At equality, the nonzero initial mean-square error does not vanish. Outside the strict region, it grows or stays constant, proving necessity as well as sufficiency. For any fixed correlation with \(D_\rho>0\), the optimal step satisfies \(\eta^2=D_\rho/(2H_\rho)\) and has exact factor \(1-D_\rho^2/(4H_\rho)\).

**Fourth, optimize sample correlation without altering the stepsize.** Differentiating the polynomial in \(\rho\) gives

\[
\frac{\partial q_\rho}{\partial\rho}=2v\eta^2[-1+2\eta^2(a^2+\rho v)],\qquad
\frac{\partial^2 q_\rho}{\partial\rho^2}=4v^2\eta^4>0.
\]

The unique unconstrained critical point projected onto \([0,1]\) is \(\rho_*\). The two endpoint transition steps are the solutions of \(\rho_*=1\) and \(\rho_*=0\); strict convexity proves the strict interior advantage whenever these inequalities are strict. Substitution of the rational parameter values proves the three rational factors above. Finally, the minibatch formulas follow by counting \(k\) identical shared Gaussian observations in the covariance of two \(B\)-term averages.

## Verification

Execute `python3 verify.py` using the Python standard library. Exact rational checks reconstruct bivariate normal moments from a Gaussian integration-by-parts recurrence rather than assuming the displayed fourth-moment formula. They test the factorization and exact stability condition on an independent rational parameter grid, the strict interior optimum, and finite minibatch overlap identities; a separately seeded Monte Carlo experiment constructs both stochastic calls directly as matrix-vector operations and checks their mean-square amplification. The supplied version passed 539 exact-rational assertions and one independent seeded numerical comparison (empirical amplification about \(0.972236\), theoretical \(0.972350\)). Finite tests do not prove the universal statements; the preceding algebra does.

## Relationship to prior work

Yoon and Loizou (2026) establish structural differences between independent-sample and same-sample stochastic extragradient and analyze high-probability gap estimates and last-iterate failures. The publicly available abstract and a detailed secondary reading were accessible, but the original full article was not available for inspection. This exact correlation-parameter Gaussian mean-square polynomial and its strictly optimal intermediate-reuse regime were not established by those accessible materials. A related specialized calculation in the inaccessible full text cannot be ruled out.

Li and coauthors (2021 preprint; 2022 proceedings) analyze bilinear stochastic extragradient, interpolation, iteration averaging and restarting. Their accessible primary full text, including its algorithm and main theorems, was inspected. It does not supply the present all-correlation Gaussian joint-moment classification, even though the same-sample endpoint is within its general methodological setting. Gorbunov and coauthors (2021 preprint; 2022 proceedings) derive a broad framework covering independent and same-sample SEG and arbitrary within-step samplings; the accessible full primary paper and its sampling assumptions/theorem statements were inspected. Its abstract upper bounds and distinct sampling constructions do not entail a necessary-and-sufficient constant-step stability polynomial for partially overlapping paired Gaussian calls. The derivation uses standard Isserlis/Wick identities, which are not claimed as new.

## Limitations

The noise acts multiplicatively on a single planar skew operator, with joint Gaussian coefficients, independent pairs over iterations, equal predictor/corrector steps, and exact arithmetic. The exact mean-square factor need not imply almost-sure rates; more general stochastic operators, additive noise, non-Gaussian fourth moments, matrix-valued coefficients, nonconstant steps, finite precision, and projection constraints are outside the theorem. For large steps the factor-minimizing correlation need not ensure stability. Full-text access to a highly relevant 2026 article was unavailable, so a specialized earlier result remains a bibliographic risk. The work has not received independent validation.

## References

1. TaeHo Yoon and Nicolas Loizou, *On Same-Sample and Independent-Sample Stochastic Extragradient for Monotone Variational Inequalities*, arXiv:2608.06182v1, first posted 2026-08-06. https://arxiv.org/abs/2608.06182
2. Chris Junchi Li, Yaodong Yu, Nicolas Loizou, Gauthier Gidel, Yi Ma, Nicolas Le Roux, and Michael I. Jordan, *On the Convergence of Stochastic Extragradient for Bilinear Games using Restarted Iteration Averaging*, arXiv:2107.00464; AISTATS 2022, PMLR 151, 9793–9826. https://proceedings.mlr.press/v151/junchi-li22a.html
3. Eduard Gorbunov, Hugo Berard, Gauthier Gidel, and Nicolas Loizou, *Stochastic Extragradient: General Analysis and Improved Rates*, arXiv:2111.08611; AISTATS 2022, PMLR 151, 7865–7901. https://proceedings.mlr.press/v151/gorbunov22b.html
