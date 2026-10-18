---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Normalized subentropy integral Q(v)=∫[t/(1+t)-∏t/(t+v_i)]dt; splitting one mass w into w-a and a changes Q by a(w-a)∫ tP/[(t+w)(t+w-a)(t+a)]dt≥0. Convexity of each product factor as exponential of sum of -log(t+v_i) makes Q concave in affine mass split; one-sided derivative at zero ≤w∫(t+w)^(-2)dt=1, so change≤a. Peel every nonmodal conditional mass, telescope to 1-Σ_b max_x p_xb. Binary (1-e,e) yields derivative exactly1 as e→0. Zero entries and repeated spectra are continuity limits. Commuting signal states share diagonal measurement. Frozen verifier supplies finite illustrative tables, not the theorem.

## originality

PASS

Datta et al. conjecture a negative-log guessing bound for general cq ensembles and prove general lower nonnegativity. Sharp Bayes-error linear upper bound with best coefficient for all commuting signals survives; Jozsa-Mitchison integral/marginal monotonicity are explicitly credited.

## value

PASS

Establishes a sharp and operationally interpretable, dimension-independent linear Bayes-error control for an entire commuting sector of a published conditional-subentropy conjecture; noncommuting case remains open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
