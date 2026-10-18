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
# Reproduction of the relative simplicial collapse

Using the supplied `verify_collapse.py` and `collapse_certificate.json` in the same directory, run `python3 verify_collapse.py collapse_certificate.json` with a standard Python 3 interpreter. No optional dependencies are required. `verification_output.txt` is a recording of the expected output, not a substitute for running the code.

The script recomputes the two complexes from all Hasse matching choices (acyclicity tested by directed topological sorting), checks their \(256\) facets each, face-vector and embedding identities, and reconstructs each of four apex links. It then checks every one of the \(3428\) certificate pairs against the **current** face poset for codimension one, unique coface, maximality, and protection of the smaller complex. The result is an exact equality of the final face set with the target. The bitmasks are of lexicographically sorted Hasse incidences, with the ordering defined in the source code's docstring.

This is an exhaustive finite combinatorial proof for exactly one tetrahedron and its boundary. It does not test general dimensions, validate unrelated mathematical claims, provide an independently reviewed certificate, or assert an equivariant sequence. The induced map on homology is integral and natural only because the verified collapse realizes the inclusion.
