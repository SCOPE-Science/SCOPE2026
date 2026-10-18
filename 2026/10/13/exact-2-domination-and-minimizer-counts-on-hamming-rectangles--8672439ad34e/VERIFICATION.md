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

The unselected (i,j) has exactly r_i+c_j selected neighbors, so feasibility iff r_i+c_j>=2. Every column occupied forces >=n; any empty column forces all m row degrees >=2 and >=2m. Explicit feasible constructions achieve min(n,2m); equality forces precisely surjective singleton columns or degree-two rows. The n=2m intersection is 2-regular rows and one-per-column, counted (2m)!/2^m, proving the counting formula incl. m=n=1. A separately written neighborhood brute force over all 10 m<=n<=4 matrices exactly reproduced size and counts (e.g. 44 at (2,4)). This finite check corroborates but is not the universal proof.

## originality

PASS

Best-of-knowledge originality only for the exact full finding and domain; prior same-invariant and general sources were compared by statement and mathematical implication, and the listed unresolved literature risks remain. Square gamma2 and total domination are insufficient to imply the full ordinary rectangular phase crossover, including the 2m branch and exact minimizer counts.

## value

PASS

Unbalanced Hamming products are a canonical two-parameter domination family. The exact n=2m phase switch changes combinatorial type of all minima, and the complete Stirling/choose enumerator describes sharp extremizers rather than a routine substitute of the known square value. Such precise equality data are reusable in domination and extremal-array work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
