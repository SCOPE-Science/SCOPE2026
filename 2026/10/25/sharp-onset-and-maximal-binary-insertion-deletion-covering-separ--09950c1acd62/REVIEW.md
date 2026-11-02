# Independent mathematical audit

## correctness

PASS

Every deletion-cover failure at y forces C⊆F_y (y-avoiding family). F_y can be an insertion cover iff no (m+2R)-word forces every length (m+R) subsequence to contain y. Explicit forcing words for all reversal/complement orbits m<=3 and for every length-four pattern except 0110,1001 establish the first separating length. The nontrivial witness z=00(10)^(R+1) for y=0010 has longest avoiding subsequence at most R+3, below R+4; alternating/run witnesses cover remaining orbits. For 0110, Xie–Sun–Ge’s balanced-symbol contradiction shows F_0110 insertion covering; complementation proves F_1001. Greedy completion shows F_y covers every deletion target other than y, hence inclusion maximal and exhausts all maximal counterexamples. Counting greedy prefix advances gives Σ binom(n,j), j<=3. The source proof has correct quantifier directions and carefully distinguishes inclusion maximality from minimum code size. Independently implemented exact finite subsequence DP for R=1..4 and m=1..4, finding exactly the two exceptional patterns at m=4; all-radius assertion is proved by explicit templates, not finite experiments.

## originality

PASS

Xie–Sun–Ge arXiv:2606.15379 Theorem III.2 already establishes the 0110-avoidance family at n=R+4; Remark III.3 extends non-equivalence to all larger n. This prior component is fully credited. The inspected full 14-page primary preprint does not classify implication at R<n<=R+3, exhaust length-four forbidden-pattern orbits, or determine inclusion-maximal counterexample families. The older Lenz–Rashtchian–Siegel–Yaakobi covering-code bounds concern cardinality rather than sharp logical implication. No dominating Resultary record on this claim found. Best-of-knowledge originality PASS for sharp onset and complete max-family classification, not for mere existence.

## value

PASS

For every error radius R the theorem resolves a natural sharp threshold question prompted by a specific published non-equivalence example and completely identifies the maximal obstruction families at the onset; the combinatorial classification is a meaningful infinite-radius structural fact, not an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
