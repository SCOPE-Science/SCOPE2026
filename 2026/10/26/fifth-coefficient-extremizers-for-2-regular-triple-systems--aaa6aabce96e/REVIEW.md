# Independent mathematical audit

## correctness

PASS

For simple 3-uniform 2-regular H on n>=9, m=2n/3 hyperedges and each 5-set contains at most three hyperedges by 3h(S)<=10. Inclusion-exclusion is exact: i5=binom(n,5)-m binom(n-3,2)+n+(n-6)p2-t, since p1+2p2=n and t counts edge-triples of union size5. Overlap-size-two pairs form a matching on m hyperedges, so p2<=m/2=n/3; t>=0 proves the sharp claimed upper bound. Equality requires p2=n/3 and t=0; the dual cubic multigraph then has perfect matching of doubled edges and the remaining single perfect matching, forcing even alternating cycles length>=4 (length2 would require forbidden triple multiplicity). The alternating family forces t=0 and attains the bound for all n divisible by3 >=9. Independently all 640 labeled admissible cubic dual graphs on six vertices verified the identity and maximum54 (120 extremizers), plus examples n=9,12,15 with counts54,540,2403.

## originality

PASS

The published 2026 Sarantis--Tetali--Zheng work formulates the coefficient-wise problem and resolves total weak-independent-set inequality at degree2, but their Proposition3.3 is about k=4 under a no-cross-edge restriction. The 2026-09-30 published Resultary theorem gives unrestricted k=4 extremizers, including the SAME alternating-cycle family; that prior equality classification is expressly acknowledged. The newly assessed object is the fifth coefficient and its exact all-order upper bound, which additionally needs the five-set triple-overlap correction t. Best-of-knowledge searches found no existing k=5 formula.

## value

PASS

The fifth weak-independent-set coefficient is the next natural unsolved slice of a published coefficient-wise extremal conjecture for 3-uniform 2-regular systems. Exact inclusion-exclusion through three edges determines a new all-order sharp numerical coefficient and proves equality for the complete natural family, yielding reusable exact enumerative data; prior k4 matching/equality structure is acknowledged and not claimed as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
