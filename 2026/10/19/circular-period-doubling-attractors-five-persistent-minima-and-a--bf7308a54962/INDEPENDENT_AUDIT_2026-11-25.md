# Independent mathematical audit

## correctness

PASS

In a length-at-most-r|w| cyclic occurrence containing a block end, there are between 1 and |w| consecutive block ends. Their input letters give a legal cyclic input factor. Reposition it at an attracting occurrence while preserving the start offset and end padding: every non-end symbol is c, so the same output factor now includes a lifted mark. This works with wraparound and without injectivity of g. If there is no end, the factor is c^t with t≤r−1; a marked image ending in c supplies a run crossing its end. The lifted positions are distinct. My independent exact replay used two-adic valuation parity of one-based positions (the odd positions give 0 and the even positions flip the corresponding input letter), integer encodings of cyclic substrings, and a rolling window of exact occurrence IDs to test every bichromatic pair. At order three all lengths yield precisely (1,3),(1,4),(2,5),(3,5),(3,7). A two-element attractor must hit both letters, so it supplies the mark with g(a)=0 for the next period-doubling lift. Iterating i↦2i+1 gives the five formulas and optimality by the two singleton factors. For each order from 4 to 13, the listed lengths with bichromaticity left exactly the five predicted pairs. These filters are necessary for any attractor, and the lift gives sufficiency of every survivor; no sufficiency assumption about the test lengths is made. At order 13 the independent bichromatic scan gives 2733 candidates after length 2049, then 1369 after 1025 and 5 after 513, in a different filter order from the frozen log.

## originality

PASS

Credit the full five-position-family guarantee, exact finite census, and marked constant-prefix circular lift. Do not credit linear size two, the two previously classified linear pairs as linear attractors, or the bare circular cardinality conclusion as separate discoveries. In fact the latter follows from the known linear optimum two for every prefix and a periodic-prefix reduction. The compared sources do not supply the five specific circular choices, the finite exhaustion, or the general single-end lift.

## value

PASS

For a canonical substitution family, the exact choice and multiplicity of optimal marks are finer than the minimum size, especially since the circular seam permits more possibilities than the linear classification. The five formulaic configurations provide persistent witnesses, the finite census distinguishes those witnesses from a claimed all-orders uniqueness theorem, and the marked-end lemma isolates a size-preserving condition that applies beyond this substitution. The value does not depend on the bare number two or on extending the finite census arbitrarily.

The dated certificate retains the supplied scientific assessment, sources and limitations.
