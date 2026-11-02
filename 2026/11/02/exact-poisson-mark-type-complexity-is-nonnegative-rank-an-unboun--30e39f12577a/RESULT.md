# Exact Poisson mark-type complexity is nonnegative rank: an unbounded-rank-three obstruction

## Finding

For a finite nonnegative matrix \(A=(a_{ij})_{i,j=1}^{n}\) and \(\ell>0\), consider the marked Poisson branching reproduction law in which a parent with mark \(i\) has independent offspring counts \(\operatorname{Pois}(\ell a_{ij})\) of each mark \(j\). A latent-type representation has \(r\) child types. A mark-\(i\) parent produces independently \(\operatorname{Pois}(b_{ih})\) children of latent type \(h\), and each child of type \(h\) receives mark \(j\) independently with probability \(q_{hj}\), where \(q_{hj}\) does **not** depend on the parent's mark. Reproduction of future particles depends on their marks by the same rules.

**Theorem.** The smallest \(r\) giving exactly the entire unthinned marked branching law, for every root mark, is
\[
 r_{\mathrm{mark}}(A)=\operatorname{rank}_{+}(A),
\]
where \(\operatorname{rank}_{+}\) is ordinary (not restricted or completely positive) nonnegative matrix rank.

Let \(n\ge k\ge3\), and put
\[
 Q^{(n)}_{ij}=(i-j)^2,\qquad
 R(n)=\min\left\{r\ge1:\binom{r}{\lfloor r/2\rfloor}\ge n\right\}.
\]
Then \(Q^{(n)}\) is symmetric of ordinary rank three, and every exact marked-type representation requires at least \(R(n)\) types. Moreover, for every fixed \(k\ge3\), the strictly positive symmetric matrices
\[
 A^{(n,k)}_{ij}(\delta)=(i-j)^2+\delta\left(1+\sum_{m=3}^{k-1}i^m j^m\right)
\]
have ordinary rank exactly \(k\) for every \(\delta>0\), and have nonnegative rank at least \(R(n)\) for all sufficiently small \(\delta>0\) (depending on \(n,k\)). Thus **no bound depending only on the ordinary rank \(k\ge3\)** controls the number of latent child types required by this exact marked-Poisson construction, even when every entry of the interaction matrix is strictly positive.

The obstruction also occurs in sparse independent-edge random graphs. Choose such a \(\delta=\delta_{n,k}\) with \(0<\delta\le n^{-2k}\) and set \(\ell=n^{-3}\). The independent probabilities \(p_{ij}=1-\exp(-\ell A^{(n,k)}_{ij}(\delta))\) all lie strictly between zero and one and the expected degree of every vertex (self-loop counted at most once) is at most \(1+k/n^2\). The natural exact unthinned marked-Poisson exploration nevertheless needs at least \(R(n)\) latent types, where
\[
 R(n)=\log_2 n+\tfrac12\log_2\log_2 n+O(1).
\]

## Assumptions and scope

The matrix is finite, symmetric and nonnegative when used as a random-graph interaction kernel, but the equality with nonnegative rank holds for any finite nonnegative rectangular intensity matrix when source and target mark sets are allowed to differ. An arbitrary positive scale \(\ell\) is permitted. A *type* here is a latent child-production channel with a fixed mark-emission distribution. Its emission law is common across all parent marks, while the rate of that type is allowed to depend on the parent mark. Each parent has independent Poisson type counts, and child marks are conditionally independent given their types. The theorem concerns equality of the **unthinned** marked offspring process (and hence supplies the standard thinning construction for graph neighborhoods). It does not claim minimality over all possible history-dependent or differently encoded graph-neighborhood samplers.

In particular, if the mark-emission law is allowed to depend on the parent mark, every matrix admits a one-channel Poisson representation: take its parent-specific row sum as the rate and that row normalized as the emission law. The parent-independent emission condition is therefore essential.

## Proof

**1. Exact representation criterion.** Let \(B=(b_{ih})\ge0\), and let \(Q=(q_{hj})\ge0\) have row sums one. Independent Poisson marking (the splitting theorem) makes the number of children of type \(h\) marked \(j\) a Poisson variable with mean \(b_{ih}q_{hj}\), independent across all pairs \((h,j)\). Superposition over the latent types gives independent mark counts with respective means
\[
 \sum_{h=1}^{r}b_{ih}q_{hj}=(BQ)_{ij}.
\]
Thus exact equality of the one-generation laws for every parent mark is equivalent to \(BQ=\ell A\); equality of all generations then follows by induction using independence of offspring families. Conversely, given \(\ell A=UV\) with \(U,V\ge0\), define \(s_h=\sum_j V_{hj}\). Drop any factor with \(s_h=0\), and set \(b_{ih}=U_{ih}s_h\) and \(q_{hj}=V_{hj}/s_h\). This is a valid type-rate/emission representation with \(BQ=\ell A\). The minimum number of factors therefore equals \(\operatorname{rank}_{+}(A)\), since multiplying by \(\ell>0\) does not change nonnegative rank.

**2. The rank-three lower bound.** The vectors \((1)_{i=1}^n\), \((i)_{i=1}^n\) and \((i^2)_{i=1}^n\) are linearly independent for \(n\ge3\); from \((i-j)^2=i^2-2ij+j^2\), the ordinary rank of \(Q^{(n)}\) is three. Suppose \(Q^{(n)}=UV\) with \(r\) nonnegative factors, and define the subsets of the factor set \([r]\):
\[
 S_i=\{h:U_{ih}>0\},\qquad T_i=\{h:V_{hi}>0\}.
\]
Because \(Q^{(n)}_{ii}=0\), nonnegativity gives \(S_i\cap T_i=\varnothing\). For any \(i\ne j\), positivity of \(Q^{(n)}_{ij}\) forces some \(h\in S_i\cap T_j\), hence \(h\in S_i\setminus S_j\). Interchanging \(i,j\) also gives \(S_j\setminus S_i\ne\varnothing\). Thus the \(n\) sets \(S_i\) form an antichain of subsets of \([r]\). Sperner's theorem yields \(n\le\binom{r}{\lfloor r/2\rfloor}\), so \(\operatorname{rank}_{+}(Q^{(n)})\ge R(n)\). Central-binomial Stirling asymptotics give the stated expansion of \(R(n)\).

**3. Stability and exact rank after full-support perturbation.** For fixed matrix dimensions, the set of nonnegative matrices of nonnegative rank at most \(r\) is closed. To see this, if \(X^{(t)}=U^{(t)}V^{(t)}\to X\), normalize each nonzero column of \(U^{(t)}\) to have sum one, transferring its scale into the corresponding row of \(V^{(t)}\); zero factors may be replaced by an arbitrary normalized column and a zero row. Every entry of the normalized \(U^{(t)}\) lies in \([0,1]\), and
\[
 \sum_h V^{(t)}_{hj}=\sum_i X^{(t)}_{ij}
\]
bounds every entry of \(V^{(t)}\). Extract a converging subsequence to obtain a nonnegative factorization of \(X\) with at most \(r\) factors.

For fixed \(n,k\), \(A^{(n,k)}(\delta)\to Q^{(n)}\) as \(\delta\downarrow0\). Closedness therefore implies \(\operatorname{rank}_{+}(A^{(n,k)}(\delta))\ge R(n)\) for every sufficiently small positive \(\delta\). To compute the ordinary rank, write \(H_{im}=i^m\) for \(m=0,\ldots,k-1\). The Vandermonde matrix \(H\) has column rank \(k\), and \(A^{(n,k)}=HCH^{\mathsf T}\), where \(C\) consists of the leading three-by-three block
\[
 \begin{pmatrix}\delta&0&1\\0&-2&0\\1&0&0\end{pmatrix}
\]
and a diagonal block \(\delta I_{k-3}\). Its determinant equals \(2\delta^{k-3}\ne0\), proving \(\operatorname{rank}(A^{(n,k)}(\delta))=k\). The uniform positive term \(\delta\) makes every entry strictly positive.

**4. Sparse graph realization.** The stability statement permits choosing \(0<\delta_{n,k}\le n^{-2k}\) with the asserted nonnegative-rank bound. For every \(i,j\),
\[
 A^{(n,k)}_{ij}(\delta_{n,k})
 \le (n-1)^2+1+(k-3)n^{-2}\le n^2+k.
\]
The inequality \(1-e^{-x}\le x\), for \(x\ge0\), yields
\[
 \mathbb E\deg(i)\le\sum_j p_{ij}\le n\cdot n^{-3}(n^2+k)=1+\frac{k}{n^2}.
\]
All edge probabilities are positive, and the mark-intensity factorization is unaffected by the positive scale \(\ell=n^{-3}\). As \(n\to\infty\) at any fixed \(k\ge3\), \(R(n)\to\infty\), proving the absence of a rank-only bound within the stated representation class.

## Verification

The accompanying standalone `verify.py` uses exact rational Gaussian elimination to confirm the rank-three squared-distance matrices and the rank-\(k\) strictly positive kernels for a range of finite sizes. It also verifies the central-binomial threshold identities and, on an independent rational factorization, the type-rate/emission normalization underlying Poisson splitting. All 2,206 finite rational assertions pass. The infinite antichain and closedness steps above are mathematical arguments, not consequences of finite testing.

## Relationship to prior work

Chakraborty, Raaijmakers and van der Hofstad (2022, Sections 1–3 and 7) give exact few-type marked-Poisson constructions for rank one and two and selected higher-rank matrix families, and explicitly ask whether a number of types depending only on ordinary rank always suffices. This theorem answers that question negatively **for the exact, parent-independent-emission Poisson class defined above**, and identifies its precise minimization invariant.

The squared-distance rank-three example and the Sperner lower bound for its **matrix** nonnegative rank are prior results of Beasley and Laffey (2009), documented and refined by Gillis and Glineur (2010); the rank-three/unbounded-nonnegative-rank phenomenon is not claimed to be new. Shitov (2013) establishes another rank-three matrix separation. The lower-semicontinuity of nonnegative rank under small perturbations is also known (Bocci, Carlini and Rapallo, 2010/2011). The contribution here is the exact type-minimality correspondence and its sparse, strictly positive random-graph consequence with arbitrary fixed ordinary rank at least three. Earlier nonnegative-rank results alone concern matrix factorization, rather than equality of the complete marked branching reproduction law.

## Limitations

The positive perturbation thresholds \(\delta_{n,k}\) are established existentially, not as explicit numerical constants. The theorem gives a necessary lower bound, not exact nonnegative ranks, for the specified kernels. It does not rule out fewer types in models allowing parent-dependent mark emissions, random-history dependencies, or equality only after pruning repeated marks; indeed, the parent-dependent-emission variant has a one-type representation. It does not identify an optimal branching-process representation for all graph-neighborhood exploration algorithms. Definitive historical priority and independent mathematical validation remain open.

## References

1. S. Chakraborty, K. Raaijmakers, R. van der Hofstad, *Rank-k random graphs and finite type branching processes*, first arXiv submission 2022-07-23, arXiv:2207.11471v1, https://arxiv.org/html/2207.11471v1.
2. L. B. Beasley, T. J. Laffey, *Real rank versus nonnegative rank*, Linear Algebra Appl. 431 (2009), 2330–2335, https://doi.org/10.1016/j.laa.2009.02.034.
3. N. Gillis, F. Glineur, *On the Geometric Interpretation of the Nonnegative Rank*, arXiv:1009.0880, https://arxiv.org/abs/1009.0880, especially Sections 3 and 4.2.
4. Y. Shitov, *Nonnegative rank of a matrix with one negative eigenvalue*, arXiv:1308.4716, https://arxiv.org/abs/1308.4716.
5. C. Bocci, E. Carlini, F. Rapallo, *Perturbation of matrices and non-negative rank with a view toward statistical models*, arXiv:1010.3566, https://arxiv.org/abs/1010.3566, Theorem 2.
