# Scientific review of the matching-priced bipartite spectral-gap theorem

## Correctness

**PASS.** The domain includes every integer \(m\ge3\), two strictly positive edge prices and budget, and all independent nonnegative edge rates. The full proof constructs two orthogonal dimension-\(m-1\) spectral subspaces, computes their edgewise projector norms exactly, and obtains universal linear upper bounds in the total matching and nonmatching conductances. Their weighted combination gives the cheap-price optimum; the antisymmetric projector gives the expensive-price optimum. The block spectrum attains both bounds. Equality of Rayleigh traces, not merely averaging symmetry, forces every unrestricted optimizer to have two edge classes, proving strict-phase uniqueness and exactly the critical segment. The included checker passes 4,506 supplementary tests, including exact symbolic factors and rational boundary cases. No finite test is used to establish the all-size quantifiers.

## Originality

**PASS on the primary texts and published-record searches inspected, with residual priority risk.** Sun–Boyd–Xiao–Diaconis (2006) establish the general continuous-time spectral-gap optimization SDP, but their inspected examples do not give the price-sensitive matching-vs-crown classification. Ghosh–Boyd–Saberi (2006) optimize the *sum of pairwise effective resistances*; their discussion of the different spectral-gap problem does not imply its optimizer here. Boyd–Diaconis–Parrilo–Xiao (arXiv:0709.0955) treat the discrete-time second-largest-eigenvalue-modulus objective. Public database results concerning crown graphs and complete bipartite graphs did not include this exact priced-gap statement; absence of a matching search result is not a mathematical uniqueness certificate. Existing work on the same priced matching graph for effective resistance and spanning trees does not automatically determine a Laplacian Fiedler optimum. The full 2009 symmetry-paper text was unavailable from one repository endpoint; specialist overlap remains possible.

## Mathematical value

**PASS.** The object is a natural two-orbit perturbation of a complete bipartite communication network, and the price threshold describes a genuine support transition from all edges to a crown graph. Beyond a numerical rate formula, the result classifies **all** independently weighted global optimizers, proving a unique design on each open price phase and exactly a nontrivial continuum at criticality. It also shows that a cheaper distinguished matching is *not* preferentially strengthened in the cheap phase: even with unequal prices, all positive optimal rates are identical. This is a natural exact benchmark for cost-sensitive continuous-time network mixing, not a finite census, parameter renaming, or a restatement of generic SDP convexity.

## Closest literature and limitations

The closest directly governing primary text is Sun et al. (2006), DOI `10.1137/S0036144504443821`, sections 1 and 5. The earlier Ghosh et al. (2006) original is DOI-related to `10.1137/050645452` but studies a distinct network objective. Boyd et al. (2007/2009) is a neighboring discrete-time symmetry treatment. The exact family and equality-rigidity proof remain the proposed contribution. Full specialist priority checking is incomplete, and independent mathematical review remains outstanding. The result does not address unequal sides, an arbitrary matching-price matrix, discrete-time chains, or prescribed nonuniform stationary distributions.

Self-review: passed. Independent audit: not yet performed.
