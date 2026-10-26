# Sharp fourth moments and phase rigidity of all square-free Fourier layers

## Finding

For every pair of integers \(n\ge k\ge3\), define the degree-\(k\) square-free Fourier layer on \(\mathbb T^n\) by
\[
P(z)=\sum_{S\in\binom{[n]}k}a_Sz_S,\qquad z_S=\prod_{j\in S}z_j,\qquad E=\sum_{|S|=k}|a_S|^2.
\]
With probability Haar measure on the torus, the **exact sharp fourth-moment inequality** is
\[
\int_{\mathbb T^n}|P(z)|^4\,dz\le C_{n,k}E^2,\qquad
C_{n,k}=\frac1{\binom nk}\sum_{r=0}^{\min(k,n-k)}\binom kr\binom{n-k}r\binom{2r}r.
\]
For any nonzero polynomial, equality holds precisely for
\[
a_S=t\prod_{j\in S}u_j\quad\text{for all}\ |S|=k,
\qquad t\in\mathbb C\setminus\{0\},\quad |u_j|=1.
\]
Thus every amplitude must be equal, and every phase must be induced by a character modulation of an elementary symmetric polynomial. The statement includes the one-dimensional boundary cases \(n=k\) and \(n=k+1\), for which this representation remains valid.

In particular, for the first cubic layer \(k=3\),
\[
C_{n,3}=\frac{2(10n^3-93n^2+299n-327)}{n(n-1)(n-2)},\quad n\ge3.
\]
For each fixed \(k\), \(C_{n,k}\to\binom{2k}k\) as \(n\to\infty\). For cubic layers, \(C_{n,3}=20-126/n+180/n^2+O(n^{-3})\).

## Assumptions and scope

All coefficients are arbitrary complex numbers, torus coordinates are independent Haar unit-modulus variables, and \(E\) is the coefficient-square sum, which by character orthogonality is exactly \(\|P\|_2^2\). There is no real-coefficient restriction, no nonnegativity assumption, and no asymptotic restriction on \(n\) or \(k\). The principal new range is \(k\ge3\); cases of degree one and two are included in the same proof only as context.

## Proof

**1. Eliminate coefficient phases.** Fourier orthogonality gives \(\|P\|_4^4=\|P^2\|_2^2\). Each coefficient of \(P^2\) is a sum of products \(a_Sa_T\) with prescribed exponent-vector sum \(\mathbf1_S+\mathbf1_T\). Replacing all \(a_S\) by \(|a_S|\) preserves \(E\) and cannot decrease any absolute value of a coefficient of \(P^2\). It remains to maximize over nonnegative coefficient arrays.

**2. Pairwise square-root balancing lemma.** Fix any coordinate pair \(i\ne j\). Write a nonnegative coefficient polynomial as
\[
P=A+z_iB+z_jC+z_iz_jD,
\]
where \(A,B,C,D\) are polynomials in the remaining coordinates. The coefficient arrays of \(B\) and \(C\) are indexed by the same \((k-1)\)-subsets. Write their entries as \(b_U,c_U\ge0\), and define \(e_U=\sqrt{(b_U^2+c_U^2)/2}\) and \(F=\sum_Ue_Uz_U\). Set \(P'=A+(z_i+z_j)F+z_iz_jD\). Then \(\|P'\|_2=\|P\|_2\).

We show \(\|P'\|_4^4\ge\|P\|_4^4\), with strict inequality whenever at least one \(b_U\ne c_U\). Expand squared polynomials by the two distinguished exponents. Orthogonality produces the exact identity
\[
\begin{aligned}
\|P\|_4^4={}&\|A^2\|_2^2+4(\|AB\|_2^2+\|AC\|_2^2)
+\|B^2\|_2^2+\|C^2\|_2^2\\
&+4\|AD+BC\|_2^2+4(\|BD\|_2^2+\|CD\|_2^2)
+\|D^2\|_2^2.
\end{aligned}
\]
For every remaining Fourier exponent \(v\), nonnegativity and the triangle inequality in \(\mathbb R^2\) imply
\[
(AB)_v^2+(AC)_v^2\le2(AF)_v^2,\qquad
(BD)_v^2+(CD)_v^2\le2(FD)_v^2.
\]
Indeed, the vectors \((b_U,c_U)\) have Euclidean norms \(\sqrt2e_U\).

For the three central square products, denote \(X=(B^2)_v\), \(Y=(C^2)_v\), \(Z=(BC)_v\), and \(W=(F^2)_v\). Cauchy--Schwarz, applied coefficientwise to the vectors \((b_U,c_U)\) and \((c_V,b_V)\), gives \(0\le Z\le W\). Furthermore,
\[
\left\|\begin{pmatrix}X&Z\\Z&Y\end{pmatrix}\right\|_F
\le\sum_{U+V=v}\sqrt{b_U^2+c_U^2}\sqrt{b_V^2+c_V^2}=2W.
\]
Consequently
\[
X^2+Y^2+4Z^2=(X^2+Y^2+2Z^2)+2Z^2\le6W^2.
\]
Because both \(AD\) and \(BC\) have nonnegative Fourier coefficients, \(Z\le W\) also yields \(\|AD+BC\|_2^2\le\|AD+F^2\|_2^2\). Combining the inequalities proves the balancing inequality.

If \(b_U\ne c_U\), inspect the Fourier exponent \(v=2\mathbf1_U\). Because \(U\) indexes a square-free monomial, the exponent vector \(2\mathbf1_U\) has only the decomposition \(U+U\) within the \((k-1)\)-th square-free layer. Therefore \(W-Z=e_U^2-b_Uc_U=(b_U-c_U)^2/2>0\) exactly at that exponent. Hence \(Z<W\) for that exponent. The central square-product inequality is then strict (if \(W>0\), as here). Therefore any maximizer is invariant in its coefficient magnitudes under every coordinate transposition.

**3. Global optimization.** The unit sphere \(\sum_S|a_S|^2=1\) is compact. A maximizing array exists. Step 1 permits choosing nonnegative entries; Step 2, applied to each pair \(i,j\), forces its coefficients to agree on any two \(k\)-sets differing by swapping \(i,j\). The Johnson graph of \(k\)-subsets is connected. Thus every maximizing coefficient magnitude equals \(\sqrt{E/\binom nk}\), and the symmetric polynomial \(\sum_{|S|=k}z_S\) attains the sharp value.

To count its fourth moment, fix \(S\), and choose \(T\) meeting \(S\) in \(k-r\) elements. There are \(\binom kr\binom{n-k}r\) such \(T\). The exponent vector \(\mathbf1_S+\mathbf1_T\) has \(k-r\) entries equal to two and \(2r\) entries equal to one. There are exactly \(\binom{2r}r\) ordered pairs of \(k\)-sets with the same exponent vector. Summation over \(S,T\), divided by \(\binom nk^2\), yields precisely \(C_{n,k}\).

**4. Complex equality phases.** Equality in Step 1 requires, for each common exponent vector, all nonzero products \(a_Sa_T\) to have the same complex phase. In particular, for each \((k-2)\)-set \(Q\) and distinct \(i,j,r,s\notin Q\), the rectangle relation holds:
\[
a_{Q\cup\{i,r\}}a_{Q\cup\{j,s\}}=
 a_{Q\cup\{j,r\}}a_{Q\cup\{i,s\}}.
\]
Assume first \(2\le k\le n-2\). For fixed \(i,j\), the ratio \(a_{R\cup\{i\}}/a_{R\cup\{j\}}\), indexed by \((k-1)\)-sets \(R\) disjoint from \(i,j\), is unchanged when \(R\) changes by one member, by the rectangle relation. Connectivity makes it independent of \(R\); call it \(\rho_{ij}\). Choosing a common \(R\) disjoint from any three distinct \(i,j,h\), possible because \(n\ge k+2\), gives \(\rho_{ij}\rho_{jh}=\rho_{ih}\). All ratios are unimodular, so \(\rho_{ij}=u_i/u_j\) for a fixed unimodular vector \((u_i)\). After dividing \(a_S\) by \(\prod_{i\in S}u_i\), coefficients agree on neighboring sets, hence on the connected Johnson graph, giving the asserted form.

For \(k=n\), there is a single coefficient and the form is immediate. For \(k=n-1\), all \(n\) coefficients have equal modulus; taking \(u_j=\overline{a_{[n]\setminus\{j\}}}/|a_{[n]\setminus\{j\}}|\) and \(t=|a_{[n]\setminus\{j\}}|/\prod_i u_i\) (the magnitude is independent of \(j\)) realizes the form. The case \(k=1\) is analogous. Conversely, every displayed coefficient family is obtained from the constant array by torus translation and complex scaling and therefore achieves equality.

**5. Cubic and large-dimensional formulas.** Insert \(k=3\) in the finite sum and simplify to obtain the rational cubic expression. For fixed \(k\), only the term \(r=k\) survives asymptotically: \(\binom{n-k}k/\binom nk\to1\), while the other terms are \(O_k(n^{-1})\). This gives \(\binom{2k}k\); elementary series expansion for \(k=3\) yields the stated coefficients.

## Verification

The standalone `verify_fourier.py` computes fourth moments by explicit exact Fourier convolution and compares them with the binomial formula, tests random nonnegative profiles, verifies character-modulation examples, and checks the coefficientwise two-vector balancing inequality. Execute `python3 verify_fourier.py` with standard Python; the recorded output is in `verification_output.txt`. The finite assertions are independent evidence for the displayed formulas but do not replace Steps 1--5 of the proof.

## Relationship to prior work

This problem belongs to sharp Fourier-moment theory for the homogeneous square-free Steinhaus layer. The comparison paper by Ivanisvili and Tkocz (2018) analyzes comparisons of moments of *Rademacher* (binary-sign) homogeneous chaoses, whereas the present theorem is an exact fourth moment on the continuous complex torus with classification of all equality families. Real Walsh layers possess extra torsion collisions and are not interchangeable with the Steinhaus layer. Broad hypercontractive inequalities generally do not supply this exact finite-dimensional sharp constant or its equality classification. The degree-two instance is a special case of the all-degree result; the main new range is \(k\ge3\).

## Limitations

This result is for the complete square-free homogeneous Fourier layer, not arbitrary Fourier supports, not powers \(L^p\) other than the fourth, and not real Walsh chaoses. It does not claim that the symmetrization principle extends to higher moments. No independent audit or external priority certification has been performed; an equivalent formulation in older symmetric-function or chaos literature remains possible.

## References

- P. Ivanisvili and T. Tkocz, *Comparison of moments of Rademacher chaoses*, arXiv:1807.04358v1, first public 11 July 2018, https://arxiv.org/abs/1807.04358 (full six-page preprint examined, in the distinct discrete-sign setting).
- A. Defant, L. Frerick, J. Ortega-Cerdà, M. Ounaïes, and K. Seip, *The Bohnenblust--Hille inequality for homogeneous polynomials is hypercontractive*, Annals of Mathematics 174 (2011), 485--497 (a related but differently normalized coefficient-to-supremum inequality).
