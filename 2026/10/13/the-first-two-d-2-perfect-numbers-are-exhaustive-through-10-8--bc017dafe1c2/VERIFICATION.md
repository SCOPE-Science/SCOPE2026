---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Defant's Schemmel formula gives L₂(1)=1, L₂(n)=0 for even n and L₂(n)=∏p^(a−1)(p−2) for odd n. An even n>1 stops at zero and cannot be fixed; an odd n>1 maps to an odd strictly smaller integer, so with D₂(1)=0 the sum of iterates really is L₂(n)+D₂(L₂(n)). The frozen linear sieve assigns least primes by their unique generating pair (n/p,p), and the two odd recurrence branches correctly account for whether p already divides n/p. The intermediate products and accumulated sums fit the stated integer types (even the bound N(N−1)/2 fits int64). Independently implemented segmented odd factor stripping with trial primes up to √N: for each odd input k the array starts at k, applies the exact integer operation /p·(p−2) once per distinct processed prime, and uses the stripped residual (1 or one prime) for the last factor. In increasing order an independent array then accumulates D₂. The replay visited all 49,999,999 odd inputs 3≤k≤10⁸; the even inputs are excluded by the formula. It gave [37147, 53290831], π=5761455 and diagnostic maximum 284911615 at 97556803. Replay: python3 -B /workspace/audit-evidence/1_segmented_odd_sieve.py 100000000 (NumPy integer vectors); prefix and terminal outputs in /workspace/audit-evidence/1_replay.txt. This is finite, not a global uniqueness assertion.

## originality

PASS

Both numbers are known. The independently substantiated claim is the inclusive exhaustion through 10⁸. The checked primary source reaches only n<100000; the database supplies point equalities, not the enlarged interval. Related Resultary stopping-time and prime-power records were compared and do not cover all odd composites on this interval.

## value

PASS

Defant explicitly asks about additional fixed points and comments on their scant data. The decimal cutoff 10⁸ is the first power of ten beyond the previously recorded second example, three decimal orders beyond the primary paper's 10⁵-scale search. An exact interval containing both and excluding any others is a useful reproducible baseline for further distribution or search work, not discovery of the two examples or evidence of global uniqueness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
