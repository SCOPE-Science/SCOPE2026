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
The standalone `verify.py` script is standard-library Python. It exactly rebuilds 15 vertices, 48 edges, and 30 squares of the unordered two-point cubical model, checks signed boundary composition, and performs rational Gaussian elimination with `fractions.Fraction` to get ranks 14 and 26. It forms four cycles from opposite triangular faces, checks their boundaries vanish and checks column rank four. The square-support uniqueness yields a unit coordinate minor, hence integrality of the top basis. It checks all 48 induced actions on the four-dimensional rational kernel, with expected trace equal to the parity of coordinate sign changes times the number of fixed opposite-face pairs. `verification_output.txt` records the executed output. The small finite computation is exhaustive for this graph; no infinite generalization is claimed.
