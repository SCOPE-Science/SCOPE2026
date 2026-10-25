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
# Reproducible verification

Run `python verify.py` from the directory containing `matching_certificate.json.gz`. Python 3 standard library suffices. The certificate uses 21-bit masks for simplices and one explicit facet/cofacet pair for each matched edge of the face poset.

The checker reconstructs \(T_7=L(K_7)\) independently from two-subsets, enumerates all nonempty subsets of every open neighborhood, checks the ten-dimensional face vector, validates unique coverage by 9,120 facet/cofacet pairs and 254 critical faces, and topologically sorts the entire reversed-matching Hasse diagram (18,494 vertices). For each of seven critical four-cells it computes all signed gradient path sums to 246 critical three-cells over the integers and asserts that every entry is zero.

The attached `verification_output.txt` records successful execution. The log is not by itself a certificate: `verify.py` and `matching_certificate.json.gz` must be present. The proof makes no claim about higher triangular graphs or natural group actions on this homotopy equivalence. No independent audit has been conducted.
