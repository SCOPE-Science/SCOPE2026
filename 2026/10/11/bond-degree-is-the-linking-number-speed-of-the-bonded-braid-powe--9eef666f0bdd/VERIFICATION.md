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

The primary theorem was checked at the generator level: braid generators are unchanged, each overpassing bond maps to \(A_{ij}^{p}\), and each threaded bond maps to a pure conjugate of that power. The defining relations preserve bond degree.

The proof then uses the Artin presentation of \(P_n\). In its abelianization the classes \([A_{ij}]\) form the standard free basis; under closure they are exactly the pairwise-linking coordinates. Conjugation by pure braids vanishes in abelianization, while conjugation by an arbitrary braid transports a basis vector only by the induced permutation of strand labels. Consequently a word with \(d_B\) bonds contributes \(p\) times a sum of exactly \(d_B\) standard basis vectors. This proves both the vector formula and its coordinate-sum formula.

No computer enumeration or finite-data extrapolation is part of the proof. The verification does not claim distinction after arbitrary component-orientation reversal or a complete classification of the closures.
