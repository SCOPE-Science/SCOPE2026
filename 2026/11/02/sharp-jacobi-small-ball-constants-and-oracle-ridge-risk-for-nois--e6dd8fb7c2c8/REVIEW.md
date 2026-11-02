# Self-review

## Correctness (C): PASS
The theorem defines the uncorrected centered sum of squares and all beta parameters, and gives explicit coefficients for strict endpoint, boundary logarithmic, and integrable-density phases. Orthogonal mean/residual coordinates have Jacobian \(\sqrt m\), producing the codimension-\(m-1\) tube factor. At a singular endpoint the scaling \(x_i=\sqrt{s}z_i\) has exponent \(m\alpha/2\) and a convergent endpoint integral exactly below \((m-1)/m\). At equality the intermediate mean coordinate produces half of the logarithmic interval per critical endpoint. The conditional ridge bias--variance formula is exact for independent centered noise of common finite variance; its derivative changes sign once at \(\lambda=\sigma^2/b^2\). The small-noise constants follow from the lower-tail Laplace/Stieltjes integral and beta integral. The reproducibility script passed 81 deterministic exact algebra/scaling tests; numerical sampling is corroborative and not an infinite proof.

## Originality (O): PASS, qualified
The new claim is the *coefficient-level* small-ball phase classification for singular Jacobi endpoints for any fixed \(m\ge4\), including precise critical logarithmic constants, and their sharp noise-risk implications. The previously known beta-design inverse-moment threshold and the continuous-density interior tube coefficient are not advanced as new, and the published three-sample beta-variance classification does not cover \(m\ge4\). Xu--Zhang studies global polynomial least-squares sampling stability, Migliorati--Nobile--Tempone provides noisy least-squares bounds, and Mourtada derives general lower-tail controls but none of the inspected statements establishes the singular-endpoint coefficients. The elementary ridge-oracle derivative identity is not claimed as historically new. A specialist priority investigation for endpoint concentration analogues remains appropriate.

## Value (V): PASS
The constants resolve how endpoint singularities control the *absolute scale* of rare ill-conditioned affine designs and, via a regularized reciprocal integral, precisely how observation noise transfers into slope risk. The distinction between four arcsine and four uniform sites is mathematically natural; its risk transition is quantified by an exact integral coefficient. These sharper constants add a motivated boundary classification beyond the earlier yes/no moment threshold. No claims are made about nonlinear regression, higher-degree design or data-driven tuning.

## Closest literature and scientific limits
1. Xu--Zhang, *Stability of Least Squares Approximation under Random Sampling*, arXiv:2407.10221 (v1: 2024-07-14), specifically high-probability Jacobi polynomial sampling stability rather than sharp fixed-count affine lower tails.
2. Migliorati--Nobile--Tempone, *Convergence estimates in probability and in expectation for discrete least squares with noisy evaluations at random points*, DOI 10.1016/j.jmva.2015.08.009, including beta sampling and noisy error bounds.
3. Mourtada, *Exact minimax risk for linear least squares, and the lower tail of sample covariance matrices*, arXiv:1912.10754, deriving general regularity-based lower-tail results rather than this coefficient.
4. Prior affine beta inverse-moment and continuous-density tube results cover the threshold and the integrable-density branch, respectively; a three-sample beta-variance result covers smaller sample size. They do not provide the singular \(m\ge4\) constants as stated.

Independent specialist assessment of publication priority and of the endpoint asymptotic uniformity has not been performed.

Self-review: passed. Independent audit: not yet performed.
