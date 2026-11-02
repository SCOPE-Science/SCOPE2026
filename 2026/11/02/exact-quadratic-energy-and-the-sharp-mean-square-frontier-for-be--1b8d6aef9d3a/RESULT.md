# Exact quadratic energy and the sharp mean-square frontier for Bernoulli stale-gradient descent

## Finding
Consider fixed-step gradient descent on the strictly convex scalar quadratic \(f(x)=\lambda x^2/2\), with an independently selected fresh or one-step-stale gradient on each update. Write \(z=\eta\lambda>0\) and let \(D_n\) be i.i.d. Bernoulli variables with \(\Pr(D_n=1)=q\in(0,1)\). The noiseless iteration is
\[
X_{n+1}=X_n-zX_{n-D_n},\qquad n\ge0,
\]
from any deterministic initial pair \((X_{-1},X_0)\in\mathbb R^2\). Then the following are equivalent:

1. \(\mathbb E[X_n^2]\to0\) for every initial pair;
2. convergence is geometrically fast in second moment for every initial pair;
3. \(0<z<z_*(q)\), where
\[
z_*(q)=\frac{4}{1+\sqrt{1+8q}},\qquad qz^2+z<2.
\]

At equality the expected quadratic energy below is conserved and no nonzero initial state is mean-square asymptotically stable. Above this frontier it grows exponentially at even update indices for every nonzero deterministic initial state.

The exact energy, valid on *both* sides of the frontier, is
\[
\mathcal V(x,y)=x^2-\frac{2qz}{1+qz}xy+qz^2y^2.
\]
It is positive definite and satisfies the exact conditional drift identity
\[
\mathbb E[\mathcal V(X_{n+1},X_n)\mid X_n=x,X_{n-1}=y]
-\mathcal V(x,y)=\frac{z(qz^2+z-2)}{1+qz}\,x^2.
\]

If the update also receives i.i.d. independent mean-zero additive errors \(\xi_{n+1}\), with variance \(\sigma^2>0\), then in the stable region the unique limiting second moment is
\[
\boxed{\lim_{n\to\infty}\mathbb E[X_n^2]
=\frac{\sigma^2(1+qz)}{z(2-z-qz^2)}.}
\]
At the critical step, the expected energy increases exactly by \(\sigma^2\) per iteration. Its stationary second-moment formula has a simple pole as the frontier is approached from below:
\[
\lim_{z\uparrow z_*}(z_*-z)\lim_{n\to\infty}\mathbb E[X_n^2]
=\frac{\sigma^2(1+qz_*)}{z_*(1+2qz_*)}.
\]

For every \(q\in(0,1)\) there is a nonempty interval of stepsizes for which the first moment converges to zero but the second moment grows exponentially. In particular \(q=1/2\), \(z=3/2\) gives first-moment characteristic roots with modulus \(\sqrt3/2<1\), while its second moment diverges geometrically.

## Assumptions and scope
All variables are real. The delay decisions \(D_n\) are independent of one another and of the fixed initial pair. The optional errors \(\xi_{n+1}\) are independent across updates, independent of the delay decisions and past states, centered, and have the same finite variance \(\sigma^2\); they need not be Gaussian. The update uses a *fixed* stepsize and a single scalar quadratic objective, with either the current gradient or precisely the preceding gradient. The stability statements for homogeneous updates are for every initial pair, not a generic or almost-everywhere initial state. Mean-square stability refers to the second moment, not pathwise convergence or finite-time consistency of a delayed differential equation.

The endpoint \(q=0\) reduces separately to ordinary explicit Euler, stable precisely for \(0<z<2\); the continuous boundary limit as \(q\downarrow0\) is \(z_*(q)\to2\). The endpoint \(q=1\) reduces to the deterministic two-step lag with threshold \(z_*(1)=1\), but the main assertions are stated for \(0<q<1\).

## Proof
**1. Explicit quadratic identity.** Put \(Y_n=(X_n,X_{n-1})^{\mathsf T}\). For the two delay outcomes,
\[
A_0=\begin{pmatrix}1-z&0\\1&0\end{pmatrix},\qquad
A_1=\begin{pmatrix}1&-z\\1&0\end{pmatrix},\qquad
Y_{n+1}=A_{D_n}Y_n.
\]
Let \(b=qz/(1+qz)\) and \(P=\begin{pmatrix}1&-b\\-b&qz^2\end{pmatrix}\). The leading principal minor is one, and
\[
\det P=qz^2\left(1-\frac{q}{(1+qz)^2}\right)>0
\]
for all indicated \(q,z\); therefore \(P\) is positive definite. Direct matrix multiplication gives the exact identity
\[
(1-q)A_0^{\mathsf T}PA_0+qA_1^{\mathsf T}PA_1-P
=\frac{z(qz^2+z-2)}{1+qz}\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]
The quadratic energy is \(Y_n^{\mathsf T}PY_n\). The identity proves its one-step drift. With independent additive errors the same drift acquires \(+\sigma^2\), because \(P_{11}=1\) and all mixed noise terms vanish conditionally.

**2. Necessity and sufficiency.** Write \(\delta=z(qz^2+z-2)/(1+qz)\). The conditional next-square is
\[
\mathbb E[X_{n+1}^2\mid X_n=x,X_{n-1}=y]
=(1-q)(1-z)^2x^2+q(x-zy)^2.
\]
Consequently the quadratic form given by \(x^2+\mathbb E[X_{n+1}^2\mid x,y]\) is positive definite, since \(qz^2>0\). In finite dimension there is a constant \(\alpha>0\) depending only on \(q,z\) such that this form is at least \(\alpha(x^2+y^2)\). There are also positive \(m,M\) with \(m(x^2+y^2)\le\mathcal V(x,y)\le M(x^2+y^2)\).

Using the drift identity twice gives
\[
\mathbb E\mathcal V(Y_{n+2})-\mathbb E\mathcal V(Y_n)
=\delta\bigl(\mathbb E X_n^2+\mathbb E X_{n+1}^2\bigr).
\]
If \(\delta<0\), this yields a fixed strict contraction of expected energy at every second step and hence geometric mean-square decay. If \(\delta=0\), expected energy is constant and cannot decay from a nonzero initial state. If \(\delta>0\), its expectation increases by a fixed positive fraction at every two steps, hence diverges geometrically from any nonzero initial state. The sign of \(\delta\) is exactly the sign of \(qz^2+z-2\); the positive zero is \(z_*(q)\).

**3. Noisy stationary law.** When \(\delta<0\), geometric mean-square stability of the homogeneous two-state linear recursion implies that the covariance series of independent additive innovations converges and gives a unique stationary covariance. The conditional energy identity, now with \(+\sigma^2\), gives at stationarity
\[
0=\delta\,\mathbb E[X_n^2]+\sigma^2,
\]
which is the stated exact formula. If \(\delta=0\), summing the identity yields \(\mathbb E\mathcal V(Y_n)=\mathbb E\mathcal V(Y_0)+n\sigma^2\). The simple pole follows from factoring \(2-z-qz^2=(z_*-z)[1+q(z_*+z)]\).

**4. A first-moment blind spot.** The mean vector follows
\[
\begin{pmatrix}\mathbb E X_{n+1}\\\mathbb E X_n\end{pmatrix}
=\begin{pmatrix}1-(1-q)z&-qz\\1&0\end{pmatrix}
\begin{pmatrix}\mathbb E X_n\\\mathbb E X_{n-1}\end{pmatrix}.
\]
The strict Jury criteria for its two characteristic roots to lie in the open unit disk reduce to \(qz<1\) and \(z(1-2q)<2\), in addition to \(z>0\). At the mean-square boundary, \(1<z_*(q)<2\) and \(qz_*(q)=2/z_*(q)-1<1\). Both first-moment conditions are therefore strict there. Continuity supplies a nonempty first-moment-stable but mean-square-unstable interval immediately above \(z_*(q)\). For the stated example, the roots of \(\mu^2-\mu/4+3/4\) have modulus \(\sqrt3/2\), while \(qz^2+z=21/8>2\).

## Verification
The standalone file `verify.py` reproduces the matrix Lyapunov identity and its positive principal-minor expression symbolically, derives the exact three-moment recurrence and stationary covariance, and tests the noise-free energy identity using exact rational branch enumeration and independent matrix-recurrence calculations. The program reported 3,510 rational branch/moment tests passed, in addition to the exact symbolic identities. Its finite checks are reproducibility aids, not substitutes for the proof for all real parameters.

Run `python verify.py` with the dependency version specified by `requirements.txt`.

## Relationship to prior work
Mishchenko, Bach, Even and Woodworth (2022) analyze asynchronous stochastic gradient descent with arbitrary delays using virtual iterates and delay-adaptive stepsizes; their theorem does not state the fixed-step Bernoulli one-lag quadratic mean-square boundary or its exact noise floor. Yu, Chen and Poor (2024) study staleness through a continuous-time stochastic delay approximation and characteristic roots; their characteristic-root conclusions concern a different model and are not a discrete Bernoulli second-moment classification. Przybyłowicz, Wu and Xie (2023) analyze finite-horizon randomized evaluation times in Euler schemes for stochastic delay differential equations; their randomization is not the random zero/one gradient lag here. General mean-square criteria for randomly switched linear systems give an implicit lifted-covariance test; the new result is an explicit positive-definite quadratic energy identity yielding the sharp closed-form threshold, exact stationary noise pole, and first/second-moment separation in this natural update model.

## Limitations
The random delay is independent and only zero or one update; no claim is made for longer or Markov-dependent delays, nonquadratic objectives, delay-adaptive learning rates, noncommuting multidimensional Hessians, or practical worker-clock dependencies. The formula concerns stationary second moments under additive update noise, not an invariant-law density, nor a bound for finite physical time. The broader earlier literature on randomly delayed linear difference equations and stochastic switched systems may contain a specialization not located in the comparisons; priority over all such work is not established.

## References
- K. Mishchenko, F. Bach, M. Even, B. Woodworth, *Asynchronous SGD Beats Minibatch SGD Under Arbitrary Delays*, first arXiv submission 15 June 2022, https://arxiv.org/abs/2206.07638.
- S. Yu, W. Chen, H. V. Poor, *Distributed Stochastic Gradient Descent with Staleness: A Stochastic Delay Differential Equation Based Framework*, first arXiv submission 17 June 2024, https://arxiv.org/abs/2406.11159.
- P. Przybyłowicz, Y. Wu, X. Xie, *On approximation of solutions of stochastic delay differential equations via randomized Euler scheme*, first arXiv submission 15 June 2023, https://arxiv.org/abs/2306.08926.
- N. D. Cong, T. S. Doan, S. Siegmund, *On Lyapunov exponents of difference equations with random delay*, Discrete Contin. Dyn. Syst. B 20 (2015), 861–874, https://doi.org/10.3934/dcdsb.2015.20.861 (general random-delay background; full-text priority comparison remains open).
