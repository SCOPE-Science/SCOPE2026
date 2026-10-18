# The exact four-level covariance spectrum of directed degree-pair histograms

## Finding

In the independent-arc, loopless directed Erdős–Rényi model, let \(H_{rs}\) count vertices with outdegree \(r\) and indegree \(s\), for \(0\le r,s\le n-1\). Even though these \(n^2\) counts are strongly constrained and dependent, their **entire finite-sample covariance spectrum** has a distribution-free-in-\(p\) form after Pearson standardization.

**Theorem.** For every integer \(n\ge2\) and every edge probability \(0<p<1\), put \(m=n-1\), \(q=1-p\), \(b_r=\binom mr p^r q^{m-r}\), and \(w_{rs}=b_rb_s\). Index the covariance matrix \(\Sigma=\operatorname{Cov}((H_{rs})_{r,s=0}^{m})\) by pairs \((r,s)\) and let \(D=\operatorname{diag}((w_{rs})_{r,s})\). Then the eigenvalues, including multiplicities, of

\[
D^{-1/2}\Sigma D^{-1/2}
\]

are

\[
\boxed{0\ \text{(twice)},\qquad n\ \text{(multiplicity }n^2-4\text{)},\qquad \frac{n^2}{n-1}\ \text{(once)},\qquad 2n\ \text{(once)}.}
\]

At \(n=2\) the middle multiplicity is zero and the last two eigenvalues coincide. The covariance matrix has rank precisely \(n^2-2\) for all \(n\ge2\). Its two exact null directions are the constant count \(\sum H_{rs}=n\) and the equal-total-degree identity \(\sum(r-s)H_{rs}=0\). The top eigenmode is the centered total in-plus-out degree; the intermediate eigenmode is the product of the centered outdegree and indegree.

The result gives the **sharp all-statistics variance bound**: for any real function \(f\) on \(\{0,\ldots,m\}^2\), writing \((R,S)\) for two independent \(\operatorname{Bin}(m,p)\) random variables,

\[
0\le \operatorname{Var}\left(\sum_{v=1}^n f(O_v,I_v)\right)\le 2n\operatorname{Var}(f(R,S)).
\]

The upper constant is attained by \(f(r,s)=r+s\), while zero variance is attained by the nonconstant score \(f(r,s)=r-s\). These statements hold at every finite size and throughout the open probability interval.

## Assumptions and scope

The labeled vertices are \(1,\ldots,n\). For every ordered pair \((i,j)\), \(i\ne j\), the arc \(i\to j\) is present independently with probability \(p\). Reverse arcs are sampled independently and may coexist. Self-loops are forbidden. The outdegree and indegree at vertex \(v\) are \(O_v\) and \(I_v\), respectively. For each \((r,s)\), set \(H_{rs}=\#\{v:O_v=r, I_v=s\}\).

Each vertex has independent in- and outdegrees with common marginal \(\operatorname{Bin}(m,p)\), hence \(\mathbb E H_{rs}=n w_{rs}\). All entries of \(D\) are positive when \(0<p<1\). The theorem is an exact covariance statement; it makes no claim of a multivariate central limit theorem, of a chi-square distribution for Pearson's statistic, or of a large-dimensional inverse-covariance approximation.

For a fully explicit covariance formula, set

\[
a_r=\Pr\{\operatorname{Bin}(n-2,p)=r\},\quad a_{-1}=a_{n-1}=0,\quad d_r=a_r-a_{r-1},
\]

and define the \(n^2\)-vectors \(u_{rs}=d_rb_s\), \(v_{rs}=b_rd_s\), and \(z_{rs}=d_rd_s\). Then the entire matrix, without matrix inversion or asymptotics, is

\[
\boxed{\Sigma=n(D-ww^{\mathsf T})+n(n-1)pq(uv^{\mathsf T}+vu^{\mathsf T})+n(n-1)p^2q^2zz^{\mathsf T}.}
\]

Here \(w\) denotes the column vector with entries \(w_{rs}\). The conditional degree-binomial probabilities outside their allowed supports are defined to be zero.

## Proof

**1. One-vertex term.** Write \(X_{v,rs}=\mathbf1\{O_v=r,I_v=s\}\). At a fixed vertex, \((O_v,I_v)\) has mass \(w_{rs}\). Hence, for any two cell indices \(a,b\),

\[\operatorname{Cov}(X_{v,a},X_{v,b})=\delta_{ab}w_a-w_aw_b.\]

Summing over the \(n\) vertices gives the term \(n(D-ww^{\mathsf T})\).

**2. Two-vertex term.** For distinct vertices \(i,j\), write \(A=\mathbf1\{i\to j\}\) and \(B=\mathbf1\{j\to i\}\). The remaining out- and in-arc counts for both vertices are four mutually independent \(\operatorname{Bin}(n-2,p)\) variables. Thus, conditional on \(A,B\), the degree-pair indicators at \(i\) and \(j\) are independent. For cell \((r,s)\) at \(i\), the conditional probability is

\[
(a_r-d_rA)(a_s-d_sB)
=w_{rs}-u_{rs}(A-p)-v_{rs}(B-p)+z_{rs}(A-p)(B-p).
\]

At vertex \(j\), the same formula holds with \(A,B\) interchanged. The centered variables \(A-p\), \(B-p\), and \((A-p)(B-p)\) are pairwise orthogonal in \(L^2\), with respective variances \(pq,pq,p^2q^2\). Taking covariance of the two conditional means therefore gives

\[
\operatorname{Cov}(X_{i,a},X_{j,b})=pq(u_av_b+v_au_b)+p^2q^2z_az_b.
\]

There are \(n(n-1)\) ordered pairs of distinct vertices. Adding their contributions proves the displayed exact covariance matrix.

**3. Four mutually orthogonal directions.** Introduce \(e=D^{-1/2}w\), \(U=D^{-1/2}u\), \(V=D^{-1/2}v\), and \(Z=D^{-1/2}z\). Because \(d_r=a_r-a_{r-1}\), telescoping gives \(\sum_r d_r=0\). The binomial identities

\[
\frac{d_r}{b_r}=\frac{mp-r}{mpq},\qquad
\sum_{r=0}^m\frac{d_r^2}{b_r}=\frac1{mpq}
\]

follow by taking the ratios of adjacent binomial coefficients and using \(\operatorname{Var}(\operatorname{Bin}(m,p))=mpq\). These imply that \(e,U,V,Z\) are pairwise orthogonal, and

\[
\|e\|^2=1,\quad \|U\|^2=\|V\|^2=\frac1{mpq},\quad
\|Z\|^2=\frac1{m^2p^2q^2}.
\]

**4. Diagonalization.** Conjugating the exact matrix by \(D^{-1/2}\) yields

\[
C=n(I-ee^{\mathsf T})+nmpq(UV^{\mathsf T}+VU^{\mathsf T})+nmp^2q^2ZZ^{\mathsf T}.
\]

The orthogonality in step 3 gives \(Ce=0\), \(C(U-V)=0\), \(C(U+V)=2n(U+V)\), and \(CZ=(n+n/m)Z=(n^2/m)Z\). Any vector orthogonal to all four of \(e,U,V,Z\) is an eigenvector with eigenvalue \(n\). All four are nonzero and independent for \(m\ge1\), so their orthogonal complement has dimension \(n^2-4\). This proves the full spectrum and rank, including the \(n=2\) coincidence.

The coordinate representations identify the modes: \(e_{rs}=\sqrt{w_{rs}}\); \((U-V)_{rs}=\sqrt{w_{rs}}(s-r)/(mpq)\); \((U+V)_{rs}=\sqrt{w_{rs}}(2mp-r-s)/(mpq)\); and \(Z_{rs}=\sqrt{w_{rs}}(mp-r)(mp-s)/(m^2p^2q^2)\). Finally, for any \(f\), the variance of \(\sum_v f(O_v,I_v)=\sum_{rs}f_{rs}H_{rs}\) is the quadratic form of \(C\) at \(D^{1/2}f\). Its squared Euclidean norm after projecting off \(e\) is \(\sum w_{rs}(f_{rs}-\sum wf)^2=\operatorname{Var}(f(R,S))\). All nonzero eigenvalues lie in \([n,2n]\), proving the stated sharp two-sided bound and its equality examples. \(\square\)

## Verification

The standalone standard-library checker `verify.py` computes all moments as exact rational numbers by enumerating every loopless labeled directed graph on two, three, and four vertices, at \(p=1/3,1/2,2/3\). In all nine parameter settings it compares every cell expectation and every entry of the full covariance matrix with the theorem's formula; this is \(3(2^2+2^6+2^{12})=12{,}492\) weighted graph configurations in all. It separately checks the binomial identities, all four eigenvector equations, and the stated eigenvalues for these settings. These computations check the small-size boundaries and algebra but are not used as a substitute for the all-\(n\), all-\(p\) proof in the preceding section. Run `python3 verify.py` from the extracted self-contained package.

## Relationship to prior work

Goldschmidt and Stephenson, *The scaling limit of a critical random directed graph* (first publicly available May 14, 2019, arXiv:1905.05397), specify exactly the same independent-arc digraph model but study strongly connected components and their scaling limit, not bidegree cell covariances.

Liebenau and Wormald, *Asymptotic enumeration of digraphs and bipartite graphs by degree sequence* (first publicly available June 29, 2020, arXiv:2006.15797), analyze the joint labeled out-/in-degree sequence in the fixed-edge-count ensemble using asymptotic degree-sequence enumeration, including a mean in-/out-degree conservation constraint. Their approximations are not finite-\(n\), unrestricted-\(p\) identities for the covariance of the **cell-count histogram**, and do not give this whitened four-level spectrum.

Lin and Reinert, *Joint Vertex Degrees in an Inhomogeneous Random Graph Model* (arXiv:0912.4812, December 24, 2009), treat dependent **single-degree** counts of an undirected independent-edge graph; their exact and approximate degree-count covariance calculations are important antecedents. In the directed model two independent oppositely oriented arcs couple distinct vertices, producing a signed \(U,V\) correction and an interaction mode \(Z\), rather than the undirected rank-one mechanism. An exact formula for undirected single-degree counts does not imply the two-null-direction, four-level directed bidegree spectrum.

Alarfaj, Taylor and Bogachev, *The joint node degree distribution in the Erdős–Rényi network* (arXiv:2303.05138, March 9, 2023), examine dependence of labeled degrees and goodness-of-fit in the undirected model; they do not analyze the directed bidegree-cell-count covariance spectrum. The present theorem addresses finite second moments only, not a replacement distributional limit or a calibrated chi-square test.

## Limitations

Historical priority is not independently certified: a broader exact random-matrix or digraph degree-sequence identity may contain the same spectrum implicitly. The inspected literature comparisons support distinct scope but do not constitute proof of universal novelty. This result assumes homogeneous, mutually independent directed arcs, no loops, and known probability \(p\in(0,1)\). It does not extend as stated to reciprocal-edge dependence, conditional fixed-edge-count models, or heterogeneous arc probabilities. Singular Pearson standardization at \(p=0,1\) is excluded. Only covariance, spectral decomposition, and variance bounds are established; no Gaussian or chi-square convergence is proved.

## References

1. C. Goldschmidt and R. Stephenson, *The scaling limit of a critical random directed graph*, arXiv:1905.05397 (2019). https://arxiv.org/abs/1905.05397
2. A. Liebenau and N. Wormald, *Asymptotic enumeration of digraphs and bipartite graphs by degree sequence*, arXiv:2006.15797 (2020). https://arxiv.org/abs/2006.15797
3. K. Lin and G. Reinert, *Joint Vertex Degrees in an Inhomogeneous Random Graph Model*, arXiv:0912.4812 (2009). https://arxiv.org/abs/0912.4812
4. B. Alarfaj, C. Taylor, and L. Bogachev, *The joint node degree distribution in the Erdős–Rényi network*, arXiv:2303.05138 (2023). https://arxiv.org/abs/2303.05138
