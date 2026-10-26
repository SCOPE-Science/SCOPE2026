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

# Reproducible checks

Execute `python3 verify.py`. All computations use Python standard-library string sets and exact integers.

The checker independently constructs four nontrivial rotations per possible five-bit window and compares the direct union of all rotated outputs with the locality sum for every binary word of lengths 5 through 14. It builds 256 suffix states and computes all 512 nine-bit local window scores. It calculates exact optimal suffix vectors and verifies, component by component, the relation \(V_{n+6}(s)=V_n(s)+19\) for every suffix and each of the six base indices \(n=12,\ldots,17\). The max-plus recurrence propagates the identity to every subsequent length; this inductive step is mathematical, not a finite experiment. It also checks the explicit six-periodic extremizer.

The emitted output must finish in `VERIFY_OK`. The separately embedded `verify_output.txt` records one execution and is not itself a proof certificate.

The theorem does not depend on floating-point computations, external network access, or unrecorded auxiliary files. Checks are self-review reproducibility work, not independent scientific validation.
