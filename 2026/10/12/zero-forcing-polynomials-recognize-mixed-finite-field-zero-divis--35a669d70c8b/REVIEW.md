# Independent mathematical audit

## correctness

PASS

Coordinate multiplication gives precisely the stated class sizes and disjoint-support adjacency. Double whites in a class prevent a first force into the class. If any singleton class is white, its support lies entirely in binary coordinates; the complement of an inclusion-minimal such white support has a nonbinary coordinate, hence an available blue vertex. Its only white neighbor lies in the chosen support, since disjointness from the complement is exactly containment in the support. After all singleton whites are gone, the same minimal-support step works for every remaining white support. This proves the product, the minimum complements and their count. For rank, order supports by increasing size and columns by their complements in the same order. The quotient becomes triangular with unit diagonal, since its entry is now 1 precisely when the row support is contained in the column's uncomplemented label. The complement permutation is an odd number of transpositions, so the determinant is -1. The lift with full-column-rank incidence matrix gives rank h, while M <= Z is the matching bound. The root count fixes r; the root product recovers the full subset product. Add the empty and full products with their multiplicities, use the multiplicity of 1 to recover binary factors, then strip the products of recovered factors as multisets. The least unexplained positive product is the next factor greater than 1; existing collisions do not matter when counts are subtracted. Finite fields are unique by order. Independent replay: python /workspace/audit_checks.py 4 tests all initial vertex subsets by direct multiplication in four mixed products and the binary exclusion; for (2,2,3) it obtains {3:8,4:36,5:66,6:63,7:33,8:9,9:1} and checks every complement profile. The all-binary example gives 2u+u², not the claimed product.

## originality

PASS

The material contribution is the exact standard forcing condition with both singleton and nonsingleton support classes, the resulting rank and the inverse from this polynomial. The class decomposition and exact graph order are prior. A catalogue theorem has the same symbolic polynomial, minimum-set count and rank on the all-nonsingleton side for co-maximal ideal graphs, but cannot be specialized to mixed supports. A same-day result has the same factor multiset for an automorphism-determining polynomial on a reduced co-maximal graph; this is not the standard zero forcing polynomial of the specified graph. Neither catalogue date decides priority. The multiple overlaps constrain distinctness but do not establish the full bound finding.

## value

PASS

This gives an exact propagation census and real minimum rank for a natural class in which some modules have no initial blue representative. The pure binary failure makes that distinction necessary, and root-multiplicity inversion is a concrete use of the full polynomial, retrieving the ring rather than just its order. The three-factor cross-overlap is real but leaves the arbitrary-factor classification and reconstruction useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
