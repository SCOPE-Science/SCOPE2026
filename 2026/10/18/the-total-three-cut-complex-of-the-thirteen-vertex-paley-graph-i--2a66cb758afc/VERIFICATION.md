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

# Reproducibility and limits

Run `python3 verify.py`. Its integer-only output should match `verification_output.txt` exactly. The script constructs the Paley graph from the six nonzero quadratic residues modulo thirteen, obtains every facet and face, pairs the stated 3,275 nonempty face pairs, and checks all 39,156 cover relations for acyclicity by a full directed topological sort. This proves that the associated ordinary Morse CW model has only a vertex and a five-cell.

The same script separately computes augmented mod-two boundary ranks in every dimension and all 78 orientation-sensitive affine Lefschetz sums. These finite computations have exact exhaustive loops; no floating-point approximation, unproved truncation or timeout interpretation enters the claim. Reproducing the output verifies the input combinatorics and proof certificate but is not an external mathematical audit.
