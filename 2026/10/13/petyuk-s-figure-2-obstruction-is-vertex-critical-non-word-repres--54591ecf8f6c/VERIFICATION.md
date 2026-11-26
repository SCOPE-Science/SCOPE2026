---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reconstructed the overlap graph by shifting each word and appending ternary digits before forgetting direction, obtaining 38 distinct simple edges. Under technical labels 1 through 17 in the displayed order, all 38 edges agree with the union of cycle/shortcut edges in Petyuk v2, Appendix proof line 1, p. 7 (and 1=102 and 2=210 agree with p. 4). This cross-check uses the published proof text, not a direct visual reading of all Figure-2 word labels. Theorem 5 formally states non-word-representability of S(3,k); its Appendix proves the Figure-2 obstruction itself is non-word-representable. I checked the precise graph against that premise rather than independently re-proving the negative result. An independent replay (branches/independent_small_replays.py petyuk, with the frozen certificate.json as data) checked all 17 distinct omissions and verified each order was a permutation. Orienting all edges forward gives acyclicity. Across all deletions the replay visited 2391 nontrivial directed paths; none of length at least three edges had adjacent endpoints, so there is no shortcut. Paths of length one or two with adjacent endpoints already form a clique in a forward orientation. The semi-transitive characterization then gives word-representability of every deletion. For any proper induced subgraph first remove an omitted vertex and restrict the word or orientation. No inference to ambient minimum order is made.

## originality

PASS

The paper explicitly poses the stronger ambient vertex-count question but supplies the negative witness only for the full obstruction, not positive witnesses for the deletions. The closest accessible follow-up treats other structured subgraphs; the strongest catalogue match concerns S(4,3), not this obstruction. No equivalent or stronger established statement was identified in the inspected sources.

## value

PASS

The object is the obstruction used to prove a published theorem, not an arbitrary slice. The exact positive deletion certificates settle a natural way of trying to shorten it and prove that any smaller ambient obstruction must use vertices outside this set. This is a useful partial advance on the expressly posed minimum-order question, without claiming to solve it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
