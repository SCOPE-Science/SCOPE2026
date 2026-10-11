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

Starting from the published definition of outer asymmetry, the translated-circle geometry gives the exact tangent chord vector \(b(x)=2\sqrt{1-a^2\cos^2 t}\,(-\sin t,\cos t)\) and an explicit opposite-ray point. The Möbius coordinate \(z=(\cos t+a)/(1+a\cos t)\) reduces the squared objective to \(64a^2(1-a^2)^3\Phi_a(z^2)/\pi^2\), where \(\Phi_a(y)=(1-y)((1+a^2)^2-4a^2y)/(1-a^2y)^4\). Independent symbolic differentiation reproduces the submitted quadratic derivative numerator \(8a^4y^2+(-3a^6-18a^4+5a^2)y+4a^6+7a^4-2a^2-1\). Its endpoint signs give the unique phase threshold and the high-branch root. The lower branch has its unique family maximum at \(a=1/\sqrt3\), below the bifurcation threshold; the submitted envelope calculation makes the upper branch strictly decreasing. Numerical boundary checks independently reproduce the threshold and high-branch root locations, corroborating the analytic proof without replacing it.

## originality

PASS

Balestro--Martini--Teixeira introduce \(c_{\mathrm{out}}\), prove its invariance, bounds and continuity, but their complete primary text contains no translated-disk or Euclidean-disk worked family. The audited result computes the entire natural off-center circle family, discovers a genuine extremizer bifurcation and determines the sharp maximum across the family. Targeted Resultary search returned the assigned phase diagram as the only exact match.

## value

PASS

A Euclidean disk with a displaced gauge origin is the canonical smooth one-parameter deformation from a norm to an asymmetric gauge. The full exact c_out profile reveals a nontrivial maximizing-configuration bifurcation and a sharp unique family maximum, making it a natural benchmark for the asymmetry invariant rather than an arbitrary example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
