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

# Verification and limits

The published proof is a complete symbolic argument for both infinite families and both exceptional small cases. Reproduction of the independent finite checks requires Python 3 only:

```bash
python3 verify_prime_triplet_g1.py
```

The program uses two independent algorithms: listing the two cheapest \(b y+c z\) costs for every residue class modulo the smallest generator, and dynamic-programming coin-change counts capped at three. It checks every integer \(k\) with \(0\le k<36\) in each of the two families (72 cases). Each trial confirms that the stated endpoint has at most one representation and that all integers in the following range of two smallest-generator lengths have at least two. It also verifies the second-residue formula. Expected output:

```
PASS 72 parameter instances; every residue has two baselines and DP confirms final gaps
```

This finite computation is not a proof for arbitrary \(k\); the symbolic residue-case argument in `RESULT.md` supplies that proof. The verification does not cover higher generalized Frobenius thresholds, primality of all generators, or exhaustive literature originality. Independent mathematical audit has not been performed.
