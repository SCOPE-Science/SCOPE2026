# Independent mathematical audit

## correctness

PASS

The committed C program implements the stated octal recursion directly and the independent Python verifier supplies a distinct mex implementation. The audit independently parsed the actual committed 12001-entry tables and rechecked the finite non-closure condition without relying on the missing witness generator: for each period p from 1 through 2000, a mismatch occurs at or after q=8000, which excludes every q at most 8000. The same independent pass reproduced both 10001..10010 slices, all cold positions, max 187 at 10736 for .13337, and max 229 at 7310 for .13137. OEIS pages for A071449 and A071448 document public tables only through 10000.

## originality

PASS

OEIS A071449 and A071448 expose 10000-term tables and the documented shift relations; the assigned package extends both to 12000 and supplies a finite period-exclusion box and new finite extrema. Resultary returned no earlier SCOPE record covering these same two parent games beyond 10000.

## value

PASS

These are recognized difficult octal-game sequences with unresolved eventual behavior. A verified frontier extension plus a large explicit no-closure rectangle, a new cold position for .13137, and a new record nimber for .13337 provide concrete constraints for future periodicity/classification work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
