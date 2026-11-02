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

# Verification of the nine-class classification

The result is a theorem proven by explicit atom extension counts and an unrestricted three-pebble strategy, not by extrapolating sample computations. For each ordered pair of vertices (including equality), the necessary and sufficient third-vertex configurations are counted in `RESULT.md`; all potentially zero factors are distinguished, and the noncollinear-pair remainder is proved positive for all allowed parameters. Four rank-at-most-three formulas (two per point/line status) distinguish the nine classes.

## Reproduction

From this directory using Python 3 and no external dependencies, run `python3 check_profiles.py` and `python3 symbolic_profiles.py`. `check_profiles.out.txt` and `symbolic_profiles.out.txt` are the respective recorded stdout. The first program constructs nine incidence systems (including symplectic, affine, transversal, Steiner and projective instances), confirms their partial-geometry axioms, and enumerates all ordered-pair atomic-extension supports. The second implements the algebraic extension-count formulas separately, compares them with the first program’s 9 examples, and checks 54,944 arithmetically admissible triples with \(2\le s,t\le80\). It recovers the nine classes with identical supports within each.

## Limits

The parameter sweep includes arithmetically admissible triples, some of which may not support actual finite partial geometries; that is a stronger algebraic consistency check, not an existence claim. The finite concrete examples verify witness existence, not the full quantified theorem. Counting logic, thin geometries, and reductions that omit the named relations are not covered. A human or other independent audit and complete priority verification have not been performed.
