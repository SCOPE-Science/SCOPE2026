---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The analytic entropy difference Δ_p(z) from the cited binary convex-envelope formula is even. At z=0 its second derivative is A(p)=F(a)/a, with one interior critical root because F(0)=0, F initially positive, Fprime strictly decreasing, and F->-1 as a->1. At p*, A=0 and source second convexity condition is strict; the quartic coefficient B=[3(1-a*^2)^2-2a*^6]/a*^2>0. For δ=p*-p>0, A=-c δ+O(δ²), c=-2Fprime(a*)/a*>0. The contact minimum solves A z+(B/6)z³+O(δ z³+z⁵)=0, giving z²=6cδ/B+o(δ). Symmetry plus strict convexity outside the central nonconvex pocket makes the convex envelope constant across the two equal minima, so C=Δ(0)-Δ(z)=3 A²/(2B)+o(δ²). Independent high-precision checks for δ=1e-5,1e-6,1e-7 approach K, but asymptotics rely on Taylor and global convexity premise.

## originality

PASS

Tikku--Berta--Renes identified the critical p around 0.1241; Hayashi--Salek give the exact binary convex-envelope expression and analytic sufficient convexity inequalities and numerical single-use values, not the one-sided Taylor onset coefficient or square-root contact point. Prior classical BSC/BEC channel comparison is a different Eve output model. A source published in 2026 is directly inspected, not inferred from abstract.

## value

PASS

The bifurcation exponent, exact amplitude and contact geometry are meaningful quantitative invariants of the same channel at an established secrecy threshold; they distinguish the onset of one-shot private information from mere zero/nonzero threshold knowledge. It neither asserts multi-use capacity behavior nor global p profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
