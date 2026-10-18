# Independent mathematical audit

## correctness

PASS

Because distinct vertices incoming directed-arc collections are disjoint, each in-degree histogram is multinomial with binomial cell probabilities; likewise for outgoing. An in-degree at i and out-degree at j share exactly one Bernoulli arc j->i if i!=j (none when i=j). Law of total covariance yields mixed entries n(n-1)p(1-p)(h_{k-1}-h_k)(h_{l-1}-h_l). Binomial score identity converts to rank-one n v v^T after whitening. u=sqrt(b) and v=standardized binomial score are orthonormal; in the 2n space, (u,0),(0,u),(v,-v) are three zeros; (v,v) has 2n; orthocomplement has n with multiplicity 2n-4. The whitened in-minus-out difference has covariance 2n(Id-uu^T-vv^T), so the mean Pearson contrast is n-2 exactly. Independently enumerated every directed loopless graph for n=2,3 at p=1/3,2/3 using exact rational probabilities, matching each covariance entry; the all-n proof uses the one-shared-arc lemma, not enumeration.

## originality

PASS

Best-of-knowledge novel exact finite covariance eigenspectrum and Pearson-contrast expectation for joint in-/out-degree histograms under independent directed arcs; models in the most relevant published papers differ materially.

## value

PASS

An exact p-independent whitened eigenvalue classification isolates all deterministic linear constraints and provides a finite-sample mean Pearson discrepancy for two natural directed-degree histograms. The whole matrix identity applies to every graph order and Bernoulli probability, providing a reusable covariance object beyond textbook separate-binomial variance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
