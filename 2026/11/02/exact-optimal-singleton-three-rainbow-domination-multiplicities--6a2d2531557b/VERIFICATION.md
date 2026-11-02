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

# Reproducibility

The included `verify.py` is standard-library Python 3 code. Run `python3 verify.py` in the directory containing this document and the script. It constructs the state set, creates both sparse integer transition matrices, checks the entire matrix equality \(A^8=A^2\), and computes the exact polynomials \(Q_0,Q_1,Q_2\) from the rational resolvent, comparing all nonzero coefficients against the claimed finite certificate.

The program then checks the closed optimal-count formulas against the *exact coefficient sequences* for the first \(97\) prism lengths and performs an independent uncoloured-support enumeration for the \(30\) combinations of lengths \(3\) through \(12\) and defect levels \(0\), \(1\), \(2\). Backtracking uses the neighbour rainbow constraints directly, not the matrix transfers.

Successful execution ends with `VERIFY_OK matrix_dimension=225 A8_eq_A2=True exact_numerators=3 symbolic_residue_classes=6 full_label_lengths=3..5 independent_support_checks=30 lengths=3..12`.

The infinite theorem relies on the finite matrix identities and the formal trace generating function; checking finitely many graph orders by itself is insufficient. The matrix arithmetic is integer exact, and the entire verifier is included rather than only a prior log. No independently authored mathematical assessment has been performed.
