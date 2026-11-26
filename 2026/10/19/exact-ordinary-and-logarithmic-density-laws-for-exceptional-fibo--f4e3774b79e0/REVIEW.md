# Independent mathematical audit

## correctness

PASS

The lengths being counted are word lengths, for each fixed q>0 and each strict intermediate threshold. Mechanical coding gives the rotation gaps (reflection of the boundary points is immaterial). For the finite table I reconstructed the insertion invariant: in direction (-1)^(j-1) at F_j points the long gaps start at the first F_(j-1) orbit points. Inserting F_j+i shifts the ith point by alpha^j in that direction, cutting off a short front piece; on reversing direction, every old endpoint now starts a gap of length alpha^(j-1), and each new endpoint starts a gap of length alpha^j. The base at F_3=2 is immediate. Binet gives uniform block convergence including the Shannon normalization. The derivative has a positive denominator and an affine numerator with strictly negative slope when q is not 1; d_1 is strictly concave. Endpoint equality gives two transverse crossings. The symmetric-difference error in each block is o(F_j) and the geometrically summed error is still o(F_j). In a partial block the count adds the clipped window length to phi L F_j from previous blocks. The resulting phase profile joins across the endpoints 1 and phi, decreases/increases/decreases, and has extrema phi L/(1+t_-) and phi^2 L/(1+t_+); compactness and continuity give exactly the full interval of limits. A complete block contributes log((1+t_+)/(1+t_-))+o(1) to the harmonic sum, an incomplete block contributes O(1), and the block count is log N/log phi+O(1). Independently replayed 56 exact rotation gap profiles in Z[alpha] through j=15 with /workspace/review_work/fibonacci.py and checked the displayed Shannon illustration. These diagnostics are not the proof of the limits. No equality-threshold claim was tested or inferred.

## originality

PASS

The contribution is the joint natural/logarithmic cutoff-density theorem for Rényi deficit threshold crossings, not rotation-gap frequencies, a statement about entropy values alone, or a finite-type-cover entropy. No equivalent earlier cutoff-density law was found in the inspected sources. The closest Shannon phase profile is later-dated and does not itself state cutoff densities.

## value

PASS

Golden rotation is the canonical bounded-type Sturmian example. The theorem resolves whether ordinary and logarithmic sampling over lengths give the same stable exceptional frequency, quantifies the full ordinary oscillation, and does so for a continuum of orders and thresholds. That distinction would be lost in an order-of-magnitude bound or an entropy-phase cluster set alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
