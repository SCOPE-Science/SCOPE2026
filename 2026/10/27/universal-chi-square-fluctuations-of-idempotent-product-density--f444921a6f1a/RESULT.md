# Universal chi-square fluctuations of idempotent-product density in random Rees matrix semigroups

## Finding

Let \(G\) be any finite group of order \(h\geq2\), let \(r\geq2\) be fixed, and for each integer \(n\geq1\) choose an \(r\)-by-\(n\) matrix \(P=(p_{\lambda i})\) whose entries are independent uniform elements of \(G\). The associated completely simple Rees matrix semigroup is
\[
S(P)=[n]\times G\times[r],\qquad
(i,a,\lambda)(j,b,\mu)=(i,a p_{\lambda j}b,\mu).
\]
Write \(E(P)\) for its idempotents and define the intrinsic *idempotent-product density*
\[
T_{r,n}(P)=\frac{\#\{(e,f)\in E(P)^2:(ef)^2=ef\}}{|E(P)|^2}.
\]
This tests whether a product of two independently uniformly chosen idempotents is again idempotent; the word "product" is ordered, and commutation is not required.

Put \(\theta_{r,h}=\frac1r+\frac{r-1}{rh}\). For each \(1\leq\lambda<\mu\leq r\), let
\[
z_{\lambda\mu,i}=p_{\lambda i}p_{\mu i}^{-1},\quad
N_{\lambda\mu}(g)=\#\{i:z_{\lambda\mu,i}=g\},\quad
Q_{\lambda\mu}=\frac hn\sum_{g\in G}\left(N_{\lambda\mu}(g)-\frac nh\right)^2.
\]
Then the following identity is exact for **every** sandwich matrix, without any randomness:
\[
\boxed{\quad n\bigl(T_{r,n}(P)-\theta_{r,h}\bigr)
=\frac{2}{r^2h}\sum_{\lambda<\mu}Q_{\lambda\mu}.\quad}
\]
In particular \(T_{r,n}(P)\geq\theta_{r,h}\), with equality precisely when every row-pair ratio vector distributes its \(n\) entries uniformly among the \(h\) elements of \(G\).

For the independent uniform-entry model, both finite-\(n\) moments are explicit:
\[
\boxed{\ \mathbb E T_{r,n}=\theta_{r,h}+\frac{(r-1)(h-1)}{rhn},\qquad
\operatorname{Var}(T_{r,n})=\frac{8\binom r2(h-1)(n-1)}{r^4h^2n^3}.\ }
\]
With \(r,h\) fixed and \(n\longrightarrow\infty\), the full non-Gaussian second-order law is
\[
\boxed{\quad n\bigl(T_{r,n}-\theta_{r,h}\bigr)
\xrightarrow{\mathrm d}\frac{2}{r^2h}\chi^2_{(h-1)\binom r2}.\quad}
\]
Here \(\chi^2_d\) is a chi-square random variable with \(d\) degrees of freedom. Moreover \(T_{r,n}\longrightarrow\theta_{r,h}\) almost surely under **any** coupling of the specified distributions across \(n\); no independence between different matrix sizes is needed.

The exact moments, limiting density, and fluctuation law depend on the group only through its cardinality, including for nonabelian groups. The finite-\(n\) Pearson statistics of different row pairs are pairwise independent, but need not be jointly independent; their Gaussian limits are jointly independent.

## Assumptions and scope

The row and column indices are labeled. Uniform randomness means independent uniform entries in \(G\), **not** a uniform distribution on isomorphism classes of semigroups. The group operation need not commute. The asymptotic keeps \(r\) and \(G\) fixed. The model has no zero entries: it is a completely simple Rees matrix semigroup, not a general Rees zero-matrix semigroup. For the trivial group \(h=1\), the excluded degenerate boundary has \(T_{r,n}=1\) deterministically. No uniformity is asserted when \(r\) or \(h\) grows with \(n\).

## Proof

**1. Idempotent products.** Direct multiplication shows that all idempotents are exactly
\[
e_{i,\lambda}=(i,p_{\lambda i}^{-1},\lambda),\qquad i\in[n],\ \lambda\in[r].
\]
Thus \(|E(P)|=rn\). If \(\lambda=\mu\), then \(e_{i,\lambda}e_{j,\lambda}=e_{i,\lambda}\), which is always idempotent. For distinct \(\lambda,\mu\), multiplication gives
\[
e_{i,\lambda}e_{j,\mu}=(i,p_{\lambda i}^{-1}p_{\lambda j}p_{\mu j}^{-1},\mu).
\]
This is idempotent if and only if its middle coordinate is \(p_{\mu i}^{-1}\), equivalently
\[
p_{\lambda i}p_{\mu i}^{-1}=p_{\lambda j}p_{\mu j}^{-1}.
\]
The same condition works in the reversed row order, even for noncommutative \(G\). Hence the exact number of successful ordered pairs is
\[
B(P)=rn^2+2\sum_{\lambda<\mu}\sum_{g\in G}N_{\lambda\mu}(g)^2.
\]
Using \(\sum_gN_{\lambda\mu}(g)=n\) and completing the square,
\[
\sum_gN_{\lambda\mu}(g)^2=\frac{n^2}{h}+\frac nhQ_{\lambda\mu}.
\]
Divide by \(r^2n^2\) to obtain the boxed exact identity and its nonnegative equality condition.

**2. Exact moments and pairwise independence.** For any one row pair, the \(n\) ratios \(z_{\lambda\mu,i}\) are independent uniform elements of \(G\). For two *distinct* row pairs, the two ratios in any given column are also independent uniform elements. If the pairs share a row, condition on that row entry; the remaining independent uniform entries make the two ratios independent uniform variables. If the pairs are disjoint, independence is immediate. Columns themselves are independent. Therefore the entire ratio sequences for distinct row pairs are pairwise independent (not necessarily jointly independent for triples).

For a single row pair, put \(C=\sum_{i<j}{\bf1}\{z_i=z_j\}\). Then
\[
\sum_gN_g^2=n+2C,\qquad \mathbb EC=\binom n2/h.
\]
The indicators of equality associated with two different column pairs are pairwise independent, including when the pairs share one column: condition on the shared value. Thus
\[
\operatorname{Var}(C)=\binom n2\frac1h\left(1-\frac1h\right).
\]
It follows that for a single Pearson statistic
\[
\mathbb EQ=h-1,\qquad
\operatorname{Var}(Q)=\frac{2(h-1)(n-1)}{n}.
\]
The exact identity, together with pairwise independence across row pairs, gives the two boxed moment formulas.

**3. Joint Gaussian limit despite triple dependencies.** For each column \(i\), form the real vector of all indicators
\(\bigl({\bf1}\{z_{\lambda\mu,i}=g\}:\lambda<\mu,\ g\in G\bigr)\).
These column vectors are i.i.d. and bounded. Their centered covariance is block diagonal across row pairs by the pairwise independence above. Each \(h\)-by-\(h\) diagonal block is
\[
\frac1hI_h-\frac1{h^2}{\bf1}{\bf1}^{\mathsf T},
\]
whose eigenvalues on the \((h-1)\)-dimensional sum-zero hyperplane all equal \(1/h\), and whose remaining eigenvalue is zero. The finite-dimensional multivariate central limit theorem therefore yields **independent** standard Gaussian vectors on these \((h-1)\)-dimensional hyperplanes after multiplying each centered occupancy block by \(\sqrt{h/n}\). Squaring their Euclidean norms gives simultaneous convergence of the \(Q_{\lambda\mu}\) to independent \(\chi^2_{h-1}\) variables. Summing them and using the exact identity gives the stated chi-square law with \((h-1)\binom r2\) degrees of freedom. This argument does not incorrectly assume finite-\(n\) mutual independence among three or more row-pair ratios.

**4. Almost-sure convergence.** The moment formulas imply
\(\mathbb E[(T_{r,n}-\theta_{r,h})^2]=O_{r,h}(n^{-2})\).
For any coupling of the random matrices across \(n\), Markov's inequality on this square and the first Borel--Cantelli lemma imply convergence of \(T_{r,n}\) to \(\theta_{r,h}\) almost surely. Independence between different values of \(n\) is unnecessary.

## Verification

The standalone \(\texttt{verify.py}\) uses explicit group multiplication rather than the row-ratio test when evaluating whether \((ef)^2=ef\). It exhaustively traverses all \(h^{rn}\) sandwich matrices in these five configurations: cyclic groups of order two with \((r,n)=(2,2),(3,3)\); cyclic order three with \((2,3)\); and the nonabelian symmetric group on three letters with \((2,2),(3,2)\). The respective numbers of matrices checked are \(16,512,729,1296,46656\). Every direct product count matched the row-ratio formula, and the exact rational mean and variance matched the displayed theoretical formulas. Invoke \(\texttt{python verify.py}\) with Python 3; the expected final line is \(\texttt{ALL_CHECKS_OK}\). These finite tests do not establish the asymptotic theorem, which follows from the proof above.

## Relationship to prior work

Rees' structure theorem and the sandwich-matrix representation are classical, and are **not** claimed as new. Quinn-Gregson's *Homogeneous completely simple semigroups* (first arXiv version 28 August 2019, Sections 4--5) develops Rees matrices and their colored bipartite graph descriptions in the study of homogeneity. Radović--Mudrinski's *Commutators in Completely Simple Semigroups* (first arXiv version 10 August 2022, Sections 2--5) studies congruence commutators and nilpotency/solvability rather than random products of idempotents. Russell's *Enumerating 0-simple semigroups* (2021, Chapters 2 and 6) counts isomorphism classes and treats presentations of factorisable orthodox monoids, not the labeled random product-density law. Paulista's *Commuting graphs of completely simple semigroups* (arXiv 9 December 2024, Section 3) studies commutation, which requires equal row and column indices, not idempotence of a possibly noncommuting product. The classical multinomial central limit theorem and Pearson chi-square asymptotics are used as known tools; their general probabilistic statements are not claimed as new. The result here is the group-universal *semigroup* identity, finite moments, and joint second-order law for products of idempotents.

## Limitations

This result does not enumerate unlabeled semigroup isomorphism types, does not address sparse or zero entries, and does not handle simultaneous growth of the row number or group order. It does not establish a universal publication-priority claim: an equivalent statement could be implicit in unindexed literature on random sandwich matrices or collision U-statistics. Finite tests do not independently establish the general claims; the asymptotic conclusions depend on the proof.

## References

1. Thomas Quinn-Gregson, *Homogeneous completely simple semigroups*, arXiv:1908.10665 (first posted 2019-08-28), https://arxiv.org/abs/1908.10665 ; published in *Mathematika* 66 (2020), 733--751.
2. Jelena Radović and Nebojša Mudrinski, *Commutators in Completely Simple Semigroups*, arXiv:2208.05237 (first posted 2022-08-10), https://arxiv.org/abs/2208.05237 .
3. Christopher Russell, *Enumerating 0-simple semigroups*, University of St Andrews PhD thesis (2021), https://doi.org/10.17630/sta/109 .
4. Tânia Paulista, *Commuting graphs of completely simple semigroups*, arXiv:2412.06560 (first posted 2024-12-09), https://arxiv.org/abs/2412.06560 .
