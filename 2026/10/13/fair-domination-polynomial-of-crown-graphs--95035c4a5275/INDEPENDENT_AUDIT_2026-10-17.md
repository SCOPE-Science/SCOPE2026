# Independent mathematical audit

## correctness

PASS

For Cr_n=K_{n,n} minus a perfect matching and selected-index sets I,J, an outside a_i sees |J|-1_{i in J} neighbors and outside b_i sees |I|-1_{i in I}. Equality and positivity of all outside degrees gives exactly I=[n] or J=[n], I=J≠empty, or I union J=[n] and |I|=|J|. Partitioning these disjoint cases gives 2x^n(1+x)^n-x^(2n)+sum_{m=1}^{n-1} binom(n,m)x^(2m)+sum_{m=ceil(n/2)}^{n-1} binom(n,m)binom(m,n-m)x^(2m). Thus fd=2 with n minimum sets, and D_f(1)=3*2^n+T_n-4. Independent literal adjacency exhaustive test 87360 subsets for n=3..8 corroborates coefficients; all n follows from the occupancy proof.

## originality

PASS

The minimum fd(Cr_n)=2 and deleted-matching-pair witnesses are PRIOR in Sampath–Uma–Karthik Raja (2022), Theorem 3; no originality is credited to that scalar or witness. The full fair-domination all-set criterion and exact polynomial with central-trinomial count are not in the inspected 2022 theorem or in Caro et al. or Alikhani–Safazadeh. The published Resultary fair-polynomial formula for complete multipartite graphs does not cover crown graphs, since deleting a perfect matching destroys complete multipartiteness. This accepted remainder is the classification and enumerator, not rediscovery of fd=2.

## value

PASS

A complete fair-domination polynomial and exact total number of valid sets for the standard crown family encode substantially more than the known minimum parameter. The index-dependent matching deletion produces structurally novel cardinality coefficients and a natural central-trinomial closed form useful for counting fair dominating sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
