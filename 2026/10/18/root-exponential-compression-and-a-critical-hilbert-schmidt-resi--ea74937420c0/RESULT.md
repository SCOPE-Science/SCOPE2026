# Root-exponential compression and a critical Hilbert–Schmidt residue for differential Hilbert operators

## Finding
Let \(-1<\alpha<0\). The operator \(\mathcal H_2\) has a complete quasi-Schatten classification between power-weighted Bergman Hilbert spaces: in its bounded parameter range, it belongs to \(\mathcal S_p\) for **every** \(p>0\) exactly when the target weight \(\beta\) satisfies \(\beta>\alpha+2\). More quantitatively, with \(\delta=\beta-\alpha-2>0\), for every integer \(J\ge1\) there is an explicitly constructed rank-\((1+J^2)\) approximant \(Q_J\) with
\[\|\mathcal H_2-Q_J\|\le C_{\alpha,\beta}\left(3^{-J}+2^{-\delta J/2}\right).\]
Consequently the singular values decay at least root-exponentially: \(s_n(\mathcal H_2)\le C'_{\alpha,\beta}e^{-c_{\alpha,\beta}\sqrt n}\). Hence accuracy \(\varepsilon\) is guaranteed with rank \(O_{\alpha,\beta}((\log(1/\varepsilon))^2)\).

The approach to the noncompact boundary is quantified by the exact Hilbert–Schmidt residue
\[\boxed{\lim_{\delta\downarrow0}\delta\,\|\mathcal H_2:A^2_\alpha\to A^2_{\alpha+2+\delta}\|_{\mathcal S_2}^{2}=(\alpha+2)(\alpha+3)B(\alpha+2,-\alpha).}\]
For example, the constant equals \(15\pi/8\) at \(\alpha=-1/2\).

## Assumptions and scope
Use the normalized area measure \(dA(z)=dx\,dy/\pi\) on the unit disk. For \(\gamma>-1\), \(A^2_\gamma\) is the analytic Hilbert space with norm
\[\|f\|_{A^2_\gamma}^{2}=(\gamma+1)\int_{\mathbb D}|f(z)|^2(1-|z|^2)^\gamma dA(z).\]
Its orthonormal basis is \(e_n^{(\gamma)}=z^n/\sqrt{w_n(\gamma)}\), where
\[w_n(\gamma)=\frac{\Gamma(\gamma+2)\Gamma(n+1)}{\Gamma(n+\gamma+2)},\qquad n\in\mathbb N_0.\]
For polynomials set \(\mathcal H_2f(z)=\int_0^1 f(t)/(1-tz)^2\,dt\), extended by continuity when bounded. The theorem concerns \(-1<\alpha<0\), \(\beta>\alpha+2\), real Schatten exponents \(p>0\), and the limit with \(\alpha\) fixed and \(\delta=\beta-\alpha-2\downarrow0\). Here \(s_n\) denotes descending singular values, and \(B\) Euler's beta function.

## Proof
**1. Exact Hilbert-space matrix.** Coefficient integration against \(t^{n+k}\) gives the matrix of \(\mathcal H_2:A^2_\alpha\to A^2_\beta\) in the displayed orthonormal bases:
\[B_{nk}=\frac{(n+1)\sqrt{w_n(\beta)}}{(n+k+1)\sqrt{w_k(\alpha)}}=:\frac{u_n v_k}{n+k+1},\qquad n,k\ge0.\]
Here \(u_n=(n+1)\sqrt{w_n(\beta)}\) and \(v_k=w_k(\alpha)^{-1/2}\) are positive. Gamma-ratio estimates, with constants depending only on the fixed parameters, give
\[u_n^2\le C_{\beta}(n+1)^{1-\beta},\qquad v_k^2\le C_{\alpha}(k+1)^{\alpha+1}.\]
Because \(-1<\alpha<0\), splitting a sum at \(k=n\) shows
\[\sum_{k\ge0}\frac{(k+1)^{\alpha+1}}{(n+k+1)^2}\le C_\alpha(n+1)^\alpha.\]
Therefore the squared Hilbert–Schmidt mass in rows \(n\ge N\), for \(N\ge1\), is bounded by
\[\sum_{n\ge N}\sum_{k\ge0}|B_{nk}|^2\le C_{\alpha,\beta}\sum_{n\ge N}(n+1)^{-1-\delta}\le C'_{\alpha,\beta}N^{-\delta}.\tag{1}\]
In particular the infinite matrix represents a Hilbert–Schmidt operator. This establishes the needed convergence independently of a finite computation.

**2. A certified separated rank approximation.** Retain the row \(n=0\) exactly as one rank-one summand. For each integer \(i=0,\ldots,J-1\), restrict rows to \(2^i\le n<2^{i+1}\), and put \(c_i=3\cdot2^{i-1}\). Uniformly for such \(n\) and every \(k\ge0\),
\[\left|\frac{c_i-n}{k+c_i+1}\right|\le\frac13.\]
On the \(i\)-th row block replace the Cauchy factor by its finite geometric expansion
\[\frac1{n+k+1}\quad\longmapsto\quad \sum_{j=0}^{J-1}\frac{(c_i-n)^j}{(k+c_i+1)^{j+1}}.\tag{2}\]
After multiplication by \(u_n v_k\), every summand in (2) is a rank-one matrix: its row vector has finite support, and its column vector lies in \(\ell^2\) since \(v_k^2/(k+c_i+1)^{2j+2}=O(k^{\alpha-1-2j})\). The total rank, including row zero, is at most \(1+J^2\). Set all rows \(n\ge2^J\) of \(Q_J\) to zero. The exact finite-geometric-series remainder is
\[B_{nk}-(Q_J)_{nk}=B_{nk}\left(\frac{c_i-n}{k+c_i+1}\right)^J\quad(2^i\le n<2^{i+1}).\]
Thus the error on retained rows has Hilbert–Schmidt norm at most \(3^{-J}\|B\|_{\mathcal S_2}\), while omitted rows have Hilbert–Schmidt norm at most \(C_{\alpha,\beta}2^{-\delta J/2}\) by (1). The operator-norm error is no larger than their sum, proving the displayed constructive approximation estimate.

**3. Complete quasi-Schatten range.** The Hilbert-space rank-approximation characterization of singular values gives
\[s_{J^2+2}(\mathcal H_2)\le\|\mathcal H_2-Q_J\|\le C_{\alpha,\beta}\bigl(3^{-J}+2^{-\delta J/2}\bigr).\]
Monotonicity of singular values yields \(s_n\le C'e^{-c\sqrt n}\) for suitable positive constants and all \(n\). Consequently \(\sum_n s_n^p<\infty\) for **every** real \(p>0\). Conversely, any \(\mathcal S_p\) operator is compact. Li and Zhou's boundedness/compactness theorem [1, Theorem 3.1], for the same operator and the indicated Hilbert spaces, excludes compactness at \(\beta=\alpha+2\) and excludes boundedness outside the stated range. This completes the classification in the bounded regime. The operator has infinite rank: any finite square submatrix of the positive Cauchy factor has nonzero Cauchy determinant, and the row/column weights are strictly positive.

**4. Exact critical Hilbert–Schmidt residue.** For fixed \(\alpha\), let \(\beta=\alpha+2+\delta\), where \(0<\delta\le1\). A Riemann-sum calculation, using the gamma-ratio asymptotic for \(w_k(\alpha)^{-1}\), gives
\[\sum_{k\ge0}\frac{1}{w_k(\alpha)(n+k+1)^2}\sim\frac{B(\alpha+2,-\alpha)}{\Gamma(\alpha+2)}(n+1)^\alpha.\tag{3}\]
The integral is finite: its integrand is \(t^{\alpha+1}(1+t)^{-2}\), integrable both at zero and infinity precisely in the relevant range \(-1<\alpha<0\). The gamma-ratio expansion
\[(n+1)^2w_n(\alpha+2+\delta)=\Gamma(\alpha+4+\delta)(n+1)^{-1-\alpha-\delta}(1+o(1))\]
is uniform for \(\delta\) in a compact interval containing zero. Combining it with (3) yields, uniformly in \(\delta\in[0,1]\),
\[\sum_{k\ge0}|B_{nk}|^2 = C_\alpha(\delta)(n+1)^{-1-\delta}(1+o(1)),\quad C_\alpha(\delta)=\frac{\Gamma(\alpha+4+\delta)}{\Gamma(\alpha+2)}B(\alpha+2,-\alpha).\tag{4}\]
The finitely many initial rows contribute negligibly after multiplication by \(\delta\). For the remaining rows the uniform \(o(1)\) in (4), together with \(\delta\sum_{n\ge1}(n+1)^{-1-\delta}\to1\), justifies passage to the limit. It is \(C_\alpha(0)=(\alpha+2)(\alpha+3)B(\alpha+2,-\alpha)\), as claimed.

## Verification
The geometric remainder in (2) is an exact identity, and the tail summation in (1) is over the entire infinite row set. A supplied standalone checker evaluates finite coefficient matrices with three representative target weights and tests the rank-block approximation for four dyadic cutoffs; the pointwise retained-row error and the total finite-matrix error obey the derived bounds. Numerical agreement does not certify the infinite-rank or limiting conclusions, which are established in the proof. The critical constant at \(\alpha=-1/2\) is \(15\pi/8\) by the beta identity.

## Relationship to prior work
Li and Zhou [1, Theorems 3.1 and 4.2] established the bounded/compact parameter range and membership in \(\mathcal S_p\) for \(p\ge1\), and [1, Theorem 4.4] gives an exact double series for the Hilbert–Schmidt norm. Those conclusions and the coefficient-matrix representation are acknowledged as prior work. The additional results here are a concrete infinite-matrix separated-rank construction, the resulting \(0<p<1\) classification and root-exponential approximation guarantee, and an explicit coefficient for the singular approach to the compactness boundary. Beckermann and Townsend [2, Section 4.2] proved dimension-dependent singular-value estimates for finite structured Cauchy matrices; these motivate the separated-rank perspective but do not state the present infinite-space row-tail bound or boundary residue. The compression method is not claimed to be new in the class of all analytic Cauchy kernels.

## Limitations
The root-exponential estimate is an upper bound; its exponent and decay constant are not proved optimal. The quasi-Schatten conclusion does not give exact singular values. The critical norm residue is proved only for the Hilbert–Schmidt exponent, not every Schatten exponent. The result assumes a fixed real \(-1<\alpha<0\), power-weighted Bergman Hilbert spaces, and the specific differential Hilbert kernel. Similar results for other Hilbert-type kernels are not claimed. Publication priority beyond the inspected sources is subject to further verification.

## References
[1] S. Li and M. Zhou, *The Differential Hilbert Operator Between Weighted Bergman Spaces*, arXiv:2610.05672, first submitted 5 October 2026, https://arxiv.org/abs/2610.05672 . In particular, the full-text Sections 2–4, Theorems 3.1, 4.2, and 4.4.

[2] B. Beckermann and A. Townsend, *On the singular values of matrices with displacement structure*, arXiv:1609.09494 (2016); *SIAM Journal on Matrix Analysis and Applications* 38 (2017), 1227–1248, https://arxiv.org/abs/1609.09494 . In particular, the full-text Section 4.2 and Corollary 7.
