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

The complete proof is in `RESULT.md`. Execute `python3 verify.py` with Python 3 and its standard library. The verifier independently assembles labelled vertices, all rim and rung edges, and closed-neighborhood edge coverage; then enumerates every vertex subset at the first eight prism orders, with and without one fixed deletion. The graph is vertex-transitive, so the deletion position does not matter. It additionally verifies closed-form witness constructions at every order from 3 through 600, covering all residues many times. Finite checks are not a formal proof of the infinite statements. Historic priority checks and scientific limitations are in `REVIEW.md` and `AUDIT.json`. Independent assessment has not been performed.
