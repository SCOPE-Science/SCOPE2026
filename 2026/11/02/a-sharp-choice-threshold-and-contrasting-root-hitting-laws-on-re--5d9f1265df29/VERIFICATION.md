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

For complete rooted b-ary tree, independent with-replacement offers k, parent appears with p=1−(b/(b+1))^k. Bellman solution H_i increases with depth since differences Δ_h=1, Δ_i=(1+q Δ_{i+1})/p>0; thus selecting parent whenever offered is optimal among arbitrary history-dependent policies (bounded stopped submartingale). Exact recurrence gives E T_h=h/(p−q)−2pq(1−(q/p)^h)/(p−q)². Coprimality rules out integer p=q and gives kcrit=floor(log(2)/log(1+1/b))+1. Independently inverted the exact radial systems for b,k,h=(2,2,4),(3,2,5),(2,1,5),(7,3,5), all exact rational formula matches. When p>q, decompose into independent downward passage times, couple reflecting-to-unbounded walk with exponentially small boundary errors and apply Lyapunov CLT: variance 4pq/(p−q)^3 per unit h. When q>p, rare leaf-return excursions have success s_h=(q/p−1)/((q/p)^h−1), bounded second moments, and renewal Laplace transform gives Exp(1) normalized by its mean, with correct exponential mean constant. All stochastic limits fix b,k and let h→∞, not simultaneous growth. Finite checks supplement the rigorous passage/renewal proof.

## originality

PASS

Qualified PASS for the complete all-integer offer threshold together with exact finite-height optimal mean and paired Gaussian/exponential depth-limit laws, not for the previously known power-of-choices model, outward drift on infinite regular trees, or classical gambler ruin.

## value

PASS

PASS: optimal local choices on regular trees provide a natural benchmark for target search. The exact integer number of offers separates O(h) from exponential-in-h expected time, and the normal versus exponential laws expose distinct fluctuations. This full structural phase classification is not merely a small numerical case or a restatement of general cover bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
