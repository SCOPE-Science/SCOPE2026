---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Every monotone map [a]×[b] -> C3 is encoded by weakly decreasing sequences of counts ell_i of 0 labels and u_i of labels <=1, 0<=ell_i<=u_i<=b. Surjectivity/endpoints require ell_1>0, u_a<b; the upward-back condition for each maximal 0 is exactly that an immediate right or lower cover is labelled 1, i.e. u_i>ell_i or (i<a and u_{i+1}>=ell_i). Row comparison conditions are purely weak-order relations of the 2a boundaries; standardizing m distinct interior ranks and selecting m of b-1 positions gives F_a(b)=sum c_{a,m}binom(b-1,m). The top m=2a strict-interlacing configurations are Catalan ballot words, giving coefficient Cat_a, degree 2a and leading b^{2a}/(a!(a+1)!). MacMahon unrestricted 3-colour grid count has the same top term, so fraction of surjective order-preserving maps satisfying back tends 1 for fixed a. Two-row weak-order enumeration gives c=(0,3,9,7,2), F_2=(b-1)(b^3+5b²+10b-12)/12, and failure b(b²-1)/3. Fresh independent direct world-map enumeration verified F_2(1..6)=(0,3,15,43,96,185) and all weak-rank c_{2,m} without using the original verifier. These finite checks do not prove all a,b; proof normal form does.

## originality

PASS

The Kripke bounded-morphism condition is classical; the unrestricted plane-partition count is MacMahon, and some order-polynomial structure is standard. The complete back-conditioned positive-binomial pattern census, Catalan top coefficient and explicit first branching-width exclusion count are a distinct statement not supplied by the inspected general sources. Qualified best-of-knowledge originality.

## value

PASS

The exact count is a natural complete enumeration of surjective bounded morphisms of grid Kripke frames, with nonnegative binomial structure and Catalan top growth; the two-row complete failure count quantifies the first nonchain branching case. This solves a motivated object/invariant combination beyond routine substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
