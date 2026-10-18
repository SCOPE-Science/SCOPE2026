---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

From folded Skellam masses p0=e^(−a−b)I0(z), pk=2e^(−a−b)cosh(kθ)I_k(z), z=2sqrt(ab), θ=(log a/b)/2, k≥1, the k≥2 log-curvature sign compares Rk=I_k²/(I_(k−1)I_(k+1)) and Qk=1+sinh²θ/cosh²(kθ). Classical strict Bessel Turán gives k1 positive even after special factor two at zero. Writing I_k=(z/2)^k A_k(ab)/k! and using positivity yields Rk≥(k+1)²/[k(k+1)+ab]; for ab≤1 this exceeds Qk<1+1/k². For any fixed k≥2, I_k(z)/I0(z)→1 as z→∞ so Rk→1<Qk for fixed θ≠0: choose s large simultaneously for finite k=2..K. For each fixed ab and θ, lower bound Rk−1=Ω(1/k), while Qk−1=O(e^(−2k|θ|)), proving eventual strict logconcavity. Rational Bessel series at a=3,b=12 has p2²<p1p3. Numerically independent high-z k2..7 checks corroborate but the analytic limiting comparison proves infinite statement.

## originality

PASS

Best-of-knowledge priority for the precisely delimited contribution. Known subfamilies, classical inputs, and plausible stronger derivations separately documented; searches alone are not treated as a novelty proof.

## value

PASS

Gives a nontrivial, mathematically motivated phase contrast for the natural folded count difference: uniform protected logconcavity, arbitrarily many consecutive opposite-sign curvatures, and eventual tail recovery. Reversals of arbitrarily prescribed finite length show failure of global shape preservation beyond an isolated tiny counterexample, useful for probabilistic distribution-shape analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
