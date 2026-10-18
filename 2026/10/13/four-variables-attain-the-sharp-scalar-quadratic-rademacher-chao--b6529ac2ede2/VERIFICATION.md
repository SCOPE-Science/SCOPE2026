---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Let u=epsilon_1epsilon_2, v=epsilon_1epsilon_3, w=epsilon_1epsilon_4, independent uniform signs. A scalar quadratic chaos maps to span{u,v,w,uv,uw,vw}; its mean and cubic Walsh coefficient are zero, forcing zero sum of the four values in each parity class uvw=+/-1. Every real zero-sum four-vector satisfies sum|y|>=sqrt(2)*sqrt(sum y^2), equality exactly one positive and one negative nonzero entry. Applying to both classes with exact 8-point normalization gives ||h||_2<=2||h||_1. Equality forces one parity class zero and a signed two-point support in the other; the 12 such pairs match products (epsilon_i+s epsilon_j)(epsilon_k+t epsilon_l). n=3 has sqrt(2), n=2 has 1.

## originality

PASS

Ivanisvili–Tkocz conjecture degree-two sharp constant 2 and exhibit its four-sign product witness but the inspected source does not prove the bound for every real scalar four-variable quadratic or the complete equality orbit; general bounds are nonsharp. The equality classification and sharp finite-dimensional theorem do not follow from a witness. Searches across Walsh and Pełczyński aliases found no covering result; full Oleszkiewicz (1999) historical chapter remains inaccessible, a priority risk.

## value

PASS

Four signs are mathematically motivated as the smallest support realizing the famous conjectured extremizer, not an arbitrary finite slice. Establishing the sharp theorem in that first attainable dimension plus all extremizers and smaller-dimensional strict gaps is a useful geometric boundary case of an open moment-comparison problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
