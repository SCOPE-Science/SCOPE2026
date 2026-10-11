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

# Reproduction and mathematical limits

Run `python verify.py` from the directory containing the standalone checker. It uses only Python's standard library. The observed output was `VERIFY_OK: 6 structured and 300 random consistency cases; non-exhaustive numerical checks only`.

The script tests unit norms, the positive dependence, a nonzero determinant of three directions, and all six strict axial vertex inequalities; it also tests a two-tangency example and the unique octahedral endpoint. Numerical evaluation is not treated as a proof for continuum parameters.

The proof is analytic: (i) the pairwise cap-body condition is equivalent to pairwise inverse squared radii sums at least one; (ii) a strict pair yields an open arc on the unit circle; (iii) two nearby nonparallel arc points produce four linearly spanning unit directions with strictly positive dependence and all six spike tests; (iv) all-equality constraints force the regular octahedral case, and at that endpoint one direction cannot cover two spikes. The cap-body criterion is explicitly attributed to the cited primary literature.

Unproved limits: no classification for nonorthogonal spike axes, other cap bodies, higher dimensions, or multi-illumination; no uniform quantitative illumination margin at the exceptional point; no claim of independent or exhaustive external novelty certification.
