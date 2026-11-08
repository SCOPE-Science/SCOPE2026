---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The polyhedral-cone volume 2πR²h/3 and lateral area 2πR√(R²+h²) combine with the directional width 2max(R√(1−u²),h u). Integrating u∈[0,1] gives mean width R[x+arctan(1/x)], so the normalized Steiner cubic is 2z³/3+a z²+b z+x/3 with b=√(1+x²). The strict Minkowski inequality for a non-ball implies a²>2b; stationary z±=(-a±q)/2 are negative. Their exact critical values are Φ∓/6, with q=√(a²−2b). Independent symbolic expansion verifies Φ± prime =1/2+3/2[(x/b)(a±q)−1]²>0 for all x>0. The limits at x↓0 are both negative; derivative >1/2 forces a unique zero of each; Φ+>Φ− orders them. The packaged rational sign brackets (1/2,3/5) and (23/20,6/5) isolate the zeros. The standard cubic sign diagram proves multiplicities and all root cases; no finite sampling substitutes for global monotonicity.

## originality

PASS

The close 2007/2008 root-location literature supplies general Steiner-root classifications and inequalities, not a read exact centered bicone two-transition parametrization. A published single right-cone result has two transitions but a different solid and different coefficient functions; the central symmetry and absence of exterior planar base prevent a direct substitution. Primary full text of Hernández Cifre–Saorín (2007) was unavailable despite arXiv/OA attempts and authorized institutional submission, leaving a real but bounded earlier-coverage risk rather than an invented exclusion.

## value

PASS

A symmetric double cone is a canonical one-parameter singular convex-body family. Determining whether all three Steiner roots are real is sensitive to intrinsic volume structure; the exact reentrant complex–real–complex transition with two rigorously unique boundary aspects is not just a plotted sample or generic cubic formula. Its strict-square monotonicity mechanism may serve as a worked structural benchmark for Steiner-root geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
