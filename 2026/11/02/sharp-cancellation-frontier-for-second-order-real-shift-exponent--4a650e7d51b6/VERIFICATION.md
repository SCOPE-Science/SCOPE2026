---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Reconstructed normalization R_t(z)=integral (1+s z)^(-1)dmu and exact order-two moments (1,t,t²/2), over finite signed Borel measures with 0<a<b and t in [a,b]. For c=(a+b)/2, h=(b-a)/2, d=t-c, δ=t²/2 the proposed λ* branches use two-point center u/endpoint v or midpoint-positive/endpoints-negative three-point measures. Substitution verifies mass, first and second moments. Their dual quadratic q(s)=1−2((s−u)/ρ)^2 lies in [−1,1] throughout [a,b] by the phase inequality ρ≥max{|u−a|,|u−b|}; in the interior use center c and ρ=h. Equality at dual contact atoms proves optimality among all signed measures and uniqueness of weights. At transition one endpoint weight vanishes; endpoint t=a,b are covered. The symmetric result total variation 1+t²/h² follows by d=0. An independently written Fraction test examined 306 exact rational triples, 38 outer and 268 inner, and verified the symmetric benchmark 26 at t=1,h=1/5. This finite test corroborates, not proves the continuum theorem.

## originality

PASS

Best-of-knowledge PASS for the fixed-window second-order signed-residue total variation phase diagram, not for general moment duality or ordinary rational exponential approximation. Prior upper roundoff and global approximation results do not directly supply the optimal signed moment bound; historical signed-moment literature remains a real exact-formula priority risk.

## value

PASS

Sharp minimum cancellation is a natural stability/conditioning obstruction for locally second-order real-simple-pole exponential rational approximations in a fixed reciprocal shift bandwidth. It quantitatively separates inevitable coefficient amplification from global approximation error or actual correlated rounding error; the two/three-node transition and unique extremizer are nontrivial exact finite-dimensional optimization, not mere rewriting of a general dual inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
