---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

At each of two DFT frequencies, vℓ=(√tℓ,√(1−tℓ)) and its orthogonal complement wℓ form a real orthonormal pair for 0<tℓ<1. A common pivot selects coordinate 1 with q=(t1+t2)/2 and coordinate 2 otherwise. The interpolatory residual norm squared is βℓ²/tℓ or βℓ²/(1−tℓ), so by length-two Parseval the expected-to-baseline ratio is the weighted average of mℓ=q/tℓ+(1−q)/(1−tℓ) with weights βℓ². The exact maximum is K=max(m1,m2), attained by residual energy confined to the adverse frequency; equal-energy B=(m1+m2)/2=2+((t1−t2)^2/4)(1/(t1t2)+1/((1−t1)(1−t2))). In the anti-aligned family t2=1−t1 the worst factor is 1/(2t(1−t)) and (K/(1+η))→1 as t↓0, though both sampled entries are positive. Fresh independent Fraction computations confirm aligned K=2, anti-aligned K=49/12 at t=1/7 and a genuinely asymmetric case K=41/20 and B=181/90. Universal algebra, not simulations, supplies the proof.

## originality

PASS

The 2026 Akdodshoev–Leplat–Ahmadi-Asl algorithm and its 1+η upper bound, perfect-alignment sharpness and finite mildly misaligned experiments are prior work. An upper factor alone cannot prove anti-aligned asymptotic attainment, nor the full sharp continuous mℓ minimax profile. Single-frequency ARP and deterministic t-Q-DEIM do not couple random pivots at distinct Fourier frequencies. Resultary returned related matrix/tensor sharpness, not this specific frequency-coupled two-point law. Simple leverage-mixture algebra is possible; value stems from sharpness boundary for newly published algorithm, not invention of interpolation.

## value

PASS

This exact natural smallest nontrivial shared-index tensor model tests sharpness of the published alignment penalty: strong cross-frequency mismatch makes mean-square amplification unbounded without singular pivots, while per-frequency pivoting remains factor two. It quantitatively distinguishes stochastic coupling from deterministic conditioning for algorithm design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
