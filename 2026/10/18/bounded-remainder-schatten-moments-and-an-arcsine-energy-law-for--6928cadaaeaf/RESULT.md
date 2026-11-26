# Explicit one-sided trace defects for finite Cesàro matrices

## Finding

Let \(C_n=(\mathbf1_{j\le i}/i)_{1\le i,j\le n}\) be the finite Cesàro matrix, \(B_n=C_nC_n^*\), \(H_n=\sum_{i=1}^n1/i\), and \(c_k=\binom{2k-2}{k-1}\). For every \(n\ge1\) and every integer \(k\ge2\),
\[
0<c_kH_n-\operatorname{tr}(B_n^k)
\le c_k\bigl(k-1+H_n-\log(n+1)\bigr)\le kc_k.
\]
Also \(\operatorname{tr}(B_n)=H_n\). In particular, every normalized moment of positive order of the energy-weighted spectral measure is strictly below the corresponding moment of its arcsine limit. The estimate controls the discrepancy at every finite size and gives a bound explicit in the moment order. The normalized limit itself is a special case of the spectral density theorem for Hardy-kernel matrices.

## Proof

The Gram entries are \((B_n)_{ij}=\min(i,j)/(ij)=1/\max(i,j)\), giving the trace identity for \(k=1\). For \(k\ge2\) define the positive, coordinatewise nonincreasing kernel
\[
F(x_1,\ldots,x_k)=\prod_{j=1}^k\frac{1}{\max(x_j,x_{j+1})},\qquad x_{k+1}=x_1,
\]
on positive coordinates. Its sum over \(\{1,\ldots,n\}^k\) is \(\operatorname{tr}(B_n^k)\).

To evaluate its integrals let \(x_j=e^{t_j}\). With all coordinates free, the Jacobians cancel the term \(\exp(-\sum_j t_j)\) in \(F(e^{t_1},\ldots,e^{t_k})\), leaving \(\exp(-\frac12\sum_j|t_j-t_{j+1}|)\). Write \(v_1=0\), \(v_j=t_j-t_1\) for \(j\ge2\), \(v_{k+1}=0\), and \(V=\sum_j|v_j-v_{j+1}|\). Then
\[
\int_{\mathbb R^{k-1}} e^{-V/2}\,dv = h^{*k}(0)
=\frac{1}{2\pi}\int_{\mathbb R}(\xi^2+1/4)^{-k}\,d\xi=c_k,
\qquad h(t)=e^{-|t|/2}.
\]
Here the convolution follows by chaining the differences around the anchored cycle, and the last equality follows from the beta integral. Integrability also follows from \(V\ge2\max_j|v_j|\).

For the upper bound on the trace, hold \(x_1=i\) fixed. On each cell \(\prod_{j=2}^k(i_j-1,i_j]\) the kernel dominates its value at the integer endpoint. The sum over \(i_2,\ldots,i_k\le n\) is therefore bounded above by the integral over \((0,n]^{k-1}\). Extending it to all positive coordinates strictly increases it for finite \(n\). Changing variables as above with \(t_1=\log i\), only the first Jacobian is absent, so the full anchored integral equals \(c_k/i\). Sum this strict inequality over \(1\le i\le n\).

For the lower bound on the trace, compare each lattice point with the cell starting at that point, obtaining
\[
\operatorname{tr}(B_n^k)\ge \int_{[1,n+1]^k}F(x)\,dx
=\int_{\mathbb R^{k-1}} e^{-V/2}(T-R)_+\,dv,
\]
where \(T=\log(n+1)\), \(R=\max_jv_j-\min_jv_j\), and \((T-R)_+\) is the length of the allowed interval for the anchor \(t_1\). The two routes around the cycle from a minimum to a maximum each have variation at least \(R\), so \(2R\le V\). Subtracting the integral from \(Tc_k\) gives a deficit bounded by \(\frac12\int Ve^{-V/2}\,dv=(k-1)c_k\). Indeed positive homogeneity in \(k-1\) dimensions gives \(\int e^{-aV}dv=(2a)^{-(k-1)}c_k\), and differentiation at \(a=1/2\) is valid by exponential domination. Combining the estimates yields the displayed defect bound, using \(H_n-\log(n+1)\le1\).

## Interpretation and prior work

The positive eigenvalues of \(B_n\) lie in \((0,4]\) by the Schur test: with \(w_i=i^{-1/2}\), the sums over \(j\le i\) and \(j>i\) in \((B_nw)_i\) are each at most \(2w_i\), by integral comparison. Put \(\mu_n=H_n^{-1}\sum_j\lambda_j(B_n)\delta_{\lambda_j(B_n)}\). With the Fourier normalization of A. Pushnitski, *The spectral density of Hardy kernel matrices*, [arXiv:2103.12642](https://arxiv.org/abs/2103.12642), the symbol \(\varphi(\xi)=(\xi^2+1/4)^{-1}\) has Fourier transform \(e^{-|t|/2}\), so \(K_N(\varphi)=B_N\). Theorem 2.1 with Lipschitz extensions of \(x^k\) from \([0,4]\) gives the moment limits after replacing \(\log n\) by \(H_n\). Weighting the limit by energy gives moments \(c_{m+1}=\binom{2m}{m}\), those of the arcsine probability measure \(\mu_\infty\) on \([0,4]\); compact support yields weak convergence. Pushnitski's Lemma 5.1 also supplies a bounded lattice/continuous trace comparison for this symbol; a bounded remainder without explicit constants is not the distinction here.

The signed finite-size estimate is the quantitative point. For any fixed polynomial \(p(x)=\sum_{m=0}^M a_m x^m\) with \(a_m\ge0\) for \(m\ge1\), it gives
\[
0\le\int p\,d\mu_\infty-\int p\,d\mu_n
\le\frac{1}{H_n}\sum_{m=1}^M a_m c_{m+1}\bigl(m+H_n-\log(n+1)\bigr).
\]
Using absolute coefficients gives an absolute error bound for any polynomial. No optimality of the defect constant or rate for arbitrary continuous tests is asserted.

## Verification

The proof is for all \(n\) and integer \(k\) in scope. `CHECK.py` is a standard-library exact-rational check of the Gram and trace identities and of the strict sign and the bound by \(kc_k\) on small cases; it does not test the logarithmic refinement. For \(k=2\), grouping the terms by their maximum gives the exact defect \(\sum_{j=1}^n1/j^2\).
