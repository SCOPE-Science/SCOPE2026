---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For the Tribonacci fixed point 0→01,1→02,2→0, the 3-pseudoperiod condition for 1≤a<b<c is equivalent to x0∈{xa,xb,xc} for every length-(c+1) factor. Independently generated sigma^15(0) length 10609; for all factor lengths 1..504 the observed factor count is exactly 2m+1, matching the established Tribonacci complexity p(m)=2m+1, hence factors are exhaustive. Independent mismatch-bitset full enumeration for every 1≤a<b<c<504 returned exactly 9352 and cumulative counts at lengths 7,13,24,44,81,149,274,504 of 0,2,9,42,172,676,2402,9352; the nine c<24 triples match the package. The finite check is exhaustive because of the complexity theorem, not merely because a large prefix was sampled.

## originality

PASS

On inspected evidence this exact final claim is not a mere restatement or implication of a known stronger theorem; all four formal comparisons below and material primary-source inspections distinguish what is already known. Originality is best-of-knowledge, not independence or certification.

## value

PASS

The original 3-pseudoperiod characterization is open. A rigorously certified 9352-member full initial domain through the canonical substitution scale q_10=504 provides a meaningful, reproducible finite classification and a structured data benchmark for future automatic, number-theoretic or morphic approaches. The cutoff is a genuine substitution length, not an arbitrary small instance; no infinite characterization claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
