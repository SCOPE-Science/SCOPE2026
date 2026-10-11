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

`verify.py` reconstructs the named eight-vertex sphere presentations from explicit tetrahedron lists. It checks Barnette's face vector, enumerates every legal \(2\)-to-\(3\), \(3\)-to-\(2\), and \(4\)-to-\(1\) move, and verifies the exact legal centers.

It then exhausts all \(8!\) vertex permutations. Exactly \(12\) preserve Barnette's facets. The orbit of one \(2\)-to-\(3\) center has size \(2\) and equals the complete upward move set; the orbit of one \(3\)-to-\(2\) center has size \(6\) and equals the complete downward move set.

Every legal move is then performed. Exhaustive relabeling identifies both upward targets with the Brückner--Grünbaum sphere and all six downward targets with one another. The downward target has face vector \((8,26,36,18)\).

Exact replay output:

`VERIFY_OK f=8,27,38,19 aut=12 move23=2 orbit23=2 target23=BG move32=6 orbit32=6 target32_f=8,26,36,18 target32_classes=1 move41=0`

The checker does not infer polytopality from coordinates. The polytopality conclusion uses the published complete eight-vertex sphere classification.
