# Scientific review

## Correctness — PASS

The proof uses the exact ternary-digit recursion \(z_{3a}=0\), \(z_{3a+1}=z_a\), \(z_{3a+2}=1\). The unique free residue at every length \(3^k\) reduces the entire arbitrary-offset window count to a single symbol. Equal-length binary Parikh vectors coincide exactly when their numbers of ones coincide; the recursion excludes runs of three equal symbols and gives the explicit adjacent-equality indicator. It proves the 1/3 square density and the 1/2 Parikh-vector frequencies. The finite checker matches the proof in 42,000 windows and 770 indicator tests, without being used as an infinite certificate.

## Originality — PASS (with residual priority risk)

Rao–Rigo–Salimov [1] introduce and analyze the exact fixed point and prove 2-binomial-cube avoidance. This does not imply Abelian-cube avoidance, since 2-binomial equivalence is stricter than Abelian equivalence; their argument does not supply the all-offset window renormalization, the scale-specific Abelian-square density, or the exact adjacent-equality sequence. Cassaigne–Richomme–Saari–Zamboni [2] study broader Abelian-power and bounded-complexity phenomena, not a covering exact comparison identified in its inspected initial discussion. Searches for alternate substitution terminology, fixed-point aliases, Abelian-power lengths and density laws, plus semantically related mathematical records and accessible related claims, did not establish coverage. An unindexed earlier identity remains possible; absence of search hits is not priority proof.

## Value — PASS

A specific infinite word already known to avoid the stronger, 2-binomial kind of cube has an exact and contrasting distribution of weaker Abelian repetitions at every scale of its defining 3-uniform substitution. The theorem completely determines the two Parikh classes, square existence and density, and cube exclusion simultaneously for all starting positions and infinitely many block lengths. The arbitrary-offset renormalization is the motivated structural mechanism; this is not an isolated small enumeration or a routine special case of the published 2-binomial-cube avoidance statement.

## Scientific boundaries

No claim concerns block lengths other than powers of three, and the proof does not establish global Abelian-cube-freeness. The finite computations are corroborative only. Equivalent unpublished or differently named previous analyses are the main historical-priority risk. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
