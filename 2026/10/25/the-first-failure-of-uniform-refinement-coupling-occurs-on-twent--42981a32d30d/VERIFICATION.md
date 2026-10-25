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

Run `python3 verify_refinement.py` in a directory containing the source file. The program uses only the Python standard library and exact integers; no external datasets or packages are required.

It enumerates the block-size profiles for every size \(2\le n\le19\), builds the complete refinement graph between every adjacent block-count pair, and tests an integral maximum flow against its exact demand. All 171 pairs pass. It also checks the 20-element two-block versus three-block witness by factorial orbit counts and cross multiplication and confirms that the corresponding exact transportation network cannot be saturated.

Observed output: `PASS 171 exact feasible adjacent couplings for n<=19; exact obstruction for n=20,k=2`.

The source reconstructs the finite certificates on demand; they are not taken from machine logs. Mathematical sufficiency of the finite checks requires the profile-flow equivalence proved in `RESULT.md` and the classical integral max-flow theorem. The finite program says nothing about coupling existence at larger sizes. No independent audit has been performed.
