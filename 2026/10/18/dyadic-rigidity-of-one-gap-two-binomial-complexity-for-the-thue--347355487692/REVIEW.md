# Independent mathematical audit

## correctness

PASS

Every length n=2^m factor of the Thue–Morse fixed point is a cut suffix of φ^m(0) or its complement followed by a prefix of either block, since all four adjacent block-label pairs occur. For length-n factor w, the one-gap ordered-pair vector equals ordinary all-ordered-pair counts minus adjacent-digram counts; the explicit formulas for c=|w|_1, I=#01 ordered pairs, and E adjacency give the five P coordinates. φ morphism recurrences establish block I=h²/2 and parity-dependent E(T). The seven exhaustive block-cut parity parameter families and bit complements yield at most twelve polynomial profiles for both parities. An independently written SymPy rational-polynomial implementation reconstructed these symbolic families, found exactly 12 distinct vectors for e=0 and e=1, and certified pairwise noncollision for every h≥4 via a coordinate difference having one strict sign after h=4+t. The original proof realizes all relevant choices for m≥5 by occurrence of every digram in φ^{m−2}(0) and checks m=3,4 directly. Separately enumerated every four-pair-block cut at m=3..6 and independently scanned long Thue–Morse fixed-point prefixes: both yielded exactly the same 12 gap profiles. Finite checks do not replace the all-m realization proof.

## originality

PASS

Rigo–Stipulanti–Whiteland (ISIT 2023) explicitly conjecture a stronger 2-regular formula for the (1,2)-binomial complexity and state as an unproved implication exactly b_t^(1,2)(2^m)=12 for m≥3. Prior conjecture records the numerical conjectured value but does not establish it; this package supplies an all-m proof of that specified consequence, not the full 2-regular conjecture. Ordinary k-binomial complexity or 2-abelian complexity are different equivalence relations because adjacent pairs are included or local statistics differ. No stronger proved gapped-all-m classification was identified from primary reviewed material.

## value

PASS

This settles a natural and explicitly documented dyadic slice of an open conjecture about a named combinatorial complexity function. The proof gives an exhaustive parametric structural mechanism and infinite-length symbolic noncollision, not merely a finite census. Exact twelve-class stabilization at all dyadic lengths is a substantive mathematical answer even without proving the whole 2-regular conjecture or extending beyond dyadic lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
