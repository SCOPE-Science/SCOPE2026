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
The exact source family was checked against arXiv:2303.04665, Example 3.3 and Theorem 3.6. The proof then independently verifies the singular locus, the analytic coefficient transformation, and the projective pencil normalizer.

The bundled `verify.py` checks the determinant of the pencil matrix, the exact coordinate identity realizing \(a\mapsto ua+v\), the second-order coefficient law, the contact-based Milnor formulas, and the explicit pair \(\{1,2,4\}\), \(\{2,3,5\}\). It is a finite symbolic replay of the algebra used in the proof; it is not a substitute for the analytic argument that a germ isomorphism must preserve the unique common tangent and hence induces the stated 2-jet law.

The global equivalence argument uses only projective rank preservation in the pencil \(\langle xz,y^2\rangle\). Aluffi--Faber's stabilizer analysis is used as literature comparison, not as an independent validation of this result.
