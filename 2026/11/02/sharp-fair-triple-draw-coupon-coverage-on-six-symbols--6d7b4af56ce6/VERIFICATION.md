---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For each nonempty subset A, inclusion-exclusion of the first uncovered coupon time gives E T=sum (-1)^(|A|+1)/p_A. On six symbols, fairness gives vertex degree M/2 and sum pair-codegrees 3M, yielding exactly 22+M/(M-1)-sum_pairs M/(M-c_e). Strict convexity forces balanced codegrees for each even M=2..20; independent exact Fraction arithmetic recomputed all ten upper bounds and found the unique maximum 157/36 at M=10, balanced pair-degree 2. The explicit ten triples were independently checked to have all vertex degrees 5 and all pair-degrees 2; direct 63-subset inclusion-exclusion independently gives 157/36, versus 327/76 for the full design. The five-symbol complement-cycle support computes 37/12<29/9, establishing the first-size cutoff.

## originality

PASS

Grunbaum–Yaakobi conjectured full-support extremality for fair group draws; Barak-Pelleg–Berend disprove it at seven points via Fano geometry and discuss broader projective supports. The six-point design optimum and equality classification are a distinct sharp finite question, with full text of the closest paper inaccessible here, so a hidden six-point table remains a priority risk.

## value

PASS

The complete optimum and unique equality design identify the first alphabet size where a fair simple uniform triple mechanism is slower than full sampling. This is a mathematically motivated minimum counterexample and exact complete classification, with design-theoretic meaning rather than a merely small gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
