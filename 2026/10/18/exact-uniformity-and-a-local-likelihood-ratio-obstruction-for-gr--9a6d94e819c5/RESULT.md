# Exact uniformity and a local likelihood-ratio obstruction for greedy independent sets on cycles

## Finding

Let \(C_n\) be the simple cycle on \(n\ge3\) labeled vertices. Process its vertices in uniformly random order, accepting a vertex if and only if none of its already accepted neighbors is adjacent to it. Write \(\mathcal M(C_n)\) for all inclusion-maximal independent sets and \(\mathbb P_n(I)\) for the probability that the output is \(I\).

**Theorem.** The law \(\mathbb P_n\) is uniform on \(\mathcal M(C_n)\) if and only if
\[
 n\in\{3,4,5,7\}.
\]
More quantitatively, whenever \(n=6\) or \(n\ge8\), there are two maximal independent sets \(I_{222}\) and \(I_{33}\), differing only on an arc of six edges, for which
\[
 \mathbb P_n(I_{222})\ \ge\ 2\,\mathbb P_n(I_{33})\ >\ 0.
\]
Along the arc, the successive distances between selected vertices are respectively \((2,2,2)\) and \((3,3)\); the selected vertices at both ends of the arc, and all selections outside it, coincide. When \(n=6\), the two endpoints refer to the same vertex.

## Assumptions and scope

The graph is a finite, simple, undirected labeled cycle with \(n\ge3\); arrival order is uniformly random among all \(n!\) permutations. The output is an *inclusion-maximal*, not necessarily maximum-cardinality, independent set. Probabilities refer to a fixed labeled output set, not to an orbit or to the distribution of output size. All inequalities concern exact probabilities, not asymptotic estimates.

A maximal independent set of a cycle is precisely a cyclic word whose consecutive selected vertices are separated by distances \(2\) or \(3\). Indeed independence makes every distance at least two; maximality rules out three consecutive unselected vertices, making every distance at most three. Such cyclic compositions may be used as complete descriptions of outputs.

## Proof

**1. The conditional factorization.** Give every vertex an independent uniform arrival mark in \([0,1]\), scanned in increasing order. Fix a maximal independent set \(I\). The greedy output equals \(I\) if and only if each vertex \(w\notin I\) has an earlier neighbor belonging to \(I\). Necessity follows from the rejected vertices. For sufficiency, the first vertex outside \(I\) that would be accepted has an earlier neighbor in \(I\); that neighbor cannot have been rejected by an earlier accepted vertex outside \(I\), contradicting the choice of the first such vertex.

Condition on the marks \(s_1,\ldots,s_k\) of the cyclically ordered vertices of \(I\). A distance-two gap contains one unselected vertex; it is rejected exactly when its arrival mark is later than at least one endpoint mark, with conditional probability
\[
 A(s,t)=1-\min(s,t).
\]
A distance-three gap contains two unselected vertices, each having exactly one selected neighbor; both must arrive after their respective selected neighbors, with conditional probability
\[
 B(s,t)=(1-s)(1-t).
\]
The unselected marks in distinct gaps are independent. If the successive gap lengths are \(d_1,\ldots,d_k\in\{2,3\}\), the exact finite-dimensional integral is therefore
\[
 \mathbb P_n(I)=\int_{[0,1]^k}\prod_{i=1}^{k}F_{d_i}(s_i,s_{i+1})\,ds_1\cdots ds_k,
 \qquad s_{k+1}=s_1,\quad F_2=A,\quad F_3=B.
\]
This identity also proves that every maximal independent set has positive probability.

**2. A strict six-edge replacement.** Fix arrival marks \(s,t\in[0,1]\) at the two selected endpoints of a six-edge arc. For three successive distance-two gaps, the two internal selected vertices have independent marks \(X,Y\sim\operatorname{Unif}[0,1]\). After integrating their marks, the arc contributes
\[
 G(s,t)=\int_0^1\int_0^1
  (1-\min(s,x))(1-\min(x,y))(1-\min(y,t))\,dx\,dy.
\]
For two successive distance-three gaps, the one internal selected vertex has mark \(Z\sim\operatorname{Unif}[0,1]\), so the contribution is
\[
 H(s,t)=\int_0^1(1-s)(1-z)^2(1-t)\,dz
 =\frac{(1-s)(1-t)}{3}.
\]
For all \(u,v\in[0,1]\), \(1-\min(u,v)\ge1-u\). Consequently,
\[
 G(s,t)\ge(1-s)(1-t)
 \int_0^1\int_0^1(1-\min(x,y))\,dx\,dy
 =\frac{2(1-s)(1-t)}{3}=2H(s,t),
\]
using \(\mathbb E\min(X,Y)=1/3\). The same calculation holds with \(t=s\) when the arc closes into a six-cycle.

Choose any common completion of the arc to a cycle by distance-two or distance-three gaps. Conditional on the endpoint marks and all selected marks of that common exterior, the exterior contributes the *same nonnegative factor* in the two target probabilities. Integrating the remaining marks and applying \(G\ge2H\) proves \(\mathbb P_n(I_{222})\ge2\mathbb P_n(I_{33})\). The latter probability is strictly positive by the integral representation, so the two probabilities are unequal.

**3. Existence of a completion.** For \(n=6\), the six-edge arc closes at its starting vertex and needs no exterior. For every \(n\ge8\), write \(n-6\) as a sum of integers \(2\) and \(3\). This is possible for every integer at least two: use all twos when even, or one three followed by twos when odd. The corresponding outside gaps give the common completion. The only \(n\ge6\) excluded by this construction is \(n=7\). Thus the greedy law is nonuniform for \(n=6\) and all \(n\ge8\).

**4. The remaining cycles.** Every maximal independent set of \(C_3,C_4,C_5,C_7\) lies in a single cyclic-rotation orbit: the respective possible cyclic gap patterns are \((3)\), \((2,2)\), \((2,3)\), and \((2,2,3)\), where entries may be cyclically permuted. Since the random greedy procedure is invariant under graph rotations and acts transitively on these sets, their output probabilities are equal. This finishes the classification. \(\square\)

## Verification

The accompanying standard-library program `verify_cycle_greedy.py` computes the *entire* exact rational output law for every \(3\le n\le15\), using a first-accepted-vertex recursion and independently enumerating all \(46{,}230\) permutations over the sizes \(3\le n\le8\). It checks support against independently enumerated maximal independent sets, verifies exactly the four uniform sizes, and checks the factor-two inequality for every tested admissible size. The general theorem follows from the analytic argument above; these finite tests do not establish the all-\(n\) claim on their own.

Run with `python verify_cycle_greedy.py` (Python 3.9 or newer); no external dependencies, network, or random seeds are needed.

## Relationship to prior work

The random-order greedy maximal-independent-set process, its priority-mark representation, and first-choice recurrence are classical. Fairfax-Ball, *Greedy Uniformity on Trees: Exact Obstruction and Near-Uniform Spiders* (2026), classifies exact uniformity **on trees** and studies near-uniformity in a spider family; it does not give a cycle classification. Krivelevich, Mészáros, Michaeli and Shikhelman (2023/2024) analyze greedy independent-set densities and local limits, rather than the equality of individual terminal-set probabilities on cycles. Kryven, Versendaal and de Vries (2026) investigate sufficient/structural uniformity notions in an iterative-graph-sampling framework; the available abstract and the cited comparison in the 2026 tree work do not establish the cycle theorem. The simple classification of well-covered cycles alone does not compare random-greedy permutation fibres. The contribution here is the all-cycle exact classification with a pointwise six-edge likelihood-ratio witness.

## Limitations

Only simple cycles and the uniform random-order greedy rule are addressed. No analogous classification is claimed for arbitrary unicyclic, regular, or vertex-transitive graphs. The result gives a ratio witness for selected pairs, not the full probability distribution or a uniform-in-\(n\) total-variation lower bound. A related source on iterative uniform sampling was available only at the abstract/secondary-discussion level, leaving possible unindexed overlap; no independent audit has been performed.

## References

1. J. Fairfax-Ball, *Greedy Uniformity on Trees: Exact Obstruction and Near-Uniform Spiders*, arXiv:2610.02276v1, submitted 1 October 2026. https://arxiv.org/abs/2610.02276
2. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, *Random Structures & Algorithms* 64 (2024), 986–1015, first online 18 December 2023. https://doi.org/10.1002/rsa.21200
3. I. Kryven, R. Versendaal and M. de Vries, *Unified framework for asymptotically uniform iterative construction of generalised random graphs with local constraints*, arXiv:2608.07239v1 (2026). https://arxiv.org/abs/2608.07239
