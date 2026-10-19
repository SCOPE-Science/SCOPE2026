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

# Verification and scope

The proof derives all equilibrium branches algebraically, proves a derivative-sign inequality for every sine half-wave, and uses those infinite-domain arguments to obtain the exact count and \(\sqrt b\) asymptotic. The independent-audit channel remains unperformed; no claim of external certification is made.

Run `python3 verify.py` from the same directory to reproduce a finite, standard-library-only set of checks. The recorded local execution produced `PASS: 260 finite consistency checks. Baseline positive equilibrium x = 2.59333620464930`. Checks cover numerous half-wave minima, three positive coefficient vectors, a source-parameter equilibrium and additional large-amplitude root counts. These are numerical cross-checks, not exhaustive proof of uniqueness or formal interval enclosures.

The source parameter vector is exactly \((a,b,c,d,g,k)=(3/2,10,4,2,4,2)\); its all-real-equilibrium count is established analytically in the last proof step. The fold statement refers to nondegenerate zeros of the equilibrium equations and singular Jacobians, *not* to the full dynamical saddle-node normal-form hypotheses. No computation about chaotic trajectories or attractor basins is included.
