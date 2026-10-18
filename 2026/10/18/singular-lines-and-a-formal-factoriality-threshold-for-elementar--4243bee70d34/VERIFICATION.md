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

## Checks
The `checker.py` script was run with Python and SymPy and returned `VERIFY_OK: symbolic 6- and 7-variable derivative tests; coordinate-line and transverse Hessian identities`.

The exact all-parameter gradient argument uses Newton sums and invertibility of the nonzero-root Vandermonde matrix. Local factoriality for \(n\ge7\) uses the published Samuel--Grothendieck theorem and is not a computer certificate. The rank-four quadratic cone in the completed generic transverse \(n=6\) germ has class group \(\mathbb Z\); this is not a claim about the uncompleted local ring. The Jacobian scheme at vertices, positive characteristic and independent validation remain outside scope.
