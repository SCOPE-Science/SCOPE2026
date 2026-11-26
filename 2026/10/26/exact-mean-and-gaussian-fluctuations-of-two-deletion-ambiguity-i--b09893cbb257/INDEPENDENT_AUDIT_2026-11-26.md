# Independent mathematical audit

## correctness

PASS

The unique greedy leftmost embedding is a bijection between outputs and canonical deletion masks. Nonadjacent deletions must each be run ends; adjacent internal deletions are canonical iff the next retained symbol differs from both, and the terminal pair is always canonical. Counting these cases gives choose(R,2)+H−T, including m=2. For uniform input, adjacent equality indicators of the underlying letters are iid Bernoulli(1/q): any chosen subset of neighboring equality constraints on a path has probability q to the negative size of that subset. Each read-repeat indicator C_i is the product of ell such consecutive bits, giving the exact joint probabilities and dependence range. H and T have the same interior expectations by counting the constant or period-two input windows, with only the initial repeat term p left over. Thus the pair expansion of choose(m−sum C_i,2) gives the stated exact mean. The bounded finite-dependence CLT applies to sum C_i with limiting variance v; expanding the quadratic gives coefficient −(m−(m−1)p−1/2). In the fourth moment of the centered indicator sum, separated singleton components vanish, leaving O(m²) nonzero terms for fixed ell. H−T has O(m) variance by locality. This establishes L² control of the normalized remainder, hence both the Gaussian and variance limits. Fresh direct enumeration independently checked both deterministic formulas and the mean at (q,ell,n)=(2,2,3),(2,2,4),(3,2,4),(4,2,4),(2,3,4), covering 377 words; means were 1, 19/8, 73/27, 181/64, 1. The attached script was inspected but not executed; its larger recorded enumeration does not prove the CLT.

## originality

PASS

The arbitrary-sequence double-deletion identity is already covered, even by an algebraically equivalent exact Resultary formula. The exact expectation and fluctuation law for the dependent, unguarded overlapping-read list are the distinct contribution. Neither the known independent-word formulas nor the inspected overlapping-read code theorems supply that law.

## value

PASS

The overlapping read list is a natural constrained random sequence. Its repeat marginal agrees with the iid model on q^ell symbols, but its leading output-volume variance does not. The exact finite mean and explicit positive covariance correction quantify this distinction and give an analytic check for any proposed approximation of the abstract read-output count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
