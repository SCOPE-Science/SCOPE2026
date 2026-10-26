# Reinforcement-monotone imbalance and asymptotically perfect edge anticorrelation

## Finding

Take the path with three vertices and two edges. Each endpoint fires at rate \(\lambda>0\); the middle vertex fires at rate \(\mu>0\). Every firing reinforces exactly one incident edge by one unit; at the middle vertex the probability of choosing an edge is proportional to its current weight raised to \(\alpha\in[0,1)\). Give both edges the same deterministic initial weight \(w>0\). Let \(C_1(t),C_2(t)\) count added reinforcements by time \(t\), excluding the initial weights, and define
\[
\Lambda=2\lambda+\mu,\qquad c=\frac{\mu}{\Lambda},\qquad b=c\alpha.
\]

**Theorem.** Conditional on exactly \(n\) firings, \(\lvert C_1(t)-C_2(t)\rvert\) increases in first-order stochastic order as \(\alpha\) increases, for each integer \(n\ge0\). For \(n\ge2\), its second moment is strictly increasing. For every fixed \(t>0\),
\[
\operatorname{Cov}(C_1(t),C_2(t))=\frac{\Lambda t-\mathbb E[(C_1(t)-C_2(t))^2]}4
\]
is zero at \(\alpha=0\), strictly negative for \(\alpha>0\), and strictly decreasing in \(\alpha\). If \(b\ge1/2\), then
\[
\lim_{t\to\infty}\operatorname{Corr}(C_1(t),C_2(t))=-1.
\]
The latter regime exists in the weakly reinforced range precisely when \(\mu>2\lambda\), and it includes every \(\alpha\in[\Lambda/(2\mu),1)\). For instance, \(\lambda=1\), \(\mu=4\) and \(3/4\le\alpha<1\) suffice.

## Assumptions and scope

The three Poisson clocks and selection marks are independent. They have fixed rates as stated; both starting weights are equal, finite and strictly positive. The theorem addresses event counts, not the initial edge weights, and uses the continuous-time process. The stochastic-order assertion is conditional on the number of rings, while the covariance and correlation statements are unconditional. The perfect-anticorrelation assertion is a sufficient condition only: no converse for \(b<1/2\) is claimed. At finite positive times both marginal variances are positive.

## Proof

**Embedded jump chain.** The total number \(N(t)\) of clock rings is Poisson with mean \(\Lambda t\), independent of the ordered vertex labels and marks. After \(n\) firings write \(D_n=C_1-C_2\) and \(s_n=2w+n\). Conditional on \(D_n=d\), the next increment \(\eta_{n+1}\in\{-1,1\}\) has mean
\[
 m_\alpha(d,n)=c\frac{(s_n+d)^\alpha-(s_n-d)^\alpha}{(s_n+d)^\alpha+(s_n-d)^\alpha}
 =c\tanh\!\left(\alpha\operatorname{arctanh}\frac d{s_n}\right).
\]
Here \(\lvert d\rvert\le n<s_n\). Indeed, each leaf always selects its own edge, and the central clock selects it according to the power-weight rule. The two leaf rates cancel in the mean; the central contribution has weight \(c\).

**Stochastic comparison.** Put \(K_n=\lvert D_n\rvert\). For \(k>0\), its next move is outward to \(k+1\) with probability
\[
 p_{\alpha,n}(k)=\frac12\left[1+c\tanh\!\left(\alpha\operatorname{arctanh}\frac{k}{s_n}\right)\right],
\]
and inward to \(k-1\) otherwise. From zero it moves to one surely. For \(\alpha_1\le\alpha_2\), use the same uniforms to choose outward moves in both chains. When their states agree and are positive, the larger exponent has the larger outward probability. When the two states differ, their integer difference is at least two because both have the parity of \(n\); even opposing nearest-neighbor moves cannot reverse their order. When the smaller state is zero, its next state is one, never exceeding the larger state's next state. Induction gives the pathwise comparison \(K_n^{(\alpha_1)}\le K_n^{(\alpha_2)}\) for every \(n\). For strict exponents, starting at \(K_1=1\), the outward probability at the next step is strictly larger. A positive-probability sequence of subsequent joint outward steps retains a strict gap; hence the second moments are strictly ordered for all \(n\ge2\).

**Poissonized covariance.** Equal initial weights and equal leaf rates give \(\mathbb E(D_n)=0\) at every \(n\), and also \(\operatorname{Cov}(N(t),D_{N(t)})=0\). Since \(C_1=(N+D_N)/2\) and \(C_2=(N-D_N)/2\),
\[
 \operatorname{Var}(C_i)=\frac{\Lambda t+\mathbb E D_{N(t)}^2}4,\quad
 \operatorname{Corr}(C_1,C_2)=\frac{\Lambda t-\mathbb E D_{N(t)}^2}{\Lambda t+\mathbb E D_{N(t)}^2}.
\]
The conditional second-moment recurrence is
\[
 v_{n+1}=v_n+1+2\mathbb E[D_n m_\alpha(D_n,n)],\qquad v_0=0,
\]
where \(v_n=\mathbb E D_n^2\). At zero exponent the increments are fair and \(v_n=n\). At any positive exponent the additional term is nonnegative and strictly positive for \(n\ge1\), so \(v_n>n\) for \(n\ge2\). Poissonization, with \(\Pr(N(t)\ge2)>0\), proves strict negative covariance and its strictly decreasing dependence on reinforcement strength.

**Perfect anticorrelation.** Concavity of \(u\mapsto\tanh u\) on nonnegative arguments and \(0\le\alpha\le1\) give \(\tanh(\alpha u)\ge\alpha\tanh u\). By oddness, for all admissible signed \(d\),
\[
 d\,m_\alpha(d,n)\ge \frac{b d^2}{s_n}.
\]
Therefore
\[
 v_{n+1}\ge\left(1+\frac{2b}{2w+n}\right)v_n+1. \tag{1}
\]
If \(2b=1\), dividing (1) by \(s_{n+1}\) and telescoping shows
\[
 v_n\ge (2w+n)\sum_{j=1}^n\frac1{2w+j}\sim n\log n.
\]
If \(2b>1\), use \(v_1=1\) and retain only the multiplicative terms of (1):
\[
 v_n\ge\prod_{j=1}^{n-1}\left(1+\frac{2b}{2w+j}\right)=\Theta_{w,b}(n^{2b}).
\]
Thus in both cases \(v_n/n\to\infty\). Since \(N(t)/(\Lambda t)\to1\) in probability and the lower bounds hold for all sufficiently large \(n\), conditioning on \(\Lambda t/2\le N(t)\le2\Lambda t\) yields \(\mathbb E v_{N(t)}/(\Lambda t)\to\infty\). Substitute into the exact correlation identity to get the limit \(-1\). This argument needs no central limit theorem and supplies no converse below the stated threshold. \(\square\)

## Verification

The included standard-library Python program `verify.py` evaluates the finite-jump distribution in exact rational arithmetic at the integer exponents zero, one and two, and by numerical state recursion at five additional exponents. It checks symmetry, normalization, the stochastic-order inequalities, moment recurrences and the Poissonized covariance identity. Its recorded run passed 650 assertions. Exponents one and two are **finite-step diagnostics only**; the main theorem is confined to \(0\le\alpha<1\). Finite tests do not establish the theorem's uniform quantifiers or its large-time limit; those follow from the proof above.

## Relationship to prior work

Qin's October 2026 homogenization theorem (arXiv:2610.11780v1) concerns deterministic normalized edge-weight limits for weakly reinforced WARM, including unequal vertex firing rates. In the present symmetric finite path it implies that edge reinforcement fractions tend to equal constants. The theorem here describes a different statistic: the full parameter ordering of the imbalance, the sign and monotonicity of the **unconditional count covariance**, and a regime in which the count correlation tends to \(-1\). The earlier Couzinié–Hirsch study (arXiv:2010.03347v2) treats existence and convergence of edge proportions. General Pólya-urn overdispersion suggests negative conditional covariance with a fixed number of events, but does not alone establish the stated Poissonized stochastic ordering or the positive-leaf-rate perfect-anticorrelation region. No priority claim about the general stochastic-comparison technique is made.

## Limitations

All three firing rates are constant, the two leaf rates and starting edge weights must be equal, and the large-time result assumes weak reinforcement. The regime \(b\ge1/2\) is sufficient for perfect anticorrelation; no assertion about necessity or exact subcritical limiting correlations is established here. The result is not a classification of general graphs or asymmetric initial states. Independent mathematical review and historical-priority validation have not been performed.

## References

1. S. Qin, *Homogenization of weakly reinforced Pólya urns on countable networks*, arXiv:2610.11780v1 (first public 2026-10-08), Theorem 1.1 and §1.2.
2. Y. Couzinié and C. Hirsch, *Weakly reinforced Pólya urns on countable networks*, arXiv:2010.03347v2, §§1–2.
3. General background on classical Pólya overdispersion: the Dirichlet–multinomial distribution (used only for conceptual comparison, not as a theorem input).
