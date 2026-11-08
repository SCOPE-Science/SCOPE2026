---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Capelli/tower criterion turns X^4+aX^2+b irreducibility into chi(b)=chi(a^2-4b)=-1. Setting t=4b/a^2 for a!=0 produces a triple nonsquare character pattern; zero factors vanish at t=0,1,1/u, so expansion is exact. Three pairwise sums (-chi(-1),-chi(-1),-1) and cubic trace give (q+1+a_q)/4. At a=0 the chi(-1) correction cancels; summing over ratio u double-counts ordered distinct nonsquare constants using r_a=(q-chi(-1))/4 and the special a=0 case. Nonsingular curve and Hasse give strict positivity. Independently enumerated all degree<=2 factors of the quartics over F3,F5,F7,F11,F13 for 300 (u,b) cases and verified individual counts and total ratio moments. This does not replace the finite-field proof for arbitrary q.

## originality

PASS

Relevant prior character-sum and Legendre-point-count techniques are classical; Auer–Top Proposition 4.1 gives the unrestricted Legendre first moment, but not fixed-ratio paired quartic irreducibility. An earlier repository theorem on composition quartics counts pairs (a,b) for (T^2+aT+b)^2+c with fixed c,d; its fixed-constant family is not equivalent to fixing b in X^4+aX^2+b, because expressing the latter as a shifted square makes the outer constant depend on a. No inspected prior theorem directly entails the fixed-ratio coefficientwise intersection count; possible older character-pattern general theorems remain a real risk.

## value

PASS

The fixed-ratio simultaneous irreducibility distribution is an exact natural arithmetic correlation, with a nontrivial elliptic trace fluctuation and a sharp mean over all square ratios; it cannot be obtained by independent-event multiplication. This is a useful closed invariant for a constrained trinomial family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
