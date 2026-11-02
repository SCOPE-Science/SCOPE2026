---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For g,h in UT4(Fq) with six coordinates each, direct group multiplication yields u=aD-Ad, v=dF-Df, w=aE+bF-Ae-Bf-(f+F)u; c,C are free and contribute q^2. For fixed u,v the outer sextuples (a,d,f,A,D,F) number S=q^2(q^2-1)+q^4*1_{u=v=0}, since (d,D)!=0 gives q choices each for (a,A),(f,F), otherwise u=v=0 and four free. The linear w constraint in (b,e,B,E) is rank one except when a=A=f=F=0, with q^2 exceptional (d,D) at u=v=0 contributing q^8 only for w=0. Thus N=q^5(S-q^2*1_{u=v=0})+q^8*1_{u=v=w=0}, giving exactly the stated three levels q^7(q^2-1), 2q^7(q^2-1), and 2q^7(q^2-1)+q^8. Sum over q^3 derived targets gives q^12. Identity fiber divided by q^12 is cp=(2q^2+q-2)/q^5; multiplying by |G| gives k=2q^3+q^2-2q. Independently enumerated all 4096 ordered UT4(F2) pairs by direct group law; each of six noncentral targets has 384 pairs, central nonidentity has 768, identity 1024. Formula holds for any prime-power characteristic by field counting. No claim for UT5 or associative commutators.

## originality

PASS

Class numbers and commutator identities for UT4 and broader pattern groups are longstanding; the numerical k and cp are not claimed as independently new, and are consequences of the identity fiber. The additional target-refined three-stratum distribution of a two-input group commutator over every Fq is not stated in inspected Marberg superclass or Bardakov–Vesnin–Yadav class-preserving-automorphism primary texts. Any older exact character sum for word maps could imply the whole formula even without matching titles, an explicit residual risk. Hołubowski–Stepanov full article was not read.

## value

PASS

The fiber function of the commutator word is a natural complete conjugation-invariant distribution measuring how often each derived-subgroup element is represented as a single commutator. Its exact nonuniform three-level stratification works uniformly through characteristic two, sharper than commutator surjectivity or commuting probability alone and potentially reusable for comparison of finite nilpotent groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
