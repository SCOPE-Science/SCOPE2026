# Scientific review

## Correctness — PASS

The Newton expansion K_x=sum c_j T_j T_j^T has exact combinatorial coefficients; for j<k, c_j is bounded below by x^((k-j)^2)(2-exp(1/4)) on x<=1/(k-1). B_k=c_k decreases strictly there by an explicit derivative estimate, and is negative at the right endpoint. The Boolean-lattice up/down commutator proves T_{k-1} full column rank for n>=2k, giving endpoint rank, nullity and a strictly negative top-sector eigenvalue immediately outside the interval. An exact standalone Python checker passes 75 rational coefficient checks, 5300 entry identities, and 8410 direct top-sector components. The claim explicitly excludes the unclassified upper-x region.

## Originality — PASS (bounded review)

Krebs and Shaheen (2008) establish the generic Johnson adjacency spectra, not this all-k n-independent first Gaussian loss or boundary rank. Feragen et al. establish general Gaussian-kernel geometric obstructions, not this finite Johnson threshold. An earlier result for Hamming products uses the same top-difference polynomial B_k but has a different ambient metric and does not imply the sharp Johnson lower bound or endpoint rank. Checked public-index hits concern Johnson spectral concentration and Hamming shell problems without the claimed all-k frontier. Residual risk: an unlocated general positivity-cone theorem might yield the present result as an immediate specialization.

The closest inspected primary sources are Krebs--Shaheen (2008), DOI 10.13001/1081-3810.1256, and Feragen--Lauze--Hauberg (2014), arXiv:1411.0296. Related Hamming-cube and Johnson spectral-concentration claims were compared for implication and differences in metric, parameter and operator. An unlocated general association-scheme cone theorem remains a real originality risk.

## Mathematical value — PASS

A single scalar determined by subset size k governs the initial Gaussian covariance feasibility on all binom(n,k) observations independently of n, and the exact singularity size at the sharp boundary is binom(n,k)-binom(n,k-1). The finding explains this with a positive incidence-Gram decomposition and identifies the top incidence-harmonic obstruction. This is a natural infinite family and a complete first-loss cutoff, not a numerical slice or routine parameter adjustment.

## Limits

The result does not exclude isolated positivity windows beyond the first crossing; the standard all-ones endpoint is semidefinite. Finite verification is supplemental.

Self-review: passed. Independent audit: not yet performed.
