---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The symbol θ=e^{iaz} has bounded derivatives (ia)^k θ, so Leibniz shows Mθ bounded on the derivative-defined H_n^p for 1<=p<=∞. For |λ|>1, θ-λ and all derivatives of 1/(θ-λ) are bounded on C+, yielding a bounded inverse multiplier. For 0<|λ|<1, zeros z_k=(arg λ+2πk)/a+i(-log|λ|)/a lie at infinite distinct interior points; each evaluation functional is continuous and finite collections are linearly independent via rational interpolation P(z)/(z+i)^{N+n+1}, hence the range has infinite codimension and cannot be Fredholm. For |λ|=1, take x with θ(x)=λ and normalized Fε=cε/(z-x+iε)^2; boundary scaling fixes ||Fε^(n)||_p=1 with cε ~ ε^{n+2-1/p} (or ε^{n+2} for p=∞). Leibniz and |θ(t)-λ|<=min(2,a|t-x|) yield ||(θ-λ)Fε||_{H_n^p}→0; p=1 logarithm multiplied by ε power also vanishes. An injective Fredholm operator is bounded below, contradiction. Closure gives λ=0. Independent finite rational interpolation and boundary-scaling checks corroborate proof, not replace the Banach argument.

## originality

PASS

Best-of-knowledge originality from distinct actual primary statements and implications: Same spectral disk can have smaller Fredholm essential spectrum for other operators; the all-point non-Fredholm conclusion needs proof, especially interior λ and all Banach p. A broader abstract multiplier theory might imply the theorem, but none of the inspected primary Banach-half-plane results states that stronger conclusion; all-p endpoints remain additional. The infinite horizontal lattice of θ-λ zeros forces infinite independent evaluation obstructions for every interior λ; this multiplicity is the essential extra invariant. Boundary approximate eigenvectors complete the classification.

## value

PASS

The source Banach Hardy–Sobolev setting has a known ordinary multiplier spectrum, but its Fredholm classification is a distinct invariant. The exact disk result exhibits an infinite-codimension interior obstruction, unlike the ordinary Fredholm unilateral shift; it settles endpoints p=1 and ∞ together with every derivative order by a common rigorous mechanism. This is a motivated complete operator classification for a natural singular inner multiplier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
