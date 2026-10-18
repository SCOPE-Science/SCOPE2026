# Independent mathematical audit

## correctness

PASS

For n-bit prefixes of (ps)^infinity with palindrome p,s and root length d<=n, each distinct d/c split yields exactly 2^(ceil(c/2)+ceil((d-c)/2)) distinct word models. Summation gives S_d=3d*2^(d/2)/2 (even d) and d*2^((d+1)/2) (odd d). For d>=n-L and split cuts away from both endpoints, the two reflection matchings of any distinct models differ on a linear number of positions; after contracting first-matching components, a max-degree-2 graph forces a linear drop in free binary choices. Thus pair intersections are exponentially negligible versus n*2^(n/2), for fixed L and cut-margin delta. Upper bound via sum S_d, lower by two-term inclusion exclusion; take n->infinity then delta->0 then L->infinity, obtaining even coefficient 5 of n*2^(n/2) and odd 7/sqrt(2). Independently re-enumerated n=6,8,10,12,14 and got 58,190,560,1574,4116 using explicit palindrome root constructions. This finite enumeration does not establish the asymptotics.

## originality

PASS

Fici, Shallit and Simpson explicitly pose the asymptotic number P(n) in Section 7 of their 2025 paper as open; their exact small-term sequence and a coarser order lower bound do not imply either leading coefficient. Earlier work on palindrome-pair root counts and overlap does not give near-disjoint periodic-prefix models with bounded root-length deficit. The matching-overlap estimate is the substantive new ingredient. Best-of-knowledge PASS.

## value

PASS

Resolves a precise published open asymptotic counting question with different even/odd leading constants, using a structural overlap bound that explains why representations mostly disjointly contribute at the dominant scale. It is a natural exact language-enumeration result, not a chosen arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
