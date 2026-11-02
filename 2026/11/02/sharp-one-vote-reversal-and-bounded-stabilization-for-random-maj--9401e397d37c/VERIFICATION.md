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

# Verification notes
The exact-rational verifier `verify_clique_majority.py` was executed with Python 3 and SymPy. It confirmed all 858 initial count-state predictions for complete graphs with 2 through 40 vertices, including every outcome probability and expected time, and solved 760 transient-state Markov equations. It also checked that outgoing transition probabilities sum to one and that claimed closed classes are absorbing under the update rule. The analytic proof in RESULT.md supplies the argument for every graph order, not just those checked computationally.

Reproduce by extracting the script as UTF-8 and running `python verify_clique_majority.py` with SymPy installed. This does not constitute independent external verification. This work does not cover other update rules, biased tie-breaking, or noncomplete graphs.
