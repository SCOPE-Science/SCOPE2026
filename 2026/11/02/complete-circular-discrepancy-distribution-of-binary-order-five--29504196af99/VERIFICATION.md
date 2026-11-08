---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The cyclic de Bruijn condition is bijective to full-period shift-register feedback tables on 16 four-bit tails; every cycle has one 00000 root. Every balanced circular-substring sum is a difference of prefix sums, so discrepancy equals prefix range. The other Eulerian representation also exhausts exactly all 2048 cycles. In a fresh independent 65536-table enumeration, 2048 yielded complete orbits and discrepancies 5:224, 6:688, 7:912, 8:224, matching the stated histogram and mean 839/128. The claim is exactly finite order five only.

## originality

PASS

PASS with priority risk: full order-five circular-discrepancy multiplicities, unlike already-known all-order minimum and single-cycle/construction-specific estimates, are a new statement not implied by inspected sources.

## value

PASS

The complete 2048-cycle distribution answers a concretely proposed discrepancy-frequency problem for a natural binary pseudorandom-sequence class, quantifies how common each exact balance level is, and is not a random unmotivated small slice. The count is a finite benchmark, not an all-order law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
