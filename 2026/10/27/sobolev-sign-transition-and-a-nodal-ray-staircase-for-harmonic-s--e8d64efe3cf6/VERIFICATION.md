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

# Reproduction and scope

The theorem is analytical; no finite computation establishes the universal statements. The checker is a finite corroboration of the stated polylogarithm kernel, local upper-half-plane zero counts, and first-order angle law. Its checks cover 10 combinations of a negative Sobolev exponent and a near-boundary radius, plus 20 positive-value evaluations of nonnegative exponents. All computed angular roots are compared with the predicted count and limiting first-order drift.

To reproduce, install packages listed in `requirements.txt` into a Python environment, and execute `python check.py` from this directory. Recorded output is in `check-output.txt`. The script brackets roots on 80 uniformly spaced angular intervals; because such a grid is finite, this check is not an exhaustive root-isolation certificate. Exhaustiveness for all sufficiently small radii and all nonexceptional negative orders is proved by the uniform angular remainder and sign-gap argument in `RESULT.md`.

For real \(\sigma<0\), the endpoint of the angular domain is \(|\theta|=\arccos(\rho/2)\), so the theorem explicitly excludes any zeros on the outside-of-disk portion of the Euclidean circle. The proof of the positive-order statement uses a probability measure representation and involves no numerical approximation. The count at the negative even exponent thresholds is intentionally not asserted. Independent audit remains not performed.
