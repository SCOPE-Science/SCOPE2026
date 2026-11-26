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

For 0<r<1 the lower Fréchet clipping is inactive, and the upper clipping cuts at L<u<H: the boundary equations are r√[u(1−u)v(1−v)]=(1−u)v and r√[u(1−u)v(1−v)]=u(1−v), respectively. For each fixed v, C(u,v) is absolutely continuous in u; its a.e. derivative gives a version of the conditional CDF (take a common full-measure set at rational v and use right continuity). For fixed u the derivative is 0, ∂uG, and 1 in the three open regions, with the right-continuous boundary values. Substituting the two boundary equations into the interior derivative gives jumps L/(2u) and (1−H)/(2(1−u)). The remaining conditional mass is smooth between the curves with the stated positive mixed partial: for a=√[u/(1−u)]<1<b=√[v/(1−v)], its negative correction is bounded using (1−a²)(b²−1)≤(b−a)² and b/a<1/r; same-sign factors give density at least one. Uniform U then gives two graph measures with zero planar Lebesgue support, each of mass −s log(s)/[2(1−s)], s=r²; there is no remaining singular-continuous or edge mass. Reflection, the product and Fréchet endpoint copulas, and −log(s)>1−s verify the sign symmetry, endpoint limits and strict monotonicity. The proof is replayable from RESULT.md lines 53–122; the supplied finite grid/quadrature verifier was inspected, not rerun.

## originality

PASS

Credit only the explicit measure-level result: the right-continuous conditional law with two atom weights and the exact aggregate singular fraction. The clipping construction, boundary curves, and regular density are already known. The strongest inspected source verifies copula positivity at a clipping boundary by bounding a first derivative; it does not identify the conditional CDF jumps, establish that they exhaust the singular part, or integrate their mass. The new measure calculation uses those known ingredients but is not a restatement of their results.

## value

PASS

For a previously proposed uncertainty copula, the fraction of observations on deterministic conditional branches is a motivated, directly usable invariant. For example at |ρ|=1/2 the Lebesgue density accounts for only about 54% of the joint probability. Knowing the two conditional atoms and their weights distinguishes the genuine law from a density-only treatment and gives the full conditional sampling distribution. No novelty or value credit is assigned to the already known clipping geometry or interior formula in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
