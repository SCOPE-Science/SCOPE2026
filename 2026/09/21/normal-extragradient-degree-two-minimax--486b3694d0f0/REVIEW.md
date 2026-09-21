# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** After scaling by \(L\), normality reduces the Euclidean operator-norm question to a scalar polynomial supremum on the compact half-disk
\(K_\delta=\{|z|\le1,\ \operatorname{Re}z\ge\delta\}\). For
\(p_*(z)=1-(1+\delta)z+z^2\), the circular arc reduces to the real factor
\(2\operatorname{Re}z-(1+\delta)\), while the chord gives
\(|p_*|^2=q^2+s[s-q(2-q)]\) with \(q=1-\delta\) and
\(0\le s\le q(2-q)\). This proves the global upper bound by the maximum-modulus principle.

The lower bound uses only the real point \(z_0=\delta\) and the circular corner
\(z_1=\delta+i\sqrt{1-\delta^2}\). The squared moduli are convex quadratics in the two real coefficients. At the proposed coefficients their gradients satisfy
\(\nabla h_0+\delta\nabla h_1=0\), so zero belongs to the subdifferential of their pointwise maximum. This is a global convex optimality certificate. The same two points occur in one explicit three-dimensional real-normal matrix, so sharpness is attained within the stated matrix class.

The unequal extragradient parameters reproduce the optimal polynomial exactly. The common-step benchmark was independently derived from its two real endpoint values and checked on both boundary pieces. Limiting cases \(\delta\downarrow0\) and \(\delta=1\), the real-normal hard matrix, dense boundary samples, deterministic random lower-certificate tests, and numerical minimization all agree with the formulas.

## Originality

**PASS, to the best of our knowledge, with a material historical-equivalence caveat.** The minimax-polynomial framework itself is classical. Manteuffel (1977, 1982) and the Eiermann--Niethammer--Varga semi-iterative literature are direct predecessors for complex-spectrum polynomial iterations. The accessible 1982 abstract states that optimal parameters for linear second-degree stationary recurrences can be found through the Chebyshev minimax problem; it does not state the present circular-segment degree-two closed form. The 1985 semi-iterative abstract likewise emphasizes that explicit optimal polynomials are known only for special sets.

The closest modern source checked at theorem level is Azizian et al. (AISTATS 2020), which uses exactly the spectral set
\(K_{\mu,L}=\{\operatorname{Re}\lambda\ge\mu,|\lambda|\le L\}\), formulates finite-time first-order behavior through real polynomials, and notes that the complex minimax object can be difficult to obtain. For this half-disk it gives an asymptotic lower bound from an inscribed disk and observes that extragradient attains the correct order. The checked text does not give the exact degree-two minimax polynomial, the factor \(1-\mu/L\), the unequal predictor/corrector pair, or the exact optimized common-step factor stated here.

Huang--Zhang's extra-point framework and Xu--Wang's sharp stepsize work were also checked as adjacent extragradient literature. Searches additionally covered the synonymous complex Chebyshev, semi-iterative, polynomial Richardson, circular-segment, and nonsymmetric linear-system formulations. No checked source stated the same finite-degree formula or extragradient realization.

The largest residual originality risk is older complex approximation and matrix-iteration literature. Full theorem-level text was not available for Manteuffel (1982), DOI 10.1137/0719058, or for every result in the older semi-iterative reference chain. Those sources could contain an equivalent special case under different parameters. This record therefore claims originality only for the explicit closed form and its optimization interpretation to the best of current checked knowledge, not for the general minimax framework.

## Value

**PASS.** The result turns a complex two-parameter robust-design problem into a closed form and identifies a concrete algorithmic consequence: allowing predictor and corrector steps to differ exactly realizes the unrestricted real quadratic minimax, whereas enforcing the classical common step incurs a strictly larger sharp factor. The theorem comes with a fixed three-dimensional sharp normal witness and separates finite-cycle exact behavior from asymptotic complexity results in the broader variational-inequality literature.

## Scientific limitations

The contraction guarantee is limited to affine real normal operators, exact arithmetic, known \(\mu,L\), and Euclidean norm. Nonnormal transient growth is outside the theorem. The degree-two minimax is not a lower bound against adaptive, nonstationary, higher-degree, projected, nonlinear, or momentum algorithms over many evaluations. The public literature search cannot exclude historical equivalence in older complex Chebyshev and semi-iterative work, especially the sources identified above.
