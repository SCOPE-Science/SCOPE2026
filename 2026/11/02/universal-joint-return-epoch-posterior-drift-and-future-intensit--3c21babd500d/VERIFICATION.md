---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For fixed a,b>0, de Finetti mixing gives Beta(a,b) latent p and conditional return probability r(p)=2min(p,1-p)=1-U. Thus N|p is geometric in positive-time return count, P(N>=k|p)=(1-U)^k. Exact beta posterior reweighting gives kU->Exp(1), sign asymptotically fair, and by Scheffe total variation of k(2p-1) to centered Laplace. Conditional future R=N-k is geometric with parameter U, hence UR->independent Exp(1). Defective first-return generating function 1-sqrt(1-4p(1-p)z^2) gives [F_p(e^-s/k^2)/F_p(1)]^k -> exp(x-sqrt(x^2+2s)) with U=x/k; post-k excursions are independent of future returns conditional on p. Mixing x~Exp(1) produces T=1/(2 Exp(1)), CDF exp(-1/(2t)). Exact a=b=1 joint survival formula follows beta integral. Independently recomputed finite posterior integrals and numeric Laplace convergence for k=100,1000 and inspected rational/exhaustive source checker.py. Infinite-limit statements are justified by uniform compact expansion/tightness, not those finite tests.

## originality

PASS

Best-of-knowledge comparison against stronger and equivalent claims, not titles alone; primary texts and known antecedents acknowledged. The joint theorem requires mixing de Finetti with k-fold defective first-return transforms and conditional geometric future returns; no direct prior implication was established in inspected full text. Unresolved historical-priority possibilities are explicitly retained; unsuccessful searches are not proof of novelty.

## value

PASS

The simultaneous limiting latent drift, k-th return epoch and future return count answers a natural rare conditioning question for exchangeable reinforcement and clarifies the dependence structure between posterior drift and Brownian first-passage time. The exact finite balanced survival formula is a useful consistency check; standalone 1/k tie intensity and balanced time marginals are already known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
