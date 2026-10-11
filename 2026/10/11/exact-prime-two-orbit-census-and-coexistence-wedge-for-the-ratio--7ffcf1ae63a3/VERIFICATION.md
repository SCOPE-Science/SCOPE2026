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

# Reproducibility and limits

Run `python check_rulkov.py` with SymPy installed. The script reconstructs both steps of each nontrivial two-cycle, verifies the exact derivative identities by symbolic cancellation, and checks the exact algebraic example \((\sigma,\alpha,\eta)=(2,5,1/1000)\). The script was executed successfully after creation and is included without external dependencies other than SymPy. The full proof of universal counting uses an analytic positive-root argument, not experimental enumeration. In the coexistence example, strict stability follows from the rational radical enclosure and the Schur inequalities written in RESULT.md; diagnostic numerical conversions in the script are not separate mathematical certificates.

No computer-assisted exhaustive search of all periodic orbits, basin topology, or literature universe was performed. Published primary-source coverage is limited as described in RESULT.md and REVIEW.md. Independent audit has not been performed.
