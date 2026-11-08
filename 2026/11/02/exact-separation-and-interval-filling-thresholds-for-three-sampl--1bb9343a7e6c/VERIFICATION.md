---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

A fresh random permutation of centers -1,0,1 under quadratic component steps x↦qx+(1-q)c yields the exact epoch IFS X↦q^3X+(1-q)^2 D with six equiprobable digits D={-1-q,-1,-q,q,1,1+q}. The hull radius is (1-q^2)/(1+q+q^2); adjacent digit gaps are q,1-q,2q,1-q,q. Comparison to 2q^3(1+q)/(1-q^3) proves first-generation hulls are strictly disjoint iff q<q_sep root 1-q-3q^3-q^4=0, and IFS support fills its hull iff q>=q_fill root 1-q^2-2q^3=0. The central gap persists below fill; standard strong-separation formula applies only below sep. Independently enumerated permutations and exact rational gaps for multiple q, bracketed both roots and verified stationary variance identities.

## originality

PASS

Best-of-knowledge exact claim-vs-prior comparison after this run’s independent Resultary search and primary-source checks. Earlier generic IFS and reshuffling theory gives the framework, not the two special roots, persistent central hole, and exact separated six-way dimension. Those conclusions require the new explicit digit geometry. Priority qualified: Older specialized six-digit self-similar IFS calculations might state equivalent overlap thresholds; recent algorithm paper was not exhaustively inspected.

## value

PASS

The precise symmetric 3-sample random-reshuffling benchmark has two noncoincident geometric phase boundaries, explicitly isolating separated fractal support, intermediate central-hole support, and interval support. These step-size thresholds and exact dimension under separation are natural geometric invariants of stochastic optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
