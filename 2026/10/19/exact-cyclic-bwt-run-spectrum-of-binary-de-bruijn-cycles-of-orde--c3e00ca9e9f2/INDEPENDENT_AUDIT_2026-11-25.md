# Independent mathematical audit

## correctness

PASS

An order-five cycle uses all 32 labeled five-bit edges in the four-bit de Bruijn graph; the unique 00000 edge fixes a starting edge. The frozen DFS generates edge-label sequences, which may be rotated relative to a word written beginning with 00000, but still represent each cycle once. For an independent finite reproduction, python3 /workspace/branches/independent-05.py enumerates all 2^16 shift successors x=abcde ↦ bcde(a XOR f(bcde)). The two states with each tail must go to distinct successors in a cycle, so every order-five word induces exactly one such map; each map is a permutation, and orbit length 32 from state 0 is both necessary and sufficient. Because the first five bits of each rotation are all distinct, lexicographic row order is exactly integer state order. For each successor state y the last-column bit is the leading bit of its predecessor state, giving the full BWT without rotation sorting. This returned 20:38, 22:426, 24:840, 26:608, 28:130, 30:6, total 2048, mean 195/8 and variance 211/64. A separate literal rotation sort in that replay confirmed both printed witness words are order-five, begin with 00000, and attain 20 and 30 linear runs. The result does not quotient by reversal/complement and does not merge terminal runs. The frozen verify.py and VERIFICATION.md were inspected, not executed. The apparent published 18-run witness is not a counterexample: for L=1(0011)^7 010, direct LF calculation via LF(i)=16L_i+# earlier occurrences of L_i gives three cycles of lengths 22, 7 and 3, whereas a primitive 32-symbol cycle requires a single LF cycle.

## originality

PASS

The pair-block encoding, the one-cycle test and the total 2048 are prior. The earlier 18–30 bounds do not give the table; the proposed earlier witness at 18 runs is an invalid single-word last column under the earlier inverse criterion itself. Two later dated catalog results are verified exact coverage (one by marginalization); their stated dates and contents do not establish publication of either result before this record. The pass is for the genuine run-refined census and verified minimum, not for uniqueness in today's catalog or for the previously known structural characterization.

## value

PASS

Order five is a natural small binary de Bruijn census at which the accepted last columns have several distinct run counts and the proposed general lower-bound witness fails. The verified minimum 20 rules out the putative 18-run optimum; the exact multiplicities quantify the real spread and how many optimal cycles there are (38). The complete benchmark is useful for testing run-sensitive construction and extending to higher orders. No general-order lower bound or encoded bit cost is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
