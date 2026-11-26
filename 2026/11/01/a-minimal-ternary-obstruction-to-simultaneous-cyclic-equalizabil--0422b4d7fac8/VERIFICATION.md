---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Translate any distance-two pair of rotations so that one word is z. Equal Parikh vectors make its two mismatches a swap. If two shifts had different swap pairs, take a symbol e involved only in the first. For its indicator f, D=R_s f−f has a unique +1, while R_t f=f for the other nonzero shift. Commutation gives R_t D=D, impossible because a nonzero cyclic translation fixes no coordinate. This holds even when z is periodic. In 012,021,120 the successive pairs swap {1,2} and {0,1}; common insertions add identical columns and therefore preserve these two mismatch pairs, making a common orbit impossible at any insertion length. The same invariant gives every length at least three by common padding. Length zero, one and two are trivial within each Parikh class; the frozen two-word boundary is exactly the published theorem for arbitrary finite alphabets. No binary three-word conclusion is needed.

## originality

PASS

Pass applies to the distinct equalizability finding: a minimum-size ternary obstruction to common-insertion equalization and its extension to all lengths. The rotation-rigidity lemma in isolation is not a new structural consequence: it follows from Gabrić's earlier Lemma 14. The work uses the exchange-pair invariant across unchanged mismatch columns to connect that structure to the separate open multiple-word insertion problem.

## value

PASS

This gives a sharp negative answer to a stated extension of the pair theorem: equal symbol counts cease to be sufficient already at family size three and ternary length three, no matter how large the permitted identical insertions are. The two aligned swaps give a usable structural obstruction beyond the single example. Novelty of the supporting orbit lemma is not needed for that contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
