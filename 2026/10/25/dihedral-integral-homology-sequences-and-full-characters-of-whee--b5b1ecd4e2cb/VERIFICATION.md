---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Every matching of the ordinary wheel W_{n+1} has zero or one spoke, so X_n decomposes as R_n=Ind(C_n) plus n spoke cones u_i*Ind(P_{n−2}). Relative augmented chains decompose equivariantly by spoke and give a long exact sequence. Standard integral path and cycle independence-complex homotopy formulas produce exactly three residue cases: n=3k rim H~_{k−1}=Z² unchanged; n=3k+1 a kernel H~_{k−1}(R_n)⊗J_n in degree k and rank n−1; n=3k+2 a rank-1 rim injection with rank-n induced spoke-link quotient in an integral D_n exact sequence, with no asserted integral splitting. Reflection reversal on Ind(P_{3k}) has degree epsilon_k=(−1)^{k(k−1)/2}. Fixed orbit-independent-set path/cycle polynomial recurrence p_j=p_{j−1}−p_{j−2} yields explicit full rotation and both reflection character classes; rational splitting in third case uses Maschke only. Independently enumerated every matching face and signed dihedral Lefschetz trace for each of 204 elements across n=3..14 and verified rank/character formulas. The all-n proof uses the relative-chain exact sequence, not finite extrapolation.

## originality

PASS

Best-of-knowledge: Vega already proves nonequivariant homotopy types of ordinary wheel matching complexes and the published dihedral cycle result supplies R_n rim characters. Neither determines the connecting maps of the spoke-cone long exact sequence or the integral D_n extension and full characters. A superficially matching Resultary record about wheel discrete-Morse complexes is about a different directed-forest complex on incidences, not ordinary matchings; its huge dimension k^3 cannot imply this theorem.

## value

PASS

Wheel graphs are a natural infinite family for matching complexes, and their rim dihedral symmetry provides a canonical equivariant invariant. The integral non-split-allowed extension and full all-n characters fill information left open by known nonequivariant wedge classifications, including parity-sensitive reflection behavior and exact orbit-space rational consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
