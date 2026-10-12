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

The standalone artifact `verify.py` uses only Python 3's standard library. In the directory containing this file and `verify.py`, run:

```sh
python3 verify.py
```

The expected final message begins with `VERIFY_OK`. The program checks every linear quotient matrix and every central scalar in the three-dimensional case over \(\mathbb F_3\), independently evaluating the defining group identity and the proposed symplectic criterion. For admissible matrices it checks each linear central twist. It separately counts isotropic subspaces and Lagrangian complements in dimension four over \(\mathbb F_3\), and runs complete or deterministically sampled group-law tests for explicit higher-dimensional operators, with the sampled cases clearly distinguished in code.

The main theoretical verification is the proof in `RESULT.md`: central preservation, quotient linearity, full polarization equivalence, and exact isotropic-subspace counting. Experiments over finitely many fields and dimensions cannot certify a theorem over all odd primes and all dimensions. Independent audit has not been performed.
