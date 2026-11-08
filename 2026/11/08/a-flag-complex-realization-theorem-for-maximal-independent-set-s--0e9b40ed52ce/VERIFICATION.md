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

# Reproducibility

Run `python3 check_whiskered_shattering.py` with Python 3 and standard library only. Expected output: `WHISKERED_MIS_SHATTERING_PASS 1188 49190`.

The code constructs each tested graph explicitly, determines independent sets by checking edges, determines inclusion-maximal independent sets of the whiskered graph independently by brute force, computes every Boolean support trace, and compares it against the stated module-projection criterion and coefficient polynomial. It covers every labeled graph on at most five core vertices when each has one leaf, on at most four vertices when each has two leaves, and on at most three vertices when each has three leaves. The correctness of the unrestricted theorem rests on the written proof rather than finite enumeration. The trusted source dates and coverage comparisons in the references do not constitute an independent audit.
