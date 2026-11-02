---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Condition on other Bernoulli variables gives one-site deviation bound. At epsilon=1/k, any two nonextreme i/k sites in one window have maximal point-mass below 1-1/k for k>=3, forcing marks to be distance>=w and deterministic GC labels to be w-periodic with m ones. Exact bin weights (i+1)(k-i+1) give a weighted hard-core mark polynomial and characteristic equation lambda^w=lambda^(w-1)+2k/(k+1). For epsilon<1/(w+1), nearest-label rigidity and window union bounds sandwich the general capacity between W(floor(k epsilon/w)) and W(floor(k epsilon)), proving the high-resolution exponent. Independently recomputed 20 exact small first-threshold word counts.

## originality

PASS

The general capacity automaton for probabilistic GC constraint is prior; the all-w>=3 symbolic first permitted defect classification, exact mark polynomial and k-dependent resolution crossover were not located in its indexed statement.

## value

PASS

Provides a sharp first-defect transition in a natural composite-DNA probabilistic window model and a high-resolution capacity exponent independent of the exact interior count, clarifying a cubic-versus-linear alphabet scaling phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
