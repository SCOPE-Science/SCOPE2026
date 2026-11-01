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

# Reproducibility and limits

The accompanying `verify.py` uses Python 3 standard library and `COCHAIN.json` and can be run directly with `python3 verify.py`. The latter file gives the 184 nonzero entries of a complete mod-three two-cochain indexed by lexicographically ordered, row-major triangular faces; no external package, network, or unavailable file is required.

The program checks all 600 tetrahedral coboundary identities, the signed integral boundary of a selected eight-triangle fundamental sphere, its nonzero cocycle evaluation, 1,800 exhaustive six-square supports, each support's nonzero evaluation, all pair incidences, the generating group actions, and the mod-three chain ranks. Its output is embedded in `verification_output.txt`.

The general flag-complex support lower bound and the derivation of all possible opposite-pair types are proved in `RESULT.md`, not inferred from enumeration. The known integral homology \(\mathbb Z/3\) is cited to Shareshian--Wachs and Jonsson rather than independently recomputed by this verifier. The cocycle certificate proves nonvanishing of the given integral carrier, not a complete integral Smith-normal-form computation.
