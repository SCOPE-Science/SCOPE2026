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

Run `python3 verify.py` using Python 3 and only the standard library. The script reconstructs the two chains from prescribed copies of each permutation pattern, forms predecessor bitmasks, and independently counts linear extensions through a memoized subset recurrence. A separate gap-counting routine evaluates the closed product formula. For overlap \(m=4\), explicit generation of all solutions returns nine permutations for \((1,3,4,7,2,5,6,8)\) and eight for \((1,3,5,7,2,4,6,8)\); each generated permutation is checked against both length-eight prescribed occurrences. The two methods agree for every \(m\) from 4 through 10 and the final line is `VERIFY_OK`.

The infinite family follows from the stated two-chain interleaving bijection and symbolic gap vectors. Computational tests are finite corroboration and do not certify arbitrary \(m\), global novelty, or independence. Independent audit status is not performed.
