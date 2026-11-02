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

# Computational and analytical verification

The universal proof is the inductive exact-partition argument in RESULT.md. The standalone standard-library program `verify.py` reproduces its finite rational cell certificate and reads `certificate.tsv` from the same directory. It treats every parameter cell as left-open and right-closed and splits at **all** reciprocal opinion-difference thresholds, thereby covering all real spacings \(0<d\le1\) without sampling gaps or endpoint ambiguity.

The calculation terminated for agent counts \(1\) through \(7\), with respective leaf counts \(1,1,2,5,10,11,26\) and global maximum freezing time twelve. The code compared its recomputed leaves against the stored certificate and checked interval coverage, cluster outcomes and exact midpoint/right-endpoint trajectory replay. All assertions passed when run from the actual checked source directory. An independent small Fraction forward implementation also checked each seven-agent change point at equality and on each side.

The certificate is finite but **exhaustive within the claim** by the proved rational-decision subdivision induction. It is not evidence about larger agent counts, other initial distributions, stochastic dynamics, or any unpublished prior theorem. No independent external audit has been performed.
