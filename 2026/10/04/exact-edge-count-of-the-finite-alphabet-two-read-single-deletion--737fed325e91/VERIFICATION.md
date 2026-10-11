---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Cai--Kiah--Nguyen--Yaakobi prove that two distinct equal-length words have two common single-deletion descendants exactly when they are Type-A-confusable: they agree outside one interval and inside it are opposite phases of an alternating word on two symbols. For each edge, the first and last differing positions therefore determine a unique interval of length \(L\ge2\); choose its start in \(n-L+1\) ways, the outside word in \(q^{n-L}\) ways, and the unordered symbol pair in \(\binom q2\) ways. The two phases form one unordered edge, so no additional factor occurs. Summing gives the first formula and a finite geometric-derivative calculation gives the closed form and average degree. Independently, direct deletion-ball enumeration matched the formula for 12 \((q,n)\) cases including binary \(n\le7\), ternary \(n\le4\), and selected quaternary cases; the package checker covers a larger grid.

## originality

PASS

The 2020 sequence-reconstruction paper gives the exact Type-A characterization of when the single-deletion balls of a prescribed pair intersect in two words, but it does not aggregate that pair classification into the all-\(q,n\) edge count, average degree, or unique-interval enumeration. Targeted Resultary and web searches for the graph invariant and its closed form found no prior table or implication-equivalent theorem.

## value

PASS

The graph is the natural confusability object for reconstruction from two distinct deletion reads, and its independent sets are exactly codes avoiding this two-read ambiguity. The theorem gives an all-alphabet, all-length density invariant plus a canonical representation of every edge, providing reusable structural input for extremal, probabilistic, and spectral analysis rather than a small isolated count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
