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
# Verification of the exact Boolean heat-flow distortion theorem

Run `python3 verification_check.py` beside this document. The script uses the Python standard library only. It checks 48 exact dual optimization cases by enumerating every integral rooted Lipschitz potential for dimensions at most three; total unimodularity supplies the finite exhaustive reduction. It also checks 360 exact rational anisotropic shadow identities and explicit dual witnesses for dimensions one through nine.

The script was executed successfully from the supplied source. Independent numerical transport LP calculations with SciPy were additionally performed for 70 small cases, including heterogeneous rates, and matched the exact formula. Those external diagnostic runs are not part of the standalone standard-library checker and are not claimed as independent research validation.

The analytic proof, not computational enumeration, establishes the theorem for all dimensions, continuous times, and positive rates. The peak asymptotics rely on exact calculus and uniform Taylor bounds, and are not machine certified. Scientific limits and bibliographic risk are described in `RESULT.md` and `REVIEW.md`.
