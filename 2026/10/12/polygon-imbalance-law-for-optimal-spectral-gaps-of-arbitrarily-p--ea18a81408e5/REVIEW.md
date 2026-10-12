# Scientific review

## Correctness — PASS

The spectral upper bound follows by inserting a minimum-resultant polygon embedding into the Rayleigh inequality. The minimizing resultant length is exactly the positive excess of the largest square-root price over all others, and the squared centered norm is \(S-\delta^2/(m+1)\). In the balanced regime a constant-rate star realizes the upper bound. In the unbalanced regime the proposed rates have exact unit cost; the displayed Cauchy--Schwarz plus square decomposition proves that their candidate eigenvalue is the second eigenvalue. Equality in the embedding bound forces each individual leaf rate, proving uniqueness in both regimes. The proof handles arbitrary real prices, the equality boundary and two-leaf stars. Exact checks: 1,360 rational price vectors and 77,488 exact quadratic certificate evaluations. Independent verification has not been undertaken.

## Originality — PASS with residual historical risk

Sun--Boyd--Xiao--Diaconis (2006, sections 1, 3--5) gives the general edge-cost spectral SDP and maximum-variance dual, not an explicit all-positive-price star solution. Göring--Helmberg--Wappler (September 2005 preprint, Example 6) treats uniformly priced stars and their embeddings, not heterogeneous prices. Farhadi--Louis--Singh--Tetali (2022 version, sections 2--3) analyzes tree embeddings and a distinct \(\lambda_\infty\) star problem, not the stated uniform-to-heterogeneous optimal-rate transition. The assertion is an exact classification derived using established geometric duality, not a claim of novelty for duality itself. There remains a risk of an unlocated historical special theorem: the full text of Fiedler (1990) was not accessible for comparison, although its available abstract treats equal average edge weights. This source-access limit is not proof of novelty.

## Value — PASS

A complete positive-price vector is a natural input for resource allocation on hub-and-spoke diffusion networks. The full-dimensional phase boundary is a polygon inequality in square-root costs, so substantial price heterogeneity can leave the optimal rates exactly uniform; across that boundary the unique optimizer and the slow-mode multiplicity change explicitly. These sharp budget, rate, and eigenvalue formulas address a motivated exact design question rather than a finite parameter table or an arbitrary slice. Scope is limited to symmetric continuous-time stars.

## Closest literature and limitations

The strongest verified precedents are the general continuous-time spectral optimization and embedding duality of Sun et al. (2006), and the equal-price star example of Göring et al. (2005). Farhadi et al. (2022) provide broader tree-embedding methodology with a different star functional. Fiedler (1990) could only be compared via its abstract; another unstated exact arbitrary-price star formula in the historical literature remains possible. The theorem is not an extension to discrete-time fastest mixing, nonuniform stationary masses, or arbitrary trees.

Self-review: passed. Independent audit: not yet performed.
