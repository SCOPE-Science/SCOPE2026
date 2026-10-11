---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The actual RESULT and verifier were inspected. The four allowed length-four paths per index and the five forbidden-face families give five linear equations. Three eliminate the auxiliary coefficients and the remaining equations reduce to the single recurrence alpha_i=-alpha_{i-1}; cyclic closure is exactly r=(-1)^m r. No division is used, so the ring-level R versus R[2] statement is valid. The verifier independently reconstructs these path-boundary matrices for widths 3 through 24 and matches the predicted nullities over characteristics 2,3,5; the finite replay is corroborative only.

## originality

PASS

Fu--Ivanov provide the width-three coefficient-sensitive example, while Burfitt--Cutler give a structurally different family with broader prime sensitivity. The inspected sources do not state or imply the exact cyclic-width all-ring module formula.

## value

PASS

This replaces an isolated coefficient-sensitive example by a natural one-parameter classification and exposes the exact parity mechanism over arbitrary coefficient rings. That is a reusable structural family, not a tiny-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
