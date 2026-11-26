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

All root-return words are concatenations of codewords. A common length divisor d>1 would require a root-reset word w to have d dividing |w| and, by starting one level down, d dividing |w|+1. Completeness makes each literal transition defined. Synchronizing to one state is equivalent to synchronizing to the root, since following zeros from any fixed state reaches its first leaf and resets. A DFA synchronizes iff every distinct pair can merge: repeatedly merge a pair in the current image until it is a singleton. For independent enumeration I used preorder branch/leaf words, with k−1 internal symbols and k leaves, starting with one pending slot, adding one for each branch and subtracting one for each leaf. The slot count must stay positive before the end and finish at zero; these words decode bijectively into ordered full trees. For each pair I searched its forward orbit for a diagonal. The exact totals for k=2,…,9 were (1,2,5,14,42,132,429,1430), nonsynchronizing totals (0,0,1,0,0,4,1,4), and coprime nonsynchronizing totals (0,0,0,0,0,0,0,4). The resulting four sorted word lists match C1–C4 exactly. Their closed distinct-pair orbits have sizes 6,12,12,6, respectively, and each has length multiplicities 1,4,4 at lengths 2,3,4. Direct complementation gives C1↔C4 and C2↔C3. The frozen scripts and JSON were inspected, not executed.

## originality

PASS

The distinct claim is the least leaf count across all finite full binary trees satisfying the gcd-one obstruction, together with exactly four labeled examples at that least size. Prior small-cardinality results and general reset-word theory give partial coverage, and a distinct later indexed record covers a substantially overlapping height-restricted universe. None of the inspected earlier statements supplies the exact first-size list and cutoff.

## value

PASS

The natural gcd condition separates synchronization from the simpler periodic obstruction; the first counterexamples show how early that condition fails to suffice and the exact count determines every labeled first witness. This is a useful benchmark for structural length criteria or decoder synchronization tests, with finite pair-orbit certificates that exhibit the obstruction directly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
