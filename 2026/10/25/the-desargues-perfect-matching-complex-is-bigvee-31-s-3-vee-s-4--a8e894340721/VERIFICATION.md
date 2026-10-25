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

# Exact reproduction

Run `python3 verify_desargues.py --certificate CERTIFICATE.json` in the directory containing both files. This is standard-library-only Python and performs a fresh complete construction from the stated graph. The program reconstructs the 30 graph edges and all 60 perfect matchings, independently verifies the perfect-matching count by subset dynamic programming, and enumerates all 44,281 nonempty faces.

The deterministic element matching gives 22,113 pairs, leaving critical cells \((1,42,12)\) in dimensions \((0,3,4)\). The Hasse graph has 244,830 nonempty face incidences; a complete directed topological sort verifies acyclicity. Exact signed Morse-boundary propagation gives 64 nonzero matrix entries in a \(42\)-by-\(12\) integer matrix. Eleven successive unimodular unit pivots leave the zero matrix, so every nonzero Smith factor equals one. The certificate is checked field-by-field against a fresh reconstruction.

The independent matching-extension enumeration gives 113,192 unrestricted matchings including the empty one, 68,910 nonextendible matchings, and exactly 220 cardinality-three and 180 cardinality-four inclusion-minimal obstructions. The calculated Euler characteristic is \(-29\), agreeing with the claimed wedge.

Verification covers the exact finite graph and the supplied algorithm. It does not independently establish bibliographic completeness, a general theorem about all graphs, or any external audit/certification status.
