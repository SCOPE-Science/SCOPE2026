# Independent mathematical audit

## correctness

PASS

Reducing sqrt(p)|000>+sqrt(1-p)|111> to any qubit kills the cross terms, giving eigenvalues p,1-p. The proposed diagonal instrument is complete, with squared diagonal sums (1+0,1/7+6/7)=(1,1). For p=1/8 the first output has two squared amplitudes 1/8 and 1/8, so its probability is 1/4 and its three marginal entropies are all 1 bit after normalization. The second output is proportional to |111>, with squared norm (7/8)(6/7)=3/4 and all marginal entropies zero. Independently evaluating the input entropy, h_2(1/8)=3-(7/8)log_2 7 < 5/8 since 524288=2^19<7^7=823543. Cubing gives a product less than 125/512, which is less than the output average 128/512. This exact arithmetic suffices without executing the frozen checker or using a floating entropy. A complete local instrument is already an LOCC protocol with known outcome, so this disproves the universal pure-state average inequality. It neither proves violation under deterministic pure-to-pure LOCC nor addresses a mixed-state extension.

## originality

PASS

The unrooted functional and generic local-concentration ideas are not new. The specific conclusion that this functional is not a strong LOCC monotone, with a single-qubit filter and exact branch comparison, is not established in the comparable indexed and primary passages inspected. The strongest earlier catalogue analogue is for a bipartite product of Schmidt probabilities rather than three marginal entropies. The 2006 antecedent cited for the entropy product is an unresolved access risk, not negative evidence or a verdict.

## value

PASS

Strong LOCC monotonicity is independently motivated because selective local operations and classical outcomes are basic to interpreting a resource measure. A two-outcome filter on one qubit shows that using legitimate marginal entropies as factors does not make their product a strong monotone. The exact counterexample directly tests a published suggested quantifier, while retaining the distinction between the raw product and its geometric mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
