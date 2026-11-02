# A tree collision law for additivity of affine modal envelopes

## Finding

Let \(T\) be any finite nonempty rooted tree, equipped with its ancestor order and the Alexandrov topology of upward-closed subsets. For each integer \(k\ge 2\), assign independent, identically distributed atomless random variables \(p_i(v)\in[0,1]\), for \(1\le i\le k\) and vertices \(v\in T\). Let \(L\) denote the lower-semicontinuous envelope. Write \(T_v\) for the descendant subtree rooted at \(v\), \(s_v=|T_v|\), and \(\operatorname{Ch}(v)\) for its set of children.

**Theorem (simultaneous additive-envelope collision law).** The probability that the pointwise modal-envelope additivity equality

\[
L\Bigl(\sum_{i=1}^{k}p_i\Bigr)(v)=\sum_{i=1}^{k}Lp_i(v)
\]

holds at **every** vertex is exactly

\[
\boxed{\displaystyle
\mathbb P\!\left\{\forall v\in T:\ L\Bigl(\sum_{i=1}^k p_i\Bigr)(v)=\sum_{i=1}^k Lp_i(v)\right\}
=\prod_{v\in T}\frac{1+\sum_{c\in\operatorname{Ch}(v)}s_c^k}{s_v^k}.}
\]

The formula is distribution-free over atomless common laws, has no unspecified constants, and includes every finite rooted-tree shape. It also applies componentwise to a rooted forest, with the product taken over all its vertices.

The shape dependence is pronounced. On a rooted star with \(n\ge2\) vertices the probability is \(n^{1-k}\). On a rooted path with \(n\ge1\) vertices it is

\[
\frac{1}{n^k}\prod_{j=1}^{n-1}\left(1+j^{-k}\right)
\sim\frac{C_k}{n^k},\qquad C_k=\prod_{j=1}^{\infty}(1+j^{-k})\in(1,\infty).
\]

For \(k=2\), \(C_2=\sinh(\pi)/\pi\). On a perfect binary tree of height \(h\) and \(n_h=2^{h+1}-1\) vertices, the probability is

\[
\prod_{j=1}^{h}\left(\frac{1+2(2^j-1)^k}{(2^{j+1}-1)^k}\right)^{2^{h-j}}
=\exp\bigl(-[\lambda_k+o(1)]n_h\bigr),
\]

where

\[
\lambda_k=\sum_{j=1}^{\infty}2^{-j-1}\log\left(\frac{(2^{j+1}-1)^k}{1+2(2^j-1)^k}\right)>0.
\]

In particular \(\lambda_2\approx0.490343891765427\). Thus the same semantic equality has polynomial probability on paths and stars but exponentially small probability on full binary trees.

## Assumptions and scope

The topology is **upward** Alexandrov: an open set containing \(v\) must contain all descendants of \(v\). The smallest open neighbourhood of \(v\) is exactly \(T_v\). The variables are independent across both vertices and indices, with one common atomless distribution on \([0,1]\); their rank orders are therefore independent uniform permutations. The integer \(k\) counts distinct atomic terms and may be any integer at least two. The finite tree is fixed, with no distribution imposed on its shape.

The affine modal interpretation used here permits real-valued bounded formula sums, so their range need not remain \([0,1]\). For any bounded \(f:T\to\mathbb R\), the lower-semicontinuous envelope is

\[
Lf(v)=\min_{w\in T_v} f(w).
\]

The event in the theorem requires equality at every vertex simultaneously. It is not a statement about almost-everywhere equality, validity under all possible valuations, arbitrary partial orders, or arbitrary distributions with ties.

## Proof

**1. Envelope reduction.** By the definition of the lower-semicontinuous envelope, \(Lf(v)\) is the supremum, over open neighbourhoods \(U\ni v\), of \(\inf_{w\in U}f(w)\). In the finite upward Alexandrov topology, every such \(U\) contains \(T_v\), so the supremum is precisely the minimum on \(T_v\). Therefore

\[
\min_{w\in T_v}\sum_{i=1}^k p_i(w)\ge \sum_{i=1}^k\min_{w\in T_v}p_i(w).
\]

Equality holds if and only if some single \(w\in T_v\) simultaneously minimizes every \(p_i\) on \(T_v\). Indeed, if equality holds, choose a minimizer of the sum: all its nonnegative individual excesses over the corresponding minima must vanish. The converse is immediate. Atomlessness ensures all individual subtree minima are unique almost surely. Thus the simultaneous envelope-equality event is exactly agreement of the \(k\) **complete subtree-argmin signatures**, one signature recording the unique argmin in \(T_v\) for each \(v\in T\).

**2. A factorization of one random signature.** Fix one index \(i\). At a node \(v\), partition \(T_v\) into disjoint blocks: the singleton \(\{v\}\) and the subtrees \(T_c\) of its children. Let \(J_i(v)\) record the block that contains the minimum of \(p_i\) on \(T_v\). Uniformity of the random rank permutation gives

\[
\mathbb P(J_i(v)=\{v\})=\frac1{s_v},\qquad
\mathbb P(J_i(v)=T_c)=\frac{s_c}{s_v}.
\]

Moreover, the family \(\{J_i(v):v\in T\}\) is mutually independent. A proof that includes the important dependence issue is as follows. Any uniform ordering of a disjoint union of blocks has a unique encoding by (a) a uniformly sampled interleaving of block labels with fixed multiplicities, and (b) independent uniform internal permutations of all blocks. Counting orderings shows that the interleaving is independent of the internal permutations. The first symbol in the interleaving determines \(J_i(v)\), whereas every proper descendant selector depends only on the internal permutation within its child block. Repeating this decomposition recursively proves independence of all node selectors. Selectors for different indices are independent by the independent valuation arrays.

**3. Equivalence of signatures and selectors.** The subtree argmin at a leaf is that leaf. At an internal node \(v\), the full argmin is \(v\) if \(J_i(v)=\{v\}\); otherwise it is the full argmin at the child selected by \(J_i(v)\). Consequently two complete argmin signatures agree everywhere if and only if the corresponding block-selector families agree at every node. The forward direction uses the disjointness of the blocks, and the reverse is induction upwards from the leaves.

**4. Collision product.** For each fixed \(v\), the probability that the \(k\) independent selectors all choose the same block is

\[
\left(\frac1{s_v}\right)^k+
\sum_{c\in\operatorname{Ch}(v)}\left(\frac{s_c}{s_v}\right)^k
=\frac{1+\sum_c s_c^k}{s_v^k}.
\]

The events for different \(v\) are independent by step 2. Multiplying these exact probabilities, and using steps 1 and 3, proves the theorem and the rooted-forest statement.

**5. Natural shapes and limits.** A rooted star has only one nontrivial node-selector factor, namely \(n/n^k=n^{1-k}\). For a chain, each subtree of size \(s\ge2\) has one child subtree of size \(s-1\), so the product telescopes to \(n^{-k}\prod_{j=1}^{n-1}(1+j^{-k})\). The infinite product converges to a finite positive constant because \(k\ge2\); the identity for \(k=2\) follows from Euler's product for the hyperbolic sine. For a perfect binary tree, each of the \(2^{h-j}\) nodes with descendant height \(j\) has two children of size \(2^j-1\), giving the stated exact expression. Dividing minus its logarithm by \(n_h\), applying dominated convergence to the absolutely convergent geometric-weighted series, yields \(\lambda_k\). Each summand is strictly positive for \(j\ge1\) when \(k\ge2\), since \((1+2a)^k>1+2a^k\) for \(a>0\). Therefore \(\lambda_k>0\).

## Verification

The accompanying standalone `checker.py` uses exact rational arithmetic and **no random sampling**. It generates every increasing-labelled rooted tree on \(n=1,\ldots,6\) vertices (a set containing representatives of every unlabelled rooted shape of those sizes), enumerates every permutation of the vertex priorities, and forms the exact distribution of complete subtree-argmin signatures. It then independently computes \(k\)-way collision probabilities from frequencies for each \(k\in\{2,3,4\}\) and compares them to the theorem's product. It tests 462 such shape-and-arity instances. For \(n\le3\), it also enumerates independent rank arrays and directly checks equivalence of the pointwise envelope equality and argmin-signature agreement. Running `python checker.py` reports `ALL_CHECKS_OK`. The exact universal proof is in the preceding section; finite enumeration is not an infinite-case certificate.

## Relationship to prior work

Hafez K. D. and Seyed-Mohammad Bagheri introduced lower-semicontinuous-envelope semantics for affine modal propositions and established, among other foundational inequalities, \(Lf+Lg\le L(f+g)\); their publicly available work motivates asking when that inequality is equal. The theorem here instead gives a distribution-free exact **probability of equality simultaneously at all worlds** for tree-shaped Alexandrov models, including dependence across nested successor sets and shape-specific asymptotics. The original semantics results neither claim nor calculate this probability.

Uniform random permutations and recursive block interleavings are classical. The collision law combines this probabilistic factorization with the modal envelope equality condition. Searches of relevant modal-logic and random-priority-tree terminology did not identify an earlier published exact match. The main residual originality risk is an equivalent collision law in older random tree records, heap priorities, or permutation-signature literature under different terminology; a failed search is not proof of novelty.

## Limitations

There is no claim of a corresponding product for arbitrary finite partial orders: overlapping upper cones generally destroy independent child-block decomposition. Atomic distributions with ties, nonidentical marginals, or dependence across coordinates need not obey the same formula. For \(k=1\), the identity is tautological, and the displayed product specializes to one, but the asymptotic claims involving \(C_k\) are stated only for \(k\ge2\). No extremal assertion across **all** trees of a given order is made. The result concerns a probabilistic semantic refinement of envelope additivity, not a new completeness or decidability theorem. Historical-priority comparison is best-knowledge, not independent certification.

## References

1. Hafez K. D. and Seyed-Mohammad Bagheri, *Affine modal propositional logic*, arXiv:2607.23323, initial public version 25 July 2026, https://arxiv.org/abs/2607.23323 . In particular, Introduction and Sections 1–2 for lower-semicontinuous envelopes and the superadditivity inequality; Sections 3–5 for the different proof-theoretic and compactness objectives.
2. R. Seidel and C. R. Aragon, *Randomized Search Trees*, Algorithmica 16 (1996), 464–497, https://doi.org/10.1007/BF01940876 . Background for independent random priorities and recursive minimum selection; not cited as containing the present equality-probability formula.
3. L. Euler's classical infinite-product identity, \(\sinh(\pi z)/(\pi z)=\prod_{j=1}^{\infty}(1+z^2/j^2)\), used only for the stated path constant at \(k=2\).
