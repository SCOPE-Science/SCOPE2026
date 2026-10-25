# Independent mathematical audit

## correctness

PASS

Define a closed nonempty word by a proper nonempty border with exactly two occurrences, allowing overlaps, and singleton as closed. For a binary de Bruijn circular word B of order h, any closed factor with border length >=h would repeat an h-factor at two distinct cyclic starts, impossible for factor length <=N=2^h; thus b<h. For each starting position and b<h, at most one complete first return exists, yielding upper bound 2+(h-1)N distinct circular closed factors. Linear closed-factor lower bound N holds for any cut of length N; linear factors embed among circular ones. For h=5, exhaustive directed de Bruijn graph local switches (2^16 pairings) and independent edge-simple Euler tours both give the 2048 rotation classes; independent direct border and first-return counts agree: 93:360,94:888,95:600,96:200, mean 1509/16, variance 195/256. An independent local 2048-cycle re-enumeration reproduced that histogram. The computer proof is exhaustive only at h=5; universal bound uses the injection.

## originality

PASS

Best-of-knowledge statement-and-implication comparison; not a priority certificate. A full paper and targeted Resultary search were inspected as described below.

## value

PASS

Closed factors encode complete first returns; de Bruijn universal cycles are a natural extremal family. The all-order O(N log N) upper bound separates their return complexity from quadratic unrestricted closed-rich words. The complete h=5 census is a natural finite classification (all 2048 distinct cycles, four consecutive attainable counts), furnishing exact invariant distribution, moments and benchmarks, not arbitrary slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
