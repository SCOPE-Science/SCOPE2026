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

# Verification of the mathematical claim

Execute `python3 artifacts/verify.py` from the directory containing this document. The supplied source uses only the standard Python library. The executable checks all nonzero-difference representation counts for the prime fields of orders \(3,7,11,19,23,31,43\) and the extension field \(\mathbb F_{27}=\mathbb F_3[T]/(T^3-T-1)\). It performs a complete enumeration of the \(19\)- and \(23\)-element fields' triple-translate intersections; their exact minima are \(1\). It checks the four order-\(11\) sum relations and evaluates their exponent-matrix determinant as exactly \(-11\). It tests \(96\) fixed-seed complex functions, performs \(1968\) direct Fourier-frequency evaluations, verifies the exact autocorrelation deficit numerically against a separately assembled pair-dispersion expression, and tests additive-character equality cases. A successful execution prints `VERIFY_OK`.

The unrestricted prime-power theorem does not follow from sampling. Its decisive general ingredients are the directly proved Paley difference-set identity, the exact algebraic sum-of-squares decomposition, the standard Hasse elliptic-curve bound for distinct cubic roots, the complete exact small-prime checks, and the order-\(11\) Smith-normal-form determinant argument. No independent external validation is asserted.
