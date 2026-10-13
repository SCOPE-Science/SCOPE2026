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

# Verification record

The supplied `check_cycles.py` independently enumerates all \(n!\) permutations for every \(n=2,\ldots,7\) under each Ewens concentration \(\theta\in\{1/2,1,2\}\), and tests every integer cutoff \(m\in\{0,\ldots,n-1\}\). All **81 covariance instances** agree exactly, using rational arithmetic and distinct implementations of the permutation law and analytic marking identity. The program also tests finite crossover sign order. Run with `python3 check_cycles.py` (Python standard library only).

Direct analytic checks in `RESULT.md` include strict normalization of the Ewens law, the marked-cycle joint expectation, gamma-ratio domination for cycles with length near \(n\), the endpoint integrability bound, and both parameter-limit dominated-convergence arguments. Numerical values for the continuum roots were separately calculated from the displayed equations and are approximations only. Finite enumeration cannot certify the theorem for arbitrary \(n\), \(\theta\), or infinitely many cutoffs; those assertions depend on the proof. Independent audit has not been performed.
