# Review

## Correctness

PASS. The proof writes collision probability as
\[
\Pr(A+T=A'+T')
\]
and evaluates it through the three background autocorrelations needed for the
difference \(T-T'\). With pair sum fixed, the two-coin law is affine in the
product \(r=pq\); after substitution, collision probability is a strict
quadratic with second derivative \(4D\). The coefficient satisfies
\[
D=\frac12\sum_k(a_k-2a_{k-1}+a_{k-2})^2>0,
\]
so the projection formula gives the unique feasible optimizer.

The feasible product interval and all two-coin phase thresholds are derived
algebraically. The verifier independently reconstructs the convolution and
checks the identities with exact rational arithmetic.

## Originality

PASS, with a residual older-convolution-literature risk. The full
Hillion--Johnson preprint was inspected through its Rényi/Tsallis section. It
formulates a critical-order Rényi conjecture with predicted threshold \(2\),
but does not solve the fixed-sum order-two optimization.

The full recent sharp-threshold paper was inspected, including its
two-variable transverse construction. It proves that every order above one
fails joint concavity and supplies a local fixed-sum witness, but does not
state the global product projection, the deterministic/unequal/balanced phase
diagram, or the arbitrary-background autocorrelation law.

The full Bernoulli-sum Rényi paper of Madiman--Melbourne--Roberto was also
compared. Its entropy--variance and anti-concentration results do not imply the
fixed-sum pair-transfer identity.

Targeted searches for collision entropy, Rényi order two, fixed Bernoulli
sum, pair balancing, and Poisson-binomial majorization did not locate an
equivalent statement.

## Value

PASS. The generalized Shepp--Olkin problem makes transverse Bernoulli
transfers a central test of entropy geometry. At the collision-entropy order,
the theorem replaces a qualitative failure of concavity with a complete
global optimizer and exact phase transitions. The arbitrary-background
formula also gives a reusable local criterion for whether balancing a selected
pair raises or lowers order-two entropy.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK convolution_checks=22415 energy_checks=12000 quadratic_checks=12000 projection_checks=252000 two_coin_phase_checks=401`.
