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

All 8!=40320 rankings of eight binary 3-mers exhaustively enumerated by a new independent C++17 program implementing leftmost-tie winner-change criterion on all 2^(w+3) iid bit strings for w=2..9. Direct counts produced exactly 1145 distinct (N4,N9) pairs; nondominated pairs (46,759) count48 and (50,750) count32, yielding stated densities /128 and /4096. Individual minima for widths 2..9 were (20,29,46,76,130,229,413,750) with multiplicities (3668,176,48,48,48,48,164,48). Exactly 48 rankings minimize all w=2..8; their first four types are 3206 or 4571 (24 each), and none minimizes w=9. The algorithm enumerates every permutation and every word (exact integer counts), not a Monte Carlo sample; rank shift and tie convention match the result. Only k=3 fair binary inputs and common strict ranking are covered.

## originality

PASS

2018 Marçais–DeBlasio–Kingsford full OA author manuscript materially read: definitions, density, k,w-dependent scalar ordering bounds, and prior exhaustive individual density statements for k=3, but not a two-objective Pareto frontier (w4,w9) nor multiplicities of simultaneous optima in the inspected material. New claim credits pre-existing exact scalar minima and asks common-order compatibility. Resultary targeted cross-width Pareto search did not yield equivalent result; supplementary order matrices or other computational sources could contain cross-width joint values, remaining risk.

## value

PASS

Choice of one global k-mer order across multiple window widths is a natural design constraint in genome minimizer/winnowing systems. An exact Pareto tradeoff and first incompatibility threshold identifies genuinely reusable multi-parameter limitations; all 40320 orders exhaustively covered. Not just an arbitrary fixed scalar optimum or a recomputation of one-width known tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
