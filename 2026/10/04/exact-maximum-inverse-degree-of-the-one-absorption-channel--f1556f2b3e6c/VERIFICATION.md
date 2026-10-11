---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Every one-absorption parent is either an ordinary one-symbol insertion supersequence of the received word or a genuine split of one received symbol into two symbols neither equal to that received symbol. The insertion sphere has exactly \(q+(n-1)(q-1)\) distinct words by the first-difference encoding. For a received symbol \(c<q-1\), the number of genuine ordered splits is \(\max(c-1,0)\); for the saturated symbol \(q-1\), it is \(\binom{q-1}{2}\). This gives the universal upper bound \(q+(n-1)\binom q2\). For the all-saturated received word, every insertion is a parent and every genuine split at every position is distinct from all insertions and from all other genuine splits, attaining the bound. A fresh independent exhaustive forward-channel check for every \(2\le q\le5\) and \(2\le n\le5\) reproduced the formula exactly; this finite check corroborates rather than replaces the universal counting proof.

## originality

PASS

Ye--Elishco define the same absorption channel and study forward one-error balls, code constructions and a restricted hypergraph argument; their conclusion explicitly treats better estimates of the forward one-absorption ball as a future ingredient. The audited invariant fixes the received word and counts all possible parents, which is the opposite incidence degree. Targeted Resultary and literature searches for inverse balls, preimages, list size and received-word degree found no matching theorem. The 2024 Nguyen--Cai--Quek--Immink follow-up advertises improved redundancy constructions rather than an inverse-degree formula. Its complete text was not inspected in this run, so that source remains an access risk rather than negative evidence.

## value

PASS

Worst-case incoming degree is a natural channel invariant measuring exact ambiguity/list size of a received word and is complementary to the forward-ball quantities used in coding bounds. The theorem is uniform in alphabet size and block length and identifies an explicit extremal received word.

The dated certificate retains the supplied scientific assessment, sources and limitations.
