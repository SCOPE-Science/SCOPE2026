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

# Verification notes

The included `verify_forced_multipartite.py` uses only the Python 3 standard library. Execute `python3 verify_forced_multipartite.py`; no external datasets, symbolic algebra library, network access, or other artifact is needed. It independently enumerates all initial per-vertex states (blank or one of the palette colours), filters proper initial assignments, executes the actual local forcing rule, and compares the complete domain-weight coefficient vector with the Stirling-profile sum. It separately computes the minimum seed by scanning admissible nontrivial polychromatic-part subsets and compares it with direct enumeration.

Actual replay: `VERIFICATION_OK profiles= 15 parameter_cases= 48 admissible_seed_assignments= 54346`. It includes \(G=K_{2,2,3}\), \(\lambda=5\), giving coefficients \((0,0,0,0,600,1800,2280,1620)\) and minimum initial size \(4\). The independent brute force is finite and not a proof for arbitrary part sizes or palette sizes; those quantifiers are supported by the written mathematical argument in RESULT.md. The historical boundary formulas are credited, not independently re-evaluated here. Independent audit has not been performed.
