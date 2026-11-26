---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The published equations (16)–(19) give exactly the stated positive scalar map at k=2, r=theta^2. Independently, for a distinct putative pair put a=sqrt(z), b=sqrt(t), S=a+b and B=ab. Taking positive square roots and subtracting the two equations gives B=theta(S+2); adding them gives S=2(1-theta^2)/(theta(theta+2)), B=2(2theta+1)/(theta+2). Conversely these sum/product relations imply the original pair equations by reversing the addition/subtraction. Their discriminant is -4P/(theta^2(theta+2)^2). Since P(0)=-1, P(1)>0 and P'>0 for theta>0, the only distinct positive pair occurs for 0<theta<theta_c, where both S and B are positive and the discriminant positive. At equality a=b, and the same pair equations establish a fixed point. The square-root recursion g(a)=(2+theta*a^2)/(2theta+a^2) has derivative -2a(a-theta)/(2theta+a^2) at that fixed point, equal to -1 by a^2=2theta(a+1). Conjugacy by squaring preserves this multiplier. The fixed-point multiplier crosses -1: locally the fixed root a(theta) has a'=(a^2-2a)/(2(2theta+a^2))<0 at collision, and a^2-2theta(a+1) has strictly negative derivative there (a>theta), so g'+1 increases across zero. Squaring the two positive roots gives the stated z_± and separation S*sqrt(S^2-4B), with the claimed coefficient by the simple zero of P. The independent symbolic replay /workspace/replay_1.py confirms the alternate algebra and frozen numerator/resultant/endpoint identities; theta_c=0.323591553488076213378..., z_c=1.417790578988352431989..., amplitude 17.26768495321154022.... At theta=1 the map is constant and the classification still holds. The result is about this boundary-law recursion, not all types of periodic or other Gibbs measures; on this line Eq. (16) in fact forces z0=t0=1 in that particular four-variable recursion.

## originality

PASS

The original source and its preprints have the reduced map, the critical polynomial and approximate threshold, and the positive-discriminant branch. The distinct supported result is that the critical double root is actually fixed and not a nontranslation-invariant period-two state, with the verified flip multiplier and explicit separation law. The nearest inspected same-model result concerns a different threshold for non-extremality on translation-invariant measures, not this issue. A plausible 2022 same-model text remains unread.

## value

PASS

The disputed coupling is the one singled out in the original source as supporting a symmetry-broken periodic state at equality. Checking the actual orbit rather than the sign of its discriminant changes that phase-boundary conclusion and gives the mechanism and quantitative rate of disappearance. The result is a correction at a canonical branch endpoint, not a routine numerical threshold refinement or an arbitrary restriction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
