---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Reconstructed the multiplication matrices over F3[x]/(x^4+x^3+x^2+1), irreducibility, dim(S)=4, dim(U)=12 and Frobenius orthogonality. Every nonzero rank-one uv^T cannot be orthogonal to all multiplication maps because as a ranges over F81, M_a v spans F3^4; so U has no rank-one matrix. An independently structured rank computation evaluated all 130 projective 2-planes N: the restrictions Mv=0 on K always have rank 8 from dim(K)=10. Each 2-dimensional annihilator therefore contains exactly 3^2-1=8 nonzero matrices of rank exactly 2; distinct rank-2 matrices have unique right kernels, so 1040 in total. This verifies the exact necessary plane balance, not the unresolved lift equation. The source program also states a full U rank distribution, but these independent checks need only the rank-one exclusion.

## originality

PASS

The exact statement was compared against the primary literature with special-case implications and pre-existing formulas separated from the contribution. Priority is a bounded best-of-knowledge assessment; see all four explicit comparisons and residual risks. Neither the binary failure theorem nor general bounds imply existence or impossibility of the displayed q=3 K. The claim explicitly stops at a necessary-condition survivor.

## value

PASS

The rank-two/plane-balance constraint is the first substantive kernel-lift obstruction at the smallest field beyond the recent binary counterexample. A concrete q=3 survivor of all 130 simultaneous geometric constraints is a motivated boundary object for assessing whether the binary impossibility mechanism extends; the necessary-condition survivor is informative despite not constructing a Ferrers code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
