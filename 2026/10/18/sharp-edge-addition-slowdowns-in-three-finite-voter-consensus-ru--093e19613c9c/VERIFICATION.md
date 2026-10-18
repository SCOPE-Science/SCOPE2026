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

# Verification details

The included `verify_exact.py` reproduces every reported number using only Python 3 standard-library exact rational arithmetic. Run `python3 verify_exact.py` and confirm the final PASS line, its six four-vertex comparison lines, and the five-vertex link-update witness. Each Markov-chain transition is constructed from oriented edges, including equal-opinion nontransitions in the diagonal. The routine solves all \(2^n-2\) transient first-step equations with fractions rather than floating-point approximations.

The program enumerates every labelled graph on two, three and four vertices by edge masks; discards disconnected source graphs; marks each missing edge; and canonicalizes the marked graph under every vertex permutation. It checks that all six manually named four-vertex cases exhaust the canonical orbit set. The script computes the five-vertex example but does not enumerate every five-vertex source graph. No infinite-graph implication is asserted.

Checks also included separate exact symbolic matrix elimination against the tabulated rational values. These are computational cross-checks, not external or independent audit. The value and originality assessment is restricted to the stated fair i.i.d. initial law and attempted-update normalization, and the named primary literature; an unlocated equivalent finite census remains a residual literature risk.
