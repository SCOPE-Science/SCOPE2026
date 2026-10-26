# Cubic singular-value law for radial Toeplitz commutators on bianalytic Bergman spaces

## Finding

Let \(\alpha>-1\). On the full order-two polyanalytic (bianalytic) weighted Bergman space \(A^2_{2,\alpha}(\mathbb D)\), use the probability measure
\[
d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dA(z).
\]
For real-valued \(g,h\in C^3([0,1])\), denote by \(T_g\) and \(T_h\) the orthogonal Toeplitz compressions of multiplication by \(g(|z|^2)\) and \(h(|z|^2)\), respectively. Put
\[
W(g,h)=g'(1)h''(1)-g''(1)h'(1),\qquad C=[T_g,T_h]=T_gT_h-T_hT_g.
\]
For the singular values \(s_1(C)\ge s_2(C)\ge\cdots\), counted with multiplicity, the following **exact leading spectral law** holds:
\[
\boxed{\lim_{j\to\infty}j^3s_j(C)=8(\alpha+2)\sqrt{\alpha+1}\,|W(g,h)|.}
\]
If \(W(g,h)\ne0\), this is a positive sharp coefficient and yields the complete Schatten threshold
\[
\boxed{C\in\mathcal S_p\ \Longleftrightarrow\ p>\frac13\qquad(p>0).}
\]
At \(p=1/3\), \(C\) belongs to weak Schatten \(\mathcal S_{1/3,\infty}\) but not to \(\mathcal S_{1/3}\). If \(W(g,h)=0\), the improved estimate \(s_j(C)=O(j^{-4})\) holds, so \(C\in\mathcal S_p\) for every \(p>1/4\); no necessity at this improved threshold is claimed.

## Assumptions and scope

The space is the entire order-two polyanalytic Hilbert space, not its orthogonal true-polyanalytic summand. Its members satisfy \(\partial_{\bar z}^2f=0\), with \(f=f_0+\bar z f_1\) for holomorphic \(f_0,f_1\). Both radial symbols are real-valued and have three continuous derivatives on the *closed* squared-radius interval \([0,1]\). The weight exponent \(\alpha\) is any fixed real number greater than \(-1\); constants implicit in asymptotic notation may depend on \(\alpha,g,h\). The statement covers all real pairs, including scalar and proportional pairs, for which the displayed limit is zero.

## Proof

**1. Angular-frequency reduction.** Rotation symmetry decomposes \(A^2_{2,\alpha}(\mathbb D)\) orthogonally into the one-dimensional frequency \(-1\) space \(\mathbb C\bar z\) and, for each integer \(m\ge0\), the two-dimensional frequency \(m\) space
\[
E_m=\{z^m(u+v|z|^2):u,v\in\mathbb C\}.
\]
Writing \(t=|z|^2\), its normalized radial probability weight is
\[
d\nu_m(t)=\frac{t^m(1-t)^\alpha}{B(m+1,\alpha+1)}\,dt.
\]
The Toeplitz block for a radial squared-radius symbol \(g\) is the degree-at-most-one compression of multiplication by \(g(t)\) in \(L^2(\nu_m)\). The commutator is zero on the frequency \(-1\) block.

**2. The exact Jacobi obstruction.** Let \(p_{m,0},p_{m,1},p_{m,2},\ldots\) be the orthonormal polynomials for \(\nu_m\), with positive leading coefficients. The three-term recurrence for multiplication by \(t\) has positive off-diagonal coefficients \(a_{k,m}\). For \(k=1,2\), their squares are
\[
a_{k,m}^2=\frac{k(k+\alpha)(k+m)(k+m+\alpha)}{(2k+m+\alpha)^2\bigl((2k+m+\alpha)^2-1\bigr)}.
\]
Let \(X_m\) and \(Y_m\) be the two-by-two compressed multiplication matrices for \(t\) and \(t^2\) in the basis \(p_{m,0},p_{m,1}\), and let \(Q=\operatorname{diag}(0,1)\). The three-term recurrence gives the **exact identity**
\[
Y_m=X_m^2+a_{2,m}^2Q,
\qquad
[X_m,Y_m]=a_{1,m}a_{2,m}^2
\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
In particular,
\[
a_{1,m}=\frac{\sqrt{\alpha+1}}m+O(m^{-2}),\qquad
a_{2,m}^2=\frac{2(\alpha+2)}{m^2}+O(m^{-3}).
\]
These asymptotics apply as \(m\to\infty\).

**3. Uniform boundary Taylor control.** Set \(U_m=X_m-I\) and \(V_m=Y_m-2X_m+I\). Beta moments give
\[
\mathbb E_{\nu_m}(1-t)^q=\frac{(\alpha+1)_q}{(m+\alpha+2)_q}=O(m^{-q})
\]
for every fixed nonnegative integer \(q\), where \((b)_q\) denotes the rising factorial. The two orthonormal polynomials are \(p_{m,0}=1\) and
\[
p_{m,1}(t)=\frac{t-\mu_m}{\sigma_m},\quad
\mu_m=\frac{m+1}{m+\alpha+2},\quad
\sigma_m^2=\frac{(m+1)(\alpha+1)}{(m+\alpha+2)^2(m+\alpha+3)}.
\]
Consequently, for every fixed integer \(q\ge0\) and \(r\in\{0,1\}\),
\[
\int_0^1(1-t)^{2q}|p_{m,r}(t)|^2\,d\nu_m(t)=O(m^{-2q}).
\]
Cauchy–Schwarz then bounds the degree-one compressions of \((1-t)^q\) by \(O(m^{-q})\). In particular \(\|U_m\|=O(m^{-1})\), \(\|V_m\|=O(m^{-2})\). Taylor's theorem with remainder \(|R_g(t)|\le\|g^{(3)}\|_\infty(1-t)^3/6\) yields, in every block,
\[
T_g|_{E_m}=g(1)I+g'(1)U_m+\frac{g''(1)}2V_m+\mathcal R_{g,m},
\qquad \|\mathcal R_{g,m}\|=O(m^{-3}),
\]
and the same for \(h\).

**4. Commutator and boundary-jet coefficient.** Bilinearity, \([U_m,U_m]=[V_m,V_m]=0\), and \([U_m,V_m]=[X_m,Y_m]\) show that all terms involving a remainder have norm \(O(m^{-4})\), while
\[
C|_{E_m}=\frac{W(g,h)}2\,a_{1,m}a_{2,m}^2
\begin{pmatrix}0&1\\-1&0\end{pmatrix}+O(m^{-4}).
\]
For real symbols the commutator block is a real skew-symmetric two-by-two matrix; therefore its two singular values coincide and both equal
\[
\frac{(\alpha+2)\sqrt{\alpha+1}\,|W(g,h)|}{m^3}+O(m^{-4})
\]
when \(W(g,h)\ne0\), and are \(O(m^{-4})\) when \(W(g,h)=0\).

**5. Ordered singular values.** A sequence with two singular values asymptotic to \(K/m^3\) for each angular index \(m\) has decreasing rearrangement asymptotic to \(8K/j^3\): this follows by bounding the counting function between the sequences \((K\pm\varepsilon)m^{-3}\), each repeated twice. The isolated one-dimensional block and any finite exceptional indices do not affect the limit. The same comparison yields \(s_j=O(j^{-4})\) in the zero-jet case. Summability of \(\sum_j s_j^p\) now proves precisely the stated Schatten conclusions.

## Verification

A standalone Python standard-library checker, `verify_radial_commutator.py`, evaluates compressed monomial matrices from exact beta moments, compares the commutator's squared singular value against \(a_{1,m}^2a_{2,m}^4\) in rational arithmetic, checks trivial commuting cases, and independently tests the large-frequency coefficient for four different monomial pairs and several weights. Running `python3 verify_radial_commutator.py` produced **224 passing assertions**. This finite computation corroborates the exact Jacobi identity and limiting normalization; the proof above establishes the theorem for the infinite-dimensional spaces and arbitrary real \(C^3\) symbols.

For the diagnostic pair \(g(t)=t\), \(h(t)=t^2\), the two singular values in angular block \(m\) equal \(a_{1,m}a_{2,m}^2\) *exactly*, the boundary pairing is \(W(g,h)=2\), and the theorem gives the limit \(16(\alpha+2)\sqrt{\alpha+1}\) for the scaled ordered singular values. In particular the value is \(32\) for \(\alpha=0\).

## Relationship to prior work

Barrera-Castelán, Maximenko and Ramos-Vazquez (arXiv:2009.14301, Sections 5 and 8) provide the Jacobi basis and radial Toeplitz matrix decomposition for weighted polyanalytic Bergman spaces. Their later work (arXiv:2306.06231, Theorems 1.1–1.2) determines the generated operator \(C^*\)-algebra with scalar matrix limits. These qualitative descriptions support the decomposition here but do not themselves state a cubic commutator singular-value law or its universal endpoint-derivative coefficient. Zhang, Yang and Lu (2021) study a bianalytic Toeplitz zero-product question, while Shi, Li, Zhang and Lu (published 2025) investigate commutativity with quasihomogeneous symbols. Their stated conclusions concern algebraic relations rather than the quantitative singular-value and Schatten threshold determined here. The Jacobi recurrence and beta moments are classical and are not claimed as new.

## Limitations

The sharp necessity of \(p>1/3\) requires \(W(g,h)\ne0\). When the pairing vanishes, only the sufficient improved inclusion \(p>1/4\) is proved; no complete hierarchy of higher-order cancellations is asserted. The analysis is for fixed weight \(\alpha\), full bianalytic order two, radial real \(C^3\) symbols, and the disk. Nothing is asserted for higher polyanalytic orders or nonradial symbols. The 2025 Shi–Li–Zhang–Lu paper's full text was not obtainable during comparison, so a historical-priority risk remains; the accessible abstract does not assert the present singular-value constant.

## References

1. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *Radial operators on polyanalytic weighted Bergman spaces*, arXiv:2009.14301, first posted 2020-09-29, especially Sections 2, 5 and 8. https://arxiv.org/abs/2009.14301
2. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *C*-algebras generated by radial Toeplitz operators on polyanalytic weighted Bergman spaces*, arXiv:2306.06231, first posted 2023-06-09. https://arxiv.org/abs/2306.06231
3. B. Zhang, Y. Yang, Y. Lu, *Products of Toeplitz Operators on the 2-Analytic Bergman Space*, Journal of Function Spaces 2021, article 6227981. https://doi.org/10.1155/2021/6227981
4. Y. Shi, Y. Li, B. Zhang, Y. Lu, *Commuting Toeplitz Operators on the 2-analytic Bergman Space*, Acta Math. Sinica 41 (2025), 1855–1867. https://doi.org/10.1007/s10114-025-3195-5
5. Z. Bendaoud et al., *Toeplitz operators with radial symbols on Bergman space and Schatten-von Neumann classes*, J. Math. Phys. Anal. Geom. 16 (2020), 3–26. https://doi.org/10.15407/mag16.01.003
