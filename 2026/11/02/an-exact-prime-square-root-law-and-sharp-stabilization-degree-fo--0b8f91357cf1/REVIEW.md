# Mathematical review

## Correctness — PASS

The proof conditions on the reduction modulo \(p\), treats every simple root by the linear Hensel congruence, and treats each distinct multiple root as an independent affine evaluation constraint on the uniformly random coefficient-lift polynomial. Distinct repeated roots number at most \(d/2\), so the Vandermonde rank argument is applicable without any bound relating \(d\) and \(p\). The Euler-product cancellation then establishes the coefficient formula for all primes, including \(2\), and all nonnegative degrees. Algebraic differentiation and the top coefficient of the numerator prove the moments and the sharp last degree jump. The finite-field squarefree count and factorial moments verify the limiting-law corollary. Exact finite enumeration provides additional, non-decisive checks.

## Originality — PASS, with priority risk

Simhi (2026), §§3.1 and A.1, studies local root counts and exceptional singular lifts but obtains estimates and does not provide the explicit monic prime-square distribution or its sharp degree-stabilization threshold. Jain–Moon–Wu (2023), §§3 and 5, study finite-field distributions and pose prime-power questions for a different, unrestricted-degree-bounded coefficient model, not an all-degree monic prime-square law. Leont'ev (2006) treats finite fields and Bhargava et al. (2022) treat actual roots over the local field, not the finite root fibers. An earlier quadratic result treats unrestricted nonzero quadratic coefficient vectors only; its statement does not cover all monic degrees or the threshold \(2p\). Searches for equivalent probability-generating functions, factorial-moment formulations, and stabilized degree laws found no explicit covering statement. Unindexed older work or straightforward but unpublished specializations remain possible.

## Mathematical value — PASS

The exact law addresses the natural prime-square local statistic used in a recent arithmetic probability theorem and provides an all-degree analogue of a prime-power distribution question in the literature. Its **sharp** stabilization cutoff \(2p\) and degree-independent variance are structural, not a small numerical improvement or ad hoc finite census. The failure of second-moment convergence despite weak convergence to the permutation fixed-point law explains the role of rare singular lifts in local arithmetic statistics.

## Closest literature and limitations

The source's local bound and the older prime-power question motivate the calculation but do not imply its explicit monic formula. No assertion is made about multivariate/unrestricted polynomials, higher prime powers, or actual roots over \(\mathbb Q_p\); priority risk remains for unindexed work.

Self-review: passed. Independent audit: not yet performed.
