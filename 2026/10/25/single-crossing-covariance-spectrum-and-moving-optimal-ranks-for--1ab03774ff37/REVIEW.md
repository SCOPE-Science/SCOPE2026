# Independent mathematical audit

## correctness

PASS

For one reused observation rather than independent fresh iteration noise, the geometric sum gives c_i(K)=sigma^2/lambda_i (1-(1-omega lambda_i)^K)^2. For lambda_i>lambda_j the derivative of log(c_i/c_j)/2 is alpha/(exp(alpha t)-1)-beta/(exp(beta t)-1)<0 for alpha>beta>0; the u=0 endpoint follows by a limit. At t=1 the ratio is lambda_i/lambda_j>1; at infinity its reciprocal is below 1. The filter F_K(z)=(1-(1-z)^K)^2/z for 0<z<=1 has a unique maximum, since its derivative changes sign once when sum_{h=0}^{K-1}(1-z)^(-h)=2K (K>=2), with K=1 monotone. Therefore its sampled spectral variances are unimodal; top-r indices admit a consecutive block. Strict crossing excludes moving a smaller index into a later optimum while a larger index departs. A two-level spectrum proves late retained-trace ratio mu/L. Independent exact rational 4-mode windows were {1,2}, {2,3}, {3,4} at K=1,10,100, and 5,200 bounded numerical rank-window checks across 100 new random spectra passed. Finite checks do not prove the continuous all-spectrum statements.

## originality

PASS

Same-object and stronger-implication search compared: Equivalent formulations checked include Landweber spectral filter unimodality, pairwise covariance singular-value ordering and optimal subspace migration across iteration time; the searched Resultary hits addressed Richardson optimization or unrelated spectra, not this covariance ranking theorem. A broader spectral-filter theorem might imply the property, but the inspected dominant-subspace and variance-estimate results do not establish the exact once-only pair crossings and monotone all-rank maximizing blocks. The claim can be derived from known elementary formulas plus the added global spectral inequalities, but the searched prior conclusions do not explicitly imply the entire universal rank-migration theorem as a stated result. A semantic Resultary query was executed for this problem. All source limitations and possible hidden equivalences are retained as residual risks, not misreported as proof of absolute priority.

## value

PASS

In inverse-problem uncertainty quantification, variance-optimal compression can differ sharply from dominant normal-operator singular directions as iterative regularization evolves. The all-pairs one-crossing and monotone contiguous-window structure are a usable global spectral rule, and the exact arbitrarily small trace fraction isolates an important mathematically motivated failure mode without incorrectly claiming reconstruction or confidence-interval failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
