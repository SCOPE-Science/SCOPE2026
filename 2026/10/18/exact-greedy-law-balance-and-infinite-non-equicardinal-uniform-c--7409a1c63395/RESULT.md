# Exact greedy-law balance and infinite non-equicardinal uniform clique bouquets

## Finding

Fix an integer \(r\ge1\) and integers \(m_i\ge1\) for \(1\le i\le r\). Let \(G\) be the *clique bouquet*
\[
G=K_1\vee\left(\bigsqcup_{i=1}^r K_{m_i}\right),\quad M=\sum_{i=1}^r m_i,\quad P=\prod_{i=1}^r m_i.
\]
The unique new universal vertex is called the hub. The random greedy process scans a uniformly random permutation of all \(M+1\) vertices, accepting a vertex if it has no previously accepted neighbour. Define \(\mathcal{M}(G)\) to be the family of inclusion-maximal independent sets, and \(b(G)\) to be the total-variation distance between the output law and the uniform law on \(\mathcal{M}(G)\).

**Theorem.** The complete greedy output distribution is
\[
\Pr(I=\{h\})=\frac1{M+1},\qquad
\Pr(I=\{v_1,\ldots,v_r\})=\frac{M}{(M+1)P}\quad (v_i\in K_{m_i}).
\]
These are all \(P+1\) maximal independent sets. Consequently,
\[
\boxed{\ b(G)=\frac{|P-M|}{(M+1)(P+1)}\ },
\qquad
\boxed{\ b(G)=0\iff P=M\ }.
\]
In particular, for every integer \(q\ge2\), the connected graph
\[
G_q=K_1\vee\left(K_2\sqcup K_q\sqcup(q-2)K_1\right)
\]
has \(2q+1\) maximal independent sets, all sampled with probability \(1/(2q+1)\), despite one set having cardinality one and every other set having cardinality \(q\). This supplies arbitrarily large gaps between cardinalities of exactly equidistributed maximal independent sets.

## Assumptions and scope

Graphs are finite, simple and undirected. The notation \(\sqcup\) denotes disjoint union, and \(\vee\) denotes graph join. Clique blocks are nonempty and labeled, but vertices within blocks are individually distinguished when counting output sets. A vertex order is sampled uniformly among all \((M+1)!\) permutations. The result holds for arbitrary positive blade sizes, including single-vertex blades and the case \(r=1\). The uniform comparison measure assigns mass \(1/(P+1)\) to each labeled inclusion-maximal independent set.

## Proof

**Classification of maximal sets.** Any independent set containing the hub is exactly the hub singleton. If it omits the hub, maximality requires that it meet every clique block (otherwise any vertex of a missed block can be added). Independence allows at most one vertex from each block. Thus such a maximal set contains precisely one vertex per block, giving exactly \(P\) transversals.

**Probability law.** If the hub is first in the random permutation, the algorithm accepts it and rejects every other vertex. This event has probability \(1/(M+1)\). Otherwise the first vertex is on the rim, blocks the hub, and the algorithm eventually accepts exactly the first vertex in the permutation from each clique block. This event has probability \(M/(M+1)\). The conditional law of the tuple of within-block first vertices is uniform on the \(P\) tuples: permutations of labels inside each clique act transitively on these tuples, preserving the uniform permutation measure and the condition that the hub is not first. Therefore each transversal has probability \(M/((M+1)P)\).

**Total variation.** The difference between the hub mass and its uniform mass is
\[
\frac1{M+1}-\frac1{P+1}=\frac{P-M}{(M+1)(P+1)}.
\]
All \(P\) transversal masses differ from their uniform masses with the opposite sign, and their signed differences sum to minus the hub difference because both distributions have total mass one. Hence half the total absolute difference is the absolute hub difference. This proves the displayed formula. Exact equality of the laws is equivalent to \(P=M\), including \(r=1\), for which both equal \(m_1\).

**Unbounded unequal-cardinality family.** For \(q\ge2\), choose two clique sizes \(2\) and \(q\) and append \(q-2\) singleton clique blocks. Their product and sum both equal \(2q\). The classification yields one maximal set of size one and \(2q\) maximal sets of size \(2+(q-2)=q\). The uniformity criterion gives exactly \(1/(2q+1)\) for each, as claimed. No limiting argument or independence assumption between globally sampled block minima is needed; the symmetry argument supplies the precise conditional joint law.

## Verification

The companion standalone `verify.py` constructs each graph from its clique-block sizes, enumerates every vertex permutation, executes the greedy algorithm literally, and compares the resulting exact integer frequencies with the formulas above. It also checks the exact rational total-variation value and the uniformity criterion. Tested cases include two triangles sharing one vertex (\((2,2)\)), the nonregular seven-vertex exactly uniform example (\((1,2,3)\)), nonuniform examples, and one-block boundary cases. These finite computations check the implementation and boundary cases only; the proof above establishes all positive integer parameters.

## Relationship to prior work

Fairfax-Ball (2026, arXiv:2610.02276v1) establishes that the vertex-order greedy maximal-independent-set law is uniform on a tree only for the one-vertex tree and the single edge. That tree-only obstruction does not cover the cyclic clique bouquets here. Kryven, Versendaal and de Vries (2026, arXiv:2608.07239v1) study the same independent-set sampling model and stronger 2-uniformity conditions for other combinatorial constructions. Krivelevich et al. (2023/2024) study the random greedy maximal-independent-set process and its limiting density. The process itself, the first-vertex conditioning method, and standard greedy recursions are established tools, not novel claims.

Existing mathematical records concerning exact greedy laws of threshold graphs or chain graphs concern distinct classes: a clique bouquet containing two rim clique blocks of order at least two has an induced \(2K_2\), so it is not a threshold graph, and contains triangles, so it is not a chain graph. Results on generalized windmill dissociation sets count a different invariant. The contribution here is the exact equality criterion for the vertex-order *greedy law* on arbitrary clique bouquets and the unbounded-gap uniform family.

## Limitations

This is a specialized structural calculation, not a classification of all finite graphs with exactly uniform random greedy maximal-independent-set laws. The proof yields no asymptotic density claim for arbitrary graph families. An equivalent formula could exist under different sampling or block-graph terminology; priority remains subject to fuller bibliographic checking, and independent mathematical review has not been performed. Finite enumeration is not used as an infinite proof.

## References

1. J. Fairfax-Ball, *Greedy Uniformity on Trees: Exact Obstruction and Near-Uniform Spiders*, arXiv:2610.02276v1 (first available 2026-10-01), https://arxiv.org/abs/2610.02276.
2. I. Kryven, R. Versendaal, M. de Vries, *Unified framework for asymptotically uniform iterative construction of generalised random graphs with local constraints*, arXiv:2608.07239v1 (2026), https://arxiv.org/abs/2608.07239.
3. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, *Random Structures & Algorithms* 64 (2024), 986–1015; first online 2023-12-18, https://doi.org/10.1002/rsa.21200.
