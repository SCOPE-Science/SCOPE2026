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

# Verification of the stated result

**Analytic checks.** For Lipschitz real maps, the absolutely continuous derivative has essential-supremum norm equal to the Lipschitz seminorm. A positive almost-everywhere lower derivative bound makes the map strictly increasing; its infimum of absolute secant slopes is the essential infimum of the derivative. Attainment at two points implies that the derivative equals that infimum almost everywhere between them. These statements establish the lower bounds without an auxiliary computational lemma.

**Upper constructions.** For every \(\delta>(h-a)/2\), select an interval on which the derivative's essential supremum is below \(a+2\delta\). Replacing the derivative by \(a+\delta\) on that interval and clipping it below by the same constant elsewhere produces an injective strongly minimum-attaining map at distance at most \(\delta\). If \(h>3a\), subtracting any slope sufficiently close to \(a\) from above makes the derivative take both signs on positive-measure sets, giving a noninjective strongly minimum-attaining map at distance arbitrarily close to \(a\).

**Sharp example.** A positive-measure nowhere-dense closed set has a complement which intersects every interval in a positive-length open subset. Thus the two-valued derivative has global essential infimum \(a\) and smallest local essential supremum \(b\). When \(b\le3a\), the midpoint affine slope attains the predicted distance. When \(b>3a\), any map within distance \(a\) has nonnegative derivative and derivative exceeding \(2a\) on a dense open set, precluding any interval attaining its minimum slope, which is at most \(2a\). Consequently the distance is unattained.

**Limits.** No finite tests serve as infinite proofs; the argument is entirely analytic. The precise formula assumes real scalar maps on an interval and a positive global essential lower derivative bound. The closest motivating preprint's complete text could not be examined, so this package does not certify publication priority or independent validation.
