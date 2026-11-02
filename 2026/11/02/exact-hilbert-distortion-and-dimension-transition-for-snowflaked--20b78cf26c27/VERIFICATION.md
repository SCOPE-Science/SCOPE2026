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
The standalone exact-arithmetic checker was executed with `python3 check.py` and returned:

`CHECK_OK exact_cases= 585 exact_rational_assertions= 72300`

The checker enumerates all block-size tuples with two to four blocks and every block size from one to three; it tests squared interblock distances \(1\), \(4/3\), \(2\), \(3\), and \(4\). Each case checks a weighted variance equality, the canonical Euclidean Gram matrix, all pairwise distances, a weighted barycenter null vector, and exact rational matrix rank. Separate balanced-size cases verify the closed threshold and distortion expressions. These are finite verification data, not a proof of the result for all real exponents or integer block sizes. The proof of the unrestricted theorem is in RESULT.md. The findings are self-reviewed; no independent mathematical audit has been performed.
