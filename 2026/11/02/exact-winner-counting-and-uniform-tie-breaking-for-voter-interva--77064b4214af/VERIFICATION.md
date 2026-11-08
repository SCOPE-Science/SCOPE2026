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

Each selected nonempty interval is contained in the first selected inclusion-maximal support type along an increasing-endpoint antichain path. If c follows p, first-owned strict subordinate types are precisely those inside c and not inside p; selecting t locally with >=1 maximal-copy gives B_pc(t)=binom(H_pc+a_c,t)-binom(H_pc,t). Coverage gain g_pc depends only on previous maximal right endpoint. A max-plus weighted count DP with state (last maximal interval, chosen cardinality) therefore enumerates each labeled committee once and sums precisely score-tied counts. Empty-support labels contribute binomial multiplicity at terminalization. O(m³+m²k²+n+m²) rational/integer arithmetic and <=m-bit counts are credible; telescoping counting gives exact unbiased weighted-backtracking sampler. Inspected source verify.py. Independent structurally different path-counting code matched brute-force optimum and winner multiplicity on 500 seeded instances up to 9 labeled candidates with zero voter weights and empty supports, including illustrative score 9 and 7 winners. Finite samples cannot prove ideal uniformity; counting bijection does.

## originality

PASS

Cohen–Gonen optimize maximum interval union (and may drop contained intervals, which destroys tied-labeled counts), while Janeczko–Faliszewski establish a general winner-counting problem and hardness outside restricted domains. Manurangsi–Sornat and Avramidis et al. supply interval-domain winner determination for Thiele-type rules, not exact multiplicity or uniform sampling. No inspected prior implication provides the canonical labeled path-counting formula. Possible #optimal-solutions semiring DP in broad interval coverage literature is a priority risk.

## value

PASS

Fair random selection from tied committees needs exact counts, which decision/optimization algorithms do not supply, especially with nested duplicate supports and empty candidates. A polynomial exact counting and uniform reconstruction theorem for natural voter-interval elections provides a nontrivial algorithmic complement to known winner determination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
