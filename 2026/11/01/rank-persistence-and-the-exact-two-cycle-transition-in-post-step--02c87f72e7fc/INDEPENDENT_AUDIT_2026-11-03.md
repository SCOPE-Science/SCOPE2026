# Independent mathematical audit

## correctness

PASS

Diagonalize W0 in signed fixed singular bases. For q=1−ηa≠0 and τ=ηλ>0, coefficients evolve x⁺=q x−τ sgn(qx) unless x=0; radii evolve by strict contraction h(r)=|s r−τ| with s=|q|∈(0,1), fixed c=τ/(1+s). Preimages of zero are exactly R_j=τ(s^(−j)−1)/(1−s), since once the backward target exceeds τ only the high-radius inverse branch remains. Zero is absorbing. All other radii approach c; eventually q>0 flips coefficient signs and hence a matrix two-cycle, while q<0 preserves signs and converges to a partial-isometry scalar multiple. At q=0 all radii zero after one step. Effective rank, Frobenius/nuclear norms and positive objective gap follow. Proximal clipped map is max(sr−τ,0), so terminates. Independent hand-derived scalar recursion, q=±1/2 example and checked exact-rational verification script support boundary signs; no numerical tolerance interpreted as true rank.

## originality

PASS

Best-knowledge PASS narrowly for exact complete repeated-iterate matrix rank/loss and resonance classification, not for the known scalar subgradient chattering or the originally published update. Compared primary 2026 spectral-weight-decay post-step operation, genuine proximal polar singular-value thresholding, and related different fixed-step/cycling algorithms.

## value

PASS

The recent un-clipped post-gradient spectral method advertises low-rank structure, yet the theorem proves generic nonzero full-rank spectral equalization, explicit exceptional rank-drop hypersurfaces, a step-size-zeroing resonance, and distinct matrix fixed/two-cycle regimes. This algorithm-specific exact classification materially informs whether the update behaves like genuine singular-value thresholding; the scalar contraction itself is classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
