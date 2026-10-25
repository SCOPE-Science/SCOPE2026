---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS. Shell counts n_i and inter-shell edge counts m_i of the girth-eight diameter-four incidence graph give the Green difference Δ_i=(1−(Σ_{j≤i}n_j)/N)/m_i. For an arbitrary oriented edge, deleting it exposes two disjoint q-ary trees of depth three whose vertex counts exhaust N; the remaining q^4 edges connect terminal opposite-side leaves. The edge-source potential is ±Δ_i and its transfer currents have absolute values 2Δ0, Δ_i−Δ_{i+1}, 2Δ3 on the three edge classes. Summing gives every Q column absolute sum 1+6q^4/H and, removing the diagonal in I−Q, every C column 8q^4/H for H=(q+1)^2(q²+1). Matrix symmetry equates row/column endpoint norms. Polynomial comparison yields q2/q≥3 reversal and derivative positivity plus prime-power GQ existence gives suprema 7 and 8.

## originality

PASS

PASS. General pseudoinverse and invariant cycle-space projection theory predates this, but does not produce the two sharp rational q formulas or the cut-versus-cycle reversal on girth-eight GQ incidence graphs. GQ topology/homotopy publications involve different invariants; a prior symmetric block-design case has girth six, not eight.

## value

PASS

PASS. Exact endpoint stability constants for natural canonical cut and cycle decompositions of highly symmetric finite generalized quadrangles are independently useful graph operator invariants. Their distinct sharp limiting ceilings and explicit order-three dominance reversal are structural discoveries rather than tiny numerical improvements or arbitrary instance enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
