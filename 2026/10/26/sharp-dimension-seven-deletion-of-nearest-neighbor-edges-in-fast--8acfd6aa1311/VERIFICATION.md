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

# Reproducible checks and boundaries

Run `python3 verify.py` using only the Python standard library. Expected output is in `verification_output.txt`.

The program checks two exact convex-dual identities for the exceptional dimensions, a polynomial factorization determining the all-dimensional Krawtchouk ordering, exact rational Fourier eigenvalue envelopes through dimension \(128\), and direct character-row sums computed from graph edges through dimension \(9\). It explicitly checks the extra equality at dimension seven. All arithmetic in those checks is integral or exact rational.

The infinite theorem does not follow from these finite loops; its proof is the algebraic argument in `RESULT.md`, including the exact quadratic-minimum inequality for all dimensions above seven, the direct dimension-seven integer inequality, the universal two-mode lower bound, and nonnegative group averaging. The row-sum, symmetry, and support hypotheses are essential. Source priority cannot be certified by program execution, and independent validation is not claimed.
