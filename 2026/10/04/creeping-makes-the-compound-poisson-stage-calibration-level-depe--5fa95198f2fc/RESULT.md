# Creeping makes the compound-Poisson stage calibration level-dependent
## Finding
For the constant-temperature development process
\[
X_t=c t+\sum_{j=1}^{N_t}G_j,
\]
with \(c,\lambda,\theta>0\), \(N_t\) a Poisson process of rate \(\lambda\), and independent jumps \(G_j\sim\operatorname{Exp}(\text{scale }\theta)\), the unconditional overshoot at a finite threshold depends on the threshold. If
\[
\tau_x=\inf\{t>0:X_t\ge x\},\qquad O_x=X_{\tau_x}-x,
\]
and \(\kappa=(c+\lambda\theta)/(c\theta)\), then
\[
\mathbb P(O_x=0)=\frac{c}{c+\lambda\theta}+\frac{\lambda\theta}{c+\lambda\theta}e^{-\kappa x},
\]
and
\[
\mathbb E O_x=\frac{\lambda\theta^2}{c+\lambda\theta}\left(1-e^{-\kappa x}\right).
\]
Consequently, for every \(0\le a<b<\infty\),
\[
(c+\lambda\theta)\,\mathbb E(\tau_b-\tau_a)
=(b-a)+\frac{\lambda\theta^2}{c+\lambda\theta}\left(e^{-\kappa a}-e^{-\kappa b}\right)>(b-a).
\]
Thus the finite-boundary calibration identity \(c=(b-a)/\mathbb E(\tau_b-\tau_a)-\lambda\theta\) used in the motivating pest-development model omits a positive level-dependent overshoot correction whenever \(\lambda\theta>0\).

## Assumptions and scope
The result concerns the constant-temperature special case with deterministic positive drift \(c\), compound-Poisson positive jumps of rate \(\lambda\), and exponential jump scale \(\theta\). The thresholds are finite and satisfy \(0\le a<b<\infty\). The claim is about the model's exact first-passage calibration; it does not alter the model outside this special case, and it does not assert that every empirical fit in the paper becomes poor after the correction.

The motivating source conditions on whether passage occurs by drift or by a jump. Conditional on a jump crossing, exponential memorylessness indeed makes the overshoot exponential with mean \(\theta\). The issue is that drift crossing has zero overshoot with positive probability, so the unconditional mean is strictly smaller than \(\theta\) and varies with the level.

## Proof
Let \(q(x)=\mathbb P(O_x=0)\), the probability that level \(x\) is reached continuously by the deterministic drift rather than crossed by a jump. Conditioning on the first jump time and size gives, for \(x>0\),
\[
q(x)=e^{-\lambda x/c}
+\int_0^{x/c}\lambda e^{-\lambda t}
\int_0^{x-ct}\frac{e^{-g/\theta}}{\theta}\,q(x-ct-g)\,dg\,dt.
\]
The first term is the event that no jump occurs before the drift reaches \(x\). In the integral, a first jump of size \(g<x-ct\) leaves a residual distance \(x-ct-g\), and independent increments restart the same problem.

Taking the Laplace transform \(Q(s)=\int_0^\infty e^{-sx}q(x)\,dx\) yields
\[
Q(s)=\frac{c}{c+\lambda\theta}\frac1s
+\frac{\lambda\theta}{c+\lambda\theta}\frac1{s+\kappa},
\qquad
\kappa=\frac{c+\lambda\theta}{c\theta}.
\]
Inverting gives
\[
q(x)=\frac{c}{c+\lambda\theta}
+\frac{\lambda\theta}{c+\lambda\theta}e^{-\kappa x}.
\]
On the complementary event, passage is by a jump. By the memoryless property of the exponential jump law, the conditional overshoot is again exponential with scale \(\theta\), hence
\[
\mathbb E O_x=\theta\bigl(1-q(x)\bigr)
=\frac{\lambda\theta^2}{c+\lambda\theta}\left(1-e^{-\kappa x}\right).
\]

Because all increments are nonnegative and \(c>0\), one has \(\tau_x\le x/c\). Therefore optional stopping applies directly to the integrable martingale
\[
M_t=X_t-(c+\lambda\theta)t.
\]
It follows that
\[
(c+\lambda\theta)\mathbb E\tau_x
=\mathbb E X_{\tau_x}
=x+\mathbb E O_x.
\]
Subtracting this identity at \(a\) from the identity at \(b\) gives the displayed stage-duration formula. Since \(e^{-\kappa a}>e^{-\kappa b}\), its correction term is strictly positive.

## Verification
For the concrete parameters \(c=\lambda=\theta=1\), \(a=1\), and \(b=2\), the exact formula gives
\[
\mathbb E(\tau_2-\tau_1)
=\frac12+\frac14\left(e^{-2}-e^{-4}\right)
\approx 0.5292549,
\]
whereas the uncorrected calibration identity gives \(1/2\). The bundled checker evaluates the closed forms and verifies the exact identity between the martingale balance and the overshoot correction using floating-point evaluation only as a reproducibility check; the proof above is analytic and does not rely on numerical experiments.

## Relationship to prior work
Perçin, Baiocco, Cavina, Pradolesi, and Pasquali derive the constant-temperature calibration by treating the overshoot mean at each stage boundary as \(\theta\), causing those terms to cancel. Their later calibration section uses the resulting relation to fit the combined deterministic and jump development rate to stage-duration data. The correction above keeps their model and first-passage definitions unchanged but distinguishes conditional jump-crossing overshoot from unconditional overshoot.

General fluctuation theory for Lévy processes already treats first-passage overshoots as level-dependent random variables. Coutin and Ngom derive joint first-passage, overshoot, and undershoot laws for Lévy processes including compound-Poisson components; Doney and Kyprianou develop general overshoot and undershoot identities. Those results provide broad context, but the accepted claim here is the explicit creeping probability and resulting correction to this finite-stage biological calibration, not a claim that overshoot theory itself is new. Pasquali's earlier no-regression stage-structured model uses a Gamma process rather than this drift-plus-compound-Poisson mechanism and does not imply the correction.

## Limitations
The closed forms use exponential jump sizes and constant coefficients. Other jump laws generally require a different renewal equation. The analysis establishes a mathematical correction to the finite-boundary calibration formula; it does not re-fit the biological data, quantify downstream parameter changes, or assess the full temperature-dependent model. General Lévy fluctuation literature may contain equivalent special-case transforms, so originality is claimed only for the source-specific exact calibration consequence and its explicit finite-stage form.

## References
1. B. T. Perçin, S. Baiocco, F. Cavina, G. Pradolesi, and S. Pasquali, “An analytical stochastic stage-structured model for pest population dynamics: a case study on Cydia pomonella in Italy,” Journal of Mathematical Biology 93 (2026), article 46. DOI: 10.1007/s00285-026-02461-8. Preprint DOI: 10.21203/rs.3.rs-9204874/v1.
2. L. Coutin and E. H. A. Ngom, “Joint law of the hitting time, overshoot and undershoot for a Lévy process,” arXiv:1603.02506.
3. R. A. Doney and A. E. Kyprianou, “Overshoots and undershoots of Lévy processes,” Annals of Applied Probability 16 (2006), 91–106. DOI: 10.1214/105051605000000647.
4. S. Pasquali, “A stage structured demographic model with ‘no-regression’ growth: The case of constant development rate,” Physica A 581 (2021), 126200. DOI: 10.1016/j.physa.2021.126200.
