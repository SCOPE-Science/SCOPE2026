# Independent mathematical audit

## correctness

PASS

Between the first and second deleted positions in a pair of words, there is exactly one pending letter in the other word; when the alignment closes, only equality is allowed. This verifies the frozen recognizer and product semantics. Equality is intentionally accepted when calculating P_n and A_n. Each of the three pair-equality events contains P_n ordered triples, and every intersection of two or three events contains 4^n all-equal triples. Inclusion–exclusion and division by six give T_4(n)=(A_n−3P_n+2·4^n)/6, and substitution gives the asserted polynomial and leading coefficient 405/288=45/32. Independently reconstructed the original 27- and 1549-state dimensions and verified exactly the corresponding annihilator checks through lengths 31 and 1556 without running the frozen script. A separate check used a different recognizer: discard the common equal prefix (an equal first symbol can be retained in a longest common subsequence), start the three possible deletion paths at the first mismatch, then quotient pair and triple machines by simultaneous alphabet relabeling. This gave dimensions 6 and 159 and reproduced the formulas and all required consecutive zeros for those dimensions using exact arithmetic. In either computation Cayley–Hamilton applied to uM^nQ(M)f extends d consecutive zeros from n=1 to every positive n; matching the initial positive indices uniquely identifies the two closed forms. In particular the formula need not hold at n=0. Independent direct deletion-set enumeration gives T_4(n)=4,172,2484,23968,187648 at n=1,…,5.

## originality

PASS

The supported distinct assertion is the exact radius-one triangle count and leading constant for the four-letter deletion graph. The general deletion graph and triangle-bound program are prior, as is the finite-state method and exact count for two symbols. The inspected stronger-domain bound does not fix this exact invariant, and the inspected exact indexed formulas count different objects.

## value

PASS

Triangles are an established invariant for assessing sparsity in deletion-confusability graphs. Four letters are a natural fixed nonbinary alphabet, and radius one is the first deletion regime. The exact count supplies a reusable reference, removes the logarithmic loss of the relevant broad upper bound for this fixed graph, and gives an explicit leading constant and finite-size corrections rather than an unproved extrapolation. No new coding-rate implication is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
