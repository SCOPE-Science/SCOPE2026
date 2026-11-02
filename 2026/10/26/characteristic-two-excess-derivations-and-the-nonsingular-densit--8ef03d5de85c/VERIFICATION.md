---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Derivations are determined by their e1,e2 images through [e1,e_j]=e_{j+1}; the zero bracket [e2,e3]=0 forces b1=0 and comparison of both e_n bracket representations forces a2=a1-b2. For zero brackets [e2,e_j], the central constraints are precisely 2b_4=2b_6=...=2b_(2m-2)=0, leaving m-2 extra parameters only at p=2. Their remaining relations are checked by the central bracket coefficient calculation and the triangular recursion. The diagonal of D is a1, b2, ja1+b2 (j=1..2m-3), and (2m-3)a1+2b2. With a1 nonzero, distinct forbidden projective slopes number min(p,2m-1): two for p=2 and 2m-1 if p>2m-3. This proves all finite-field counts with q^(d-2) free fiber. Independent full derivation-condition matrices and Lie Jacobi checks for n=6,8,10 over p=2,3,5,7 reproduce ranks and diagonal determinant; bounded checks are not the all-m proof.

## originality

PASS

Independent comparison of statements, standard reductions, stronger sources and exact parameter tables. Accessible evidence does not decisively cover this final claim; limitations and material unread sources remain recorded without inferring novelty from search silence.

## value

PASS

Derivation dimension is a basic Lie-symmetry invariant; the exact unbounded characteristic-two defect m-2 and complete finite-field nonsingular density/field-extension threshold jointly give a natural family-wide arithmetic classification, not a single small-case computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
