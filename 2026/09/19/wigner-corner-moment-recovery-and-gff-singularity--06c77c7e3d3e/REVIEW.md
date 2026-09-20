# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** For a Hermitian matrix,
\[
\operatorname{tr}(M_k)-\operatorname{tr}(M_{k-1})=X_{kk}
\]
and
\[
\operatorname{tr}(M_k^2)-\operatorname{tr}(M_{k-1}^2)
=
X_{kk}^2+2\sum_{i<k}|X_{ik}|^2.
\]
These identities establish that the proposed statistics are functions of nested corner spectra alone and reduce the probabilistic analysis to independent entry blocks.

Writing \(Y=|X_{12}|^2\), \(v=b-1\), and
\(Z_k=(\sum_{i<k}(Y_{ik}-1))/\sqrt{k-1}\), direct fourth-moment expansion gives
\[
\mathbb EZ_k^4
=
3v^2+\frac{\mu_4-3v^2}{k-1}.
\]
Independence across columns then gives the displayed exact variance of \(\widehat b_n\). The strong law follows from summable variance weights, and the central limit theorem follows from Lyapunov's condition using the source model's all-moments assumption. Exact independence of \(\widehat a_n\) and \(\widehat b_n\) follows from independence of the diagonal and off-diagonal entry families.

For the limiting field, Raposo explicitly identifies the first two angular modes with independent Brownian motions scaled by \(\sqrt a\) and \(\sqrt{b-1}\). Integrating the stated mode normalizations against the corresponding sine functions gives the two normalized Brownian processes in the record. Standard Brownian quadratic variation then recovers \(a\) and \(b-1\) almost surely. Distinct parameter pairs therefore concentrate on disjoint measurable quadratic-variation events, proving mutual singularity. The finite-grid Hellinger, KL, and chi-square formulas are the standard exact formulas for independent centered normal increments.

A standalone numerical check reconstructs the diagonal entries and new-column energies from corner eigenvalues to floating-point precision and evaluates the exact variance and finite-grid separation formulas.

## Originality

**PASS, to the best of our knowledge.** Borodin's submatrix CLT and Raposo's two-parameter extension are prior art. Raposo already identifies \(a\) and \(b\) as the parameters controlling the first two Fourier modes. Classical Feldman--Hájek theory already implies broad equivalence/singularity principles for Gaussian measures, so generic Gaussian singularity is not claimed as new.

The novelty claim is restricted to the explicit nested-spectrum estimators, their exact finite-\(n\) variance and universal leading variance for \(b\), the strong parameter recovery and induced singularity statement for infinite nested-corner spectral laws, and the explicit quadratic-variation/finite-resolution statistical separation for Raposo's field family. Targeted searches for Wigner fourth-moment estimation from principal-minor spectra, corner-spectrum moment recovery, and quadratic-variation identification of the new field parameters did not locate these formulations.

The main residual risk is that the finite-corner construction may be implicit in older literature on low-degree trace statistics, spectral minor processes, or method-of-moments inference. The field singularity is structurally close to a direct application of classical scaled-Brownian singularity; its value here is the explicit source-specific separator and its match to the finite-corner parameter.

## Value

**PASS.** The result turns the two moment parameters that govern the new limiting field into observable statistics of nested eigenvalues alone. It gives finite-sample unbiased estimators, an exact variance formula, a universal first-order fluctuation scale for the off-diagonal fourth moment, and almost-sure identification from a single growing corner process. At the limiting-field level it shows that the interpolation parameters do not merely alter covariance continuously: distinct parameter values define mutually singular continuum laws, despite remaining mutually absolutely continuous at every fixed positive finite radial resolution.

## Limitations

The finite-matrix statements are presented for the complex Hermitian normalization. The proposed estimator is not claimed to be statistically optimal for the full corner-spectrum experiment. The CLT uses the source model's all-moments hypothesis. The field singularity requires refining radial observation; fixed finite grids with positive variances remain equivalent. The circle modes are generalized-field linear functionals, not pointwise field values. Independent audit has not been performed.
