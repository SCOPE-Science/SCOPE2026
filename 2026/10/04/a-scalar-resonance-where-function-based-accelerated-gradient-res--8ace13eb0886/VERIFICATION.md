---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Specializing the source's constant-momentum scalar quadratic recurrence at lambda/L=5/8 and beta=1/3 gives x_{k+1}=x_k/2-x_{k-1}/8 with x_1=3x_0/8. The characteristic roots (1±i)/4 have fourth power -1/64, so x_{k+4}=-x_k/64 for every k. The first block (1,3/8,1/16,-1/64,-1/64)x_0 yields the permanent magnitude-ratio cycle 3/8,1/6,1/4,1; hence the quadratic objective never strictly increases. Since x_{k+1}=(3/8)y_k, the gradient-restart sign is the sign of x_{k+1}(x_{k+1}-x_k), negative for the first two updates and positive for the update producing x_3. Independent exact-rational replay verified the block, four-step identity, objective inequalities and trigger sign.

## originality

PASS

O'Donoghue-Candes introduce the strict function and gradient restart rules and analyze the same fixed-step constant-beta quadratic mode, but their high-momentum timing discussion is phase-approximate and does not state this exact rational-phase blind spot. Fercoq-Qu later emphasize the heuristic nature of adaptive restart and report a long non-trigger episode, but do not supply this permanent scalar mechanism. Fresh Resultary search returned nearby acceleration/counterexample records but no implication-equivalent scalar no-function-restart theorem. Best-of-knowledge originality therefore passes.

## value

PASS

The result identifies a concrete structural distinction between two widely used restart detectors in the simplest strongly convex setting: genuine oscillation can be permanently invisible to strict objective increase while immediately visible to the gradient sign. This supplies a motivated boundary mechanism for later forced-restart safeguards and is more than a numerical curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
