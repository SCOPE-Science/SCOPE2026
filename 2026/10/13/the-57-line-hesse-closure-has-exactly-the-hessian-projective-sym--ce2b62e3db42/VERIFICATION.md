---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Exact rational computations in Q(eps), eps^2+eps+1=0, from all 57 printed line forms independently reproduced the 453 singular points with multiplicity distribution n2=252,n3=108,n4=72,n8=21. All 1596 line pairs were accounted for; incidence with 21 eightfold points gave profile 12 lines at five, nine at four and 36 at two. Exact projective normalization matched the 12 lines with x,y,z axes plus nine x+eps^i y+eps^j z=0. A projectivity preserving H57 preserves singular multiplicities and so the original Hesse 12, proving Stab(H57)<=Stab(H)=G216. Covariance of the incidence-based Lambda_(2,2) operation gives reverse inclusion. The known Hessian group action is verified against Artebani–Dolgachev Proposition4.1, and the combinatorial recovery is exhaustively exact (not a sample).

## originality

PASS

Pokora–Roulleau Theorem A constructs and counts H57 but does not state its exact projective stabilizer or the discriminating 12+9+36 eightfold-incidence profile. Artebani–Dolgachev supplies the old G216 symmetry of the original Hesse arrangement; the structural new input is intrinsic recovery of H inside H57 preventing extra symmetries. An earlier arrangement classification could give the same stabilizer under a different name.

## value

PASS

The full projective symmetry group of a canonical 57-line incidence closure is a natural exact invariant; proving its action creates no extra projective symmetries requires the substantive intrinsic Hesse-recovery lemma, useful for arrangement symmetry and rigidity investigations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
