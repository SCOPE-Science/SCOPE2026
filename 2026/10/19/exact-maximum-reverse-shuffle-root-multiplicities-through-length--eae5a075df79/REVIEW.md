# Independent mathematical audit

## correctness

PASS

Independently exhausted the full range using half-word gluing rather than the frozen enumerator's length-2n position masks. In any interleaving with root r=ab split after k letters, if the first half uses k forward-root letters it uses exactly n-k letters of the reverse root. It is therefore a shuffle of a and reverse(b), while reversing the second half gives another shuffle of those same two strings. Conversely any two such half-shuffles concatenate, reversing the second one, to realize r. The reproduction recursively forms distinct half-shuffles, takes all ordered pairs for each of the n+1 splits of every root, and deduplicates across splits by stamping each word with its last root. Scanning the full labeled universe returns maxima 1,2,3,5,9,16,29,52,94,170 and optimizer counts 2,4,8,8,8,8,8,8,8,8, with all optimizer sets matching profile.txt and the eight length-20 words matching RESULT.md. A direct grid interleaving test agreed on all words through n=5 and on every optimizer through n=10. Both halves of a realizable word have the same letter counts by the split argument; conversely if counts agree, take a and b to be the monochromatic zero and one blocks of those lengths. Thus coverage is binomial(2n,n), agreeing with the run, including 184756 of 1048576 at n=10. The frozen enumerate.cpp and profile.txt are present and were read, not executed; the C++ bitset merges repeats of a root correctly. A separate read-only check verified each of the 170 supplied witness selections for the first listed optimizer. Replay: python3 /workspace/branches/reverse_halves_review.py 1 7 and python3 /workspace/branches/reverse_halves_review.py 8 10 (NumPy); outputs /workspace/branches/reverse_halves_1_7.txt and /workspace/branches/reverse_halves_8_10.txt. The conclusion stops at n=10.

## originality

PASS

The exact distinct-reverse-root extremal profile and optimizers through length 20 are the supported distinct claim. The characterization and number of coverable binary words are prior results used only as checks; the analogous ordinary-root table uses a different operation.

## value

PASS

This is the per-word ambiguity of a natural word operation whose binary existence condition is already known. Length 20 is a meaningful matched cutoff with the published ordinary-shuffle profile; 170 versus 19 and the exact optimizer sets give a reusable extremal benchmark and test instances. The result is finite, not evidence of an infinite recurrence or asymptotic law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
