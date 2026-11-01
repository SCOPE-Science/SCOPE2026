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

# Reproducibility and verification

Run the included \(\texttt{verify.py}\) using a standard Python 3 installation; it requires no third-party packages. It checks the exact finite polynomial identity (3) modulo \(32\) and independently reconstructs the coefficients of \(H(x)\) via its partition product through the stated cutoff. Its output includes the counts of tested identities and coefficient indices.

The polynomial identity is a complete certificate: both sides are polynomials of degree at most \(23\), so checking all \(24\) coefficients exhausts the identity rather than sampling it. The coefficient computations are finite tests only; the proof of the unbounded statement uses the algebraic Mahler equation, congruences, and induction.

The proof applies to positive indices only; \(h_0=1\) has valuation zero. Literature priority is checked against the identified primary and adjacent work, but cannot be guaranteed. Independent validation has not been performed.
