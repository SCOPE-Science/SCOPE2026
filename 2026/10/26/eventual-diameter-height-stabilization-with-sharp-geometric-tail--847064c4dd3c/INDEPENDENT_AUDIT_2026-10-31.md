# Independent mathematical audit

## correctness

PASS

PASS: Induction on parent choice proves vertex depth increments in {0,1}, so H_n=depth(v_n)>=ceil(n/2). Infinitely many first-predecessor choices force all late vertices to descend from unbounded ancestor markers, hence a unique infinite spine with finite offspine paths. The length of each tooth at spine position i equals ceil(r_i/2) for the initial zero run of second-predecessor choices, and its label satisfies sigma_i<=2i. With K=sup_i(L_i-i), the event L_i-i>=k requires a specific run of >=2(i+k)-1 zeros, and union bounding <=(2i+1) possible starts yields C(q)q^{2k-1}. The first 2k-1 zeros from the root give lower bound q^{2k-1}. K is a finite attained maximum almost surely and d(u,v)<=H_n+K for all vertices; a far-tip witness and late v_n attain equality. Thus eventual stabilization is proved, not extrapolated. An independent finite tree checker verified 511 eventual-tail tree instances by direct all-pairs BFS and spine decomposition.

## originality

PASS

PASS (qualified): Tang–Wang–Wu 2026 study exactly this attachment process and in their §3.1 already prove the one-end spine and compute geometric tooth length marginals (including a deterministic run-to-tooth lemma). Those are explicitly credited, not claimed new. The exact finite-tree diameter-minus-height stabilization law with random global supremum K and its sharp two-sided tail rate is not stated in the accessible full paper, whose searchable text has no diameter claim. The geometric distance identity is a standard comb fact; the sharp stochastic tail is model-specific. A prior comb-diameter theorem may imply the deterministic portion but not automatically this tail.

## value

PASS

PASS: The limit converts a global finite-tree metric observable into an eventual stationary integer correction, and identifies its rare-deviation exponent sharply for every Bernoulli parameter. That is a substantive probabilistic extension of the known one-endedness and marginal tooth calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
