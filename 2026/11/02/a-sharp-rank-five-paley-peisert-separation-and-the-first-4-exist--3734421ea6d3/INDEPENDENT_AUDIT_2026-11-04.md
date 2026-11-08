# Independent mathematical audit

## correctness

PASS

For Peisert P*(q) at q=p^(2e), p≡3 mod4, quartic-coset adjacency D={g^j:j mod4∈{0,1}}, explicit irreducible polynomial models were checked for q=9,49,81,121,361 and primitive generators. The tuples (0,1,2,3) at 9 and49, (0,1,2,42) at81 and (0,1,16,17) at121 have a zero four-extension count (not necessarily same pattern), ruling out all smaller eligible orders. For q=361, translations and fourth-power multiplications reduce every unordered four-set and adjacency mask to (0,b,c,d) with b∈{1,g,g²,g³}, 1≤c<d<361, c,d≠b; exactly 4*binom(359,2)=257044 cases. Independent bit-mask exhaustive census (new implementation) returns global min10, attained at (0,1,2,3). For q121 translations reduce to all binom(120,3)=280840 anchored four-subsets; independent complete enumerations show Paley min2, zero failures; Peisert min0, 400 failing anchored tuples. Both 3-e.c.: all binom(120,2)=7140 anchored triples have minimum 12 (Paley) or11 (Peisert). Both share (121,60,29,30) by exact field count. Their 3-extension property gives a four-round back-and-forth strategy, so rank≤4 elementary equivalence, while ∃4 distinct vertices with no common neighbor is a rank-five sentence true for Peisert and false for Paley, giving sharp depth. Finite exhaustive ranges are mathematically complete because of the supplied orbit reduction, not extrapolated to all larger orders.

## originality

PASS

PASS qualified: classical Peisert construction, finite-field graph pseudorandomness and Rado extension logic are earlier; the exact first Peisert 4-e.c. order, tenfold extension minimum, q=121 Paley–Peisert first-order rank-five separation do not appear in inspected thesis and retrieved primary summaries. Inaccessible Kisielewicz–Peisert 2004 full text leaves a concrete historical priority risk.

## value

PASS

Peisert and Paley at order 121 share full strongly regular parameters, so an explicit difference at the first separating first-order quantifier rank is a natural model-theoretic invariant. The first order with Peisert four-extension property and its exact min10 matter to finite pseudorandom extension thresholds; exhaustive finite classification is independently meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
