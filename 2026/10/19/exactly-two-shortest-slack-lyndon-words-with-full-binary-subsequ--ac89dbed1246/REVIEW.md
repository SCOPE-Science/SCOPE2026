# Independent mathematical audit

## correctness

PASS

The greedy arch criterion gives the length bound: the last letters of successive arches are matched first at the successive arch ends, so appending a symbol absent from the remainder gives a missing subsequence. A binary Lyndon word containing both symbols starts with 0 and ends with 1 (a trailing zero-run would extend its leading zero-run under rotation). At length 2k the arches are pairs; the initial 01 forbids all 00, so the only candidate is (01)^k, strict only for k=1. At length 2k+1 an initial 01 likewise forbids 00, hence k zeroes delimit k positive one-runs with one doubled run. Lexicographic minimality puts the doubled run last. An initial 00 forces a first arch 001 and pair arches thereafter, ending in 01. If any 10 occurs, rotate from the second letter of the last 10; with b trailing 01 arches the new prefix is 001(01)^(b-1)00. Compare with the original prefix 001(01)^a10 up to its first 10: the rotation wins whether b-1<a or b-1>=a. Thus all suffix arches are 01. Both resulting words pass the strict rotation comparison, are reverse-complements, and contain k arches. The disjoint arch/remainder counts are 2^(k+1) and k2^k, including k=1. Inspected RESULT.md §§1–5 and the finite-check design in CHECK.py; no supplied code was executed.

## originality

PASS

The supported distinct contribution is the exact classification of lexicographically least strict rotations that are themselves linearly universal, not arch theory, unrestricted counting, circular counts, or priority for the related unbordered threshold and witnesses. The strongest indexed comparisons materially overlap but do not supply the two-word Lyndon filter.

## value

PASS

There is a natural extremal question: for a canonical primitive rotation representative, what is the least length that can carry the full linear subsequence spectrum, and which representatives attain it? The result eliminates all but two out of an exponential first-slack linear family. It separates a genuine least-cut constraint from merely counting admissible rotation classes, and gives exact test cases for that distinction at all k.

The dated certificate retains the supplied scientific assessment, sources and limitations.
