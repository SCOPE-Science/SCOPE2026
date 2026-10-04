# Exact Ehrenfest law and linear noise floor for additive-noise signSGD
## Finding

Consider the scalar quadratic
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0,
\]
with stochastic gradient oracle
\[
\widetilde g(x)=\lambda x+\xi,
\qquad
\xi\sim\operatorname{Unif}[-B,B],
\qquad
B>0,
\]
where the noises are iid across iterations. Run constant-step signSGD,
\[
x_{t+1}
=
x_t-\delta\,\operatorname{sign}(\widetilde g(x_t)),
\qquad
\delta>0.
\]

Assume the noise band is commensurate with the signSGD lattice:
\[
M
=
\frac{2B}{\lambda\delta}
\in\mathbb N,
\]
and the initial point lies on the support-aligned lattice
\[
x_0
\in
-\frac{B}{\lambda}
+
\delta\mathbb Z.
\]
The integer \(M\) is exactly the number of signSGD step intervals across the gradient-noise uncertainty band
\[
\left[-\frac{B}{\lambda},\frac{B}{\lambda}\right].
\]

After finitely many deterministic inward steps, define
\[
K_t
=
\frac{x_t+B/\lambda}{\delta}
\in
\{0,1,\ldots,M\}.
\]
Then the recurrent signSGD dynamics are exactly
\[
\mathbb P(K_{t+1}=k-1\mid K_t=k)
=
\frac{k}{M},
\]
\[
\mathbb P(K_{t+1}=k+1\mid K_t=k)
=
\frac{M-k}{M}.
\]
This is the classical \(M\)-ball Ehrenfest urn projected to its Hamming weight.

Consequently, the unique invariant law is
\[
\pi_k
=
2^{-M}\binom{M}{k},
\qquad
k=0,\ldots,M.
\]
The chain is irreducible but has period two. Thus, from a deterministic lattice start, its one-time law does not converge to \(\pi\). Instead, the even and odd subsequences converge to \(\pi\) conditioned on the corresponding parity class.

Under the invariant law,
\[
\mathbb E_\pi[x]=0,
\qquad
\operatorname{Var}_\pi(x)
=
\frac{\delta B}{2\lambda},
\]
and therefore
\[
\mathbb E_\pi[f(x)]
=
\frac{\delta B}{4}.
\]
The constant-step additive-noise loss floor is exactly linear in the step size.

There is also an exact transient second-moment law. Let \(\tau\) be the first time the support-aligned chain enters
\[
\left[-\frac{B}{\lambda},\frac{B}{\lambda}\right],
\]
and put
\[
Y_t=K_t-\frac{M}{2}.
\]
Then for every \(r\ge0\),
\[
\mathbb E[Y_{\tau+r}]
=
\left(1-\frac{2}{M}\right)^rY_\tau,
\]
and
\[
\mathbb E[Y_{\tau+r}^2]
=
\frac{M}{4}
+
\left(1-\frac{4}{M}\right)^r
\left(
Y_\tau^2-\frac{M}{4}
\right).
\]
Hence, for \(M=1\) and for every \(M\ge3\),
\[
\mathbb E[f(x_t)]
\longrightarrow
\frac{\delta B}{4}.
\]
For the exceptional two-ball case \(M=2\), the expected loss can alternate forever between its two parity values, while its Cesàro mean is still
\[
\frac{\delta B}{4}.
\]

The periodicity is not a defect of the invariant law. It is the exact consequence of signSGD moving by one lattice spacing at every iteration.

## Assumptions and scope

The result uses a deterministic scalar quadratic and iid uniform additive gradient noise. Uniform noise is a canonical bounded symmetric unimodal model and satisfies the unbiased bounded-variance oracle conditions used in the defining signSGD analysis.

The commensurability condition
\[
M=\frac{2B}{\lambda\delta}\in\mathbb N
\]
is a support-resolution condition: exactly \(M\) algorithmic steps fit across the uncertainty band. The support-aligned lattice is the natural class on which both noise endpoints are signSGD lattice points. Other lattice offsets still give finite birth-death chains, but their invariant weights are not the simple binomial law asserted here.

The theorem concerns one worker and constant learning rate. Majority voting, momentum, decaying schedules, nonsymmetric noise, and multidimensional coupling are outside the claim.

## Proof

Normalize by the signSGD step. Write
\[
x
=
-\frac{B}{\lambda}
+
\delta k.
\]
Because
\[
\lambda\delta
=
\frac{2B}{M},
\]
the deterministic part of the stochastic gradient is
\[
\lambda x
=
-B+\frac{2Bk}{M}.
\]
For \(0\le k\le M\),
\[
\mathbb P(\widetilde g(x)>0)
=
\mathbb P\left(
\xi>
B-\frac{2Bk}{M}
\right)
=
\frac{k}{M}.
\]
A positive stochastic gradient makes signSGD move down one lattice point, while a negative stochastic gradient makes it move up one. Hence
\[
k\to k-1
\quad\text{with probability}\quad
\frac{k}{M},
\]
and
\[
k\to k+1
\quad\text{with probability}\quad
\frac{M-k}{M}.
\]

If \(k<0\), then even the largest noise value leaves the stochastic gradient negative, so the step is deterministically upward. If \(k>M\), the stochastic gradient is deterministically positive and the step is downward. Therefore every support-aligned initial point enters \(\{0,\ldots,M\}\) in finitely many steps.

For
\[
\pi_k=2^{-M}\binom{M}{k},
\]
detailed balance follows from
\[
\pi_k\frac{M-k}{M}
=
\pi_{k+1}\frac{k+1}{M}.
\]
The finite chain is irreducible, so this invariant law is unique.

Every move changes \(k\) by one, so parity flips at each step and the period is two. The two-step chain restricted to either parity class is finite, irreducible, and aperiodic. Its invariant law is the binomial law conditioned on that parity class. Standard finite-state Markov-chain convergence therefore gives the stated parity-subsequence limits.

Set
\[
Y=K-\frac{M}{2}.
\]
Conditionally on \(Y=y\),
\[
\mathbb E[Y^+\mid Y=y]
=
\left(1-\frac{2}{M}\right)y.
\]
Also,
\[
\mathbb E[(Y^+)^2\mid Y=y]
=
\left(1-\frac{4}{M}\right)y^2+1.
\]
Iterating these scalar affine recurrences yields the exact transient moment formulas.

Under the invariant binomial law,
\[
\operatorname{Var}(K)=\frac{M}{4}.
\]
Since
\[
x=\delta\left(K-\frac{M}{2}\right),
\]
one obtains
\[
\operatorname{Var}_\pi(x)
=
\frac{\delta^2M}{4}
=
\frac{\delta B}{2\lambda}.
\]
Multiplying by \(\lambda/2\) gives
\[
\mathbb E_\pi[f(x)]
=
\frac{\delta B}{4}.
\]

For \(M>2\),
\[
\left|1-\frac{4}{M}\right|<1,
\]
so the last-iterate second moment converges to its invariant value. For \(M=1\), every recurrent state already has
\[
Y^2=\frac14,
\]
so the loss is constant after entrance. For \(M=2\), the multiplier is \(-1\), which gives the exact period-two second-moment obstruction. Cesàro averaging removes that oscillation and recovers the invariant mean.

## Verification

The accompanying `verify.py` constructs the exact transition matrix with rational arithmetic for multiple values of \(M\), verifies detailed balance against the binomial law, checks the conditional first- and second-moment recurrences state by state, and confirms parity-conditioned convergence numerically by exact matrix iteration.

Finite enumeration is not used as an infinite proof. Irreducibility, detailed balance, period two, and the scalar moment recurrences establish the theorem analytically.

## Relationship to prior work

Bernstein et al. introduced signSGD with the constant-magnitude update
\[
x_{t+1}=x_t-\delta\,\operatorname{sign}(\widetilde g_t),
\]
and analyze unbiased bounded-variance stochastic gradients. Their paper also discusses symmetric unimodal gradient noise and includes a constant-learning-rate noisy quadratic experiment. The inspected full text does not derive a stationary law for additive uniform noise.

Balles, Pedregosa, and Le Roux develop the geometry of sign gradient descent through maximum-norm smoothness and deterministic quadratic comparisons. Their analysis explains when sign geometry is favorable but does not study stochastic invariant distributions.

Singh, Mishra, and Raut recently solve an exact stationary law for constant-step signSGD on a quadratic under pure multiplicative noise. Their chain is an infinite two-ladder reflected walk with geometric invariant tails and a period-two obstruction. The same paper discusses additive noise as the boundary where cooldown helps every method, but its additive proposition derives the exact stationary second moment for SGD rather than an additive-noise signSGD invariant law. The present result therefore complements that work in the persistent additive regime: on the support-aligned uniform-noise family, the signSGD chain is finite, its invariant law is binomial rather than geometric, and its exact loss floor scales as
\[
\frac{\delta B}{4},
\]
which is linear rather than quadratic in the constant step.

## Limitations

The exact binomial law requires support-lattice commensurability and alignment. Without that alignment, the additive-uniform signSGD chain remains a finite birth-death process, but the endpoint weights change.

The period-two obstruction means invariant expectations and last-iterate limits must be distinguished. In particular, the \(M=2\) last-iterate second moment does not generally converge.

The result does not compare the communication or oracle complexity of signSGD and ordinary SGD, and it does not claim that uniform noise is a universal model of minibatch gradients.

A mathematically equivalent Ehrenfest identification may exist in generic birth-death-chain literature without signSGD terminology; this remains the principal originality risk.

## References

1. Jeremy Bernstein, Yu-Xiang Wang, Kamyar Azizzadenesheli, and Anima Anandkumar, “signSGD: Compressed Optimisation for Non-Convex Problems,” arXiv:1802.04434v1, 2018.
2. Lukas Balles, Fabian Pedregosa, and Nicolas Le Roux, “The Geometry of Sign Gradient Descent,” arXiv:2002.08056v1, 2020.
3. Subham Singh, Ashutosh Mishra, and Subha Raut, “Same Loss, Same Noise, Opposite Schedules: Noise Structure and Optimizer Normalization Jointly Determine Whether Learning-Rate Cooldown Helps,” arXiv:2607.12360v1, 2026.
