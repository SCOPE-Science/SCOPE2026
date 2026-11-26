# Independent mathematical audit

## correctness

PASS

An inverse start is precisely an eight-letter palindrome, and deleting its final four letters is the inverse for the stated reversal channel. Two such starts separated by h=1 or 2 imply y_j=y_(j+2h) on the common reflection range by composition. For h=1 and h=2 the required remaining substrings after deleting four are equal since the period divides four (the compared positions are j=4,…,3+h and j+4 in local coordinates). One representative per distinct parent has spacing at least three in the n−3 start positions. For the period-three witness with a≠b, each start i divisible by three sees the palindrome aabaabaa; for i<j the deletion at i gives b at output index i+4 while the deletion at j leaves a there. The later legal start ensures that coordinate and y_(i+8) exist. This also covers n=4, when there is just one start, and uses only equality of letters, so q≥2 suffices. Frozen notes, code and stored output were inspected without executing the upload. Independent forward-image enumeration (deduplicate each parent's children) checked q=2,3,4 for n=4 through 11,8,6 respectively; replay with python3 /workspace/branches/independent_bounded_checks.py. Neither census replaces the all-length proof.

## originality

PASS

Qualified to the exact sharp result and period-three attainment for every n and q≥2. The adjacent-start collision is known, and the October 26 boundary proof already gives the distance-two collision locally, so the one-third upper bound follows immediately from prior arguments; those mechanisms are not original here. The decisive extra step is the all-length matching construction with distinct parents. A distinct November 2 general theorem covers this exact specialization, but its later catalogue date does not establish that this result was pre-empted. No earlier exact all-length sharpness or equivalent witness was established in the inspected sources.

## value

PASS

The exact worst-case number of distinct parents is a natural local decoding ambiguity, not a count of syntactic edit positions. Length four is the first case outside the earlier uniform formula for blocks not divisible by four. Even though the sharp upper bound follows from known local collisions, proving that one receives that many distinct parents in every length gives a substantive exact invariant and identifies a simple witness. This is not a claim about codebook optimality or about multiple errors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
