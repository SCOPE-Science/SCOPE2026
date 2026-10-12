---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite checks and mathematical verification

`verify_square_inradius.py` reproduces two exact integer constructions: (i) Euclid parameters \(m,n\) with coprime opposite parity and \(n(m-n)\) a square, and (ii) coprime positive \(u,v\) with \(v\) odd and \((u^2+v^2)^2+u^4\le X\). The sets of primitive triples agree at six cutoffs: 100 (2), 1000 (9), 10000 (29), 100000 (89), 1000000 (280), 2000000 (396). The script also prints \(\kappa\approx0.278365132811\) via standard-library Simpson quadrature.

For the unbounded theorem, the necessary chain is: Euclid's uniqueness and \(r=n(m-n)\); square status of two coprime factors; \(v\) odd and \(\gcd(u,v)=1\); monotone column summation \(L(t)=At^2/2+O(t+1)\); odd-divisor Möbius inversion with sum \(8/\pi^2\); and polar area \(A=\frac12\int_0^{\pi/2}(1+\cos^4\theta)^{-1/2}\,d\theta\). All hypotheses and endpoints are stated in the main proof. The finite checker confirms no analytic estimate and is not a substitute for that proof.

The numerical constant is an approximation to the displayed exact integral; no numerical quadrature result is needed for correctness or positivity. An earlier unindexed matching asymptotic cannot be excluded by finite searches.
