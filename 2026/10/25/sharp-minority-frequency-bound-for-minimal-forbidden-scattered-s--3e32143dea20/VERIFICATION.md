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

PASS: Defined scattered-subsequence minimal absence as absence with every one-symbol deletion present. For a binary source with k ones, the published minimal-forbidden-word append recurrence partitions minimal absent strings by last symbol: A counts ending 0, B ending 1; the strengthened induction gives A,B≤2^k with B,C≤2^(k-1) on a prefix ending 1, where C counts ending 00. Appending 1 preserves B and changes A by at most B; append 0 after a single final 1 adds exactly C to B, and after a longer final 1-run is controlled by deleting a repeated 1 and the stronger prefix estimates. The k=0 unary/empty cases and the first 1 are explicitly covered. The witness (010)^k has A=B=2^k under the append recurrence, proving |M(w)|=2^(k+1), including k=0 by the empty word. Independently generated distinct scattered subsequences and one-position deletion tests for all 2,047 words of length <=10; no violations and equality for witness k=0..4. Finite enumeration corroborates but does not prove universal induction; Theorem 4.1 of the actual 2004 primary paper was inspected to substantiate the nonstandard append rule.

## originality

PASS

PASS, qualified: Petković–Ćirić–Bogdanović's 2004 Theorems 4.1 and 5.2 supply the append recurrence and an optimal Fibonacci bound at fixed number of constant-letter runs. Neither is a sharp bound at fixed number k of ONE symbol independent of arbitrarily many occurrences of the other. Kosche et al's shortest absent subsequences and Resultary's binary SAS Fibonacci extremum count a different subset of minimal absences at a fixed minimum length, not the full set M(w). The original use of the append theorem is attributed; an older frequency-specific specialization may exist under 'minimal absent subsequences' terminology.

## value

PASS

PASS: Boundedness of all minimal absent scattered words by the sparse letter count, with no limit on the total word length, is a nontrivial compression/representation parameter. The explicit tight 2^(k+1) and witnesses with singleton runs answer a natural extremal question not settled by the prior run-count Fibonacci bound. It is a self-contained structural combinatorial theorem rather than a trivial renaming of alphabet or known shortest-absence count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
