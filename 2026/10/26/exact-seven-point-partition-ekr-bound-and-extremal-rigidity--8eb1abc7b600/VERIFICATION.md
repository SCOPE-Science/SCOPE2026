---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A family with a prescribed pair has S(6,4)=65 members by contracting that pair, and the 21 such families are distinct. The frozen Python search uses the exact shared-pair adjacency; its reverse colour ordering means each remaining prefix inherits a proper colouring with at most the recorded number of colours. Its neighbour intersection and deletion therefore enumerate threshold cliques without duplication or unsound pruning. A separate exact reproduction (/workspace/audit_replay_4.py) generated partitions by peeling off the block of the least remaining point, obtaining 350 partitions, and used include/exclude branching with clique covers of the incompatibility graph. Fixing one anchor in each of the three block-size types suffices by permutation symmetry. There were respectively 6, 4, 3 families of size 65 through the three anchors, all exactly the pair-stars through the anchor, and no family of size 66 in any anchored search. This proves the complete equality statement for the stated finite parameters. The saved C++ output concerns the maximum alone, not its equality classification.

## originality

PASS

The bound is explicitly conjectured in older literature, not proved there; the inspected broader EKR and Hilton–Milner theorems do not include seven points at rank three. No independent exact proof or equality enumeration at these parameters was identified in the inspected material.

## value

PASS

Seven points are singled out by the conjectured boundary for four blocks. At that boundary a sharp proof and the full rigidity statement fill a motivated case not reached by the large-ground-set results, and give an exact benchmark for prospective general arguments. The claim is finite and says nothing about the full conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
