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

# Verification of maximal-degree Nash-facility theorem

No independent external audit has been performed. The mathematical proof and standalone exact-arithmetic program are provided for reproducibility, not as a claim of external certification.

Run `python3 verify_degree.py` from the folder containing this file. On Python 3 with only its standard library, the verifier constructs 18 different integer profiles (for every \(n\) from 3 through 20), checks that each profile lies in the required open two-cluster region, and tests the exact modular Eisenstein conditions, real-root distinctness, and the two strict logarithmic-derivative signs using `fractions.Fraction`. It additionally checks the displayed four-agent certificate and its exact integer derivative. The package test passed, printing `PASS: 19 independent exact finite witnesses; infinite theorem requires proof`.

Proof checkpoints not dependent on software: (1) all smooth-cell first-order equations have degree at most \(n-1\); (2) strict decrease of the log-welfare derivative makes its sign change sufficient for unique global optimality; (3) every \(n\)-th root of unity modulo \(p\) participates in the congruence \(Y^n-1\); (4) the first lifting derivative is nonzero modulo \(p\); (5) a sufficiently fine fixed-residue rational grid hits arbitrary specified real intervals; (6) the derivative integer polynomial is Eisenstein; and (7) its conjugates are real by Rolle's theorem.

Limits: 19 finite certificates alone cannot prove the all-\(n\) theorem, nor do they establish publication priority. The theoretical proof uses Dirichlet's prime theorem, a classical nonconstructive existence statement for every \(n\). The source's earliest public date is confirmed no later than the June 10, 2021 close of its workshop; the original PDF upload timestamp remains unavailable.
