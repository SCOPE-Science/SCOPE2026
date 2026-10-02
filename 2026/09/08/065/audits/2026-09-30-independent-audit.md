# Scientific audit — SCOPE-20260908-065 — 2026-09-30

## Final claim assessed

For octal games .13337 and .13137, the committed Grundy tables through heap 12000 extend the public 10000-term tables; within those committed tables no candidate with preperiod at most 8000 and period at most 2000 closes, and the stated cold positions and extremal nimbers are exact for the finite window.

## Correctness — PASS

The committed C program implements the stated octal recursion directly and the independent Python verifier supplies a distinct mex implementation. The audit independently parsed the actual committed 12001-entry tables and rechecked the finite non-closure condition without relying on the missing witness generator: for each period p from 1 through 2000, a mismatch occurs at or after q=8000, which excludes every q at most 8000. The same independent pass reproduced both 10001..10010 slices, all cold positions, max 187 at 10736 for .13337, and max 229 at 7310 for .13137. OEIS pages for A071449 and A071448 document public tables only through 10000.

## Originality — PASS

OEIS A071449 and A071448 expose 10000-term tables and the documented shift relations; the this package extends both to 12000 and supplies a finite period-exclusion box and new finite extrema. Resultary returned no earlier matching record covering these same two parent games beyond 10000.

## Value — PASS

These are recognized difficult octal-game sequences with unresolved eventual behavior. A verified frontier extension plus a large explicit no-closure rectangle, a new cold position for .13137, and a new record nimber for .13337 provide concrete constraints for future periodicity/classification work.

## Residual risks and limitations

- Flammenkamp or independent hobbyist computations may exist beyond the linked OEIS tables without being indexed or formally published.
- The archived witness-matrix generator is missing, so the exact logged 'first failing index for every (q,p)' matrix was not independently reconstructed; the stronger scientific exclusion statement itself was independently rechecked from the tables.
- The result remains finite and gives no eventual-period theorem.

## Sources inspected

- OEIS A071448
- OEIS A071449
- OEIS references to Winning Ways and Flammenkamp; public 10000-term tables.
- Resultary query: octal game .13337 .13137 Sprague-Grundy period table
- artifacts/colds_*.txt
- artifacts/g13137_n12000.txt
- artifacts/g13337_n12000.txt
- artifacts/octal_dp.c
- artifacts/verify.py
- https://oeis.org/A071448
- https://oeis.org/A071449
