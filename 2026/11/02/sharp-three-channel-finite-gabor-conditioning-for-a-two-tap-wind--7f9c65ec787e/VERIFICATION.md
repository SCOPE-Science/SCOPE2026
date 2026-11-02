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

From the extracted package directory, run `python3 CHECK.py` using Python 3 with NumPy. The run printed:

```
CHECK_OK 102701 N=4..40 exhaustive optimizers; direct spectral checks N=4..11
```

The code independently enumerates **every** unordered set of three distinct frequencies for each integer \(4\le N\le40\), computes sampled operator eigenvalues and the frame-potential defect, and checks the exact optimizer sets and values. For \(4\le N\le11\) it constructs and diagonalizes the full Gabor frame operator for all coprime window spacings and a range of all frequency triples. The analytic proof in RESULT.md, not these finite enumerations, covers arbitrary \(N\ge4\). The proof depends on known Fourier diagonalization and elementary trigonometry; the strict second-best-separation inequality and its low-order boundaries are exhibited explicitly in RESULT.md. Scientific originality was assessed only relative to inspected primary text and database results; no external or independent audit or infinite certification is claimed.
