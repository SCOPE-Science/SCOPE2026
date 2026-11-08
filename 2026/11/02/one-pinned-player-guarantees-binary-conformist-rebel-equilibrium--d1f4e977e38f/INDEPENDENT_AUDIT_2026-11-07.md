# Independent mathematical audit

## correctness

PASS

Derive exact local binary best-response condition on adjacent disagreement bits y: either they differ or both equal type bit. For each contiguous nonpinned path with fixed endpoint actions, parity(last XOR, last bit) reachability starts from states (0,0),(1,1), reaches 3 of 4 after one internal vertex, and >=3 after each further vertex; hence both endpoint parities possible, joining all pinned blocks gives a PNE. In alternating one-pin case, z_i=y_i XOR t_i forms a weakly decreasing binary word 1^ell 0^(n-ell); XOR closure forces ell congruent n/2 mod2, giving stated exact count. Direct independent bitwise payoff enumeration checked every pinned type vector for n=3,4,5,6 and all alternate single pin choices through n=10. It is finite corroboration only.

## originality

PASS

Cao–Yang 2014 treats unpinned binary alternating cycles and their nonexistence; later 2026 conformist/rebel/stubborn papers introduce relevant game types and discuss ring conditions in a multiple-strategy regime. Their accessible abstracts and secondary description do not establish unconditional existence for every binary pinned ring or this exact one-pin equilibrium count. Full 2026 primary texts were not retrievable, so best-of-knowledge only.

## value

PASS

Pinning one vertex is a meaningful intervention for resolving the classical alternating 4k+2 no-PNE obstruction; the theorem proves unconditional binary restoration and gives a nontrivial length-dependent count, rather than an arbitrary example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
