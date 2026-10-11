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

For \(N_a=15\cdot2^a\), the displayed \(P_i\) and \(Q_i\) exhaust the complementary divisor pairs. Every proposed witness selects whole pairs, so complement closure is automatic. The five residue classes modulo 5 reduce to exact geometric sums with ratio 32 and produce respectively the required total \(30\cdot2^a\); the listed small exceptions cover all values excluded by the residue-class ranges. An independent reimplementation of the five selection rules checked every \(a\) from 2 through 52 exactly and found the selected pair-sum equal to \(30\cdot2^a\) in every case. The finite replay is corroborative; the symbolic geometric identities establish all exponents.

## originality

PASS

The 2023 primary source explicitly lists the first nine dyadic multiples and asks as Question 38 whether \(60\cdot2^n\) is strongly pseudoperfect for every \(n\ge0\). The complete September 2026 Wang--Zelinsky paper was read through all 17 pages using authorized access after public full-text retrieval failed. Its Theorem 5 concerns powers of a strongly pseudoperfect number under an extra representation hypothesis, and Theorem 9 constructs a different linked \(pq2^a\) family; its open-questions and data sections do not state the fixed-odd-part dyadic-60 theorem. Current OEIS A334405 lists the sequence and cites both papers but does not state all dyadic multiples of 60. Fresh Resultary search self-matches the submitted record and finds no older covering theorem.

## value

PASS

The theorem answers an explicit infinite-family question by uniform constructions in all five exponent residue classes, replacing finitely many observations with exact complement-pair certificates for every exponent. This is a natural complete family result with reusable arithmetic structure, not a table extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
