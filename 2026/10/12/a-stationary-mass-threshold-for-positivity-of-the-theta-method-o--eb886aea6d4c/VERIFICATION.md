---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For n>=3 and positive cyclic rates, (I-aQ)^(-1) factors through the cyclic weighted shift ED_q, with q_j=a lambda_j/(1+a lambda_j), P=product q_j<1. The inverse is strictly entrywise positive and its jj entry is F_j=(1-q_j)/(1-P). The theta step is (R_a-(1-theta)I)/theta; column sums remain one and only its diagonal may turn negative. The derivative a d log(F_j)/da = -q_j+P/(1-P)*sum_k(1-q_k) is strictly negative via product vs sum on all other states; F_j goes 1 down to pi_j=s_j/S strictly from above. Thus the fastest-rate coordinate gives exactly one crossing for theta<1-pi_min, no crossing for theta>=1-pi_min. At theta=0 the bound is h<=1/lambda_max; theta=1 is positive. The expansion F*=pi_min+K/a+O(a^-2) proves the unique cutoff divergence (theta_c-theta)h_c->K/theta_c. Independent exact SymPy rational inversions for four different cyclic rate lists and multiple rational steps verify diagonal formula, off-diagonal positivity and stochastic sums but do not replace the limit proof.

## originality

PASS

The Cayley identity, resolvent positivity and known reversible-chain Crank-Nicolson diagonal criteria are prior mathematics. The primary issue here is a nonreversible heterogeneous directed n-cycle for arbitrary theta in [0,1], and an exact all-rate stationary-mass threshold with unique finite cutoff and divergence constant; the inspected prior theorem for reversible chains does not imply the nonreversible strict monotonicity or general-theta parameter crossing.

## value

PASS

An exact unconditional-stochasticity frontier depending only on the least stationary mass gives a sharp, usable positivity criterion for a natural nonreversible continuous-time Markov test family. The heterogeneous cutoff and its divergence are not cosmetic epsilon improvements; they distinguish probability preservation from ordinary scalar stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
