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

# Verification of the exact biclique cyclic census

Run `python3 verify_cca_biclique.py` with a standard Python 3 installation. The script reads no outside data, enumerates all 49 support-pair transitions, checks every row of the finite classification, and simulates 72,720 independently labelled initial states on bicliques with up to nine total vertices. For 196 further parameter pairs it checks weighted support enumeration against the six closed formulas, total mass \(3^{a+b}\), and integrality of orbit counts. The recorded output is `verification_output.txt`. The final success marker is `CCA_BICLIQUE_EXACT_VERIFY_OK`.

These computations check the finite-support proof object and small labelled examples; they do not prove that no earlier literature contains an equivalent claim, nor do they replace the universal inclusion-exclusion argument and its verified forty-nine-state classification.
