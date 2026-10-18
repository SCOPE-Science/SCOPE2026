---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Read the frozen RESULT.md and Sun--Li Definition 18/Lemma 19/Proposition 20. With X=R^2, K=diag(2,1/2), K-dagger=diag(1/2,2), F=(e1,e2,0,...), G=(2e1*,0,...), both mixed reconstructions equal diag(2,0); primal and dual errors are diag(0,1/2) with exact norm 1/2<1, and ||K||=2>1. Both sequences are Bessel in ell2. Nevertheless K-dagger T_F R_G=diag(1,0) is singular, while R_G e2=0 and K e2=(1/2)e2 refute the lower K-frame bound. The general proposed sufficient repair follows from injectivity and K K-dagger K=K (giving K-dagger K=I), then ||I-K-dagger A||<=||K-dagger|| ||K-A||<1 and Neumann inversion; Bessel synthesis supplies the frame bound. Equality product=1 fails in this example; no necessity claim.

## originality

PASS

The counterexample targets the actual unscaled hypotheses of Sun--Li Lemma 19 and Proposition 20, not the established near-identity approximate-dual theorem. Search and actual publisher full-text reading found no identical printed correction or logically dominating norm-scaled theorem in the checked sources. The conditioning factor follows from the defect identity but its omission and singular counterexample are source-specific and unreported in the inspected full text; originality remains best-of-knowledge.

## value

PASS

A published foundational frame assertion that two errors <1 ensure invertibility and a K-frame is false. A minimal 2D counterexample locates the precise normalized defect, and the norm-product bound supplies a universally valid, dimensionless, Neumann-series repair; this changes applicability of downstream approximate K-dual constructions, rather than giving an unmotivated type check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
