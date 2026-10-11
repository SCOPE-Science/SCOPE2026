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
# Reproducibility of the finite homotopy certificate

Run `python3 verify.py` and `python3 crosscheck.py` in the directory containing this document. Both scripts use only the Python standard library and reconstruct graph edges and complex faces from definitions.

`verify.py` enumerates all \(10{,}012\) augmented faces, constructs \(5002\) augmented matching pairs (corresponding to \(5001\) ordinary pairs and one critical vertex), checks all \(47{,}968\) oriented Hasse incidences by a topological sort processing every face, and computes the complete signed integer Morse differential from the two critical five-dimensional cells to the six critical four-dimensional cells. That matrix is exactly zero. The ordinary Morse CW complex has only one zero-cell, six four-cells, and two five-cells. Its two attaching maps are null by the fourth-dimensional Hurewicz isomorphism, giving the stated wedge.

`crosscheck.py` uses a different edge ordering and independent recursive enumeration followed by exact binary elimination for every simplicial chain boundary. It yields reduced mod-two Betti ranks six in degree four and two in degree five, and zero elsewhere.

This is an exhaustive finite proof for one graph, not a probabilistic test or an extrapolation. The homotopy conclusion requires both the acyclic matching and the exact integer Morse attaching calculation: mod-two ranks alone would not establish it. No independent external audit is reported.
