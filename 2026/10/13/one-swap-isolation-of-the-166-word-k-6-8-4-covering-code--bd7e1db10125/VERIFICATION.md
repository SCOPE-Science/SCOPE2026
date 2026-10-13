---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

Run:

`python3 artifacts/verify.py`

The verifier contains the exact published 166-word representative and uses only exact integer Hamming distances. It checks:

- all \(6^8=1679616\) ambient words are covered within radius \(4\);
- the radius-\(4\) ball size is \(51491\);
- the full coverage multiplicity histogram is exact;
- there are exactly \(7173\) singly covered words;
- every codeword has a nonempty private region, of size from \(8\) through \(105\);
- after each of the \(166\) possible single deletions, every newly uncovered word has nearest remaining-code distance exactly \(5\);
- for each deletion, every possible one-word repair is exhausted by intersecting the radius-\(4\) balls centered at its private words;
- \(165\) repair intersections have size \(1\), one has size \(2\), and the sole nontrivial repair is \(\mathtt{51004501}\mapsto\mathtt{51004441}\);
- a direct recount after that exceptional replacement still covers the entire ambient space within radius \(4\).

The replay used for this package ended with:

`VERIFY_OK`

The finite checker proves only the stated representative-specific claims. It does not certify global optimality of \(166\), equivalence classes of all covers, or any multiword-exchange statement.
