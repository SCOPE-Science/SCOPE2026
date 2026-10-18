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

The mathematical object consists of the twenty-four exact \(D_4\) root vectors with two nonzero entries in \(\{-1,1\}\). The inclusive Euclidean Rips complexes change at squared distances \(2,4,6,8\), corresponding to unsigned distances \(\sqrt2,2,\sqrt6,2\sqrt2\).

Execute the included exact program and data from the same directory:

```text
python verify_24cell.py 24cell_certificate.json
```

The program reconstructs every finite face, checks both face vectors, verifies each indicated elementary free-face pair or maximal critical removal, checks all faces are accounted for exactly once, and confirms the perfect critical-cell dimension counts. It separately verifies the antipodal distance property at squared scale six. The expected final output is `CERTIFICATE VERIFIED`. This is a complete finite combinatorial certificate, not an inference from floating point homology or a timed experiment.

Boundaries: no equivariant matching is proved, no extension to other polytopes is inferred, and previously published integral Betti numbers are credited. Independent assessment has not been performed.
