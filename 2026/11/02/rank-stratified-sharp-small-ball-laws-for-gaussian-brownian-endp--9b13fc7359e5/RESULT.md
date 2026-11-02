# Rank-stratified sharp small-ball laws for Gaussian Brownian endpoint processes

## Finding

For every positive-semidefinite real \(2\times2\) matrix \(C_\varepsilon\), including matrices depending arbitrarily on \(\varepsilon\), consider the centered Gaussian process
\[
X_{C_\varepsilon}(t)=B^\circ(t)+(1-t)Y_0+tY_1,
\qquad 0\le t\le1,
\]
where \(B^\circ\) is a standard Brownian bridge and \(Y=(Y_0,Y_1)\sim N(0,C_\varepsilon)\) is independent of it. Put
\[
\phi(u)=\begin{cases}\cos(\pi u/2),&|u|<1,\\0,&|u|\ge1,\end{cases}\quad
H(D)=\mathbb E_{Z\sim N(0,D)}[\phi(Z_0)\phi(Z_1)],
\quad A_\varepsilon={\sqrt{2\pi}\over\varepsilon}
\exp\bigl(-\pi^2/(8\varepsilon^2)\bigr).
\]
Every positive-semidefinite \(D\) has \(H(D)>0\), including singular and zero matrices. Uniformly over **all** such choices \(C_\varepsilon\),
\[
\boxed{\displaystyle
\mathbb P\{\|X_{C_\varepsilon}\|_\infty<\varepsilon\}
=A_\varepsilon H(C_\varepsilon/\varepsilon^2)
\bigl(1+O(\varepsilon^2)\bigr).}
\tag{1}
\]
The implicit relative-error bound in (1) is independent of the covariance and its rank. More explicitly, with
\[
R_\varepsilon=\sum_{n=2}^\infty n^2
\exp\bigl(-(n^2-1)\pi^2/(8\varepsilon^2)\bigr),
\]
for all sufficiently small \(\varepsilon>0\) (such that \(R_\varepsilon<1\)), the left side of (1) lies between
\[
(1-R_\varepsilon)A_\varepsilon H(C_\varepsilon/\varepsilon^2)
\quad\text{and}\quad
(1+R_\varepsilon)e^{2\varepsilon^2}
A_\varepsilon H(C_\varepsilon/\varepsilon^2).
\tag{2}
\]

For a **fixed** positive-semidefinite matrix \(C\) of rank \(r\in\{0,1,2\}\), the exponential factor is universal but the polynomial prefactor has order \(\varepsilon^{r-1}\), with the following exact constants:
\[
\mathbb P\{\|X_C\|_\infty<\varepsilon\}\sim
 e^{-\pi^2/(8\varepsilon^2)}
\begin{cases}
\sqrt{2\pi}\,\varepsilon^{-1},&C=0,\\[2mm]
\lambda^{-1/2}I(w),& C=\lambda ww^\top,\ \lambda>0,\ \|w\|_2=1,\\[2mm]
\dfrac{16\varepsilon}{\pi^2\sqrt{2\pi\det C}},& C\text{ positive definite},
\end{cases}
\tag{3}
\]
where
\[
I(w)=\int_{-b}^{b}\phi(w_0u)\phi(w_1u)\,du,
\qquad b=\frac1{\max(|w_0|,|w_1|)}.
\]
Each displayed constant is strictly positive. For example, the rank-one Brownian-motion member has constant \(4/\pi\), and the anti-periodic member has constant \(2\).

There is also a sharp **endpoint crossover**: if \(C_\varepsilon/\varepsilon^2\to D\) as matrices for some finite \(D\succeq0\), then \(H(C_\varepsilon/\varepsilon^2)\to H(D)>0\). Conditional on the rare confinement event, \(Y/\varepsilon\) converges **weakly** to the probability measure on \(\mathbb R^2\) proportional to \(\phi(z_0)\phi(z_1)\,N(0,D)(dz)\). More generally, for **every** \(C_\varepsilon\) the conditional law of \(Y/\varepsilon\) is within \(O(\varepsilon^2)\) total variation, uniformly in the covariance, of the corresponding cosine-weighted Gaussian \(N(0,C_\varepsilon/\varepsilon^2)\). Thus (1) describes moving covariances and rank transitions without separate asymptotic regimes.

## Assumptions and scope

The bridge is standard with \(\operatorname{Cov}(B^\circ(s),B^\circ(t))=\min(s,t)-st\); time length and diffusion coefficient are one. The endpoint vector is independent of the bridge, mean zero, and has covariance \(C_\varepsilon\succeq0\). The matrix may be singular, zero, unbounded, or dependent on the small tolerance \(\varepsilon>0\). The event is confinement over the **whole continuous interval** \([0,1]\), not on a finite grid. This independent endpoint construction unifies the Brownian bridge, Brownian motion, anti-periodic and Slepian-type examples catalogued in Raket's 2026-10-24 *Bestiary of Brownian Processes*. A later endpoint-classification manuscript (2026-10-27) identifies the same construction as the complete ordinary positive Brownian covariance family. No claim is made for projected nonnegative-operator processes with null modes, nonlinear endpoint interpolation, or non-Brownian bridges.

## Proof

**Step 1: conditional bridge survival.** Condition on \(Y=(x,y)\). Then \(X_C\) is the standard Brownian bridge from \(x\) to \(y\) in unit time. If either endpoint lies outside \((-\varepsilon,\varepsilon)\), its strict confinement probability is zero. Otherwise the conditional probability is the ratio of the killed Brownian heat kernel and free heat kernel:
\[
Q_\varepsilon(x,y)=\frac{p_1^{(-\varepsilon,\varepsilon)}(x,y)}{p_1(x,y)},
\qquad p_1(x,y)=\frac1{\sqrt{2\pi}}e^{-(y-x)^2/2}.
\tag{4}
\]
The Dirichlet eigenfunctions on \((-\varepsilon,\varepsilon)\) are \(\varepsilon^{-1/2}\sin[n\pi(x+\varepsilon)/(2\varepsilon)]\), with eigenvalues \(n^2\pi^2/(8\varepsilon^2)\) for the generator \(\tfrac12\partial_x^2\). Therefore
\[
p_1^{(-\varepsilon,\varepsilon)}(x,y)=\frac1\varepsilon\sum_{n=1}^\infty e^{-n^2\pi^2/(8\varepsilon^2)}
\sin\frac{n\pi(x+\varepsilon)}{2\varepsilon}
\sin\frac{n\pi(y+\varepsilon)}{2\varepsilon}.
\tag{5}
\]
This convergent exact spectral identity is valid for every interior pair.

**Step 2: a uniform principal-eigenfunction estimate.** For any integer \(n\ge1\) and \(0\le\theta\le\pi\),
\( |\sin(n\theta)|\le n\sin\theta\). Apply this bound separately to the two sine factors in (5), and factor out its positive first term:
\[
p_1^{(-\varepsilon,\varepsilon)}(x,y)=
\frac{e^{-\pi^2/(8\varepsilon^2)}}{\varepsilon}
\phi(x/\varepsilon)\phi(y/\varepsilon)(1+\delta_\varepsilon(x,y)),
\qquad |\delta_\varepsilon(x,y)|\le R_\varepsilon.
\tag{6}
\]
The error bound is **relative and independent of the endpoints**, even arbitrarily near the absorbing boundary. It is exponentially small, because the first omitted term has exponent \(-3\pi^2/(8\varepsilon^2)\) relative to the leading term. Since \(|x-y|<2\varepsilon\), dividing (6) by (4)'s free kernel changes the multiplier by a factor between \(1\) and \(e^{2\varepsilon^2}\). Integrating against any probability law for the endpoints, including any degenerate Gaussian, establishes (2). As \(R_\varepsilon=o(\varepsilon^k)\) for each fixed \(k>0\), equation (1) follows uniformly. The positivity of \(H(D)\) follows because every centered Gaussian has positive probability in a neighborhood of the origin in its linear support, and both cosines are positive there.

**Step 3: rank constants.** For \(C=0\), \(Y=0\) and \(H(0)=1\). For \(C=\lambda ww^\top\), \(Y=\sqrt\lambda\,wG\) with \(G\sim N(0,1)\). Substitute \(G=\varepsilon u/\sqrt\lambda\) into \(H(C/\varepsilon^2)\), obtaining
\[
H(C/\varepsilon^2)=\frac{\varepsilon}{\sqrt{2\pi\lambda}}
\int_{-b}^b\phi(w_0u)\phi(w_1u)
 e^{-\varepsilon^2u^2/(2\lambda)}\,du
\sim\frac{\varepsilon}{\sqrt{2\pi\lambda}}I(w).
\tag{7}
\]
For \(C\succ0\), its Gaussian density at zero is \((2\pi\sqrt{\det C})^{-1}\), and substitution \(Y=\varepsilon u\), followed by uniform convergence on the compact square, yields
\[
H(C/\varepsilon^2)\sim\frac{\varepsilon^2}{2\pi\sqrt{\det C}}
\left(\int_{-1}^1\cos\frac{\pi u}{2}\,du\right)^2
=\frac{8\varepsilon^2}{\pi^3\sqrt{\det C}}.
\tag{8}
\]
Multiplication by \(A_\varepsilon\) proves (3). For Brownian motion, choose \(\lambda=1\), \(w=(0,1)\), so \(I=4/\pi\). For anti-periodic Brownian motion, choose \(\lambda=1/2\), \(w=(1,-1)/\sqrt2\), which gives \(I=\sqrt2\) and constant \(2\).

**Step 4: conditional endpoint law.** Let \(\mu_\varepsilon\) denote the law of \(Y/\varepsilon\), namely \(N(0,C_\varepsilon/\varepsilon^2)\). Conditional on confinement, (4)–(6) show that the endpoint law has Radon–Nikodym derivative proportional to \(\phi(z_0)\phi(z_1)q_\varepsilon(z)\) relative to \(\mu_\varepsilon\), where \(q_\varepsilon\in[1-R_\varepsilon,(1+R_\varepsilon)e^{2\varepsilon^2}]\) wherever the cosine product is positive. Normalizing against the law with density \(\phi(z_0)\phi(z_1)/H(C_\varepsilon/\varepsilon^2)\), its likelihood ratio lies in the interval given by the ratio of these same endpoints. Its total-variation distance from the cosine-tilted law is thus at most a quantity tending to zero as \(O(\varepsilon^2)\), independent of \(C_\varepsilon\). If \(C_\varepsilon/\varepsilon^2\to D\), Gaussian weak convergence plus bounded continuous cosine weights give weak convergence of the tilted laws. Since the Gaussian laws converge in total variation only when their supports stabilize, **the last convergence is weak in general**, not total variation: for example \(N(0,\varepsilon^2I)\) does not converge in TV to \(\delta_0\). The uniform TV approximation to the *moving* tilted Gaussian remains valid without a rank-stability hypothesis.

## Verification

The accompanying \(\texttt{verify.py}\) uses Python 3's standard library, computes sine-eigenfunction bounds, compares Brownian bridge and Brownian-motion survival to independent classical spectral series, and numerically integrates the rank-one and rank-two principal-eigenfunction approximations. It also checks limiting constants for several covariance shapes. It produces \(2381\) passing deterministic assertions, with output recorded in \(\texttt{verification_output.txt}\). These finite calculations are consistency checks; the all-matrix theorem follows from (4)–(8), and no numerical extrapolation proves an infinite claim.

## Relationship to prior work

Raket's *A Bestiary of Brownian Processes* (first public 2026-10-24) provides the relevant Brownian, anti-periodic, Slepian and Robin/nonlocal examples, boundary kernels, and conditioning perspective that motivate comparing their continuous-path confinement laws. The later 2026-10-27 classification (Theorem 2.1) proves that the independent bridge/Gaussian-endpoint construction exhausts ordinary positive endpoint covariances. Neither inspected work states the uniform sup-norm small-deviation formula (1), its rank-dependent prefactors (3), or the conditional endpoint cosine law. Classical heat-kernel eigenfunction expansions and the familiar small-ball formulas for pinned Brownian bridge and Brownian motion supply indispensable proof components, and these classical special cases are **not** claimed as novel. Li (1999) treats logarithmic small deviations of Gaussian Markov processes under the supremum norm according to its abstract; the present claim supplies exact rank-sensitive prefactors and a uniform law encompassing non-Markov endpoint covariances. Petrova (2019) treats \(L^2\) small balls under finite-dimensional perturbations, a different norm. A survey by Fatalov on small-deviation constants is a possible broader antecedent, but only bibliographic metadata and abstracts were accessible; definitive historical priority remains open.

## Limitations

All asymptotic assertions concern small tolerance \(\varepsilon\to0\) for processes with standard Brownian diffusion on the unit interval. The fixed-covariance rank law (3) must **not** be applied naively when an eigenvalue of \(C_\varepsilon\) vanishes at the same rate as \(\varepsilon^2\); use the uniform crossover formula (1) instead. Rank and covariance can change arbitrarily with tolerance only because the leading coefficient retains the exact function \(H(C_\varepsilon/\varepsilon^2)\). The covariance-dependent tilted Gaussian limit is weak, not TV, when the limit is rank-deficient and the Gaussian supports vary. No priority claim is made for the Brownian killed-kernel method or its classical boundary cases. Publication-level novelty requires broader historical review, especially books and surveys of Gaussian small deviations and non-Markov Gaussian-bridge crossings.

## References

1. Lars Lau Raket, *A Bestiary of Brownian Processes: A Field Guide to Boundary Conditions and Conditioning*, arXiv:2610.33747v1 (first public: 2026-10-24), Sections 3–4 and 9. https://arxiv.org/html/2610.33747v1
2. Lars Lau Raket, *Brownian covariances on an interval: a complete endpoint classification*, arXiv:2610.36762v1 (later, first public: 2026-10-27), Theorem 2.1 and Sections 2–6. https://arxiv.org/html/2610.36762v1
3. Wenbo V. Li, *Small Deviations for Gaussian Markov Processes Under the Sup-Norm*, Journal of Theoretical Probability (1999); abstract/index inspected. https://doi.org/10.1023/A:1021771503265
4. Yulia Petrova, *L2-small ball asymptotics for a family of finite-dimensional perturbations of Gaussian functions*, arXiv:1905.07804 (2019). https://arxiv.org/abs/1905.07804
5. V. R. Fatalov, *Constants in the asymptotics of small deviation probabilities for Gaussian processes and fields*, Russian Mathematical Surveys 58 (2003), 725–772; abstract and bibliographic-level comparison only, https://doi.org/10.1070/RM2003v058n04ABEH000643. Classical Dirichlet heat-kernel eigenfunction expansion on an interval is used directly in the proof.
