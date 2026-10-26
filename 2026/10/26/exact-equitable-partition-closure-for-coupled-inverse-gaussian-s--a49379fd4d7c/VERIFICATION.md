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

# Verification notes

Run `python verify_ig_lumping.py` with Python and SymPy. The program checks the explicit four-type quotient relation and \(M\)-matrix inverses, 16 exact quadratic substitutions, and a two-type dependent example including its three cumulants. All arithmetic is exact, and the expected output begins with `PASS`.

The logical proof is the analytic matrix intertwining, uniqueness of the nonnegative root, and differentiation of Laplace exponents at the origin. The verification does not test arbitrary matrices, all immigration vectors, or infinite-dimensional path-space laws, and does not constitute an independent scientific audit.
