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

# Reproducible mathematical checks

From the accompanying source files, compile and run `rb_triangular_verify.cpp` with `g++ -std=c++17 -O3 rb_triangular_verify.cpp -o rb_check && ./rb_check`. It checks the original identity on all basis pairs for every projective rank-one operator in the six-dimensional algebra over the prime fields of orders 2 and 3. The expected exact success marker is `UT3_RANK_ONE_RB_DIRECT_OK`, following totals 155 and 1082 with image-type partitions (91,64) and (722,360).

Run `python3 rb_peirce_verify.py` to enumerate every idempotent in upper-triangular binary matrix algebras of orders 2,3,4 and independently calculate both Peirce-corner dimensions by binary elimination. The expected success marker is `TRIANGULAR_PEIRCE_COUNTS_OK`, following counts 4, 64, and 1280.

The all-prime-power results, the all-dimension formula, and the case of characteristic two over nonprime fields are proved symbolically. No finite computation certifies those infinite domains by itself. These checks do not constitute independent external validation.
