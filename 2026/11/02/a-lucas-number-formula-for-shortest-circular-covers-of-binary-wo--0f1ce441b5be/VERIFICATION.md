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

# Verification details

The all-order theorem is established by the proof in `RESULT.md`, not by a finite computational extrapolation. The upper-bound Eulerian multigraph and the universal lower-bound potential inequality are algebraically quantified for every integer \(n\geq3\). The potential is explicitly defined on every binary de Bruijn vertex, so the lower bound remains valid even when a candidate cover contains forbidden supplementary windows.

Running `python3 verify.py` from this package returned `VERIFY_OK`. It generated each finite required edge set, balanced augmented degree lists, strongly connected graphs, Euler tours and complete cyclic window histograms for orders 3 through 16; it also checked the potential inequality on every binary edge at those orders. Running `python3 crosscheck.py` returned `CROSSCHECK_OK`; it used an independent integer representation and Hungarian minimum-cost matching to reproduce minimum route-inspection augmentation for orders 3 through 13. The deterministic optimal sequences for orders 3 through 12 are in `witnesses.csv` and are checked by the construction verifier. No third-party runtime dependencies are required.

These finite checks do not independently certify the infinite theorem, historical priority, or the completeness of the literature survey. No independent scientific audit has been performed.
