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

# Verification of the exact semigroup maximal norm

The proof uses the identity \(\sup_{t\ge0}|P f+e^{-t}(I-P)f|=\max(|Pf|,|f|)\), event-selector linearization, conditional Cauchy--Schwarz, the two-dimensional singular-value polynomial \(z^2-(1+b)z+b^2\), an explicit conditional eigenvector profile, and the strict concavity of \(\Lambda\). The argument applies to arbitrary probability spaces and conditioning sub-\(\sigma\)-algebras. The finite-atom residue law follows from a proved deficit comparison, not enumeration.

`verify.py` executes deterministic finite-state diagnostics. Run with `python3 verify.py`; it uses only the Python standard library. The tests verify the singular-value characteristic polynomial and equality profile for rational probabilities, nearest-index classification for 2 through 150 uniform atoms, and thousands of complex-valued input tests for simple conditional expectation partitions. Finite tests do not prove the universal claim.

The scientific status is self-reviewed, not independently audited. Potential equivalent formulations in earlier two-step martingale literature remain a publication-priority risk.
