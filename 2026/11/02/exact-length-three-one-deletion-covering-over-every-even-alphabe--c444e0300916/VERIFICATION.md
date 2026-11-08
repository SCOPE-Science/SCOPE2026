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

Any length-three word has at most three distinct one-deletion outputs, giving ceil(q²/3) lower bound. The ten explicit optimal finite seed covers (q=2,4,6,8,10,12,14,16,20,22) were fetched from the exact pinned data blob and independently enumerated, checking all q² ordered target pairs and codeword counts 2,6,12,22,34,48,66,86,134,162. For all remaining even q, published Colbourn–Hoffman–Rees 3-GDD existence (restated as Chang–Chee–Zhou Lemma 1.1) gives types 6^t u^1, t>=3, u=0,8,10. Insert local optimal 6,8,10 seed codes and two opposite words per transversal triple; every cross-group pair covered both directions. Formula sum ceil(g_i²/3)+2B=ceil(q²/3) with B=(q²−sum g_i²)/6 is exact, and these sizes exhaust all even q apart from the checked seeds. Finite checks are certificates for seeds, infinite existence comes from published theorem.

## originality

PASS

An indexed related exact theorem proves the same formula for ODD q>=3 only, not even alphabets. Xie–Sun–Ge 2026 Section V gives general q-ary deletion covering bounds and asymptotic construction but not the exact fixed-length-three all-even optimum. Group-divisible design existence is established, but combining it with directed-edge/triple deletion-ball certificates and finite sharp seeds is a nontrivial bridge. This completes a natural parity gap.

## value

PASS

The exact minimum size of a single-deletion covering code is a natural information-theory invariant. Covering every even alphabet with a sharp lower-bound construction settles the remaining parity family and supplies explicit finite certificates plus a general combinatorial design lift, rather than a tiny computational example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
