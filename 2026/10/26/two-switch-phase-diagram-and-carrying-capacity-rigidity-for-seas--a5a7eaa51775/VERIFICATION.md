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

Direct composition yields exact normalized log-ratio g(x)=(b−a)+aR₂e^{−bx}−bR₁e^{−ax}. g’=ab(R₁e^{−ax}−R₂e^{−bx}) has at most one positive stationary point, a strict minimum if R₂>R₁; g(∞)=b−a>0. Strict g(0)>0 and g(x*)<0 are equivalent to R₁>1 and 1+(b/a)(R₁−1)<R₂<R₁^{b/a}, giving exactly two positive simple crossings and exterior/interior opposite preferred order. Equal carrying capacity R₁=e^{aK},R₂=e^{bK} reduces to convex u^{b/a}−(b/a)u+(b/a−1)≥0 with equality only x=K. At the upper boundary R₂=R₁^{b/a}e^{−δ}, Taylor at x*=K−δ/(b−a) yields crossings x*±√[2δ/(b(b−a))]+O(δ). Independent fresh checker compared 3,000 randomized direct compositions/signs and the rational a=1,b=2,R₁=2,R₂=7/2 witness; finite checking is not the universal proof.

## originality

PASS

This is a sharp parameter characterization for ordering two distinct-crowding Ricker environments and its common-equilibrium tangency, not a recurrence stability theorem. Earlier periodic Ricker work uses fixed crowding or a modified Allee map; a 2022 proper-periodic-Ricker study is a plausible uninspected source. Wider exponential-polynomial comparison theory supplies basic root-count tools, but was not found to imply the model-specific complete wedge and square-root coefficient verbatim.

## value

PASS

The order of environmental regimes affects finite-horizon population output; knowing exactly when preference reverses twice with initial population, and when common capacity forces no reversal, answers a natural scheduling/sequence problem with a sharp bifurcation boundary. It does not claim ecology field forecasts or long-term stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
