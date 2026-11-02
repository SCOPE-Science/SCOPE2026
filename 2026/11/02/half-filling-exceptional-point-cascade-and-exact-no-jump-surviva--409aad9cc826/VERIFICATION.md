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

# Verification of the exact finite-time and exceptional-point theorem

Run `python verify.py` with Python 3, NumPy, SciPy and SymPy installed. The script constructs the entire Johnson adjacency matrix directly from all \(k\)-subsets rather than trusting a precomputed spectrum. It reconstructs the monitored occupation projector and independently compares numerical eigenvalue multisets and direct complex matrix exponentials against the formula in `RESULT.md` for all tested \(4\le n\le10\) and \(1\le k\le\min(4,\lfloor n/2\rfloor)\). It then verifies six exact symbolic characteristic polynomials and five exact exceptional-point algebraic/geometric multiplicity pairs. The recorded successful invocation returned `VERIFY_OK checks=121`.

The finite tests do not prove an infinite classification. The general proof is the exact up/down commutator and the all-parameter harmonic decomposition in `RESULT.md`, followed by a direct two-dimensional discriminant calculation. The coverage is \(n\ge2k\), \(k\ge2\), \(J>0\), \(\gamma>0\). In particular, the verification does not concern Liouvillian exceptional points, off-sector state dynamics, an arbitrary initial density, or rates varying by configuration.
