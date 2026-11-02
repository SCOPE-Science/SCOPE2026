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

# Verification and limits

The analytical proof in `RESULT.md` is the evidence for the infinite-parameter result. The critical identities are the exact prolate commutator, positivity from the one-interval spectral gap, and the explicit two-dimensional reduced-resolvent expansion. The remainder is uniform because the finite fixed interval bounds the cross-kernel Taylor remainders and the complementary spectral gap remains positive for fixed interval length.

Run `python CHECK.py` with NumPy as listed in `requirements.txt`. This executes Gauss–Legendre Nyström discretizations for three fixed interval lengths, multiple integer separations and microscopic detunings, tests the commutator and positivity, checks the ordering of the first three eigenvalues, and compares the full spectrum against the two leading asymptotic formulas. The actual executed result from the package was `CHECK_OK 279` with no exceptions.

The finite matrix checks are supplementary and do not certify the infinite asymptotics. The spectral simplicity and parity of the top prolate eigenfunction are classical external premises, supported by references [1], [3] and [4] of the result. The conclusion is not uniform as interval length varies, nor at unbounded detuning. The resonance gives leading-order gap cancellation only, not exact equality of eigenvalues. No independent mathematical audit has been performed.
