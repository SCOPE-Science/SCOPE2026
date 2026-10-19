# Sharp stationary shape ordering for Brownian motion with random partial resetting

## Finding

Let a Brownian particle with diffusion generator \(D\partial_{xx}\), \(D>0\), undergo independent Poisson alarms of rate \(r>0\). At each alarm its position changes from \(x\) to \(Ax\), where fresh independent multipliers \(A\in[0,1]\) have a common law. Put \(B=A^2\) and fix \(m=\mathbb E B\in(0,1)\). There is a unique stationary position distribution \(X\), having the same variance \(2D/[r(1-m)]\) for *every* such law of \(A\).

There is a positive random Brownian operational time \(V_B\) such that
\[
X\ \stackrel{d}{=}\ \sqrt{2D V_B}\,Z,\qquad
V_B\ \stackrel{d}{=}\ E+B V_B',
\]
where \(Z\) is standard normal, \(E\) is exponential of rate \(r\), and the variables on the right are independent. For two squared-multiplier laws with the same mean \(m\), **convex ordering propagates to the entire stationary clock**:
\[
B_1\preceq_{\mathrm{cx}}B_2
\quad\Longrightarrow\quad
V_{B_1}\preceq_{\mathrm{cx}}V_{B_2}.
\]
In particular, writing \(V_{\mathrm{fix}}\) for \(B=m\) almost surely and \(V_{\mathrm{bin}}\) for \(\mathbb P(B=1)=m\), \(\mathbb P(B=0)=1-m\), the **sharp, globally valid bounds** are
\[
V_{\mathrm{fix}}\preceq_{\mathrm{cx}}V_B\preceq_{\mathrm{cx}}V_{\mathrm{bin}},
\quad
V_{\mathrm{fix}}\stackrel d=\sum_{j=0}^{\infty}m^j E_j,
\quad
V_{\mathrm{bin}}\sim\operatorname{Exp}(r(1-m)),
\]
with independent rate-\(r\) exponentials \(E_j\). Both boundary laws are attainable.

Consequences at the *same stationary position variance* include: every even moment of order at least four, the bilateral moment-generating function in the common domain, and the stationary central density \(p_X(0)\) are nondecreasing under the displayed coefficient convex order; the mean absolute displacement \(\mathbb E|X|\) is nonincreasing. This is a comparison of operational clocks and selected shape observables; it does **not** assert convex ordering of the positions themselves or pointwise ordering of spatial tails.

For each integer \(n\ge1\),
\[
\mathbb E X^{2n}=
\frac{(2n)! (D/r)^n}{\prod_{j=1}^n\bigl(1-\mathbb E B^j\bigr)}.
\]
Hence the stationary kurtosis \(K=\mathbb E X^4/(\mathbb E X^2)^2\) has the complete sharp range
\[
\boxed{\quad\frac{6}{1+m}\le K\le6,\quad}
\]
with equality at the lower endpoint **only** for deterministic \(B=m\), and at the upper endpoint **only** for binary \(B\in\{0,1\}\) of mean \(m\). All intermediate kurtoses are attained. For example, at \(m=1/4\), deterministic, uniform \(B\) on \([0,1/2]\), and binary protocols yield respectively \(K=24/5\), \(K=54/11\), and \(K=6\).

For \(0\le |t|<\sqrt{r(1-m)/D}\), the sharp bilateral moment-generating-function envelope is
\[
\prod_{j=0}^{\infty}\frac1{1-(D/r)m^j t^2}
\ \le\ \mathbb E e^{tX}\ \le\
\frac1{1-Dt^2/[r(1-m)]}.
\]
The lower extremal position law is the standard fixed-partial-reset steady state; the upper extremal is the Laplace steady state of full resetting at the thinned rate \(r(1-m)\).

## Assumptions and scope

The particle moves on the whole real line without drift, with nondegenerate Brownian diffusivity \(D>0\). Alarm times are Poisson with rate \(r>0\), and independent multipliers are independently sampled at every alarm and independent of the Brownian path. The multiplier law is supported in \([0,1]\), including possible exact zeros (full resets) and ones (ineffective alarms), with \(0<m=\mathbb E A^2<1\). All distributions and moments described above refer to the unique stationary state. For the convention \(A\in(0,1)\) strictly, the lower extremizer remains admissible, and the upper extremizer is a supremum approached by two-point laws near zero and one.

For integrable real random variables \(U,V\) of the same mean, \(U\preceq_{\mathrm{cx}}V\) means \(\mathbb E f(U)\le\mathbb E f(V)\) for every convex real \(f\) for which the expectations are defined. It suffices to compare \(\mathbb E(U-s)_+\) and \(\mathbb E(V-s)_+\) at every real \(s\).

## Proof

**1. Stationarity and the random clock.** Couple two copies driven by the same Brownian motion, alarms and multipliers. Their displacement difference after time \(t\) is the initial difference multiplied by the product of the multipliers at all alarms. Its expected square is multiplied by \(\exp[-r(1-m)t]\). This contracts squared Wasserstein distance for finite-second-moment initial laws; coupling an arbitrary invariant initial law to the constructed stationary one makes the difference tend to zero in probability, proving uniqueness without a moment assumption. Existence follows by running the process from the remote past, or explicitly by summing independent Brownian increments over the past Poisson intervals. Stationary backward inter-alarm intervals are independent rate-\(r\) exponentials \(E_0,E_1,\dots\); conditioning on multipliers gives the nonnegative clock
\[
V_B=\sum_{j=0}^{\infty}E_j\prod_{i=1}^j B_i,
\quad
\mathbb E V_B=\frac1{r(1-m)}.
\]
The empty product equals one. This sum is finite almost surely because its expected value is finite. Gaussianity conditional on the clock gives \(X\stackrel d=\sqrt{2DV_B}Z\), and hence the asserted position variance.

**2. Monotonicity in convex order.** Fix a coefficient law \(B\) and write \(T_B\mu\) for the law of \(E+BY\), with \(Y\sim\mu\) independent of \(E,B\). For any convex \(f\), the function \(y\mapsto\mathbb E f(E+By)\) is convex. Thus \(T_B\) preserves convex order between laws on \([0,\infty)\). If \(B_1\preceq_{\mathrm{cx}}B_2\), then for each nonnegative \(y\), the function \(b\mapsto\mathbb E f(E+by)\) is convex, so \(T_{B_1}\mu\preceq_{\mathrm{cx}}T_{B_2}\mu\) for any \(\mu\). Start both recursions from the common law of \(E\), apply these two facts inductively, and take limits of the finite past sums. Convergence in \(L^1\) follows by monotone convergence and the geometric mean \(m\); the stop-loss test functions \((v-s)_+\), dominated by an integrable affine expression in \(v\), pass to the limit. Every \(B\in[0,1]\) with mean \(m\) obeys \(m\preceq_{\mathrm{cx}}B\preceq_{\mathrm{cx}}\operatorname{Bernoulli}(m)\): the first inequality is Jensen's and the second is the chord bound \(f(b)\le(1-b)f(0)+bf(1)\). This proves the sharp clock sandwich. For fixed \(B=m\), its clock is the displayed weighted exponential sum. For binary \(B\), an alarm acts as a full reset with probability \(1-m\), so Poisson thinning gives a stationary Brownian age exponential at rate \(r(1-m)\).

**3. Position-shape consequences.** Given \(V=v\), the position is normal with variance \(2Dv\). Thus \(\mathbb E e^{tX}=\mathbb E e^{Dt^2V}\), \(\mathbb E|X|=\sqrt{4D/\pi}\,\mathbb E\sqrt V\), and
\[
p_X(0)=\frac1{\sqrt{4\pi D}}\,\mathbb E[V^{-1/2}].
\]
The central-density expectation is finite since \(V\ge E_0>0\) and an exponential variable has finite negative half-moment. Apply clock convex ordering to the convex functions \(e^{s v}\) and \(v^{-1/2}\), and to the concave function \(\sqrt v\). The sharp moment-generating-function bounds follow by taking the exponential transforms of the two clocks. The upper bound is finite on the stated common domain, justifying these expectations.

**4. Moments, equality, and sharp range.** The stationary generator is \(\mathcal Lf(x)=Df''(x)+r[\mathbb E f(Ax)-f(x)]\). Applied to even monomials it gives, successively,
\[
r(1-\mathbb E B^n)\mathbb E X^{2n}=2n(2n-1)D\,\mathbb E X^{2n-2}.
\]
Finite moments follow directly from Minkowski's inequality for the positive clock series: the \(L^n\) norm of its \(j\)-th term is at most \((n!)^{1/n}r^{-1}(\mathbb E B^n)^{j/n}\), with \(\mathbb E B^n\le m<1\). The stated product formula follows. Write \(s=\mathbb E B^2\); its fourth-to-second moment ratio is \(K=6(1-m)/(1-s)\). Jensen and \(B^2\le B\) give \(m^2\le s\le m\). Equality on the left forces constant \(B=m\); equality on the right forces \(B\in\{0,1\}\) almost surely. The mixture of the deterministic law and the Bernoulli law, both of mean \(m\), realizes every intermediate \(s\) and hence every intermediate kurtosis. These equalities also force the only possible extremizers in the nontrivial second-clock-moment comparison.

## Verification

The accompanying independent Python program evaluates the operational-clock and spatial even moments by *different exact rational recursions*, checks the agreement through order twenty, verifies both sharp moment bounds and the kurtosis identity for five multiplier families, and compares stationary-clock means with seeded finite-past simulations. In the prepared run it passed 172 checks. The full convex-order theorem is established analytically in the proof; finite checks cannot certify its universal quantifiers.

## Relationship to prior work

Dahlenburg, Chechkin, Schumer, and Metzler (2021) introduced random-amplitude resetting and derived general renewal representations, specializing their explicit dependent-amplitude calculations to ballistic motion. Tal-Friedman, Roichman, and Reuveni (2022) proved the fixed-fraction Brownian stationary product formula and its Laplace-to-Gaussian interpolation. Pierce (2022) derived fixed-proportion advection–diffusion stationary moments, and Di Bello and collaborators (2023) developed fixed-factor partial-reset propagators. Olsen (2023) established all-moment formulas for resets to an independently drawn spatial distribution, a different protocol from random multiplication of the current position. Their published formulas provide the motivating model and boundary examples. The present claim is the distribution-free *fixed mean-squared multiplier* comparison, sharp clock convex-order sandwich, and joint stationary-shape envelopes, not a new derivation of the pre-existing fixed-factor propagators or generic resetting constructions.

## Limitations

The theorem concerns independent nonnegative contractions, homogeneous Brownian diffusion, Poisson alarm times and stationary one-point marginals. It does not handle multipliers above one, negative multipliers, state-dependent multipliers, renewal alarms with memory, drift, targets or first-passage optimization. The comparison is in convex order for the latent random Brownian clock; the position distributions need not be convex-ordered. The moment-generating-function envelope is asserted only in the common finite domain specified above. General affine-perpetuity convex-order techniques may implicitly subsume the probabilistic comparison; no independent audit of scientific priority has been performed.

## References

1. M. Dahlenburg, A. V. Chechkin, R. Schumer, and R. Metzler, *Stochastic resetting by a random amplitude*, arXiv:2104.14866v1 (30 April 2021), https://arxiv.org/abs/2104.14866.
2. O. Tal-Friedman, Y. Roichman, and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363v1 (6 May 2022), https://arxiv.org/abs/2205.03363.
3. J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215v1 (14 April 2022), https://arxiv.org/abs/2204.07215.
4. C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski, and R. Metzler, *Time-dependent probability density function for partial resetting dynamics*, arXiv:2305.13722v1 (23 May 2023), https://arxiv.org/abs/2305.13722.
5. K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840v1 (7 October 2023), https://arxiv.org/abs/2310.04840.
