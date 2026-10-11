---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The primary multi-knockoff paper gives conditional iid uniform null winner labels on \(\{0,\ldots,\kappa\}\) and the exact FDP threshold. At \(q=1/(\kappa r)\), the threshold reduces to first passage of level \(r\) by iid increments \(+1\) with probability \(1/(\kappa+1)\) and \(-r\) with probability \(\kappa/(\kappa+1)\). Raney's cycle lemma gives the submitted first-hit count, and the bounded harmonic equation gives the smaller-root limit. A fresh independent exact-rational replay matched the formula to dynamic programming over several \(\kappa,r,d\) ranges and reproduced all three displayed \(q=0.1\) values.

## originality

PASS

Gimenez-Zou provide the uniform winner law, threshold and generic FDR control, including the detection threshold, but do not evaluate the complete-null crossing probability. Emery-Keich use a different multiple-knockoff construction. The ordinary single-knockoff exact law is not sufficient because the winner probabilities change with \(\kappa\). Targeted Resultary and primary-literature searches found no source with the submitted \((\kappa,r)\) Raney staircase or calibration comparison.

## value

PASS

The source explicitly motivates multi-knockoffs through the detection threshold. The exact staircase converts that design parameter into an attained complete-null error law and shows that different admissible \((\kappa,r)\) choices at the same nominal level can consume very different fractions of the FDR budget. That is a natural calibration question with direct theoretical and diagnostic use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
