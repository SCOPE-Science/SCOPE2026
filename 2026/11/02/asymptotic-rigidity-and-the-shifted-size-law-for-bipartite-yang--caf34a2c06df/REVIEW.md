# Scientific review: bipartite Yang–Baxter orbit asymptotics

## Correctness — PASS

The exact finite orbit formula and the nonsplit stabilizer interpretation are taken from Militaru's Theorem 2.12, Corollary 2.13, and Proposition 2.15. The proof first brackets orbit counts by multiset counts divided by or not divided by \(m!\), controlling the logarithm to \(O(n\log n)\) in the dominant regime. Strict saddle concavity supplies the \(1/16\) correction and the shift \(n/(4\log n)\). For typical stabilizers, the proof counts fixed tuples of \(S_m\times S_k\): identity-conjugator coordinate cycles give \(O(k^2/m!)\), while all other conjugators are bounded by the minimal nontrivial conjugacy class size \(m(m-1)/2\) and the partition-number bound. Burnside's lemma supplies the relative orbital approximation. Counting nontrivial stabilizers proves asymptotic rigidity, rather than inferring it merely from a large orbit count. The verifier reconstructs all published values through size eight and independently examines five finite saddle points. These finite checks are supplementary, not infinite proofs.

## Originality — PASS, qualified

Militaru (arXiv:2610.30845v1) already proves the exact orbit classification and automorphism formula, which are used as premises, not claimed. His primary paper was inspected across its statement of results and relevant classification and counting sections; it does not state a joint large-size saddle, its \(1/16\) coefficient, or almost-sure rigidity over uniformly sampled isomorphism classes. Kaur–Prajapati–Prasad (arXiv:1905.07957) consider simultaneous conjugacy classes of ordered tuples when the acting finite group is fixed. Sadov (arXiv:1312.6886) studies general asymptotic freeness for permutation actions on subsets and multisets; that contextual theorem is not the joint \(S_m\times S_k\) Yang–Baxter orbit-count asymptotic or its displaced size law. No direct covering implication was identified by the searches and inspected source portions. Residual priority risk: additional results about unlabeled permutation tuples, multiset conjugacy, or effective joint-parameter asymptotics could imply some claims.

## Mathematical value — PASS

The count of an explicitly defined and newly classified natural family changes sharply with the size of its intrinsic permutation block. The theorem determines its second-order logarithmic entropy, a nontrivial order-\(n/\log n\) block displacement, and generic rigidity under the class-uniform measure. The \(1/16\) term and the asymmetry of typical block size are missed by simply fixing balanced block sizes. Such information is useful for understanding the structural and probabilistic geometry of the new classification.

## References and limits

1. G. Militaru, *Bipartite solutions of the set-theoretic Yang–Baxter equation*, arXiv:2610.30845v1 (first posted 22 October 2026). https://arxiv.org/html/2610.30845v1 .
2. D. Kaur, S. K. Prajapati, A. Prasad, *Simultaneous Conjugacy Classes as Combinatorial Invariants of Finite Groups*, arXiv:1905.07957. https://arxiv.org/abs/1905.07957 .
3. S. Sadov, *On asymptotically free action of permutation groups on subsets and multisets*, arXiv:1312.6886. https://arxiv.org/abs/1312.6886 .

Independent historical priority and independent mathematical validation have not been established. The result is specific to bipartite solutions, and the probability is uniform on isomorphism classes rather than on labeled maps.

Self-review: passed. Independent audit: not yet performed.
