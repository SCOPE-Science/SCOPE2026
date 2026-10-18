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

The exact integral H=p(x)^2y^2/2+∫_0^x p(s)^2s(1+βs^4)ds with p=e^{αx^4/4} is conserved under x'=y, y'=-x-αx³y²-βx⁵. Its even coercive potential yields precisely one compact smooth oval for each A>0. The time-preserving coordinate z=∫_0^x p(s)ds gives z''+h(z)=0 with h(Φ(x))/Φ(x)=x(1+βx^4)/B(x), B=Φ/p. When α>0, B' + αx³B=1 and B>x/(1+αx⁴), so x/B increases; α=0<β gives k(z)=1+βz⁴. The exact period quadrature 4∫_0^1[2∫_u^1 t k(Rt)dt]^-1/2du is strictly decreasing with R for α+β>0 and constant 2π otherwise. Expanding h(z)=z+(β+α/5)z⁵+O(z⁹) yields T(A)=2π[1-(α+5β)A⁴/16+O(A⁸)]. Pure β-axis dominated convergence gives T~[(2√3)/(3√β)] B(1/6,1/2) A^-2. For α>0, exact endpoint-layer scaling with q=αA⁴ has pointwise kernel e^-u/sqrt(1-e^-2u) dominated by 4e e^-u/4 /sqrt(min(u,1)), yielding sqrtα A² sqrt(1+βA⁴)T→2π. I independently verified conservation and fifth-order force jet symbolically and independently checked pure-β period quadratures at finite amplitudes, which are not proofs of the infinite family.

## originality

PASS

Best-of-knowledge original physical-time all-amplitude strict period function and both sharp high-A parameter-regime coefficients for precisely the da Cruz–Llibre nonnegative global-center stratum. Their Theorem 1 classifies centers, not periods. Classical oscillator and Liénard period comparison literature supplies general tools and partial special cases; material read did not establish the joint global quantitative conclusion. Incompletely inspected Yang–Zeng final text remains an overlap risk.

## value

PASS

Completes the period portrait on a nontrivial natural two-parameter global-center locus, giving uniqueness of each prescribed physical period and sharp crossover between A^-2 and A^-4 decay. Exact times matter in center dynamics and are not implied by a phase portrait or topological existence classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
