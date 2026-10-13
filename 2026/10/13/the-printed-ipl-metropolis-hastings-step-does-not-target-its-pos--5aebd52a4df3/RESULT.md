# The printed IPL Metropolis–Hastings step does not target its posterior
## Finding
Consider the Bayesian sampler proposed for the inverse power Lomax stress–strength model. The paper defines the conditional posterior of the common IPL shape parameter \(\nu\) as
\[
\pi_\nu^*(\nu\mid\gamma,\eta,\xi)
\propto
\nu^{n_1+n_2-1}
\exp\!\left[
-\nu\left(
\sum_{i=1}^{n_1}\log x_i+
\sum_{j=1}^{n_2}\log y_j
\right)
\right]
\]
times
\[
\prod_{i=1}^{n_1}
\left(1+\xi^{-1}x_i^{-\nu}\right)^{-(\gamma+1)}
\prod_{j=1}^{n_2}
\left(1+\xi^{-1}y_j^{-\nu}\right)^{-(\eta+1)}.
\]
It similarly defines a nonstandard conditional posterior for \(\xi>0\).

Algorithm 1 then says to use a normal proposal for \(\nu\), but Eq. (3.10) prints the acceptance probability in the form
\[
q_\nu
=
\min\!\left[
1,\,
\frac{
\pi_\nu^*(\nu^*,\operatorname{var}(\widehat\nu))
}{
\pi_\nu^*(\nu^{(i-1)},\operatorname{var}(\widehat\nu))
}
\right].
\]

As printed, this is not a valid Metropolis–Hastings acceptance probability for the conditional posterior just defined.

There are only two natural readings of the displayed notation.

First, if \(\pi_\nu^*\) still denotes the conditional posterior from Eq. (3.5), then the expression is not defined by the source's own formula: the target depends on the current \(\gamma,\eta,\xi\), not on a variance argument.

Second, if the displayed quantities are intended to denote the normal proposal density with variance
\[
s_\nu^2=\operatorname{var}(\widehat\nu),
\]
then the posterior target is entirely absent from the acceptance ratio. For a symmetric random-walk normal proposal,
\[
q(v^*\mid v)=q(v\mid v^*),
\]
so the proposal terms cancel and the correct Metropolis acceptance probability is
\[
\boxed{
\alpha_\nu(v,v^*)
=
\min\!\left\{
1,\,
\frac{
\pi_\nu^*(v^*\mid\gamma,\eta,\xi)
}{
\pi_\nu^*(v\mid\gamma,\eta,\xi)
}
\right\}.
}
\]
A proposal \(v^*\le0\) can simply be rejected after extending the target density by zero outside its positive support.

The same correction is required for the \(\xi\) update:
\[
\boxed{
\alpha_\xi(w,w^*)
=
\min\!\left\{
1,\,
\frac{
\pi_\xi^*(w^*\mid\gamma,\eta,\nu)
}{
\pi_\xi^*(w\mid\gamma,\eta,\nu)
}
\right\}
}
\]
for an untruncated symmetric normal random walk with automatic rejection outside \(w>0\).

If a positively truncated normal proposal is used instead, it is not symmetric; the appropriate Hastings proposal-density ratio must then be retained.

The defect can be stated without relying on notation. Under the proposal-density reading of Eq. (3.10), the printed acceptance probability depends only on the normal random-walk displacement. It is therefore symmetric in the two states. A symmetric proposal combined with a symmetric acceptance function is reversible with respect to Lebesgue measure, not with respect to an arbitrary nonconstant conditional posterior. Hence it cannot target Eq. (3.5).

For a concrete check, take
\[
(\gamma,\eta,\xi)=(1.2,1.8,0.9),
\]
\[
x=(0.7,1.3,2.0),
\qquad
y=(0.8,1.7),
\]
and consider a move
\[
\nu:0.7\longrightarrow1.0.
\]
The conditional-posterior density ratio is
\[
\frac{\pi_\nu^*(1.0\mid1.2,1.8,0.9)}
{\pi_\nu^*(0.7\mid1.2,1.8,0.9)}
=
3.8446793063\ldots,
\]
so the correct random-walk Metropolis acceptance is \(1\).

With proposal variance \(0.04\), a ratio based only on the displacement from the normal proposal gives
\[
\exp\!\left(
-\frac{(1.0-0.7)^2}{2(0.04)}
\right)
=
0.3246524674\ldots.
\]
These are different because one uses the posterior target and the other does not.

Therefore Algorithm 1, as printed, does not define an MCMC kernel having the stated IPL posterior as its invariant distribution. The Bayesian estimates and credible intervals in the article cannot be reproduced from the printed algorithm without repairing this step.

## Assumptions and scope
The finding concerns Algorithm 1 and the conditional posterior formulas printed in Eqs. (3.5)–(3.6).

It does not claim that the mathematical posterior density itself is invalid. The gamma full-conditionals for \(\gamma\) and \(\eta\) are not challenged.

It also does not assert that the authors' unavailable implementation used the defective printed ratio. A private implementation may have used a standard Metropolis–Hastings update despite the displayed algorithm.

The positive-support issue has two valid standard resolutions: use an ordinary symmetric normal proposal on the real line and reject nonpositive proposals, or use a truncated positive proposal together with its noncancelling Hastings correction.

## Proof
Let \(\pi(v)\) denote the conditional target density in Eq. (3.5), extended by zero for \(v\le0\). Let the proposal be
\[
q(v^*\mid v)
=
\phi(v^*;v,s^2),
\]
where \(\phi(\cdot;v,s^2)\) is the normal density with mean \(v\) and variance \(s^2\).

The Metropolis–Hastings acceptance probability for target \(\pi\) is
\[
\alpha(v,v^*)
=
\min\!\left\{
1,\,
\frac{\pi(v^*)q(v\mid v^*)}{\pi(v)q(v^*\mid v)}
\right\}.
\]
Because the random-walk normal proposal is symmetric,
\[
q(v^*\mid v)=q(v\mid v^*),
\]
and so
\[
\alpha(v,v^*)
=
\min\!\left\{
1,\frac{\pi(v^*)}{\pi(v)}
\right\}.
\]
This is the corrected formula above.

Now suppose instead that acceptance is a symmetric function \(a(v,v^*)=a(v^*,v)\) depending only on the proposal displacement, as under the natural proposal-density reading of Eq. (3.10). Since \(q\) is also symmetric,
\[
q(v^*\mid v)a(v,v^*)
=
q(v\mid v^*)a(v^*,v).
\]
Detailed balance with a target \(\pi\) would additionally require
\[
\pi(v)q(v^*\mid v)a(v,v^*)
=
\pi(v^*)q(v\mid v^*)a(v^*,v).
\]
Whenever the transition probability is positive, cancellation gives
\[
\pi(v)=\pi(v^*).
\]
Thus such a kernel can be reversible with respect to \(\pi\) only on regions where \(\pi\) is constant. The conditional posterior in Eq. (3.5) is not constant. Hence the printed proposal-only rule cannot target it.

The alternative literal reading fails earlier: Eq. (3.5) defines
\[
\pi_\nu^*(\nu\mid\gamma,\eta,\xi),
\]
whereas Eq. (3.10) supplies a variance in place of those conditioning variables. No target density with arguments
\[
(\nu,\operatorname{var}(\widehat\nu))
\]
is defined in the article.

## Verification
The bundled checker evaluates the log of Eq. (3.5) up to its normalizing constant for a concrete positive dataset.

It compares the correct target ratio for the move \(0.7\to1.0\) with the displacement-only normal factor at proposal variance \(0.04\).

It also verifies the detailed-balance obstruction numerically: using a symmetric proposal and symmetric displacement-only acceptance, the two probability fluxes differ exactly by the nonunit target-density ratio.

These calculations are finite demonstrations of the general algebraic proof. The proof that the printed rule fails is the detailed-balance argument above, not the numerical example.

## Relationship to prior work
The source explicitly states that Eqs. (3.5) and (3.6) are the conditional posterior densities for \(\nu\) and \(\xi\), observes that they are not standard distributions, and proposes normal Metropolis–Hastings updates inside Gibbs sampling.

The classical Metropolis–Hastings rule requires an acceptance ratio containing the target-density ratio and, for an asymmetric proposal, the reverse-to-forward proposal ratio. For a symmetric random-walk normal proposal the proposal ratio is one, leaving only the target ratio.

Targeted searches using the exact DOI, the inverse power Lomax model name, stress–strength terminology, Algorithm 1, Metropolis–Hastings, acceptance-probability language, and correction terminology did not locate a published correction of Eq. (3.10).

## Limitations
The unavailable code prevents determining which acceptance formula was actually used to produce the article's numerical Bayesian results.

The result establishes invalidity of the printed sampling step; it does not recompute all reported posterior estimates or intervals.

A very recent or unindexed author correction could exist outside the sources examined.

## References
1. A. Mustafa, M. I. Khan, and S. M. Ahmed, “Estimating the stress-strength reliability parameter of the inverse power Lomax distribution,” AIMS Mathematics 10 (2025), 15632–15652. DOI: 10.3934/math.2025700.
2. W. K. Hastings, “Monte Carlo sampling methods using Markov chains and their applications,” Biometrika 57 (1970), 97–109. DOI: 10.1093/biomet/57.1.97.
