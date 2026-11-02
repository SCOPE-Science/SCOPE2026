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

The analytic argument in `RESULT.md` establishes the all-prime statement. The standalone program `verify.py` implements finite spectral-projector and non-Hermitian propagation checks; its captured stdout appears in `verification_output.txt`.

The executed program verified 1,364 individual-site probabilities over eight odd-prime grids, grouped their energy eigenvalues by a separate computational route, verified all expected bright-space dimensions and class counts, and checked time-evolution under local loss for three smallest prime sizes. The greatest spectral discrepancy was approximately \(2.78\times10^{-15}\). The largest residual in the three explicit long-time loss comparisons was approximately \(1.57\times10^{-10}\), with the chosen observation times and rate documented by the output.

Floating-point agreement and finite computations are not an infinite proof. The nonstandard steps requiring mathematical scrutiny are the rational independence of the half-angle cosine basis for odd primes, the exact zero-energy multiplicity, and the projector-diagonal identities. All are reconstructed in `RESULT.md`. The conclusion concerns infinite-time capture, not uniform convergence of capture times as grid size increases. No independent audit or external proof certification has been performed.
