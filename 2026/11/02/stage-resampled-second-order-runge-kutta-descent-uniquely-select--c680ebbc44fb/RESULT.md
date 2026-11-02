# Stage-resampled second-order Runge–Kutta descent uniquely selects Heun

## Finding

Fix a real symmetric positive-definite matrix \(H\in\mathbb R^{d\times d}\), \(d\ge1\), and minimize \(F(x)=\tfrac12x^{\mathsf T}Hx\). Suppose each stochastic gradient evaluation returns \(G(x,Y)=YHx\), where the nonnegative scalar multiplier \(Y\) satisfies \(\mathbb EY=1\) and \(\mathbb EY^2=a<\infty\), with \(a\ge1\). Use independent multipliers at the two stages and at successive iterations. For a fixed step \(h>0\) and any real nonzero second-stage weight \(b\), apply the deterministic-order-two explicit Runge–Kutta tableau

\[
 k_1=Y_1Hx,\qquad y=x-\frac{h}{2b}k_1,\qquad
 k_2=Y_2Hy,\qquad x^+=x-h[(1-b)k_1+bk_2].
\]

Define
\[
 C_{a,b}=1+a-2(a-1)b(1-b),\qquad
 Q_b(a,z)=1-2z+C_{a,b}z^2-az^3+\frac{a^2z^4}{4}.
\]

For an orthogonal eigenbasis \(Hu_j=\lambda_j u_j\) and coefficients \(x_0=\sum_jc_ju_j\), the exact moment law is
\[
 \mathbb E\|x_n\|^2=\sum_{j=1}^d c_j^2Q_b(a,h\lambda_j)^n,\qquad n\ge0.
\]

The following **global tableau-optimality identity** holds for every \(h>0\) and every deterministic \(x\):
\[
 \mathbb E\|x^+_b\|^2-\mathbb E\|x^+_{1/2}\|^2
 =2(a-1)(b-\tfrac12)^2h^2\|Hx\|^2.
\]
Thus, if \(a>1\), the equal-weight Heun tableau \(b=1/2\) uniquely minimizes the expected squared error among all explicit two-stage deterministic-order-two Runge–Kutta tableaux, simultaneously for every nonzero initial state, step size, and positive integer horizon. If \(a=1\), every tableau has the same deterministic amplification.

For each \(a\ge1\) and \(b\ne0\), write \(z_b(a)\) for the **unique positive root** of
\[
 a^2z^3-4az^2+4C_{a,b}z-8=0.
\]
The iteration converges exponentially in mean square for every deterministic initial condition **if and only if**
\[
 0<h<\frac{z_b(a)}{\lambda_{\max}(H)}.
\]
At equality, an initial state in the top eigenspace retains constant positive expected squared norm; above it, that expected norm diverges exponentially. In particular, the midpoint tableau \(b=1\) has threshold \(z_1(a)=2/a\), identical to ordinary one-gradient stochastic Euler descent.

For the optimal Heun tableau, let \(z_*(a)=z_{1/2}(a)\). Its sharp cubic is
\[
 a^2z^3-4az^2+(2a+6)z-8=0.
\]
For \(a>1\),
\[
 \frac2a<z_*(a)<\frac4a,
 \qquad \frac{a z_*(a)}2\text{ increases strictly from }1\text{ to }2
 \text{ as }a\text{ increases from }1\text{ to }\infty.
\]
More precisely, \(z_*(a)=4/a-12/a^2+O(a^{-3})\) as \(a\to\infty\). Hence independent-stage Heun can approach twice the normalized mean-square stability step of midpoint or one-gradient stochastic Euler, although it uses two gradient evaluations per step.

The role of stage independence is essential. If one reuses the *same* random multiplier at both stages, then every tableau has amplification \(R_{\mathrm{reuse}}(z,Y)=1-zY+z^2Y^2/2\); for any \(z>0\), its squared amplification has finite expectation **if and only if** \(\mathbb EY^4<\infty\). In contrast, independent stage sampling requires only \(\mathbb EY^2<\infty\). For example, take \(Y=2V/3\), with Pareto law \(\Pr(V>t)=t^{-3}\) for \(t\ge1\). Then \(a=4/3\), \(\mathbb EY^4=\infty\); for scalar \(H=1\) and \(h=1/4\), independently sampled Heun has the exact contraction factor \(355/576\), while every reused-multiplier tableau has infinite one-step squared moment.

## Assumptions and scope

The class includes all standard explicit two-stage Runge–Kutta methods of deterministic order two: the weights are \(b_1=1-b\), \(b_2=b\), the unique nonzero internal coefficient is \(a_{21}=1/(2b)\), and the classical order conditions are \(b_1+b_2=1\), \(b_2a_{21}=1/2\). Every \(b\in\mathbb R\setminus\{0\}\) is allowed on a linear quadratic; in particular, the usual nonnegative-coefficient methods belong to this class. The midpoint method is \(b=1\) and Heun is \(b=1/2\).

Stage multipliers are identically distributed, independent of the past, and independent between stages. The scalar multiplier is shared among coordinates *within* a stage, so it commutes with the fixed matrix \(H\); arbitrary matrix-valued stochastic gradients are not covered. No fourth moment is imposed on independent-stage multipliers. The initial condition is deterministic, and statements about exponential mean-square convergence apply uniformly to all initial conditions rather than to a selected subspace.

## Proof

**Step 1: scalar polynomial.** For an eigenvalue \(\lambda>0\), write \(z=h\lambda\). The two independent draws produce
\[
 R_b(z,Y_1,Y_2)=1-z[(1-b)Y_1+bY_2]+\frac{z^2}{2}Y_1Y_2.
\]
Set \(L=(1-b)Y_1+bY_2\). Independence and the first two moments give
\[
 \mathbb EL=1,\quad \mathbb EL^2=a[(1-b)^2+b^2]+2b(1-b),\quad
 \mathbb E(LY_1Y_2)=a,\quad \mathbb E(Y_1^2Y_2^2)=a^2.
\]
Expansion of \(\mathbb ER_b^2\) yields exactly \(Q_b(a,z)\). In particular,
\[
 Q_b(a,z)-Q_{1/2}(a,z)=2(a-1)(b-\tfrac12)^2z^2.
\]
This proves pointwise uniqueness for \(a>1\); if \(a=1\), the nonnegative multiplier has variance zero and equals one almost surely.

**Step 2: all-dimensional moments.** By the spectral theorem, every update is a polynomial in \(H\), with the scalar random factor \(R_b(h\lambda_j,Y_{n,1},Y_{n,2})\) on eigendirection \(u_j\). Orthogonality removes cross terms in the squared Euclidean norm. Independence across iterations gives exactly \(\mathbb E|\langle x_n,u_j\rangle|^2=c_j^2Q_b(a,h\lambda_j)^n\). Summing gives the full moment formula and its one-step optimality identity. Since \(Q_b(a,z)\ge0\), the pointwise ordering also persists at every positive integer horizon.

**Step 3: uniqueness of every stability boundary.** For \(z>0\),
\[
 Q_b(a,z)-1=\frac z4H_{a,b}(z),\qquad
 H_{a,b}(z)=a^2z^3-4az^2+4C_{a,b}z-8.
\]
Because \(b(1-b)\le1/4\), we have \(C_{a,b}\ge(a+3)/2\ge2\). The derivative \(H'_{a,b}(z)=3a^2z^2-8az+4C_{a,b}\) has minimum \(4C_{a,b}-16/3\ge8/3>0\) on the real line. Moreover, \(H_{a,b}(0)=-8\) and \(H_{a,b}(z)\to+\infty\) as \(z\to+\infty\). Hence it has exactly one positive root, and \(Q_b(a,z)<1\) precisely for \(0<z<z_b(a)\). The top eigenvalue yields the stated full-space criterion, including both boundary and instability cases.

**Step 4: midpoint and the sharp Heun gain.** For midpoint,
\[
 H_{a,1}(z)=(az-2)(az^2-2z+4).
\]
The quadratic factor is strictly positive for \(a\ge1\) and every real \(z\), proving \(z_1(a)=2/a\). For Heun, substitution of \(z=2/a\) and \(z=4/a\) into its cubic gives \(-4+4/a\) and \(24/a\), respectively. If \(a>1\), strict monotonicity yields \(2/a<z_*(a)<4/a\).

Put \(r(a)=az_*(a)\). The Heun root equation becomes
\[
 2r-8+\frac{r(r^2-4r+6)}a=0.
\]
The polynomial \(r(r^2-4r+6)\) and its derivative \(3r^2-8r+6\) are strictly positive for positive \(r\). Implicit differentiation gives \(r'(a)>0\). The bounds give \(2<r(a)<4\) for \(a>1\), and the equation implies \(r(a)\to4\). Expanding the equation at \(r=4\) gives \(r(a)=4-12/a+O(a^{-2})\), hence the stated expansion for \(z_*(a)\). At \(a=1\), \(z_*(1)=2\), so the gain ranges continuously from one toward two.

**Step 5: reused-stage moment obstruction.** With \(Y_1=Y_2=Y\), the deterministic order condition collapses every tableau to \(1-zY+z^2Y^2/2\). Its square is a degree-four polynomial in \(Y\) with positive leading coefficient \(z^4/4\). For fixed \(z>0\), it is asymptotic to \(z^4Y^4/4\) as \(Y\to\infty\). Thus for nonnegative \(Y\), its second moment is finite exactly when the fourth moment of \(Y\) is finite. The independent-stage formula is finite under a second moment, and \(Q_{1/2}(a,z)=1-2z+O(z^2)<1\) for sufficiently small positive \(z\). For the stated Pareto example, \(\mathbb EY=1\), \(\mathbb EY^2=4/3\), \(\mathbb EY^4=\infty\), and direct substitution yields \(Q_{1/2}(4/3,1/4)=355/576\).

## Verification

The standalone file `verify_rk2.py` runs using Python's standard library, without external datasets. It independently enumerates the four stage-outcome combinations of three rational two-point curvature laws and checks the exact squared-amplification polynomial for nine tableau choices and six steps (162 exact-rational cases). It verifies 162 coefficient-gap identities; 63 numerical stability-root comparisons; 108 independently assembled two-dimensional, rotated, symmetric positive-definite matrix cases with rational entries; and the exact Pareto contraction factor. It additionally checks the midpoint factorization, monotone normalized Heun frontier and its large-noise limit. The recorded execution output is:

```text
VERIFY_OK exact_laws=162, variance_identity=162, frontiers=63, matrix_cases=108, shared_vs_independent=1 normalized_horizon_last=3.999988000
```

The infinite moment statement, uniqueness for every dimension, and asymptotic gain are analytic consequences of the proof, not extrapolations from these finite checks. Run `python3 verify_rk2.py` alongside this document.

## Relationship to prior work

Stillfjord and Williamson (2022) propose and analyze stochastic Runge–Kutta–Chebyshev descent, with a shared minibatch across the internal stages and diminishing-step convergence guarantees. Their preprint explicitly states reuse of the same batch in its implementation discussion. It does not supply the independent-stage second-order tableau comparison, the sharp fourth-versus-second-moment separation, or the Heun cubic frontier derived here. Mulayoff and Michaeli (2023) give sharp mean-square stability conditions for ordinary minibatch SGD, which supply a relevant Euler benchmark but do not select among second-order Runge–Kutta tableaux. Earlier stochastic Heun analysis by Saito (2011) studies a Stratonovich stochastic differential equation with a Brownian increment, not repeated stochastic-gradient curvature samples. The classical deterministic Runge–Kutta order conditions and second-order stability polynomial are prior mathematics, not asserted to be new.

The contribution is the exact distribution-free stage-resampled moment identity for all second-order two-stage tableaux, its universal Heun optimizer in any symmetric positive-definite dimension, the sharp stability gain, and the contrast with stage reuse. Published mathematical-record searches and comparisons did not identify a theorem with these combined hypotheses and conclusions; absence of a match does not prove publication priority.

## Limitations

The result concerns scalar multiplicative gradient-oracle noise on a centered, exactly quadratic, symmetric positive-definite objective; it does not cover additive gradient noise, independent per-coordinate random matrices, nonlinear neural-network optimization, or state-dependent noise whose distribution changes between stages. The deterministic order-two designation does not assert stochastic second-order accuracy. The number of gradient evaluations differs between Euler and Heun, so the larger stepsize interval is not by itself a cost-normalized efficiency guarantee. The sharp convergence criterion is in mean square, not a characterization of almost-sure Lyapunov exponents. Specialized earlier work on noisy-stage Runge–Kutta coefficient optimization could affect publication priority and requires independent checking.

## References

1. T. Stillfjord and M. Williamson, *SRKCD: A stabilized Runge–Kutta method for stochastic optimization*, arXiv:2201.12782v1, first posted 2022-01-30. https://arxiv.org/abs/2201.12782
2. R. Mulayoff and T. Michaeli, *Exact Mean Square Linear Stability Analysis for SGD*, arXiv:2306.07850, first posted 2023-06-13; proceedings version 2024. https://arxiv.org/abs/2306.07850
3. Y. Saito, *Mean-square and Asymptotic Stability of the Stochastic Heun Method*, Transactions of the Japan Society for Industrial and Applied Mathematics 21 (2011), 125–134. https://doi.org/10.11540/jsiamt.21.1_125
