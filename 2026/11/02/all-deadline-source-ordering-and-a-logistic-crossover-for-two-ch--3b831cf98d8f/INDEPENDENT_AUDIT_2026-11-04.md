# Independent mathematical audit

## correctness

PASS

Alternation decouples A and B visits, greedy selection has greatest success probability whenever a new offered neighbor exists, and a monotone count coupling gives optimality at every deadline. Each side is a sum U_m of independent geometric waits of success r(2m-r)/m²; parity gives T^A=max(2U_a-2,2U_b-1), T^B=max(2U_a-1,2U_b-2). Geometric-delay factorization U_a=U_b+W independent and log-concavity of each completion CDF imply the monotone CDF ratio and source ordering for a>=b. Direct coupling yields expected difference P(U_a>U_b)-P(U_b>U_a). For a-n ~delta n/log n, independent centered collectors converge to Gumbels with δ shift, maximum has log(1+expδ) shift and win probability logistic, giving tanh(δ/2) signed difference. Independently checked coupon CDF and source inequality for 1<=b<=a<=6, deadlines <=28 using exact rational dynamics. The written step-4 fixed-K remainder mean omits a vanishing-as-K→infinity correction; the double-limit argument survives after accounting for it. Finite tests not infinite proof.

## originality

PASS

Two-choice random walks and one-collector multiple-choice coupon asymptotics are prior work. The exact all-deadline biclique source stochastic ordering, independent-delay ratio argument, and near-balanced signed logistic source-advantage window are not stated in inspected relevant work; qualified best-of-knowledge originality.

## value

PASS

Optimal source part being the larger lower-degree side is a counterintuitive full stochastic optimization result; its exact signed window provides a nontrivial sharp transition even though the expected advantage is bounded by one step. This natural cover-time problem is not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
