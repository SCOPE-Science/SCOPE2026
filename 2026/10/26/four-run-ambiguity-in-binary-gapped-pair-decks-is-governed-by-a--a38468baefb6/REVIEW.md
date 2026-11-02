# Independent mathematical audit

## correctness

PASS

Singleton deck counts give t,z; nonadjacent same-symbol pair counts yield g11=C(t,2)−t+r1 and g00=C(z,2)−z+r0, recovering each run count. At fixed composition and run counts all mixed nonadjacent counts follow from q=g01 via g01+g10=tz−(r0+r1−1). For ≤3 runs, a one-parameter block length is uniquely determined by q, excluding all other run counts globally for n≥3; n=2 words 01,10 are properly excepted. For four runs, type A 0^a1^b0^c1^d has q=zt−2−bc and type B 1^a0^b1^c0^d has q=bc−1. Positive constrained lengths yield exact bounded divisor-representation fiber size R_{t,z}(q+1)+R_{t,z}(tz−2−q). Its q-range is the union of a multiplication table S−1 and reflection tz−2−S, giving K=2|S|−#{p∈S:tz−1−p∈S}. Direct exhaustive positional enumeration for binary lengths up to 12 and t,z through 9 independently checked all four-run fibers and first 3 length-six doubletons. Construction t=z=2^k+1, product 2^k, yields k+1 distinct words in one four-run fiber for all k≥1, not a finite extrapolation.

## originality

PASS

Golm et al. arxiv:2201.12671 establish the gapped-k-deck problem and length-six collision threshold, which the audited theorem explicitly credits. A highly relevant additional primary full text, Rigo–Stipulanti–Whiteland, ISIT 2023, has Lemma 2.1 giving a complete alternative general criterion for binary (1,2)-binomial equivalence in terms of usual 2-binomial and 2-abelian equivalence, plus a separate exceptional class. It even explicitly identifies the pair 100110,011001 of the three length-six collisions. This is important stronger general EQUALITY-TEST coverage, not a four-run fiber-size/count classification: the paper studies infinite-word factor complexity, Thue–Morse and Sturmian, and gives no formula R_{t,z}, K_{t,z}, or unbounded fibers at a fixed run count. The four-run factor-product census requires an additional combinatorial derivation. The prior general equivalence criterion significantly reduces the scope of originality and is a serious risk for implicit derivability, but does not in its read claims immediately supply the new exact parameterized invariant. Resultary’s adjacent-pair spectrum record is a different adjacency model.

## value

PASS

A complete exact fiber classification at the first nontrivial run complexity is naturally needed for reconstruction-code design, where ambiguity cardinalities and maximum distinct observed profiles matter, not merely deciding whether a pair is equivalent. The number-theoretic bounded multiplication-table structure and unbounded ambiguity despite fixed four-run complexity are motivated results. Their novelty is specifically the enumerative fiber and packing invariants, not the already-known gap-deck equivalence framework or existence of a length-six collision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
