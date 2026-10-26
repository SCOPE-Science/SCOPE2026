# Scientific review

## Correctness — PASS

The weighted-wheel adjacency splits orthogonally into a two-dimensional hub/uniform-rim sector and the nonuniform Fourier modes of the cycle. The two hub-sector eigenvalues are \(1\pm\sqrt{1+n\tau^2}\); the nonuniform rim energies are \(2\cos(2\pi k/n)\) with multiplicities one or two. Only the lower hub eigenvalue can collide with a rim Fourier value, and the resulting real algebraic equation gives the complete positive spoke-weight list. Normalized spectral projections prove the resonant survival coefficient and a dissipative spectral lemma rules out other persistent hub mass. The exact unit-spoke classification additionally follows from a degree bound and irreducible cyclotomic polynomials for the remaining small sizes. The standalone checker passed 1,438 finite spectral and exact-rank assertions; its finite sample is not substituted for proof.

## Originality — PASS relative to inspected sources

The most relevant full texts are Anishchenko–Blumen–Mülken (arXiv:1111.7065), Razzoli–Paris–Bordone (arXiv:2011.13794), and Razzoli–Bordone–Paris (arXiv:2202.13824). Their respective results concern Laplacian-type unitary spreading on star-to-complete networks; a general spectral subspace method for absorptive transport on other graph families; and a universal-hub reduction for adjacency walks plus a Laplacian result for absorption at the hub. None states the complete positive spoke resonance weights and exact hub-to-**rim** absorption survival coefficients for the adjacency wheel. The present claim uses their methods but requires additional Fourier collision, trap-projection and arithmetic arguments. Searches using aliases such as wheel/cone over cycle, spectral observability, dark modes, and weighted spoke trapping found no dominating direct statement. A broad spectral-observability theorem or unidentified specialist calculation could still imply the specialized result; historical priority is not conclusively established.

## Mathematical value — PASS

This is a natural complete classification in one physically interpretable parameter (uniform spoke strength) for a fixed source-to-detector geometry. It distinguishes a generic absorbing hub excitation from isolated exactly protected resonances, supplies exact survival masses and bright ranks for all cycle lengths, and isolates the two unweighted exceptions \(n=3\) and \(n=8\). The singular dependence of eventual survival on the spoke parameter illuminates noncommutation of infinite-time and detuning limits rather than presenting an arbitrary small graph numerical artifact.

## Scope and remaining risk

Only finite, coherent, adjacency-generated single-particle dynamics with equal rim hopping and equal positive spokes are classified; finite absorption times, general topology, and robustness under noise are not. The general method of spectral dark-state detection and the two-dimensional hub sector were known, and an unlocated broad theorem could imply the explicit formula. No claim of independent verification or historical uniqueness is made.

Self-review: passed. Independent audit: not yet performed.
