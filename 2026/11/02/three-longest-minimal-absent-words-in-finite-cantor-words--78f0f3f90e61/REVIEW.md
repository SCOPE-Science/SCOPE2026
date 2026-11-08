# Independent mathematical audit

## correctness

PASS

C_k=C_(k-1) 0^G C_(k-1), G=3^(k-1), with W=C_(k-1) and V=C_(k-2). W has longest proper border H=3^(k-2) and maximal zero run H. For length G the only repeated strings are W at starts 0,2G and F=0^H V 0^H at H,2G-H: cross-copy equality forces two exterior zero runs a,b<=H and a border of W of length G-a-b>=H, hence a=b=H. All length G+1 factors are unique by the corresponding strict border bound. A minimal absent word of length>=3 has a repeated interior, hence maximal length G+2, and context pairs of W and F yield exactly 0W0, 0F0, 1F1. Independently enumerated literal factors/minimal absent words for k=2..5 and inspected checker.py k=2..7. Infinite result follows from the border proof, not finite enumeration.

## originality

PASS

Minimal absent word definitions and linear-time algorithms are established; factor and permutation complexities for Cantor-like fixed points are also studied. The exact maximal-length three-factor stratum of each finite linear Cantor iterate is not supplied by those inspected statements; residual risk remains because the 2016 primary Cantor paper was not accessible in full.

## value

PASS

The finite 1->101,0->000 Cantor substitution is a canonical self-similar word; its longest minimal forbidden extensions and repeated-factor threshold are natural structural invariants useful for substitution factor dictionaries and boundary behavior. This provides a complete extremal classification over all levels k>=2, not an arbitrary length slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
