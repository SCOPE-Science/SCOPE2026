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
# Reproduction and proof boundaries
Run `python3 verify.py`. Its complete execution enumerates \(375\) distinguished lines; for each of the \(70125\) pairs it decides exact complex intersection by congruences among fifth roots, and compares the decision against an independently built linear-algebra rank test modulo \(11\). The modular test is a check of the implementation, not an argument that finite-field ranks prove complex incidence.

The exact argument uses the coordinate-support dichotomy: points of a line have two or four nonzero coordinates; the two-support points are the \(50\) labelled cone vertices, each incident with \(15\) special lines; the four-support points incident with at least two distinct special lines have two positive and two negative fifth powers, giving \(5\cdot3\cdot5^3=1875\) distinct points, each of incidence multiplicity two. The rank-test module additionally validates that no coding error in the congruence convention changes any pair's adjacency. An exhaustive common-neighbor check distinguishes the two edge types \((13\) versus \(1\) common neighbors\()\), proving the unique \(50\) cliques of maximum size \(15\).

This is a finite proof over \(\mathbb C\) only for the specified \(375\) lines. It does not compute intersection multiplicities, scheme structure, virtual contributions or other families of lines. Independent external review and audit have not been performed.
