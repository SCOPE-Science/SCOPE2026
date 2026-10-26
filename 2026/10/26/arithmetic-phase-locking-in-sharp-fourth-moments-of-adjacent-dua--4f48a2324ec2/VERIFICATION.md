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
# Verification and reproducibility

Run `python3 verify.py` in the same directory, using Python 3 and its standard library. The program returns `ALL_CHECKS_PASSED assertions=3148` on successful execution.

The checker independently represents \(\chi_r\) as the complete homogeneous symmetric Laurent polynomial of degree \(r\) in three torus eigenvalues with product one. The \(SU(3)\) Weyl integration formula reduces all six quartic moments to exact integer constant terms after multiplication by the Weyl denominator and division by six. The checker verifies the expected six moments at every integer degree \(1\le n\le9\). Separate deterministic checks evaluate the analytic upper/lower formulas, root stationarity, phase and amplitude grids through \(n=16\), and the nonmonotone-degree inequality for seventeen resonant degrees.

The finite checks support the proof but cannot establish statements for arbitrary degree. The all-degree content depends on the multiplicity-free Pieri rule, central-character selection, the uniqueness of the invariant pairing, and the elementary global optimization supplied in RESULT.md. No third-party proof assistant, independent reviewer, or independent validation is claimed.
