# Independent mathematical audit

## correctness

PASS

All 4-subsets are facets of rank4 by four-neighborliness, and 8-facets of even-dimensional cyclic C(n,8) are unions of four disjoint edges of cycle C_n by Gale evenness. D4 is 1-dimensional (no 12-vertex facets), with V=C(n,4), #facets F_n=n(n−5)(n−6)(n−7)/24 and E=35F_n (unique 8-union per edge). For path-edge subgraph H_n, complementary 4-subsets preserve the three parity classes j=0,1,2. I checked the written induction: n=10 finite base has 210 vertices/15 path facets/525 edges, component sizes 10,100,100. For any new T containing last label, use forced last path edge and cover at most 3 other marked vertices by 3 disjoint edges in an N=n−2>=9 path; if N odd, at least one unmarked even-indexed vertex can be omitted, leaving perfectly matched even paths. Thus every new vertex connects to old same-j component. Even-n closing edge preserves parity and no classes merge. Odd-n wrap edge connects 4→1 and 3→2 parity-count types and merges all three H_n classes; n=9 KG(9,4) connected via one-vertex exchanges. For even n, each facet has four even/four odd and contributes respectively 1,16,18 distinct edges to classes, giving E_j and the stated ranks. Independent regeneration for n9..17 checked F_n, edge counts, parity components and betti ranks; finite examples are only a cross-check, not the proof for all n.

## originality

PASS

The natural source Lesh–Schreiner–Wahl defines r-tuplings and proves only weak Cohen–Macaulay lower bounds. At input sphere dimension7 and r4 the cited bound is dimension 0, insufficient to determine component count, parity graph or π1 ranks. Gale evenness characterizes facets but supplies no graph connectivity. A previous D2 result on cyclic 4-polytope boundaries is a different r, input dimension and edge predicate; it does not force these three four-tupling components.

## value

PASS

The boundary of the neighborly cyclic eight-polytope is a canonical simplicial seven-sphere. Its four-tupling, a natural extension of the recently introduced double, exhibits an exact odd/even connectivity phase transition and three distinct parity-complement components; four is the first tuple size admitting three complement-invariant classes. Uniform formulas for all integral first-homology circle ranks and a constructive parity mechanism make this a substantive structural theorem, not a finite tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
