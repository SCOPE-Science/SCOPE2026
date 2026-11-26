---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For interior x the deterministic zero equation is C=A/x+B/(1−x), whose minimum is the stated fold; the quadratic sign gives stability of r+. Integrating the factored quadratic to r+ gives Ψ(r+)/w=C r+²(r+−3r−)/6. The height is negative at the fold, rises strictly because ∂C D=x(1−x), and becomes positive as r+ tends to 1 and the C term dominates the integral. The root-ratio condition and Vieta give the larger stated solution for √C. At stationarity, q+(0)=μ and q−(N)=μ. In the interior write q+=x(1−x)σ(wD)[1+μ/(x σ(wD))] and similarly q− with 1−x and σ(−wD); summing the logarithmic corrections gives O(μ N log N). Telescoping the x(1−x) factors and the one-step logistic arguments gives π(k)/π(0) comparable uniformly to μ exp(N Ψ(k/N))/[x(1−x)], including the O(1) Riemann error for fixed parameters. The far endpoint has at most an extra O(N) relative to its nearest interior state and a strict exponential deficit against the maximum. At equal height a boundary layer next to zero contributes O(μ N), and the interior quadratic maximum contributes O(μ √N), both relative to π(0), with exponentially small remainder. These vanish for μ=N⁻² and prove boundary selection, not just the large-deviation tie. Away from the tie the unique potential maximum wins exponentially. The symmetric example follows by substitution. The limitations' wording about needing exactly N⁻² should be read as identifying the scale of the theorem, not as a necessity result: for example the same comparison at N⁻³ also selects zero. The frozen finite diagnostics were inspected, not run or treated as proof.

## originality

PASS

The payoff, deterministic onset and use of an integrated log-rate potential are prior. The supported distinct claim is the closed threshold for the separately defined irreducible stationary closure and its endpoint preference at exact equality with polynomially small exploration. The closest fixation theorem does not give that invariant law, even where the Maxwell algebra is the same. No direct earlier coverage was established in the bounded comparison.

## value

PASS

The two thresholds answer different natural questions in a payoff family already used to model explosive cooperation. Their exact separation gives a nonempty interval, when accessible, in which deterministic cooperative attraction fails to predict the large-population stationary outcome. Resolving equal heights by finite-weight asymptotics distinguishes this from a routine computation of the deterministic roots or a bare large-deviation maximizer. The conclusion is for the specified closure, not evidence for a hypergraph process it does not model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
