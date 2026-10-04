---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
Compile and run `verify.cpp` with a standards-compliant C++17 compiler. The checker builds the exact largest-prime-factor table through \(41472\), enumerates every odd \(k\le20735\), starts from every prime \(p\le k\), and identifies all directed cycles.

Acceptance requires the program to print `VERIFY_OK`, the strict odd-\(k\) record sequence ending in
\[
(20735,36),
\]
the exact loop count \(36\), and the period histogram
\[
4:6,\quad6:14,\quad8:10,\quad10:5,\quad12:1.
\]

The finite exhaustiveness rests on the symbolic reduction proved in `RESULT.md`: for odd \(k\ge3\), every loop contains a prime \(p\le k\), and trajectories from those primes remain in \(2\le x\le2k+2\). Thus no unscanned initial value can contribute an additional loop.

`cycles.txt` records the exact successful replay and all 36 canonical cycles.
