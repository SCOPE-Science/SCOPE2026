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

The statements in `RESULT.md` follow from a finite quotient on the 961 ordered nonempty support pairs, together with a mathematical lifting lemma showing that every periodic support cycle induces a permutation of occupied color classes. The latter lemma proves that the microscopic entry depth equals the support entry depth for *all* shore sizes, not just the checked examples.

Run `python3 fca5_bipartite_verifier.py` from the same directory using the Python standard library. The output must end with `FCA5_BIPARTITE_EXACT_VERIFY_OK`. The program recomputes the exact functional graph and its cycles, every support-pair terminal period and preperiod, the full basin coefficient matrix, the exact 64 parameter-pair polynomial comparisons, and five direct microscopic examples totalling 97,525 initial configurations.

`support_attractors.csv` is an independently readable list of every support pair and its exact support preperiod and eventual microscopic period. `support_cycles.csv` lists all 16 periodic support cycles, their occupied-color cardinalities, and their monodromy orders. `fca5_bipartite_verification.txt` records the output of the checked program.

This is a finite exact algorithm for a quotient with a proved reduction from arbitrary shore sizes; the additional microscopic enumeration is a consistency test rather than a proof of a general theorem on its own. There has been no independent audit of this mathematics.
