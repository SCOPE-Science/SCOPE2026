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

Define Σ-type of each local point and keep one original component per distinct root Σ-signature (preserving the distinguished component). In each chosen component order retained local Σ-types by inclusion. For each false □ψ of a representative root retain an original successor-root witness; every true □χ remains true at selected successor roots. Induction on Σ proves atomic, implication and □ truth at every retained local type: false implications have an original upward extension whose type remains in the filtered component. Counts are ≤2^s components and ≤2^s points each. Original paper establishes soundness/completeness of iK+bem for these concrete mixed models, yielding FMP and a coNEXPTIME upper bound by finite countermodel guessing. Independently checked a constructed two-component Kripke model across seven modal/implicational formulas; finite diagnostic cannot replace unrestricted induction.

## originality

PASS

The primary van der Giessen et al. 2025 article proves mixed-model completeness, while its conclusion explicitly notes finite-model property as a plausible but unfinished question. The two-level root/local filtration resolves that missing step for this precise class; existing IS4 and finite intuitionistic frame results are not a covering FMP for iK+bem.

## value

PASS

Finite-model property and a constructive exponential finite-size bound resolve a natural decidability gap for a named mixed-modal logic whose completeness was already established; this is a meaningful structural theorem independent of lower-bound complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
