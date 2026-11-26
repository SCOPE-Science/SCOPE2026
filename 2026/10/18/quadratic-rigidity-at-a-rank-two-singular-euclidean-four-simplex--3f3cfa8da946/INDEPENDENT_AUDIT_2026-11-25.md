# Independent mathematical audit

## correctness

PASS

I rebuilt the squared area map using the 2-by-2 triangle Gram determinants in the frozen lexicographic orders, and recomputed the base areas, exact rank eight and minor -1/4194304, both nullspaces, and the two projected kernel quadratics t(2s+t)/8 and s(s+2t)/8. Their squared sum is (s²+t²)²/192+(s²+3st+t²)²/96. Replay: python3 /workspace/branches/check_simplex.py; this independently checks the polynomial certificates, not the uniform estimate. For that estimate, a hypothetical sequence with data defect o(||h||²) has complement component w=O(||h||²), by injectivity of the differential on the complement and the exact homogeneous quadratic remainder. The two left-null projections then agree with the coercive kernel quadratics up to O(||h||³), a contradiction. Positive definiteness at I/2 gives an open realizable edge domain. On the nonzero kernel direction U the defect is exactly s²H(U), with a nonzero left projection, proving sharpness. This is stability relative to the given fiber, not injectivity or a two-point inverse estimate on a neighborhood.

## originality

PASS

There is substantial prior work on the same area/length map, including global ambiguity and generic recovery, but no inspected result covers the rank-eight singularity of this labeled right simplex together with its isolated local fiber and sharp pointwise stability. The novelty is the specific second-order obstruction, not the use of Heron's formula or generic finite recovery.

## value

PASS

At a natural nondegenerate but singular four-simplex the two-dimensional infinitesimal kernel does not integrate to a fixed-area deformation. The exact obstruction furnishes a useful second-order test case for continuous area rigidity and shows what quantitative stability survives the failed inverse function theorem. The explicit sharp exponent is informative even without a global uniqueness result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
