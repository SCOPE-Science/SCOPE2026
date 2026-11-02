# Universal finite partition supports: exact orbit-refinement criterion and sharp block capacity

## Finding

Let \(A\) be a finite nonempty set of \(N\) distinguishable atoms, and let \(k\geq2\). Call a partition \(R\) of \(A\) **\(k\)-orbit-universal** if for *every* partition \(Q\) of \(A\) into at most \(k\) nonempty blocks there is a permutation \(\pi\in\operatorname{Sym}(A)\) such that \(R\) refines \(\pi Q\). The same \(R\) must work for all \(Q\), although \(\pi\) can depend on \(Q\).

**Criterion.** Suppose \(R\) has \(b\geq1\) nonempty blocks with ordered sizes \(1\leq a_1\leq\cdots\leq a_b\), and set \(S_0=0\) and \(S_j=\sum_{i=1}^j a_i\). Then

\[
R\text{ is }k\text{-orbit-universal}
\quad\Longleftrightarrow\quad
(k-1)(a_j-1)\leq S_{j-1}\quad(1\leq j\leq b).
\]

**Exact capacity and cost.** For \(b\geq0\) set \(G_k(0)=0\) and

\[
G_k(b+1)=G_k(b)+1+\left\lfloor\frac{G_k(b)}{k-1}\right\rfloor.
\]

Among all \(k\)-orbit-universal partitions with exactly \(b\) blocks, the greatest possible number of atoms is exactly \(G_k(b)\) (for \(b=0\), the statement is understood for the empty ground set only). For each \(N\geq1\), the minimum number of nonempty blocks in such a partition of an \(N\)-element set is exactly

\[
\min\{b\geq1:G_k(b)\geq N\}.
\]

These bounds are attained constructively. In particular, \(G_2(b)=2^b-1\); for \(k=3\), the values for \(b=1,2,3,4,5,6,7\) are \(1,2,4,7,11,17,26\). Thus universal support for all three-block target partitions of a seventeen-atom set needs exactly six blocks; one optimum size sequence is \((1,1,2,3,4,6)\).

## Assumptions and scope

All sets, partitions and permutations are finite and classical. A partition means pairwise disjoint *nonempty* subsets with union \(A\). The target quantifier permits any number of blocks from one to \(\min(k,N)\); it is not restricted to exactly \(k\). Refinement means every block of the left partition is included in a block of the right. The theorem counts only the number of **support blocks**, not the number of labelled orbit representatives, permutations, or elements of an infinite permutation model. No assertion concerning an axiom of choice in an infinite Fraenkel–Mostowski model is made.

## Proof

**Step 1 (orbit profiles versus allocations).** A permutation can carry any partition of \(A\) to any other partition with the same multiset of block sizes: choose a bijection between corresponding finite blocks. Thus \(R\) refines a conjugate of \(Q\) exactly when the blocks of \(R\) can be grouped into collections whose union sizes equal the block-size multiset of \(Q\). By permitting empty bins, the required property is equivalent to this *strong* integer statement: for every weak composition \((t_1,\ldots,t_k)\) of \(N\), there is a map \(f:\{1,\ldots,b\}\to\{1,\ldots,k\}\) with

\[
t_c=\sum_{j:f(j)=c}a_j\qquad(1\leq c\leq k).
\]

**Step 2 (sufficiency).** A more general induction works for a positive weight sequence in any given order. Assume its first \(j-1\) terms, of total \(S\), realize every weak \(k\)-composition of \(S\), and that the next term \(a\) satisfies \((k-1)(a-1)\leq S\). Any weak composition of \(S+a\) has a coordinate \(t_c\geq a\): otherwise each coordinate is at most \(a-1\), yielding \(S+a\leq k(a-1)\), while the assumed inequality yields \(S+a\geq k(a-1)+1\), a contradiction. Subtract \(a\) from that coordinate; the remaining nonnegative target coordinates sum to \(S\) and are supplied by the earlier terms. Put the new weight in coordinate \(c\). This proves induction starting with \(S=0\); the criterion implies \(a_1=1\) and therefore yields universality.

**Step 3 (necessity).** Assume that for some index \(j\) in the nondecreasing ordering,

\[
S=\sum_{i<j}a_i<(k-1)(a_j-1),\qquad a=a_j.
\]

All later weights are at least \(a\). Put \(N=\sum_i a_i\). If \(N\leq k(a-1)\), write \(N\) as a sum of at most \(k\) positive integers each at most \(a-1\), possible since \(a\geq2\); this target contains no place for any weight numbered \(j\) or later. If \(N>k(a-1)\), consider the weak composition with its first \(k-1\) entries equal to \(a-1\) and last entry \(N-(k-1)(a-1)\). Every weight numbered \(j\) or later must go in the last bin. Their total is \(N-S>N-(k-1)(a-1)\), impossible. Both cases contradict universality. All hypotheses and boundary cases are covered.

**Step 4 (optimal capacity).** By the criterion and sorted order, any \(k\)-universal \(b\)-block partition has

\[
a_j\leq1+\left\lfloor\frac{S_{j-1}}{k-1}\right\rfloor.
\]

As the right side is nondecreasing in its argument, induction against the recurrence gives \(S_j\leq G_k(j)\), hence \(N\leq G_k(b)\). Conversely, select the successive greedy weights \(a_j=1+\lfloor G_k(j-1)/(k-1)\rfloor\), which are nondecreasing, satisfy the criterion with equality up to the floor, and sum to \(G_k(b)\). Therefore the capacity is attained.

**Step 5 (all intermediate atom counts).** Let \(b\) be the least index with \(G_k(b)\geq N\). Thus \(G_k(b-1)<N\leq G_k(b)\). Take the first \(b-1\) greedy weights, whose sum is \(G_k(b-1)\), and append the positive weight \(a=N-G_k(b-1)\). Since \(a\leq 1+\lfloor G_k(b-1)/(k-1)\rfloor\), the *order-independent sufficiency induction of Step 2* applies to this sequence, even if its final term is smaller than preceding terms. It realizes every weak \(k\)-composition of \(N\), and therefore is an optimum \(b\)-block support. For \(k=2\), the capacity recurrence doubles the previous capacity and adds one, giving the closed formula. The displayed \(k=3\) values follow by integer recurrence. \(\square\)

## Verification

The independent direct-search script `checker.py` exhaustively enumerates every unordered positive-integer partition of each \(N\in\{1,\ldots,17\}\). For each \(k\in\{2,3,4,5\}\), it tests *all* target integer partitions having at most \(k\) parts by recursively allocating the indivisible support weights, and independently compares the outcome against the local prefix inequality. It checks \(4{,}844\) weight-multiset instances. It additionally evaluates greedy constructions for \(2\leq k\leq6\). The executable result is:

`ALL_CHECKS_OK compared_weight_multisets=4844 k_ranges=2..5 n_ranges=1..17`

To replay, run `python3 checker.py`. These finite checks are consistency tests, not a proof of the theorem for arbitrary \(N,k,b\). The complete arbitrary-parameter proof is in Steps 1–5.

## Relationship to prior work

Venkataramani's *Choice principles in countable partition models* (2026), §6, Lemmas 6.2–6.3 and Corollary 6.4, establishes the permutation/profile correspondence and constructs countable refinements universal under suitable conjugations in infinite atom sets; those results motivate the finite support-budget question. They do **not** state the present all-finite-sizes prefix equivalence or optimal block-capacity recurrence. Bruce's earlier paper introduces finite partitions as supports in the countably infinite atom setting, and Banerjee studies weak choice in related partition models. Their infinite-model conclusions are not attributed to the finite theorem.

For \(k=2\), the numerical prefix condition coincides with the classical complete subset-sum sequence criterion. This is not a claim of novelty for the binary case. The content under consideration is the all-\(k\) orbit-refinement classification together with exact finite resource optimization. Similarities to multi-bin integer partitioning are reductions, not evidence of priority; see the limitations.

## Limitations

The theorem concerns a *finite ground set* and a *single target-block budget* \(k\). It supplies no finite-budget substitute for infinite-cardinality, infinite-partition, or dependent-choice assertions. The all-\(k\) numerical criterion and recurrence have not received independent scholarly priority review; older multiway complete-sequence or universal-coarsening literature could contain an equivalent statement. Search nonmatches do not establish uniqueness. Verification of computational instances is bounded by the sizes stated above.

## References

1. Brinda Venkataramani, *Choice principles in countable partition models*, arXiv:2610.29752v1, first submitted 2026-10-21, especially §6, Lemmas 6.2–6.3, Corollary 6.4. https://arxiv.org/html/2610.29752v1
2. Benjamin Bruce, *A Permutation Model with Finite Partitions of the Set of Atoms as Supports*, preprint dated 2014-07-25, published in Rose-Hulman Undergraduate Mathematics Journal 17 (2016), no. 1, art. 4. https://lsa.umich.edu/content/dam/math-assets/math-document/reu-documents/Bruce_Ben%20REU%202014.pdf
3. Amitayu Banerjee, *Partition models, Permutations of infinite sets without fixed points, and weak forms of AC*, arXiv:2109.05914, first submitted 2021-09-13. https://arxiv.org/abs/2109.05914
