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

For any two characters, factoring the \(2\times2\) restriction determinant leaves the nonzero factor \(\psi(d_j)-1\), so one quotient character outside all annihilators is necessary and sufficient. Each annihilator has size \(|G|/o(d_j)\le|G|/p\) and all contain the trivial character; the overlap-aware union estimate is strictly below \(|G|\) for \(m\le p\). In \(\mathbb Z_p^2\), the annihilators of representatives of the \(p+1\) directions are exactly all dual lines and cover the dual. The actual verifier exhaustively checks the determinant equivalence and small-group threshold examples.

## originality

PASS

The primary source explicitly leaves the pair-of-equal-size-sets question unresolved. Its simultaneous-basis section gives three two-point sets only for \(\mathbb Z_2^2\), and for general prime \(p\) its obstruction uses \(p\)-point subgroups, not arbitrary two-point sets. Classical subgroup-covering theory becomes relevant only after the new determinant reduction.

## value

PASS

The theorem completely classifies a natural two-point regime, resolves the cardinality-two case of an explicit open question, and supplies a sharp uniform family-size threshold for every prime. That is a reusable structural result, not a routine isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
