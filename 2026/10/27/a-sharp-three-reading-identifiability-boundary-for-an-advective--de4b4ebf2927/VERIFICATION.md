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

For the fixed known injection location/time, take p=1/D, q=v/D and A=log(M√p/√(4π)). This maps the physical domain bijectively to p,q>0 and A real; Y=log(C√t)=A−x²p/(4t)+xq/2−q²t/(4p). Differencing at the first time fixes q=ap+b, with a=(x₁+x₂)/(2t₁)>0 and b determined by the readings. Differencing across times at x₁ then gives γ=κp−2ab−b²/p. Exactly the positive roots satisfying ap+b>0 are physical: Y₁₁ fixes A freely, and the two differences then certify the other readings. For κ>0 the right-hand side is strictly increasing. For κ<0, choose b>0 and distinct positive p values with product b²/(−κ); then both slopes q are positive and the two time differences coincide. The resulting quadratic roots are simple and positive, persist with both inequalities strict under small changes of (Y₁₁,b,γ), and exhaust the fiber. Since these three data coordinates are invertible affine functions of the Y values, the double-fiber set is open also in positive concentrations. For κ=0, b=γ=0 makes every p>0 admissible at a fixed Y₁₁; this is an existence assertion, not a statement about every critical-design data triple. Taking positive square roots in κ>0 gives the exact sensor inequality, which imposes x₂<x₁ and t₂/t₁<4. For the rectangle, spatial slopes at two distinct times determine the slope and intercept of a line in 1/t: their difference uniquely fixes p since x₁+x₂>0, then q and A follow. The example can be replayed by inserting (p,q,A)=(1/2,7/4,0) and (8/7,19/7,−27/112) into Y; the ordered L readings are (−25/32,−9/32,−9/4) for both, with distinct fourth readings −25/16 and −37/28. RESULT.md §§1–5 establish global noiseless identification only. The finite rational verifier and its notes were inspected, not executed.

## originality

PASS

The supported distinct result is the exact joint mass/diffusion/positive-drift L-design boundary, fiber multiplicities and rectangular remedy for the specified Gaussian pulse. Neither classical Gaussian transport nor observation geometry affecting identifiability is itself novel.

## value

PASS

Two stations with one repeat measurement impose a natural sparse observation budget. The theorem decides whether noiseless global identification can even be attempted at that budget and separates unique, two-valued and continuous ambiguity, with an explicit fourth-reading remedy. The coupling of geometry and time, rather than just a local rank calculation or a count of unknowns, makes the exact boundary useful. It supplies neither noise conditioning nor field guidance beyond the ideal passive model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
