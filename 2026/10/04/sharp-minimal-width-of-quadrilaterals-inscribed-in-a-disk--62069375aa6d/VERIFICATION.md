---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The global upper bound and equality analysis reconstruct correctly. Radial expansion reduces to cyclic quadrilaterals. For a cyclic quadrilateral, the four edge-normal widths reduce after the stated cyclic/reversal relabeling to a minimum equal to \(a q\). Writing the relevant half-arcs as \(s\le t\) gives \(w=\sin s\,\sin(s+t)\). If \(s\le\pi/4\), this is already below the target; if \(s\ge\pi/4\), then \(t\ge s\) and monotonicity of sine past \(\pi/2\) gives \(w\le\sin s\sin(2s)=2\sin^2s\cos s\), whose unique maximum is attained at \(\sin^2s=2/3\) with value \(4\sqrt3/9\). Equality forces \(s=t=\arcsin\sqrt{2/3}\), and the remaining arc inequalities give exactly the stated one-parameter family. The triangle bound is strictly smaller. A fresh independent numerical replay over fifty thousand random cyclic quadrilaterals stayed below the constant and reproduced the complete displayed equality family to machine precision; this finite replay is corroborative only.

## originality

PASS

Lassak's complete primary paper explicitly exhibits the same normalized \(0.7698\ldots\) quadrilateral family and explicitly conjectures that it is globally optimal. It also describes motion of one vertex through a family ending in two trapezoids, so those example/equality-family observations are prior and are not credited as new by themselves. The audited theorem supplies the missing global upper bound and proves that all equality cases are exactly that family. Current Resultary and targeted exact-constant searches returned no later proof of Lassak's conjecture.

## value

PASS

The theorem settles an explicit published extremal conjecture and completely determines its equality set. Minimal-width approximation of a disk by few-vertex inscribed polygons is a natural convex-geometric optimization problem, and the result closes the first even case where the regular polygon ceases to be optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
