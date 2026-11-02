---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS. The exact specified unitary and CPTP environment reset leave vacuum plus one-excitation block invariant; the ground input stays vacuum and the excited-input reduced population p_n gives exactly their trace distance. Tracking P,Q,Im coherence gives the stated real 3×3 recurrence. Its characteristic polynomial at ε0 is (x²−λ)(x+λ); for each fixed λ in (0,1) the three roots √λ,−√λ,−λ are distinct and analytic in ε near0. First-order derivatives yield r+−|r−|∼[(1+6λ+λ²)/(1−λ)] ε times appropriate scaling; the two oscillatory eigenweights tend to 1/2 and the third to0. Even-index increments stay negative; odd-index increments switch at nε=K(√λ) by comparison of a strictly decreasing ratio of leading positive/negative modes, with third-mode remainder uniformly controlled by O(ε)q^n. Counting every other index yields the asserted K/2 coefficient; positivity at exact SWAP alternates indefinitely. Independently checked nine characteristic polynomials and six bounded trace-distance revival counts against the limiting scale at ε=.002,.001,.0005 for fixed λ, without inferring the limit from finite time. This is a pointwise fixed-λ local result: at larger ε the eigenstructure may differ and is outside scope.

## originality

PASS

PASS as qualified best-of-knowledge. The June 2026 Bhoi–Shaji primary work studies a highly relevant repeated system–environment qubit collision with partial reset and analyzes memory regime boundaries/Bloch dynamics; its accessible abstract and preview do not give the infinite-step fixed-pair revival count. However the full primary manuscript was not accessible in this run and must NOT be labeled wholly noncovering; authorized institutional download failed with storage limit. Other earlier collision renewal and non-Markovianity studies address different channels or counts and do not directly imply this exact coefficient. No decisive equivalent found in Resultary, but material historical priority risk remains substantial.

## value

PASS

PASS. The explicit number of strict information-return events, unlike their integrated magnitude or a yes/no CP-divisibility phase classification, is a natural quantitative memory invariant. The inverse-square horizon and exact coefficient describe a sharp singular boundary between finitely many and infinitely many revivals as exchange approaches SWAP. It yields a nontrivial asymptotic observable for a motivated finite-environment quantum dynamics, while carefully restricting to a fixed input pair rather than the optimized BLP measure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
