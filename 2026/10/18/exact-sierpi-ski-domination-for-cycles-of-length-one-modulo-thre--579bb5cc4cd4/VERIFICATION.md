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

# Verification scope

Run `python3 verify.py` with Python 3 and its standard library. The program constructs the Sierpiński product edges from the map \(f\), builds their closed-neighborhood bitsets, and confirms domination directly for explicit certificate maps and vertex sets. It verifies 522 parameter pairs in the range \(3\le n\le60\) and \(1\le k\le9\), comparing the closed-walk condition with an independently implemented modular reachability computation. The four nonattaining small cases exhaust the full normalized connecting-map space and all selections of the candidate size. The fifth case stops after finding an attaining witness, so that particular enumeration is not exhaustive. The recorded run is preserved in `verify_output.txt`.

The finite searches do not certify infinitely many instances, and the two exhaustive negative checks at higher order do not by themselves establish the theorem. The proof's unrestricted steps are the sharp per-layer lower bound, one-hole equality rigidity, induced coherent orientation, reduction to closed walks, complete classification of their lengths, and a uniform explicit upper construction. These steps are presented in `RESULT.md`. There is no claim of independent external audit or machine-formal proof.

The program additionally checks the explicit \(n=7,k=3\) map \(f=(0,4,5,6,0,8,2)\), confirming that its \(21\) selected vertices dominate all \(70\) vertices. This is relevant to the historical comparison with an indexed, superseded submitted-draft formula, not a substitute for inspection of that unavailable draft.
