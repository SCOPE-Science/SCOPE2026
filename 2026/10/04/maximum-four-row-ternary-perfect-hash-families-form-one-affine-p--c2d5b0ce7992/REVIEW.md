# Review

## Correctness
PASS. The proof normalizes an arbitrary pair by the full row/symbol symmetry, exhaustively resolves all four possible Hamming-distance cases for a hypothetical nine-column family, and then uses injectivity of every two-coordinate projection for the sharp upper bound. The explicit affine-plane family attains nine. Equality cases reduce to ordered orthogonal Latin-square pairs of order three, and the bundled verifier independently checks the finite counts and full orbit.

## Originality
PASS. The closest inspected same-parameter literature constructs a \(\operatorname{PHF}(4;9,3,3)\) but does not prove that ten columns are impossible or classify all nine-column extremizers. Semantic searches under perfect-hash, orthogonal-array, affine-plane, and exact-parameter formulations found no implication-equivalent statement. A residual risk remains that an older design-theory source contains the classification under different terminology.

## Value
PASS. The result closes the natural four-row ternary extremal case immediately adjacent to the classical affine-plane construction and identifies all extremizers, rather than merely recomputing one construction. The forced distance-three/OA structure and unique orbit explain why the size-nine construction is extremal.

## Closest literature and limitations
Walker and Colbourn (2007) list the size-nine four-row ternary construction among best-found perfect hash families. Bshouty (arXiv:1406.2108v1) is an archive-era algorithms-and-complexity source for perfect hash families. The result here is parameter-specific and does not claim a general perfect-hash bound.

Same-model review: passed. Independent audit: not yet performed.
