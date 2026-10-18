# A logarithmic-Laplacian spectral limit for critical discrete HLS path matrices

## Finding
For every integer \(N\ge2\), let \(A_N\) be the real symmetric matrix with \((A_N)_{ii}=0\) and \((A_N)_{ij}=1/|i-j|\) for distinct indices in \(\{1,\ldots,N\}\). Write \(\lambda_N\) for its largest eigenvalue, and \(v_N\) for its unique positive, Euclidean-unit Perron vector. Let \(I_{N,j}=((j-1)/N,j/N)\) and define \(f_N(x)=\sqrt N\,(v_N)_j\) on \(I_{N,j}\).

For a function \(f\in L^2(0,1)\), extended by zero to the real line, let \(\widehat f(s)=\int_0^1 f(x)e^{-isx}\,dx\). Define the logarithmic form domain and quadratic functional by
\[
\mathcal D=\left\{f\in L^2(0,1):\int_{\mathbb R}\log(2+|s|)|\widehat f(s)|^2\,ds<\infty\right\},\qquad
\mathcal B(f)=-\frac1\pi\int_{\mathbb R}\log|s|\,|\widehat f(s)|^2\,ds.
\]
The integral is finite for \(f\in\mathcal D\); the singularity at zero is harmless because \(|\widehat f(s)|\le\|f\|_1\). Set
\[
\Lambda=\max_{\substack{f\in\mathcal D\\\|f\|_2=1}}\mathcal B(f).
\]
Then
\[
\boxed{\lambda_N=2\log N+\Lambda+o(1)},\qquad
\boxed{f_N\longrightarrow f_*\ \text{strongly in }L^2(0,1)},
\]
where \(f_*\) is the unique nonnegative unit maximizer of \(\mathcal B\). Equivalently, \(\Lambda=-\lambda_1^L((0,1))\), with \(\lambda_1^L\) the first zero-exterior Dirichlet eigenvalue of the logarithmic Laplacian, normalized by the Fourier multiplier \(2\log|s|\). The existence, positivity, and simplicity of this continuum eigenfunction are known results, not new claims.

There is also an exact all-\(N\) identity underlying the limiting theorem. For each \(u\in\mathbb C^N\), extend \(u\) by zero to \(\mathbb Z\), and let \(F_Nu=\sqrt N u_j\) on \(I_{N,j}\). Put \(0\log0=0\) and
\[
c_k=(k+1)\log(k+1)+(k-1)\log(k-1)-2k\log k,\qquad d_k=c_k-\frac1k\quad(k\ge1).
\]
Then \(d_k>0\), \(d_k=1/(6k^3)+O(k^{-5})\), and \(\sum_{k\ge1}d_k=1-\gamma\), where \(\gamma\) is Euler's constant. For every unit \(u\),
\[
\boxed{\langle u,A_Nu\rangle-2\log N
=\mathcal B(F_Nu)+\sum_{k=1}^{\infty}d_k\sum_{j\in\mathbb Z}|u_{j+k}-u_j|^2.}
\]
The identity holds for every complex vector, and its remainder is nonnegative.

## Assumptions and scope
All Fourier transforms use the unnormalized convention specified above; Plancherel therefore includes the factor \(1/(2\pi)\). Matrix indices start at one. The logarithmic Laplacian is defined by the Fourier multiplier \(2\log|s|\) with zero extension outside \((0,1)\); using a different Fourier convention or a shifted logarithmic operator changes the additive spectral constant. Only \(N\to\infty\) through integers is asserted. The eigenvectors are normalized to have unit Euclidean norm and strictly positive entries; the histogram is consequently unit in \(L^2(0,1)\).

## Proof
**1. Logarithmic form and its cell matrix.** On compactly supported smooth functions, Fourier inversion of the logarithmic multiplier yields
\[
\mathcal B(f)=2\gamma\|f\|_2^2+\int_0^1\log(x(1-x))|f(x)|^2\,dx
-\frac12\int_0^1\!\int_0^1\frac{|f(x)-f(y)|^2}{|x-y|}\,dx\,dy.
\tag{1}
\]
This identity is obtained by truncating the off-diagonal kernel at separation \(\varepsilon\), using the standard distributional identity \(\lim_{\varepsilon\downarrow0}[2\int_\varepsilon^\infty\cos(sh)\,dh/h+2\log\varepsilon]=-2\gamma-2\log|s|\), and cancelling the diagonal logarithmic divergence. It extends to the stated form domain by smooth approximation; in particular it applies to finite step functions. For a unit indicator of an interval of length \(1/N\), dilation in the Fourier representation gives the diagonal quadratic-form value \(2\gamma-2-2\log N\). The cross-cell bilinear value at separation \(k\ge1\) is
\[
N\int_{I_{N,1}}\!\int_{I_{N,1+k}}\frac{dx\,dy}{|x-y|}
=\int_0^1\!\int_0^1\frac{ds\,dt}{k+s-t}=c_k.
\]
Thus, for arbitrary \(u\in\mathbb C^N\),
\[
\mathcal B(F_Nu)=(2\gamma-2-2\log N)\|u\|_2^2
+2\sum_{k=1}^{N-1}c_k\operatorname{Re}\sum_{j=1}^{N-k}\overline{u_j}u_{j+k}.\tag{2}
\]

**2. The exact positive remainder.** Convexity of the reciprocal on positive arguments and the symmetric triangular distribution of \(s-t\) show \(c_k>1/k\); the potentially singular corner when \(k=1\) is integrable. Taylor expansion gives \(d_k=1/(6k^3)+O(k^{-5})\). Telescoping the second differences of \(k\log k\) yields
\[
\sum_{k=1}^{m}d_k=(m+1)\log(m+1)-m\log m-H_m\longrightarrow1-\gamma,
\]
where \(H_m=\sum_{k=1}^m 1/k\). With zero-extended \(u\), the elementary polarization identity is
\[
\sum_{j\in\mathbb Z}|u_{j+k}-u_j|^2
=2\|u\|_2^2-2\operatorname{Re}\sum_{j\in\mathbb Z}\overline{u_j}u_{j+k}.
\]
Subtracting (2) from the quadratic form of \(A_N-2\log N\) proves the boxed identity, including nonnegativity and convergence of its series. Denote its remainder by \(E_N(u)\); then \(0\le E_N(u)\le4(1-\gamma)\|u\|_2^2\).

**3. Compactness of near-extremizers.** For \(f\) supported in \([0,1]\) with \(\|f\|_2=1\), one has \(|\widehat f(s)|\le1\). Hence the positive-frequency contribution from \(|s|<1\) to \(\mathcal B(f)\) is uniformly bounded. If \(\mathcal B(f)\ge-C\), it follows that
\[
\int_{|s|>1}\log|s|\,|\widehat f(s)|^2\,ds\le C'
\]
with \(C'\) independent of \(f\). Consequently its Fourier mass above \(R>1\) is at most \(C'/\log R\). This uniform tail bound controls translation moduli in \(L^2(\mathbb R)\); common compact support gives relative compactness by the Fréchet–Kolmogorov theorem. The same argument proves upper semicontinuity of \(\mathcal B\) under strongly convergent bounded-below sequences: the low-frequency integral converges by Plancherel and boundedness of the logarithmic kernel near zero, while the negative high-frequency term is lower semicontinuous by Fatou.

The constant unit vector gives
\[
\lambda_N\ge2H_{N-1}-\frac{2(N-1)}N
=2\log N+2\gamma-2+o(1).
\]
Apply the exact identity to \(u=v_N\): since \(E_N(v_N)\le4(1-\gamma)\), the sequence \(\mathcal B(f_N)\) is bounded below. By compactness, every subsequence of \(f_N\) has an \(L^2\)-convergent further subsequence with unit limit \(f\in\mathcal D\).

**4. Disappearance of the discrete remainder.** If \(f_{N_j}\to f\) strongly in \(L^2\), then for each fixed \(k\ge1\), using zero extension,
\[
\sum_{\ell\in\mathbb Z}|(v_{N_j})_{\ell+k}-(v_{N_j})_{\ell}|^2
=\|f_{N_j}(\cdot+k/N_j)-f_{N_j}\|_{L^2(\mathbb R)}^2\longrightarrow0.
\]
Every term is bounded by four. Dominated convergence against the summable positive \(d_k\) proves \(E_{N_j}(v_{N_j})\to0\). Upper semicontinuity therefore gives
\[
\limsup_j(\lambda_{N_j}-2\log N_j)\le\mathcal B(f)\le\Lambda.
\]

**5. Matching lower bound and identification.** The smooth test space \(C_c^\infty(0,1)\) is dense in \(\mathcal D\) for the Fourier-weighted norm \(\int\log(2+|s|)|\widehat f(s)|^2ds\): first compress and translate the support into a smaller closed subinterval, then mollify. These operations converge in the logarithmic Fourier norm by change of variables and dominated convergence. For every smooth compactly supported unit \(g\), let \(P_Ng\) be its cell-average step approximation and normalize it. The approximation converges in every fractional Sobolev \(H^t(\mathbb R)\) with \(0<t<1/2\), hence in \(\mathcal D\); one may verify this with the Gagliardo double integral and the \(O(N^{-1})\) cell-oscillation bound. Thus \(\mathcal B(P_Ng)\to\mathcal B(g)\), and the same fixed-shift argument as in step 4 gives \(E_N(P_Ng)\to0\). The maximum Rayleigh principle and the exact identity show
\[
\liminf_N(\lambda_N-2\log N)\ge\mathcal B(g).
\]
Density and maximization over \(g\) give \(\liminf\ge\Lambda\). Combined with step 4 this proves the constant limit. Every cluster point \(f\) attains \(\Lambda\); since the matrix eigenvectors are positive, \(f\) is nonnegative. The known strict positivity and simplicity of the first Dirichlet logarithmic-Laplacian eigenfunction (Chen–Weth, Theorem 1.4) identify the cluster point uniquely as \(f_*\). Relative compactness therefore upgrades subsequential convergence to convergence of the entire sequence.

## Verification
The accompanying `verify.py` is a standard-library-only checker. It compares the exact finite cell-form decomposition against direct matrix Rayleigh forms for several deterministic real and complex vectors, verifies telescoping and positivity for a finite range of \(d_k\), and computes selected Perron eigenvalues numerically. It is an independent implementation check of normalization and finite algebra only. It does not certify the continuum limit; that follows from the compactness and density arguments above. Run from the directory containing the artifact with `python3 verify.py`.

## Relationship to prior work
Li and Villavert (2011) initiated the critical finite Hardy–Littlewood–Pólya path-matrix question, proved \(2\log N-2\le\lambda_N\le2\log N+2(1-\log2)\), and did not evaluate the limiting additive constant. Cheng and Li (arXiv:1306.1649v1, June 7, 2013) study **the identical matrix** as the one-dimensional critical discrete Hardy–Littlewood–Sobolev optimizer and establish \(\lambda_N=2\log N+O(1)\), together with uniqueness, symmetry, and monotonicity of discrete maximizers. The present claim is specifically the previously unprovided limiting additive constant, its identification with the Dirichlet logarithmic Laplacian, the strong limit of normalized Perron profiles, and the finite cell-form identity. Chen and Weth (arXiv:1710.03416, Theorem 1.4) already prove the existence, simplicity, positivity, and compact spectral theory of the **continuum** logarithmic-Laplacian ground state, which are used here as prior input. Zhou and Trinajstić's 2007 Harary-matrix papers establish graph-theoretic spectral bounds, not the claimed additive limit or profile theorem. Earlier Toeplitz results for smooth symbols, jump singularities, and uniformly bounded families do not by themselves cover the logarithmically unbounded symbol underlying this path matrix.

## Limitations
The constant \(\Lambda\) is characterized exactly as a variational eigenvalue, not evaluated in elementary closed form or accompanied by a certified decimal enclosure. The theorem is for the one-dimensional uniform path kernel only; no rate for the \(o(1)\) remainder is asserted. Finite numerical checks do not prove the limit. A more general historical Toeplitz or Harary spectral-edge theorem might imply part or all of the result and remains a residual bibliographic risk. Independent mathematical review has not been performed.

## References
- C. Li and J. Villavert, *An Extension of the Hardy–Littlewood–Pólya Inequality*, Acta Math. Sci. 31 (2011), 2285–2288, DOI:10.1016/S0252-9602(11)60400-1, open author manuscript https://faculty.utrgv.edu/john.villavert/research%20papers/acta%20math%20scientia.pdf.
- Z. Cheng and C. Li, *An Extended Discrete Hardy–Littlewood–Sobolev Inequality*, arXiv:1306.1649v1 (June 7, 2013), https://arxiv.org/abs/1306.1649.
- H. Chen and T. Weth, *The Dirichlet Problem for the Logarithmic Laplacian*, arXiv:1710.03416 (first posted 2017), especially Theorem 1.4, https://arxiv.org/abs/1710.03416.
- B. Zhou and N. Trinajstić, *Further Results on the Largest Eigenvalues of the Distance Matrix and Some Distance-Based Matrices of Connected (Molecular) Graphs*, Internet Electron. J. Mol. Des. 6 (2007), 375–384, https://biochempress.com/Files/iejmd_2007_6_0375.pdf.
- B. Zhou and N. Trinajstić, *Maximum Eigenvalues of the Reciprocal Distance Matrix and the Reverse Wiener Matrix*, Int. J. Quantum Chem. 108 (2008), 858–864; first online November 29, 2007, https://doi.org/10.1002/qua.21558.
- S.-Y. Lee, H. Dai, and E. Bettelheim, *Asymptotic Eigenvalue Distribution of Large Toeplitz Matrices*, arXiv:0708.3124 (2007), https://arxiv.org/abs/0708.3124.
