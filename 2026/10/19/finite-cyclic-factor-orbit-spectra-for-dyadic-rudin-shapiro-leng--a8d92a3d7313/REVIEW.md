# Independent mathematical audit

## correctness

PASS

For binary index i, take the state pair (parity of adjacent 11, last bit), encoded 0=(0,0), 1=(0,1), 2=(1,1), 3=(1,0). Appending a 0 preserves the parity and sets last bit zero; appending a 1 adds the old last bit and sets last bit one. These are precisely the stated uniform images, proving the sequence identification. All eight state pairs occur by the fourth substitution and expanding these pairs introduces no other pairs. Every length-2^k window meets at most two aligned blocks of length 2^k; each allowed pair really occurs, so the eight concatenations with offsets 0 through 2^k give exactly the infinite word's factor set. The separate exact replay at /workspace/branches/8bdc29b3-6289-4e2b-8b53-2f5c60787748/independent_replay.py uses fixed-width integer factor keys and exact lexicographic least rotations, with no probabilistic equality. Its class sizes count represented factors, not cyclic positions. /workspace/branches/8bdc29b3-6289-4e2b-8b53-2f5c60787748/replay_4_13.txt lines 3–12 give all ten complete rows and line 13 gives REPLAY_OK. Endpoint rows (n, factor total, class total, singleton, double, full) are (16,120,58,52,2,4) and (8192,65528,32762,32756,2,4). The replay tests that no other class sizes occur. The frozen C++ verifier was inspected, not run. This is exhaustive only for k=4 through 13, with no inference outside the range.

## originality

PASS

The number four for complete primitive classes at these dyadic lengths is already covered by the two checked Rudin–Shapiro records. The distinct accepted content is the exact finite histogram of partially represented classes, in particular the two doubletons, the absence of intermediate multiplicities other than two, and the resulting full census. The complete-orbit statistic and the total number of ordinary factors do not determine this histogram. This is a bounded comparison, not a priority certificate.

## value

PASS

Rudin–Shapiro is a standard substitution word and occupancy of represented necklaces distinguishes nearly rigid factors from freely rotatable ones. The ten substitution-aligned scales give a reproducible exact benchmark for the intermediate cases that ordinary factor complexity and Lie complexity omit: only two partial classes contain more than one factor at each scale. The highest scale is a computational cutoff, not a claimed structural threshold; the value is in the complete aligned census rather than in guessing an infinite law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
