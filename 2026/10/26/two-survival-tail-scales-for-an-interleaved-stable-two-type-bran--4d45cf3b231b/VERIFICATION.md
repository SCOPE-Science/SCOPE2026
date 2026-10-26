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

The proof uses the exact disjoint partition of the half-line to identify \(\phi_1+\phi_2=2\sqrt\pi\sqrt{\cdot}\), bounds for the total cumulant, and the exact evolution of its two coordinates. Positive-initial-data solutions are unique and global. Their monotone zero-initial limit is nontrivial for every positive time, and the Laplace semigroup identifies it with the actual explosion cumulant.

The asymptotic computation first proves \(u_2(t)=2Lt+o(t)\), then differentiates \(r(t)=\sqrt{u_1(t)}\) and integrates a \(\sqrt{2L}\,t^{-1/2}\) correction. The logarithmic survival exponents follow from the cumulant formula, not numerical simulation.

Run `python check.py` for independent finite numerical illustrations. They verify elementary numerical bounds and integrate the positive-argument system for sampled times only. For \(A_2\), the script replaces the interval starting at \(a_3\) by the full tail and bounds the discrepancy by \(2a_4^{-1/2}\); it does not silently treat this truncation as exact. The proof of the asymptotic limits is given in RESULT.md and remains independent of the program.

The inspection of older literature cannot establish absolute novelty; no independent audit has been performed.
