---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Modulo 3 the three classes follow 0→1→2→2. For both unit classes the derivative is a unit, so simple-root lifting supplies one predecessor in each unit class at each periodic target. This makes the class 2 a permutation and gives the claimed depth strata and unique transient predecessor. For depth-two points the exact identity F²(x)−2=x²(x²−4) gives twice the valuation of x and leading digit 2 until truncation. The zero-difference target counts multiples of 3^ceil(k/2). At any allowed nonzero difference with s=2v, dividing by 3^(2v) gives two simple unit roots modulo 3, lifted to modulus 3^(k−2v) and repeated 3^v times in the original variable, which gives the fibre formula. The multiplier y+2 preserves both shell invariants. On s≥2, y−F(y) has valuation s+1 because v_3(y+1)=1. For an iterate H with displacement valuation m≥3 and derivative 1 mod 3, the integral Taylor expansion gives the displacement of H³ as (1+H′+H′²) times the original modulo 3^(2m); the multiplier has valuation one. An iterate count prime to 3 preserves the displacement valuation by first-order iteration. This proves the period equals the cardinality of its leading-digit sector, including singleton sectors and k=1 with only the special root. The uploaded verifier was inspected, not executed. Independent replay: python3 /workspace/branches/47e5fac2-6e75-447e-b393-f5f363bb1e3c/independent_check.py 4 (also with argument 8); observations are in independent_k4.txt and independent_k8.txt there. Every fibre and rich shell was checked in those finite cases (11 cycles, 2 rich at k=4; 27 cycles, 4 rich at k=8, including the root 2 in each). Those checks are corroboration, not the all-k proof.

## originality

PASS

Credit the existing exact-period and cycle census, and the closely related five-adic attachment classification. Neither states or implies the checked nonperiodic fibre assignment to individual ternary cycles. The distinct result is that assignment and its exact fibre counts, not Chebyshev conjugacy or periodic-point counting.

## value

PASS

The result identifies exactly how transient states are distributed in a natural nonpermutation dynamical system, distinguishing branch-bearing cycles from cycles with the same possible lengths but no such branches. It gives a local tree invariant at every periodic vertex for arbitrarily deep moduli and explains why uniform depth strata do not imply uniform trees. The ternary orbit argument addresses a different local lifting regime from the analogous five-adic calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
