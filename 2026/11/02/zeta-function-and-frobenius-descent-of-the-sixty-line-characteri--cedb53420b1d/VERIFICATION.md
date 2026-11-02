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

# Exact verification and limits

Run `python verify.py` with the package's `requirements.txt`. The checker builds \(\mathbb F_{16}=\mathbb F_2[a]/(a^4+a^3+a^2+a+1)\), validates the embedded primitive fifth and third roots, computes the Gröbner basis of the affine Jacobian gradient to exclude all geometric singularities, and checks all \(16^2\) linear combinations spanning the distinguished line. It then normalizes all coordinate permutations to sixty different lines and verifies the thirty Frobenius transpositions.

All \(85\) projective points over \(\mathbb F_4\) and all \(4369\) over \(\mathbb F_{16}\) are tested once. Exact rational matrix arithmetic gives the line-intersection rank twenty and fixed divisor rank ten. The last two Frobenius eigenvalues follow from the two exhaustive point counts and standard K3 cohomology, not from numerical fitting. The recorded execution ended with `VERIFY_OK` and is embedded as `verify_output.txt`.

The computation is finite and exhaustive only for the explicit field, line orbit, and matrix calculations. It does not by itself prove the general cohomological trace formula, the Hodge index theorem, or complete geometric line enumeration without the cited full-text literature. Independent audit has not been performed.
