# Independent mathematical audit

## correctness

PASS

The original package requires a narrow but genuine scientific correction: its T_n triple count is mislabeled as the number of circuits in the dual matroid. With M represented by [I_n|G_n], minimal supports of C_n^perp are circuits of M, whereas dual-matroid circuits correspond to minimal supports of C_n; the latter code has minimum distance 2·3^(n−1)+1≥7, hence no size-3 circuits. The full corrected RESULT.md replaces this false terminology at the theorem and proof and defines the two matroids explicitly. The surviving final theorem is correct: PG(n−1,3) has L=(3^(n−1)−1)/2 lines through P, each with 3 other points. Every point has two nonzero-vector copies; coordinate axes have a third identity copy. Minimal two-helper recovery iff the target and the two distinct helper projective points lie on a line, producing 12 pairs per line plus four per other axis and one extra for a two-axis line. Axes through a target weight-2 point share one line, yielding the 1_{h=2} correction. Local tripartite helper graphs K_{2,2,2},K_{3,2,2},K_{3,3,2} have matching numbers 3,3,4, and different lines have disjoint helper universes. Parallel target copies add 2 singleton helpers when h=1 and 1 otherwise. Direct independent enumeration of all nonzero vectors, projective lines, generator-column linear dependencies and exact integer counts for every target in n=2,3,4 verified the R2/A2/T formulas and code minima 7,19,55. The arbitrary-n proof is projective combinatorics, not extrapolation from finite checks.

## originality

PASS

Best-of-knowledge originality for the *corrected* exact local two-helper and sharp disjoint availability profile, not for the known systematic code, classical projective-line incidences, or general multiset formalism. Mondal–Lee Theorem 3.7 proves the family and codeword weight distribution. Grezet–Hollanti and Silberstein–Zeh discuss deleting simplex columns to obtain locality/availability rather than a fully duplicated nonzero ternary column set with one further copy on each coordinate axis. Jurrius gives simplex primal-subcode support enumerators. A fully read published Resultary theorem treats generalized Hamming support spectra of precisely this same code family, a distinct invariant not determining minimal dual-code local circuits or sharp helper-set packing. General projective incidence and matroid machinery makes the present formulas approachable but none of the inspected primary statements/implications dominates all h-dependent R2/A2 and T formulas. Search noncoverage is not proof of novelty; the inaccessible 2018 high-availability full text and possible unindexed weighted-projective enumeration remain explicit risks.

## value

PASS

The specific original family is motivated in coding theory and storage repair: it has ordinary locality one because each projective coordinate is repeated, but when a parallel copy is unavailable the number and maximum simultaneous disjoint packing of strictly minimal two-helper alternatives are a separate, natural structural invariant. The exact h=1, h=2 and h≥3 classification identifies a real projective incidence discontinuity from the unique line through two coordinate axes, and the all-n dual-code minimal-triple total T_n gives further relevant combinatorial information. These facts are not the mere known Hamming weight distribution or a small arbitrary instance, nor do they assert unverified reliability improvement. The result can be reused as an exact baseline for availability and erasure-tolerance analysis of replicated projective LCD codes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
