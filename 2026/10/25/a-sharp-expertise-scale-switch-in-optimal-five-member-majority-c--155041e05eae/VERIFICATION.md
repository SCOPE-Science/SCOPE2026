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

# Reproduction and limits

Run `python verify.py` with Python 3 (standard library only); the deterministic JSON output must equal `certificate.json`. All comparisons use integer or exact `fractions.Fraction` arithmetic, including the 126 unordered committee partitions, the three exclusion margins, and the two representative scales. The checker separately computes all majority-success probabilities by exhaustively summing vote outcomes, and verifies the separately affine majority identities by exact 0 / 1/4 interpolation. This is an exhaustive finite proof of the 126-partition endpoint certificate, *not* a numerical extrapolation from sampled skill scales. The continuum conclusion is supplied in `RESULT.md` by affine endpoint domination. The comparison with earlier literature is based on the cited accessible texts, not an independent bibliographic validation.
