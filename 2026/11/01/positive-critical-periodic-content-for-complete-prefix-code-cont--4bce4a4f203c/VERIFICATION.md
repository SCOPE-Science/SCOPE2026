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

# Reproducibility and mathematical verification
The package includes `artifacts/verify_prefix_content.py`, a self-contained standard-library Python program. It constructs the usual de Bruijn cycles, validates three complete prefix-code dictionaries, follows a deterministic code-boundary map, checks the resulting cycle's primitivity, and compares every pair of its code-boundary shifts against the weighted digit-common-prefix bound. The recorded test orders are finite: binary orders 1–7 for two complete codes and ternary orders 1–4 for a third code. A successful run prints `VERIFY_OK`.

The exact all-order proof in `RESULT.md` uses the primitive length \(b^k\) of the de Bruijn word, residue-cycle congruences and strict strong separation; it is not inferred from this finite test. The explicit real-line example uses interval gaps and elementary square roots, not floating-point optimization. The theorem makes no claim about incomplete codes, overlapping IFSs, or arbitrary inhomogeneous contraction lists. Independent scientific review has not been performed.
