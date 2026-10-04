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
The proof reconstructs the distributed scalar EF21 update with independent half-dropout contractive compressors.

`verify.py` independently builds the four-moment recursion, checks the determinant identity
\[
\det(I-M_n(s))
=
\frac{s[6n-(n+8)s]}{16n},
\]
enumerates all compressor outcomes for small worker counts, and verifies spectral radii immediately below and above the claimed frontier.

The finite checks are algebra and transcription guards. Exactness of the infinite-time boundary follows from positivity and continuity of the covariance operator together with the analytic determinant calculation in `RESULT.md`.
