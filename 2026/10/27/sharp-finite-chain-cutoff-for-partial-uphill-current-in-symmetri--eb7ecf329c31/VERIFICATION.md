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

This passes the actual corrected RESULT.md in /workspace/repairs/2, not the frozen Finding. Its unqualified interior-positive sentence fails: at N=2, a=1, b=1/2, U=1, m=1/4, δ=1/100, t=1/2, physical reservoirs give R=3/25<F_3=18/7 and exact currents (−143,−43,−143)/2800. The proof in the frozen file had used the extra assumption R>2. The replacement keeps the valid all-link cutoff, restricts the interior-positive guarantee under F_L>R to R≥2, and documents the counterexample. In the exact one-point Dirichlet problem, T is affine and M is proportional to sinh(λ(j−L/2)); for N=1 both reservoir generators act on the sole site. Differences of M are a positive constant times cosh(λ(j+1/2−L/2)), strictly largest at the two endpoints except when there are only those endpoints. The minimum current is therefore (a−b)m(R−F_L)/(2L); the telescoping sum is (a−b)m(R−2)/2. If both endpoints are strictly negative and that sum is nonnegative, a positive interior link must exist, including R=2 when L>2. The log derivative of F_L is 1/L−c cosh(c)/(sinh(Lc)cosh((L−1)c))>0 for c=λ/2 and L≥2; F_2=2 and F_L~L(1−z). An independent rational propagation of the recurrence checked the two published example vectors and the counterexample. The frozen script and output were inspected, not executed; their R=18/5 example does not certify the original unqualified sentence. The repair also corrects the attribution about the hydrodynamic limit and keeps the constitutive-current restriction.

## originality

PASS

For the corrected claim, credit the exact finite mean closure, generator and phenomenon of local uphill transport to the literature. The reviewed new statement is the evaluated strict finite-length criterion with boundary-link extremality, monotonicity and the qualified post-cutoff sign regime for this reservoir family. The strongest sources examined give either the starting finite equations or a different continuum or microscopic model, not the discrete all-link cutoff.

## value

PASS

The corrected result gives a necessary and sufficient size criterion for when the opposing gradients can sustain uphill constitutive A-current even at the reservoirs, and distinguishes boundary reversal from loss of all positive currents. This is a meaningful finite-chain cutoff independent of the particular rational illustration; neither a finite sample nor a continuum bound answers that length question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
