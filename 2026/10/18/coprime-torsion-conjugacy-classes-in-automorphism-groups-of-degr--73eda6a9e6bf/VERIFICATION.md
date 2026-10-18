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

The accompanying `verify_torsion.py` executes direct modular matrix multiplication and row reduction. For each prime field and order below, it enumerates \(\operatorname{GL}_2(\mathbb F_q)\) matrices with \(g^\ell=I\), constructs the induced action on \(\operatorname{Hom}(V,V\otimes V)\), computes the norm-map kernel, and compares against the eigenvalue-resonance formula and its total.

Checked combinations: \((q,\ell)=(3,2),(5,2),(5,4),(7,2),(7,3),(7,6)\). Output ends `ALL_TORSION_ENUMERATIONS_PASSED 6`.

The checker uses prime fields and dimension two; the proof covers every prime-power \(q\), every \(d\ge2\), and \(\ell\mid(q-1)\). It does not verify nonsplit eigenvalues or wild-order torsion. Independent mathematical audit is not performed.
