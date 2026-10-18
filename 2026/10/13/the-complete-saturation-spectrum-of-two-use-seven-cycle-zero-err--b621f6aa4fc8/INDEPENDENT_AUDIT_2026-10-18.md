# Independent mathematical audit

## correctness

PASS

On 49 labeled ordered pairs, zero-error sets are exactly cliques of the compatibility graph whose edges have at least one coordinate separation 2,3,4,5 mod 7. Inclusion-maximal zero-error sets are maximal cliques. Inspected the complete RESULT.md and actual verify_a.py/verify_b.cpp Git tree and independently implemented a pivoted Bron–Kerbosch maximal-clique recursion on the 49-vertex graph. It enumerated exactly 83,181 distinct terminal sets with counts 28 at size 7, 9,016 at size 8, 73,157 at size 9, and 980 at size 10; all passed direct adjacency and maximality tests. The sorted 13-hex-digit-per-line list has SHA-256 362d213751756f339a3319847ce2bc6b580fd2ddc34d124b265e0a1dd417de13, equal to the package’s uncompressed catalogue digest. Independent generator orbit traversal under shifts, reflections, and swap yields 229 orbits and the stated nine (cardinality,orbit-size,multiplicity) classes. This is complete finite enumeration, not extrapolation to more channel uses.

## originality

PASS

The full spectrum of inclusion-maximal codes, particularly 82,201 nonmaximum terminal codes in 226 symmetry orbits, is not the known independent domination minimum 7, independent-set counts, or known maximum size 10 with 980 maximum-size codes. The primary Yang–Zhang strong-product independence-domination result provides the minimum 7 but not the histogram. Hildebrant 2026 gives ordinary independence polynomials of the same graph, including coefficient 980, but those count all independent sets and do not furnish the maximal-set census. A semantic Resultary query returned no exact prior spectrum, but that absence is not a proof of originality.

## value

PASS

Inclusion-maximal codebooks are precisely terminal feasible communication designs: unlike maximum cardinality, terminal size measures how a zero-error code can saturate prematurely. The complete finite spectrum and natural channel-isometry orbit census are meaningful exact invariants of the canonical C7 two-use instance, not arbitrary sample values. The overwhelming nonmaximum count demonstrates a structural distinction from capacity-optimal codes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
