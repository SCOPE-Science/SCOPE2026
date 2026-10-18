---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The analytic continuous-allocation proof is in `RESULT.md`. The source's `artifacts/verify.py` checks deterministic positive inputs by sorting \(\rho_j=G_j/a_j\), selecting the first admissible threshold index, reconstructing the unique minimizing delay vector, testing the KKT signs and exact product identity to floating-point tolerance, and checking the factor-two ceiling guarantee. These tests corroborate but cannot prove the general formula.

There need not be a unique eligible **index**: for \(a=(1,1)\), \(G=(1,3)\), \(g=2\), both \(k=1\) and \(k=2\) satisfy the stated inequalities while the optimizer is uniquely \((1,1)\). The repaired result specifies a canonical first eligible index and proves that all eligible indices describe the same minimizer. The verifier uses first crossing and does not establish uniqueness of an arbitrary eligible index.

No computation in this package addresses the full precision-aware objective, analytic-domain restrictions, exact floor-valued query counts, or downstream total circuit cost. Independent and expert attestation channels remain not performed.
