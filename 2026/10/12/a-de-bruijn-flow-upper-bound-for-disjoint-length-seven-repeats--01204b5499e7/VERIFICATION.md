---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Every admissible word induces a de Bruijn walk with edge counts x_w<=ceil(7/per(w)) by the cited original occurrence lemma and incidence 0 or e_s-e_t. Independent certificate replay recomputed all 128 period capacities, total sum=236, all 4033 endpoint/closed cases and integral LP-dual bounds, each >=16 deleted; all 4033 actual lower-bound values matched the stored potentials exactly. The stored size-16 deleted vector has correct edge integrality/capacities and incidence, proving exact flow optimum 236-16=220 windows and C(2,7)<=220+6=226. The relaxation is not asserted realizable as a word.

## originality

PASS

Gabrić–Shallit–Zhong 2020/2021 Theorem 6 sums factor capacities individually, giving upper242 at C(2,7), and their Table 1 gives lower192; it does not impose de Bruijn incidence consistency. Resultary semantic search and indexed search for C(2,7), de Bruijn flow and bound226 did not return a theorem implying the stronger result. This refinement imposes a new global necessary condition rather than renaming their per-factor bound.

## value

PASS

C(2,7) is the first binary length beyond previously exact n<=6, with source interval [192,242]. The exact 4033-case dual-certified flow upper bound cuts this to [192,226], closes sixteen upper values, and introduces a reusable consistency improvement for analogous word problems. It neither claims an exact C nor equates LP feasibility with realizable words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
