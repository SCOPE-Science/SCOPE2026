---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Since every immunity factor lies in \([0,1]\), the effective reproduction number is at most \(\tau\); therefore \(\tau<1\) forces zero outbreak. Repeating the exact no-outbreak update \(r-1\) times sends every population vector to \((0,\ldots,0,1)\) and makes each retained immunity coordinate a product of only within-block drift factors. Conditional on all \(r-1\) transmissibilities being below one, the terminal law is thus independent of the incoming state. The event has probability \(\beta^{r-1}\), giving the claimed Doeblin decomposition and contraction. The edge case \(\beta=1\) is also valid because the \((r-1)\)-step kernel is then state-independent. The exact verifier independently confirms the finite-memory coalescence for \(2\le r\le12\); the universal proof is algebraic.

## originality

PASS

The source Proposition 2.1 assumes a continuous positive density plus positive mass at complete drift and explicitly says that removing the atom may be possible, with only the one-season-memory case singled out. The audited proof replaces that deterministic-reset event by a random but state-independent no-outbreak block and obtains a quantitative global minorization. Fresh Resultary search returned no same-model covering theorem.

## value

PASS

The source itself flags the complete-drift atom as potentially removable. Eliminating it for every finite immunity memory while obtaining an explicit uniform mixing rate strengthens the model's basic ergodic theorem under a natural epidemiological condition and is useful for stationary simulation and sensitivity analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
