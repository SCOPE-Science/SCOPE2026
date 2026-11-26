# Independent mathematical audit

## correctness

PASS

Substitution in either implicit stage equation yields R=1−r/(1+ru). The inverse map u=(1−R)^{-1}−1/r gives multiplier density (1−R)^{-2} on [1−r,1/(1+r)]. Integrating over [−t,t] and clipping at the two endpoints verifies each quantile branch: before clipping the CDF is 2t/(1−t²); afterward it is 1/(1−t)−1/r or 1+1/r−1/(1+t). The endpoint magnitudes tie exactly at r=√2. As stated by continuity, the quantile at p=0 is its support endpoint (the literal infimum over all real x at p=0 would instead be −∞; the continuous convention affects no integrals or couplings). The layer-cake Fréchet lower bound is attained by opposite response ranks. The joint survival probabilities are continuous because the response marginals have no atoms, so equality of integrals forces equality in the bound everywhere; disintegration over g=R² gives uniform-stage lifts. For r≤1 strict monotonicity forces ordinary antithetic stages. For each r>1 both g(u) and g(1−u) strictly decrease on a nontrivial initial interval, which rules out opposite response ranks and permits a strictly improving equal-length partner exchange. An independent adaptive Simpson reproduction gave K2=0.001879920275199488 and checked the ordinary antithetic value 5/3−(3/2)log 3=0.01874823366450218, ratio 9.9728876335. Replay: /workspace/branches/8b1d4df8-f4f0-4276-8cf1-187ace755bdd/r2_independent_reproduction.py. The uniform-in-law conclusion is analytical, not inferred from the frozen discretization or the benchmark.

## originality

PASS

The countermonotone extremum itself is known. What remains distinct in the checked sources is the method-specific exact optimum with its piecewise quantile and the sharp separation between fixed-r RMS optimality of ordinary antithetics and the sign branch supplying the upper response tail.

## value

PASS

The prescribed-stage antithetic construction is a natural candidate for this stability objective; the result supplies the exact frontier where it ceases to be optimal, the correct rank target thereafter, and an exact design objective for each fixed decay rate. The sharp strict failure for every r>1 and nearly tenfold r=2 difference are meaningful in this scoped scalar question, without implying nonlinear accuracy or a coupling optimal across rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
