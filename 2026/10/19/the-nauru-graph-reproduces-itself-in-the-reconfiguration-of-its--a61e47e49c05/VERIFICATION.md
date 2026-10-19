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

# Finite verification and reproducibility

All paths below are relative to the directory containing this file. Python 3 with only standard-library modules is required.

Run:

```sh
python3 verify_structure.py
python3 verify_reconfiguration.py
python3 verify_product.py
```

These commands deterministically overwrite the three named JSON certificates. Their SHA-256 digests are printed on stdout and should match the bundled certificate hashes. Each program reconstructs its graph combinatorially, rather than trusting certificate contents. `verify_structure.py` checks every vertex's distance profile, exactly 60 MMD pairs, and an explicit two-component rook decomposition. `verify_reconfiguration.py` enumerates all independent sets in both MMD components, verifies the 576 proposed size-18 bases directly against all unordered original vertex pairs, determines every allowed single-vertex exchange and performs 576 breadth-first searches. `verify_product.py` tests the complete 24-vertex permutation correspondence and checks all ordered pairs of minimum bases against the Cartesian-square condition.

The complete certificates are `structural_certificate.json`, `bases_certificate.json`, and `product_isomorphism.json`. The accompanying `structure_output.txt`, `reconfiguration_output.txt`, and `product_output.txt` capture actual successful executions. No testing of an infinite family and no independent external validation is claimed. The proof's lower bound uses the MMD-cover necessity and its sufficiency is independently established by checking every size-18 candidate directly.
