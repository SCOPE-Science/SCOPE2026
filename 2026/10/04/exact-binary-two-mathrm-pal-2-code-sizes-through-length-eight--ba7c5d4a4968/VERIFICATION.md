---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

A length-two PAL duplication of ab inserts ba after ab, and every second operation is allowed to overlap newly inserted symbols. The two-step descendant confusability graph is exact by direct set intersection. I fetched the actual source certificate.json and independently regenerated descendant sets for every binary word of each length n=2,...,8 with a fresh JavaScript implementation. For EACH n, the stored size-M witness consisted of pairwise nonconfusable words and the stored M conflict cliques partitioned all 2^n source words, with pairwise confusability in every clique. Both directions independently passed for M=4,8,14,20,28,42,66; hence this is an exact matching independence-number lower and upper certificate, not a solver log. Current full primary paper establishes exact-two/at-most-two equivalence and even-length PAL/RC conjugacy, permitting the same values for RC2.

## originality

PASS

Zabokritskiy’s 33-page primary paper defines the exact same sequential PAL/RC channel and its confusability graph, proves even-length conjugacy, gives general sphere and code bounds, and explicitly retains binary two-error questions; it does not state the exact finite length-2 code table through n=8 in its principal theorems or appendix. Exact PAL/RC equality comes from that source, not novelty. The distinct result is exact graph independence numbers certified from new finite cliques/witnesses.

## value

PASS

The two-error binary PAL2 channel is a natural explicitly motivated finite-error coding problem with a nontrivial confusability graph and open general optimal redundancy bounds. Matching lower code witnesses and upper clique covers through the first nontrivial lengths provide independent exact benchmark invariants, not arbitrary list entries. Finite scope n≤8 is stated without extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
