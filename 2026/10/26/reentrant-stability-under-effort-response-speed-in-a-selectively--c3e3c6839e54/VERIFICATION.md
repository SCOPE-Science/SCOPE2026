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

In the strictly positive cone the effort equation forces E=2y for every rho>0. The predator equation then gives x/(x+y)=25/26, and the prey equation fixes x=31/52; the reductions are reversible. Independently differentiating the per-capita rates and multiplying by the equilibrium coordinates gives the stated Jacobian and all three positive cubic coefficients. The quadratic A B-C has positive leading coefficient and distinct positive roots 0.04806452072803434 and 0.2208472716438506, agreeing with the exact radical expressions. Strict Routh–Hurwitz gives stability outside and two right-half-plane roots inside; positive coefficients preclude positive real roots. At a critical rate the factorization is (lambda+A)(lambda^2+B) with distinct imaginary pair and negative root. Differentiating P=(lambda+A)(lambda^2+B)-(AB-C) gives Re(lambda')=-(AB-C)'/[2(A^2+B)], positive at the first root and negative at the second. Exact replay: python3 /workspace/reproductions/independent_checks.py 5. Neither this crossing nor the robustness argument establishes nonlinear Hopf nondegeneracy, periodic orbits or nonlinear endpoint stability.

## originality

PASS

The specific two crossings under an effort-speed-only sweep, including the stable low-speed interval outside the source's local theorem, survive the model and broader literature comparisons. The model, equilibrium formula independent of rho, cubic criterion and generic idea of reentrance are prior or standard.

## value

PASS

Changing the responsiveness of harvesting effort without moving the coexistence state is a natural stability question. The two exact, transverse crossings give a robust counterexample to monotone stabilization or destabilization in that parameter and reveal stable behavior outside a commonly quoted sufficient condition. This is useful independently of possible later nonlinear Hopf or empirical work; no such claim is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
