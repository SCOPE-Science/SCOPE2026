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

The proof concerns smooth eight-hyperplane sections of \(\operatorname{Gr}(2,8)\) over \(\mathbb C\) and the ordinary integral middle cup-product pairing. The included standalone `checker.py` uses only Python 3 standard-library rational arithmetic; executing it yielded all PASS messages.

The exact coefficient rule \(\int_G f=[x^7y^6](x-y)f\) was evaluated for the normal-bundle Chern classes and Schubert products. The checks obtained \(\deg G=132\), the Schubert matrix \(\left(\begin{smallmatrix}62&28\\28&14\end{smallmatrix}\right)\), discriminant \(84\), Smith factors \(2,42\), Euler number \(636\), second-Chern square \(692\), signature \(244\), and middle rank \(632\). The finite quadratic form was checked on all \(84\) cosets, including invariance under the defining lattice generators and the Gauss-sum check. Direct comparison with the published Appendix A.6 confirms the Chern and Schubert inputs.

Crucial non-computational proof steps are successive integral hyperplane Lefschetz, the universal coefficient theorem, Poincaré duality, the Wu formula, primitive-sublattice discriminant gluing, and indefinite even-lattice uniqueness. They are applied with explicit dimension, primitivity, signature, and length hypotheses in `RESULT.md`; the computational verifier does not certify or replace them. The source comparison does not rule out unindexed prior specialization.
