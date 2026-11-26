# Independent mathematical audit

## correctness

PASS

With wall indicators w, total walls W and adjacent wall pairs P, expand the nearest and next-nearest bonds to get H/J=−(1−κ)N+(2−4κ)W+4κP. The cyclic parity is even. A length-one domain admits a strictly lowering single flip for κ<1; with no adjacent walls, an interior single flip costs at least 4J(1−κ), and a boundary single flip is nonnegative. For a pair at distance ≥3 the single costs add. At distance two the only potentially negative correction is −4Jκ, when the pair spans exactly one wall. On the side with the equal-sign intervening bond, the end spin has single cost at least 4J if internal or exactly 4Jκ if it lies at the next wall, so the correction is harmless. For adjacent flips only the two exterior bonds are toggled. With both exterior bonds walls their removal costs 4J(2κ−1) (a length-two domain); with both exterior bonds wall-free the cost can be negative only when all five bonds in the affected stencil are wall-free, in which case it is 4J(1−2κ). With one exterior wall the wall count is unchanged and P cannot decrease. Five wall-free bonds mean a domain of length at least six or the uniform word. At κ=1/2 the energy depends only on P, so all one-stable words, including the uniform pair, are ground states. Rooting each nonuniform word at any of its 2r walls, then dividing by 2r, gives C(z)=−z(d/dz)log(1−F(z)²) for the allowed-length series F; the uniform contribution is inserted separately. The unique positive F=1 root gives a simple pole with coefficient asymptotic r^(−N), using consecutive allowed lengths to exclude any other equal-modulus pole. The three polynomials give the stated entropies and the smaller off-critical bases. Independently written exact spin-energy enumeration (branches/279b5cbe-624f-4d42-99b4-44d1f6e68306/independent_pair_check.py) tested all words and unordered pairs for N=8,9,10 at κ=1/4,1/2,3/4; counts in coupling order were (26,46,28), (38,74,36), (52,122,60), with no nonadjacent strictly lowering pair from a one-stable word. The source verifier was read, not executed. Finite enumeration corroborates but does not establish the all-N proof.

## originality

PASS

Credit the off-critical cooperative-stability classification and both entropy roots only. The one-spin baseline materially overlaps a separate Resultary finding, and the multiphase-point golden-mean degeneracy is established prior work. The inspected overlaps do not cover the simultaneous-pair constraints away from the multiphase point; Ismail–Hassan remains an access risk, not a negative result.

## value

PASS

This is a complete classification of a motivated cooperative stability test on a canonical frustrated chain, not merely a new way to count the known critical ground states. The change from eliminating short domains to eliminating long ones, and the two distinct exponential survival rates relative to single-spin minima, quantify how move-set enlargement changes metastability on either side of the multiphase point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
