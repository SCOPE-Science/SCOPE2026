# Layered order polytopes approach the cube isotropic constant with a universal logarithmic defect

## Finding

Let \(k\ge2\) be fixed and let \(m_1,\ldots,m_k\ge1\) be integers, with \(n=\sum_{i=1}^k m_i\). Write \(A_{m_i}\) for an antichain of size \(m_i\) and consider the ordinal-sum poset \(P=A_{m_1}\oplus\cdots\oplus A_{m_k}\). Its standard order polytope \(K=\mathcal O(P)\) consists of vectors in \([0,1]^n\) for which every coordinate in layer \(i\) is no greater than every coordinate in each later layer.

For the uniform distribution on \(K\), denote the positive definite covariance matrix by \(\Sigma\), and define the affine-invariant isotropic constant by
\[
 L_K^{2n}=\frac{\det\Sigma}{\operatorname{vol}_n(K)^2}.
\]
The following statements hold.

**Exact all-layer covariance determinant.** Put \(s_i=m_1+\cdots+m_{i-1}\), \(I_i=\{s_i+1,\ldots,s_i+m_i\}\), and
\[
 c_{rs}=\frac{\min(r,s)\,[n+1-\max(r,s)]}{(n+1)^2(n+2)}\qquad(1\le r,s\le n).
\]
Construct the \(k\times k\) matrix
\[
 B_{ij}=\frac1{\sqrt{m_i m_j}}\sum_{r\in I_i}\sum_{s\in I_j}c_{rs}.
\]
Then
\[
 \boxed{\operatorname{vol}_n(K)=\frac{\prod_{i=1}^k m_i!}{n!},\qquad
 \det\Sigma=(\det B)\prod_{i=1}^k
 \left(\frac{(m_i+1)(m_i+2)}{12(n+1)(n+2)}\right)^{m_i-1}.}
\]
The empty exponent is interpreted as one when \(m_i=1\). Thus an exact \(n\)-dimensional determinant reduces to \(k\) explicit finite sums and one \(k\)-dimensional determinant.

**Fixed-layer asymptotic.** Suppose \(k\) stays fixed, \(n\to\infty\), and \(m_i/n\to\alpha_i>0\), with \(\sum_i\alpha_i=1\). Define \(a_i=\sum_{j<i}\alpha_j\), \(\mu_i=a_i+\alpha_i/2\), and the positive definite \(k\times k\) matrix
\[
 C_{ij}=\sqrt{\alpha_i\alpha_j}\left(\mu_{\min(i,j)}[1-\mu_{\max(i,j)}]-\frac{\alpha_i}{6}\mathbf1_{\{i=j\}}\right).
\]
Then, with
\[
 \gamma_k(\alpha)=3(k-1)-(k-1)\log(2\pi)+k\log12+\log\det C
 -3\sum_{i=1}^k\log\alpha_i,
\]
one has the **sharp two-scale expansion**
\[
 \boxed{n\log(12L_K^2)=-(k-1)\log n+\gamma_k(\alpha)+o(1).}
\]
In particular, \(L_K\to1/\sqrt{12}\) and \(L_K<1/\sqrt{12}\) for every sufficiently large \(n\) along each such sequence. The coefficient \(k-1\) counts the interfaces between antichain layers, independent of the proportions and widths.

**Explicit two-layer version.** For \(k=2\), write \(p=m_1\), \(q=m_2\), \(n=p+q\), and \(\alpha=p/n\), \(\beta=q/n\). For every positive \(p,q\),
\[
 \boxed{\det\Sigma=
 \left(\frac{(p+1)(p+2)}{12(n+1)(n+2)}\right)^{p-1}
 \left(\frac{(q+1)(q+2)}{12(n+1)(n+2)}\right)^{q-1}
 \frac{(p+1)(q+1)(2pq+n+2)}{72(n+1)^2(n+2)^2}.}
\]
When \(p/n\to\alpha\in(0,1)\), the constant simplifies to
\[
 \boxed{n\log(12L_K^2)+\log n\longrightarrow
 3+\log\frac{2}{\pi\alpha(1-\alpha)}.}
\]

## Assumptions and scope

The ambient metric is standard Euclidean and all volumes and covariances use the full \(n\)-dimensional affine hull. Coordinates in each layer are distinct labels but are pairwise incomparable. The order inequalities are weak; measure-zero ties do not affect the probability argument. Exact formulas permit every positive layer size. The asymptotic requires **a fixed number of layers and each limiting proportion strictly positive**. No assertion is made for a number of layers growing with \(n\), or for a layer of negligible proportional size.

## Proof

**Step 1: Uniform rank allocation and volume.** Stanley's canonical triangulation partitions the unit cube into \(n!\) congruent simplices indexed by permutations of its coordinate ranks. Exactly \(\prod_i m_i!\) permutations respect the ordinal-sum comparisons. Consequently \(\operatorname{vol}_n(K)=\prod_i m_i!/n!\). Equivalently, choose \(n\) independent uniform random variables on \([0,1]\), sort them into \(U_{(1)}\le\cdots\le U_{(n)}\), and independently assign the consecutive rank block \(I_i\) to the \(m_i\) labeled positions of layer \(i\) by a uniform random bijection. This construction is the uniform distribution on \(K\).

**Step 2: Order-statistic covariance and contrasts.** For \(1\le r,s\le n\), the beta-spacing calculation gives
\[
 \mathbb E U_{(r)}=\frac r{n+1},\qquad
 \operatorname{Cov}(U_{(r)},U_{(s)})=c_{rs}.
\]
Alternatively, for \(r\le s\), \(\mathbb E[U_{(r)}U_{(s)}]=r(s+1)/[(n+1)(n+2)]\). The coordinate covariance is invariant under the permutation group within each layer. Its \(m_i-1\)-dimensional within-layer contrast subspace therefore has a scalar eigenvalue \(\lambda_i\). Choosing two distinct coordinates in layer \(i\), the expected squared difference, averaged over all distinct ranks from \(I_i\), is
\[
 \mathbb E[(X_{i,1}-X_{i,2})^2]
 =\frac{1}{m_i(m_i-1)(n+1)(n+2)}
 \sum_{r\ne s\in I_i}|r-s|(|r-s|+1)
 =\frac{(m_i+1)(m_i+2)}{6(n+1)(n+2)}.
\]
Here the last equality follows by summing the \(m_i-d\) unordered pairs at each gap \(d=1,\ldots,m_i-1\). As the squared difference has expectation \(2\lambda_i\), this gives \(\lambda_i=(m_i+1)(m_i+2)/[12(n+1)(n+2)]\). A one-element layer has no contrast direction and needs no use of that formula.

**Step 3: Group means.** Define the layer mean \(A_i=m_i^{-1}\sum_{a=1}^{m_i}X_{i,a}\). Given the order statistics, \(A_i=m_i^{-1}\sum_{r\in I_i}U_{(r)}\) exactly, irrespective of the random allocation. Therefore \(\operatorname{Cov}(\sqrt{m_i}A_i,\sqrt{m_j}A_j)=B_{ij}\). The orthogonal decomposition of \(\mathbb R^n\) into its \(k\) normalized group-constant directions and all within-group contrast subspaces diagonalizes \(\Sigma\) into the block \(B\) and the scalar blocks \(\lambda_i I_{m_i-1}\). Multiplying determinants establishes the exact identity.

**Step 4: Continuous Brownian-bridge covariance and its positivity.** For \(r/(n+1)\to u\) and \(s/(n+1)\to v\), the order-statistic covariance satisfies
\[
 n c_{rs}\longrightarrow \min(u,v)-uv.
\]
The preceding double sums, with \(m_i/n\to\alpha_i>0\), are Riemann sums over the disjoint adjacent intervals \([a_i,a_i+\alpha_i]\). Thus \(B\to C\), where the average of the Brownian-bridge kernel over different intervals is \(\mu_i(1-\mu_j)\) for \(i<j\), and the average over one interval is \(\mu_i(1-\mu_i)-\alpha_i/6\). To establish strict positive definiteness, write the quadratic form as the variance of a nonzero step-function integral against a standard Brownian bridge. For completeness, if \(f\) is a step function on these intervals and \(W\) is Brownian motion, the random integral of \(f(t)[W(t)-tW(1)]\) equals an Itô integral with integrand \(g(s)=\int_s^1 f(t)\,dt-\int_0^1 t f(t)\,dt\). Zero variance forces \(g=0\) almost everywhere; differentiating gives \(f=0\). Thus the Brownian-bridge covariance kernel is strictly positive on the span of the nonzero, linearly independent interval indicators. Hence \(C\) is positive definite and \(\log\det B\to\log\det C\).

**Step 5: Expand the determinant and volume, retaining all constant terms.** Put \(a_i^{(n)}=m_i/n\). Uniformly as the \(a_i^{(n)}\) remain in a compact subinterval of \((0,1)\), elementary Taylor expansion yields
\[
 \log(12\lambda_i)=2\log a_i^{(n)}
 +\frac3n\left(\frac1{a_i^{(n)}}-1\right)+O(n^{-2}).
\]
Stirling's formula yields
\[
 2\log\operatorname{vol}_n(K)=2n\sum_i a_i^{(n)}\log a_i^{(n)}
 +(k-1)\log(2\pi n)+\sum_i\log a_i^{(n)}+o(1).
\]
Consequently
\[
 \sum_i(m_i-1)\log(12\lambda_i)
 =2n\sum_i a_i^{(n)}\log a_i^{(n)}
 -2\sum_i\log a_i^{(n)}+3(k-1)+o(1).
\]
Using \(n\log(12L_K^2)=n\log12+\log\det\Sigma-2\log\operatorname{vol}_n(K)\) and the exact determinant factorization now proves the displayed expansion. Since \(k-1>0\), the logarithmic negative term eventually dominates the bounded constant and proves the strict cube comparison.

**Step 6: Two-layer evaluation.** For two groups, direct substitution of the finite rank blocks into the \(2\times2\) determinant yields
\[
 \det B=\frac{(p+1)(q+1)(2pq+n+2)}{72(n+1)^2(n+2)^2}.
\]
For \(\alpha+\beta=1\), the continuous matrix has \(\det C=\alpha^2\beta^2/36\); substituting this in the constant from Step 5 reduces it to \(3+\log[2/(\pi\alpha\beta)]\).

## Verification

The included standalone Python program `verify.py` uses exact rational arithmetic to compare direct covariance-matrix entries against an independent full enumeration of admissible rank allocations for eleven small multilayer profiles, and to compare full determinants with the block factorization. For each two-layer test it additionally checks the closed formula symbolically over the rationals. Nine two-layer and seven multilayer numerical comparisons test the asymptotic constants at several sizes, including dimensions above two thousand. All executed assertions passed. These finite checks corroborate, but do not replace, Steps 1–6, which apply to arbitrary valid dimensions and to the stated limits.

## Relationship to prior work

Stanley's canonical triangulation and order-polytope framework provide the volume/rank starting point. Fang, Fourier and Pegel study marked poset-polytope decomposition and reflexivity, not uniform Euclidean covariance or the isotropic constant. Can and Hibi identify an affine free-sum description of ordinal-sum order polytopes and investigate associated toric-code parameters; their free-sum lemma is explicitly incorporated in the comparison but is not a covariance-determinant calculation. Kipp studies isotropic-constant extremizers of regular polytopes, including centrally symmetric cases, but provides no order-polytope layered asymptotics. The previously established isotropic bounds for centrally symmetric Hanner polytopes do not directly cover this family: even the two-singleton case is a triangle and not centrally symmetric. A separate existing result computes the exact spherical mean width of the same two-layer standard order polytope; that support-function average does not determine an interior uniform covariance determinant. The claimed contribution is precisely the exact all-layer uniform covariance determinant and its interface-count logarithmic isotropic-constant defect.

## Limitations

The limit is established only for fixed \(k\) and proportions bounded away from zero. Neither a growing-layer theory nor finite-dimensional sign thresholds for the isotropic-constant comparison are claimed. The originality check cannot rule out every possible equivalent theorem expressed in the language of free joins, Dirichlet mixtures or Gaussian bridges. Independent external verification has not been performed.

## References

1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23. DOI: 10.1007/BF02187680.
2. X. Fang, G. Fourier, C. Pegel, *The Minkowski Property and Reflexivity of Marked Poset Polytopes*, Electronic Journal of Combinatorics 27(1) (2020), P1.27. First public version 2018-07-11, arXiv:1807.03970. Primary MSC 52B20.
3. M. Bilen Can, T. Hibi, *Toric Codes from Order Polytopes*, first public version 2021-02-06, arXiv:2102.03651. See §5, especially Lemma 5.1 on ordinal sums and free sums.
4. C. Kipp, *Isotropic Constants and Regular Polytopes*, first public version 2024-07-01, arXiv:2407.01353. See introductory definition and extremal theorems.
