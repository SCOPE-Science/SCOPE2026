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
# Mathematical verification

Reproduce by running `python verify_hlawka.py` with Python 3. The script is included as a full standalone file. It checks, in exact `fractions.Fraction` arithmetic, the degree-nine characteristic polynomial, the trace, and the one-dimensional null direction of the rational projection matrix. The expected polynomial is \(t(t-1)^4(3t^2-12t+4)^2/9\).

Additional independent floating-point checks use an explicit least-eigenvalue eigenvector to approach the sharp second-order coefficient along five decreasing nonzero step sizes. They also check positivity along 1,200 pseudorandom but deterministic real transverse directions and the sign and slope of the endpoint exponent variation. The script prints the attained checks and numerical values. These are supplementary: the complete nine-dimensional spectral assertion is already established by an exact rational identity, and the local uniform and parameter-persistence statements follow from the explicit \(C^2\) Taylor expansion and implicit-function theorem in the proof.

Unproved limits: no global Hornich--Hlawka positivity classification for real \(\ell_p^3\) in the open range, no effective maximal radius of the local neighborhood, no claim of uniqueness or novelty beyond the inspected literature, and no independent scientific validation.
