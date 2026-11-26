# Independent mathematical audit

## correctness

PASS

For finite supports S and T, all transpositions fixing S∩T either fix one support pointwise or factor through a fresh atom outside S∪T, so the common intersection also supports. Intersecting supports inside S yields the least one, contained in any other finite support by intersecting that other support with S. For equivalences, the complement of S is either all singleton classes or part of a single infinite class. In the singleton case a named atom may be exchanged with a fresh atom precisely if it is itself a singleton; in the giant case this is true precisely for named atoms in the infinite class. In each case removing all such names still supports the relation and the others are indispensable. Choosing the d removable names gives binom(k,d)(a_{k−d}+B_{k−d}), including k=0. A marked element in a partition accounts for the B_{k+1} giant cases. For arbitrary directed binary relations there are k² named cells, 2k directed mixed cells and two fresh cells (equal/distinct); intersections of deletion events are support on the intersection context. Inclusion–exclusion and Bonferroni then give the exact count and the displayed asymptotic, since the 1- and 2-deletion ratios are 2^{−2k−1} and 2^{−4k}. The giant case has probability 1−o(1); its marked-block deficit has first and second factorial moments kB_k/B_{k+1} and k(k−1)B_{k−1}/B_{k+1}. Bell ratios give mean asymptotic to W(k) and variance o(W(k)^2). The same factorial-moment check for singleton blocks gives a_k/B_k→0; hence full support has probability asymptotic to W(k)/k for equivalences. `python3 /workspace/branches/frozen_replay.py 4` verified complete deficit histograms for k=0,…,4 by enumerating partitions and testing complementary permutation groups for every subcontext.

## originality

PASS

The supported contribution is the exact least-support stratification for equivalences on equality atoms and the resulting contrast with uniformly sampled supported binary relations. The least-support intersection theorem, partition numbers, the Bell-ratio estimate and the marked-block moments are not claimed as original. The ordered-atom catalogue result has different stabilizer orbits and the opposite equivalence full-support behavior; the equality-atom binary orbit normal form does not state the support-stratified census. The 2021 binary-relations paper was recovered in full via its publisher's PDF CDN; its pertinent theorem proves finiteness for a fixed support, not the least-support laws. The arithmetic of the unrestricted class alone is elementary once the orbit cells are known; the comparison is credited for the support-theoretic equivalence census, not the inclusion–exclusion technique by itself.

## value

PASS

The least support controls how many names must be retained. For the same infinite carrier, imposing transitivity and symmetry changes exact full support from overwhelmingly typical to rare; the defect is nevertheless only logarithmic. The exact strata and the W(k) scale quantify both effects in two natural finite ensembles and are directly useful for reasoning about context minimization. This is more than counting all binary orbit assignments or restating an isolated Bell-number estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
