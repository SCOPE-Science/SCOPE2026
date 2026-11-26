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

Every trigram occurs at exactly one of the 27 linear starts. A nine-element hitting set must cover exactly three starts per mark without overlap, forcing marks 2,5,…,26. Hitting all such windows hits every occurrence of every longer factor, so the only further tests are the three letters and nine digrams. I independently enumerated all 2·6^8 local exit orders of the Euler graph with 000 fixed first. Every complete tour uniquely determines and is reproduced by its orders. All ten-subsets were filtered by explicit bit-mask coverage of the 27 starts, yielding 275, and each of the 27 linear cuts per tour was tested directly, without the source's residue shortcut. The seven disjoint chunks in /workspace/audit-evidence/2/census.py and totals.txt give 373248 cycles, 8274096 cuts of size nine, 1803600 of size ten and none unresolved; the cycle histogram is 0:1632, 9:19968, 18:155568, 27:196080. Direct all-factor checking confirms the displayed witness's ten marks; all its cuts fail nine. A second independent symbol-recursion run agreed. The source C++ was inspected but not executed, and no claim for other orders follows.

## originality

PASS

An unfavorable cut and examples of favorable recuts were known. The inspected sources do not settle which labeled ternary order-three cycles lack a favorable cut at every rotation, or give the 9/10 counts and distribution. The result answers the universal-cycle question negatively, not the separate existence question.

## value

PASS

The finite domain is the natural small nonbinary case of a published universal unfolding question. The verified all-rotation obstruction gives a clean counterexample, and the complete labeled distribution quantifies how often cut selection can or cannot recover the lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
