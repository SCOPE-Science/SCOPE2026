# Independent mathematical audit

## correctness

PASS

For a nonempty largest part L, the lower sizes contribute factors (w+(1-w)q^j)/(1-q^j) and L contributes q^L/(1-q^L), consistent with the cited bivariate product and the empty contribution. After factoring out Q, the coefficient of w^m in the exponential has just one monomial with m factors, H_1^m/m!; all remaining monomials have at most m-1 factors. The Riemann sum for tH_1 tends to the integral of e^(-2u)/(1+e^(-u)), equal to 1-log 2. In the sector |Im z|<=Delta Re z, each 1+exp(-kz) is bounded away from zero uniformly in k: use a nonnegative real part for small k Re z and the reverse triangle inequality otherwise. Thus all fixed H_r are O(1/|z|). The eta quotient for Q has exponential exp(pi^2/(12z)) uniformly there, whose modulus is at most exp(pi^2/(12|z|)); this supplies the corrected Ingham complex bound, not just a real-axis estimate. The coefficients are nonnegative, with radius one by convergence inside and positive-axis divergence, and the cumulative theorem uses beta=-m, gamma=pi^2/12 and lambda=(1-log 2)^m/(m! sqrt(2)). Its constant lambda gamma^(-m/2-1/4)/(2 sqrt(pi)) is the printed one. Real X follows by taking the integer part. The separate replay /workspace/branches/d4847873-e9af-4fca-855e-db0059c586c6/independent_replay.py matched product and direct partition counts for n<=16 and m<=4; at X=1000 the normalized cumulative ratios were about 0.9683, 1.0099 and 1.1283 for m=1,2,3. These are diagnostics only. The supplied checker reports numerical ratios, but its assertions do not certify convergence or tight agreement.

## originality

PASS

The gap-free base case and exact bivariate generating product are already known. The supported distinct claim is the fixed-m cumulative hierarchy beyond that case, including its explicit factorial dependence and factor 1-log 2; it requires coefficient-sensitive asymptotic analysis and sector control. The exact enumerative identities reviewed do not themselves state that hierarchy, and the general cumulative theorem only applies after its singular inputs are established.

## value

PASS

The law quantifies how each additional allowed missing size changes the growth scale relative to gap-free partitions: an explicit factor of order sqrt(X) at each step, with a factorial normalization and the same exponential scale. This concerns a natural fixed-defect statistic and does not conflate its distribution with aggregate or least-gap results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
