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

The theorem's complete proof is analytic. The structural step uses local commutation parity and the exact two-dimensional Pauli centralizer; Gibbs factors follow because the Hamiltonian summands act on disjoint tensor factors. The partial-transpose spectrum of an arbitrary Bell-diagonal two-qubit state is \(\{1/2-q_s\}\); the upper bound follows from a largest possible Bell-sector energy gap of \(4J\). The three-term Heisenberg dimer witnesses the sharp boundary.

The provided `verify.py` is standalone apart from NumPy; run `python3 verify.py` with the version requirement in `requirements.txt`. It exhaustively enumerates all commuting subsets of up to four one- and two-site Pauli terms on three sites and up to three terms on four sites, yielding **9,957** structural checks. It also performs **6,600** direct matrix partial-transpose comparisons for one-, two-, and three-term Bell dimers and **3,960** independent full-matrix bipartition checks on examples with four and five sites, in addition to both analytic threshold endpoint tests. The actual run printed `VERIFY_OK 9957 commuting-subset structure checks; 6600 matrix-PPT checks; 3960 bipartition log-negativity checks; sharp beta thresholds`.

The computed samples do not establish the theorem at unbounded system size, and floating-point agreement is not a machine proof. The statement is valid only for commuting qubit Pauli terms with support at most two, with coefficients bounded after collecting identical strings.
