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

# Verification performed

Python 3 standard-library program `verify.py` was inspected and executed from the extracted package location. It checks 2317 admissible unary-style six-item 3-PARTITION instances with targets \(8\) to \(48\), comparing separate original triple partition and completed-cycle block-packing programs; it constructs 15 valid witness permutations and checks cycle sizes and prescribed path edges. It also checks 5004 count-multiset instances comparing the fixed-exponent DP with indexed-subset cycle packing. Observed output: `VERIFICATION_OK three_partition_instances=2317 positive=1275 constructed_permutation_witnesses=15 fixed_exponent_DP_tests=5004`.

# Limits

The formal NP-hardness conclusion is established by the proof's many-one reduction from strongly NP-complete 3-PARTITION; the verifier does not decide arbitrary unbounded input instances. All claims concern explicitly encoded finite partial bijections, with no added vertices. The review is same-model only; independent audit is not performed.
