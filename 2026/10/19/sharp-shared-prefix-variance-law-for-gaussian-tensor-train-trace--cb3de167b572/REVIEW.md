# Independent mathematical audit

## correctness

PASS

The partially contracted normalized tensor has squared Frobenius norm S_h. Conditioned on its predecessor and writing lambda_i for the reshaped contraction's squared singular values, S_h has the law sum_i lambda_i chi²_(r,i)/r with sum_i lambda_i=S_(h-1). Its conditional second moment is S_(h-1)^2+(2/r)sum_i lambda_i^2, at most (1+2/r)S_(h-1)^2. Centered Jensen over the PSD spectral decomposition transfers both single-probe and conditional-mean variance bounds to every trace-one target. The last core gives conditional fourth moment 3S_(d-1)^2, and conditioning on the shared cores gives the exact two-term variance decomposition. Every separable direction makes each conditional map rank one, attaining both bounds simultaneously. The ratios then have conditional laws independent of the preceding tensor, so the same shared prefix multiplies independent suffix factors. This verifies the finite law, almost-sure random limit and persistent MSE for the stated coupling, including k=0, k=d-1, L=1 and r=1. The gamma-ratio expansion around zero and log(1+2/r) yield the proportional limits under exactly the stated scalings. Replay of the independent proof: reviews/evidence/tt_moments.md. The frozen checks were inspected but not executed and do not establish generality. No pointwise exact variance formula is claimed for arbitrary PSD targets.

## originality

PASS

Two primary papers already cover the marginal Gaussian TT or rMPS sharp variance, and independent averaging covers k=0. The strongest indexed exact alternatives concern one-probe order dependence and one-vector coordinate covariance with independent probes. None of the inspected results analyzes the joint shared-prefix law, finite-probe random-scale factorization and resulting persistent worst-case floor. That coupled-law contribution is the basis of the pass, not the known marginal moment tools or the independent-probe specialization.

## value

PASS

Reusing initial cores is a natural structured-probe design. Knowing its exact worst-case variance, rather than only that some correlation arises, shows when suffix resampling cannot make the estimator consistent, quantifies the rank/order tradeoff, and provides a concrete worst-case family and law. This concerns accuracy under reuse, not a claimed improvement in cost or performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
