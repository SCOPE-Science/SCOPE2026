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

Run `python3 verification/verify_async_bipartite.py` and `python3 verification/verify_async_bipartite_quotient.py` from the directory containing this file. The first script computes every vertex update directly for 12,416 scan orders across ten complete bipartite graph sizes; it checks 1,433,144 state-order pairs, checks that every map is bijective, and compares every microscopic least-period count and the even-size schedule enumeration with the theorem. The second script multiplies explicit binary two-by-two parity matrices and tests the mod-three criterion for all 32,738 mixed shore-words of length two through fourteen. Both are self-contained standard-library programs.

The actual run produced `ASYNC_BIPARTITE_PARITY_VERIFY_OK` and `ASYNC_BIPARTITE_QUOTIENT_OK`; complete outputs are included as `verification/states_output.txt` and `verification/quotient_output.txt`. These checks are finite and not a proof of the theorem for arbitrary sizes; the proof uses invertibility, the parity quotient, injectivity of its lifting map, and exact binomial counting. No independently authored mathematical audit has been performed.
