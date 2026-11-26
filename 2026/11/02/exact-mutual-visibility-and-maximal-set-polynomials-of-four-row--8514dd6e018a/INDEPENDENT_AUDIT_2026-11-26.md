# Independent mathematical audit

## correctness

PASS

For a diagonal pair in a rectangle the only shortest internal vertices are the two cross corners, so all-set admissibility is exactly pairwise disjointness of the row pairs used by columns. With no triple or quadruple the double columns inject into six pairs; with a triple they inject into the three edges from the omitted row, and with a quadruple none remain. Empty or singleton columns yield a factor 1+4z each. For maximality there are no empty columns, a singleton must be on a degree-three row in the graph of used pairs, and a double column's edge must dominate every other row. With a triple present, at least one link to the omitted row must be occupied in a double column, and t=1,2,3 gives singleton alphabets 1,2,4. In the doubles-only regime the complement of the used-pairs graph is a union of cliques (two nonedges with a common endpoint force the third nonedge). This gives the star, cycle, K4 minus one edge, and K4 once the extendible all-singleton case is removed. The cycle has no degree-three row, hence needs n=4 and is excluded by n>=6. Injective column assignments for these structures and the full-column configuration give the stated four coefficients. The largest competing-to-maximum term ratio is 64/((n−4)(n−5)); all other ratios are O(n^−3) or smaller. Thus the claimed probability concerns uniform sampling from maximal sets, not greedy sampling. The independent replay branches/independent-replays/rook.py used row masks (not occupied-column-type enumeration), intersected row subsets, and computed each row's forbidden extensions from other rows sharing a column. It checked every admissible set at n=2..6 (1,587,227 total), the V_n coefficients, and the n=6 maximal counts (6984,11520,31680,720) at sizes 9 through 12. This is corroboration; the structural proof establishes the full ranges. Frozen code was inspected, not run.

## originality

PASS

For the repaired attribution, the distinct claims supported by the comparison are the full V_n, the full M_n including three larger cardinality strata beyond the covered minimum coefficient, and the uniform-maximal asymptotic. The rectangle characterization, definition of visibility polynomial, extremal sizes already implied by prior results, and the minimum-size multiplicity are not novel components.

## value

PASS

The four-row shore is a natural fixed-width graph family in which subsets and terminal configurations can both be counted structurally across arbitrarily many columns. The complete counts quantify the gap between existence of small maximal sets and the fact that almost every uniformly sampled maximal set is largest, with a sharp leading asymptotic deficit. This is not just a new derivation of the known minimum coefficient, and no assertion about a greedy distribution is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
