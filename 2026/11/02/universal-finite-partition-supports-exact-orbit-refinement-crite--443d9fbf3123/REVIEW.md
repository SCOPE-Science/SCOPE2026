# Self-review

## Correctness — PASS

The orbit-profile reduction is exact for finite sets: two partitions with equal block-size multisets are conjugate under their full symmetric group. The proof verifies both implications of the prefix inequality, including the two exhaustive cases of the obstruction construction. The sufficiency argument works in any prefix order and is used explicitly for truncated greediness at intermediate ground-set sizes. Integer monotonicity gives the universal capacity upper bound, and greediness attains it. All quantifiers require a finite nonempty set, a positive number of support blocks, and a target budget of at least two. The standalone exhaustive checker agreed with the criterion on 4,844 support-multiset instances and supports the proof only finitely.

## Originality — PASS within assessed evidence

The closest full primary source, Venkataramani (2026), §6, Lemma 6.3 and Corollary 6.4, gives a countably infinite refinement existence construction for specified infinite atom/cardinality profiles; it does not calculate any sharp minimum number of finite support blocks. Bruce (2014/2016) constructs an infinite-atom finite-partition-support model, and Banerjee (2021) addresses weak choice. The binary complete-sequence special case and the ability to use singleton supports are not new contributions. Searches of related universal-coarsening, multibin subset-sum, and indexed mathematical results did not disclose the full \(k\)-parameter criterion or sharp recurrence. Absence from results is not mathematical proof of originality; older combinatorial folklore and terminology changes are residual priority risks. No independence or external validation is implied.

## Value — PASS

The theorem fully identifies, for every target-budget parameter, which fixed finite supports can refine every conjugacy class of bounded target partitions. Unlike the qualitative infinite-atom existence theorem, it computes exactly how many finite support blocks suffice and are necessary, with explicit optimal constructions; at \(N=17\), \(k=3\), the minimum is six blocks. This is a natural representation-resource question whose precise invariant depends on the intended support/refinement operation, not an arbitrary finite slice or a known-table recomputation. The binary criterion alone would not support a new claim.

## Closest literature and limitations

The direct motivation and strongest accessible nearby comparison is Venkataramani, arXiv:2610.29752v1, complete relevant §6 and supporting definitions, https://arxiv.org/html/2610.29752v1. Bruce's freely accessible 2014 preprint was inspected at the support definitions and finite-partition-model arguments. Banerjee's arXiv record and published abstract were read; the entire Banerjee paper could not be inspected through its HTML endpoint in this check. A prior exact \(k\)-way complete-weight theorem under a different name remains possible. No claim about infinite choice principles, unique first discovery, or formal external certification is made.

Self-review: passed. Independent audit: not yet performed.
