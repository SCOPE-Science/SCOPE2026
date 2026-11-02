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
# Reproducibility and verification

Run `python3 verify.py` with standard Python 3 and no third-party dependencies. The code constructs every binary word for each \(2\le n\le14\), computes its cyclic integer window sums for every \(1\le\ell\le n\), groups equal outputs, and compares actual fibers with the claimed binomial histogram, capacity and constant-weight generating polynomial. It verifies singleton and maximum-fiber counts and total preimage mass. An independently implemented inverse recurrence is tested for every output through \(n=8\).

Actual result:

```
VERIFY_OK source_words= 425984 profiles= 381082 inverse_cases= 3036 all_n=2..14 all_ell=1..n
```

The main proof of all-length correctness is the residue-class difference argument in RESULT.md. The finite tests verify implementation details and boundary examples but cannot substitute for that proof. They do not test noisy, incomplete or unindexed read data. The case \(n=12\), \(\ell=6\) gives exactly \(2187\) read outputs, \(1394\) singleton outputs and maximum fiber size \(20\). The case \(n=12\), \(\ell=5\) has \(4096\) distinct outputs.
