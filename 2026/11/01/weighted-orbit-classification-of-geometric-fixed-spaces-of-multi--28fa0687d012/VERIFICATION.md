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

# Reproduction
Run `python3 verify.py` with a standard Python 3 interpreter. This reads no external datasets and computes candidate faces from orbit weights, then mod-two boundary ranks. The current verification was performed using the packaged program. It exhaustively checks 2,474 bipartite orbit profiles, one mixed-dimensional example, and 80 seeded multipartite trials. The mathematical proof, rather than these finite tests, supplies the general integral statement. No independent audit has been performed.
