# Poisson threshold hierarchy and complete first-order convergence criterion for coloured equivalence blocks

## Finding

Let \(m_n,r_n\to\infty\) be arbitrary positive integer sequences. Form a deterministic finite equivalence structure with exactly \(m_n\) equivalence classes, each of size \(r_n\), and independently put each element into a unary predicate \(P\) with probability \(1/2\). The vocabulary is exactly \(\{E,P\}\), with equality, and has **no order, constants, or class names**. For every fixed integer \(j\geq0\) define
\[
\lambda_{n,j}:=m_n 2^{-r_n}\binom{r_n}{j},\qquad \binom{r_n}{j}=0\ \text{if }j>r_n.
\]

**Complete convergence criterion.** Every first-order \(\{E,P\}\)-sentence has a limiting satisfaction probability if and only if each \(\lambda_{n,j}\) converges in the extended interval \([0,\infty]\). Under this condition, the first-order zero-one law holds if and only if every such limit belongs to \(\{0,\infty\}\).

**Unique nontrivial phase and its logical profile.** At most one index \(j\) can have \(0<\lambda_j:=\lim_n\lambda_{n,j}<\infty\). If it does, the counts of classes containing exactly \(j\) red points, respectively exactly \(j\) blue points, converge jointly to *independent* \(\operatorname{Pois}(\lambda_j)\) variables \(X,Y\). For every first-order sentence \(\varphi\) there is a finite \(q\) and a Boolean decision function \(F_{\varphi}:\{0,\ldots,q\}^2\to\{0,1\}\) such that
\[
\lim_n\Pr(\mathcal A_n\models\varphi)
=\mathbb E\big[F_{\varphi}(\min(X,q),\min(Y,q))\big].
\]
In particular, this value is a finite sum of products of Poisson point and tail probabilities; it need not equal zero or one. If no index has a finite positive limit, every first-order sentence has limiting probability zero or one.

**Sharp natural nonconvergence example.** With \(m_n=n\) and \(r_n=\lceil\log_2 n\rceil\), the uncoloured equivalence-reducts obey a zero-one law, but their independent red/blue expansions have *no* first-order convergence law: the sentence asserting that an entirely blue equivalence class exists has subsequential probabilities \(1-e^{-1}\) and \(1-e^{-1/2}\). Thus, an apparently harmless independent unary expansion can destroy even convergence.

## Assumptions and scope

An \(E\)-class is a block in a partition; \(E\) is reflexive, symmetric, and transitive. The integer \(n\) is only a sequence index. The conditions \(m_n\to\infty\) and \(r_n\to\infty\) are essential. The blocks are deterministically specified, with one fair independent Bernoulli choice for each element; randomizing the labels of the blocks gives the same isomorphism-invariant statement. There are no edges between different classes and no predicates other than \(E,P\). Every sentence and every quantifier rank are fixed *before* the limit. All convergence and zero-one assertions refer to this family of probability spaces, not to uniformly random equivalence relations or expansions with a growing vocabulary.

For \(r_n>2j\), let \(X_{n,j}\) count classes with exactly \(j\) red points, and let \(Y_{n,j}\) count classes with exactly \(j\) blue points. They are distinct class categories. Writing \(p_{n,j}=2^{-r_n}\binom{r_n}{j}\), their exact joint probability generating function is
\[
\mathbb E\big[s^{X_{n,j}}t^{Y_{n,j}}\big]
=\big(1+p_{n,j}(s-1)+p_{n,j}(t-1)\big)^{m_n}.
\]
In particular, for \(u,v\geq0\) with \(u+v\leq m_n\),
\[
\Pr(X_{n,j}=u,Y_{n,j}=v)=\frac{m_n!}{u!v!(m_n-u-v)!}
 p_{n,j}^{u+v}(1-2p_{n,j})^{m_n-u-v}.
\]
This is an *exact finite-size identity*, separate from the logical asymptotic theorem.

## Proof

**1. Complete local classification at a fixed quantifier rank.** Fix an integer \(q\geq1\). For each equivalence class \(C\), record the pair
\[
\tau_q(C)=\big(\min(|C\cap P|,q),\min(|C\setminus P|,q)\big).
\]
For each such pair, count the number of classes carrying it and truncate that count at \(q\). If two finite coloured equivalence structures have equal resulting truncated class-profile vectors, Duplicator wins the \(q\)-round Ehrenfeucht–Fraïssé game. Maintain a partial matching of classes and, inside each matched class, injective colour-preserving maps between selected points. On a move in an already matched class, any previously unseen point of the requested colour can be matched: either the original colour population is less than \(q\) and the two populations are equal, or both populations are at least \(q\), exceeding the number of previously selected points. On a move in a new class, a fresh class with the same \(\tau_q\)-type exists by the truncated class-count agreement (fewer than \(q\) classes have been used). The resulting map preserves equality, \(P\), and \(E\). Thus any rank-at-most-\(q\) sentence is determined by the finite truncated class-profile vector.

**2. Which profiles occur.** For \(r_n\geq2q\), every class has one of the profiles \((j,q)\) and \((q,j)\) for \(0\leq j<q\), or the generic profile \((q,q)\). The count of red-minority classes of type \((j,q)\), and symmetrically blue-minority classes of type \((q,j)\), has mean \(\lambda_{n,j}\). The probability that a class is generic tends to one since for fixed \(q\),
\[
\Pr(\operatorname{Bin}(r_n,1/2)<q\ \text{or}\ >r_n-q)
\leq 2^{1-r_n}\sum_{j<q}\binom{r_n}{j}\longrightarrow0.
\]
Therefore, as \(m_n\to\infty\), the number of generic classes exceeds \(q\) with probability tending to one.

**3. Limits of all truncated counts.** For finitely many disjoint class categories whose means tend to finite values, the multinomial probability generating function is
\[
\Big(1+\sum_i p_{n,i}(s_i-1)\Big)^{m_n}
\longrightarrow\exp\Big(\sum_i\lambda_i(s_i-1)\Big),
\]
so the corresponding counts tend jointly to independent Poisson variables (including degenerate zero means). If the mean of any category tends to infinity, its binomial count exceeds any fixed threshold with probability tending to one, since its variance is at most its mean and Chebyshev's inequality applies. These statements jointly imply convergence in distribution of the complete finite \(q\)-truncated class-profile vector whenever all \(\lambda_{n,j}\), \(j<q\), converge in \([0,\infty]\). By Step 1, this suffices for limiting probabilities of every fixed rank-at-most-\(q\) sentence. Since every first-order sentence has finite rank, convergence of all the means is sufficient.

**4. Necessity of every mean limit.** For every fixed \(j\), the first-order sentence \(\eta_j\) saying that *some equivalence class has exactly \(j\) red elements* exists. For \(j\geq1\), explicitly use \(j\) distinct red witnesses within one \(E\)-class and a universal quantifier saying every red member of that class is one of the witnesses. For \(j=0\), say there is a point whose entire \(E\)-class contains no red point. Its exact satisfaction probability is
\[
\Pr(\eta_j)=1-(1-p_{n,j})^{m_n}.
\]
For fixed \(j\), \(p_{n,j}\to0\). On every subsequence with \(\lambda_{n,j}\to L\in[0,\infty]\), this probability tends to \(1-e^{-L}\), using the convention \(e^{-\infty}=0\). If \(\lambda_{n,j}\) has no extended limit, compactness of the extended interval supplies two subsequences with different limits \(L\), and the strictly increasing function \(L\mapsto1-e^{-L}\) gives two different sentence-probability limits. Hence first-order convergence implies convergence of every \(\lambda_{n,j}\).

**5. Exactly one possible critical profile.** For each fixed \(j\), eventually \(r_n>j\) and
\[
\frac{\lambda_{n,j+1}}{\lambda_{n,j}}=\frac{r_n-j}{j+1}\longrightarrow\infty.
\]
If some \(\lambda_{n,j}\to\lambda\in(0,\infty)\), then all lower-index means tend to zero and all higher-index means tend to infinity. This proves uniqueness and, via Step 3, the two independent Poisson counts at the unique critical index. In every finite-rank class-profile vector all other coordinates tend to deterministic zero or truncated-maximum values; hence its limiting Boolean decision depends only on the two truncated Poisson counts as displayed.

**6. Zero-one characterization.** If no mean has a finite positive limit, all the coordinates in every finite-rank truncated profile converge in probability to deterministic values; therefore every sentence probability tends to zero or one. Conversely, if \(\lambda_{n,j}\to\lambda\in(0,\infty)\), the sentence \(\eta_j\) has probability tending to \(1-e^{-\lambda}\in(0,1)\), contradicting a zero-one law.

**7. Nonconvergence and realizability.** Let \(m_n=n\), \(r_n=\lceil\log_2n\rceil\). Along \(n=2^k\), \(\lambda_{n,0}=1\); along \(n=2^{k-1}+1\), \(\lambda_{n,0}\to1/2\). Step 4 yields the two displayed limits. For any chosen fixed \(j\geq0\) and \(\lambda>0\), choosing integers \(r\to\infty\) and \(m_r=\lfloor\lambda 2^r/\binom rj\rfloor\) realizes \(\lambda_{r,j}\to\lambda\), with \(m_r\to\infty\). Therefore every level of the Poisson hierarchy genuinely occurs. Finally, the uncoloured \(E\)-reducts satisfy a zero-one law by the same \(q\)-round strategy: each has at least \(q\) classes with at least \(q\) elements, eventually, so every such reduct has the same rank-at-most-\(q\) theory. This proves the claimed contrast.

## Verification

The provided `checker.py` enumerates finite fair-colouring assignments for seven choices of class count and class size, comparing 12 exact bivariate count distributions against the multinomial formula using rational arithmetic. It also reconstructs truncated class profiles, directly solves 417 finite two-sided Ehrenfeucht–Fraïssé games on representative same-profile pairs (ranks one and two), and computes sample subsequential probabilities for the oscillatory example. Run with `python3 checker.py`; expected terminal line: `ALL_CHECKS_OK`. These finite checks probe normalizations and boundary cases but are **not** proofs of any asymptotic or universal game statement; the proof is in Steps 1–7.

## Relationship to prior work

Koponen (2026, arXiv:2610.16163v1) supplies the motivating distinction between first-order convergence of deterministic base structures and of their random expansions (Introduction, Example 2.12, Corollary 2.14, Remark 2.15). It does not state a necessary-and-sufficient threshold characterization for iid unary colours on growing uniform equivalence classes, nor the paired Poisson critical laws. Braunfeld and Kukla (2021, arXiv:2111.06307v1) establish first-order limit laws for uniformly random *ordered* convex equivalence relations/layered permutations, a different distribution and vocabulary. Demin and Zhukovskii (2024) study general first-order complexity and use Poisson rare isolated-edge components in sparse random graphs (Claim 2.3); those results motivate the general method but do not identify the present equivalence-block hierarchy. Spencer and St. John (1997) study independent random unary predicates *with a fixed linear order* and scale-dependent almost-sure theories, not unordered equivalence blocks. The Ehrenfeucht–Fraïssé game and multinomial Poisson approximation are classical tools and are not claimed as new. The asserted contribution is their exact, bidirectional synthesis in the specified natural base-expansion model, including the complete convergence criterion, hierarchy, two-dimensional critical theory and concrete nonconvergence example.

## Limitations

No claim is made about biased colouring, unequal block sizes, correlated colours, random partitions, added order, second-order logic, or formula rank increasing with the domain size. The probability formula for a fixed rank can be computationally large. Independent examination of the derivation and exhaustive literature coverage have not been performed. Related special-case statements may exist under the equivalent graph language of vertex-coloured disjoint equal-sized cliques (or complete multipartite complements), or in unindexed theses; prior-publication priority is not asserted as a theorem. This work does not settle general random-expansion convergence questions for arbitrary base structures.

## References

1. Vera Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1 (publicly posted 2026-10-12), https://arxiv.org/html/2610.16163v1 . See Introduction, Example 2.12, Corollary 2.14 and Remark 2.15.
2. Samuel Braunfeld and Matthew Kukla, *Logical limit laws for layered permutations and related structures*, arXiv:2111.06307v1 (2021), https://arxiv.org/html/2111.06307v1 . See Theorem 1.1 and Section 2.
3. Danila Demin and Maksim Zhukovskii, *First order complexity of finite random structures*, LICS 2024, DOI 10.1145/3661814.3662127, lawful author manuscript https://eprints.whiterose.ac.uk/id/eprint/219343/1/LICS_FO_complexity_RS.pdf . See Section 2.1 and Claim 2.3.
4. Joel H. Spencer and Katherine St. John, *Random Unary Predicates: Almost Sure Theories and Countable Models* (1997), https://stjohn.github.io/research/rsa98.pdf . See Introduction and Section 2.
