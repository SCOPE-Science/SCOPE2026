# Scientific review

## Correctness — PASS

For every \(n\ge5\), a selected edge family of \(K_n\) fails to dominate \(K(n,2)\) exactly when it is a subset of one of the \(\binom n2\) sets \(F_e\) of size \(2n-4\). Two intersecting witnesses overlap in \(n-2\) allowable selected edges; two disjoint witnesses overlap in exactly four cross-edges; no third witness contains those four. Families of at least three witnesses with nonempty intersections at cardinality at least four must form stars, whose intersections have size \(n-1-j\). Inclusion-exclusion and a binomial identity give the complete coefficient formula. The three-edge classification and the exceptional \(K(4,2)=3K_2\) boundary are addressed separately. Direct adjacency-based testing agrees for all 2,131,008 subsets across \(n=4,5,6,7\), and for 1,950,012 cardinality-restricted candidates across \(n=8,9,10\). These computations corroborate, rather than establish, the general proof.

## Originality — PASS, qualified by publication-priority risks

The same-object primary sources were compared at the statement level. Cornet–Torres, arXiv:2308.15603 (first posted 2023-08-29), gives an incidence characterization of \(k\)-tuple domination on \(K(n,2)\), and specializes to a test for ordinary domination; it neither states the uniform coefficient formula nor evaluates the higher witness intersections required for it. Brešar–Cornet–Dravec–Henning, arXiv:2312.15464 (2023-12-24), treats scalar domination and packing variants, not an all-cardinality distribution. Akbari–Alikhani–Peng, arXiv:0905.3281 (2009-05-20), explicitly proves the Petersen domination polynomial; the \(n=5\) specialization is credited, not presented as a discovery. Other indexed and research-record searches found no stronger covering distribution. An unindexed or differently described enumeration could still exist, so global priority is not certified.

## Mathematical value — PASS

The result determines the complete domination polynomial of an infinite natural Kneser-graph family beyond its previously published Petersen member. The nontrivial four-edge correction reflects a genuine overlap between disjoint failure witnesses and is not contained in the ordinary minimum-domination number. The sharp universal cardinality threshold and exact boundary multiplicity supply useful structural information about robust selections, in addition to every coefficient.

## Limitations

No claim is made about higher-uniformity Kneser graphs, distinct domination variants, or worldwide uniqueness. The finite tests are not infinite proof. The accessible scientific literature establishes known special cases and contextual inequalities, not independent audit or publication priority.

Self-review: passed. Independent audit: not yet performed.
