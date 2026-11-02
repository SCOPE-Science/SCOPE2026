---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Fact 2 of Beigi–Tomamichel supplies a real degree≤D NOR polynomial p with p(0)=1 and |p(k)|≤epsilon for integers 1≤k≤n. Setting q(x)=p(n-x) and S=sum P_i gives q(n)=1 and |q(j)|≤epsilon for j<n, so operator-norm approximation and exact projector product identities follow from commuting spectral projections. For D≤n/2<n, the Newton coefficients a_s=Δ^s q(0)=sum_{j=0}^s(-1)^(s-j)binom(s,j)q(j) obey |a_s|≤epsilon 2^s for every 0≤s≤D. The identity binom(S,s)=sum_{|T|=s}prod_{i∈T}P_i and tensor-product projective-norm submultiplicativity yield ||q(S)||_pi≤epsilon sum_s binom(n,s)(2mu)^s; mu≤kappa gives the dimension/entropy form. Verified all imported hypotheses directly against Fact 2 and Lemmas 2–3 of the original published full PDF; no numerical certificate is needed for these exact identities. The restriction D<n is necessary: q(n)=1 must not enter finite differences.

## originality

PASS

Best-of-knowledge PASS for the stronger epsilon-weighted projective norm estimate for the same projector, not for NOR approximation, projective tensor norms or quantum strong converse. Inspection of Beigi–Tomamichel full updated preprint Fact 2 and Lemma 3 shows Newton expansion in failure projections Δ_i with coefficient upper bound 2^s and final norm without epsilon. The alternative success-projection Newton expansion and epsilon gain are not in that inspected source; earlier projective tensor norm studies concern other spaces or norms. An unindexed alternate-basis calculation remains a priority risk.

## value

PASS

The same polynomial approximation of a Stinespring-image tensor-power projector is a central technical norm input in the quantum strong-converse proof. Switching the interpolation basis from failed to successful local projections exposes an extra exponentially small epsilon factor while keeping the identical approximate projector and error. This materially improves a natural norm bound without presuming a stronger quantum-capacity theorem; it is a motivated structural lemma, not merely a renamed constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
