---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For independent edge clocks, a selected vertex set stays uncovered iff every edge in its incident-edge union has failed to ring; the union size is Σdeg−e(W). In a fixed factorial moment, an adjacent selected low-degree component is a path unless it is the entire connected graph, excluded for large D. A size-s path without a leaf uses s+1 incident edges and has O(D) placements; one with a leaf uses s and has O(L) placements. Both contribute O(D^((1−s)/2)) when s≥2 and are negligible; two leaf endpoints in such a component would make it the whole graph. Nonadjacent tuples have the product limit (subtracting the adjacent tuples with the smaller independent probability also gives o(1)), so the mixed moments give independent Poisson counts. The high-degree union bound is Rq³=o(1). Mixed deterministic observation times for the two classes use the maximum of the two times for a shared edge and change these path estimates only by constant factors. This gives independent last-class times, with the leaf time escaping to −∞ if c=0. Integrating the first class's density against the second's CDF yields the stated integral and erfc formula. If the last cover is after a fixed early centered time, any tied pair must be adjacent and still uncovered at that early time. The probability of a remaining higher-degree vertex or adjacent degree-one/two pair there tends to zero by Rq³ and O(Dq³+Lq²); the chance of finishing before the early time tends to zero as the window is widened. In the leaf regime the L distinct leaf edges are independent, with other classes negligible at log L+x. For discrete completion, label the m-rate arrivals by independent uniform edges; conditional on the draw count T, the scaled clock sum has variance T/m², which vanishes in probability using the union bound T=O_Pr(m log m). Last-vertex labels are identical under this coupling. For the fixed-time count statement in discrete draws, sandwich the deterministic draw count by Poisson arrival counts at centered times x±ε (variance m times the observation time, and log D/m→0), apply monotonicity to the joint count CDF, then send ε→0. For the finite law, a covered noncentral arm has a present last edge and no adjacent absent pair before it. The term qp²F_(ℓ−3) is the joint probability of that arm being noncentrally covered and its first edge absent (the conditional probability given absence omits q). Subtracting its kth power removes the missed-center case. The Poisson transform then determines every discrete probability by coefficient uniqueness, including the t=0 convention. Independent exact subset and onto-history counting (python3 /workspace/branches/reproduce.py 5) matched both laws for (k,ℓ)=(3,3),(3,4),(4,3),(3,5) through 2kℓ draws. The bounded check validates examples only; the convergence and finite formula for arbitrary parameters follow analytically.

## originality

PASS

The supported distinct contribution is the explicit two-hazard irregular-degree limit with its degree mark, plus the evaluated balanced-spider arm formula as a specialization. The generic edge-cover transform is prior, and the leaf-only Gumbel endpoint uses the classical collector mechanism; neither is credited as a standalone originality claim. The strongest compared results cover different sampling laws, graph classes, or strengths of conclusion. The assessment is limited to inspected evidence and does not certify historical priority.

## value

PASS

The two competing degree hazards locate the natural L≈√D transition and give both a non-single-Gumbel law and a quantitative answer for which degree finishes last. Neither is captured by a mean, a threshold order or an unmarked concentration estimate. The balanced spider realizes the three regimes by tuning arm length against arm count, and the compact finite recurrence gives an interpretable exact benchmark rather than a table of small instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
