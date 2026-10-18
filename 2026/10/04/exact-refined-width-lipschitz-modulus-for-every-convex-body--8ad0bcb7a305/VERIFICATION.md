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

For arbitrary full-dimensional compact convex K in R^n (n>=2), choose maximum-length A-B between exposed opposite support faces at u. Then <A-B,u>=w_K(u); its orthogonal component has length p_K(u). Perturb u by v_t=cos(t)u+sin(t)(A-B-wu)/p; the fixed two support points imply w_K(v_t)>=w_K(u)cos t+p_K(u)sin t, so the two-point local limsup slope is >=p. For p=0 it is >=0. Proposition 14 of Mushkarov--Nikolov--Thomas gives <=p; upper semicontinuity attains max p and yields the global exact Lipschitz constant. Does not assert diameter-function equality. Independently checked cube face case p=2sqrt(2), directional slopes approach p and smooth ellipsoid/square examples; finite tests are only consistency checks.

## originality

PASS

Best-of-knowledge statement-level prior comparison: the exact final claim goes beyond inspected narrower qualitative, lower-bound, upper-bound or Poisson-restricted results. This is not a claim of exhaustive historical priority; see four comparisons and source-specific risks.

## value

PASS

A natural, previously open exact local and global modulus of continuity for width in arbitrary nonsmooth convex bodies; turns direction-dependent inequality in Proposition 14 into equality without regularity hypotheses. A direct resolution of the source's named open question is useful to convex geometry; not merely an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
