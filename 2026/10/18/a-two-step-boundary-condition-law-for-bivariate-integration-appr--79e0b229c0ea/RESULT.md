# A two-step boundary-condition law for bivariate integration approximation numbers

## Finding

Let \(J\) and \(B\) act on complex \(L^2(0,1)\) by
\[
(Jf)(x)=\int_0^x f(t)\,dt,\qquad
(Bf)(x)=\int_0^x f(t)\,dt-x\int_0^1 f(t)\,dt.
\]
For \(r=0,1,2\) define \(T_0=J\otimes J\), \(T_1=J\otimes B\), and \(T_2=B\otimes B\) on complex \(L^2((0,1)^2)\). Let \(a_k(T)\) be the minimum operator-norm error of approximation of \(T\) by operators of rank less than \(k\), with \(k\ge1\). Write \(\gamma\) for Euler's constant and \(W\) for the principal real Lambert function, uniquely determined by \(W(z)e^{W(z)}=z\) for positive \(z\).

With the **explicit boundary constants**
\[
B_r=2\gamma+(4-2r)\log 2-1,
\qquad r\in\{0,1,2\},
\]
the sharp approximation-number asymptotic, including a quantitative remainder, is
\[
\boxed{\displaystyle
 a_k(T_r)=\frac{W(e^{B_r}k)}{\pi^2 k}
 +O\!\left(\frac{\sqrt{\log k}}{k^{3/2}}\right)
 \quad (k\to\infty).}
\]
The constants in the error may depend on \(r\), which belongs to the fixed three-element set. In particular,
\[
\boxed{\displaystyle
\pi^2 k\,a_k(T_r)
 =\log k-\log\log k+B_r
 +O\!\left(\frac{\log\log k}{\log k}\right),}
\]
and for either adjacent boundary change,
\[
\boxed{\displaystyle
 \lim_{k\to\infty}\pi^2k\big(a_k(T_r)-a_k(T_{r+1})\big)
 =2\log2,\qquad r\in\{0,1\}.}
\]
Thus changing each coordinate from one-sided anchored integration to endpoint-pinned integration subtracts the same nonzero amount from the constant-order part of the rank-scaled approximation error. In particular, the two-endpoint difference tends to \(4\log2\) after multiplication by \(\pi^2k\).

## Assumptions and scope

All tensor products are Hilbert-space tensor products and all norms in the approximation numbers are \(L^2\)-operator norms; there is no bound on the rank of the integral kernel beyond the rank of the approximating operator. Both one-dimensional operators have Lebesgue measure and the unit interval as domain and codomain. The choice \(T_1=B\otimes J\) instead of \(J\otimes B\) has the same singular numbers by swapping coordinates. No additional boundary conditions are imposed on input functions. The kernel of \(B\) contains constants, which contribute only zero singular values and therefore do not alter the positive approximation-number sequence.

## Proof

**Step 1: exact one-dimensional spectra.** The adjoint covariance kernels are
\[
(JJ^*)(x,y)=\min(x,y),\qquad
(BB^*)(x,y)=\min(x,y)-xy.
\]
The first is the Green operator of \(-d^2/dx^2\) on \((0,1)\) with a Dirichlet condition at \(0\) and a Neumann condition at \(1\). The second is the Green operator of the same differential expression with Dirichlet conditions at both ends. Solving \(-u''=\lambda u\) with these boundary conditions gives, in descending order,
\[
 s_j(J)=\frac{1}{\pi(j-\tfrac12)},\qquad
 s_j(B)=\frac{1}{\pi j},\qquad j\ge1.
\]
The singular values of a tensor product of two compact Hilbert-space operators are the products of their singular values, with multiplicities. Therefore the positive singular sequence of \(T_r\) is the descending rearrangement of
\[
 \frac{1}{\pi^2 (j+\beta)(\ell+\delta)},
 \qquad j,\ell\ge0,
\]
where \((\beta,\delta)=(\tfrac12,\tfrac12)\), \((\tfrac12,1)\), or \((1,1)\) according as \(r=0,1,2\). For a compact operator between Hilbert spaces, the \(k\)-th singular value is exactly the best rank-less-than-\(k\) approximation error.

**Step 2: exact counting reduction.** For \(\beta,\delta\in\{\tfrac12,1\}\), define
\[
 N_{\beta,\delta}(X)
 =\#\{(j,\ell)\in\mathbb N_0^2:
 (j+\beta)(\ell+\delta)\le X\},\quad X>0.
\]
Write \(A_\eta(y)=\#\{j\ge0:j+\eta\le y\}\), and \(m_\eta=A_\eta(\sqrt X)\). Every counted pair has at least one factor not exceeding \(\sqrt X\), so the exact two-dimensional hyperbola identity is
\[
 N_{\beta,\delta}(X)
 =\sum_{j=0}^{m_\beta-1} A_\delta\!\left(\frac{X}{j+\beta}\right)
 +\sum_{\ell=0}^{m_\delta-1} A_\beta\!\left(\frac{X}{\ell+\delta}\right)
 -m_\beta m_\delta.
\]
Since \(A_\eta(y)=y+O(1)\) uniformly for \(y\ge0\) and either allowed \(\eta\), we obtain
\[
 N_{\beta,\delta}(X)
 =X\left(\sum_{j=0}^{m_\beta-1}\frac{1}{j+\beta}
 +\sum_{\ell=0}^{m_\delta-1}\frac{1}{\ell+\delta}\right)
 -m_\beta m_\delta+O(\sqrt X).
\]
For the usual harmonic numbers \(H_m=\sum_{j=1}^m 1/j\),
\[
 \sum_{j=0}^{m-1}\frac1{j+1}=H_m
 =\log m+\gamma+O(m^{-1}),
\]
while
\[
 \sum_{j=0}^{m-1}\frac1{j+\tfrac12}
 =2H_{2m}-H_m
 =\log m+\gamma+2\log2+O(m^{-1}).
\]
Moreover \(m_\eta=\sqrt X+O(1)\), hence \(m_\beta m_\delta=X+O(\sqrt X)\). Combining these expressions proves
\[
 \boxed{\displaystyle
 N_{\beta,\delta}(X)
 =X\log X+
 \big(2\gamma-1+2\log2\,\mathbf1_{\beta=1/2}
                   +2\log2\,\mathbf1_{\delta=1/2}\big)X
 +O(\sqrt X).}
\]
The coefficient of \(X\) is exactly \(B_r\).

**Step 3: inversion with tied singular values.** Let \(X_k\) denote the \(k\)-th smallest product \((j+\beta)(\ell+\delta)\), counting multiplicities. In every allowed case, multiplying a product by four produces an integer factorization. At any one product, its multiplicity is bounded by the integer divisor function at four times that product, and in particular by \(O(\sqrt{X_k})\) using divisor pairing. Consequently
\[
 k=X_k(\log X_k+B_r)+O(\sqrt{X_k}).
\]
The leading term forces \(X_k\sim k/\log k\). Put \(w_k=k/X_k>0\). As \(\log X_k=\log k-\log w_k\), the last estimate becomes
\[
 w_k+\log w_k=\log k+B_r+O(X_k^{-1/2}).
\]
The strictly increasing function \(u\mapsto u+\log u\) on the positive real axis has inverse \(z\mapsto W(e^z)\) with inverse Lipschitz constant at most one. Hence
\[
 w_k=W(e^{B_r}k)+O\!\left(\sqrt{\frac{\log k}{k}}\right).
\]
Finally \(a_k(T_r)=1/(\pi^2X_k)=w_k/(\pi^2k)\), giving the first boxed formula. The standard elementary expansion of the positive solution of \(w+\log w=\log k+B_r\) yields
\[
 W(e^{B_r}k)
 =\log k-\log\log k+B_r
 +O\!\left(\frac{\log\log k}{\log k}\right).
\]
For fixed real \(c\), the derivative of \(W(ke^c)\) with respect to \(c\) equals \(W(ke^c)/(1+W(ke^c))\), which tends to one. Because \(B_r-B_{r+1}=2\log2\), subtracting adjacent expansions proves the final boxed boundary law. All error terms are uniform over the stated finite family of boundary types.

## Verification

An accompanying executable checks the hyperbola identity by independent exact-integer row enumeration, verifies exact ranks including ties by heap merging, compares counting functions with their two-term predictions, and compares finite-rank singular numbers with numerical solutions of the Lambert equation. It completed 636 finite consistency assertions successfully. The analytic bound and the infinite limit follow from the argument above, not from those finite tests. The numerical checker uses only Python standard-library modules and exact integer arithmetic for all rank and lattice-count decisions.

## Relationship to prior work

The classical Volterra and Brownian-bridge one-dimensional spectra, the Hilbert-space tensor singular-value rule, and the Dirichlet divisor hyperbola method are established ingredients, not presented as new. Kühn–Sickel–Ullrich (2013) analyze mixed-Sobolev embedding approximation numbers, establishing logarithmically corrected leading asymptotics in a periodic setting; Nguyen–Sickel (2014) establish tensor-product Besov Weyl-number decay rates. Krieg (2016, first posted after the archive source date) gives a general tensor-power leading constant and discusses mixed Sobolev spaces on the cube. These sources establish the context and several stronger general leading-order estimates, but the inspected material does not give the three boundary-specific constant terms \(B_r\), their quantitative Lambert inversion, or the additive boundary step \(2\log2\) in this exact operator model. Comparison is by implication: a leading asymptotic \(a_k\sim(\log k)/(\pi^2 k)\) does not determine the term of order \(1/k\), and a one-dimensional singular-value theorem alone does not state the sorted two-factor spectrum's constant-order correction.

## Limitations

This result covers the indicated two-dimensional separable Hilbert-space operators only. It does not establish a nonseparable perturbation theorem, a higher-dimensional boundary law, or an optimal finite numerical value of the implicit \(O\)-constants. The underlying lattice-counting method is classical; the claim of contribution concerns its boundary-sensitive sharp spectral application. A prior statement encoded in the terminology of shifted divisor counts, Brownian-sheet covariance eigenvalues, or homogeneous mixed-Sobolev widths could be equivalent even if its title does not mention these operators. Complete historical priority has not been independently established. The 1996 Tuan–Gorenflo paper was available for comparison at abstract level rather than as fully inspected text.

## References

1. T. Kühn, W. Sickel, and T. Ullrich, *Approximation of mixed order Sobolev functions on the d-torus—Asymptotics, preasymptotics and d-dependence*, arXiv:1312.6386v1 (first posted 2013-12-22), https://arxiv.org/abs/1312.6386.
2. V. K. Nguyen and W. Sickel, *Weyl Numbers of Embeddings of Tensor Product Besov Spaces*, arXiv:1409.7565v1 (first posted 2014-09-26), https://arxiv.org/abs/1409.7565.
3. D. Krieg, *Tensor power sequences and the approximation of tensor product operators*, arXiv:1612.07680v1 (first posted 2016-12-22), https://arxiv.org/abs/1612.07680.
4. V. K. Tuan and R. Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numerical Functional Analysis and Optimization 17 (1996), 453–461, doi:10.1080/01630569608816704 (abstract-level comparison).
