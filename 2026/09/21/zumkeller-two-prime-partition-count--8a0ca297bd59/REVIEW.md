# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked adversarially at the following points.

1. The divisor set of 2^a p is exactly two binary rows, so an equal-sum bipartition is equivalent to a signed equation A+pB=0.
2. Signed sums of 1,2,...,2^a are in bijection with all odd integers in [-(2^(a+1)-1), 2^(a+1)-1]. This follows from the unique binary representation of (M+s)/2 and supplies both existence and uniqueness, not merely a range bound.
3. B is necessarily odd and nonzero. Quotienting ordered partitions by global sign is therefore legitimate: every unordered partition has exactly one orientation with B>0.
4. The floor formula and the interval characterization were rederived directly from the count of positive odd integers r with pr<=M; endpoint inequalities were checked separately.
5. The fixed-k prime count follows exactly from the interval theorem, and the limiting mass follows from the prime number theorem for fixed k.
6. The aggregate identity is a double count of pairs (p,r), and the asymptotic follows from the prime Mertens theorem plus an O(pi(M)) floor error.

A standalone exact computation directly counted equal-sum divisor subsets for 315 pairs (a,p) with 1<=a<=7 and odd prime p<=199. It found zero mismatches with the theorem. A second check verified the aggregate omega identity for 1<=a<=17 with zero mismatches. These computations support but are not used in the proof.

## Originality

The closest located sources were checked for both existence and partition multiplicity.

- Bhaskara Rao--Peng (arXiv:0912.0052; JNT 2013) was inspected in its full arXiv HTML form. It defines Zumkeller partitions, records the known condition for 2^a p to be Zumkeller, and develops structural criteria for np, but no arbitrary partition-count formula was located.
- Mahanta--Saikia--Yaqubi (JNT 2020), especially Theorem 2.6, gives the complete existence criterion for 2^a p^b. The accessible theorem statement and surrounding section were checked; the contribution here strictly refines the b=1 existence statement to multiplicity.
- The current OEIS A083206 entry defines the exact counting function and gives generic subset-sum/coefficient formulas. A083209 explicitly records T. D. Noe's 2010 unique-partition interval for p2^a; that k=1 slice is therefore treated as prior art, not as a new result. A378652 lists the exactly-two values but gives no comparable structural interval in its current entry.
- Exact and synonymous searches for “number of Zumkeller partitions”, “equal-sum divisor partitions”, A083206 together with 2^a p, and arbitrary partition-count formulas did not locate the all-k formula or the distribution results.
- The current SCOPE archive was searched for Zumkeller-related records and no overlapping record was found.

Residual risk: older informal sequence material could contain an equivalent observation that was never indexed in papers. A web page by Reinhard Zumkeller/Peter Luschny advertising finite tables of Zumkeller partitions could not be inspected in full during this check, and the 2008 Clark et al. announcement cited by Rao--Peng was not inspected in full. These are plausible places for early special-case observations, although no located source states the all-k theorem or its distribution consequences.

Originality verdict: PASS, to the best of our knowledge.

## Value

The result upgrades a known yes/no classification to an exact closed-form partition count, completely resolves every fixed multiplicity k in the 2^a p family, and links the aggregate count to the classical additive function omega. The limiting distribution 2/(4k^2-1) gives a concise global description of multiplicities across the prime parameter. This is a substantive quantitative refinement of the established two-prime-support Zumkeller theory.

Value verdict: PASS.
