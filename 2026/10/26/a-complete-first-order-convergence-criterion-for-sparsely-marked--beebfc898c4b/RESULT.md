# A complete first-order convergence criterion for sparsely marked Ewens permutations

## Finding
Fix a real parameter \(\theta>0\). For every integer \(n\geq1\), choose a permutation \(\sigma_n\) of \([n]\) from the Ewens distribution
\[
\Pr(\sigma_n=\sigma)=\frac{\theta^{c(\sigma)}}{\theta(\theta+1)\cdots(\theta+n-1)},
\]
where \(c(\sigma)\) is its number of cycles. Independently mark each vertex with probability \(p_n\in[0,1]\). Assume \(p_n\to0\), without assuming monotonicity or regular variation, and interpret the result in the first-order language with a directed bijection relation \(F(x,y)\) (meaning \(\sigma_n(x)=y\)) and a unary mark predicate \(P(x)\).

**Theorem.** The sequence satisfies a first-order convergence law if and only if, for every integer \(k\ge1\), the extended limit
\[
a_k=\lim_{n\to\infty}n p_n^k\in[0,\infty]
\]
exists, allowing the value \(\infty\). Whenever these limits exist, probabilities of all fixed first-order sentences are determined by finitely many explicitly described Poisson variables and deterministic saturated local types. Given the finitely many limiting parameters relevant to a sentence, its limit is computable by a finite Poisson calculation.

At the critical scale \(n p_n^k\to\lambda\in(0,\infty)\), the count \(Y_{k,n}\) of ordered starts of \(k\) **distinct** consecutive marked vertices converges to \(\operatorname{Pois}(\lambda)\), jointly and independently of all fixed short-cycle counts \(C_{j,n}\to\operatorname{Pois}(\theta/j)\). Hence the first-order sentence demanding such a marked run **and** a fixed point has limiting probability
\[
(1-e^{-\lambda})(1-e^{-\theta}).
\]
There is never a zero–one law because the unmarked sentence asserting a fixed point always has limit \(1-e^{-\theta}\in(0,1)\).

## Assumptions and scope
The parameter \(\theta\) is fixed and strictly positive. The random permutation is weighted by \(\theta^{\#\mathrm{cycles}}\), not by inversions. Marks are mutually independent and independent of the permutation, with a possibly oscillating \(p_n\to0\). The language consists only of equality, the graph of the permutation, the unary predicate and ordinary first-order quantification. In particular there is no linear order, transitive closure, global orbit-equivalence predicate, arithmetic, or counting quantifier. \(\infty\) is an extended limit, not a real Poisson parameter. All asymptotics are over positive integers \(n\to\infty\).

For the probability representation, fix a first-order quantifier rank \(s\). A bounded-degree Hanf theorem supplies integers \(r,M\) such that truth at rank at most \(s\) depends only on every rooted radius-\(r\) type count truncated at \(M\). Orient neighbourhoods by the permutation. Choose any fixed integer \(H>2r\) and any cycle-length cutoff \(L>(2r+3)H\). Cycle types of length at most \(L\) are recorded individually; those longer than \(L\) are treated as oriented paths locally.

## Proof
**1. Ewens small-cycle law and negligible marked small cycles.** Write \((\theta)^{\overline n}=\theta(\theta+1)\cdots(\theta+n-1)\). For fixed nonnegative integers \(m_1,\ldots,m_L\) and \(h=\sum_{j=1}^{L}jm_j\leq n\), direct enumeration of disjoint specified cycles gives
\[
\mathbb E\prod_{j=1}^{L}(C_{j,n})_{\underline{m_j}}
=\Bigl(\prod_{j=1}^{L}(\theta/j)^{m_j}\Bigr)
\frac{(n)_{\underline h}(\theta)^{\overline{n-h}}}{(\theta)^{\overline n}}.
\]
The ratio tends to one, proving convergence of the short-cycle vector to independent Poisson variables with respective means \(\theta/j\) by factorial moments. Moreover, the expected total number of vertices in these cycles tends to \(\theta L\), and the probability any such vertex is marked is at most \(p_n\) times that expectation, hence tends to zero. The number of vertices lying on cycles longer than \(L\) is \(n-O_{\Pr}(1)\).

**2. Local marked patterns away from short cycles.** On each cycle longer than \(L\), a radius-\(r\) rooted neighbourhood is a directed path of \(2r+1\) vertices with a binary marked word. If a particular such word has exactly \(j\ge1\) marks, its probability, conditional on the permutation, is \(p_n^j(1-p_n)^{2r+1-j}\). If \(X_{j,n}\) counts roots of this fixed word on long cycles, its conditional expectation is \((n-O_{\Pr}(1))p_n^j(1+o(1))\). Two different rooted windows of fixed length are independent when disjoint. In overlapping windows their prescribed marked position sets either conflict or have at least \(j+1\) elements in their union: two different translates of a nonempty finite set of marked offsets cannot coincide on a sufficiently long cycle. Thus, with a constant depending only on \(r\),
\[
\operatorname{Var}(X_{j,n}\mid\sigma_n)
\le n p_n^j+O_r(n p_n^{j+1}).
\]
Consequently a type with \(np_n^j\to0\) disappears by Markov's inequality, and a type with \(np_n^j\to\infty\) has count tending to infinity in probability by the second-moment bound. An all-unmarked path type has count \(n-o_{\Pr}(n)\), since at most \((2r+1)\) windows are affected by each marked vertex and the number of marked vertices is \(o_{\Pr}(n)\).

**3. Joint Poisson limit at one critical mark number.** Suppose \(np_n^k\to\lambda\in(0,\infty)\). Then \(np_n^{k+1}\to0\), whereas \(np_n^j\to\infty\) for every integer \(1\le j<k\). On long cycles, link successive marked vertices whenever their forward gap is at most \(H\), and call the resulting maximal runs of marks *clusters*. A cluster with \(k\) marks has an ordered gap vector \(d=(d_1,\ldots,d_{k-1})\in\{1,\ldots,H\}^{k-1}\) (the empty vector for \(k=1\)). The event that a given vertex starts a maximal cluster of type \(d\) prescribes exactly \(k\) marked vertices and finitely many surrounding unmarked positions. It has probability \(p_n^k(1+O_{H,k}(p_n))\).

The number of starts of each gap type therefore has limiting mean \(\lambda\). For every fixed collection of gap types and factorial-moment orders, candidates with disjoint finite support have joint probability equal to the product and contribute the product of the prescribed powers of \(\lambda\). Configurations with nearby candidate starts contribute \(O_{H,k}(n^{t-1}p_n^{kt})=o(1)\) for \(t\) starts when their red supports are disjoint; overlapping red supports cannot realize two distinct *maximal* clusters. Cycles that wrap inside the fixed support cutoff have only \(O_{\Pr}(1)\) vertices and negligible marked contribution. Thus the vector of cluster counts converges to **independent** \(\operatorname{Pois}(\lambda)\) variables indexed by the finitely many gap vectors. The convergence holds conditionally on the permutation in probability, giving joint independence from the limiting Ewens short-cycle vector in Step 1.

The expected number of ordered runs of \(k+1\) marked vertices with every successive gap at most \(H\) is at most \(nH^k p_n^{k+1}=o(1)\). Hence with high probability no cluster has more than \(k\) marks. A rooted radius-\(r\) word with exactly \(k\) marked vertices lies entirely in one \(k\)-mark cluster (because its successive marked gaps are at most \(2r<H\)), up to an event of vanishing probability. A maximal cluster of each gap type contributes a fixed computable nonnegative integer number of roots of each critical type. The vector of critical rooted-type counts is therefore a deterministic linear image of the finite independent Poisson cluster vector, up to an error vanishing in probability. This *compound-Poisson* dependence between different rooted types is retained rather than incorrectly asserting independence of the rooted counts themselves.

**4. Sufficiency for first-order convergence.** Assume all extended limits \(a_j\) exist. There cannot be two different indices with finite positive limits, because \(np_n^{j+1}=p_n(np_n^j)\) and \(p_n\to0\). For each fixed Hanf radius, the finite list of rooted types splits into unmarked small cycles with independent limiting Poisson counts, a saturated all-unmarked long-cycle type, local patterns whose mark count \(j\) has \(a_j=0\) or \(\infty\), and, if present, patterns with the unique critical \(a_k\in(0,\infty)\). Steps 1–3 give a joint limit for the entire vector of counts truncated at \(M\). It takes values in a finite set. A rank-\(s\) sentence has a constant truth value on any fixed truncated Hanf profile, so its satisfaction probability converges. Enumerating the finitely many profiles and evaluating their finite Poisson probabilities yields the asserted computation, relative to the specified real parameters.

**5. Necessity.** For each fixed \(k\ge1\), let \(\psi_k\) state that there exist pairwise distinct vertices \(x_0,\ldots,x_{k-1}\) with \(F(x_i,x_{i+1})\) for \(0\le i<k-1\) and \(P(x_i)\) for all \(i\). When \(np_n^k\to\lambda<\infty\), the number of roots of such marked runs converges to \(\operatorname{Pois}(\lambda)\): disjoint runs provide the leading factorial moments and overlapping distinct runs need at least \(k+1\) marked vertices, contributing \(O(np_n^{k+1})=o(1)\). Short cycles contribute a vanishing probability. When \(np_n^k\to\infty\), the Ewens identity \(\mathbb E c(\sigma_n)=\sum_{i=0}^{n-1}\theta/(\theta+i)=O_\theta(\log n)\)\) implies that all but \(o_{\Pr}(n)\) permutation vertices can be partitioned into at least \(n/k-o_{\Pr}(n)\) disjoint consecutive \(k\)-blocks, whose all-marked events are independent with probability \(p_n^k\); hence \(\Pr(\psi_k)\to1\). The case \(np_n^k\to0\) follows from Markov's inequality. Thus along every subsequence on which \(np_n^k\) has an extended limit \(t\),
\[
\Pr(\psi_k)\longrightarrow1-e^{-t},\qquad e^{-\infty}:=0.
\]
The map \(t\mapsto1-e^{-t}\) is injective on \([0,\infty]\). If every first-order sentence converges, distinct extended subsequential limits of \(np_n^k\) are impossible; by compactness of \([0,\infty]\), the extended limit \(a_k\) must exist. This holds for every \(k\), completing necessity.

## Verification
The standalone script `check_ewens_sparse_runs.py` uses exhaustive permutations and independent binary markings for sizes up to six and exact rational arithmetic. It checks the Ewens normalization, the exact expectation of distinct length-\(k\) marked runs for \(1\le k\le4\), two integer Ewens parameters and mark probability \(1/3\). It also checks two-mark rooted neighbourhood multiplicities on cycles of lengths 13 and 17. The executed check reported `EWENS_SPARSE_FINITE_OK 100724 36 12 214`. Its finite identities test the sampling normalization and local-count formulas, not the infinite law. Reproduction: `python3 check_ewens_sparse_runs.py` using Python 3 standard library.

The proof of the theorem above invokes the classical bounded-degree Hanf locality theorem and the independently derived Ewens factorial-moment enumeration. It neither assumes an unproved infinite computation nor promotes finite testing to an asymptotic certificate.

## Relationship to prior work
Mirabi and Shelah, arXiv:2607.11033 (first submitted 13 July 2026), analyze first-order laws for **bond percolation on deterministic tori in dimension at least two**, including reciprocal-power defect thresholds under polynomial scaling; their Section 4.2 supplies a closely related locality-and-Poisson-cluster method. They do not state this theorem for a random union of directed cycles, vertex markings, Ewens cycle weights or arbitrary oscillatory vanishing marking probabilities. Thus the defect principle is borrowed, while the exact necessary-and-sufficient criterion and joint Ewens-background critical law are separate statements.

Müller, Skerman and Verstraaten, arXiv:2302.10148 (first submitted 20 February 2023), prove first-order convergence for **unmarked uniform permutations** in the one-bijection language, and discuss earlier work of Compton. Their result provides the unmarked limit-law baseline, but its premises lack the independent vanishing unary predicate and associated staircase. Godbole's 1990 success-run theorem supplies the classical Poisson approximation for runs in a Bernoulli sequence, not the permutation/logic equivalence. Koponen, arXiv:2610.16163 (first submitted 12 October 2026), motivates the general study of random expansions and logical convergence; only its abstract was accessible in this inspection, so no full-text exclusion claim is made about it.

## Limitations
This theorem concerns first-order logic with one bijection and one unary predicate, fixed \(\theta>0\), and vanishing independent mark probabilities. It makes no assertion for \(p_n\not\to0\), varying Ewens parameters, global orders, reachability predicates or monadic second-order logic. The mathematical argument provides a same-document proof rather than an independent external audit. It does not claim that the local-pattern/Poisson methodology is new; a general earlier theorem for random marked bounded-degree structures could subsume the result. Priority beyond the inspected sources is not independently certified.

## References
1. M. Mirabi and S. Shelah, *Limit laws for component-pruned sparse random graphs and percolated tori*, arXiv:2607.11033, first submitted 2026-07-13, HTML version 2, Sections 2 and 4.2, https://arxiv.org/html/2607.11033v2.
2. T. Müller, F. Skerman and T. W. Verstraaten, *Logical limit laws for Mallows random permutations*, arXiv:2302.10148, first submitted 2023-02-20, introduction, Theorem 1.1 and Section 4, https://arxiv.org/abs/2302.10148.
3. V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163, first submitted 2026-10-12, https://arxiv.org/abs/2610.16163.
4. A. P. Godbole, *Degenerate and Poisson convergence criteria for success runs*, Statistics & Probability Letters 10 (1990), 247–255, DOI:10.1016/0167-7152(90)90082-I.
5. J. Najnudel and J. Pitman, *Feller coupling of cycles and Poisson spacings*, arXiv:1907.09587, https://arxiv.org/abs/1907.09587.
