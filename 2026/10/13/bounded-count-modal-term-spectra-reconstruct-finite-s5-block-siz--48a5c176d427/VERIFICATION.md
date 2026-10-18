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

For each r-ary Boolean valuation, q=2^r colors encode atomic input minterms. Every graded-modal formula at a pointed equivalence class depends exactly on distinguished color c and truncated class-color counts t_i=min(K,m_i). All pointed types have depth-one characteristic formulas; nested D_j sees only a union of fixed colors per class, and the clamped count of such a union is determined by t. Types are realizable iff (no t_i=K and sum t_i is an actual class size s∈S) OR (some t_i=K and sum t_i<=M=max S), with t_c>=1. Therefore T(r)=2^{E(2^r)}, E/q=Σ_{s∈S}A_s(q)+R_{M,K}(q). For K>=2, deg A_s=s-1 with leading 1/(s-1)!, deg R<=M-K, so equality for infinitely many q=2^r recovers M and all S by maximal symmetric difference; for K=1 recover only M. Repeated class multiplicity is indeed invisible. Zero arity, M=1 and K=1 boundaries are included.

## originality

PASS

Graded bisimulation/type distinction is classical in Otto arXiv:1910.00039 and graded epistemic/S5 modalities in Chen–van Ditmarsch–Greco–Tzimoulis arXiv:2105.09202. Those source statements concern expressive equivalence and graded semantics, not the explicit all-arity Boolean term-operation *counts* of arbitrary finite equivalence-class unions nor the sharp K=1 versus K>=2 reconstructible class-size-set dichotomy. Resultary semantic searches produced general modal/finite algebra entries but no implication-equivalent polynomial fingerprint classification; older modal algebra clone literature is residual risk.

## value

PASS

A complete explicit term-operation census and the threshold where a graded modality reveals every distinct S5 class size are natural algebraic expressiveness invariants. It specifies exactly which structural information is invisible, including class multiplicities, for a broad nontrivial family; it is not an arbitrary tiny finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
