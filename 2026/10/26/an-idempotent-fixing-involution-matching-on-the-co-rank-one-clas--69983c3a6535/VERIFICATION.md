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

Every rank n-1 isotone map of a finite n-chain is uniquely determined by adjacent collapsed kernel indices i,i+1 and omitted image value t. The explicit piecewise J_n maps (i,t) to (t-1,i) if t>=i+2, to (t,i+1) if t<=i-1, otherwise fixes it; the outer branches reverse one another. For its mate (j,u), both u in {i,i+1} and t in {j,j+1}, which are precisely the crossed image-kernel transversal conditions for mutual inverse maps. Fixed points occur iff t=i or i+1 and are exactly the idempotents, hence 2(n-1) fixed and (n-1)(n-2)/2 two-cycles, including n=2. Independent direct composition verified 240 maps for n=2..9; the all-n proof is structural rather than extrapolated.

## originality

PASS

Qualified best-of-knowledge comparison: the accessible primary works supply originating models or generic techniques but their inspected mathematical statements do not establish this exact complete final result; the four implication checks and specific priority risks below delimit this conclusion.

## value

PASS

The rank n-1 D class is the maximal nonbijective layer of the natural order-preserving transformation monoid. An explicit idempotent-fixing mutual-inverse involution with exact cycle decomposition gives a constructive infinite-family strengthening of whole-monoid permutation-matching existence on this distinguished layer. The claim does not purport to solve the still broader whole-monoid involution problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
