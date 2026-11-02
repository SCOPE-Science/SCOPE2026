---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The mathematical proof separately checks the exhaustive cases: (i) finite principal generator, (ii) absence of a least filter member, (iii) infinite principal generator. Case (ii) uses the finite-intersection property of point-omission sets on the carrier consisting of filter members and applies the ultrafilter lemma; its large-row set is precisely the kernel, which is not a member of the filter. Case (iii) uses a free ultrafilter on an infinite generator and the off-diagonal incidence relation. These are infinite proofs independent of computation.

The self-contained `checker.py` enumerates all proper filters of carriers of sizes one, two, and three, and all binary relations for every ordered pair of these carriers. It directly compares the two nested Fubini membership predicates and reports `ALL_CHECKS_OK`, 121 filter pairs, and 28,058 relations. The checker does not simulate nonprincipal filters, free ultrafilters, arbitrary infinite sets, or the axiom of choice.

Self-review: passed. Independent audit: not yet performed.
