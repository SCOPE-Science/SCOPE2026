---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The four-state R+/R-/T+/T- chain with mandatory T± -> R∓ at rate β, run to same-sign pause at α, and trap damping κ yields antisymmetric orientation generator B=[[-α,α],[-β,-β]], D(s)=(s+α)(s+β)+αβ. Stationary forcing covariance G(t)=A(e^{Bt})11, A=v²β/(α+β). Exponential position filtering produces C(t)= A Re[c e^{zt}/(κ²-z²)] +A α(2β²-κ²)e^{-κt}/[κD(κ)D(-κ)], z=-(α+β)/2+i sqrt(-χ)/2 and χ=(α-β)²-4αβ. The complex sinusoidal coefficient cannot vanish, while the trap residue cancels iff κ=sqrt(2)β. If χ>=0, real exponential polynomial has finitely many zeros. If χ<0, asymptotic sign crossings follow from which decay rate is slower, with κ>λ always infinite, κ<λ infinite exactly at cancellation, and κ=λ decided by oscillatory amplitude L against real H. Independent Sympy exact factorization gives (r+1)²(3r²+14r+3)-r[8-(r+1)²]²=-(r+3)(r²-6r+1)(r²+4r-1), forcing infinite strict crossings iff r=α/β>sqrt5-2 within the complex regime. At r=sqrt5-2 equality merely tangential zeros and no sign changes. Sample α3 β1 κsqrt2 yields exact e^{-2t} sinusoid. Independently derived covariance ODE and symbolic algebra corroborate; infinity comes from analytically nonzero oscillatory tail, not simulated long-time sampling.

## originality

PASS

Best-of-knowledge originality assessment of this EXACT final statement against published mathematical results and the source model, not certification of historical priority. General mathematical machinery and prior model definitions are attributed; claim-specific evaluated classification is not found among inspected primaries. A failed search is not novelty proof. Sadjadi–Shaebani describe orientation autocorrelation of multistate particles, whereas Sun–Ye–Podgornik obtain harmonic-trap stationary moments for a tumble mechanism with independently sampled heading. Neither implies the sign-change trichotomy for compulsory opposite sign on return without rebuilding the transition generator, residue cancellation, and equal-exponent amplitude condition.

## value

PASS

For a physically motivated active particle with finite pauses, mandatory reversals and confinement, the exact infinite-anticorrelation phase diagram reveals a non-obvious pole cancellation when the trap decay is nominally slower than orientation decay. It delineates when confinement hides versus preserves oscillatory persistence, including a sharp equal-rate tangency boundary; this is more than computing a routine covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
