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

The complete graph-family proof is in `RESULT.md`; execute the independent finite tests using `python3 VERIFY.py`.

The packaged program independently builds Cartesian graph adjacency from factor coordinates and tests the induced-degree characterization. Exhaustive enumeration established the exact minimum core size and the full list of minimizers in \(C_4\square C_4\), \(C_4\square C_5\), and \(C_5\square C_5\), examining 39,202, 263,949, and 7,119,515 nonempty subsets of size at most the predicted bound, respectively (7,422,666 total). The numbers of minimum complements were 8, 5, and 10, as predicted.

It additionally tested all predicted slabs and seeded random subsets in eight higher-dimensional instances, performing 878 construction/random checks. The last line of successful execution is `VERIFY_OK exhaustive_subsets 7422666`.

No finite enumeration establishes the induction for every \(r\) and every factor length. Historical priority was assessed against accessible primary papers and research-record searches, not independently certified. This is a self-review; no independent audit has been performed.
