# An exact cyclic fragmentation of conditioned random-walk excursion lengths

## Finding

**Theorem (successive-return fragmentation).** Let \(n\ge2\) and let \((S_t)_{t=0}^{2n}\) be a simple symmetric random walk started at zero, conditioned on \(S_{2n}=0\). Let \(K=\#\{t\in\{1,\ldots,2n\}:S_t=0\}\), counting the terminal return. If the consecutive excursions from zero have durations \(2L_1,\ldots,2L_K\), then for every \(k=1,\ldots,n-1\) there is an explicit **one-coordinate splitting coupling** between the full ordered excursion-half-length vectors conditional on \(K=k\) and \(K=k+1\). In this coupling the latter vector is a cyclic rotation of the former after exactly one strictly positive coordinate is split into two strictly positive coordinates. These couplings can be chained simultaneously for all \(1\le k\le n\).

Consequently, write \(\Lambda_{n,k}\) for the sorted excursion half-lengths conditional on \(K=k\), padded with zeroes to length \(n\). There is one probability space on which
\[
\Lambda_{n,1}\succeq\Lambda_{n,2}\succeq\cdots\succeq\Lambda_{n,n}
\]
almost surely, where \(\succeq\) denotes vector majorization. In particular, the maximum half-length is stochastically nonincreasing in the conditioned number of returns, and the conditional expectation of every integrable symmetric Schur-convex function of the zero-padded vector is nonincreasing.

For \(Q=\sum_{i=1}^K L_i^2\) the following quantitative inequality is sharp for all \(n\ge2\):
\[
\mathbb E[Q\mid K=k]-\mathbb E[Q\mid K=k+1]\ge2,
\quad 1\le k<n,
\]
with equality **if and only if** \(k=n-1\). Thus the last transition always reduces \(Q\) by exactly two; all earlier transitions reduce its expectation by strictly more than two.

## Assumptions and scope

All increments are independent with probabilities \(1/2\) for each of \(+1\) and \(-1\); the bridge is tied down at the prescribed even time \(2n\). The return count includes time \(2n\) but excludes time zero. Each of its \(K\) complete excursions has positive integer half-length, and \(\sum_{i=1}^K L_i=n\). Conditioning on any \(K=k\) with \(1\le k\le n\) has positive probability. Only the excursion **lengths** are coupled, not the signs, peak heights, or full paths. Majorization compares sorted vectors after adding zero coordinates and means that each initial partial sum of the decreasing arrangement is at least as large, while total sums agree.

## Proof

**1. The conditioned Catalan composition law.** Define \(w_j=C_{j-1}=\frac1j\binom{2j-2}{j-1}\) for positive integers \(j\), with \(C_r\) the Catalan numbers. There are \(2w_j\) signed simple-walk primitive excursions of duration \(2j\) (two signs, and \(w_j\) positive excursions). Conditional on the return count, the factors of two cancel. Therefore, for every ordered composition \(\ell=(\ell_1,\ldots,\ell_k)\) of \(n\),
\[
\mathbb P((L_1,\ldots,L_k)=\ell\mid K=k)
=\frac{W(\ell)}{Z_{n,k}},\qquad
W(\ell)=\prod_{i=1}^k w_{\ell_i},
\]
where \(Z_{n,k}=\sum_{\ell_1+\cdots+\ell_k=n}\prod_i w_{\ell_i}\). The generating series \(F(z)=\sum_{j\ge1}w_jz^j=(1-\sqrt{1-4z})/2\) satisfies \(F=z/(1-F)\); Lagrange inversion gives
\[
Z_{n,k}=[z^n]F(z)^k
=\frac{k}{2n-k}\binom{2n-k}{n-k},
\quad 1\le k\le n.
\]
In particular,
\[
\frac{Z_{n,k+1}}{Z_{n,k}}
=\frac{(k+1)(n-k)}{k(2n-k-1)}.
\]
The Catalan convolution identity gives \(\sum_{a=1}^{j-1}w_aw_{j-a}=w_j\) for \(j\ge2\).

**2. A normalized transition kernel.** Start with a vector \(\ell\) having the above conditioned law at \(k<n\). Choose index \(i\) with probability \((\ell_i-1)/(n-k)\), which is a probability distribution because \(\sum_i(\ell_i-1)=n-k\). The selected size \(j=\ell_i\) is necessarily at least two. Choose a split \((a,b)\), with \(a,b\ge1\), \(a+b=j\), with conditional probability \(w_aw_b/w_j\). The Catalan convolution makes these probabilities sum to one. Replace \(j\) by \((a,b)\), producing a \((k+1)\)-tuple; then rotate this tuple cyclically by a uniform number of positions in \(\{0,\ldots,k\}\).

**3. Exact identification of the output law.** Fix an ordered composition \(y=(y_1,\ldots,y_{k+1})\) of \(n\), and write \(y_{k+2}=y_1\). For every cyclic adjacent pair \((y_i,y_{i+1})\), merging that pair produces a possible parent in any of the \(k\) cyclic orientations where the pair is adjacent without crossing the linear boundary. For each such oriented preimage, the weight of the parent, times the selection and conditional-split weights, cancels all Catalan factors except \(W(y)\); the contribution is
\[
\frac{W(y)}{Z_{n,k}}\frac{y_i+y_{i+1}-1}{(n-k)(k+1)}.
\]
The enumeration counts occurrences (not just distinct numerical tuples), so repeated part sizes do not change it. Summing over the \(k\) allowed rotations for each of the \(k+1\) circular edges, and using \(\sum_i(y_i+y_{i+1}-1)=2n-k-1\), gives
\[
\mathbb P(Y=y)
=\frac{k(2n-k-1)}{(k+1)(n-k)Z_{n,k}} W(y)
=\frac{W(y)}{Z_{n,k+1}}.
\]
This is exactly the conditioned law at \(K=k+1\). Iterating the kernels from \(k=1\), whose law is the point mass on \((n)\), yields one simultaneous family with the required marginal at every return count.

**4. Majorization and the sharp quadratic bound.** Splitting a nonnegative mass into two positive masses preserves the sum and cannot increase any sum of the \(r\) largest entries once zeros are appended; rotation preserves the sorted vector. Hence the coupling gives the claimed almost-sure majorization, stochastic ordering of the longest excursion, and Schur-convex expectation inequalities. A split of \(j=a+b\) changes the quadratic statistic by
\[
(a+b)^2-a^2-b^2=2ab\ge2.
\]
For \(k=n-1\), the only possible vectors have one part of size two and all remaining parts of size one; the split has \(a=b=1\), giving a deterministic drop of two. For \(k<n-1\), a composition with a part at least three has positive conditional weight, its index has positive selection probability, and any positive split of that part has \(ab\ge2\). Therefore the expected drop is strictly greater than two. This completes the proof.

## Verification

`CHECK.py` uses exact rational arithmetic to enumerate every positive composition of \(n\) and compare the output of the stated transition kernel against the target Catalan product law for each \(2\le n\le10\) and each \(1\le k<n\). It separately enumerates **all** \(2^{2n}\) sign sequences for \(1\le n\le6\) and checks the primitive-excursion product weights directly. It also verifies the strict quadratic-expectation drop at each tested transition. The reproducible output is in `CHECK_OUTPUT.txt`. These finite checks corroborate, but do not replace, the all-\(n\) proof above.

## Relationship to prior work

Csáki and Hu (2003) derive exact and limiting distributions of ranked excursion lengths of simple random walks, using reflection and renewal recurrences. Lindell and Holst (2007) derive ranked-excursion distribution and generating-function laws for tied-down walks and Brownian bridges. Serlet (2014), specifically the enumeration on page 4 and its Catalan generating series, explicitly supplies the conditioned excursion-composition weight used in step 1, in the course of studying a **few-return asymptotic**. The contribution asserted here is not that weight or its coefficient alone: it is the *cross-return-count* cyclic splitting transition, its exact all-level joint construction, and the consequent pathwise majorization. These previously known distributions alone do not specify a coupling having a single split per transition, nor do they assert the all-level majorization statement.

## Limitations

This is a finite, simple, symmetric nearest-neighbor bridge theorem; it does not assert analogous couplings for arbitrary jump distributions, general renewal weights, continuous-time bridges, or Brownian local-time conditioning. It provides stochastic ordering of excursion **durations**, not their heights, signs, or the maximum path displacement. A size-biased single-excursion length regression can yield related scalar moment inequalities without proving a simultaneous vector refinement. Comparisons with broader random-tree fragmentation literature were necessarily nonexhaustive; historical priority of a related abstract fragmentation construction is not established independently. Exact tests stop at the stated finite bounds, while the mathematical proof is all-dimensional.

## References

1. E. Csáki and Y. Hu, *Lengths and heights of random walk excursions*, Discrete Mathematics & Theoretical Computer Science, AC (2003), 45–52, doi:10.46298/dmtcs.3337. Public bibliographic record: https://dmtcs.episciences.org/en/articles/3337
2. A. Lindell and L. Holst, *Distributions of the Longest Excursions in a Tied Down Simple Random Walk and in a Brownian Bridge*, Journal of Applied Probability **44** (2007), 1056–1067, doi:10.1239/jap/1197908824. Public full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/DBFE4C12676F551D6F5095BAAA8ED354/S0021900200003739a.pdf/distributions_of_the_longest_excursions_in_a_tied_down_simple_random_walk_and_in_a_brownian_bridge.pdf
3. L. Serlet, *Invariance Principle for the Random Walk Conditioned to Have Few Zeros*, Lecture Notes in Mathematics **2123** (2014), 461–472, doi:10.1007/978-3-319-11970-0_19. Author-accessible full text: https://lmbp.uca.fr/~serlet/rwfew.pdf
