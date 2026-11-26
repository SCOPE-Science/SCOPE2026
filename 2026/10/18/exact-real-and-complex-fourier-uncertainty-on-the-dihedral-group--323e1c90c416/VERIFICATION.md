---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The four characters factor through D8/<r²>; the faithful block has determinant x²+y²−z²−w² in central-pair differences. If only one central sector is present, support is even. The basic product bound follows from independent translates selected greedily to cover previously uncovered entries. At support three, left translation and automorphism reduce to a single rotational coset, or to two rotations and a reflection with rotation separation 1 or 2, accounting for 8+32+16 subsets. In the first case the scalars come in duplicate pairs and at least two survive; the real determinant (a−c)²+b² is strictly positive. In the separation-one mixed case two independent signs give four scalars, at most one zero, and a zero scalar forces the determinant to be ±2ab≠0. In the separation-two case a scalar cancellation forces c²=(a+b)² and nonzero determinant −4ab; without the cancellation all four scalars survive. This proves the three-point bounds. At support five, rank≤3 needs exactly one scalar and a rank-one faithful block. The four pair sums are ±t with t≠0, so three pairs must be singletons. Their squared differences are t²; the zero determinant forces the fourth to have squared difference t² as well, an impossible fourth singleton. At seven, rank≤2 restricts to one sector. Other lower rows come from the product bound. Independent exact rank calculations on the regular multiplication matrices confirm all nine distinct witnesses, yielding both stated profiles. Replay: python3 /workspace/reproductions/group_rank.py (SymPy). This verifies upper witnesses only; analytic lower bounds quantify over arbitrary amplitudes. The supplied checker and notes were inspected but not executed.

## originality

PASS

The complete field-sensitive D8 profiles survive the strongest located comparisons, most notably the support-five obstruction and the real support-three bound. Prior general uncertainty inequalities, including a stronger group-algebra bound that forces the complex support-three lower bound, and the exact general two-spike law are not new here.

## value

PASS

The square group gives a canonical nonabelian rank-weighted uncertainty benchmark, not a random support pattern: each of its eight exact-support strata is resolved over two fields. The sharp support-five obstruction is visible neither in the basic support-product bound nor in the order-eight quaternion analogue, and the support-three difference isolates the field-sensitive rank behavior of the faithful block. These exact minima contain information that a monotone at-most-support envelope loses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
