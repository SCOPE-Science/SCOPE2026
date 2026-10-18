# Scientific review: fixed-weight-two single-deletion code capacity

## Correctness — PASS
For a weight-two word with one-positions \((i,j)\), the two possible one-weight deletion outputs are indexed by the distinct elements of \(\{i,j-1\}\). Hence a code with \(t\) adjacent-one codewords and \(e\) nonadjacent-one codewords obeys \(t+2e\le n-1\). Consecutive starting indices of adjacent-one words are impossible because a common weight-two descendant results. Thus \(t\le\lceil(n-1)/2\rceil\) and the upper bound is \(\lfloor(3n-2)/4\rfloor\). The stated construction has exactly this size, its weight-one outputs occupy pairwise distinct odd and even slots, and its weight-two output coordinates fall in disjoint adjacent and nonadjacent families. This proves an all-length bound; the accompanying direct-output and exact-clique checks confirm small and moderate instances.

## Originality — PASS, with limitations
The primary technical predecessor is Cullina, Kulkarni and Kiyavash (arXiv:1211.4056), who study the same fixed-weight graph and solve an associated chromatic-number problem, but that result does not imply the exact independence-number formula here. No (DOI: 10.3390/e21121202) gives nonasymptotic bounds for unrestricted binary deletion codes; these do not determine the weight-two optimum for every length. Comparisons also considered published unrestricted length-six single-deletion maxima and confusability graph motif counts; neither implies the all-length constant-weight-two capacity. Searches for alternative names and the specific proposed closed form found no covering statement. The risk of an equivalent formulation in an unindexed work is not eliminated.

## Mathematical value — PASS
The question is a natural capacity problem for a constrained deletion channel: find the exact largest recoverable message set when the transmitter must use exactly two ones. The result provides an optimal, explicit code for every blocklength and a sharp \(3/4\) linear leading coefficient. The matching obstruction makes the otherwise hidden collision among adjacent-one words decisive. It distinguishes exact packing capacity from existing coloring and unrestricted bounds, instead of merely refining a numerical table.

## Remaining scope
The code is restricted to binary weight-two words and exactly one deletion. No independent audit has been performed; direct enumeration is not an infinite proof, and undetected prior equivalence is possible.

Self-review: passed. Independent audit: not yet performed.
