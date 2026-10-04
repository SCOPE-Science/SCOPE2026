# Cardinality-free slice Daugavet thickness for multi-summand \(\ell_p\)-sums
## Finding
Let \(1<p<\infty\), let \(\Gamma\) be an index set with at least three elements, and let \((X_\gamma)_{\gamma\in\Gamma}\) be nonzero real Banach spaces, each with the Daugavet property. Put
\[
Z=\left(\bigoplus_{\gamma\in\Gamma}X_\gamma\right)_p.
\]
For a Banach space \(E\), write \(\mathcal T^s(E)\) for the slice Daugavet index of thickness,
\[
\mathcal T^s(E)=\inf\left\{r>0:\exists x\in S_E,\ \exists\text{ a slice }S\subset B_E\text{ with }S\subset B(x,r)\right\}.
\]
Then
\[
\mathcal T^s(Z)=2^{1/p}.
\]
Hence the exact two-summand constant persists unchanged for every finite or infinite number of Daugavet summands; it does not depend on the cardinality of \(\Gamma\).

## Assumptions and scope
All Banach spaces are real. The exponent satisfies \(1<p<\infty\). The index set has at least three elements; the two-summand case is already contained in the cited 2020 source. The direct sum is the usual \(\ell_p\)-sum, and \(q=p/(p-1)\) is the conjugate exponent. No separability assumption is made on \(\Gamma\) or on the summands.

A slice of \(B_Z\) is \(S(B_Z,z^*,\alpha)=\{z\in B_Z:z^*(z)>1-\alpha\}\), where \(z^*\in S_{Z^*}\) and \(\alpha>0\). Since \(1<p<\infty\), \(Z^*=(\bigoplus_{\gamma\in\Gamma}X_\gamma^*)_q\).

## Proof
We prove the upper and lower bounds separately.

For the upper bound, choose distinct coordinates \(\gamma_0,\gamma_1\in\Gamma\), choose \(x_1\in S_{X_{\gamma_1}}\), and let \(x\in S_Z\) be supported only at \(\gamma_1\), with value \(x_1\). Choose \(x_0^*\in S_{X_{\gamma_0}^*}\). For \(\delta>0\), consider the slice
\[
S_\delta=\{y\in B_Z:x_0^*(y_{\gamma_0})>1-\delta\}.
\]
For \(y\in S_\delta\), set
\[
t=\left(\sum_{\gamma\ne\gamma_0}\|y_\gamma\|^p\right)^{1/p}.
\]
Then \(\|y_{\gamma_0}\|>1-\delta\), so
\[
t\le\left(1-(1-\delta)^p\right)^{1/p}.
\]
Writing the \(\gamma_0\)-coordinate and its complement as disjoint \(\ell_p\)-blocks gives
\[
\|y-x\|^p
=\|y_{\gamma_0}\|^p+\|P_{\Gamma\setminus\{\gamma_0\}}y-x\|^p
\le 1+(1+t)^p.
\]
As \(\delta\downarrow0\), the right-hand side tends to \(2\). Therefore, for every \(\varepsilon>0\), some slice \(S_\delta\) is contained in \(B(x,2^{1/p}+\varepsilon)\), and hence
\[
\mathcal T^s(Z)\le2^{1/p}.
\]

For the lower bound, fix \(x=(x_\gamma)\in S_Z\), a slice \(S(B_Z,z^*,\alpha)\), and \(\varepsilon>0\). Write \(z^*=(z_\gamma^*)\in S_{Z^*}\). Choose a finitely supported nonnegative vector \(a=(a_\gamma)\in S_{\ell_p(\Gamma)}\), with support \(F\), such that
\[
\sum_{\gamma\in F}a_\gamma\|z_\gamma^*\|>1-\alpha/4,
\]
and \(a_\gamma=0\) whenever \(z_\gamma^*=0\). This is possible by finite truncation of the norming vector for \((\|z_\gamma^*\|)\in S_{\ell_q(\Gamma)}\).

Choose \(0<\eta<1\) so small that
\[
(1-\eta)\sum_{\gamma\in F}a_\gamma\|z_\gamma^*\|>1-\alpha
\quad\text{and}\quad
2^{1/p}(1-\eta)>2^{1/p}-\varepsilon.
\]
For every \(\gamma\in F\), apply the Daugavet slice characterization in \(X_\gamma\) to the slice
\[
\left\{u\in B_{X_\gamma}:\frac{z_\gamma^*}{\|z_\gamma^*\|}(u)>1-\eta\right\}.
\]
If \(x_\gamma\ne0\), choose \(u_\gamma\) in this slice with
\[
\left\|\frac{x_\gamma}{\|x_\gamma\|}-u_\gamma\right\|>2-\eta;
\]
if \(x_\gamma=0\), choose any \(u_\gamma\) in the slice. Define \(y_\gamma=a_\gamma u_\gamma\) for \(\gamma\in F\) and \(y_\gamma=0\) otherwise. Then \(\|y\|=1\) and
\[
z^*(y)>(1-\eta)\sum_{\gamma\in F}a_\gamma\|z_\gamma^*\|>1-\alpha,
\]
so \(y\) belongs to the prescribed slice.

We use the elementary consequence of the triangle inequality employed in the cited direct-sum argument: if \(e,v\in B_E\) and \(\|e-v\|>2-\eta\), then for all \(r,s\ge0\),
\[
\|re-sv\|\ge(1-\eta)(r+s).
\]
Indeed, apply the inequality \(\|\lambda e+\mu w\|\ge(\lambda+\mu)\theta\) whenever \(\|e+w\|\ge1+\theta\), with \(w=-v\) and \(\theta=1-\eta\).

Put \(r_\gamma=\|x_\gamma\|\). For \(\gamma\in F\), the preceding estimate gives
\[
\|x_\gamma-a_\gamma u_\gamma\|\ge(1-\eta)(r_\gamma+a_\gamma),
\]
with the zero-coordinate case even easier. Therefore
\[
\begin{aligned}
\|x-y\|^p
&\ge (1-\eta)^p\sum_{\gamma\in F}(r_\gamma+a_\gamma)^p
   +\sum_{\gamma\notin F}r_\gamma^p\\
&\ge (1-\eta)^p\sum_{\gamma\in F}(r_\gamma^p+a_\gamma^p)
   +\sum_{\gamma\notin F}r_\gamma^p\\
&\ge 2(1-\eta)^p.
\end{aligned}
\]
The last inequality uses \(\sum_\gamma r_\gamma^p=1\), \(\sum_{\gamma\in F}a_\gamma^p=1\), and \(0<(1-\eta)^p\le1\). Thus
\[
\|x-y\|\ge2^{1/p}(1-\eta)>2^{1/p}-\varepsilon.
\]
Since the center, slice, and \(\varepsilon\) were arbitrary,
\[
\mathcal T^s(Z)\ge2^{1/p}.
\]
Combining the bounds proves the formula.

## Verification
The proof was checked at the level of definitions and quantifiers. The only nonstandard imported fact is the standard slice characterization of the Daugavet property, stated as Proposition 1.2(ii) in the cited source. The finite-support reduction is legitimate because every vector in \(\ell_q(\Gamma)\), with \(q<\infty\), has countable support and its norm can be approximated by finite truncations.

The lower estimate does not use a finite-dimensional experiment: it constructs an element in an arbitrary slice. The key numerical inequality is \((r+s)^p\ge r^p+s^p\) for \(r,s\ge0\) and \(p>1\). The upper estimate uses only two selected coordinates and therefore works uniformly for every larger cardinality.

## Relationship to prior work
Haller, Langemets, Lima, Nadel, and Rueda Zoca introduced and studied \(\mathcal T^s\), \(\mathcal T\), and \(\mathcal T^{cc}\) in direct sums. Their Theorem 2.6 proves for two Daugavet spaces \(X,Y\) that
\[
\mathcal T^s(X\oplus_pY)=\mathcal T(X\oplus_pY)=\mathcal T^{cc}(X\oplus_pY)=2^{1/p}.
\]
Immediately before that theorem, Remark 2.5 says that their upper-bound proposition generalizes to finite absolute sums, but the theorem itself and its matching lower-bound argument are stated for two summands. The full-text inspection therefore supplies the exact two-summand benchmark and a finite-sum upper estimate, not the multi-summand equality proved here.

Focused searches for arbitrary-cardinality, finite multi-summand, and equivalent direct-sum formulations did not locate a published statement of the exact slice-index formula above. published-finding corpus searches likewise returned no matching finding; the nearest semantic hits concerned unrelated \(\ell_p\)-sum operator geometry.

## Limitations
The claim concerns only the slice index \(\mathcal T^s\). It does not assert the same arbitrary-cardinality formula for \(\mathcal T\) or \(\mathcal T^{cc}\). The endpoints \(p=1\) and \(p=\infty\) are excluded. The originality assessment is limited by searchable published literature and database records; an equivalent statement under different notation remains a residual risk.

## References
1. R. Haller, J. Langemets, V. Lima, R. Nadel, A. Rueda Zoca, *On Daugavet indices of thickness*, arXiv:2005.02045v1, 5 May 2020; Journal of Functional Analysis 280 (2021), 108846, doi:10.1016/j.jfa.2020.108846.
