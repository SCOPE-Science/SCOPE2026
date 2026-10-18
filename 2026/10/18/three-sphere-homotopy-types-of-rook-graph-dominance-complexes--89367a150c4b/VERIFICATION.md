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

The all-parameter proof is in `RESULT.md`. Its critical inputs are the exact row–column cover, the nerve identification for the combinatorial Alexander dual of the intersection, integral Alexander duality, elementary triangle fillings or two-facet deletion to establish the intersection sphere's homotopy type, and the null-map homotopy pushout.

To reproduce the finite cross-checks, run `python3 rook_dominance_verifier.py` in the same directory. The script enumerates all subsets for \((p,q)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,4)\), tests independent face predicates, checks reduced Euler characteristics, and performs complete mod-two boundary-rank calculations on all listed boards with at most twelve vertices. The larger \(4\times4\) board is enumerated for face counts and Euler characteristic but not for mod-two boundary ranks.

`CHECK_OUTPUT.txt` records the output actually obtained. The checker is finite and cannot establish the general theorem by itself. No independent mathematical audit has been performed.
