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

The finding is established by the finite-language two-round game criterion and an all-parameter group-theoretic atomic-profile lemma. Computational checking is supplementary; it does not extend a finite test into an infinite proof.

Run `python3 verify.py` and `python3 direct.py` with a standard Python 3 interpreter. The scripts use no third-party dependencies. `verify.py` checks the algebraic seven-category mask formula against exact enumeration of every atomic mask for abelian 2-groups of total exponent up to eight, tests all integer multiplicity profiles with cyclic-factor count at most thirteen, and checks fifteen pairwise different representative signatures. `direct.py` separately builds complete equality and ternary addition tables on \(0,x,y\) for each representative and checks further nonisomorphic equivalences.

Results are preserved in `verify_output.txt` and `direct_output.txt`. The full signatures of the fifteen representatives appear in `profile_table.json`. The unbounded parameter reduction is justified in RESULT.md, Proof steps 3–5. No independent audit or external formal certification is claimed.
