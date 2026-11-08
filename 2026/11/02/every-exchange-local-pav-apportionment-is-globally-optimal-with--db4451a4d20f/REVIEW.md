# Independent mathematical audit

## correctness

PASS

For three parties, partition nonempty approval ballots by singleton i, complement-of-i, and all-three. With K seats, score is cH_K+sum_i(a_i H_{k_i}+b_i H_{K-k_i}). Forward marginal delta_i(t)=a_i/(t+1)-b_i/(K-t) is nonincreasing. One-seat-exchange local optimality forces every last selected marginal >= every first unselected marginal in other party; monotonicity extends inequality to all selected vs unselected entries including same party. Thus selected K marginals are global top K; greedy prefix selection is optimal. m=1,2 similarly. The m=4 K=2 obstruction was published previously and is not claimed new.

## originality

PASS

Best-of-knowledge original in its precise qualified statement. Gölz–Yaghoubizade show local optimality implies priceability, not PAV global optimality, and provide four-party non-global local maximizer. The theorem here supplies the universal positive exact m<=3 boundary using a separable-concavity reduction; the general separable greedy lemma is standard and not a new technique. Priority limits are recorded; an inaccessible plausible source alone is not treated as automatic failure.

## value

PASS

This is the sharp naturally parameterized positive local-to-global regime for an established apportionment objective, giving reliable greedy exact optimization under at most three parties. The structural boundary is meaningful despite elementary discrete-concavity proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
