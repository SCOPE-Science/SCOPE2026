# Independent mathematical audit

## correctness

PASS

The number of greedy complete binary arches equals the subsequence universality index. A Dyck word length 2n with n−1 arches has length surplus 2 over 2(n−1). Balance and nonnegative heights exclude rest of length2 and rest0 (one length4 arch or balanced length3 001/110 pair would cross below zero). Thus rest is exactly one final 1, exactly one exceptional 001 arch, preceding 2-letter arches all 01, following ones 01/10 arbitrarily. The distinct family count is sum_{j=1}^{n−1}2^(n−1−j)=2^(n−1)−1. Exact shortest-absent gluing via 2x2 forbidden-pair matrices gives row transformations (x,y)A=(x+y,y), (x,y)B=(x,x+y) and the exceptional 001 reset. The last 011 gives x+y and 101 gives x; Fibonacci coordinate induction shows max F_n, with one equality at n2,3 and exactly two alternating choices for n≥4. Independent exhaustive direct subsequence computation for n=2..7 checked counts, F_n maxima and number of maximizers; all-n follows from arch and transfer arguments.

## originality

PASS

The unrestricted binary SAS Fibonacci bound and exact binary universality distribution are already published; neither implies the Dyck-restricted penultimate-index class, its 2^(n-1)−1 exact enumeration and F_n extremizers. Full primary arch/SAS source was inspected. Best-of-knowledge originality PASS with bounded-search caveat.

## value

PASS

The class is a natural sharp boundary of subsequence universality under Dyck prefix balance; the exact enumeration and constrained Fibonacci extremum/equality cases are complete nontrivial combinatorial information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
