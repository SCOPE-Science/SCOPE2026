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

# Reproduction and finite checks

Execute `python3 verify.py` from the directory containing the standalone Python 3 file `verify.py`. It uses only the Python standard library. The actual package verifier was executed on its exact contents and returned:

`VERIFY_OK 266 signed character comparisons, 8742 fixed oriented faces, 10 exact reduced mod-2 chain-rank calculations; n=3..16 character and quotient checks`

The verifier exhaustively enumerates all independent subsets of the simple cycle on the specified small values, tests face stabilization under each natural rotation and reflection, and computes orientation signs by inversion count. It compares each resulting alternating reduced simplicial chain trace to the separately derived path/cycle orbit-graph formulas. It checks cyclic and full dihedral character averages, and independently enumerates the augmented simplicial chain boundaries and ranks over \(\mathbb F_2\) for ten small cycles.

# Infinite mathematical argument and limits

The general proof rests on the published integral homology suspension recurrence, the exact orientation-sign identity for a vertex permutation restricted to an invariant simplex, classification of the orbit graphs as cycles or paths, the path independence-polynomial recurrence \(P_m=P_{m-1}-P_{m-2}\), and exact rational averaging after subdivision. Each statement is proved or explicitly attributed in `RESULT.md`; none depends on a finite search extending to infinity. Computations check representative small boundary values but do not establish an infinite theorem, a claim about integral quotients, or independence from unindexed literature.

Independent audit has not been performed.
