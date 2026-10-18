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

# Reproduction and limits

Run `python morse_integral.py` with Python 3. Run `python verify.py` with NumPy and NetworkX installed as described in `requirements.txt`.

The integer script checks the complete 1,090-face complex, 542 matching pairs, all 4,272 oriented Hasse covers, acyclicity by directed topological sort, the six critical cells, and the exact zero Morse boundary between dimensions four and three. This confirms the ordinary integral homotopy type and the absence of torsion (the attaching degree vector vanishes).

The character script reconstructs exactly 24 edges and all 96 graph automorphisms. It checks degree-four/five boundary ranks 181/58 over the fields of 101 and 103 elements, verifies that the fourth mod-prime quotient is one-dimensional, calculates every induced scalar, identifies the bipartition sign on that line, computes all signed Lefschetz traces, and verifies all character-table frequencies and irreducibility inner products. It separately checks the published rotation-subgroup character.

These are exhaustive finite checks for this finite graph, not merely numerical samples. Mod-prime ranks alone would not certify integral freeness; the matching proof supplies that premise. No external independent audit or integral equivariant direct-sum classification is provided.
