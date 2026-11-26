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

In the spectral Fourier convention of the cited Gaussian power-series literature, the diagonal kernel is u/(1-r²), with u the Poisson extension at the same angle (the opposite Fourier convention reflects the angular label). Positivity and harmonicity give Δ log u=-|∇u|²/u², and the ordinary-area Edelman–Kostlan formula gives (3), including the factor π. Under C^(2m+2), the derivative Fourier series converge uniformly up to the boundary. The Poisson quotient at the zero is dominated by a constant multiple of w(θ0+s)/(1-cos s), integrable because m>=1; its limit is b>0 and u_r tends to -b there. Consequently u=as^(2m)+bδ+o(δ)+O(|s|^(2m+1)) for δ=1-r and s→0, with derivatives tending to (-b,0); the δ remainder is uniform along approaching angles. At s=δ^(1/(2m))x the denominator after dividing by δ is uniformly bounded below on compact x-sets, yielding the profile, including x=0. At fixed x≠0 the outer and inner powers give respectively normalized limits 1 and 0. For δ=εt, t in [1,2], the same uniform estimate gives u/ε→bt+ax^(2m) and ε²ρ tends to the stated integrand with 1/(4πt²). The polar area factor is (1-εt)ε^(1+1/(2m)); the resulting constant is positive for C>0. A closed-form sanity check is w=2-2 cos θ, for which u=2(1-r cos θ), b=2, and the normalized formula is 1-[(1-r²)/(2(1-r cos θ))]². The frozen checker corroborates the critical-scale profile and boundary slopes only; it does not itself test both off-critical angular exponents or prove uniformity. The analytic proof covers those claims.

## originality

PASS

The nonlocal slope, covariance description and fixed-angle asymptotics have explicit precedents. The distinct claim is the compact-uniform angular crossover at a smooth even-order zero, its scale separation and the local sector coefficient. The closest inspected moving-angle result concerns a jump, while the closest smooth-zero results give a radial direction or disk integral, not this local law. No priority beyond the compared evidence is asserted.

## value

PASS

A fixed-ray law cannot quantify how zeros return to the generic intensity across the boundary near spectral degeneracy. The theorem gives the exact crossover scale, distinguishes a local Taylor coefficient from a nonlocal spectral contribution, and determines a measurable sector first moment on that scale for any width and finite even order. The conclusion is local and first-moment only, with no supported claim about fluctuations or convergence of the zero process.

The dated certificate retains the supplied scientific assessment, sources and limitations.
