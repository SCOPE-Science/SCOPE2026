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

# Reproducible finite verification

Run from the unpacked artifact directory:

```sh
python3 verify.py
```

The code uses only the Python standard library. It implements \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\), independently forms a two-dimensional length-four code from its two listed generators, and forms the ordinary Euclidean dual by an exhaustive dot-product test over all \(4^4\) words. It independently enumerates every dimension-zero, dimension-one, and dimension-two subcode, and the 25 pairs of \(\mathbb F_2\)-subspaces of \(\mathbb F_2^2\).

Observed output:

```text
block profiles: 9; base-field support-space pairs: 25
all duality shifts: -2,-1,0,1,2
exact subcode-to-moment transforms checked at ranks 0,1,2
VERIFY_OK
```

The checks compare directly enumerated exact subcode-support profiles against Gaussian-binomial support moments, then check both complementary dual-shift identities coefficient by coefficient for every possible block-support profile. No precomputed table is used. These finite checks do not verify the infinite quantifiers for arbitrary prime powers, extension degrees, block dimensions, or code dimensions. Those follow solely from the proof in `RESULT.md`. No independent external validation was performed.
