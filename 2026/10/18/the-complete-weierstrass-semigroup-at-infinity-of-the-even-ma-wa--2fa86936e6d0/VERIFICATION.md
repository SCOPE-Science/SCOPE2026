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

Exact proof checks: the Kummer valuations and genus, and the specific shorter nongap list of Lemma 4.1, are present in the specified Ma–Wang source; the local regularity argument uses only these valuations and the integer identity \(N=br+q+1\); the Apéry residue/permutation count exactly equals genus. The determinant-\(N\) lattice fan is a complete covering by unimodular sectors in its lattice, not an empirical enumeration. The maximum-Apéry inequality, the conductor formula, and generator irreducibility are shown in the proof.

The included `verify_semigroup.py` is standalone, uses Python standard library only, and prints `VERIFY_OK` after independently checking Apéry minima against Dijkstra shortest paths in the finite residue graph. `VERIFICATION_OUTPUT.txt` records the exact run. Six parameter pairs were tested. Finite checks cannot prove the infinite-family statement; that is supplied by the displayed algebraic proof.

The arithmetic invariant belongs to a specified rational point. No independent audit, independent mathematical validation, or external theorem certification has occurred.
