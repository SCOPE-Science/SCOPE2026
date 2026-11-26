# Independent mathematical audit

## correctness

PASS

Grouping roots is equivalent to collapsing each group into one weighted root, since the parent weight is the sum of the grouped root weights and only ordinary leaves are counted. Given the colors, the component parent-choice probabilities factor into independent Hoppe growth processes; their leaf laws depend on the colors only through the sizes. Given group A's size s, the usual beta-mixture coupling generates B's size by n-s draws (or n-s deterministically for no remaining group), decreasing stochastically in s. For strictly increasing g the averaged leaf test strictly increases with the size, since root attachment has positive probability at every step and the leaf count never decreases. The conditional regression of the g-test against s is therefore strictly decreasing; independent-copy covariance of this regression and the averaged f-test proves the sign, strict when both tests are strictly increasing since N_A is nondegenerate. Independently expanding the increments for distinct roots gives the printed recurrences: in the mixed size-leaf equation the two existing size-leaf terms cancel, and in the leaf-leaf equation they give the two H terms against the subtraction of 2J. The factorization by root weights follows by induction from these recurrences and the size moments, not from assuming equal weights. I checked the three closed-form recurrence identities by exact rational simplification, using the empty and one-vertex values separately (and the two-vertex values for H and J). For the limit, conditional leaf variance obeys V_(m+1) <= (1-1/(a+m))^2 V_m + 1/4, giving V_m <= m/4 from m=1 onwards. The bias relative to m/2 is bounded uniformly for positive a, with T_0=0 treated separately. The conditional variance bound plus the Dirichlet color coupling proves the claimed L2 convergence and both limits; the limiting variances are strictly positive.

## originality

PASS

The model, size allocation and single-component leaf laws are prior. The arbitrary-transform aggregate ordinary-leaf dependence theorem, including strictness and arbitrary positive weights, is the distinct claim supported here. The moments are a closed-form evaluation for the model, not a new joint probability mechanism; the limiting covariance and correlation are standard consequences of the mixture and half-size leaf asymptotics. No primary passage checked establishes the joint strict sign theorem for these aggregate leaf counts.

## value

PASS

A sign for every increasing transform of two disjoint groups is a useful joint constraint in a model whose earlier leaf results focus on single marginals. It distinguishes conditional tree independence from the unconditioned negative dependence induced by allocating a fixed population among competing roots. The exact covariance gives a finite-size benchmark, while the limits distinguish persistent random proportions from smaller within-component fluctuations. The meaningful new part is the aggregate dependence result, not the general urn machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
