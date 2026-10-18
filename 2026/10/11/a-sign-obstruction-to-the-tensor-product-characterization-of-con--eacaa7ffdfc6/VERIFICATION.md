---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each nonzero real scalar \(f\), the factor energy equals \(-|f|^2\), violating every positive lower frame bound. In the tensor product, \((-I)\otimes(-I)=I\) and the single tensor block gives \(|f\otimes g|^2\), hence tensor Parseval bounds \(A=B=1\); in one dimension all tensor vectors are simple. The primary article distinguishes \(GB(H)\) from \(GB^+(H)\) and prints \(T,U\in GB(H)\) in its definition and Theorem 4. For the repaired positive branch, a tensor lower bound \(A\|f\|^2\|g\|^2>0\) and factorization force strictly positive energies on nonzero vectors; fixing \(g_0\ne0\) yields factor bounds after division by \(q_K(g_0)>0\), and symmetrically for the other factor. Nonnegative real factor energies are sufficient, not a claimed necessary characterization for complex controls.

## originality

PASS

The focal 2021 theorem is the object being refuted, not an antecedent covering the correction. Full examination of its printed controls and faulty division shows this minimal sign counterexample and the necessary positivity condition were not expressed there. Searches for an erratum, tensor negative-control counterexamples and alternate control conventions found the source and general fusion-frame work, but no verified prior statement of this sign failure.

## value

PASS

This is a decisive correction to the claimed tensor-product characterization, not an arbitrary negative example: the smallest admissible tensor frame refutes the exact reverse implication and exhibits the missing sign logic; the positive-branch repair gives a useful criterion for safely applying the theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
