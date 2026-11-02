# Scientific review: Joint rare-return asymptotics for a Pólya urn walk

## Correctness — PASS

For every fixed positive initial urn mass pair, the de Finetti directing probability is beta distributed. Conditional on its value, the increment sequence is iid. Its probability of eventually returning to zero is exactly \(1-|2\Theta-1|\), so conditioning on at least \(k\) returns tilts the directing density by the \(k\)-th power of that quantity. The tilted posterior, normalized by a boundary Laplace integral, has the stated total-variation Laplace limit. The strong Markov property of the conditional iid random walk gives an independent geometric future-return count. The conditional first-return generating function \(1-\sqrt{1-4p(1-p)z^2}\) yields the simultaneous scaled return-epoch Laplace transform. Its limiting inverse-Gaussian conditional density mixes with the exponential drift density to give the exact inverse-exponential law. The argument controls all fixed positive beta shapes, not only integer initial masses.

The standalone standard-library checker verifies 2,335 assertions: exact rational beta and excursion identities, small exhaustive first-return walks, and an independent pair of numerical representations of the limiting timing transform. These checks are finite diagnostics, not proofs of convergence. The analytic proof is supplied in RESULT.md.

## Originality — PASS, qualified

The strongest prior work is Jiang, Sun, Figueiredo, Ribeiro and Towsley (2014), arXiv:1402.4536. It establishes marginal tail asymptotics for the total number of competition ties and the last tie time, and gives exact probabilities for the time of a fixed indexed tie (Section 5.3, Eq. 19–25). This dominates finite-index timing information for the balanced-mass competition and potentially implies the new *marginal timing limit* there after additional asymptotic analysis. Neither that marginal, the geometric return-count mixture, nor a basic beta posterior is claimed as a separate discovery. The central contribution assessed here is a *joint conditional asymptotic coupling* of the hidden directing drift, the \(k\)-th return epoch, and future return intensity, universally for arbitrary fixed positive masses, with explicit conditional transform and independence structure. The inspected 2014 text does not state that joint theorem, and its unequal-mass competition-tie event is not identical to equality of postinitial colour-draw counts.

Balaji and Mahmoud (2025), arXiv:2504.14813, motivate the urn-driven-walk problem, without this joint theorem. Jiang et al. (2016), arXiv:1604.02097, generalize duration/intensity to nonlinear fitness-reinforcement regimes but do not give this latent posterior and joint timing limit. Antal et al. (2010), arXiv:1005.0867, concern first-passage properties, and Mookerjee and Kostinski (2024), arXiv:2412.17994, concern fixed-bias returns. published-finding corpus searches using return-index, mixing, posterior drift, Pareto, inverse-exponential and Pólya aliases returned no matching claim. This is best-knowledge originality, not a proof of priority. Earlier exact indexed-tie kernels and unindexed conditioned-renewal theory remain material priority risks.

## Mathematical value — PASS

A rare high number of returns arises by strongly selecting urn environments with near-zero latent drift. The joint limit describes how that selection quantitatively couples three naturally important quantities: unobservable ultimate urn bias, time spent acquiring the returns, and how many returns remain afterwards. It identifies a universal quadratic time scale, a non-Gaussian inverse-exponential clock, an independently fluctuating future-return mark conditional on drift, and a posterior Laplace structure. This goes beyond separate tail exponents for duration and intensity and gives a usable probabilistic description of an unusual rare-trajectory regime.

## Limitations and closest literature

The conditioning event uses the infinite return count and is not directly observable from a finite path. The result assumes fixed positive initial masses and classical linear reinforcement, with no claimed convergence rate or nonlinear-urn extension. The 2014 all-index probability formulas deserve special independent priority review because they can imply some of the displayed marginals. Earlier works on randomly biased renewal processes or mixture excursions may also contain related conditional limits. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
