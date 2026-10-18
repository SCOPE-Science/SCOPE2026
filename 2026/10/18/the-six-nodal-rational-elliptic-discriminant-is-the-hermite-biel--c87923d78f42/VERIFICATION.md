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

# Reproduction and logical limits

Run the standalone `verify.py` with a Python 3 standard-library interpreter. It checks exact integer determinants over the fifteen matchings and their \(720\) permutations for one generic root configuration; it also tests a collision, a one-matching bielliptic configuration, and a three-quadratic Weierstrass example.

The finite tests check arithmetic and exhibit useful witnesses. They **do not prove** that the locus is irreducible, that a defining polynomial has degree \(15\), or that the moduli map is birational. The mathematical arguments for those universal assertions are Steps 1--4 in `RESULT.md`, which reduce the claims to pair-quadratic linear algebra, the involution criterion and the root-space incidence geometry.

The historical binary-sextic Hermite invariant and the Humbert-\(H_4\) locus are known mathematics; no independent priority determination is claimed.
