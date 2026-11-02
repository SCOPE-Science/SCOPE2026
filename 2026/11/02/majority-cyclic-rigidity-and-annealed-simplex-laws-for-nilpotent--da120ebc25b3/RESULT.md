# Majority cyclic rigidity and annealed simplex laws for nilpotent matrix centralizers

## Finding
Let \(q\) be a prime power, \(n\ge1\), and \(k\ge2\) an integer. Choose \(N\) uniformly from the nilpotent \(n\times n\) matrices over \(\mathbb F_q\). A labeled invariant \(k\)-splitting is an ordered direct-sum decomposition \(\mathbb F_q^n=V_1\oplus\cdots\oplus V_k\), with zero summands permitted and \(N(V_i)\subseteq V_i\) for all \(i\). Let \(L_k(N)\) count these splittings. For a weak composition \(\mathbf r=(r_1,\ldots,r_k)\) of \(n\), put
\[
Q_m(q)=\prod_{i=1}^m(1-q^{-i}),\qquad Q_0(q)=1,\qquad Q_\infty(q)=\prod_{i=1}^\infty(1-q^{-i})>0.
\]
Then the exact mean of the number of invariant splittings of dimension vector \(\mathbf r\) is
\[
\boxed{\mathbb E\,L_{k,\mathbf r}(N)=\frac{Q_n(q)}{\prod_{j=1}^kQ_{r_j}(q)}.} \tag{1}
\]
For each *fixed* \(q,k\),
\[
\boxed{\mathbb E\,L_k(N)=\frac{n^{k-1}}{(k-1)!Q_\infty(q)^{k-1}}+O_{q,k}(n^{k-2}).} \tag{2}
\]
If instead an ordered pair \((N,(V_1,\ldots,V_k))\) is chosen uniformly among **all** nilpotent matrices with labeled invariant \(k\)-splittings, its normalized dimension vector converges weakly to \(\operatorname{Dirichlet}(1,\ldots,1)\), the uniform probability distribution on the standard \((k-1)\)-simplex. In particular, the rank of the commuting idempotent projection divided by \(n\) converges to \(\operatorname{Uniform}[0,1]\) for \(k=2\).

Conversely, under the original uniform-nilpotent distribution,
\[
\boxed{\Pr\{L_k(N)=k\}=\prod_{i=2}^{n}(1-q^{-i})>\frac12.} \tag{3}
\]
This event is exactly that \(N\) consists of one nilpotent Jordan block; thus \(k\) is a median of \(L_k(N)\) for every \(n\), despite the polynomially divergent mean in (2). For \(k=2\), \(L_2(N)\) is the number of idempotents in the full matrix centralizer of \(N\), and \(L_{2,(r,n-r)}(N)\) is the number of commuting idempotents of rank \(r\).

## Assumptions and scope
All spaces and matrices are over the finite field \(\mathbb F_q\), with \(q\ge2\) a prime power. Nilpotent means some matrix power is zero. Direct summands may be zero. A rank-\(r\) idempotent \(E\) commuting with \(N\) corresponds bijectively to the ordered pair \((\operatorname{im}E,\ker E)\) of \(N\)-invariant complementary spaces. The random pair distribution in the simplex assertion is **size-biased in** \(N\): it is not obtained by first choosing \(N\) uniformly and then a splitting uniformly conditional on \(N\). The asymptotics hold as \(n\to\infty\) with \(q,k\) fixed, not uniformly in growing \(k\) or varying \(q\).

## Proof
**Exact counting.** Fine--Herstein's count gives exactly \(q^{d^2-d}\) nilpotent endomorphisms in dimension \(d\), including the \(d=0\) convention. For fixed weak composition \(\mathbf r\), \(\operatorname{GL}_n(q)\) acts transitively on labeled direct-sum decompositions \(V=\bigoplus_iV_i\) with \(\dim V_i=r_i\), whose stabilizer is the block-diagonal subgroup \(\prod_i\operatorname{GL}_{r_i}(q)\). Therefore the number of such decompositions is
\[
\frac{|\operatorname{GL}_n(q)|}{\prod_i|\operatorname{GL}_{r_i}(q)|}=q^{n^2-\sum_i r_i^2}\frac{Q_n(q)}{\prod_iQ_{r_i}(q)}.
\]
For any fixed decomposition, its nilpotent-preserving endomorphisms are the independent direct sums of nilpotents on each block, in number \(q^{\sum_i(r_i^2-r_i)}\). Multiplication gives \(q^{n^2-n}Q_n/\prod_iQ_{r_i}\) pairs. Divide by the \(q^{n^2-n}\) nilpotents to obtain (1). The same argument proves the claim for \(n=1\) and for zero components.

**Mean asymptotics.** Write \(Q=Q_\infty(q)\). The tail of the product gives \(Q_d=Q+O_q(q^{-d})\), and \(Q\le Q_d\le1\). Consequently
\[
\frac{Q_n}{\prod_iQ_{r_i}}=Q^{1-k}+O_{q,k}\Bigl(q^{-n}+\sum_{i=1}^kq^{-r_i}\Bigr).
\]
There are \(\binom{n+k-1}{k-1}\) weak compositions. For fixed \(i\),
\[
\sum_{r_1+\cdots+r_k=n}q^{-r_i} =\sum_{s=0}^n q^{-s}\binom{n-s+k-2}{k-2}=O_{q,k}(n^{k-2}).
\]
Summing and expanding the binomial coefficient proves (2). For \(k=2\), a sharper expression is \(\mathbb E L_2(N)=\sum_{r=0}^n{n\brack r}_{q^{-1}}=(n+1)/Q+O_q(1)\), where the Gaussian binomial is evaluated at \(q^{-1}\).

**Simplex law.** Under uniform sampling of a pair \((N,\mathbf V)\), the probability of a weak composition \(\mathbf r\) is the positive weight in (1) divided by its sum. The displayed error bound shows that the total variation distance between this probability law on weak compositions and the *uniform* law on weak compositions is \(O_{q,k}(1/n)\), since the sum of absolute weight deviations is \(O(n^{k-2})\) while the normalizing sum is \(\Theta(n^{k-1})\). The normalized uniform weak composition tends, by Riemann-sum convergence on the simplex, to the uniform Dirichlet law. This proves the announced weak convergence. It also gives total variation convergence **on the discrete composition space** to the uniform composition law, not total variation convergence between a discrete distribution and its continuous Dirichlet limit.

**Majority cyclic rigidity.** Nilpotent \(N\) is an indecomposable \(\mathbb F_q[t]\)-module if and only if its Jordan type is \((n)\). In that case the only labeled \(k\)-splittings put the entire space in one of the \(k\) positions, so \(L_k(N)=k\). Otherwise the Jordan decomposition supplies two nonzero invariant summands; placing them into two distinct labeled positions gives additional splittings and \(L_k(N)>k\). The \(\operatorname{GL}_n(q)\)-orbit of one Jordan block has size \(|\operatorname{GL}_n(q)|/[(q-1)q^{n-1}]\), since its invertible centralizer comprises the polynomials in it with nonzero constant term. Dividing by the total \(q^{n^2-n}\) nilpotents gives \(Q_n/(1-q^{-1})=\prod_{i=2}^n(1-q^{-i})\). Finally, this product exceeds \(1/2\): by monotonicity in \(q\) it is at least the \(q=2\) infinite product, and the strict inequality \(\prod_{i\ge2}(1-2^{-i})>1-\sum_{i\ge2}2^{-i}=1/2\) follows from the elementary finite-product inequality with strict positive cross terms and passage to the limit. This proves (3), including \(n=1\).

## Verification
Run `python3 verify.py` from the same directory as this document. The script generates all matrices over \(\mathbb F_2\) in sizes 1, 2, and 3 and all matrices over \(\mathbb F_3\) in size 2; it independently tests nilpotence, idempotence, commutation, ranks, and ordered three-way decompositions (including zero summands), and matches all exact counts with formula (1). It prints `VERIFY_OK: matrix enumeration, idempotency, commutation, and ordered triples`. These finite computations check definitions and small instances only; the asymptotics are proved analytically above.

Examples: for \(n=3,q=2\), 64 nilpotents occur. Summed over these matrices, the numbers of commuting idempotents of ranks 0,1,2,3 are \(64,112,112,64\), respectively, yielding \(\mathbb E L_2=11/2\). The regular-nilpotent probability is \(42/64=21/32\).

## Relationship to prior work
Bogdanić--Đurić--Koljančić--Oblak--Šivic (arXiv:2212.08425, first posted December 16, 2022) analyzes which **nilpotent** Jordan classes intersect the nilpotent centralizer of a two-block nilpotent matrix. Here the commuting objects are **idempotent** projections of arbitrary ranks; the conclusions concern a uniform random nilpotent centralizer and its invariant-splitting statistics in all sizes. Khatami's 2023 survey (arXiv:2304.08550) addresses generic commuting nilpotent Jordan types. Fulman--Guralnick (arXiv:1611.05499) count commuting matrix pairs and, separately, commuting pairs in which both matrices are nilpotent; those enumerations do not state the present idempotent-splitting law or median/mean contrast. Leinster (arXiv:1912.12562) gives a proof of the Fine--Herstein nilpotent count used here. The Gaussian multinomial identities and direct-sum orbit counting are classical; no novelty is claimed for those ingredients. The claimed increment is their exact finite-\(k\) synthesis into a size-biased Dirichlet simplex limit with simultaneous majority-cyclic/mean-growth disparity.

## Limitations
The assertion is about **labeled ordered** decompositions, including zero summands; counting unordered decompositions or forbidding zero blocks changes the finite formulas. \(\Pr(L_k=k)>1/2\) says that cyclic matrices form a majority, not that their probability tends to 1. The simplex law uses uniform sampling of compatible pairs and is not a quenched law for a typical fixed matrix. The proof does not characterize the full distribution of \(L_k(N)\) under uniform \(N\). Equivalent formulations might exist in Hall-algebra or finite-module random-splitting literature; the inspected sources did not present the combined finite-\(k\) mean, simplex law and median contrast. An independent priority review is still needed.

## References
1. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak, K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425v1 (2022-12-16), https://arxiv.org/abs/2212.08425.
2. L. Khatami, *Commuting Jordan Types: a Survey*, arXiv:2304.08550v1 (2023-04-17), https://arxiv.org/html/2304.08550v1.
3. J. Fulman, R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499 (2016-11-16), https://arxiv.org/abs/1611.05499.
4. T. Leinster, *The probability that an operator is nilpotent*, arXiv:1912.12562 (2019-12-29), https://arxiv.org/abs/1912.12562.
