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

# Verification

The companion `verify.py` reconstructs the two seven-dimensional algebra multiplications and enumerates all invertible homomorphisms by generator images over \(\mathbb F_2\), obtaining \(512=(2-1)^2 2^9\) and \(2048=(2-1)^2 2^{11}\) automorphisms. It constructs explicit thin and non-thin subalgebras of \(k[t]/(t^{14})\) in characteristics \(2,3,5\), with each of the two valuation sets, and verifies the bases, closure, and expected vector-space dimensions. It checks that square-zero elements project to different-dimensional subspaces of the first radical layer for the thin local algebra and its associated graded algebra in characteristics \(2,3\). Running the included file under Python 3 prints `VERIFY_OK`.

These are exhaustive checks only in the explicitly specified finite cases. The infinite-field/characteristic-independent assertions require the displayed algebraic arguments. The proof checks the generator relations and the morphisms and inverses of the automorphism normal-form parameterizations, rather than treating experiments as infinite evidence.

No independent mathematical audit has been performed.
