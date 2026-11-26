# Independent mathematical audit

## correctness

PASS

The frozen full probability formula is false at s=1, not merely unverified. In RESULT.md line 58, a single tangency point on a side is wrongly taken to imply a null event for segments on that side. If both independently uniform endpoints are on a side, they straddle its midpoint with probability 1/2; the segment then contains that tangency point. With σ=Σp_i² the frozen formula misses σ/2 at full scale (1/6 even in the equilateral case), and its advertised full-scale range fails. The frozen checker explicitly masks out all same-side pairs, so it cannot detect the defect. Complete corrected files are in /workspace/repairs/3. The repaired probability is (1−σ)Q(s)+(σ/2)1_{s=1}; the conditional Q remains continuous and has the originally calculated cusp. I checked the affine conic support and equivalence of the line and segment tests for different sides, and verified the incidence polynomial and its integration: u=tv, v=z gives Jacobian z, and the signed roots where z_− or z_+ crosses 1 exhaust the three regimes. Differentiating F gives (1+t)√(t²−t+1)/t². At s=1 the distinct-side polynomial factors and excludes an area ∫₀^(1/2)(1−2u)/(2−3u)du, giving Q*=2/3+2 log(2)/9. As s tends to 0 the symmetric interval has nonradical integral O(s³) and radical leading term −4sF(1/2)/9. As δ=1−s tends to 0, a~2δ/3; the would-be singular term is −δ²/(9a)=O(δ), and the surviving log a coefficient is δ/3+O(δ²), giving the cusp relative to the left limit. Zero-area polynomial level sets give continuity of Q; on the diagonal u=v=w the required scale is |3w−2|, so every interval of levels counts an open set and Q strictly increases. The new coefficient of σ at 1 is 1/2−Q*<0, preserving strict Schur concavity and giving the sharp corrected range (7/12+log(2)/9, 11/18+4log(2)/27]. The rewritten checker (python3 /workspace/repairs/3/checker.py) passed symbolic identities, 10 direct quadratures with first endpoint fixed, 20 physical-segment trials including same-side pairs, and 4 explicit midpoint-contact tests. The proof, not these samples, establishes the repaired continuum and shape claims.

## originality

PASS

For the repaired finding the credited classical midpoint tangencies and their elementary same-side mass alone are not novelty. The distinct claim is the exact conditional law for centroidally scaled Steiner ellipses under independent perimeter-endpoint sampling, its logarithmic cusp, and the resulting sharp full shape law with the boundary atom correctly accounted for. Neither verified kinematic-line comparators nor the later triangular-core results supply those ellipse-specific conclusions.

## value

PASS

For canonical affine targets and Euclidean endpoint sampling, the repaired result separates shape weights, a universal continuous incidence distribution, and a positive discrete mass that is invisible if one substitutes random lines or discards same-side chords. The exact cusp and distinct sharp full-scale bounds make it a useful benchmark throughout the triangle family, not just a single probability or a routine observation about midpoint tangency. It does not claim optimization over other ellipses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
