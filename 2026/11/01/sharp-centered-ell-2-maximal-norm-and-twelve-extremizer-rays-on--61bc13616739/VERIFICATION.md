---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For each nonnegative input choose one of four radii independently at six vertices, reducing ∥M∥² to max_{r∈{0,1,2,3}^6} λmax(A_r^TA_r). Full 4096 exact selection set tested with integer fraction-free Sylvester on 13653 I−10 B_r^TB_r: 4084 strictly PD, 12 exceptional dihedral images of (0,1,2,3,0,1). For exceptional Q, char det(zI−Q/900)=zP(z)/24300; P shifted above cutoff has one Descartes sign change and rational isolating interval. Polynomial eigenvector components satisfy Qv=900λ*v exactly modulo P, strictly positive and 18 chosen-ball inequalities; PF simplicity and 12-element orbit classify equality. Independent integer Bareiss, sympy char/eigenpoly and 4096 scipy eig tests reproduce all counts.

## originality

PASS

General sharp graph maximal results, complete/star graph ℓ², and graph variation bounds do not compute C6 strong centered ℓ². Previously recorded four-/five-cycle cases are different local ball geometry; no directly covering exact C6 spectral/certificate table found. Originality qualified because an unindexed C6 enumeration may exist.

## value

PASS

The smallest cycle with diameter three has four distinct graph-ball radii and an exact nontrivial algebraic ∥M∥₂ plus complete 12-ray rigidity. This is a natural exact invariant of a canonical graph, with a nontrivial finite spectral classification useful for comparative graph maximal problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
