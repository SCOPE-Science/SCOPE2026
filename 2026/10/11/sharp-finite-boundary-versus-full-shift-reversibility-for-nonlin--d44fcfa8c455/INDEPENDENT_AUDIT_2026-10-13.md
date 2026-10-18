# Independent mathematical audit

## correctness

PASS

PASS. For every d≥2, under gcd(c5,d)=1, rad(d)|c0..c3, and rad(d)|c4c6, all finite zero-boundary maps lift their prime-wise triangular invertible reductions, hence are bijective for every size. For the bi-infinite map, if rad(d)|c4 and rad(d)|c6 separately, mod p inversion is coordinatewise; at p^k→p^(k+1), all derivative terms except the central c5 term vanish mod p, so each new output digit fixes one input digit using output neighborhood enlarged by at most one. CRT yields inverse radius ≤E−1 where E=max v_p(d). Conversely if c4 or c6 nonzero at p, the product condition forces exactly one; choose nonzero root λ of c4+c5λ+c6λ² over F_p. δ_i=(d/p)λ^i is nonzero periodic of order L|p−1 and F(δ)=F(0), since higher mixed coefficients are p-divisible; works also p=2. Example I+rad(d)S^−1 has inverse sum_{j=0}^{E−1}(−rad(d))^j S^−j with nonzero final coefficient mod a prime power of maximal exponent, proving sharp least centered radius E−1. Independently checked this inverse on periodic words at d=2,3,4,6,8,9,12,16,18,24 and explicit collisions at d=2,3,4,8,9,15. Inspected actual verify.py; finite tests corroborate, do not prove universal theorem. Primary Baby–Bhattacharjee theorem 3.1 finite-null-boundary hypotheses verified directly in full open HTML.

## originality

PASS

Best-of-knowledge PASS for nonlinear eight-parameter family boundary transition, explicit prime-periodic collision and optimal full-shift inverse radius. Source Baby–Bhattacharjee exact theorem is only finite null-boundary. General periodic and additive CA papers cover methods or linear subfamilies, not the combined nonlinear iff/radius claim in inspected statements; older additive source full texts are access risks.

## value

PASS

PASS. Precisely separates all-finite-length null-boundary invertibility from bi-infinite reversibility in a natural nonlinear polynomial family, supplies bounded-period concrete obstructions, and gives a sharp reconstruction locality E−1 depending on modulus arithmetic. These structural boundary phenomena and inverse-radius cutoffs are meaningful beyond routine finite checks. Linear specializations are explicitly credited as prior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
