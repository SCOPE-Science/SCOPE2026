# Exact \(C_Z(2,3)\) for the regular octagonal Banach plane
## Finding
Let \(X_8=(\mathbb R^2,N)\) with
\[
N(s,t)=\max\!\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For the generalized Zbăganu constant introduced by Liu, Sarfraz, and Li,
\[
C_Z(\lambda,\mu,X)=\sup_{(x,y)\ne(0,0)}
\frac{2\,\|\lambda x+\mu y\|\,\|\mu x-\lambda y\|}
{(\lambda^2+\mu^2)(\|x\|^2+\|y\|^2)},
\]
one has
\[
C_Z(2,3,X_8)=\frac{144+149\sqrt2}{312}.
\]

## Assumptions and scope
The space is real and two-dimensional, with the displayed regular-octagonal norm. The parameters are exactly \(\lambda=2\) and \(\mu=3\), the pair singled out as an illustrative case in the defining 2021 paper. The supremum is over all \(x,y\in X_8\) not both zero. No claim is made here for other parameter pairs or for other octagonal norms.

## Proof
Put
\[
K=\frac{144+149\sqrt2}{312},\qquad
C_0=\frac{13K}2=3+\frac{149\sqrt2}{48}.
\]
Let
\[
s_j=(\cos(j\pi/4),\sin(j\pi/4)),\qquad j=0,\ldots,7.
\]
Then \(N(v)=\max_j s_j\cdot v\). If \(G=\sum_j\omega_j s_js_j^T\), where \(\omega_j\ge0\) and \(\sum_j\omega_j=1\), then
\[
v^TGv=\sum_j\omega_j(s_j\cdot v)^2\le N(v)^2. \tag{1}
\]

For fixed active supports \(c,d\in\{s_0,\ldots,s_7\}\), write \(z=(x,y)\in\mathbb R^4\),
\[
\ell=(2c,3c),\qquad m=(3d,-2d),\qquad
S_{c,d}=\frac{\ell m^T+m\ell^T}2.
\]
If \(c\) norms \(2x+3y\) and \(d\) norms \(3x-2y\), then
\[
N(2x+3y)N(3x-2y)=z^TS_{c,d}z. \tag{2}
\]
By the dihedral symmetry of the regular octagon, it is enough to fix \(c=s_0\) and consider the five relative classes \(d=s_k\), \(0\le k\le4\); reflection supplies \(k=5,6,7\).

Set \(P_j=s_js_j^T\) for \(j=0,1,2,3\) and
\[
\theta=\frac{81-36\sqrt2}{49}.
\]
For the five relative classes choose the following quadratic minorants \((G_x,G_y)\):
\[
\begin{array}{c|c|c}
k&G_x&G_y\\ \hline
0&P_0&P_0\\
1&(1-\theta)P_0+\theta P_1&P_3\\
2&\tfrac14P_2+\tfrac34P_1&\tfrac14P_0+\tfrac34P_3\\
3&P_2&\theta P_0+(1-\theta)P_3\\
4&P_0&P_0.
\end{array}
\]
Here \(0<\theta<1\), so every displayed matrix is a convex combination of support projections and therefore satisfies (1). Direct exact calculation in \(\mathbb Q(\sqrt2)\) gives
\[
C_0\,\operatorname{diag}(G_x,G_y)-S_{s_0,s_k}\succeq0
\qquad (k=0,1,2,3,4). \tag{3}
\]
A finite certificate for (3) is included in `verify_zbaganu.py`: it recomputes every principal minor of each of the five symmetric \(4\times4\) matrices using exact rational arithmetic in \(\mathbb Q(\sqrt2)\), checking all \(75\) principal minors without floating-point decisions.

For arbitrary \(x,y\), choose active supports \(c,d\) in (2), reduce their relative class by an octagonal isometry, and apply (3) and (1). This yields
\[
N(2x+3y)N(3x-2y)
\le C_0\bigl(N(x)^2+N(y)^2\bigr).
\]
Consequently
\[
\frac{2N(2x+3y)N(3x-2y)}{13(N(x)^2+N(y)^2)}\le\frac{2C_0}{13}=K. \tag{4}
\]

It remains to attain (4). Let \(a=\sqrt2-1\),
\[
z_0=\frac6{9+4\sqrt2}=\frac{54-24\sqrt2}{49},
\qquad
w_0=\frac{9-4\sqrt2-6z_0}{12}
=\frac{39}{196}-\frac{13\sqrt2}{147},
\]
and take
\[
x=(-a,-1),\qquad y=(-z_0,-w_0).
\]
The inequalities \(0<w_0<a z_0\) imply \(N(x)=1\) and \(N(y)=z_0\). On this pair the active support of \(2x+3y\) is the southwest diagonal support and the active support of \(3x-2y\) is the negative vertical support. With
\[
D=9+4\sqrt2+6z_0,
\]
one obtains exactly
\[
N(2x+3y)=\frac{D}{4\sqrt2},\qquad
N(3x-2y)=\frac D6.
\]
Substitution gives
\[
\frac{2N(2x+3y)N(3x-2y)}{13(1+z_0^2)}
=\frac{144+149\sqrt2}{312}=K,
\]
so the upper bound is sharp.

## Verification
`verify_zbaganu.py` is a standalone exact-arithmetic checker. It represents every number as \(a+b\sqrt2\) with rational \(a,b\), verifies \(0<\theta<1\), constructs the five support certificates, checks all principal minors exactly, verifies the active-support maximum for the explicit equality pair, and recomputes the final quotient. A successful run prints `VERIFY_OK`.

## Relationship to prior work
Liu, Sarfraz, and Li introduced \(C_Z(\lambda,\mu,X)\) in 2021 and devoted Example 4.3 specifically to \((\lambda,\mu)=(2,3)\). Their example proves \(C_Z(2,3,X)=25/13\) at the square endpoint \(C_{\mathrm{NJ}}(X)=2\), but it does not evaluate the regular octagonal plane.

A 2025 paper by Wang, Liu, Li, and Huang restates the same two-parameter constant and embeds it as the \(p=2\) member of a skew generalized \(p\)-Zbăganu family. Its full text gives exact examples for \(\ell_1^2\) and \(\ell_\infty^2\), general inequalities, and a separate unit-sphere example on an \(\ell_1-\ell_\infty\) plane; it does not compute the regular octagon.

Yang, Li, and Yang computed the exact Euler--Lagrange sum-of-squares constants \(L_{YJ}(\lambda,\mu,X)\) and \(L'_{YJ}(\lambda,\mu,X)\) for the regular octagon in 2024. Those constants use the same transformed vectors but optimize a sum of squares rather than their product, so their exact formulas do not determine the product extremum above.

## Limitations
The theorem fixes the natural parameter pair \((2,3)\). It does not provide the full two-parameter surface \(C_Z(\lambda,\mu,X_8)\), nor does it classify maximizing pairs up to symmetry. The positive-semidefinite upper bound is certified by a finite exact calculation; although the checker is self-contained and uses no numerical approximation, a shorter symbolic factorization of all five matrix certificates may exist.

## References
1. Q. Liu, M. Sarfraz, Y. Li, “Some aspects of generalized Zbăganu and James constant in Banach spaces,” Demonstratio Mathematica 54 (2021), 299–310. DOI: 10.1515/dema-2021-0033.
2. X. Yang, H. Li, C. Yang, “On the \(L_{YJ}(\lambda,\mu,X)\) constant for the regular octagon space,” Filomat 38(5) (2024), 1583–1593. DOI: 10.2298/FIL2405583Y.
3. Y. Wang, Q. Liu, Q. Li, Q. Huang, “Some aspects of skew generalized Zbăganu constant in Banach spaces,” Journal of Fixed Point Theory and Applications 27 (2025), article 22. DOI: 10.1007/s11784-025-01178-3.
