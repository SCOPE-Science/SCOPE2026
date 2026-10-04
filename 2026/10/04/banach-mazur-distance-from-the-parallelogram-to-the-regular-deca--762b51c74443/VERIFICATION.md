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

The geometric proof was reconstructed with all hypotheses and quantifiers explicit. The lower-bound reduction uses the published proposition that an optimal homothetic sandwich may be taken with the inner parallelogram inscribed in the centrally symmetric body. Dihedral symmetry then leaves exactly three side-separation classes.

For the nontrivial separation-two class, with \(q=(\sqrt5-1)/2\), \(\varphi=(1+\sqrt5)/2\),
\[
E=\varphi-qu(1-v),
\]
and
\[
A=2-u+qv,\qquad B=\varphi+v-qu,\qquad C=2+q(u+1-v),
\]
the checker verifies the crossing identities, derivative numerators and all five residual factorizations used to prove
\[
\max\{A,B,C\}\ge\frac{3\sqrt5-1}{4}E.
\]

The exact packaged checker was replayed from `research20_bm_decagon/verify.py` before packaging and returned:

`VERIFY_OK exact symbolic identities`

No finite numerical experiment is used to infer a continuum statement. The checker verifies symbolic identities in the proof; the continuum coverage follows from the stated monotonicity and case partition.
