---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For q=2 all admissible noises are the two alternating complement words, so two distinct input words have intersecting output sets iff they are bitwise complements. Thus 2^(n−1) disjoint confusability edges imply M_2(n)=2^(n−1) and exactly 2^(2^(n−1)) maximal transversals. For q≥3, for every input difference d recursively choose z'_(i+1) outside the at most two values z'_i and z'_i+d_i−d_(i+1), and set z_(i+1)=d_(i+1)+z'_(i+1); this realizes any d as two proper-colouring noise differences, making the graph complete. Holds for all n≥1, q≥3 including q=3 boundary. Independent exhaustive difference-set checks covered q=2..5 and n=1..4; symbolic recursion proves the universal statement.

## originality

PASS

The q≥3 impossibility is a quick application of general prior confusability principles after proving specific difference coverage. The finite-block q=2 extremizer classification and 2^(2^(n−1)) labeled optimal codebooks, together with the exact sharp q=2/q≥3 split, are an explicit all-n classification not supplied by the inspected general-capacity references. Priority is best-of-knowledge with low but nonzero risk of an earlier elementary coding lemma.

## value

PASS

Finite-block zero-error coding for a fixed finite-state adversarial noise constraint is a natural operational invariant, and the q=2-to-q=3 jump from 2^(n−1) reliable messages to one is a sharp alphabet threshold. Counting all 2^(2^(n−1)) maximum binary transversals, not just an asymptotic capacity, provides a fully solved benchmark for exact finite-block code design. The argument is elementary but the exact self-contained all-length classification is motivated by channel confusability, rather than an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
