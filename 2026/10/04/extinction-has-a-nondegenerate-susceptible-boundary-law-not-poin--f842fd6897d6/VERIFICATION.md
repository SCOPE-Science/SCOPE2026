---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The 2026 primary paper Eq.(1.3) indeed has susceptible multiplicative mortality noise -epsilon*sigma1*S dB1 and assumes f(0)>0. Let a=epsilon*sigma1>0. On the hypothetical event S→Lambda/mu>0, I,R→0, Ito gives d(log S)=[Lambda/S-mu-beta I/f(I)+delta R/S-a^2/2]dt-a dB1; the bracket tends -a²/2, and B1(t)/t→0 a.s., forcing log S(t)/t→-a²/2. Positive point convergence instead forces log S(t)/t→0, contradiction. On invariant face I=R=0 the zero-current stationary equation (a²s²p)'=2(Lambda-mu s)p integrates to InvGamma(k=1+2mu/a²,q=2Lambda/a²), normalized on (0,infinity). Moments are q/(k-1)=Lambda/mu and q²/[(k-1)²(k-2)]=Lambda²a²/[mu²(2mu-a²)] when mu>a²/2. With a=9/20,Lambda=1,mu=1/5 compute k=241/81,q=800/81, mean=5 and variance=2025/79 exactly. Source Theorem3.2 proves time averages, which remain consistent with the finding. Neither eventual interior-to-boundary convergence in law nor almost-sure convergence of S to a random constant is claimed.

## originality

PASS

Inverse-gamma laws for affine multiplicative diffusions are classical and not asserted as new. The novel specific assertion is the incompatibility between this exact source SIRS equation and its narrative pointwise extinction claim, together with a concrete invariant susceptible law and nonzero variance in the exact published noise regime. Indexed comparable SIR/SIRS papers involve different diffusion coefficients and do not directly settle this source-specific inconsistency.

## value

PASS

The source interprets an extinction simulation as nearly deterministic convergence to its disease-free equilibrium, but the paper’s own SDE sustains nonzero susceptible noise. Proving that distinction and computing a boundary variance about 25.63 when mean=5 materially changes interpretation of extinction and numerical output. The source-specific contradiction is a motivated diagnostic, not a tiny artificial instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
