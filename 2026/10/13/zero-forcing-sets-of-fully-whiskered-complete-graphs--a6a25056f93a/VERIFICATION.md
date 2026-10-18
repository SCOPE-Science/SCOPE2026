---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For W_n=K_n corona K1 (n>=2), classify each core-leaf pair as empty, core-only, leaf-only or both. With >=2 empty pairs the two uncolored cores permanently block any blue core, even after all available leaf forces. With exactly one empty pair and no initial blue leaf every black core has two white neighbors (missing core and own leaf), so stalled. With one empty and a blue leaf, all leaf-only pairs first activate their core, a core whose leaf is already blue forces the unique missing core, and the new core forces its pendant; remaining whites are forced. With no empty pairs all initial leaf-only states activate cores, which force all remaining white leaves. This complete case split gives polynomial (2x+x²)^n+n((2x+x²)^(n-1)-x^(n-1)), Z=n-1, minimum-set count n(2^(n-1)-1) and total (n+3)3^(n-1)-n. The actual artifacts/verify.py Git blob was read; a separately implemented brute zero forcing simulation exactly matched polynomial coefficients for n=2,3,4,5. Infinite theorem follows from structural four-state proof, not finite tests.

## originality

PASS

AIM and Javaid et al. have general/special zero forcing corona numbers, with main Javaid assumptions attached graph order at least two, or specific tree bases for attached singleton. None of the inspected relevant statements determines all ordinary zero forcing sets of K_n corona K1. Resultary full publication on the identical graph uses the general-position polynomial, which is a different combinatorial invariant.

## value

PASS

The iff classification identifies every ordinary zero forcing set in a canonical infinite family and yields exact coefficients, number of minimum bases and total. This goes beyond the known scalar zero forcing numbers and permits analysis of random forcing seeds and polynomial shape for a natural extremal chordal family. The formula is a concise but nontrivial complete finite-state count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
