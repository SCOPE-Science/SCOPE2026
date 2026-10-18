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

# Reproducible verification and boundaries

Run `python3 verify.py` using Python 3 and the standard library. The output must agree byte-for-byte with `verification_output.txt` and finish with `VERIFY_OK`.

The checker independently lists all labeled Steiner triple systems of order seven by recursively covering the 21 unordered pairs with 7 triples, and obtains 30 systems. It builds the associated centered 16-word codes, verifies Hamming minimum distance at least three and exact radius-one coverage, and checks that translation produces 240 codes. A distinct Hamming parity-check construction, permuted over every permutation of the seven coordinates, gives exactly the same 30 centered codes. Its Fano-line intersection distribution is eight, fourteen, seven, one at shared-line counts zero, one, three, seven.

For one fixed perfect code, the checker loops over all 240 second perfect codes. For each of the resulting 240 explicitly constructed 32-vertex subsets in the eight-cube, it verifies that the 256 open-neighborhood incidences are distinct. It constructs the 16 matching edges by unique nearest-codeword relations and verifies the eight-direction count vector. The resulting profile counts are multiplied by 240 only through the separately proved transitivity of the labeled code family. The script does not search the \(2^{256}\) arbitrary subsets of the cube, does not test every ordered pair separately, and does not replace the written completeness proof. No independent audit or external certification has been performed.
