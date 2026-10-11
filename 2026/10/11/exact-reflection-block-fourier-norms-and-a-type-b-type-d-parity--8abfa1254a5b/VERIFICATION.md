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

# Verification

The complete analytic proof appears in `RESULT.md`. Run `python3 verify.py` using Python 3's standard library. The checker rederives the exact rational type-B and type-D norms from a separate enumeration of sign vectors and permutations in ranks \(1\) through \(7\), as well as the mean-square character orthogonality identity. It also verifies the finite alternating-sign absolute-sum identity through rank \(100\) and checks \(249\) coefficient ratios.

Observed output:

```
VERIFY_OK direct_signed_group_ranks=1..7 checked=7 parity_moments_n=1..100 checked=100 bessel_coefficients_checked=249
NORM 3 B 9/4 D 9/4
NORM 4 B 31/12 D 5/2
NORM 5 B 655/192 D 655/192
NORM 6 B 1289/320 D 129/32
NORM 7 B 6041/1280 D 6041/1280
```

The checker proves no statement for unenumerated ranks. Those ranks are handled by the character orthogonality calculation, exact signed fixed-point and derangement generating functions, beta-integral evaluation, parity-conditioned sign identity and alternating-series bound. The same-model mathematical review passed. Independent audit is not performed.
