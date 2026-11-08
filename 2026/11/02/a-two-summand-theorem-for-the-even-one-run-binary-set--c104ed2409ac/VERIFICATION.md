---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For each 2j-block of 1s starting at h, the contribution 2^h(2^{2j}-1) is divisible by 3. For the converse, the 8 possible states (odd/even open-run parities of each summand plus binary carry) give a nondeterministic LSB-first addition machine; a 0 after an odd run is forbidden. Determinization with the mod-3 residue and parity of the binary digit index has exactly 10 reachable configurations, closed under both input bits, and the NFA acceptor (0,0,0) occurs exactly when residue=0. The independent construction recreated all 10 states and 20 transitions, proving an all-input-length regular-language identity, not extrapolating a numerical range. Zero and end-of-word finishing parities are handled by the unique accepting state; 9 not in E, but 3 and 6 are, giving sharp order.

## originality

PASS

Best-of-knowledge originality assessment: the exact new claim was compared by implications with same-object primary results; known definitions/source results are credited, and no directly covering proved theorem was identified in the inspected material. This is not exhaustive priority certification. A two-summand theorem for the even-one-run binary set. The reconstructed 10-configuration closure provides the nontrivial missing implication E+E⊇3Z_{>=0}; exact order follows 9∉E.

## value

PASS

A precise additive basis theorem for a natural automatic set that also arises as the support of the generalized Baum–Sweet-type T_2 sequence; the sharp two-summand order is a nontrivial combinatorial sumset invariant, not a mere restatement of regularity or 3-divisibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
