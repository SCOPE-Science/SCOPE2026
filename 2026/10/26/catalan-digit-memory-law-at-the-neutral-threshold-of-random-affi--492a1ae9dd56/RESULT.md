# Catalan digit-memory law at the neutral threshold of random affine interval maps

## Finding

For the symmetric expanding/contracting affine iterated function system defined below, the centered leading-base-\(b\) digit observable has an exact stationary temporal covariance law. Write \(C_m=\frac{1}{m+1}\binom{2m}{m}\) for the Catalan numbers and \(\theta=p(1-p)\). For every integer \(m\ge0\),
\[
\operatorname{Cov}(Y_0,Y_{2m})=\sigma_f^2 C_m\theta^m,
\qquad \operatorname{Cov}(Y_0,Y_{2m+1})=0.
\]
For every integer \(N\ge1\), the exact integrated-observable variance is
\[
\operatorname{Var}\left(\sum_{j=0}^{N-1}Y_j\right)
=\sigma_f^2\left[N+2\sum_{m=1}^{\lfloor(N-1)/2\rfloor}(N-2m)C_m\theta^m\right].
\]
Its limiting variance density is
\[
\Gamma(p):=\lim_{N\to\infty}\frac1N\operatorname{Var}\left(\sum_{j=0}^{N-1}Y_j\right)
=\sigma_f^2\left(\frac{2}{\max(p,1-p)}-1\right).
\]
The maximum is uniquely attained at the zero-Lyapunov threshold \(p=1/2\), where \(\Gamma(1/2)=3\sigma_f^2\). At this threshold the covariance decays algebraically, and the finite-length variance obeys the sharper critical law
\[
\operatorname{Cov}(Y_0,Y_{2m})\sim\frac{\sigma_f^2}{\sqrt\pi\,m^{3/2}},
\qquad
\operatorname{Var}\left(\sum_{j=0}^{N-1}Y_j\right)
=3\sigma_f^2N-8\sigma_f^2\sqrt{\frac{2N}{\pi}}+O_f(1).
\]
For every fixed \(p\ne1/2\), with \(s=|2p-1|\), the finite-size variance has instead a finite intercept:
\[
\lim_{N\to\infty}\left[\Gamma(p)N-\operatorname{Var}\left(\sum_{j=0}^{N-1}Y_j\right)\right]
=\frac{4\sigma_f^2(1-s)}{s(1+s)}.
\]
These statements characterize a precisely identifiable temporal signature of the expanding/contracting Lyapunov transition, despite the same uniform stationary one-time law for every parameter.

## Assumptions and scope

Fix any integer \(b\ge2\) and a switching probability \(0<p<1\). Independently at each time step choose the expanding map \(S(x)=bx\pmod{1}\), with probability \(p\), or one of the \(b\) inverse-branch contractions \(R_a(x)=(x+a)/b\), each with probability \((1-p)/b\), for \(a\in\{0,\ldots,b-1\}\). Work on \([0,1)\); the standard terminating base-\(b\) convention is used at points with two expansions. Initialize \(X_0\) independently and uniformly on \([0,1)\). Every \(X_n\) is then uniform. This is the stationary *annealed* law; no quenched assertion is made.

Let \(f:\{0,\ldots,b-1\}\to\mathbb R\) be any nonconstant function. Define \(\mu_f=b^{-1}\sum_{a=0}^{b-1}f(a)\), \(\sigma_f^2=b^{-1}\sum_{a=0}^{b-1}(f(a)-\mu_f)^2>0\), and \(Y_n=f(\lfloor bX_n\rfloor)-\mu_f\). All covariance statements concern this fixed observable at integer times under the described stationary law.

## Proof

**Stationarity and digit orthogonality.** The expanding map preserves Lebesgue measure, and the equally weighted images under all inverse branches sum to Lebesgue measure. Consequently the random system preserves the uniform law. For each integer \(j\ge0\), put \(h_j(x)=f(d_j(x))-\mu_f\), where \(d_j(x)\) is the digit in position \(j+1\) of the base-\(b\) expansion. Under Lebesgue measure the digits are independent and uniform, so
\[
\int_0^1h_j\,dx=0,\qquad
\int_0^1h_jh_k\,dx=\sigma_f^2\mathbf{1}_{\{j=k\}}.
\]

**Exact transfer dynamics.** Let \(P\) denote the observable transition operator:
\[
(Pg)(x)=p\,g(Sx)+\frac{1-p}{b}\sum_{a=0}^{b-1}g(R_a x).
\]
Expanding deletes the first digit and every contraction inserts the chosen symbol. Directly, modulo a Lebesgue-null set,
\[
Ph_0=p h_1,\qquad
Ph_j=p h_{j+1}+(1-p)h_{j-1}\quad(j\ge1).
\]
The inverse-branch contribution at level zero vanishes because the inserted digit is uniformly averaged. Thus \(\int h_0P^nh_0\,dx\) is \(\sigma_f^2\) times the sum of weights of all length-\(n\) walks on the nonnegative integers, starting and ending at zero, with up-step weight \(p\) and down-step weight \(1-p\), and prohibited from crossing below zero. There are no odd-length return walks; each length-\(2m\) return path has exactly \(m\) up-steps and \(m\) down-steps, and the number of these paths is the Catalan number \(C_m\). The Markov property supplies
\[
\mathbb E[Y_0Y_n]=\int_0^1h_0(x)(P^nh_0)(x)\,dx,
\]
which proves the complete covariance formula.

**Variance and maximum.** Summing stationary covariances over all pairs of times yields the stated finite formula. The Catalan generating series satisfies
\[
\sum_{m\ge0}C_m z^m=\frac{2}{1+\sqrt{1-4z}}
\quad (0\le z\le1/4).
\]
It follows that \(\sum_{m\ge0}C_m\theta^m=1/\max(p,1-p)\). The covariance is absolutely summable, including at the critical point, by \(C_m=O(4^m m^{-3/2})\). Dominated convergence applied to the finite variance formula gives \(\Gamma(p)\). Since \(\max(p,1-p)\) is uniquely minimized at \(p=1/2\), the claimed sharp maximum follows. The Lyapunov exponent of the maps is \((2p-1)\log b\), so this is precisely the neutral point.

**Critical and noncritical finite-size terms.** At \(p=1/2\), set \(a_m=C_m4^{-m}\) and \(M=\lfloor(N-1)/2\rfloor\). Because \(\sum_{m\ge1}a_m=1\), direct subtraction from the variance formula gives
\[
\frac{3\sigma_f^2 N-\operatorname{Var}(\sum_{j=0}^{N-1}Y_j)}{\sigma_f^2}
=2N\sum_{m>M}a_m+4\sum_{m=1}^{M}m a_m.
\]
Stirling's formula \(a_m=(\sqrt\pi\,m^{3/2})^{-1}+O(m^{-5/2})\) implies
\[
\sum_{m>M}a_m=\frac{2}{\sqrt{\pi M}}+O(M^{-3/2}),
\qquad\sum_{m=1}^{M}m a_m=\frac{2\sqrt M}{\sqrt\pi}+O(1).
\]
Substituting \(M=N/2+O(1)\) gives the \(8\sqrt{2N/\pi}\) coefficient, with an \(O(1)\) remainder. For \(p\ne1/2\), exponential summability also holds after weighting each covariance by its time lag. The finite-size deficit converges to \(4\sigma_f^2\sum_{m\ge1}m C_m\theta^m\). Differentiating the Catalan generating series yields \(\sum_{m\ge1}m C_m\theta^m=(1-s)/(s(1+s))\) for \(s=\sqrt{1-4\theta}=|2p-1|>0\), proving the intercept formula.

## Verification

The accompanying standalone file `verify.py` uses only Python's standard library and exact integer/rational arithmetic. It directly propagates finite base-\(b\) digit strings under independently selected expansion and uniformly chosen inverse-branch contractions. For four parameter sets, all lag correlations through the specified truncation length match the Catalan prediction exactly. Separate exact checks confirm Catalan convolution and the stationary pair-sum variance identity. The verifier prints the number of assertions on successful completion.

The finite-word computation is independent of the nonnegative-walk representation but is not an infinite proof. That proof is given above; in particular the critical variance asymptotic follows from the analytic Catalan estimates, not extrapolated numerics.

## Relationship to prior work

Homburg and Kalle introduce the general expanding/contracting iterated function system, prove that Lebesgue measure is stationary for the balanced inverse-branch probabilities, and analyze synchronization, intermittent behavior and two-point stationary measures according to the Lyapunov sign. Their 2022 initial manuscript and later published version supply the model and stationary-measure premise. The new statement concerns a one-point trajectory observed at two different times: its first-digit covariance, exact finite-time integrated variance, sharp neutral maximum and distinct critical finite-size correction. Those conclusions are not implications of the published two-point synchronization and stationary marginal statements alone.

The related Pelikan-map literature computes position autocorrelation for a different random model with one contraction \(x\mapsto x/2\), rather than a uniformly random inverse branch. Its stationary law is not uniformly Lebesgue for the full parameter range and its position-correlation formulas do not imply these balanced-digit laws. The Catalan excursion enumeration is elementary once the observable operator's half-line representation has been identified; historical priority is not certified by this observation.

## Limitations

Only equal expansion and inverse-branch bases \(b\), uniform inverse-branch selection, stationary annealed initialization, and observables depending on one leading digit are covered. The findings do not assert a central limit theorem, quenched mixing, uniqueness of stationary distributions, or corresponding formulas for unequal expansion and contraction bases or for nonuniform inverse-branch probabilities. An equivalent result in unindexed or broader literature remains possible, and independent mathematical review has not been undertaken.

## References

1. A. J. Homburg and C. Kalle, *Iterated function systems of affine expanding and contracting maps on the unit interval*, arXiv:2207.09987v1 (first public version July 20, 2022), https://arxiv.org/html/2207.09987v1 ; final journal version, *Advances in Mathematics* 482 (2025), 110605, DOI:10.1016/j.aim.2025.110605.
2. M. Majumdar, S. Ruffo, Y. Sato, C. Beck, and R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269 (2023), https://arxiv.org/abs/2308.09269.
