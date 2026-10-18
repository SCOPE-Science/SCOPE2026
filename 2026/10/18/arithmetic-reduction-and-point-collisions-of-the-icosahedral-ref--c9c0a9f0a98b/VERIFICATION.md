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

Run `python3 verify_icosahedral_reduction.py`. The certificate uses only exact integer-pair arithmetic in `Z[phi]` and the four-element finite field in characteristic two; successful completion prints `VERIFY_OK`. It exhaustively checks every one of 455 unordered line triples, all 105 unordered pairs and their 31 equivalence classes, and every characteristic-two specialization, so no random sample or external package is involved. The theorem for infinitely many odd primes follows mathematically from the determinant absolute norms being powers of two, not from the finite-field enumeration.

Limits: only this explicit integral model; specialization of old point sections is different from flat or Jacobian scheme-length calculation. Published characteristic-zero incidence (15 double/10 triple/6 quintuple) is a reference baseline. Independent scientific audit was not performed.
