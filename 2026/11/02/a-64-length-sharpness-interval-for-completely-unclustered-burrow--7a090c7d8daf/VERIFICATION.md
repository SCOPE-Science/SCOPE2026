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
Execute from the folder containing the evidence files:

```
python3 verify_direct.py witnesses.tsv
python3 verify_inverse.py witnesses.tsv
```

The first program checks the stable LF permutation and exact Hamming-distance certificate, including the alternating-binary perturbation bound. The second reconstructs the underlying primitive necklace, computes the complete sorted rotation table, and counts cyclic input runs directly. Both require only the Python standard library, and their actual output is included in `check_output.txt`. All 34 certificate rows for lengths 31 through 64 are individually examined. Neither program enumerates all possible ternary last columns, since enumeration is unnecessary when the universal lower bound is known.

The mathematical use of the two verifiers relies on the explicit one-cycle criterion and the proven relationship between input runs and last-column Hamming distance. The general lower bound is published; the certificates are finite and establish no statement outside the reported range. Independent mathematical validation has not been performed.
