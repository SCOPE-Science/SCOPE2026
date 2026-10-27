# Rank-sensitive moment frontiers for Gaussian-sketched Householder QR

## Finding
For the block-preserving Gaussian sketch underlying reconstructed randomized Householder QR, the existence of unconditional Euclidean basis moments depends **exactly on the rank of the unsketched leading input block**, rather than on its positive singular values. Let \(r\) denote that rank, let \(m\) be the number of columns, let \(\ell>m\) be the number of Gaussian rows, and put \(k=m-r\). For the reconstructed basis \(Q\) defined below, if \(k>0\) and \(p>0\), then
\[
\mathbb E\|Q\|_2^p<\infty\quad\Longleftrightarrow\quad p<\ell-k+1,
\]
and
\[
\mathbb E\|Q^{\mathsf T}Q-I_m\|_2^p<\infty\quad\Longleftrightarrow\quad 2p<\ell-k+1.
\]
At the indicated equalities the moments diverge. If \(k=0\), **all** positive-order moments in both displays are finite (indeed, both quantities are deterministically bounded). The same moment cutoff holds for \(\|Q\|_F\). These are exact moment-existence criteria, not assertions that a failure is typical.

For example, with the minimally oversampled choice \(\ell=m+1\), a zero leading block gives an infinite mean Euclidean Gram defect, whereas a leading block of rank one makes that mean finite. Even an arbitrarily small nonzero leading singular value changes the integrability threshold; the finite moment may, however, become arbitrarily large as that singular value tends to zero.

## Assumptions and scope
Work in real exact arithmetic. Fix integers \(m\ge2\), \(\ell>m\), and \(n\ge2m\). Let \(W\in\mathbb R^{n\times m}\) have orthonormal columns and partition it as
\[
W=\begin{bmatrix}B\\ C\end{bmatrix},\qquad B\in\mathbb R^{m\times m},\qquad C\in\mathbb R^{(n-m)\times m},\qquad W^{\mathsf T}W=I_m.
\]
Assume \(\|B\|_2<1\), so \(C\) has full column rank and the source's simultaneous-factorization hypotheses hold. Draw an independent Gaussian sketch \(\Omega\in\mathbb R^{\ell\times(n-m)}\) with entries distributed as \(N(0,1/\ell)\). Form the *block-preserving* sketch
\[
\Psi=\operatorname{diag}(I_m,\Omega),\qquad Z=\Psi W=\begin{bmatrix}B\\ \Omega C\end{bmatrix}.
\]
Almost surely \(Z\) has full column rank. Take its unpivoted thin QR factorization \(Z=\widetilde Q R\) with positive diagonal of \(R\), and reconstruct the exact input factor \(Q=WR^{-1}\). This is the algebraic basis factor of the sketched/recRHQR construction; \(\Psi Q\) is orthonormal, while \(Q\) need not be Euclidean-orthonormal. The theorem concerns these exact factors only, not roundoff error or a finite-precision software implementation.

## Proof
**1. QR norm reduction.** Because \(W^{\mathsf T}W=I_m\), the singular values of \(Q=WR^{-1}\) are those of \(R^{-1}\). From \(R^{\mathsf T}R=Z^{\mathsf T}Z\),
\[
\|Q\|_2=\frac{1}{\sigma_{\min}(Z)}.
\]
Also \(\|Q\|_2\le\|Q\|_F\le\sqrt m\,\|Q\|_2\), so the operator and Frobenius norms have identical positive-moment integrability criteria.

**2. Deterministic regularization leaves a Gaussian null block.** Choose a right orthogonal coordinate change diagonalizing \(B^{\mathsf T}B\). Since \(C^{\mathsf T}C=I_m-B^{\mathsf T}B\), the corresponding \(m\) Gaussian columns of \(\Omega C\) become independent, with variances determined by the diagonal entries of \(C^{\mathsf T}C\). Further left orthogonal changes (which preserve singular values) put \(Z\) in the form
\[
\mathcal Z=\begin{bmatrix}D&0\\ U&G\end{bmatrix},
\]
with \(D\in\mathbb R^{r\times r}\) invertible, \(U\in\mathbb R^{\ell\times r}\) Gaussian (possibly with distinct column scales), and \(G\in\mathbb R^{\ell\times k}\) independent of \(U\), with independent \(N(0,1/\ell)\) entries. Zero top rows have been suppressed. This representation also covers \(r=0\), when only \(G\) remains.

For \(k>0\), choosing a unit vector supported in the \(k\)-dimensional null block gives
\[
\sigma_{\min}(\mathcal Z)\le\sigma_{\min}(G).
\]
If \(r>0\), write \(\delta=\sigma_{\min}(D)>0\). For every pair \((a,b)\), the block form implies
\[
\|a\|\le\delta^{-1}\|\mathcal Z(a,b)\|,
\quad
\|b\|\le\sigma_{\min}(G)^{-1}(1+\|U\|_2/\delta)\|\mathcal Z(a,b)\|.
\]
Consequently,
\[
\sigma_{\min}(G)^{-1}\le \sigma_{\min}(\mathcal Z)^{-1}
\le\delta^{-1}+(1+\|U\|_2/\delta)\sigma_{\min}(G)^{-1}.
\]
For \(r=0\) these reduce to equality between the singular values of \(\mathcal Z\) and \(G\). Since \(U\) and \(G\) are independent and \(U\) has finite moments of every order, the existence or divergence of moments of \(\sigma_{\min}(\mathcal Z)^{-1}\) is exactly that for \(\sigma_{\min}(G)^{-1}\).

**3. Sharp Gaussian singular-value moment criterion.** Let \(G\) have \(\ell\) rows and \(k\ge1\) columns, with \(\ell\ge k\). Gaussian Gram–Schmidt produces a triangular factor with independent diagonal entries having the laws \(\chi_{\ell-j+1}/\sqrt\ell\) at steps \(j=1,\ldots,k\); the strictly upper triangular entries are independent Gaussian variables. The final reciprocal diagonal is a lower bound for the inverse triangular operator norm. Thus its \(p\)-moment diverges whenever \(p\ge\ell-k+1\). Conversely, every entry of the inverse triangular matrix is a finite sum of products involving Gaussian off-diagonal entries and reciprocals of distinct chi diagonals; all these products have finite \(p\)-moment for \(p<\ell-k+1\). In fixed dimension, entrywise moments control the operator norm. Therefore
\[
\mathbb E\sigma_{\min}(G)^{-p}<\infty
\quad\Longleftrightarrow\quad p<\ell-k+1.
\]
Steps 1–3 prove the first asserted equivalence.

**4. Gram defect and full anchoring.** Let \(H=Q^{\mathsf T}Q-I_m\). Its eigenvalues are the squared singular values of \(Q\) minus one; hence
\[
\|Q\|_2^2-1\le\|H\|_2\le\|Q\|_2^2+1.
\]
On the event \(\|Q\|_2^2\ge2\), the left side is at least \(\|Q\|_2^2/2\). Therefore the \(p\)-moment of \(\|H\|_2\) is finite exactly when the \(2p\)-moment of \(\|Q\|_2\) is finite. If \(r=m\), the deterministic first block already gives \(\sigma_{\min}(Z)\ge\sigma_{\min}(B)>0\) for every sketch, so the stated norms are bounded. This completes the proof, including both critical equalities.

## Verification
A standalone checker (`verify.py`) forms the actual block sketch, performs independent dense QR factorization, reconstructs \(Q\), and checks the factor identity, sketch orthogonality, and the equality between the factor norm and reciprocal smallest singular value. It tests anchored ranks \(0\) through \(m\), rotated as well as diagonal input blocks, and the exact unanchored chi-square product law underlying the proof. The executable reported **3,937 passed checks**. These finite tests validate formulas and implementations; the all-dimension and moment-divergence assertions rest on the analytical argument above.

A revealing boundary family has \(m=3\), \(\ell=4\), and \(B=\operatorname{diag}(\beta_1,\ldots,\beta_r,0,\ldots,0)\), with \(0<\beta_i<1\) and \(C\) chosen so that \(W\) has orthonormal columns. As \(r=0,1,2,3\), the basis-norm critical exponents are, respectively, \(2,3,4,\infty\). Thus the mean Gram defect diverges at \(r=0\) and is finite at every \(r\ge1\). No finite simulation can itself demonstrate an infinite expectation.

## Relationship to prior work
Grigori and Timsit introduced the block-preserving randomized Householder sketch and the recRHQR reduction to Householder QR of the sketch. Their Theorem 3.7 and Section 3.3 provide the factorization identity used here; their embedding and finite-precision results address high-probability conditioning and backward stability, rather than the exact unconditional moment cutoff classified here. Balabanov and Grigori's randomized Gram–Schmidt analysis supplies the earlier high-probability embedding framework. Standard Gaussian QR/Bartlett and inverse-Wishart theory supplies the singular-value ingredients; those ingredients are not claimed as new. The rank-sensitive cutoff for the specific partially deterministic sketch is the assessed consequence. This is **not** a novel claim about general Gaussian QR or about QR backward stability.

## Limitations
The model uses a fixed orthonormal input, Gaussian bottom-block sketches, a fixed column count, and exact arithmetic. It says nothing about frequency of large conditioning errors in realistic oversized sketches, numerical rounding behavior, non-Gaussian sketches, or actual solver convergence. Large finite moments may coexist with poor practical conditioning if the nonzero singular values of the leading block are very small. The novelty assessment is self-review only; publication priority, including potentially equivalent partial-Gaussian smallest-singular-value results, has not been independently established.

## References
1. L. Grigori and E. Timsit, *Randomized Householder QR*, first HAL version stated by the authors as public 2023-07-07, HAL hal-04156310; arXiv:2405.10923 (2024), Sections 1, 3.1, 3.3, 4.
2. O. Balabanov and L. Grigori, *Randomized Gram–Schmidt process with application to GMRES*, arXiv:2011.05090 (2020); SIAM Journal on Scientific Computing 44 (2022), A1450–A1474.
3. Y. Jang and L. Grigori, *Randomized Orthogonalization Process With Reorthogonalization*, Numerical Linear Algebra with Applications 32 (2025), e70029, doi:10.1002/nla.70029 (related contrast with Euclidean reorthogonalization).
4. W. Anderson and M. Wells, *The Exact Distribution of the Condition Number of a Gaussian Matrix*, SIAM Journal on Matrix Analysis and Applications, doi:10.1137/070698932 (background on Gaussian singular-value laws).
