---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

PASS. Direct substitution verifies x=0,1/(GS),1/(G(S+k)); G,S,S+k are strictly positive. For any other entire nonzero periodic x, W=1/x and z=W/G−S give z'=−(G'/G)z(z−k)/(S+z). On the two branches of ξ=log G, S_+>S_−; at every z_+=z_− meeting the derivative-difference has fixed nonzero sign −sgn(z(z−k)), because x and W have fixed sign. A common endpoint at each end would require opposite near-endpoint signs, impossible without an interior forbidden crossing. This covers negative and nonrational solutions; no truncated numerical integration is used to exclude them. Linearization around both explicit curves gives Λ_+=kJ(w)>0 and Λ_-=-kJ(w+k)<0, and expanding the return map at 0 gives +πvs u²+O(u³). A scalar monotone return map has no true integer-multiple subharmonics. Independent symbolic substitution checked invariant-curve identities; finite source numerical script examined, not used as proof.

## originality

PASS

PASS, best knowledge. Bravo–Calderón–Ojeda arXiv:2302.10743 Proposition 2.10 gives the construction of two rational invariant curves, which is credited, but does not there prove there are no other negative/nonrational periodic solutions or give the present universal Floquet ordering. Huang–Tian–Zhao arXiv:2506.14091 Theorem 1 imposes an extended Chebyshev three-function coefficient-span condition; its explicit applications are linear trigonometric and quadratic polynomial coefficient classes. Here A=GS(S+k)G' has generally higher harmonics; no verified implication puts this entire positive 5-parameter family under that bound, and a general upper bound alone would not compute exponents. These are adjacent but not documented as sufficient prior coverage; Resultary unavailable and older uninspected uniqueness criteria remain risks.

## value

PASS

PASS. Counting every real cycle, including nonrational and negative candidates, in a concrete Abel family with two rational invariant curves resolves a motivated gap left by constructions of rational curves. The two-sweep crossing argument supplies a substantive structural exclusion, and exact multipliers distinguish the cycles; this is not simply recomputing known rational solutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
