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
# Verification details

Run `python3 verify_multipartite.py` with NumPy and SciPy installed. The program reports `VERIFY_OK` after (i) direct support checks against explicitly enumerated stable-set incidence vertices, (ii) 1,980 exact rational transfer inequalities for independent Bernoulli positive-part surrogates, (iii) a quadrature/simulation comparison of three Gaussian critical profiles with a total of 150,000 Gaussian samples, and (iv) the analytic three-block centered constant checked numerically.

The script is self-contained and uses a fixed deterministic random seed. Its comparisons are finite checks; the infinite strict majorization theorem, boundary cases and central limit assertions follow from the proof in RESULT.md, not from testing. Publication priority remains uncertain pending any independent literature investigation. Independent mathematical validation was not performed.
