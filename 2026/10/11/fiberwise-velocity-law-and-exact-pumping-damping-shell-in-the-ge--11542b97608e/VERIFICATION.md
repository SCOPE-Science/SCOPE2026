---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

On a compact invariant flow, invariant generator integrals of antiderivatives F(x) and K(y) give E[y|x]=0 and E[x|y]=a(1-y^(2n))y (a.e.); F(x)=x²/2 also gives E[xy]=0. H=(x²+y²)/2 satisfies L H=a y²(1-y^(2n)), proving E[y^(2n+2)]=E[y²] since a≠0. The second fiber regression has residual -ydot orthogonal to every y-measurable function; total variance yields Var(x)=Var(a(1-y^(2n))y)+E[ydot²]. Strict convexity of Z^(n+1), Z=y², gives E[y²]≤1, with zero implying only origin support, and equality-one impossible because |y|=1 along a full invariant orbit would force x=0 and simultaneously xdot=±1. A zero averaged signed pumping term not supported only at y=0,±1 forces occupation on both sides |y|=1. Positive x/y variances for nonorigin states give exact Corr=0; periodic continuity gives ≥2 crossings per least period. Rechecked the algebra independently; packaged verify.py merely tests rational instances, not these analytic support arguments.

## originality

PASS

The public primary global-dynamics paper studies exactly this nonlinear Rayleigh oscillator and even classifies its unique limit cycle; that orbit-level result does not imply the two conditional regression laws, the exact orthogonal speed residual, or the strict pumping/damping occupation shell as stated. Independent published semantic searches found related conditional laws in DIFFERENT flows but no broader same-model result. The scalar energy identity is elementary and may pre-exist as an implicit balance; qualified original content rests on the combined stationary-fiber result and strict physical threshold crossing. Older 2013 exact-model source was abstract-only; preserve residual risk, do not claim proof of universal novelty.

## value

PASS

The nonlinear damping zero at |y|=1 is an intrinsic physically meaningful pumping/dissipation boundary. Exact conditional regression, orthogonal variance decomposition and strict RMS ceiling plus mandatory excursions give attractor-independent checkable invariants across arbitrary compact stationary mixtures and periodic cycles; neither a normalized trivial zero nor an arbitrary parameter slice. The energy balance alone would be routine, but the combined fiberwise and strict crossing structure has substantive oscillator motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
