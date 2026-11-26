# Independent mathematical audit

## correctness

PASS

The unnormalized cube Laplacian has Walsh eigenvalues 2j. Thus the squared kernel uses z^(j²), z=e^(−4t). Splitting off one coordinate gives the sum identity (the previous-dimension kernel) and the difference identity. The latter uses (2j+2)²=(2j)²+4(2j)+4, so the difference is z times the previous squared-heat kernel composed with ordinary heat e^(−4tL). Ordinary heat is strictly positive for t>0 on the connected cube. Whenever the lower-dimensional squared heat is nonnegative its rows sum to one, making every such difference strict. The sum identity excludes any recovery before τ_(d−1); at τ_(d−1) the two identities show the d-dimensional antipodal entry is negative. From then on every radial list strictly decreases in distance. If the m-dimensional kernel is nonnegative at t>0, its origin row is a probability measure with Walsh means z and pair moments z⁴. The variance of the sum of the m spins is m(1−z²)(1−(m−1)z²), giving t≥log(m−1)/8. The successive derivative magnitudes for the antipodal polynomial have ratio at most 2(d−1)z³, which is <1 at and after τ_(d−1): use τ_2>1/8 for d=3, τ_3>1/4 for d=4–7, and 2(d−1)/(d−2)^(3/2)<1 for d≥8. The small bounds follow from the indicated explicit polynomials and exponential brackets; p_2=(z−1)(z³+z²+z−1) proves the initial unique crossing and the other d=2 entries are positive at t>0. The strictly positive alternating derivative then yields one last crossing and strict increase of the thresholds. At t_0=(log d)/4 the first two terms cancel and the strictly decreasing alternating tail begins positive. At t_0−d^(−2), above τ_(d−1) for large d, the leading contributions are −4d^(−2) and +1/(2d²). For z≤2/d the tail starting at j=3 is O(d^(−6)), by the lower linear bound on j² and binomial magnitude bound. Hence at the root dz=1+1/(2d²)−1/(2d³)+O(d^(−4)); taking −log(z)/4 gives the coefficients claimed. Row sums equal one, so the maximum absolute row sum is one iff entrywise nonnegative. At the recovery time strict radial ordering leaves just the antipodal zeros, while at t=0 the identity is a separate allowed case. Earlier zeros of the antipodal entry are not excluded. Separate replay `python /workspace/review_checks/frozen_probes.py` uses high-precision Newton iterations in dimensions 2,3,4,8,40,100 and checks opposite antipodal signs before the final crossing in d=4; the uniform proof, not the numerical root solver, establishes the last-zero assertion.

## originality

PASS

The supported distinct contribution is the uniform higher-cube phase diagram, strict dimension monotonicity, and quantitative last-antipodal cutoff expansion. The d=2 special case has demonstrable same-day coverage from complete multipartite graphs and is not claimed as independently new. The exact d=4 overlap with a later zero-crossing record is credited. The three-spectral-value discussion in the frozen literature prose needs a finite-dimensional qualification: the cited catalogue Finding itself is an infinite-dimensional counterexample to that extension, not the finite-dimensional theorem. This does not affect the mathematical statement or induction.

## value

PASS

For a canonical product graph and a non-Markovian fourth-order flow, the question concerns the exact return of bounded-data contraction and the geometry at that time. Strictly ordered dimension thresholds despite possible earlier antipodal zeros, antipodal-only vanishing at recovery, and the logarithmic law with signed corrections address this natural stability problem rather than just rechecking eventual positivity or a base graph. The scope is valuable without asserting comparable results for weighted or other graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
