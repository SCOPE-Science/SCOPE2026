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

For each word the descendant obtained by deleting marker 1 has precisely one marker 2 at a coordinate v, and vice versa with coordinate u. Any code has at most k=n-1 distinct singleton-marker outputs. At equality u and v separately index every position, inducing v=pi(u). If u<v, the original marker positions are (u,v+1) and orientation +; if u>v they are (u+1,v) with orientation -, with both signs possible for u=v. The zero-deletion descendants for + are (u-1,v),(u,v),(u,v+1) under respective exact feasibility conditions; for - are (u,v-1),(u,v),(u+1,v). Comparing distinct rows/columns shows overlap exactly for labels (u,v),(u+1,v+1) with the same sign. Rising successions off the fixed-point diagonal force the same sign and are excluded; along fixed-point runs the choices alternate. This proves the full classification and 2^{number of fixed-point runs} count. Alternating adjacent markers realize k words for all k>=1. Independently reconstructed direct descendant conflicts for every signed permutation k<=7 and enumerated all maximum k-subsets for n=2..6; matched B_k and direct no-collision tests. These finite checks are corroboration, not proof.

## originality

PASS

The novel portion assessed is the complete classification and labeled enumeration of all optimal fixed-composition ternary deletion codebooks for every n, not the elementary singleton-output upper bound or classical permutation succession statistics.

## value

PASS

The thin (n-2,1,1) ternary layer is a natural deletion-channel model with two distinguishable markers. Exact classification of all capacity-achieving codebooks, rather than only the easy size n-1, gives an intrinsic parameterization and enumeration that can be used to impose additional design constraints. The orientation-dependent fixed-point-run obstruction is a nontrivial structural coding fact across infinitely many lengths, not arbitrary enumeration of a tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
