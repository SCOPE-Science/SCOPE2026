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

With occupation-density local time, the unrestricted resolvent at x is e^(−κ|x|)/κ for κ=√(2λ); killing at m>0 subtracts the image at 2m. For x<m the pre-hit part of the local-time increment must be weighted by the future hitting factor e^(−κ(m−x)), while the post-hit part has the independent restarting factor e^(−κm). For x≥m every increment is post-hit, and the transform is the unrestricted one divided by λ. Integrating over m gives e^(−κx)[x/(λκ)+7/(6λκ²)] for x≥0 and [e^(−κ|x|)/2+2e^(−2κ|x|)/3]/(λκ²) for x<0. These branches agree at zero. Time continuity follows by path continuity and domination on compact time intervals by an integrable product (Brownian maximum and local time each have finite second moments). Inverting and reflecting gives the claimed span product, and subtraction of E R_t times E L_t^x gives the formula. The zero-level value is strictly negative and both h-terms are strictly positive also at the boundary |x|=E R_t. Continuity gives existence, not uniqueness, of a crossing on each side. An independent bounded check conditioned on B_s=x, used the bridge and free-segment maximum distributions and integrated against p_s(x)ds; 24 signed mixed-moment checks agreed. Replay: OPENBLAS_NUM_THREADS=1 python /workspace/independent_checks.py (NumPy/SciPy). No finite calculation is required to extend the proof to all x,t.

## originality

PASS

The supported distinct result is the evaluated deterministic-time span–point-local-time covariance at arbitrary spatial levels and its sign separation. The classical local-time identities, range laws, resolvents and hitting transforms are prior. The exact origin constant alone is not the basis of the originality decision.

## value

PASS

The result quantifies the dependence of a path's total spatial footprint on occupation at a prescribed location, a natural marked first mixed moment of the occupation field. A negative center and positive outer region cannot be represented by a single correlation sign; the exact normal-tail law gives a usable spatial profile and a quantitative positive region. The occupation identity additionally enforces zero integral of that covariance. Neither unique crossing nor a full joint distribution is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
