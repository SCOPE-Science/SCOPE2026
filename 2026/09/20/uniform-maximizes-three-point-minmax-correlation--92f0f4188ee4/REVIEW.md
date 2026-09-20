# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The reduction to support \(\{-1,0,1\}\) is valid by affine invariance of correlation. Direct enumeration of the nine iid outcomes verifies the covariance and variance identities used to obtain the two-parameter rational formula for squared min–max correlation. Exact symbolic differentiation gives the stated resultant. In the strict nonsymmetric interior, that resultant leaves only \(q=1/2\), where the only common derivative root is \(t=1/4=q^2\), hence not interior. The symmetric line has its unique maximum at \(q=2/3\), and both simplex-edge families have squared correlation at most \(1/9\). These checks establish the global squared-correlation maximum \(64/361\), hence correlation \(8/19\), uniquely at uniform weights.

The included exact-arithmetic artifact independently reconstructs the moment formula, derivative elimination, boundary extrema, and benchmark values. The attainable-range statement follows from continuity and strict increase along the symmetric family up to \(q=2/3\).

## Originality — PASS, to the best of our knowledge

The closest prior work is explicitly acknowledged. López-Blázquez and Salamanca-Miño (2021) develops computational methods for discrete-parent order-statistic correlations and displays the \(N=3,n=2\) calculation. Papadatos (2022/2023) formulates the probability-vector extension on fixed support and states that uniform weights are expected to maximize the correlation, but that no proof is available; it also supplies nonuniform \(N=3\) examples, including \(p=(1/4,1/2,1/4)\), for which the present formula reproduces \(9/23\).

Searches for the exact three-point optimization, the constant \(8/19\), synonymous min–max/order-statistic formulations, and later work citing the 2021/2023 papers did not identify a proof that subsumes the theorem. The new claim is deliberately narrow: exact global optimization over the three-point probability simplex, with equality, boundary, and range characterization. It does not claim novelty for the fixed-\(p\) correlation formula or for the general Terrell/Székely–Móri theory.

Residual risk remains that an older discrete-order-statistics or maximal-correlation source contains the same three-point simplex optimization under different notation, or that a later result is absent from the searched indexes. This is a residual terminology/indexing risk rather than concrete evidence of coverage.

## Value — PASS

The result resolves the first nontrivial probability-weight instance of an explicitly stated open direction and yields a simple exact constant and unique extremizer. It also separates two sources of extremality: equal spacing of support points and uniformity of probability weights. The proof is reusable as a low-dimensional template for larger-support versions, because it isolates a symmetry coordinate and an exact elimination condition for nonsymmetric critical points.

## Scientific limitations

The theorem only treats \(N=3\), sample size two, the minimum–maximum pair, and equally spaced fixed support. It does not establish the conjecture for larger supports, other order-statistic pairs, arbitrary support geometry, nonlinear maximal correlation, or sampling without replacement. The exact algebraic elimination is reproducible in SymPy but has not been formalized in a proof assistant.
