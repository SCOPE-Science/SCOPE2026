# Review

## Correctness
PASS. With \(A_B=\sum_{i\in B}(d_i-2)\), the recent bound is \(U(B)=2^{|B|-1}(A_B+2)\), including singletons because \(U(\{i\})=d_i\). For disjoint nonempty \(I,J\), direct expansion gives
\[
U(I)U(J)-U(I\cup J)=2^{|I|+|J|-2}A_IA_J>0.
\]
Iterating this strict two-block merge proves the statement for every nontrivial partition. The only non-elementary premise is the published decomposition bound itself.

## Originality
PASS. The initiating paper states the improved bound and construction, but the inspected full text does not state the exact merge-saving identity or arbitrary-partition dominance. The 2019 predecessor gives a weaker all-degree bound and a sharper special cubic bound; the 2021 strict-submultiplicativity paper gives geometric criteria and examples; Gałązka covers the two-factor estimate. Targeted searches of published findings found no implication-equivalent all-degree partition statement.

Residual risk remains that the elementary identity was noted informally or in an unindexed source.

## Value
PASS. A basic way to exploit tensor-rank submultiplicativity is to decompose blocks separately and tensor the decompositions. The result proves that the new all-factor construction has a genuine, quantified many-factor advantage over every such recursive use of the same bound. The exact merge saving identifies where that advantage comes from and is reusable for comparing decomposition strategies.

## Closest literature and limitations
The closest source is arXiv:2512.05828v1, which supplies the bound being compared. arXiv:1803.01623v2 supplies the preceding general W-state bounds, and arXiv:1909.03811v2 supplies broader geometric context for strict submultiplicativity. The statement concerns certified upper-bound lengths only; it neither computes exact nonsingleton ranks nor proves global optimality among all possible decompositions.

Self-review: passed. Independent audit: not yet performed.
