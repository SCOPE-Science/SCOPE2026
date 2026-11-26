---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

# Verification

The analytic proof uses finite character orthogonality, the ordered-difference count, and elementary finite-field facts. The included `verify.py` enumerates ordered differences and Weyl ambiguity coefficients in the four cyclic examples with \(k=3,4,5,6\), using example phases and selected nonuniform weight configurations. It checks the three labeled spectral blocks in those dimensions and reports ordinary (unsquared) full and trace-free singular-value condition numbers. Those runs do not include \(k=2\). In that case the multiset formula in `RESULT.md` combines the last two blocks because \(k-1=1\); for the flat support \(\{0,1\}\subset\mathbb Z_3\) it gives \(3\) once and \(3/4\) eight times.

The finite computations are supporting tests. The universal inequalities, optimizer rigidity, spectral degeneracy at the endpoint, and Singer infinite-family argument rely on the analytic proof. See the comparison of prior results in `RESULT.md` for the mathematical scope of the optimization.
