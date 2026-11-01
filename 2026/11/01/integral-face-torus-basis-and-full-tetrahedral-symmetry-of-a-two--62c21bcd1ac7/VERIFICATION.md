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

# Reproducibility

Run `python3 verify.py` in a directory containing `verify.py`, with Python 3 and SymPy available. The script reconstructs the graph and all 66, 180, 117 cubical cells from definitions; checks all integer cellular boundary relations; constructs ten explicit signed face-pair product 2-cycles and verifies their integer primitiveness; computes the mod-two and integral Smith ranks; enumerates all 24 graph symmetries and checks every signed cellular action commutes with boundaries and maps top cycles to signed top cycles; computes all five conjugacy-class character values and irreducible multiplicities; and checks the symmetry-quotient invariant dimensions.

The exact standard output of an executed run is embedded as `verifier_output.txt`. The verification depends on the finite graph presentation and the two-point sufficient-subdivision theorem. A finite computation does not establish a theorem for all graphs and no such general claim is made. An independent publication audit has not been performed.
