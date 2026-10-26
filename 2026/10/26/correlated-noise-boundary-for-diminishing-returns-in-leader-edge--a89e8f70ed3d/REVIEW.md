# Scientific review

## Correctness: PASS

The central claim specifies every quantifier: fixed positive-semidefinite correlated-noise covariance, all finite connected undirected positive-weight graphs with fixed leaders, all finite collections of missing leader-to-follower edges. The stationary Lyapunov equation gives exactly half the trace of the grounded inverse times covariance. Its first derivative is nonpositive for every positive-semidefinite covariance; its mixed derivative is the product of an inverse entry and a covariance-weighted inverse entry. Positivity of inverse grounded Laplacians proves the sufficient covariance sign condition. The two-leader large-grounding construction proves necessity for every fixed negative covariance entry. The explicit rational two-follower formula provides an independent sharp sign threshold. The accompanying exact-rational checker passed 8,686 assertions. The proof, not the checker, establishes arbitrary network size and parameter ranges.

## Originality: PASS with residual risk

The strongest direct comparison is Xu--Zhang (2023), arXiv:2308.07008v1, especially its noisy DeGroot equation (3), stationary variance formula (5), and leader-edge supermodularity Theorem 4.3. Its independent-noise objective is a special case, not the iff characterization for fixed correlated forcing. Clark--Bushnell--Poovendran (2012) consider independent link noise and leader-node selection; Summers et al. (2014) treat independent-noise ungrounded coherence edge additions; Mackin--Patterson (2017) treat a leader-node selection formulation. These are substantive stronger-coverage checks, not title matches. Matrix inverse-positivity and second-derivative techniques are standard and may imply some steps from general results. The available literature search did not locate an equivalent general covariance-sign iff or the sharp two-follower correlation frontier. Unindexed or differently described prior theorems remain a priority risk; no publication exclusivity is asserted.

## Value: PASS

Independent-noise supermodularity is used to justify diminishing-return algorithms for leader-edge interventions. Realistic shared or opposing disturbances change covariance signs, so it matters to know whether that guarantee survives. This result gives a full **universal covariance class**, preserves the monotonic variance-reduction guarantee even outside it, and supplies both an exact small counterexample and a sharp tunable correlation boundary. It is not an arbitrary finite enumeration or mere reparameterization: the iff criterion covers networks of all finite sizes and exhibits the precise failure mechanism of the optimization guarantee. Its limitations concern fixed intervention-independent noise, the chosen variance objective, and undirected positive interactions.

Self-review: passed. Independent audit: not yet performed.
