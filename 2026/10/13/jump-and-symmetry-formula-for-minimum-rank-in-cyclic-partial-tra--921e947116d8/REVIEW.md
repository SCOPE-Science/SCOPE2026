# Independent mathematical audit

## correctness

PASS

Both letters commute with H translations, so every word image is a union of entire H orbits and its size is s times the quotient rank. Any period of the quotient pattern would lift to a period in H, so it has no nonzero period. The quotient residue partition modulo d=gcd(m,h) is preserved by b and permuted by a, bounding the quotient rank below by d. Independently of the interval proof, if two quotient states in the same class have gap jh, 1<=j<m/d, choose a translate of the active set containing the first but not the second. Such a translate must exist: otherwise equal cardinalities make the quotient pattern invariant by jh. The corresponding conjugate of b reduces the gap to (j-1)h. Iterating merges the pair. Successively merging two current image points in any nonsingleton residue class reduces its cardinality without ever undoing an earlier merger or crossing classes. This gives exactly d image points. If d=m the lower bound already gives equality; in particular m=1 (empty/full active sets) yields original rank n. Thus rank one is exactly s=1 and gcd(n,h)=1. The bundled finite exhaustive checks and word-witness code were inspected, not executed; the independent symbolic argument establishes arbitrary size, not shortest word length.

## originality

PASS

The indexed unit-jump classification overlaps exactly and is credited; the passing contribution is the additional gcd obstruction and its simultaneous attainability for noncoprime jumps and arbitrary active sets. No inspected minimum-word or primitive-automaton theorem gives that classification. The overlapping record's displayed date does not decide priority.

## value

PASS

The minimum image size is intrinsic to this natural two-letter automaton family. The theorem resolves exact ranks even when rank-one synchronization is impossible, and separates the cost of rotational symmetry from jump connectivity on its quotient. E.g. with n=24, a single active residue modulo 8 repeated three times, and h=4, the two factors give 3*4=12; neither the unit-jump symmetry count nor the jump residue count alone gives that value. This is a uniform structural classification, not a subset-graph computation or a shortest-word claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
