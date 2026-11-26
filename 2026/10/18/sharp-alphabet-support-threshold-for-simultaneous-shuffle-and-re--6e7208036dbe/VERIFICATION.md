---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Use the two witness partitions independently. In the ordinary matching both minima and maxima of the paired positions increase in pair-rank, excluding a nested pair. In the reverse matching paired subsequence ranks sum to n+1. If both endpoints were in one half, their prefixes or suffixes would require n+1 distinct positions there. With left ends partitioned by witness side, the right ends decrease on each side, so no increasing triple exists. Shared edges cross the midpoint and have increasing right ends by non-nesting, hence there are at most two. In the two-colored multigraph, a shared pair yields a size-two component and every other alternating cycle has at least four positions. Thus c≤floor((n+h)/2)≤floor(n/2)+1, and equality labels on edges give support at most c. For n=1 the argument allows the one shared edge. The explicit word aPaP with P a palindrome on the maximum number of letters uses both ordinary equal halves and reverse subsequences aP,Pa, giving equality for all n. Merging symbols proves exact full-support feasibility for smaller q, and injecting labels in the maximum-support pattern proves the lower counting exponent; finitely many equality patterns prove the upper one. For an alphabet fixed too small for the first unrestricted maximum, the actual maximum is min(q,floor(n/2)+1), as the relabeling argument shows. Independent replay: python3 -B /workspace/branches/reproduce_frozen_checks.py 4 directly enumerated equality partitions with even multiplicities for n=1..5 (1, 4, 31, 379, 6556 cases) and tested bipartitions without relying on the matching encoding, finding the claimed maxima 1,2,2,3,3. Uploaded checker and recorded support were inspected, not executed. The proof, not the replay, handles arbitrary n.

## originality

PASS

The known separate matching encodings and separate asymptotic counts are credited. What survives comparison is the coupled bound on shared edges, the sharp component/support ceiling for simultaneous membership, and its full-support and counting consequences. In the relevant retrieved primary passages and indexed records, no equivalent or stronger mixed-family classification was found. This is a bounded comparison, not a priority guarantee.

## value

PASS

This asks a natural compatibility question about two standard word languages, and resolves it for every length rather than a finite census. The exact drop in admissible letters and in the counting exponent, with a sharp full-support threshold and an independent structural explanation via shared edges, are useful even without the exact joint enumerator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
