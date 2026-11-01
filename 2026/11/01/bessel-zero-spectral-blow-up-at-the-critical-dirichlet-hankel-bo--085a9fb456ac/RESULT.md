# Bessel-zero spectral blow-up at the critical Dirichlet Hankel boundary

## Finding
Let \(\mathcal D\) be the classical analytic Dirichlet Hilbert space on the unit disk, with
\[\|f\|_{\mathcal D}^2=|a_0|^2+\sum_{n=1}^{\infty}n|a_n|^2,\qquad f(z)=\sum_{n=0}^{\infty}a_nz^n.\]
For every \(\varepsilon>0\), set \(d\mu_\varepsilon(t)=(1-t)^\varepsilon dt\) on \([0,1)\), and define the moment Hankel operator initially on polynomials by
\[H_\varepsilon f(z)=\sum_{n=0}^{\infty}\left(\sum_{m=0}^{\infty} B(n+m+1,1+\varepsilon)a_m\right)z^n.\]
For each \(\varepsilon>0\), this operator extends uniquely to a Hilbert–Schmidt operator on \(\mathcal D\). Let \(j_{0,k}\) be the \(k\)-th positive zero of the ordinary Bessel function \(J_0\), and let \(s_k\) denote decreasing singular values. Then, **for every fixed integer \(k\ge1\)**,
\[\boxed{\lim_{\varepsilon\downarrow0}\varepsilon s_k(H_\varepsilon)=\frac1{j_{0,k}}.}\]
In addition,
\[\boxed{\lim_{\varepsilon\downarrow0}\varepsilon\|H_\varepsilon\|_{\mathcal S_2}=\frac12.}\]
In particular, the exact leading divergence of the operator norm is \(\|H_\varepsilon\|\sim (j_{0,1}\varepsilon)^{-1}\). At \(\varepsilon=0\), the classical Hilbert-moment operator is unbounded on \(\mathcal D\).

## Assumptions and scope
The Hilbert structure is the displayed squared Dirichlet norm, with normalized area on the disk in its derivative-integral representation. The measure is **unnormalized**: its total mass is \((1+\varepsilon)^{-1}\). All limits are for positive real \(\varepsilon\downarrow0\); the singular-value limit holds at each **fixed** rank, not uniformly in rank. The classification is 30H25 (classical Dirichlet space as analytic Besov \(B^2\)). This is an operator-norm and singular-spectrum boundary result, not a general characterization of all radial measures.

## Proof
**1. Dirichlet matrix and finite Hilbert–Schmidt norm.** The orthonormal basis is \(e_0=1\), \(e_n=z^n/\sqrt n\) for \(n\ge1\). Write \(b_\varepsilon(N)=B(N+1,1+\varepsilon)\). The positive-index block of the matrix is
\[A_\varepsilon(i,j)=\sqrt{\frac ij}\,b_\varepsilon(i+j),\qquad i,j\ge1.\]
The other entries are \(b_\varepsilon(0)\) at \((0,0)\), \(b_\varepsilon(j)/\sqrt j\) at \((0,j)\), and \(\sqrt i\,b_\varepsilon(i)\) at \((i,0)\). For \(0<\varepsilon\le1\), using \(1-t\le-\log t\),
\[0<b_\varepsilon(N)\le\frac{\Gamma(1+\varepsilon)}{(N+1)^{1+\varepsilon}}\le\frac{C}{(N+1)^{1+\varepsilon}}.\]
For the block \(A_\varepsilon\), split into \(i\ge j\) and \(i<j\). Its squared entries sum to at most
\[C\sum_{i=1}^\infty i^{-1-2\varepsilon}\sum_{j\le i}j^{-1}
+C\sum_{j=1}^\infty j^{-3-2\varepsilon}\sum_{i<j}i<\infty.\]
The zero row has uniformly bounded Euclidean norm and the zero column has squared norm \(O(\varepsilon^{-1})\); thus both disappear in Hilbert–Schmidt norm after multiplication by \(\varepsilon\). The entries and estimates also show extension by continuity from polynomials.

**2. A common logarithmic coordinate.** For \(i\ge1\), partition \([0,\infty)\) into
\[I_{i,\varepsilon}=[\varepsilon\log i,\varepsilon\log(i+1)),\qquad \ell_{i,\varepsilon}=\varepsilon\log(1+1/i).\]
Map the standard basis of \(\ell^2(\{1,2,\dots\})\) isometrically to the normalized indicators \(\ell_{i,\varepsilon}^{-1/2}\mathbf1_{I_{i,\varepsilon}}\) in \(L^2(0,\infty)\). Under this embedding, \(\varepsilon A_\varepsilon\) has step kernel
\[K_\varepsilon(x,y)=\frac{\varepsilon\sqrt{i/j}\,b_\varepsilon(i+j)}{\sqrt{\ell_{i,\varepsilon}\ell_{j,\varepsilon}}},\quad (x,y)\in I_{i,\varepsilon}\times I_{j,\varepsilon}.\]
For almost every \((x,y)\) with \(x>y>0\), the corresponding indices satisfy \(i,j\to\infty\), \(j/i\to0\), and \(\varepsilon\log i\to x\). Uniform gamma-ratio asymptotics for \(0<\varepsilon\le1\) give \(b_\varepsilon(i+j)=\Gamma(1+\varepsilon)(i+j)^{-1-\varepsilon}(1+o(1))\), so \(K_\varepsilon(x,y)\to e^{-x}\). When \(0<x<y\), the additional factor \(i/j\to0\) gives \(K_\varepsilon(x,y)\to0\).

For domination, \(\log(1+1/i)\ge1/(i+1)\) and the beta bound imply
\[0\le K_\varepsilon(x,y)\le C\frac{i}{(i+j)^{1+\varepsilon}}
\le C\max(i,j)^{-\varepsilon}\le C'e^{-\max(x,y)}\]
with constants independent of \(\varepsilon\in(0,1]\). The final envelope belongs to \(L^2((0,\infty)^2)\). Dominated convergence therefore proves Hilbert–Schmidt convergence of the embedded operators to
\[(Tf)(x)=e^{-x}\int_0^x f(y)\,dy.\]
Adding back the zero-index row and column does not change this limit. Because isometric embeddings preserve all nonzero singular values, norm convergence yields \(\varepsilon s_k(H_\varepsilon)\to s_k(T)\) for every fixed \(k\), and Hilbert–Schmidt convergence gives convergence of the corresponding norms.

**3. Exact spectrum of the limit.** The positive trace-class operator \(T^*T\) has integral kernel
\[(T^*T)(y,z)=\tfrac12 e^{-2\max(y,z)}.\]
If \(T^*Tf=\lambda f\) with \(\lambda>0\), differentiation shows
\[\lambda(f''+2f')+e^{-2y}f=0,\qquad f'(0)=0.\]
Square integrability at infinity discards the Bessel \(Y_1\) solution and leaves
\[f(y)=C e^{-y}J_1(e^{-y}/\sqrt\lambda).\]
The boundary derivative condition is exactly \(J_0(1/\sqrt\lambda)=0\). Conversely, each positive \(J_0\) zero supplies an \(L^2\) eigenfunction satisfying the original integral equation (the difference has zero derivative and tends to zero at infinity). Hence \(s_k(T)=j_{0,k}^{-1}\); completeness follows from compact self-adjoint spectral theory and the absence of other positive eigenvalues. Directly,
\[\|T\|_{\mathcal S_2}^2=\int_0^\infty xe^{-2x}\,dx=\tfrac14.\]
The displayed limits follow. Finally, the zero-input column at \(\varepsilon=0\) has output squared norm \(\sum_{i\ge1}i/(i+1)^2=\infty\), so the endpoint operator is not bounded on \(\mathcal D\).

## Verification
Run `python check.py` with NumPy and SciPy. It checks beta-moment identities and bounds, resolves the first four eigenvalues of the limiting integral kernel by finite Nyström matrices, checks the Bessel-root trace truncations, and compares sampled logarithmic step kernels to their limiting values; **54 finite assertions** passed in the recorded execution. These finite tests are consistency checks only. The infinite-dimensional and parameter-limit statements are proved above, not inferred from sampling.

## Relationship to prior work
Galanopoulos, Girela, Mas and Merchán (2023) investigate boundedness criteria for measure-induced Hilbert and Cesàro operators on the Dirichlet space, including the critical Lebesgue measure. Bao, Guo, Sun and Wang (arXiv:2401.09188v1, January 17, 2024) give characterizations of boundedness and compactness for Dirichlet Hankel matrices via Carleson measures, Widom conditions, and reproducing-kernel tests. These results motivate the beta-moment approach to the unbounded Lebesgue endpoint. The present statement is **quantitative and different**: it resolves the full fixed-rank blow-up constants and their Bessel-zero law as the beta weight approaches the endpoint. The known boundedness/compactness characterizations do not by themselves supply these constants. Other literature could contain an equivalent asymptotic representation; no exhaustive priority claim is made.

## Limitations
The scaling is specific to beta-moment measures \((1-t)^\varepsilon dt\) and the classical Dirichlet norm. It does not assert uniformity over growing singular-value ranks, general perturbations of the measure, or a complete expansion beyond leading order. Earlier literature on integral Hardy operators, Bessel spectral problems, and weighted Hankel matrices may contain equivalent results that have not been located. The proof uses standard uniform gamma-ratio asymptotics and the compact-operator singular-value inequality; neither is obtained by finite computations. No independent mathematical validation has been performed.

## References
1. G. Bao, K. Guo, F. Sun, Z. Wang, *Hankel matrices acting on the Dirichlet space*, arXiv:2401.09188v1, publicly submitted 2024-01-17, https://arxiv.org/abs/2401.09188.
2. P. Galanopoulos, D. Girela, A. Mas, N. Merchán, *Operators Induced by Radial Measures Acting on the Dirichlet Space*, Results in Mathematics 78 (2023), article 106, https://doi.org/10.1007/s00025-023-01887-6.
3. S. Ye, G. Feng, *Generalized Hilbert Operator Acting on Weighted Bergman Spaces and on Dirichlet Spaces*, arXiv:2207.11176, publicly submitted 2022-07-22, https://arxiv.org/abs/2207.11176.
4. NIST Digital Library of Mathematical Functions, Chapter 10, Bessel Functions, https://dlmf.nist.gov/10.
