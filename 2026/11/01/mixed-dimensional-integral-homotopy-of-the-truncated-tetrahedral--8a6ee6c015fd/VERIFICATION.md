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

# Exact finite verification

The standalone file `truncated_tetrahedron_ind2_verify.py` is executable with Python's standard library. Its deterministically recorded output is stored in `verification_output.txt`.

The procedure checks the graph on twelve oriented tetrahedral half-edges with eighteen edges; all 4096 vertex subsets; the 864 augmented two-independence faces and 65 facets; the 429 augmented toggle pairs; all 3432 directed Hasse covering relations in an acyclicity check; the ordinary Morse critical profile (one zero-cell, three three-cells and three four-cells); and all nine exact signed integer entries in the zero dimension-four-to-three Morse boundary matrix. A separate full simplicial-chain rank reduction over the field of two elements verifies reduced Betti ranks three in dimensions three and four and zero elsewhere.

The exact integral gradient-path identities are what certify nullhomotopic four-cell attachments; field ranks alone are not used to assert an integral homotopy type. No claim is made about an infinite family or an independent external audit.
