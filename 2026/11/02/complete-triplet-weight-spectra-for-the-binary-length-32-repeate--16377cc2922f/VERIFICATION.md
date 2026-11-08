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

The Hasse-derivative congruences H_j(c)=0 for j<i exactly characterize membership in C_i=((x+1)^i) in F_2[x]/(x^32-1), because x^32-1=(x+1)^32. For i<=11 the 11-bit syndrome/last-two-bits dynamic program counts each 32-bit word once, accumulating 30 ordinary triples and two cyclic wrap triples; for i>=12 distinct messages of degree <32-i yield all and only the 2^(32-i) words. The actual verify.c implements these recurrences and elementwise comparison with actual SPECTRUM.csv; the separate crosscheck.py handles both sides i=11/12. I inspected the C transitions, Gray updates and supplied CSV. Independently enumerated all messages for i=16,20,24,28,30,31,32; obtained A_16,32=17155 and the published minimum-weight counts for these rows. The program is a finite exhaustive algorithm, not an extrapolation; the complete 33-row C program was not independently rerun in this execution, so the remaining CSV coefficients rely on the inspected exhaustive code and existing package verification.

## originality

PASS

Existing repeated-root papers determine minimum b-symbol distances, not all 33 complete cyclic triplet-weight enumerators. Irreducible and semiprimitive complete-enumerator theorems have incompatible hypotheses at n=32 over characteristic two. An earlier general ambient-space recurrence covers C_0, expressly excluded from the claimed novelty; the remaining proper-ideal coefficient table is a narrow but distinct tabulation. Resultary semantic search found coding-spectrum records for different code families, not this repeated-root length-32 chain.

## value

PASS

Every ideal in the natural binary length-32 repeated-root cyclic chain is accounted for, including exact multiplicities beyond minimum distances, enabling comparisons such as C_3 versus C_4 with equal distance six but 144 versus 112 minimum-weight words. The exact full finite spectrum is a motivated communication-code invariant and is independently useful as benchmark data. Neither an arbitrary code subset nor an unfounded generalization to other lengths is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
