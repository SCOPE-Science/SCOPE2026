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

# Reproducible verification

Execute `python3 verify.py` with standard-library Python 3. The recorded result is `PASS 3762 finite exact/numerical assertions`.

The script verifies exact rational moments and the four-atom quadratic-defect eigenvalue for 49 positive pair weights, circular four-design harmonics and quadratic spectra for polygons with 5 through 29 vertices, and a perturbative Vandermonde Gram mechanism on 200 reproducible near-pentagon inputs. It requires no external data or dependencies.

The universal classification and quantitative rigidity are proved in `RESULT.md`. Neither these finite computations nor their successful execution establishes the infinite-dimensional or universal claims on its own. The stability constants follow by explicit Cauchy–Schwarz, spectral and root-separation inequalities in the proof.
