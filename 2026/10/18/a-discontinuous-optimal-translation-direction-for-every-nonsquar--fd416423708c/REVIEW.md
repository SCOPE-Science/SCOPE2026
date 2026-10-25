# Independent mathematical audit

## correctness

PASS

PASS: The exact product covariogram on positive-overlap shifts is (a-t cos θ)(b-t sin θ). Coordinate swapping excludes θ>π/4. Subtracting axial overlap b(a-t) factors as t sinθ cosθ[t−f(θ)], f=(a−b tan(θ/2))/cosθ; f has unique minimum from strictly increasing q(z)=z^4−4z²+4(a/b)z−1 on [0,√2−1]. Stationary-angle equation T(θ)=(a cosθ−b sinθ)/cos2θ has a unique upper-branch local maximum because H(w)=aw³−3bw²+3aw−b is strictly increasing (H′=3a[(w−b/a)²+1−(b/a)²]>0). This upper branch starts at the axial tie t0, increases to θD=atan(b/a) as t→D=√(a²+b²), and strictly beats the zero-overlap competitors. At t0, the derivative jump is t0 sinθ0 cosθ0>0. At t=0 and t≥D the endpoint degeneracies are correctly excluded from uniqueness. The explicit t0, θ0 quartic and inequalities follow; original source verify.py read. Independently tested aspect ratios 1.0001..10, stationarity and ties and grids. Finite checks do NOT prove the all-parameter theorem.

## originality

PASS

PASS (best-of-knowledge): The published equal-side hypercube phase theorem classifies finitely many equal-coordinate support sizes; its parameter a=b is specifically excluded here. The nonsquare rectangle has an oblique continuously moving optimizer with a single discontinuous onset governed by an aspect-ratio-dependent quartic, not implied by equal-side symmetry. Prior full-covariogram uniqueness/rigidity theorems concern reconstruction or body-gauge radiality, not the maximizer of g at a fixed Euclidean radius. No equivalent anisotropic all-radius theorem located after queries and substantive primary inspection; general elementary constrained-product precedents remain a bibliographic risk.

## value

PASS

PASS: This resolves a natural geometric extremization of the covariogram for all strict rectangle aspect ratios, including a genuinely discontinuous optimizer, exact switch threshold and envelope derivative jump. The explicit jump, not a routine parameter substitution of the square theorem, gives a motivated exact boundary result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
