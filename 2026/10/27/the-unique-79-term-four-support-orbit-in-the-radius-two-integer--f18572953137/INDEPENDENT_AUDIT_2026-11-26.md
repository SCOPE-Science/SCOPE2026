# Independent mathematical audit

## correctness

PASS

This is a classification for exactly four distinct vectors, with no order on the terms. In rank three the signed deleted-column determinants span the one-dimensional rational kernel. Strict positivity requires four nonzero cofactors of one sign, and dividing by their gcd generates the integer kernel. The positive primitive generator is minimal and any other positive relation contains it. In rank at most two, injective choice of coordinate projections preserves every zero-sum submultiset and reduces to the published planar bound 45. A separate rank-two check is that the nonnegative kernel is a pointed cone of dimension at most two; each extreme ray has support at most three (otherwise one can perturb within the supported kernel) and its primitive generator has length at most 24 by the 2-by-2 minor bound 8. A minimal relation is either a primitive ray or uses both rays with coefficients below one, so its length is below 48. In rank one the primitive rays have at most two coordinates and length at most 4; conic Carathéodory uses at most three rays. These also exclude lengths at least 79. A fresh exact enumeration traversed all 9,691,375 four-sets, found 779,864 positive circuits, maximum length 79, and 48 maximizing multisets. The computed set equals the signed-permutation orbit of the stated weighted representative and has all 48 group images distinct, proving freeness as well as transitivity. Fresh replay: python3 /workspace/branches/f395f5d8-758b-443d-a972-b7d27112b049/verify_four_support.py (no sample argument). The frozen census and saved output were inspected, not treated as an independent run. The frozen planar citation should point to Eq. (1), not Eq. (3); the bound used is correct.

## originality

PASS

Credit goes to the exact inverse classification within the four-support layer, not to discovery of the value 79 or of the extremal construction. The closest published result reports the length equality computationally and discusses essential uniqueness conjecturally; its length result does not determine the maximizer set. The inspected related catalog entry is for a different configuration and does not specialize to the cube.

## value

PASS

The paper motivating the support-size invariant explicitly raises essential uniqueness. Radius two is its first even case and the classification answers the inverse question over every minimal multiset in that fixed layer, providing a concrete rigidity benchmark rather than merely rechecking a reported length. It does not purport to solve the broader unrestricted conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
