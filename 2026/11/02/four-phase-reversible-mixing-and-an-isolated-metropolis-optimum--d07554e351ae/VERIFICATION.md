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

Convex stationary-preserving averaging over within-class and ordinary-part permutations justifies unrestricted-to-invariant reduction while preserving total distinguished flow x. Invariant eigenvalue decomposition has λ_A=1-x/a, λ_B=1-x/b-(r-2)t/(r-1), λ_C=1-x/b-t, λ_D=1-x/(ab) with full multiplicity for m>=2, r>=4. Fixed x, balancing ordinary contrast gives t*=2(r-1)(1-x/b)/(2r-3), inside 0<=t<=(r-1)/(r-2)(1-x/b). The scalar f(x)=max{1-x/a, |1-x/(ab)|,(1-x/b)/(2r-3)} is maximum of decreasing envelope and increasing branch, whose intersection/capacity endpoints yield the four rational regimes a=1/(2r-1),1/r,2/3. This proves unique optimal aggregate x; nonnegative flows force ordinary edges absent at x=b. Metropolis parameters x=min(a,b/(r-1)), t=1 can equal full optimality only at a=1/(2r-1), including the other possible x equality failing ordinary contrast. Independently checked exact reduced LP for 42 (r,a) combinations; inspected full source matrix checker; this does not replace the all-a proof.

## originality

PASS

Best-of-knowledge original for the distinguished-mass r>=4 formula, forced aggregate flow, support-screening, isolated Metropolis optimum. General SDP, multipartite block decomposition and 2010 path-like K-PPDR results are credited; checked prior does not imply this quantified solution.

## value

PASS

A sharp all-mass analytic phase diagram for fastest reversible chains on an important complete multipartite family is a substantive solved spectral optimization problem. The unique aggregate flow and exactly one Metropolis-optimal bias show structural optimizer rigidity and a sharp high-bias support-screening transition. Parameter r>=4 prevents repackaging the previous three-part result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
