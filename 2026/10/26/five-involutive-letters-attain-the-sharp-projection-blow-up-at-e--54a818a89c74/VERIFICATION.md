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

The all-parameter proof is in `RESULT.md`. In particular, check the explicit five involutions, the generation of the symmetric group on hidden pairs by three observable involutions, the single-pair growth operation, the Myhill--Nerode distinction of all nonempty unions, and the transitivity proof for original minimality. The known orbit upper bound is rederived directly for the single hidden fixed-point-free involution.

Execute `python3 verify.py` using Python 3 and only its standard library. Actual execution returned `VERIFY_OK configurations=9 independent_projected_words=4095 largest_projected_states=1023`. The checker independently constructs all five permutations, checks involutivity, explores and minimizes reachable projected subset automata for all \(k=2,\ldots,10\), checks original reachability, and compares determinized projection against exhaustive hidden-letter insertion patterns for 4095 short words. At each gap, one insertion suffices because the hidden letter is involutive.

The computed range is finite and does not independently establish the theorem for arbitrary \(k\). No independent external mathematical audit or certification is claimed.
