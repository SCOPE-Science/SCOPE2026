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

The theorem follows analytically from the normalized sine eigenbasis of \(T^{\!*}T\), the complete chiral zero-mode vector, the dissipative spectral-projector limit, Bézout divisibility, and an exact finite sine-square sum. These arguments prove all positive hopping, all positive absorber rates and all chain sizes \(m\ge2\), without finite-enumeration assumptions.

Running `python verify.py` with the versions listed in `requirements.txt` checks all single-site monitor ranks and several joint minority-monitor sets for lengths \(5\) through \(25\), compares the sitewise capture projector diagonals with the gcd formula, compares directly dissipative eigenvalue imaginary parts, evaluates a characteristic-polynomial gcd over the integers at the eleven-site majority-monitor resonance, and compares four finite-time no-detection limits. The replayed output is:

```
VERIFY_OK spectral_rank_cases=1135 sitewise_capture=2260 loss_spectrum=32 exact_polynomial=1 finite_time_convergence=4
```

These finite checks are corroboration, not infinite mathematical certification. The result does not bound convergence times uniformly in hopping ratios or absorber strengths. Independent auditing and independent validation have not been performed.
