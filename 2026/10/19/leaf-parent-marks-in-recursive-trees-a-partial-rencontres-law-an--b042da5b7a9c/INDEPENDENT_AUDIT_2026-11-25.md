# Independent mathematical audit

## correctness

PASS

Rechecked repairs/2/RESULT.md and its slogan. Conditioning on a prescribed set of children S all being leaves preserves independence of parent choices and restricts P_i to the earlier labels outside S. For the s-th member i_s of S the allowed count is i_s−s, so the conditional factors 1/(i_s−s) cancel the numerators of the leaf-set law, yielding 1/(n−1)_r for a compatible cylinder, including r=n−1. A marked child that is also a prescribed parent or a child with two prescriptions is impossible. For j<k and each child h>k, j has n−j−2 compatible choices, excluding k and h. Subtracting the product of means gives the displayed negative covariance, whereas the two same-parent marks never have those conflicts and give the stated positive covariance. In arbitrary fixed mixed factorial order, collision and forbidden-label exclusions cost at most O(n^(r−1)) uniformly over parent indices; dividing by (n−1)_r proves convergence of all mixed factorial moments to those of the moment-determinate product Poisson law, also at u_s=1. The single-parent indicator law is identified by inclusion-exclusion with a subset of coordinates of a uniform (n−1)-permutation. Subtracting the leaf probability gives protection, and removing one constrained coordinate proves strict adjacent differences except for the two final zero probabilities. Termwise magnitudes are bounded by 1/r!, giving the stated profile by dominated convergence. Independent replay (python /workspace/branches/independent_checks.py 2) passed 33,866 exact cylinder checks over all orders in trees of n=2..6 and exact protection probabilities for every label in that range. It does not prove the limit. The frozen supplementary script was read, not run, and its reported finite result is not an independent certificate.

## originality

PASS

Pass for the repaired theorem, not for the frozen presentation of the arbitrary-parent cylinder as a new claim. The earlier leaf-set proof itself gives the conditional uniform parent choices, so multiplying the probability of the leaf set by the conditional probabilities of the specified parents yields the full cylinder law. The restricted fixed-point identity is then a direct inclusion-exclusion consequence. The repair explicitly credits this coverage and removes both as independent novelty claims. The surviving result concerns joint direct-child dependence across prescribed parents, the simultaneous Poisson age limit from mixed compatible assignments, and birth-label-resolved protection and its ordering. The strongest inspected comparisons give the root-only exact law, leaf-only birth-label events, a scalar root Yule/mixture law, or the aggregate and root protection formulas. None gives that joint deterministic-age theorem or the all-label protection analysis without the additional interaction and limiting arguments. This is a bounded best-of-knowledge assessment, not a historical priority claim.

## value

PASS

After removing the novelty claim for the exact cylinder, the repaired result still separates within-parent and cross-parent dependence at finite size and shows when the latter vanishes at the joint distribution level across different birth fractions. Direct leaf children are exactly the obstruction to protection for nonleaves. The all-label probability and strict ordering give information that a root law or total expectation cannot recover. The result is useful at fixed dimension without making an unsupported claim of asymptotic independence over all parents.

The dated certificate retains the supplied scientific assessment, sources and limitations.
