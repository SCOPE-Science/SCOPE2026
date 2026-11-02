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

# Verification of the three-patch covariance theorem

The standalone `CHECK.py` uses only standard-library rational arithmetic and verifies all six independent matrix entries of the stationary Lyapunov solution at \(\gamma=1\) and \(\delta=1/4\). As the covariance has an overall factor \(1/\gamma\), the Pearson correlation is a function of \(t=m/\gamma\) alone. The script also rederives the squared-correlation identity, the full derivative sign polynomial, its coefficient sign pattern and a rational bracket for its single positive zero, and symbolically tests the general noise-family initial-slope identity.

Run `python3 CHECK.py` alongside these files. The expected success line is:

```text
VERIFY_OK symbolic_identities=13 exact_sample_checks=24
```

The 24 finite exact or floating-point diagnostics are checks, not the proof of the all-parameter theorem. The all-parameter proof uses the differentiated Lyapunov equation and zero-mode limit; the uniqueness proof uses exact algebra and Descartes' rule. The model uses symmetric dispersal, identical stable local regulation, and non-distance-monotone environmental covariances. Independent scientific validation has not been performed.
