---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

With X=T_Lambda T_{Gamma-Omega}^*, duality is exactly X=0, while the published orthogonality sum equals (I-S^{-1})X. Thus the criterion is equivalent to range(X) lying in ker(S-I). If this eigenspace is zero, injectivity gives duality. Conversely, when it is nonzero, the bounded right inverse T_Lambda^* S^{-1} realizes any nonzero operator into that eigenspace as a Bessel-family defect, proving sharp necessity. In the concrete C^2 example, the frame operator is diag(1,2), the orthogonality operator is exactly zero and the reconstruction operator is diag(2,1), so the candidate is not a dual.

## originality

PASS

The 2022 source states an unrestricted iff criterion and its proof reaches (I-S^{-1})X=0 before incorrectly treating I-S^{-1} as invertible for an arbitrary frame operator. The audited result identifies the exact kernel obstruction, proves sufficiency of injectivity, proves necessity by realizing every defect with range in the 1-eigenspace, and supplies a concrete non-Parseval counterexample. No indexed erratum or prior source with this exact correction was located.

## value

PASS

This is a sharp correction to a published iff theorem: it identifies the exact spectral obstruction, proves the corrected boundary in arbitrary Hilbert space and supplies a minimal explicit counterexample. Such a repair is directly useful for future dual-frame arguments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
