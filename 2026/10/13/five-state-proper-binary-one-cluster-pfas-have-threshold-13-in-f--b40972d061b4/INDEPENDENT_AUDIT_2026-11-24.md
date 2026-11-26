# Independent mathematical audit

## correctness

PASS

Properness and the one-cluster condition jointly force exactly one total letter and require its functional graph to have one directed cycle. As an independent count check, classify total maps by the cycle length: the cycle choices times the number of rooted forests feeding the prescribed cycle vertices give 625, 500, 300, 120 and 24 for lengths 1–5, hence 1,569. There are 6⁵−5⁵=4,651 partial nontotal maps, so the ordered candidate total is 2·1,569·4,651=14,594,838 without duplication. A letter edge in the subset graph exists only if every active state has a defined image; each visited set is nonempty. BFS from the full set thus gives the shortest careful length exactly when some singleton is reachable. Reverse multisource BFS in the companion code verifies distances by a second traversal but shares its transition routine. A separate bounded independent implementation exhausted the full candidate set and matched all histogram entries and the sync total 8,206,270. The maximum finite length is 13, with 1,200 labeled cases. Canonicalization under S5 and letter exchange matched all five representatives and sizes 240; separate scalar BFS replay confirmed the five shortest words, including the three copies of bbababbbababb. Nonsynchronizing inputs have no finite threshold; complete DFAs are excluded even if one-cluster.

## originality

PASS

The supported distinct finding is the exact five-state restricted threshold and equality census. The total-letter functional-graph definition, finite power-automaton method and broader binary PFA enumerations are prior; no inspected source gives the joint one-cluster/proper filter's maximum and classes.

## value

PASS

One-cluster structure arises naturally in synchronization theory: a total letter with one basin is a standard structural competitor to unrestricted transitions, and properness separates careful reset from familiar complete examples. The exact drop from the unrestricted five-state proper-binary maximum 15 to 13 and the equality classes quantify the effect of that restriction and give reusable test cases for proposed bounds or algorithms. This is a meaningful small-order benchmark, not a general upper-bound theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
