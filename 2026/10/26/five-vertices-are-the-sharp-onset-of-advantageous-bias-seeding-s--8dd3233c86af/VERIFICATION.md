---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The reproduction program `verify.py` uses exact symbolic elimination of the absorbing finite Markov chains and rational-polynomial coefficient certificates; no floating-point threshold is used as a proof.

It checks the full three-orbit fixation formulas for \(K_{2,3}\), the factorization and sign of all three pairwise differences, positivity of the common denominator, and the existence of exactly one root above \(1\). It then compares every two-vertex seed pair on one representative of each connected graph isomorphism class of orders three and four. For all competing pairs, each nonzero advantage has a rational expression whose numerator and denominator become coefficientwise nonnegative after replacing \(r\) by \(1+z\), proving the comparison for every \(z>0\). The case of order two is tautological.

An independent all-configuration check solves the 32-state death–birth transition system for \(K_{2,3}\) at rational fitness values \(r=2,3\), verifying agreement with the symmetry-reduced formulas without using the lumped transition matrix.

The program was executed successfully. The proofs cover all positive real fitness for the exact five-vertex comparison, and all advantageous fitness for the sharp minimality result. The checks do not claim an external audit, larger-graph enumeration, or full-text discovery of every related publication.
