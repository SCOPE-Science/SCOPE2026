# Independent mathematical audit

## correctness

PASS

In Yudin Appendix A let R=ceil(exp(m-gamma)), R0=R+pi(R), K=1+(m-1)R0 for any prime-power m>=2. The row count M0=sum_{ell<=R}(floor(K/ell)+1) exceeds K H_R; the standard sharp harmonic estimate H_R>log R+gamma>=m gives M0>mK. For the prime-power group C_m^(R+K+pi(R)), Olson’s Davenport constant is 1+(m-1)(R+K+pi(R))=1+(m-1)(R0+K)=mK. Therefore at least D elements in the original distinct affine-factorial row family are present and a nonempty zero-sum subfamily of <=D yields an mth-power product, with N divisible by m. The bound is N<=m[1+(m-1)(R+pi(R))], improving Yudin’s 2m(m-1)ceil(e^m) for prime-power m and yielding leading coefficient e^-gamma. In the explicit harmonic-majorant relaxation R~e^(m-1+s-gamma) and K~(m-1)R/s, coefficient e^(s-1-gamma)/s minimizes at s=1, not a claim of global optimality. Independent integer computations for prime powers m=2,3,4,5,7,8,9,11,13 checked all row and Davenport inequalities, but the unbounded proof follows from the inequalities and group theorem, not the finite tests.

## originality

PASS

Yudin arxiv:2610.01899v1 Appendix A supplies exactly the affine factorial family, zero-sum exponent-vector encoding, Olson prime-power Davenport constant and looser H_R>log R estimate, producing N<=2m(m-1)ceil(e^m). The accepted new claim is the optimized parameter choice retaining Euler’s constant and its within-relaxation minimax constant, not an invented different combinatorial construction. Bérczes et al (Acta Arith. 190, 2019), full paper Theorem4.2 proves existence of bounded-logarithmic number of factors for infinitely many STARTING n in the cube case; it does not state uniform-in-parameter affine function family for every prime-power exponent. Published relevant SCOPE search hits concern distinct factorial/square results, not this appendix optimization. Because derivation from known proof is relatively short, credit is limited to a quantitatively substantial coefficient improvement; residual priority risk acknowledged.

## value

PASS

The prime-power exponential construction count is a natural quantitative invariant in a previously published new existence theorem; shrinking the leading constant from 2 to e^-gamma (~0.561) saves ~72% of the guaranteed factors while preserving same universal affine-family property. The within-method optimum makes the bound purposeful and sharp for the stated relaxation, while explicitly NOT proving globally minimum N or improving general composite exponents.

The dated certificate retains the supplied scientific assessment, sources and limitations.
