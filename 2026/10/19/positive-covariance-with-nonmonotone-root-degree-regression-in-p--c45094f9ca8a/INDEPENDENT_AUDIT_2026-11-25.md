# Independent mathematical audit

## correctness

PASS

For Q=2(n−1), the degree-1 survival multiplier is 1−1/Q and the degree-2 mass evolves by (1−2/Q)r_n+p_n/Q, so the masses agree from their common n=3 initialization. Counting separately whether the root is a leaf gives restricted first-moment recurrences u_{n+1}=(1−2/Q)u_n+p_n and v_{n+1}=(1−3/Q)v_n+(1−2/Q)p_n+u_n/Q. Normalizing by p_{n+1} gives E[L_n|D_n=1]=2n/3, while the complement of the drop multiplies by (2n−5)/(2n−3), telescoping to 1/(2n−5). Thus the drop is zero at n=3, strict for n≥4, and followed by a larger conditional value at the positive-probability star outcome. The cited earlier covariance is valid for exactly this seed. In the frozen broader proof the covariance increment follows by cancellation of the two conditional mixed-product terms and induction on both marginal means. With p_n∼1/√(πn), Var(D_n)∼(2−4/π)n and Var(L_n)∼n/9, all original asymptotic constants check. Independent exact rational joint-state propagation (`python3 review_checks/finite_checks.py 5`) checked the conditional means, covariance sum and both variance calculations through n=25. The packaged checker did not itself test the leaf second moment in its history loop, contrary to the original verification notes; the corrected notes describe its actual scope.

## originality

PASS

Pass only for the repaired claim: the two exact conditional leaf means at root degrees 1 and 2, and the resulting nonmonotonicity. The earlier exact covariance result is credited and used as context, not restated as a contribution. The covariance and marginal moments do not determine this regression. No covering conditional statement was identified in the available closely relevant material.

## value

PASS

The exact regression drop is an all-size witness that the known positive covariance does not correspond to monotone dependence of the conditional mean on the root degree. It compares the natural, equally probable first two degree classes, is strict from the first nontrivial size, and tends to one leaf. The positive-probability maximum-degree star rules out monotone decrease as well. This identifies precisely where a covariance-only interpretation fails without presenting the covariance as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
