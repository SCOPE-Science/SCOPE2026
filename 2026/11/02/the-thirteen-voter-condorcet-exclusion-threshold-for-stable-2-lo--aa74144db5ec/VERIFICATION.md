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

Run `python3 verify.py` using Python 3 and the standard library. The script checks exact rational payoff identities for all six possible strict rankings on a finite rational simplex grid; enumerates all six-type anonymous profiles for each electorate size from one through thirteen, identifying every strict Condorcet winner and every two-candidate interior stationary solution; and counts the exact Condorcet-exclusion witnesses.

The executed results were zero exclusion profiles at every size through twelve and two anonymous profiles at size thirteen, among 2688 profiles where the named candidate was a strict Condorcet winner. Exact evaluation of the example gives \(H_A=703/2197\), \(H_B=H_C=1/3\), and pairwise margins \(7\)-to-\(6\). The verifier also reconstructs the earlier eighteen-voter symmetric exclusion construction with payoffs all equal to \(1/3\).

The unrestricted twelve-voter impossibility is justified by the parity-sensitive symbolic lower bounds in `RESULT.md`; the finite enumeration is supplementary and does not certify infinite families. The thirteen-voter uniqueness is established by explicit polynomial inequalities in `RESULT.md`, not by a numerical optimization search. Independent audit has not been performed.
