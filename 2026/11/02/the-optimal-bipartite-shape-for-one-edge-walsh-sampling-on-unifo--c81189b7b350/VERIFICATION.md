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

# Verification record
The standard-library-only command `python verify.py` completed successfully. It independently enumerated all 4,657 labelled spanning trees across the six graph types \(K_{a,b}\) with \(2\le a\le b\le4\), computed their exact rational Gram entries, and checked the predicted Gram matrices entrywise, ranks, invariant-sector eigenvector equations, and squared condition numbers. Separate exact-rational arithmetic exhausts all candidate bipartitions for each \(4\le n\le15\) and confirms the minimizers including the \(n=9\) tie. The code also evaluates the closed large-order exclusion inequality for \(16\le n\le200\); the actual infinite proof is the symbolic inequality given in the main result. No randomized computation, floating-point premise, independent audit, or external certificate is used.
