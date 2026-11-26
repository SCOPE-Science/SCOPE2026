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

In the replacement, reversal permits a≤d. Counting zero-, one-, two- and three-one palindrome strings separately gives the stated objective; in the two-one layer the first/third rectangle supplies all rows through i=a (and contains the first/second rectangle), with only the second/third pair supplying further rows. This includes the empty-gap boundaries without counting the empty word. Writing h=d−a, p=b+c, m=min(b,c), t=min(b,h) gives quadratic part Q=a(p+m)+tc and remainder at most 3z+3. For h≥b, reducing h to b at fixed z,b,c can only raise Q, and the two subcases give respectively at most z²/6 and the checked strictly positive certificate for 3z²−16Q. For h≤b the slopes at fixed z,b,c are −b/2 when b≥c and c/2−b when b≤c. The only potentially sharp endpoint is h=0, since the other endpoint is h=b or a=0 (then hc≤z²/8). At h=0, p+m≤3p/2 and 2a+p=z give Q≤3z²/16; equality forces b=c>0, which makes the slope strictly negative and forces h=0, and forces 2a=p. Four balanced gaps achieve the homogeneous maximum. Appending up to three zeros to a balanced integer word gives the claimed matching lower bound to O(z). Continuity on the normalized simplex and the sole homogeneous equality point give rigidity for every maximizing sequence.

## originality

PASS

The original's separate all-gap enumeration contribution is covered and does not pass. In the replacement the enumeration is explicitly credited and retained only as a proof input. The distinct remaining claim optimizes over asymmetric as well as symmetric sources and proves the sole asymptotic shape. Neither the exact symmetric-class optimization, the random-word limit law, nor the broader run-bounded theorem establishes that unrestricted inequality or its equality characterization. The comparisons concern coverage, not priority.

## value

PASS

The replacement gives a sharp global answer in a natural sparse-content class and proves that every maximizing word spreads its zeros nearly evenly despite allowing asymmetric placements. The unrestricted upper bound and structural equality case sharpen what the per-word formula or a balanced example can tell a researcher about extremal geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
