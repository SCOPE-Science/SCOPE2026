# Independent mathematical audit

## correctness

PASS

PASS: The greedy next-occurrence automaton recurrence d(p)=1+min_c d(next_c(p)+1), with nonexistent occurrences valued zero, gives the full periodic comparison word G_m=(101000)^(m/2-1)101 distance table and exactly nine optimal absent strings. Inductive Cantor gap identity g_j=3^nu2(j) implies G_m is a subsequence of C_n, so no extra words are absent at shortest length. The skip-count for initial {00,01,11} and final {00,10,11} requires at least m+1 ones for any of the nine strings, while C_n contains m, so all nine are absent. Independent dynamic-programming recreation checked G_m for h=2..12 and C_n for n=2..5; proof handles every n.

## originality

PASS

PASS best-of-knowledge: Kosche–Koß–Manea–Siemer supply generic SAS definitions and algorithms, not the Cantor-family infinite-rank formula; Lü et al. analyze contiguous permutation/factor complexity, Chen et al. contiguous k-abelian complexity. Published Resultary binary universality distribution and Fibonacci extremals quantify over all words, not the specific nine-string language of these recursive iterates.

## value

PASS

PASS: Natural complete shortest-absence invariant of a classical recursive Cantor word, constant cardinality nine while the word length is 3^n and shortest absence length 2^n+1. Exact symbolic pattern and combinatorial explanation are structurally informative independently of downstream applications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
