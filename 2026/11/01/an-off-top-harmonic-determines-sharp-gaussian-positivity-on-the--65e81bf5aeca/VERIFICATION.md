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

# Mathematical verification

The exact certificate implemented in `check_odd6.py` first proves that the fourth nonconstant spectral eigenvalue is strictly increasing using the integer inequality \(5^8>2^6 3^7\). It then validates rational bounds for positive rational powers by raising endpoint inequalities to integer powers. At the rational endpoints \(71/200\) and \(89/250\), the fourth eigenvalue changes sign; over the entire interval every other nonconstant eigenbranch has a strictly negative rational upper bound. These finite exact comparisons, the explicit harmonic decomposition, and Schoenberg's theorem establish the sharp conclusion for all real exponents.

The same checker reconstructs the complete 462-vertex graph, verifies every pairwise shortest-path distance independently by breadth-first search, confirms the intersection-array recurrence by integer matrix multiplication, and compares the predicted spectrum with direct numerical symmetric diagonalization at three illustrative exponents. The numerical tests are finite consistency checks, not proof of universal negative type. The exact sign assertions execute with integer arithmetic and rational numbers only; floating-point estimates are not trusted as sign evidence.

Run with `python3 check_odd6.py` (Python 3 and NumPy). The expected markers are `EXACT_INTERVAL_CERTIFICATE_OK` and `CHECK_OK`. Independent audit and validation have not been performed.
