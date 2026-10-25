---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

A group containing the unique largest divisor m! must have total at least m!, hence five-layered implies sigma(m!)/m!≥5. This abundancy quotient is monotone under divisibility, so all m≤13 fail once sigma(13!)=31044179712<5·13!=31135104000 is checked. At 14!, sigma=442487616480, equal group sum T=88497523296. I independently parsed all four explicit supplied divisor lists (lengths 5,7,10,27), tested all 49 entries are pairwise distinct positive divisors of 14!, summed each exactly to T, and used tau(14!)=2592 to show the nonempty complement of 2543 divisors sums to T. This proves the complete minimality assertion, not just a finite sample.

## originality

PASS

Best-of-knowledge priority assessment distinguishes the actual joint/exact invariant and mathematical implications from stronger but non-covering frameworks; pertinent primary statements were compared and residual risks are explicit. Least five-layered factorial is 14!

## value

PASS

The first five-layer factorial is a sharply defined unknown boundary in the standard k-layered divisor-partition hierarchy. The explicit nontrivial 49-divisor witness and a clean optimal exclusion proof make the precise threshold useful even without all m>14 being classified; it is neither arbitrary slices nor mere sigma divisibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
