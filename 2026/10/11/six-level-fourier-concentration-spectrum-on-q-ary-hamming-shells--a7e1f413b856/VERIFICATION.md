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

# Verification of the six-branch Hamming-shell concentration theorem

The analytic proof in RESULT.md is the basis for the all-parameter claim. Every eigenvalue, multiplicity, domain restriction, null direction, and normalization has been explicitly recomputed from the conditional support-and-label basis.

Run the standalone standard-library script with `python3 artifacts/verify.py` from the extracted package root. It computes the integer kernel of the degree-two ambient Fourier projector on each sampled shell, verifies exact predicted eigenvalues through power sums, and checks that the product of the corresponding distinct integer-shifted matrices annihilates that kernel. It does not use floating-point comparisons or external dependencies.

Actual completed output:

```
EXACT_OK q=3 n=4 k=2 shell=24 spectrum_levels=4 rank=24
EXACT_OK q=3 n=5 k=2 shell=40 spectrum_levels=6 rank=40
EXACT_OK q=3 n=5 k=3 shell=80 spectrum_levels=5 rank=40
EXACT_OK q=4 n=4 k=2 shell=54 spectrum_levels=6 rank=54
VERIFY_OK cases=4 exact_integer_spectral_moments_and_annihilators=PASS
```

An independently implemented normalized ambient character-basis Gramian check also agreed in nine cases: \((q,n,k)=(3,4,2),(3,5,2),(3,5,3),(3,6,2),(3,6,3),(4,4,2),(4,5,2),(4,5,3),(5,4,2)\). The finite tests are nonexhaustive. The theorem does not assert the six-level decomposition for \(k\le1\) or \(k\ge n-1\).
