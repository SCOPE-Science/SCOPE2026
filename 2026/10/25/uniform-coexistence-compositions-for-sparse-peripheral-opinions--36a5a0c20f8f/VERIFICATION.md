---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Counting productive hub/leaf pairs gives P(x±e_i)=x_i/(2s), with s=sum leaf counts; all idle steps can be ignored for absorption probabilities. h(x)=∏x_i is harmonic for the chain, vanishes if any leaf is extinct, and is positive at fully surviving terminals. Doob h-transform gives probabilities (x_i+1)/(2s) up and (x_i−1)/(2s) down. Their total up/down probabilities (s+d)/(2s) and (s−d)/(2s) depend only on s; with t_i=x_i−1, the conditional leaf composition under any realized total-size trajectory is Dirichlet-multinomial with shape 2 for each type: upward steps are Pólya additions of weight t_i+2; downward steps uniformly delete among t_i tokens. At size n, h-transform probability is C∏ell_i, and dividing by h(ell)=∏ell_i gives identical original probability C=(n−d)!(2d−1)!/(n+d−1)!. The chain is finite and a.s. absorbs at an extinction or s=n; under the transform s hits n a.s. Counting positive compositions yields full coexistence and the fixed-d asymptotic and simplex weak limit. Independent exact-rational absorbing-chain solves agree for six small cases, e.g. d=3,n=7 each of 15 compositions 1/126; finite computations corroborate only.

## originality

PASS

Best-of-knowledge PASS limited to the exact all-leaf terminal composition law and its asymptotics. Berenbrink–Götte–Hoefer–Koglin introduce EdgeVOG and study single opinion survival / number survivors and convergence; a full joint terminal composition is not stated in inspected indexed sections. Generic Doob transformations and urn deletion consistency are established and not claimed original. Full 2026 EdgeVOG preprint access failed; stronger hidden coverage is a real risk.

## value

PASS

The probability that every peripheral opinion survives is a natural rare-event statistic missing from individual survival estimates. The theorem determines the entire labelled composition law, reveals exact unconditioned uniformity independent of balance, and supplies a sharp n^(-d) coexistence probability and conditional Dirichlet law. This gives a meaningful complete result for a specified natural star compatibility model rather than an arbitrary small sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
