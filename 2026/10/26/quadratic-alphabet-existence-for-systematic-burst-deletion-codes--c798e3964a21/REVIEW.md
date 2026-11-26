# Independent mathematical audit

## correctness

PASS

With M=n+t+1, the full word set partitions into equal parts of size q^(t+1) by literal prefix. At each r≥1 a word has at most B_r=M−r+1 descendants; a descendant has at most B_r q^r preimages by block reinsertion, including the starting word. Thus the degree of the union over 1≤r≤t is at most the sum of B_r(B_r q^r−1), which is at most M²(q^(t+1)−q)/(q−1) and strictly less than q^(t+1)/2 when q>2M²+1. The hypotheses of the independent-transversal criterion hold, so one representative per prefix suffices; r=0 uses distinct codewords and different r give different output lengths. The least power of two above 2M²+1 is strictly below twice that odd integer. The proof covers trailer deletions since positions are counted in the full transmitted word.

## originality

PASS

The prefix-transversal framework and the one-length insertion/descendant counting argument are directly antecedent. The supported distinct guarantee is simultaneous correction of all contiguous lengths through t with exactly t+1 deletion-prone appended symbols at quadratic alphabet size, independent of t in the exponent. None of the closest inspected claims dominates the full resource and correction regime.

## value

PASS

Deletion-prone systematic redundancy is the substantive constraint. Through t=2 the result attains the necessary three trailer symbols with a quadratic rather than quartic alphabet-size guarantee, at the stated cost of losing efficient encoding. For arbitrary t it keeps the exponent fixed while retaining the t+1-symbol trailer. This is a meaningful resource-regime gain over the inspected existence benchmark, despite the short degree estimate and standard transversal step.

The dated certificate retains the supplied scientific assessment, sources and limitations.
