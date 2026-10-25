# Independent mathematical audit

## correctness

PASS

For a subset D of the m-by-n rook board, ordinary rook domination is equivalent to every row occupied or every column occupied; complement-total domination is equivalent to no row-column cross containing all D. For all occupied rows a>=3, exact cross-failure classification subtracts b z^a and ab z^(a-1)(U_b-z), whereas a=2 requires >=2 cells per row; full both-row-column coverage is E via inclusion-exclusion, with deficient cross-overlap mn z^(m+n-2)(1+z) except degenerate 2x2. Therefore the asserted F formula is correct. Sharp lower bound min(m,n) and cross obstruction lead to min=4 for m=2 and =m for m>=3; minimizing placement counts n^m-n-mn(n-1) or 2[...]-m! in square case follow by exact outlier/pigeonhole classification. Independent direct adjacency-mask brute force matched every coefficient and all minimum sets on 7 boards through 4x4 (71,504 subsets total), independent of the all-size combinatorial proof.

## originality

PASS

Bermudo et al introduce mixed ordinary domination of a graph with total domination of its complement for modular product families; Mertens solves ordinary domination polynomial of rook graph, but not the complement-total condition. The source’s all-size mixed enumerator and optimizer count require a different row/column cross exclusion.

## value

PASS

A complete counting polynomial, sharp mixed domination minimum and all exact minimizers on canonical Cartesian products of cliques is a motivated naturally defined graph invariant, distinguishable from ordinary rook domination or complementary total domination alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
