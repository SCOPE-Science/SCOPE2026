# Independent mathematical audit

## correctness

PASS

The weight-four reduced Świątkowski basis comprises c_q=binom(10,q)4^q binom(28-q,4-q), with dimensions (20475,117000,234000,192000,53760). Inspected verify.py implements all basis monomials and each boundary column over F2 using exact XOR bitset elimination, with claimed boundary ranks (20474,96509,136963,53759) under two reference choices. Independent union-find over the 20475 edge-multisets and 117000 q=1 incidences gives rank d1=20474; independent binomial Gal coefficient gives chi=-765 and claimed Betti formula reproduces it. An Cor 3.18 establishes top F2 class dimension one. The large middle-boundary eliminations were reviewed at code level but NOT executed afresh; this is a computational verification limit, not an imaginary independent rerun.

## originality

PASS

Exact middle-degree mod-two Betti dimensions for four points on K5,5 are not a stated or immediate consequence of An’s top homology and degree-three torsion calculation. The complete reduced-chain computation supplies the missing numerical data; the nearby K5,4 published result concerns a different graph. This remains a best-of-knowledge judgment without exhaustive archival certainty.

## value

PASS

A natural complete mod-two homology table for a canonical balanced complete-bipartite graph at the first difficult four-particle threshold is a useful benchmark for the lower-Betti problem explicitly posed in the primary paper. The result does not claim general polynomial formulas or integral splitting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
