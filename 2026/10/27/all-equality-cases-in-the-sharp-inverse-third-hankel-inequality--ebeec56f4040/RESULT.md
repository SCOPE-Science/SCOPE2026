# All equality cases in the sharp inverse third Hankel inequality for starlike functions

## Finding
Let \(\mathcal S^*\) be the class of normalized analytic starlike functions on \(\mathbb D\): \(f(0)=0\), \(f'(0)=1\), and \(\operatorname{Re}(zf'(z)/f(z))>0\). Write its local inverse as \(f^{-1}(w)=w+\sum_{j\ge2}A_jw^j\) and set
\[
\mathcal H(f)=\det\begin{pmatrix}1&A_2&A_3\\A_2&A_3&A_4\\A_3&A_4&A_5\end{pmatrix}.
\]
All equality cases in the sharp Allu--Kumar bound \(|\mathcal H(f)|\le1\) are exactly
\[
 f(z)=e^{-i\theta}F_c(e^{i\theta}z),\quad F_c(z)=\frac{z}{1-cz+z^2},\quad 0\le c\le2,\quad \theta\in\mathbb R.
\]
Indeed \(\mathcal H(F_c)=1\) for every \(c\), while \(\mathcal H(e^{-i\theta}F_c(e^{i\theta}\cdot))=e^{6i\theta}\). The parameter \(c=|f''(0)|/2\) is rotation invariant, so the resulting continuum is pairwise inequivalent under rotations; the Koebe function occurs only at \(c=2\).

## Assumptions and scope
The domain is the open unit disk; local inversion is at \(0\). We rely on the published bound and its *explicit Bernstein nonnegative coefficient certificate* from Allu--Kumar, arXiv:2604.23220v1, Theorem 2.1 and proof, equations (2.5)--(2.6). Its polynomials are given below so strictness and the new equality calculation can be reconstructed. The extremal statement is for \(\mathcal S^*\), not the broader univalent class, not the direct-coefficient Hankel determinant, and not starlike functions of positive order.

## Proof
**1. The published upper bound is strict off two boundary faces.** Put \(p(z)=zf'(z)/f(z)=1+\sum_{j\ge1}c_jz^j\). By rotating, assume \(c_1=c\in[0,2]\). The Carathéodory--Schur parametrization of the first four coefficients uses \(\gamma,\eta,\rho\in\overline{\mathbb D}\); set \(x=|\gamma|\), \(y=|\eta|\). Allu--Kumar derive
\[
1152|\mathcal H(f)|\le H(c,x,y),\qquad1152-H(c,x,y)=(4-c^2)(1-x)\Phi(c,x,y).
\]
In the Bernstein expansion of \(\Phi(2u,x,y)\) on the unit cube (degree \(4,3,2\)), their displayed coefficient matrices \(M_0,M_1,M_2\) are entrywise nonnegative, and **every entry of \(M_0\) and \(M_1\) is strictly positive**. Furthermore the single zero in \(M_2\) is in its last row and last column; consequently \(\Phi(c,x,y)>0\) whenever \(c<2\) and \(x<1\), even at \(y=1\) (where positive entries of \(M_2\) have positive Bernstein support). Equality thus demands \(c=2\) or \(|\gamma|=1\). The first case is the Koebe function up to rotation by the Carathéodory equality theorem.

**2. Reduce the second boundary face to a single phase.** If \(|\gamma|=1\), the Schur function \(h=(p-1)/(p+1)\) necessarily satisfies, with \(a=c/2\),
\[
h(z)=z\frac{a+\gamma z}{1+a\gamma z}.
\]
This follows from Schwarz--Pick equality after removing the first Schur parameter: the remainder is the unimodular constant \(\gamma\). For \(c=2\), the same expression reduces to \(h(z)=z\). Substituting the rational Carathéodory coefficients into the inverse-coefficient determinant gives
\[
1152\mathcal H(f)=A(c,\gamma),
\]
where, setting \(k=c^2\),
\[
\begin{aligned}
 A(c,g)={}&18k^3+51gk^2(k-4)+g^2 k(688-368k+49k^2)\\
 &+g^3(-1152+704k-172k^2+17k^3)+g^4k(k-4)^2.
\end{aligned}
\]
This agrees with the source's \(\widetilde A\) term in (2.5) and was also recalculated directly from the rational \(h\).

**3. Exact phase rigidity.** For \(|g|=1\), let \(y=\operatorname{Re}g\). Expansion using \(g^j+g^{-j}=2T_j(y)\), with \(T_j\) Chebyshev polynomials, gives the polynomial identity
\[
1152^2-|A(c,g)|^2=8k(4-k)(1+y)P(k,y),
\]
where
\[
\begin{aligned}
P(k,y)={}&36k^4y^3+321k^4y^2+542k^4y+257k^4\\
&-144k^3y^3-2136k^3y^2-3936k^3y-1944k^3\\
&+6000k^2y^2+13032k^2y+7608k^2\\
&-30752ky-14624k+50688.
\end{aligned}
\]
For an exact positivity certificate on \(0\le k\le4\), \(-1\le y\le1\), split \(k\) into \([0,2]\) and \([2,4]\), write \(k=k_0+2u\), \(y=2v-1\), and expand \(P\) in the tensor Bernstein basis \(B_i^4(u)B_j^3(v)\). The two \(5\times4\) matrices are, respectively,
\[
\begin{pmatrix}
50688&50688&50688&50688\\
58752&145504/3&114752/3&28000\\
67200&141472/3&32448&23072\\
76032&46528&28480&19584\\
85248&139712/3&78784/3&19712
\end{pmatrix},\qquad
\begin{pmatrix}
85248&139712/3&78784/3&19712\\
94464&139840/3&72128/3&19840\\
104064&47328&70720/3&23584\\
114048&48672&24768&33120\\
124416&50688&32256&69120
\end{pmatrix}.
\]
Every entry is strictly positive. Since nonnegative Bernstein basis functions sum to one, \(P(k,y)>0\) everywhere on the stated rectangle. Thus, for \(0<c<2\), \(|\mathcal H(f)|=1\) forces \(y=-1\), hence \(g=-1\). At \(c=0\), the formula simplifies to \(A(0,g)=-1152g^3\), so every unimodular \(g\) attains equality, and a rotation makes it \(-1\).

**4. Identify and realize the functions.** Taking \(g=-1\) yields
\[
 h(z)=\frac{z(a-z)}{1-az},\qquad p(z)=\frac{1-z^2}{1-cz+z^2}.
\]
Integrating \(zf'/f=p\) with normalization \(f'(0)=1\) gives \(f=F_c\). Conversely, for \(c=2\cos t\), \(0\le t\le\pi/2\), this \(p\) is the average of \((1+e^{it}z)/(1-e^{it}z)\) and \((1+e^{-it}z)/(1-e^{-it}z)\), so its real part is strictly positive. Thus every \(F_c\) belongs to \(\mathcal S^*\). Its inverse starts
\[
F_c^{-1}(w)=w-cw^2+(c^2+1)w^3-(c^3+3c)w^4+(c^4+6c^2+2)w^5+O(w^6).
\]
Direct insertion yields \(\mathcal H(F_c)=1\), proving all candidates realize equality and completing the classification.

## Verification
The standalone `verify_exact.py` symbolically reconstructs the rational-Schur inverse determinant, the phase-factor identity, and both exact Bernstein coefficient matrices, and checks the inverse coefficients for \(F_c\). Run `python verify_exact.py` with SymPy installed. These finite symbolic polynomial identities are exact; no numerical sampling is used to infer positivity, and the reduction of the unrestricted function class to the boundary face rests on the source's proved Bernstein inequality.

## Relationship to prior work
Allu--Kumar (2026) proved the sharp modulus bound over \(\mathcal S^*\) and exhibited the Koebe function as an equality example. Their proof's displayed factorization leaves an equality analysis on \(|\gamma|=1\); the full continuous extremizer family and the phase-rigidity certificate above go beyond the theorem stated there. Trąbka-Więcław and Zaprawa (2025) treat inverse Hankel determinants for starlike functions of positive order in a distinct parameter regime, not the full equality classification here. Results for starlike functions *with respect to symmetric points* are not statements about the present class \(\mathcal S^*\). Searches of related published findings and primary-literature variants found no implication establishing this precise complete equality family; absence of search matches is not a proof of historical priority.

## Limitations
The underlying sharp inequality is prior work, not a new inequality. The new result is its complete equality classification, using the published global inequality and exact new phase analysis. The proof does not give quantitative stability, higher Hankel determinant inequalities, or classification outside the normalized starlike class. Priority relative to papers not indexed or unavailable in full text remains a residual risk. No independent audit has been performed.

## References
1. V. Allu and S. Kumar, *On the Third Hankel Determinant for Inverse Coefficients of Starlike Functions: A Bernstein Polynomial Approach*, arXiv:2604.23220v1, first public 25 April 2026; https://arxiv.org/html/2604.23220v1.
2. K. Trąbka-Więcław and P. Zaprawa, *Third Hankel Determinant for the Inverse of Starlike Functions of Order α*, Bulletin of the Malaysian Mathematical Sciences Society (2025).
3. R. J. Libera and E. J. Złotkiewicz, *Early coefficients of the inverse of a regular convex function*, Proceedings of the American Mathematical Society 85 (1982), 225–230 (Carathéodory coefficient parametrization).
