# A sharp noncommutativity constant for nested-disk concentration in the bianalytic Fock space

## Finding

Let \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\), let \(\mathcal F_2\) be the closed order-two polyanalytic subspace of \(L^2(\mathbb C,d\gamma)\), and let \(P_2\) be its orthogonal projection. For \(x>0\), put
\[
D_x=\{z\in\mathbb C:|z|^2\le x\},\qquad A_x=P_2M_{\mathbf 1_{D_x}}\big|_{\mathcal F_2}.
\]
For any distinct \(x,y>0\), define
\[
s_j(x,y)=|x-y|\sqrt j\,e^{-(x+y)}\frac{(xy)^j}{(j!)^2},\qquad j=1,2,\ldots.
\]
**Theorem.** The compact skew-adjoint commutator \([A_x,A_y]\) has the nonzero eigenvalues \(\pm i s_j(x,y)\), each sign occurring once for every \(j\ge1\). Its singular values are precisely \(s_j(x,y)\), each repeated twice. It has a one-dimensional kernel and belongs to every Schatten class \(S_p\), \(p>0\). Thus distinct finite positive disk cutoffs never commute, and
\[
\|[A_x,A_y]\|=\max_{j\ge1}s_j(x,y),\qquad
\|[A_x,A_y]\|_{S_p}^p=2\sum_{j\ge1}s_j(x,y)^p.
\]
The maximizing angular index is governed *exactly* by \(q=xy\): with \(T_0=0\), \(T_j=\sqrt{j(j+1)^3}\), it is uniquely \(j\) when \(T_{j-1}<q<T_j\), and the adjacent indices \(j,j+1\) tie at \(q=T_j\).

More strongly, the optimal universal operator-norm bound is
\[
\boxed{\sup_{0<x<y<\infty}\|[A_x,A_y]\|=\frac1{\pi\sqrt{2e}}},
\]
and it is **strict** for every individual pair of radii. If \(\delta_j=\sqrt{2j+1}\), the radii
\[
x_j=\frac{2j+1-\delta_j}{2},\qquad y_j=\frac{2j+1+\delta_j}{2}
\]
uniquely maximize the \(j\)-th singular-value branch and approach the universal supremum as \(j\to\infty\).

For completeness, the Hilbert–Schmidt norm admits the hypergeometric expression
\[
\|[A_x,A_y]\|_{S_2}^2=2(x-y)^2e^{-2(x+y)}(xy)^2\,{}_0F_3(;2,2,2;(xy)^2).
\]

## Assumptions and scope

The space consists of functions \(f(z)=f_0(z)+\overline z f_1(z)\) with entire \(f_0,f_1\) and finite Gaussian norm. The two cutoffs are **centered disks** of squared radii \(x,y\), and the compression is taken to the full order-two space, not either individual true-polyanalytic level. At \(x=y\) the commutator is zero; the result above assumes distinct positive finite values. The normalization of the Gaussian and the squared-radius convention are essential for the numerical constant.

## Proof

**1. Complete orthogonal block decomposition.** For integers \(k\ge0\), set
\[
u_k(z)=\frac{z^k}{\sqrt{k!}},\qquad
v_k(z)=\frac{z^k(k+1-|z|^2)}{\sqrt{(k+1)!}}.
\]
The angular-order \(k\) subspace of \(\mathcal F_2\) is the orthogonal span of \(u_k,v_k\). The sole angular-order \(-1\) subspace is \(\mathbb C\overline z\), with \(\|\overline z\|_2=1\). The spans exhaust \(\mathcal F_2\) by the normalized complex Hermite basis. In polar coordinates \(t=|z|^2\), the radial measure is \(e^{-t}dt\). Direct integration yields \(\|u_k\|_2=\|v_k\|_2=1\) and \(\langle u_k,v_k\rangle=0\).

**2. Disk-compression blocks.** Write \(j=k+1\), \(I_j(x)=\frac1{(j-1)!}\int_0^x t^{j-1}e^{-t}dt\), and \(E_j(x)=e^{-x}x^j/j!\). The radial antiderivative
\[
\frac d{dt}\big(t^je^{-t}\big)=t^{j-1}(j-t)e^{-t}
\]
and one integration by parts give the exact compression block, in the ordered basis \(u_{j-1},v_{j-1}\),
\[
A_x^{(j)}=
I_j(x)\begin{pmatrix}1&0\\0&1\end{pmatrix}
+E_j(x)\begin{pmatrix}0&\sqrt j\\ \sqrt j&j-1-x\end{pmatrix}.
\]
The remaining one-dimensional block is scalar and hence contributes zero to every commutator. No approximations occur in this decomposition.

**3. Exact commutator spectrum.** Matrix multiplication gives
\[
[A_x^{(j)},A_y^{(j)}]=(x-y)\sqrt j\,E_j(x)E_j(y)
\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
The matrix on the right has eigenvalues \(\pm i\), establishing the announced eigenvalues and singular values. Because \(s_j(x,y)\) decays superfactorially for fixed \(x,y\), the direct sum is compact and is in every Schatten class; it is nonzero in every \(j\ge1\) block if \(x\ne y\). The only null block is angular order \(-1\), so the kernel is exactly one-dimensional. Summing the squares of the two singular values gives the stated \({}_0F_3\) identity by its defining series.

**4. Exact angular mode switching.** For fixed \(x\ne y\), consecutive singular-value branches have ratio
\[
\frac{s_{j+1}(x,y)}{s_j(x,y)}=\frac{xy}{\sqrt{j(j+1)^3}}.
\]
The denominators strictly increase to infinity. The sequence is therefore strictly increasing up to one mode and strictly decreasing afterwards, except for one possible adjacent tie. This proves the exact threshold statement and ensures the maximum is attained at a finite index for each fixed radius pair.

**5. Optimization over disk cutoffs.** For fixed \(j\), maximize the positive function \((y-x)e^{-x-y}(xy)^j\) over \(0<x<y\). It vanishes at the boundary and tends to zero at infinity. The two logarithmic stationary equations are
\[
-\frac1{y-x}-1+\frac jx=0,\qquad
\frac1{y-x}-1+\frac jy=0.
\]
They imply \((y-x)^2=x+y=2j+1\), which has the unique solution \((x_j,y_j)\) displayed above. Hence the exact \(j\)-branch maximum is
\[
M_j=\sqrt{j(2j+1)}e^{-(2j+1)}
\frac{\big(j(2j+1)/2\big)^j}{(j!)^2}.
\]

**6. Sharp dimensionless universal constant, and nonattainment.** Define the Stirling remainder by
\[
\log(j!)=\big(j+\tfrac12\big)\log j-j+\tfrac12\log(2\pi)+\varepsilon_j.
\]
The standard strict factorial bound \(\varepsilon_j>1/(12j+1)\) holds for every integer \(j\ge1\). After substitution,
\[
\log\left(\frac{M_j}{1/(\pi\sqrt{2e})}\right)
=\big(j+\tfrac12\big)\log\big(1+1/(2j)\big)-\tfrac12-2\varepsilon_j.
\]
The alternating Taylor bound \(\log(1+t)\le t-t^2/2+t^3/3\) for \(0<t\le1/2\) implies
\[
\big(j+\tfrac12\big)\log\big(1+1/(2j)\big)-\tfrac12
\le\frac1{8j},
\]
while \(2\varepsilon_j>2/(12j+1)>1/(8j)\). Thus every \(M_j<1/(\pi\sqrt{2e})\). Ordinary Stirling asymptotics give \(M_j\to1/(\pi\sqrt{2e})\), proving sharpness. For any *fixed* \((x,y)\), the superfactorial decay makes the operator norm a finite-mode maximum; every branch remains below the limiting bound, so equality is impossible for finite radii.

## Verification

Run `python3 checker.py` with Python, NumPy, SciPy, SymPy, and mpmath installed. The script checks the two radial antiderivative identities symbolically, evaluates matrix entries through independent numerical quadrature, compares block commutators with their singular-value formulas, verifies mode-switching identities, and compares the Hilbert–Schmidt hypergeometric series. It also checks finite instances of the strict universal bound and the limiting sequence. The analytic infinite-index argument is contained in Step 6, not inferred from numerical experiments.

## Relationship to prior work

Maximenko and Tellería-Romero (arXiv:1905.00978, first publicly available 2019-05-02), especially Theorem 1.1 and Proposition 6.7, establish the general block structure and radial Toeplitz integral representation for polyanalytic Fock spaces. The block framework is the starting point here, **not** claimed as new. The present theorem specializes to two disk-compressions but determines their entire paired singular spectrum, exact mode-switching thresholds, and a globally sharp, nonattained commutator norm. Those quantitative claims are not supplied by the cited general framework.

Fulsche and Hagger (arXiv:2308.11292, first publicly available 2023-08-22) develop quantum harmonic analysis and essential commutants for polyanalytic Fock spaces; this provides a distinct operator-theoretic setting and does not furnish the centered two-disk constant. In contrast, on the ordinary analytic Fock space, radial disk compressions are simultaneously diagonal and commute. The order-two full space is the first setting in which this particular radial phenomenon can occur.

## Limitations

This theorem addresses only full order-two Gaussian polyanalytic space, centered disks, and their pairwise commutator. It does not give a comparable constant for displaced disks, higher polyanalytic orders, arbitrary radial symbols, or general Toeplitz commutators. The operator norm is an exact infinite-dimensional statement established analytically; finite checker instances are supporting diagnostics only. Priority with respect to unindexed or inaccessible literature is not independently confirmed.

## References

- E. A. Maximenko and A. M. Tellería-Romero, *Radial operators on polyanalytic Bargmann–Segal–Fock spaces*, arXiv:1905.00978 (initial posting 2019-05-02), especially Theorem 1.1 and Proposition 6.7. https://arxiv.org/abs/1905.00978
- R. Fulsche and R. Hagger, *Quantum harmonic analysis for polyanalytic Fock spaces*, arXiv:2308.11292 (initial posting 2023-08-22), especially the introduction and Section 4. https://arxiv.org/abs/2308.11292
- H. Robbins, *A Remark on Stirling's Formula*, American Mathematical Monthly **62** (1955), 26–29, for the standard factorial remainder inequality.
