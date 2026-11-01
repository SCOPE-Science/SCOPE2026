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

# Verification and reproducibility

Run `python3 check_fixed_double_swap.py` with Python 3.9 or newer. Its orbit enumeration reconstructs the cyclic-involution and whole Klein-four orbit families independently; for dimensions 4 through 8 it checks exact coincidence of admissible orbit sets, derives the full clique complexes, computes the first mod-two Betti number by boundary elimination, and checks all 11 elementary collapses in the four-coordinate case. The finite sequence of nonempty face counts is 32, 124, 492, 1984, 8032. Each first mod-two Betti number is 1. The four-coordinate complex collapses to a 5-cycle.

These finite observations **do not prove** the claims for arbitrary dimension or integral coefficients. The general proof in RESULT.md uses orbit supports, fundamental groups of graphs of simply connected spaces, explicitly connected cone links, and a split simplicial retraction. No external computational certificate, proprietary library, or program output is assumed in that proof. Independent mathematical review has not been performed.
