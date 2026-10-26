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

# Verification of the wheel absorption theorem

Run `python wheel_verify.py` with the versions specified in `requirements.txt`. Execution returned: `PASS: 1438 independent checks, 37 wheel sizes, all resonance branches, detuning and exact Krylov ranks.` The second status line reported exact unit-spoke survival \(2/3\) at \(n=3\) and \(1/2\) at \(n=8\), and zero for the other sizes tested.

The program constructs adjacency matrices directly from cyclic rim edges and equal hub spokes. It uses independent numerical eigenspace projection against the trapped rim vector for every resonant branch and small positive/negative spoke detunings at each \(3\le n\le39\). In the unweighted regime, it also performs exact SymPy rational Krylov-rank and projector calculations at \(3\le n\le13\). At resonance, the expected bright rank decreases by exactly one, and the computed long-time dark overlap agrees with the closed formula. The program does not approximate long-time dynamics via arbitrary finite-time cutoffs.

The analytical proof itself establishes the result for every finite \(n\ge3\), every \(\tau>0\), and every \(\gamma>0\). Its critical steps are: orthogonal decomposition into a hub-uniform two-dimensional block and rim Fourier modes; exhaustive eigenvalue-collision classification; normalization and projection in the unique degenerate sector; and dissipative removal of all trap-visible modes. The integer-spoke classification follows separately from a universal upper bound \(n\le8\) and exact small-size algebraic incompatibilities. The numerical tests are finite corroboration and cannot alone establish an all-dimensional theorem or historical novelty.

No independent scientific audit has been performed. Comparisons to earlier work and unresolved historical-priority risks are documented in the supplied review and audit materials.
