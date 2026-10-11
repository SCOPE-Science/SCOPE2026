---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

A constant Itô solution must have zero diffusion coefficient, so with common nonzero noise \(\sigma(x,y,z)\) only the origin qualifies. The face \(Y=Z=0\) is invariant and gives \(dX=-k_A X\,dt+\sigma X\,dW\), hence a lognormal solution with \(P(X_t>1)>0\) for every \(X_0\in(0,1)\), \(t>0\), \(\sigma>0\). For the paper's values \(\pi=30,r_A=1/6,u=0.6,a=2\), \(k_A=6/5\) and the modified A-drift at all-join is \(19/5\), not zero. A fresh numerical replay also reproduced the package's illustrative escape probability \(0.1957956706626627\).

## originality

PASS

The defining 2024 article was reread at the exact model equations. It explicitly treats the three state variables as joining probabilities, removes the three logistic boundary factors on the stated ground that those factors are nonnegative, then adds multiplicative Gaussian noise and later describes the all-join corner as stable. The printed stochastic equations themselves contradict those interpretations. Fresh searches of the article title/DOI plus correction and erratum terms, and a Resultary semantic search on the source-specific defect, found no published correction or equivalent diagnosis.

## value

PASS

The defect affects both the probabilistic state-space interpretation and the paper's headline stochastic-stability conclusion. Exhibiting the exact invariant-face escape mechanism and the nonzero all-join drift is a substantive source correction, not a cosmetic notation complaint or routine numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
