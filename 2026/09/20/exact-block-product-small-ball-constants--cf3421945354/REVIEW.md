# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness — PASS

The block factors are centered averages of independent \(\operatorname{Unif}[-1,1]\) variables. Their densities are even and log-concave, hence decreasing on the positive half-line. The product-density formula preserves this symmetric monotonicity, so the concentration function is maximized exactly at zero.

For the asymptotics, the logarithmic transform \(T_m=-\log|A_m|\) converts products into sums. Its density has the form \(e^{-u}r_m(u)\), with \(r_m(u)\to c_m\) and \(r_m-c_m\in L^1\). Expanding the additive convolution gives the leading polynomial and the next coefficient in \(u\); integrating against \(e^{-u}\) gives the stated two-term small-ball expansion. The same convolution expansion gives the density singularity. The exact \(L^p\) constant then follows from the gamma integral and Stirling's formula. The central-density finite sum follows by rescaling the Irwin--Hall density, and the large-block correction follows from the characteristic-function expansion at the Gaussian saddle.

The special cases \(m_k=1\) reduce to the exact product-of-uniforms law, and the \((2,2)\) case has an elementary closed form agreeing with both displayed asymptotic coefficients.

## Originality — PASS, to the best of our knowledge

The direct 2026 source proves the product-profile lower and upper bounds for the centered block-product models only up to constants depending on \(d\), and proves the \(p^{d-1}\) density growth up to such constants. It does not state the exact all-center maximizer, the explicit block-dependent leading coefficient, the second logarithmic term, or the exact high-\(p\) coefficient derived here.

The Irwin--Hall/Bates density formula and Mellin methods for products of independent random variables are classical prior art. No novelty is claimed for those ingredients by themselves. Searches for the recent source together with exact block-product small-ball constants, centered concentration, Bates products, and Mellin-product formulations did not locate an equivalent specialization.

The main residual originality risk is older product-distribution literature: general Mellin-transform formulas or tables may imply the leading singular coefficient after a short specialization, even if not stated in this block-product anti-concentration language. The 1970 Springer--Thompson paper was inspected at the abstract/bibliographic level rather than exhaustively line by line. The direct source is also recent enough that an unindexed contemporaneous refinement may exist. These risks do not affect correctness but limit the originality claim to “to the best of our knowledge.”

## Value — PASS

The result replaces unspecified degree-dependent constants by explicit constants on the canonical extremizers used to establish sharpness in the source theorem. It also identifies the exact concentration center for every radius, gives a second logarithmic coefficient sensitive to the complete block-size vector, and upgrades order-sharp density growth to an exact high-\(p\) asymptotic. The large-block expansion links the constants to the Gaussian central-density limit and quantifies the first finite-block correction.

## Limitations

- Exact constants are proved for the centered block-product models, not for arbitrary multi-affine polynomials.
- The second-order expansion is for fixed block sizes as the small-ball radius tends to zero.
- No uniform second-order remainder is claimed when the block sizes grow simultaneously.
- The optimal general constant for arbitrary admissible partitions is not determined.
- The singleton-partition exponent gap highlighted in the source paper remains open.
- Classical Irwin--Hall and general Mellin-product machinery are prior art.
- Older product-distribution literature was not exhaustively inspected.
- Cross-model review has not been performed.
