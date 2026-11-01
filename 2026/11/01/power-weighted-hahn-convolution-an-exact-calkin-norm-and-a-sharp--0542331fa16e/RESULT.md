# Power-weighted Hahn convolution: an exact Calkin norm and a sharp compact-defect law

## Finding

Let \(\alpha>0\). On the complex *power-weighted Hahn space* \(h_\alpha\), define \(d_n=(n+1)^\alpha\) and
\[
 h_\alpha=\{x\in c_0(\mathbb N_0):\ \|x\|_\alpha=\sum_{n\ge0}d_n|x_n-x_{n+1}|<\infty\}.
\]
For any complex sequence \(a=(a_k)_{k\ge0}\) satisfying \(\sum_{k\ge0}(k+1)^\alpha|a_k|<\infty\), define \((T_ax)_n=\sum_{k=0}^na_kx_{n-k}\), and let \(f_a(z)=\sum_{k\ge0}a_kz^k\). Write \(\mathbb T=\{z\in\mathbb C:|z|=1\}\).

**Theorem.** For every \(\alpha>0\) and every such \(a\), \(T_a\) is bounded and
\[
 \boxed{\|T_a\|_{\mathrm{ess}}=\sum_{k\ge0}|a_k|,\qquad \sigma_{\mathrm F}(T_a)=f_a(\mathbb T).}
\]
Whenever \(\lambda\notin f_a(\mathbb T)\),
\[
 \boxed{\operatorname{ind}(T_a-\lambda I)=-\sum_{\substack{z\in\mathbb D\\f_a(z)=\lambda}}\operatorname{ord}_z(f_a-\lambda).}
\]
The sum is finite and is interpreted as zero when there are no roots. In particular, the Fredholm data and exact essential norm are independent of the positive power \(\alpha\). The ordinary-spectrum formula \(\sigma(T_a)=f_a(\overline{\mathbb D})\) is already available under analytic-neighborhood hypotheses in the motivating literature and follows here for the displayed weighted Wiener subalgebra; it is not asserted as a new independent result.

Let \(Sx=(0,x_0,x_1,\ldots)\) be the right shift on \(h_\alpha\). Set \((Dx)_n=d_n(x_n-x_{n+1})\), an onto isometry from \(h_\alpha\) to \(\ell_1\), and write \(U\) for the standard right shift on \(\ell_1\). Then
\[
 \boxed{\|S\|=1+2^\alpha,\qquad \|S\|_{\mathrm{ess}}=1,\qquad\|DSD^{-1}-U\|=2^\alpha.}
\]
For approximation numbers \(a_m(B)=\inf\{\|B-F\|:\operatorname{rank}F<m\}\), the compact defect \(K_\alpha=DSD^{-1}-U\) has the sharp limit
\[
 \boxed{\lim_{m\to\infty}m\,a_m(K_\alpha)=\alpha.}
\]
Thus the same shift has a large initial norm, a weight-independent Calkin norm, and a universal harmonic-rate compact correction with exact leading coefficient.

## Assumptions and scope

Indices start at zero, spaces and symbols are complex, and \(\alpha\) is an arbitrary fixed positive real number. The coefficient assumption is stronger than mere boundedness of the convolution operator; it makes the series \(\sum_ka_kS^k\) operator-norm convergent. Here \(\sigma_{\mathrm F}\) means failure of Fredholmness, not any other essential-spectrum convention, and \(\operatorname{ind}B=\dim\ker B-\operatorname{codim}\operatorname{ran}B\). The approximation-number limit concerns the **specific canonical difference-coordinate representation** \(D\) and the standard \(\ell_1\) shift \(U\), not a similarity-invariant notion of approximation numbers.

## Proof

**1. Explicit isometry and conjugacy.** For \(y\in\ell_1\), put \(x_n=\sum_{j=n}^\infty y_j/d_j\). Because \(d_j\ge1\), this belongs to \(c_0\), and \(d_n(x_n-x_{n+1})=y_n\). Therefore \(D:h_\alpha\to\ell_1\) is a surjective isometry with the stated inverse. Write \(V=DSD^{-1}\), and let \(\phi(y)=\sum_{j\ge0}y_j/d_j\). Direct calculation gives
\[
 (Vy)_0=-\phi(y),\qquad (Vy)_n=\frac{d_n}{d_{n-1}}y_{n-1}=\left(1+\frac1n\right)^\alpha y_{n-1}\quad(n\ge1).
\]
Thus \(V=U+\Delta-e_0\otimes\phi\), with \((\Delta y)_0=0\) and \((\Delta y)_n=\delta_n y_{n-1}\) for \(n\ge1\), where \(\delta_n=(1+1/n)^\alpha-1\). The sequence \((\delta_n)\) decreases to zero. Hence \(\Delta\) is compact by finite-coordinate truncation and \(e_0\otimes\phi\) is rank one. The defect \(K_\alpha=\Delta-e_0\otimes\phi\) is compact.

The \(\ell_1\) norm of an operator defined by columns is the supremum of their \(\ell_1\)-norms. The \(j\)-th column of \(V\) has nonzero entries \(-1/d_j\) at row zero and \(d_{j+1}/d_j\) at row \(j+1\). Both magnitudes decrease with \(j\), giving \(\|V\|=1+2^\alpha\). The \(j\)-th column of \(K_\alpha\) has magnitudes \(1/d_j\) and \(\delta_{j+1}\), likewise decreasing, giving \(\|K_\alpha\|=2^\alpha\). Since \(V-U\) is compact, \(\|S\|_{\mathrm{ess}}=\|U\|_{\mathrm{ess}}=1\), with the last equality justified in Step 3.

**2. Norm-convergent convolution and compact model.** For every integer \(k\ge1\), the same calculation gives
\[
 (DS^kD^{-1}y)_{k-1}=-d_{k-1}\phi(y),\qquad
 (DS^kD^{-1}y)_n=\frac{d_n}{d_{n-k}}y_{n-k}\quad(n\ge k),
\]
with all other coordinates zero. Because the ratio \(d_n/d_{n-k}\le(k+1)^\alpha\) and \(d_{k-1}=k^\alpha\),
\(\|S^k\|\le(k+1)^\alpha+k^\alpha\). Thus \(T_a=\sum_{k\ge0}a_kS^k\) in operator norm. Since \(V-U\) is compact, every \(V^k-U^k\) is compact; absolute convergence gives
\[
 DT_aD^{-1}=f_a(U)+K_a,\qquad K_a\text{ compact}.
\]
(The equality with coefficient-wise convolution follows from continuity of the coordinate functionals.)

**3. Exact Calkin norm on \(\ell_1\).** The operator \(f_a(U)\) is lower-triangular convolution on \(\ell_1\); its norm is exactly \(A=\sum_k|a_k|\): the upper bound is the triangle inequality and equality holds on \(e_0\). Let \(L\) be any compact operator. By relative compactness, a subsequence \((Le_{n_j})\) converges in norm. Given a coefficient truncation \(a^{(N)}\), choose two terms \(e_{n_j}\) and \(e_{n_l}\) with \(|n_l-n_j|>N\) and \(\|L(e_{n_j}-e_{n_l})\|\) arbitrarily small. Their images under \(f_{a^{(N)}}(U)\) have disjoint supports, so the image of the difference has norm \(2\sum_{k\le N}|a_k|\). The discarded tail contributes at most \(2\sum_{k>N}|a_k|\), and \(\|e_{n_j}-e_{n_l}\|_1=2\). Taking limits gives \(\|f_a(U)-L\|\ge A\), while \(L=0\) gives the reverse bound. Compact similarity and Step 2 yield \(\|T_a\|_{\mathrm{ess}}=A\).

**4. Fredholm symbol and winding index.** The right shift \(U\) on \(\ell_1\) has Fredholm index \(-1\) for \(U-zI\), \(|z|<1\): it is injective and its adjoint has the single eigenvector \((1,z,z^2,\ldots)\) in \(\ell_\infty\), so its range has codimension one and is closed (equivalently, use a left-shift parametrix). For \(|z|>1\), \(U-zI\) is invertible by a Neumann series.

Write \(b(z)=f_a(z)-\lambda\) for \(\lambda\notin f_a(\mathbb T)\). Because \(b\) is analytic in \(\mathbb D\), continuous on \(\overline{\mathbb D}\), and nonzero on the boundary, its interior zeros \(z_1,\ldots,z_q\) are finite, multiplicities included. Division by \(z-z_j\) preserves the analytic Wiener algebra \(A^+=\{\sum c_kz^k:\sum|c_k|<\infty\}\): indeed the coefficient of \((b(z)-b(z_j))/(z-z_j)\) at degree \(n\) is \(\sum_{k\ge n+1}b_kz_j^{k-n-1}\), absolutely summable since \(|z_j|<1\). Thus \(b(z)=\prod_{j=1}^q(z-z_j)g(z)\) for a zero-free \(g\in A^+\). The analytic Wiener inverse theorem implies \(1/g\in A^+\), so \(g(U)\) is invertible. Consequently \(f_a(U)-\lambda I\) is Fredholm with index \(-q\). Compact invariance transfers the index to \(T_a-\lambda I\).

For any \(\zeta\in\mathbb T\), \(U-\zeta I\) has unit vectors supported on long finite intervals with phase \(\zeta^{-n}\) for which \(\|(U-\zeta I)y\|_1\to0\). Polynomial approximation of the analytic Wiener series gives \(\|(f_a(U)-f_a(\zeta)I)y\|_1\to0\). If \(f_a\) is nonconstant, the lower-triangular convolution \(f_a(U)-f_a(\zeta)I\) is injective (its first nonzero coefficient forces the first nonzero input coefficient to yield a nonzero output); a Fredholm injective operator would be bounded below, contradiction. For constant \(f_a\), its zero difference is not Fredholm on an infinite-dimensional space. Hence \(f_a(\mathbb T)\) is exactly the Fredholm essential spectrum; compact invariance completes the classification.

**5. Exact compact-defect rate.** The approximation numbers of the diagonal weighted shift \(\Delta\) on \(\ell_1\) satisfy \(a_m(\Delta)=\delta_m\): truncating its first \(m-1\) columns proves the upper bound, and every rank-\(<m\) perturbation has a kernel vector in the first \(m\) coordinates, where \(\|\Delta y\|_1\ge\delta_m\|y\|_1\). Since \(K_\alpha-\Delta\) has rank one, for \(m\ge2\) the rank inequalities imply
\[
 \delta_{m+1}\le a_m(K_\alpha)\le\delta_{m-1}.
\]
As \(\lim_{m\to\infty}m\delta_m=\alpha\), the squeezed approximation-number limit follows. This is an infinite-dimensional proof; a finite matrix calculation alone would not suffice.

## Verification

The standalone `check.py` reconstructs the conjugacy identities and higher shift powers exactly using rational arithmetic for four integer values of \(\alpha\), multiple finite supports and deterministic test inputs. It checks the exact column norm formulas and numerically checks the asymptotic coefficient at fractional and integer powers. It is supplementary evidence only; Steps 1–5 establish the universal statements for every real \(\alpha>0\) and every coefficient sequence in the stated weighted Wiener class.

## Relationship to prior work

Saha and Patra, *Convolution Operators on Weighted Hahn Spaces* (arXiv:2606.22912v1), define \(h_d\), study boundedness and compactness, and determine ordinary and fine spectra. In particular their Section 6 establishes ordinary spectral mapping under analytic-neighborhood assumptions. Their sections and theorems inspected here do not give the exact Calkin norm, Fredholm boundary and index, or the sharp approximation-number asymptotic of the canonical power-weight shift defect.

A separate published result, *Flat operator-ideal profile and Fredholm boundary for dual-Hahn convolution* (2026), proves a Fredholm boundary and coefficient-norm identity on the **dual** \(\sigma_\infty\) with the **lower-triangular** convolution action. That is not an implication of the present theorem: the Banach adjoint of lower-triangular convolution on \(h_\alpha\) is an upper-triangular operator on its dual, not the lower-triangular dual-Hahn convolution in the prior result. Moreover the explicit \(\alpha/m\) compact-defect rate on the primal \(\ell_1\) model has no counterpart there. The analytical Wiener factorization is a classical input, not asserted as a new method.

## Limitations

The theorem treats only real \(\alpha>0\) and symbols with \(\sum(k+1)^\alpha|a_k|<\infty\). It does not characterize all bounded multipliers on \(h_\alpha\), general irregular Hahn weights, or other essential-spectrum conventions. The \(\alpha/m\) law is representation-dependent and is not a claim about approximation numbers of \(T_a\) itself. Classical Toeplitz/Fredholm machinery could contain closely related special cases, and independent publication-priority review remains necessary. No independent external audit has been performed.

## References

1. S. Saha and A. Patra, *Convolution Operators on Weighted Hahn Spaces*, arXiv:2606.22912v1 (first public 2026-06-22), especially Sections 3, 4 and 6; https://arxiv.org/abs/2606.22912.
2. S. Saha and A. Patra, *Spectral Properties of Convolution Operators on Non-Separable Sequence Spaces*, arXiv:2610.02919v1 (first public 2026-10-02), concerning dual Hahn convolution; https://arxiv.org/abs/2610.02919.
3. *Flat operator-ideal profile and Fredholm boundary for dual-Hahn convolution* (2026), published research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-flat-operator-ideal-profile-and-fredholm-boundary-for-dual-hahn--bd7ef66f6aed.
4. Classical analytic Wiener inverse theorem, Atkinson's Fredholm theorem and one-sided shift index theory (standard background).
