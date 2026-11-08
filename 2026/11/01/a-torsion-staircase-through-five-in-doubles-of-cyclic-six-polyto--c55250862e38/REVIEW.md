# Independent mathematical audit

## correctness

PASS

PASS. The finite domain is exactly 7<=m<=16, with K_m=boundary of cyclic C(m,6) and double vertices unordered two-sets; faces are matchings whose union is a Gale-evenness facet face. Independently regenerated all Gale 6-facets, every 1/2/3-pair face, and full 2-dimensional simplicial poset for every m=7..16. Independently performed a complete sequential-toggle acyclic matching, directed-Hasse DAG topological sorting for every face, and oriented integer gradient-path Morse boundary, Hermite+Smith normal forms (with a separate program, not merely checking the reported stdout). The ten facet counts (7,16,30,50,77,112,156,210,275,352), all face vectors, critical cells and exact invariant factors agreed with source table: H1 torsion Z/3 at m=7; Z/2, Z/3, Z/4, Z/5 at m=10,12,14,16; no torsion at 8,9,11,13,15; H1 free ranks 0,15,0,24,0,35,0,48,0,63 and H2 ranks 20,78,134,263,384,610,818,1167,1484,1982. Raw and Morse modular ranks were independently cross-checked for primes 2,3,5,7. In particular m=16 Morse d2 has rank110, nonunit Smith factor5; H1=Z^63+Z/5, H2=Z^1982. The result claims only this finite range; no extrapolation to m>16.

## originality

PASS

PASS on checked source implications. Lesh–Schreiner–Wahl arXiv:2506.10436v1 defines the double and proves connectivity bounds using weak Cohen–Macaulay hypotheses; its full arXiv HTML does not state the cyclic-six-polytope exact integral H1/H2 table or order-five m=16 fact. Jonsson arXiv:1203.5650 gives Z/5 torsion for the ordinary matching complex on 14 vertices, a different complex (all disjoint pairings allowed), hence does not imply torsion in doubles of cyclic boundaries. No exact published table of these ten cyclic-boundary doubles was found in the searches, with standard risk of unindexed equal computations.

## value

PASS

PASS. Doubling is a natural recently introduced functor; six-dimensional cyclic polytopes are canonical neighborly polytopes with explicit Gale facets and natural smallest m=7. Exact integral homology through m=16, including the first order-five torsion and alternating free/torsion behavior, is a useful fully determined natural-family finite classification; no larger or infinite formula is needed for a meaningful exact invariant and no unsupported infinite torsion claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
