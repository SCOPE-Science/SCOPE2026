---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Brownian time-change with generator ∂xx and mean-life conservation gives Q=rT=S^p/M(p), p=1/(2H), E Q=1, and stationary age survival density f(a)=Pr(Q>a). Two-sided Mellin moments imply L1 convergence (Q−1)/p→W=log S−Elog S. Fubini gives exact 2dTV=E|Q−1|, whence H dTV→E|W|/4; continuous log-exit law yields non-Gaussian f(1+py)→Pr(W>y). Independently recomputed first four exit moments and the special-function constant ≈0.160663948457; finite H checks only corroborate rate.

## originality

PASS

The prior complete stationary age-resolved heat kernel is expressly treated as covered. Sharp H^-1 total variation coefficient and non-Gaussian log-exit age edge layer require an additional singular normalization not stated in the inspected source; this is a best-of-knowledge judgment with material implicit-coverage risk.

## value

PASS

Age since reset is an intrinsic temporal observable in the published farthest-particle model; precise H^-1 loss and logarithmic exit-time edge profile reveal asymptotically clocklike synchronization beyond existing spatial radius asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
