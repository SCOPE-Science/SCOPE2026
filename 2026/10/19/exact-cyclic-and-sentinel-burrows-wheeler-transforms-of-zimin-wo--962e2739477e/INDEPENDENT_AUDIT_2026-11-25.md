# Independent mathematical audit

## correctness

PASS

For Z_n let m=|Z_{n-1}|. Even starts have predecessor 1 and sort after all odd starts; the extra sentinel start sorts before both groups and also has predecessor 1. For odd starts, replace each parent letter a by (1,a+1) and the terminal marker by (1,0). First differences are preserved including a parent suffix ending earlier. For cyclic rotations that last comparison instead reads the seam (1,1), still smaller than (1,a+1); that comparison fits within a full rotation because the shorter of two distinct parent suffixes has at most m-1 positive letters. Predecessors lift by a↦a+1 off the first start, and the first start has predecessor 0 with a sentinel and 1 without it. Therefore the sentinel recursion prepends 1, relabels the parent last column and appends m ones; the cyclic recursion drops that first 1 and changes the unique 0 to 1. Starting at B_1=10 gives both claimed formulas. C_1=1 and C_2=211, while for n≥3 exactly 2n−1 adjacent-distinct blocks remain. The input alternates 1 and a larger symbol, so it has 2^n−1 runs. Reviewed RESULT.md §§1–5 and the sorting code in verify.py; the recorded level-16 checks are finite corroboration, not the proof, and were not executed for this review.

## originality

PASS

The verified exact catalog overlap is real for the entire cyclic component, including its run count, but is recorded under a later date (2026-11-02 versus 2026-10-19); no earlier derivation of the all-rank pair was established. The later item explicitly excludes the end marker. The period-doubling reduction and fixed-alphabet morphic bounds do not imply the ordered transforms. The assessment is for the paired all-level formulas, not an assertion that every special case is first or that the cyclic formula is unique in the current catalog.

## value

PASS

These are exact transforms of the canonical finite ruler/Zimin hierarchy, not a numerical instance. The odd-start correspondence explains when the sentinel and seam order agree and turns run counting into an exact block law. It exhibits 2n−1 runs after transforming an input with 2^n−1 runs, and supplies reproducible reference transforms under both common conventions. This is a run bound, not an encoded bit-cost bound for a growing alphabet.

The dated certificate retains the supplied scientific assessment, sources and limitations.
