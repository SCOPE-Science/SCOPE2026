# Identical mean-square transport with opposite fourth-cumulant signs from paired run and rest times

## Finding

An intermittent particle can have **exactly the same mean-square displacement at every lag** in two different models, while the leading long-time fourth cumulant has opposite signs. Both run and rest durations have identical exponential marginal laws; only their **within-cycle dependence** changes.

For each \(\theta\in[0,1]\), the full second-order laws are
\[
\mathbb E[W_0W_s]=\frac{v^2}{2}e^{-|s|},\qquad
\mathbb E[(X_t-X_0)^2]=v^2(t-1+e^{-t}).
\]
The fourth-cumulant rate is
\[
\lim_{t\to\infty}\frac{\kappa_4(X_t-X_0)}{t}
=\frac{v^4}{2}\bigl[\theta(\pi^2+12\zeta(3))-24\bigr].
\]
It has a unique zero at
\[
\theta_*=\frac{24}{\pi^2+12\zeta(3)}=0.9878865662487100\ldots.
\]
Thus the comonotone coupling has rate \(-12v^4\); the countermonotone coupling has rate \(\tfrac12(\pi^2+12\zeta(3)-24)v^4>0\), despite identical second-order transport.

## Assumptions and scope

Let the motion have speed \(v>0\) while active, and speed zero while resting. Independent cycles contain one active run of length \(U_j>0\) with an independent equiprobable sign \(\varepsilon_j\in\{-1,1\}\), followed by one rest of length \(V_j>0\). All cycles and signs are independent across cycle indices, but \(U_j\) and \(V_j\) **need not be independent within a cycle**.

For each cycle independently choose a Bernoulli mixture indicator: with probability \(1-\theta\), set \((U,V)=(-\log Z,-\log Z)\); with probability \(\theta\), set \((U,V)=(-\log Z,-\log(1-Z))\), where \(Z\) is fresh uniform on \((0,1)\). All models have \(U,V\sim\operatorname{Exp}(1)\) separately and mean cycle length \(m=\mathbb E(U+V)=2\). Their joint laws have finite exponential moments in a neighborhood of zero. The cycle-length laws are nonarithmetic.

Construct the two-sided equilibrium renewal process using the length-biased cycle containing time zero, a uniform position within that cycle, and independent surrounding cycles. Write \(W_t\) for instantaneous velocity and \(X_t-X_0=\int_0^t W_s\,ds\). Stationarity is invoked for the exact all-lag covariance; cumulant growth rates also hold under initiation at a fresh cycle boundary.

## Proof

**1. Identical entire velocity autocorrelation and MSD.** If \(s\ge0\) lies in a different active run from time zero, the two independent fair signs make the velocity product have zero mean. If the times lie in the same active run, the product is \(v^2\). Stationary renewal-reward sampling therefore gives
\[
\mathbb E[W_0W_s]=\frac{v^2}{\mathbb E(U+V)}\,\mathbb E[(U-s)_+]
=\frac{v^2}{2}e^{-s}.
\]
Only the marginal law of \(U\) enters: the dependence of the subsequent rest cannot affect this two-time product. The velocity mean is zero. Integrating the covariance twice yields
\[
\operatorname{Var}(X_t-X_0)=2\int_0^t(t-s)\frac{v^2e^{-s}}2\,ds
=v^2(t-1+e^{-t}).
\]
In particular the variance rate is \(v^2\) and the diffusion constant under the convention \(\operatorname{Var}(X_t)\sim2D_{\rm eff}t\) is \(D_{\rm eff}=v^2/2\).

**2. Regenerative cumulant identity.** Put \(T=U+V\). One complete cycle contributes displacement \(R=v\varepsilon U\). The renewal transform of the moment generating function has, near its dominant singularity, a denominator
\[
1-\mathbb E[e^{-sT}\cosh(kvU)].
\]
Its positive real dominant exponent \(\lambda(k)\) is determined for \(k\) near zero by
\[
F(\lambda,k):=\mathbb E[e^{-\lambda T}\cosh(kvU)]=1,\qquad \lambda(0)=0.
\]
Because the cycle lengths are nonarithmetic with exponential moments, the renewal-transform numerator is analytic and nonzero near this simple pole (its value at the origin is \(\mathbb ET=2\)). Standard exponential renewal asymptotics, or analytic inversion of the renewal transform, yields \(\log\mathbb E[e^{k(X_t-X_0)}]=t\lambda(k)+O(1)\), with derivatives through order four near \(k=0\). Boundary pieces of unfinished cycles affect the \(O(1)\) term, not the linear cumulant rates.

Write \(\lambda(k)=Ak^2+Bk^4+O(k^6)\). Expanding \(F=1\) gives
\[
2A=v^2\frac{\mathbb EU^2}{\mathbb ET},\qquad
24B=\frac{v^4}{\mathbb ET}\left[
\mathbb EU^4-6\frac{\mathbb EU^2}{\mathbb ET}\mathbb E(U^2T)
+3\left(\frac{\mathbb EU^2}{\mathbb ET}\right)^2\mathbb ET^2
\right].
\]
Here the second equation is \(\lambda^{(4)}(0)\); it is the claimed fourth-cumulant growth rate. All moments are finite.

**3. Evaluate two extreme dependence laws.** Both have \(\mathbb ET=2\), \(\mathbb EU^2=2\), and \(\mathbb EU^4=24\). For comonotone pairing \(T=2U\), so \(\mathbb E(U^2T)=12\) and \(\mathbb ET^2=8\). Substitution gives \(-12v^4\).

For countermonotone pairing, the elementary beta-integral derivative identities are
\[
\mathbb E(UV)=\int_0^1\log z\log(1-z)\,dz
=2-\zeta(2),
\]
\[
\mathbb E(U^2V)=\int_0^1(-\log z)^2(-\log(1-z))\,dz
=6-2\zeta(2)-2\zeta(3).
\]
Consequently
\[
\mathbb ET^2=8-2\zeta(2),\qquad
\mathbb E(U^2T)=12-2\zeta(2)-2\zeta(3).
\]
Substitution, using \(6\zeta(2)=\pi^2\), gives the rate \(\tfrac12[\pi^2+12\zeta(3)-24]v^4\). It is strictly positive: the elementary bounds \(\pi>157/50\) and \(\zeta(3)>\sum_{j=1}^5j^{-3}\) already imply \(\pi^2+12\zeta(3)>24\).

**4. Exact mixing threshold.** Each cycle independently selects one of the two dependence laws. The quantities \(\mathbb ET\) and \(\mathbb EU^2\) are fixed, while \(\mathbb E(U^2T)\) and \(\mathbb ET^2\) are affine in \(\theta\). Therefore the rate interpolates **linearly** between the two endpoint rates, giving the displayed formula and its unique strict sign reversal. The value at equality is a zero fourth-cumulant *growth rate*, not an assertion that the fourth cumulant vanishes at every finite time.

## Verification

The standalone `CHECK.py` independently expands the implicit renewal equation symbolically, checks the required logarithmic integrals numerically at high precision, validates the threshold with a rational strict-sign certificate, and independently solves both endpoint and mixed-copula implicit renewal equations using beta functions. It checks equality of the second-order coefficient and the distinct fourth-order coefficients, and verifies the exact comonotone closed-form root
\[
\lambda_+(k)=\frac{\sqrt{1+4v^2k^2}-1}{4}.
\]
The checker passed 55 deterministic exact or high-precision assertions on the packaged source. The analytic proof above, rather than those finite numerical checks, establishes the assertion for all \(t\), \(v>0\), and \(\theta\in[0,1]\).

## Relationship to prior work

Datta, Beta and Großmann (first arXiv version 21 June 2024) develop intermittent self-propelled motion with arbitrary run/turn **marginal** waiting-time distributions, concentrating on velocity correlations, MSD, and diffusion. Santra, Olsen and Gupta (first arXiv version 29 August 2024) give a general switching-process transform and fourth-cumulant results for models with separately sampled phase durations, including Poissonian active/passive switching. The same independent-phase products do not represent the explicit within-cycle comonotone/countermonotone couplings here.

Niemann and Kantz (2008) address CTRW multi-point functions including dependent jump/wait times. General renewal-reward and coupled-CTRW transforms underlie the present proof. The specific evaluated statement here is the *exactly indistinguishable entire MSD with a sign-reversing fourth-cumulant family and sharp mixing boundary*; it is not a claim to have invented renewal transforms, coupled CTRWs, or generic higher-cumulant calculations.

## Limitations

The pair correlation concerns signed velocity, with fresh independent unbiased run directions. Other sign-memory rules need not share it. The two interval margins are unit-rate exponentials; rescaling time changes numerical rates accordingly. The result concerns the stationary process for exact all-lag covariance and an asymptotic large-time fourth-cumulant coefficient; it does not classify finite-time excess kurtosis or provide finite-sample identification accuracy. A broad pre-existing CTRW formula could allow independent derivation of this particular counterexample: specialized priority remains open to independent scholarly review.

## References

1. A. Datta, C. Beta and R. Großmann, *The random walk of intermittently self-propelled particles*, arXiv:2406.15277 (first version 21 June 2024), https://arxiv.org/abs/2406.15277.
2. I. Santra, K. S. Olsen and D. Gupta, *Dynamics of switching processes: general results and applications to intermittent active motion*, arXiv:2408.16643 (first version 29 August 2024), https://arxiv.org/abs/2408.16643.
3. M. Niemann and H. Kantz, *Joint probability distributions and multipoint correlations of the continuous-time random walk*, Phys. Rev. E **78**, 051104 (2008), doi:10.1103/PhysRevE.78.051104.
