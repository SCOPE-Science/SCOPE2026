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

`verify_heawood_matching.py` and `morse_certificate.json` form a standard-library replay package. The verifier reconstructs the Fano-plane incidence graph, checks its incidence axioms and degrees, exhaustively enumerates all 3,461 nonempty matching-complex faces, rebuilds the 1,722-pair deterministic matching, checks the 17 critical faces, orients all 14,574 face-poset cover relations, and certifies acyclicity by a complete topological sort. It separately reduces every simplicial boundary matrix over \(\mathbb F_2\) and obtains reduced homology only in degree \(4\), of rank \(16\). A successful run ends with `VERIFY_OK`.

The finite replay proves the stated matching and homology facts only for this explicit Heawood graph. The inference from an acyclic matching to a CW model with one cell per critical simplex uses the standard discrete-Morse theorem. No independent audit has been performed.
