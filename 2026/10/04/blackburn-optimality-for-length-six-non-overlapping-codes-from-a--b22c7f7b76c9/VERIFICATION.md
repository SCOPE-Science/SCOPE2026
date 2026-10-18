---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

The claim is S(q,6)=max_{1<=l<=q-1} l^5(q-l) for every integer q>=10, relying on the published SQN integer-program equivalence for ALL maximum non-overlapping codes. Swapping x,y permits a=x1<=b=y1 and a+b=q; the x5/y5 term is maximized at x5=T5, y5=0. Direct expansion of the recurrence produces F=a^4b^2+3a^2b^2u-a^2u^2+2ab^2v-2auv+b^2u^2+(b^2-2u)w-u^3-v^2 with 0<=u<=ab,0<=v<=T3,0<=w<=T4. The w optimum is T4 if 2u<=b^2 and zero otherwise. In the T4 branch, differentiating in v independently gives dF/dv=b^2(a+b)-2bu-2v and d^2F/dv^2=-2; its endpoint v=T3 equals H(u) as printed. On the interior-vertex branch, an independent symbolic substitution gives dF/dz=-2x^3+2x^2z+2x^2-8xz+x+3z^2+2z-1, convex in z with second derivative 6; the two endpoint derivatives exactly equal 5(x-1)(4x^2-x+1)/(4(x-2)^2), -3x^2+3x-1 (z=x), and -(8x^3-12x^2+12x-3)/4 (z=1/2), all nonpositive in their used domains. In the endpoint branch, stationary z satisfies 3z^2-6z+(1-x)(1+3x)=0; the derivative in x along that curve is -2B/(1+x)^7, with B positive after the z<13/50 and positive increasing-cubic bounds. In w=0 branch the bound <=q^6/16 follows the displayed R(x) positivity for x>=1/2. Thus all a<=q/5 contribute <=ab^5, and all a>=q/5 contribute <=Kq^6 (K=1024/15625). For q>=10 choose c=floor(q/5), c/q in [1/7,1/5] and h(t)=t(1-t)^5 >=h(1/5)=K; the Blackburn construction meets every upper bound. Independently evaluated the reduced exact SQN optimizer at q=6,7,8,9,10,11,12,17,23; it recovers the q=9 exception 33872>33614 and agrees with Blackburn for tested q>=10. These finite checks do not prove the infinite claim.

## originality

PASS

Best-of-knowledge PASS: an infinite exact tail q>=10 in code length six, not merely a known Blackburn construction, rounding table, or fixed small-q instance. Source papers describe SQN but leave this particular tail conjecture open.

## value

PASS

Determines a natural infinite family of an unsolved extremal coding function with an explicit sharp threshold q=10, rather than recomputing a finite table. Settles a length-six instance of Blackburn eventual-optimality conjecture and separates the exceptional q=9 regime; future coding constructions and bounds can use the exact function for arbitrary alphabets. Does not claim maximum-code classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
