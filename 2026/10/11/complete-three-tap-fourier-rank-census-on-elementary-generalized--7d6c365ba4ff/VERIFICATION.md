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
# Verification record

The exact complex proof reduces the group convolution operator to \(N\) explicit two-dimensional character blocks, then classifies their zero determinants and counts the corresponding characters and supports. No numeric threshold, truncated list, or stochastic test enters that argument.

The independent executable `check_triads.py` uses only Python 3 standard-library facilities. Run it with `python3 check_triads.py`. It constructs every left-regular translation matrix and calculates its rank by modular Gaussian elimination modulo \(1000003\), then compares the resulting nullities with the predicted formulas. The exhaustive test sizes were \(56+560+20+816+120=1572\) supports. There were \(81\) further sampled supports for \((p,d)=(3,3)\), making \(1653\) tests. (The modular-rank computation is arithmetic in the test modulus; it is **not** an independent characteristic-zero rank proof.)

Observed output:
```
CHECK (2, 2) tested 56 nullities {0: 56}
CHECK (2, 3) tested 560 nullities {0: 560}
CHECK (3, 1) tested 20 nullities {2: 18, 4: 2}
CHECK (3, 2) tested 816 nullities {4: 144, 6: 648, 12: 24}
CHECK (5, 1) tested 120 nullities {0: 120}
CHECK (3, 3) tested 81 nullities {12: 19, 18: 61, 36: 1}
VERIFY_OK
```

Unproved limits: no claim for weighted taps, larger supports, arbitrary nonabelian groups, or finite-characteristic convolution rank. Independent mathematical validation has not been performed.
