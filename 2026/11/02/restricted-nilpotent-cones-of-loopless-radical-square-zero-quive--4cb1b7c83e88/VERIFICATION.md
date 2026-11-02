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

# Verification

Run `python verify.py` with standard Python 3. The program performs nine full quotient-orbit enumerations for arrow-block sizes \((2)\), \((3)\), and \((2,1,1)\) over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\); its quivers include a directed triangle and a tree, tested at powers \(2\), \(3\), and \(4\). It also enumerates all \(16^4=65,536\) linear maps on the four-dimensional two-arrow Kronecker algebra in characteristic two, directly checks all basis Leibniz identities, constructs inner derivations, and tests restricted squaring modulo inners. Seven separate Jordan-type sum comparisons literally count matrices. The expected terminal markers are `RESTRICTED_HH1_QUOTIENT_OK 9 complete quotient enumerations` and `JORDAN_CENTRALIZER_SUM_OK 7`, followed by no assertion failures.

The direct Leibniz case has \(64\) derivations, \(8\) inner derivations, \(8\) outer classes, and \(4\) restricted-square-zero classes. The three-arrow Kronecker case has \(22\) restricted-square-zero classes and \(64\) restricted-fourth-power-zero classes over \(\mathbb F_2\). The finite tests do not prove the statements in all dimensions. The theoretical proof relies on idempotent normalization, perfect-field Frobenius roots, and standard Jordan centralizer and nilpotent-orbit closure formulas. No independent mathematical audit was performed.
