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
# Verification

The accompanying `verify.py` was executed from the actual included package directory with the standard Python library only. It passed 510 independently constructed exact rational transition/occupation Green-identity comparisons, covering sizes 4 through 8 and every permitted partial cutoff, and 54 high-precision tests of the strong-reward, finite-cost, full-funding, and logistic-crossover formulas.

Proof-level checks: the birth–death generator is normalized with stay probability \(1-u_j\); the occupation kernel solves the absorbing Dirichlet problem with unit source, and both exponentials \(A=t(\theta-d)\) and \(B=(N-1-t)d\) are derived from the exact ratios. All interior scale terms are separated from the endpoint contributions by a fixed positive exponent in the asserted uniform regime. Funded state \(t\) dominates the cost, with exact prefactor \(\theta N^2/(N-t)\). For \(\theta\le d\), evaluation of the same exact kernel yields the stated finite limits.

Finite calculations cannot establish an infinite-parameter theorem or publication priority. The proof assumes fixed \(N\), strictly partial funding in the exponential regime, state-independent disadvantage and no recurrent mutation. Independent scientific assessment has not been performed.
