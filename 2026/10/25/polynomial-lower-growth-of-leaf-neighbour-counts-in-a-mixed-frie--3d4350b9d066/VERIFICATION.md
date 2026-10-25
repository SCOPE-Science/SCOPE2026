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

# Verification

The mathematical claim is verified by the proof in `RESULT.md`.

- Model convention: each arrival chooses a uniform target and then attaches directly with probability \(p\), or to a uniformly sampled neighbour with probability \(1-p\).
- Transition check: a leaf-neighbour is born exactly when the new vertex attaches to the fixed vertex; it is lost exactly when that leaf-neighbour receives the new edge. The two conditional probabilities are enumerated in the proof.
- Algebra check: subtracting the death probability from the birth probability gives the displayed drift identity. Subtracting \((1-2p)(L-1)/n\) leaves \((1-p)(1-L/D+S)/n\), which is nonnegative because \(L\le D\) and \(S\ge0\).
- Recurrence check: for \(Y=(L-1)_+\), the drift bound applies when \(L\ge2\); for \(L\le1\), \(Y=0\) and the next value is nonnegative. Thus the multiplicative expectation inequality holds for all states.
- Initialization check: one direct attachment at the initial edge suffices for labels 1 and 2; two consecutive direct attachments to any fixed label \(v\ge3\) create two leaf-neighbours with probability \(p^2/[v(v+1)]\).
- Product check: the recurrence iterates to \(\prod_{k=m}^{n-1}(1+c/k)=\Gamma(n+c)\Gamma(m)/(\Gamma(n)\Gamma(m+c))\); the standard gamma-ratio limit gives the explicit positive liminf constant.

Limits: no independent audit was performed. The conclusion is an expectation lower bound only; finite calculations, if any, are not used to justify the infinite statement. The trusted importer initializes absent external channels as unperformed; research does not assess or author those channels.
