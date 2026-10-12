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

The standalone `verify.py` uses exact rational polynomial operations to reconstruct the Wick-pairing recursion for four fourth powers, checking every coefficient of the resulting degree-eight moment polynomial. It also verifies exact positive degree-four Bernstein coefficients for the second derivative of the sharpness polynomial, the rational isolation bracket for its unique minimizer, and positive- and negative-correlation boundary identities. Running `python3 verify.py` finished with all assertions passing.

The symbolic check does not claim independent audit, originality certification, or validity for non-Gaussian vectors or nonequicorrelated covariance matrices. The mathematical argument gives the general quantified inequality within the stated one-parameter Gaussian family.
