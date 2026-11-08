---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For 1<=a<=b and 1<=n<=a+b with possibly different monotone normalized valuations, prove three complementary ranges. For n<=a, Bei et al. Proposition 4.8 applies; n=1 is immediate. For n>=b, t=a+b-n<=a, after each agent chooses her best available singleton, the x leftover L vertices fit among b-y chosen R vertices and the y leftover R among a-x chosen L: both inequalities follow from t<=a<=b. Attach each leftover to a different opposite-side chosen singleton. Every bundle is a singleton or an edge, and each agent i may remove the chosen vertex of j, leaving a leftover that was available at i's pick, so even EF1_outer follows without additivity. For a<n<b, an R-only singleton is forced; unit additive envy implies every other bundle size<=2, at most a size-2 bundles, and n+a<a+b is a contradiction. Independently checked all residual cardinality inequalities in 36,769 cases; no finite check is used as an infinite proof.

## originality

PASS

PASS with priority qualification. Existing Bei et al. gives the low-agent band and Chen–Zwicker gives a generic cutset obstruction/limited high-n consequences. Neither inspected result supplies a high-agent construction for all n>=b at unbounded a under arbitrary heterogeneous monotone valuations. A highly relevant 2026 paper on EF1_outer and graph classes could implicitly contain such a result; only its abstract was accessible, so that remains a substantial explicit priority risk.

## value

PASS

The universal n-spectrum of connected fair division is a natural structural parameter, and this result resolves a possibly unbounded forbidden interval using an EF1_outer construction under the strongest relevant arbitrary monotone heterogeneous model; it is not merely a table of small additive examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
