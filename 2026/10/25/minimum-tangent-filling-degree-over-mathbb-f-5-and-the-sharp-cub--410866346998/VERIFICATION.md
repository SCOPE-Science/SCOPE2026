---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Enumerated every projective scalar class of nonzero forms over F5 in degrees 1,2,3 (31,3906,2441406). For each, computed all 31 projective zeros and gradients and union of rational tangent lines, independently of repository verifier, obtaining exact maxima 6,21,29 and zero tangent-filling cases. Smooth quartic X^4+X^3Y+Y^3Z-Z^4 has six distinct tangents forming complete six-line pencil through (1:1:0); gradient equations show geometric smoothness and hence irreducibility. Displayed smooth cubic reaches 29, so minimum irreducible tangent-filling degree is exactly four over F5. This is complete finite exhaustive proof only for F5.

## originality

PASS

Asgarli and Ghioca explicitly ask the minimum tangent-filling degree over finite fields (Question 1.5) and note their degree q-1 construction fails at q=5, but that does not exclude other quartics or cubics; the sharp all-cubic obstruction and explicit alternative smooth quartic witness are not given by inspected results. Earlier Asgarli/Ghioca/Yip blocking-curve theorem is about covering with curve points rather than tangent lines.

## value

PASS

An exact finite-field cutoff answering a published minimum-degree question is substantive, with an independently exhaustive 2.44-million-form obstruction and sharp smooth witnesses; no unwarranted generalization to other fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
