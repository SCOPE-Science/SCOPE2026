# Independent mathematical audit

## correctness

PASS

The path maximal independent sets are exactly independent dominating sets. Recursive decomposition on the first vertices gives 16 distinct P_10 concepts, independently exhaustively recomputed from adjacency. Their membership frequencies are (9,7,5,8,6,6,8,5,7,9); since only positions 4 and 7 occur in exactly 8 of 16 concepts, no four columns can realize 16 patterns, while columns {1,4,7} shatter all 8. An explicit complete depth-four adaptive query certificate with 16 distinct leaf concepts was fetched and checked for consistency; cardinality 16 excludes depth five. Disjoint-union maximality factors componentwise, so VC dimensions sum; concatenating complete adaptive trees gives Ldim>=4m and cardinality 16^m bounds above. For degree at most one, every edge contributes one independent binary choice and isolates are fixed. Independently exhaustively enumerated P1..P10 concept sets and VC/Ldim recursion, reproducing minimality profile and 256 two-block products. The finite P10 census plus arbitrary-product proof establishes the infinite gap without extrapolation.

## originality

PASS

Chase–Freitag define/generalize Littlestone/thicket shattering; maximal independent dominating sets are an established graph class. Guingona et al. prove VC/Ldim equality for zero sets of *full linear-combination classes*, not these memberships (which exhibit strict inequality). Ghazi et al. give general Boolean aggregation bounds and Song–Yao count MIS but neither provides this exact first path or degree threshold. Resultary graph results discovered are about domination/other graph parameters, not the same pair of shattering dimensions.

## value

PASS

This is a sharp structural degree threshold distinguishing static and adaptive shattering of an elementary natural graph concept class; one finite certified P10 witness plus a general disjoint-union amplification proves an unbounded difference. The specified narrow graph order is motivated by minimality, not a randomly chosen finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
