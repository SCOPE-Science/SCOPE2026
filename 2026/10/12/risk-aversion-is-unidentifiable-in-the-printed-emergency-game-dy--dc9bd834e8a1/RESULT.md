# Risk aversion is unidentifiable in the printed emergency-game dynamics
## Finding
Su and Long introduce a mean–variance media utility
\[
U_m=\mathbb E(\pi_m)-\lambda\operatorname{Var}(\pi_m)
\]
with risk-preference coefficient \(\lambda\) and study the effects of risk attitude in Figures 6–7. The risk parameter survives in their intermediate risk-aware media equation (18), but **disappears entirely** from the final governing equations (19)–(24) and the discrete numerical formulas (42)–(44).

For fixed remaining parameters and initial conditions, each of those published post-simplification evolution laws is exactly the same for all values of \(\lambda\). Every well-posed solution law and every value produced by the displayed numerical update formulas is therefore insensitive to that parameter. Hence its value is not identifiable from any finite collection of ideal observations, or even the entire noiseless evolution or finite-time stochastic path law.

The parameter is not genuinely redundant in the stated payoff table. On the admissible face \(y=0\) the correct two-action mean–variance replicator has the explicit positive response
\[
\frac{\partial\dot z_{\rm util}}{\partial\lambda}
=x(1-x)z(1-z)^3(F_m-F'_m)^2.
\]
For the source's fine values and the simple interior media/government state \(x=z=1/2\), this response is exactly \(729/6400\), in sharp contrast to the zero sensitivity of its final evolution equations.

## Assumptions and scope
The paper defines \(x,y,z\in[0,1]\) as frequencies of strong government supervision, active disaster-victim response, and accurate media reporting. The risk-aversion coefficient \(\lambda\in\mathbb R\) enters Equation (3) as a multiplier of payoff variance; all other parameters, initial conditions, subsidy functions, and any driving Brownian paths or numerical random increments are held fixed when \(\lambda\) varies.

The first conclusion compares the formulas **as printed**. Deterministic path equality is asserted on intervals with uniqueness, and stochastic path-law equality is asserted only for a consistent, well-posed interpretation of the source's noise specification, up to any domain-exit or explosion stopping time. The result does not assume that the printed stochastic formulas yield globally well-posed strategy frequencies. Discrete-map equality is unconditional for each pair of runs with identical inputs and noise increments for which the update formulas are defined.

The contrasting positive-sensitivity calculation uses the source's original payoff definitions and standard binary replicator formula, not an interpretation of the final simplified equations as a valid replicator. The boundary face \(y=0\) is used to make the payoff variance exact and independent of subsidy functions.

## Proof
Write the vector of post-simplification drifts as
\[
F=(F_x,F_y,F_z)
\]
from Equations (19)–(21). Their displayed terms contain government benefits and costs, fines, subsidies, reporting gains, \(x,y,z\), but **no** \(\lambda\). Equations (22)–(24) repeat the same \(\lambda\)-free drifts and specify noise terms with no \(\lambda\). Their Milstein-type recurrences (42)–(44) likewise depend on the same parameters and noise increments but never on \(\lambda\).

Consequently, for any values \(\lambda_1,\lambda_2\), the deterministic vector fields are literally identical, not merely equivalent by a change of variables. Uniqueness of the local initial-value problem yields
\[
X_{\lambda_1}(t)=X_{\lambda_2}(t)
\]
for their shared interval of definition. If the source's stochastic terms are interpreted so that pathwise uniqueness holds, coupling the two copies with identical noise gives equal stopped trajectories; if one assumes only uniqueness in law, the two parameter values specify the same martingale problem and thus the same stopped law. Finally, induction over the displayed updates (42)–(44), with identical initial states and random increments, gives the same numerical iterates for all \(\lambda\).

Thus any measurable statistic of such paths or iterates has the same distribution for all \(\lambda\). A statistical model whose distributions are constant in a parameter cannot identify that parameter. If a dominated differentiable likelihood exists, its derivative with respect to \(\lambda\) is zero, and the associated Fisher information is zero. This is an exact observational-equivalence statement, not a claim of low finite-sample estimation accuracy.

It remains to verify that the payoff prescription itself *would* depend on \(\lambda\). Fix \(y=0\). Table 2 and the paper's Equations (12)–(15) give the media payoffs: reporting accurately gives \(-C_m\), whereas reporting ambiguously gives
\[
R_m-(1-z)F_m
\]
if the government supervises strongly and
\[
R_m-(1-z)F'_m
\]
if it supervises weakly. The respective probabilities are \(x\) and \(1-x\). Writing \(\overline U_f\) and \(V_f\) for the mean and variance of the latter payoff, direct two-point calculation gives
\[
\overline U_f=R_m-(1-z)[xF_m+(1-x)F'_m],
\]
\[
V_f=x(1-x)(1-z)^2(F_m-F'_m)^2.
\]
The truthful payoff is constant at \(y=0\), so its variance is zero. The mean–variance utilities therefore differ by
\[
U_t^{\lambda}-U_f^{\lambda}
=-C_m-\overline U_f+\lambda V_f.
\]
For two strategies the elementary replicator identity is
\[
\dot z_{\rm util}=z(1-z)(U_t^{\lambda}-U_f^{\lambda}).
\]
Differentiating exactly with respect to \(\lambda\) proves
\[
\frac{\partial\dot z_{\rm util}}{\partial\lambda}
=x(1-x)z(1-z)^3(F_m-F'_m)^2.
\]
For \(0<x,z<1\) and unequal fines it is strictly positive.

Using Table 3's values \(F_m=7/2\) and \(F'_m=4/5\), together with \(x=z=1/2\), one obtains
\[
F_m-F'_m=\frac{27}{10},\qquad
\frac{\partial\dot z_{\rm util}}{\partial\lambda}
=\frac{1}{2}\frac{1}{2}\frac{1}{2}\left(\frac12\right)^3\left(\frac{27}{10}\right)^2
=\frac{729}{6400}.
\]
In contrast, the corresponding \(\lambda\) term inside the bracket in the source's intermediate Equation (18) is
\[
\lambda(1-x)(x+y-2xy)(1-z)^2(F_m-F'_m)^2;
\]
at \(y=0\) the equation multiplies this bracket by \(z\), giving the different but still strictly positive coefficient
\[
\frac{729}{3200}.
\]
The printed final equations and recurrences give zero. Thus the disappearance is not a valid payoff-level cancellation; the risk information is removed in passing from Equation (18) to (19)–(21), before writing the stochastic and numerical models.

## Verification
The bundled `verification/verify.py` uses exact rational arithmetic and symbolic differentiation to reconstruct the two-outcome payoff variance and both risk derivatives. It confirms the exact values \(729/6400\) for the payoff-consistent binary replicator and \(729/3200\) for the coefficient in the source's intermediate Equation (18). It also constructs an explicit \(\lambda\)-free representative of the printed final media drift for the \(y=0\) face and checks that its derivative vanishes identically.

The universal observational-equivalence conclusion is proved by inspection of the complete displayed governing and numerical equations, coupled with ordinary uniqueness/induction. No finite experiment is used as an infinite-time proof. No unprinted implementation is assumed.

## Relationship to prior work
The motivating paper explicitly presents the mean–variance risk parameter in Equation (3), derives a risk-bearing Equation (18), and claims risk-dependent evolutionary trajectories in Figures 6–7 and Section 4.2. Its subsequent printed stochastic and numerical evolution laws instead do not contain that parameter. The discrepancy is a **source-specific structural nonidentifiability** of the displayed model, not a claim that risk cannot affect evolutionary games in general.

Wang, Su, Wang and Plotkin (2024) develop a distinct evolutionary model in which risk preference affects expected imitation utility. Song (2026) studies disinformation governance with loss-sensitive evolutionary incentives. These primary works motivate retaining risk parameters inside strategy-update laws; neither covers the mismatch between the successive equations of the Su–Long source.

A separate analysis of this same source observes that removing complement-frequency factors destroys probability-cube invariance. That boundary-dynamics issue does not imply the present finding, which concerns the \(\lambda\)-sensitivity and identifiability of the stated stochastic and numerical dynamics; neither result is used as a substitute for the other.

## Limitations
This theorem concerns the *printed* equations and displayed recurrences. It does not establish which equations were used to create the paper's figures, nor that its numerical output is false. If the underlying implementation in fact used a risk-bearing equation such as (18), the zero-sensitivity result would not describe that implementation.

The paper's printed stochastic coefficients have additional interpretation issues; no general global solution or invariant probability cube is claimed here. Local law equality holds to a common stopping time whenever the stochastic problem is defined. Stationary-distribution claims are not made.

The source's risk-bearing Equation (18) itself differs from the fully payoff-consistent binary replicator by a complement factor; this is why two distinct, explicitly identified nonzero sensitivities are reported. The present result is the stronger contrast that the final governing model has sensitivity **zero**, not that either nonzero formula is an exact representation of the final model.

## References
1. J. Su and J. Long, “Tripartite stochastic evolutionary game and its evolutionary stability under emergencies,” *Journal of Dynamics and Games* (early access 2026), DOI: 10.3934/jdg.2026051.
2. G. Wang, Q. Su, L. Wang and J. B. Plotkin, “The evolution of social behaviors and risk preferences in settings with uncertainty,” *Proceedings of the National Academy of Sciences* 121 (2024), DOI: 10.1073/pnas.2406993121.
3. X. Song, “A prospect-theoretic evolutionary game approach for disinformation governance in social-media ecosystems,” *Scientific Reports* 16 (2026), 25347, DOI: 10.1038/s41598-026-53697-9.
