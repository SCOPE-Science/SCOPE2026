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

Run `python3 verify.py` in the same directory as `coloring.json`.

The verifier independently reconstructs \(S(4,3)\) from the overlap definition: all \(81\) length-\(4\) ternary words are generated, outgoing one-symbol shifts are symmetrized, loops are removed, and duplicate edges are collapsed. It obtains \(237\) edges.

It then checks that `coloring.json` assigns exactly one colour in \(\{0,1,2\}\) to every vertex and that no edge is monochromatic. The three colour classes have sizes \(28,30,23\). Finally it reconstructs the three edges of the triangle \(0000,0001,1000\), giving the matching lower bound \(\chi(S(4,3))\ge3\).

The word-representability conclusion uses the published theorem that every \(3\)-colourable graph is word-representable. The verifier does not attempt to construct or minimize an explicit representing word.
