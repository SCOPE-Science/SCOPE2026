# Scientific review

## Correctness — PASS

The three auxiliary denominations \(1,b+1,b^2+b+1\) have a proved optimal greedy coin count: count-reducing or count-preserving replacements terminate at the unique greedy normal form. The resulting Apéry formula \(W(t)=aL(t)+((b-1)a+1)t\) is proved from strict monotonicity, rather than guessed from a finite table. A quantified one-step maximality criterion derives all possible Apéry-maximal indices in the last denomination-sized slab. Three residue cases yield the stated pseudo-Frobenius differences. The independent exact-integer Dijkstra checker confirms all Apéry representatives and pseudo-Frobenius values in 330 generic and 31 repunit instances. The checker is a cross-check; the infinite claim depends on the symbolic proof.

## Originality — PASS within inspected evidence

The closest primary work is Liu--Xin--Ye--Yin, arXiv:2306.03459, whose Theorem 2.10 covers the greedy Apéry calculation for this generator family and whose Theorem 3.4 **already establishes** the divisible \(a\equiv0\pmod{b^2+b+1}\) type-two case. It does **not** give the two nondivisible terminal-slab classifications \(a\equiv1\) and \(a\equiv b+1\), with their types 3 and 2 and sharply different pseudo-Frobenius gaps. Their shorter note arXiv:2306.10738 calculates the Frobenius number and genus without these two classifications. Branco--Colaço--Ojeda classify pseudo-Frobenius sets for the full \(n\)-generator semigroup, not the four-term truncation for \(n\ge5\). Komatsu studies generalized representation-count Frobenius invariants, not the specified pseudo-Frobenius order spectrum. Published-paper and indexed research-record searches found no equivalent cross-parameter statement. Residual risk: an equivalent specialization may be unindexed or derivable from a more general greedy-Apéry theorem; a relevant two-base generalized-repunit chapter was accessible only at abstract level.

## Mathematical value — PASS

The type of a naturally truncated repunit numerical semigroup switches sharply between 2 and 3 according to the length modulo three. More surprisingly, its pseudo-Frobenius points are consecutive in two classes but can be separated by the unbounded explicit quantity \(R_{n+2}+1\) in the third. This addresses the natural invariant explicitly studied in the motivating literature, distinguishes truncations from full repunit semigroups, and supplies a complete classification rather than an arbitrary finite table or routine numerical improvement.

## Limits and literature risks

The Frobenius-number formula and the divisible case are prior results, not independent novelty. The proof covers only four consecutive ordinary repunits with \(n\ge5\). Exact computations support but do not establish universal conclusions. The related generalized two-base triple chapter's full text could not be reviewed, and scholarly literature cannot be claimed exhaustively indexed. There is no independent audit.

Self-review: passed. Independent audit: not yet performed.
