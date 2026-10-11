# Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses

## Finding
Let \(H\) be any finite abelian group with \(n=|H|\ge5\). Put
\[
\Omega=(H\times\{0\})\cup(\{0\}\times H)\subset H\times H.
\]
For every \(f:\Omega\to\mathbb C\), define its Fourier extension by
\[
\mathcal E_\Omega f(\xi,\eta)=\frac1n\sum_{(x,y)\in\Omega}f(x,y)\xi(x)\eta(y),
\qquad (\xi,\eta)\in\widehat H\times\widehat H.
\]
The exact sharp fourth-power bound is
\[
\boxed{\sum_{\xi,\eta\in\widehat H}|\mathcal E_\Omega f(\xi,\eta)|^4
\le n\left(\frac1n\sum_{z\in\Omega}|f(z)|^2\right)^2.}
\]
Every nonzero equality case is supported on exactly one of the two whole coordinate subgroups, and, on that subgroup, is a nonzero scalar multiple of one character of \(H\). Conversely, every such function attains equality. The result depends only on \(|H|\), not on the isomorphism type of \(H\). In contrast, at \(H=\mathbb Z_3\), the constant \(3\) fails: the indicator of the five-point cross gives the fourth-power quotient \(77/25>3\) under the displayed normalization.

## Assumptions and scope
All groups are finite, abelian, and written additively; \(0\) is the identity. The dual \(\widehat H\) comprises all unitary characters, and sums use counting measure. The two axes share one point \((0,0)\), which is counted once. The normalization of \(\mathcal E_\Omega\) is \(1/n\), not \(1/(2n-1)\). No assumption of prime or odd order is required. The sharp theorem assumes \(n\ge5\); it makes no optimal-constant assertion for order \(4\).

## Proof
**A sharp centered fourth-moment lemma.** Suppose \(n\ge4\) and complex numbers \(z_1,\ldots,z_n\) satisfy \(\sum_i z_i=0\). Then
\[
\frac1n\sum_i|z_i|^4\le\kappa_n\left(\frac1n\sum_i|z_i|^2\right)^2,
\qquad \kappa_n=n-2+\frac1{n-1}.
\tag{1}
\]
To prove (1), normalize \(\sum|z_i|^2=1\) and maximize \(\sum|z_i|^4\) on the compact mean-zero sphere. The vector proportional to \((n-1,-1,\ldots,-1)\) yields the value \((n^2-3n+3)/(n(n-1))>1/2\). The Lagrange equations at any maximizer are
\[
(2|z_i|^2-\lambda)z_i=\mu,\qquad \lambda\in\mathbb R,\ \mu\in\mathbb C.
\]
If \(\mu=0\), all nonzero coordinates have the same modulus, so the objective is \(1/k\le1/2\), where \(k\ge2\) is their number: impossible. Thus \(\mu\ne0\), and all coordinates are collinear complex numbers. After rotation they are real and solve a cubic \(2t^3-\lambda t-\mu_0=0\). There are at most three distinct values. If three distinct values \(a,b,c\) occurred, Vieta gives \(a+b+c=0\). Choose one coordinate of each value. Keeping their sum and sum of squares fixed, the identity
\[
a^4+b^4+c^4=\tfrac12(a^2+b^2+c^2)^2\quad(a+b+c=0)
\]
allows a small nontrivial movement of this triple with no change in the objective. Since \(n\ge4\), an untouched coordinate repeats one of the original three values. A generic small movement produces four distinct real coordinate values in another global maximizer, contradicting the cubic stationarity condition. Hence there are just two values, of multiplicities \(m\) and \(n-m\). Under the normalization \(\sum_i|z_i|^2=1\), the fourth-power sum equals \(n/[m(n-m)]-3/n\), maximized precisely when \(m=1\) or \(n-1\). This proves (1), including sharpness.

If \(Z\) is uniformly distributed on any \(n\) complex numbers with \(\mathbb EZ=0\), write \(u=\mathbb E|Z|^2\). Equation (1) and Cauchy--Schwarz give
\[
\mathbb E|Z|^4\le\kappa_n u^2,\qquad
|\mathbb E(|Z|^2Z)|
=|\mathbb E((|Z|^2-u)Z)|
\le\gamma_n u^{3/2},\quad
\gamma_n=\sqrt{\kappa_n-1}=\frac{n-2}{\sqrt{n-1}}.
\tag{2}
\]

**Independent-axis reduction.** Write \(c=f(0,0)\), and let
\[
U(\xi)=\sum_{x\in H\setminus\{0\}}f(x,0)\xi(x),\qquad
V(\eta)=\sum_{y\in H\setminus\{0\}}f(0,y)\eta(y).
\]
Under independent uniform characters \(\xi,\eta\), the variables \(U,V\) are independent and centered. Orthogonality gives
\[
u=\mathbb E|U|^2=\sum_{x\ne0}|f(x,0)|^2,\quad
v=\mathbb E|V|^2=\sum_{y\ne0}|f(0,y)|^2.
\]
Put \(w=u+v\). Expand the fourth power of \(c+U+V\), use (2), \(|\mathbb EU^2|\le u\), \(|\mathbb EV^2|\le v\), and independence. This yields the explicit estimate
\[
\begin{split}
\mathbb E|c+U+V|^4\le{}&|c|^4+6|c|^2w
+4\gamma_n|c|(u^{3/2}+v^{3/2})\\
&+\kappa_n(u^2+v^2)+6uv.
\end{split}
\tag{3}
\]
For \(n\ge5\), \(\kappa_n>3\), so \(u^{3/2}+v^{3/2}\le w^{3/2}\) and \(\kappa_n(u^2+v^2)+6uv\le\kappa_nw^2\), strictly in the latter estimate if \(uv>0\). Consequently
\[
\mathbb E|c+U+V|^4\le |c|^4+6|c|^2w+4\gamma_n|c|w^{3/2}+\kappa_nw^2.
\tag{4}
\]
For \(w>0\), put \(r=\sqrt{n-1}\) and \(t=|c|/\sqrt w\). The exact algebraic identity
\[
 n(t^2+1)^2-\bigl(t^4+6t^2+4\gamma_n t+\kappa_n\bigr)
=\frac{(rt-1)^2(r^2t^2+2r^2+2rt-1)}{r^2}\ge0
\tag{5}
\]
finishes the bound because the second factor is positive for \(r\ge2\), \(t\ge0\). When \(w=0\) the estimate is immediate. Since \(\mathbb E|c+U+V|^2=|c|^2+w=\sum_{\Omega}|f|^2\) and \(\mathcal E_\Omega f=(c+U+V)/n\), multiplying (4)--(5) by the Fourier counting-measure factor \(n^{-2}\) gives the stated inequality.

**All equality cases.** A nonzero equality case has \(w>0\). By the strict inequality in (3)--(4) for \(uv>0\), it has \(uv=0\); hence one whole punctured axis vanishes. Assume \(v=0\). For the remaining one-dimensional Fourier array \(F(\xi)=c+U(\xi)\), the ordinary inequality
\[
\frac1n\sum_\xi|F(\xi)|^4\le n\left(\frac1n\sum_\xi|F(\xi)|^2\right)^2
\]
is equality exactly when \(F\) is concentrated at one character. Fourier inversion then forces the coefficients on the full horizontal axis to be a nonzero scalar times one character, and the vertical punctured axis to vanish. The vertical case is identical. Direct orthogonality shows all these functions give equality.

Finally, for the order-three five-point cross and \(f\equiv1\), direct pair-sum counting gives \(\mathbb E|\sum_{z\in\Omega}f(z)\xi(z)|^4=77\) and \(\sum_\Omega|f|^2=5\), so the quotient is \(77/25\).

## Verification
The accompanying standalone `artifacts/verify.py` uses direct character tables, not the moment inequality itself. It checks \(4,400\) random complex Fourier inputs on eleven cyclic and noncyclic groups of orders \(5\)--\(11\), all \(178\) character-supported axis examples on those groups, \(3,900\) independent centered-moment samples on orders \(5\)--\(17\), exact centered two-level examples, and the order-three witness. Run from the directory containing this document with `OPENBLAS_NUM_THREADS=1 python artifacts/verify.py` and NumPy installed. The unrestricted assertion is proved above; finite numerical testing alone would not prove it.

## Relationship to prior work
Iosevich--Koh (2008) establishes extension exponent ranges for nonzero quadratic levels; its two-dimensional results assume a **nonzero level** and do not provide the sharp constant/equality cases for the zero-level union of two lines. Iosevich--Koh--Lee--Pham--Shen (2018) establishes restriction exponent ranges for zero-radius spheres, with stated theorems in other dimensions rather than the present exact two-dimensional fourth moment. González-Riquelme--Oliveira e Silva (2024) establishes sharp extension for parabolas, paraboloids, hyperbolic paraboloids and higher-dimensional cones, not the general two-axis set. The present result instead supplies a group-independent sharp coefficient and a complete extremizer classification on a union of two transverse subgroups. Equivalence to a general published fourth-moment theorem for the additive subspace of a Cartesian square remains a bibliographic possibility.

## Limitations
Only the fourth-power exponent and the two-axis union are analyzed. The proof does not determine the optimal coefficient for group orders \(2\), \(3\), or \(4\); the exhibited order-three example is only a strict lower-bound witness. The statement concerns Fourier extension on \(H\times H\), not arbitrary unions of intersecting subgroups with nontrivial intersection.

## References
1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505 (first public version 2008-04-28), https://arxiv.org/abs/0804.4505.
2. A. Iosevich, D. Koh, S. Lee, T. Pham, C.-Y. Shen, *On restriction estimates for the zero radius sphere over finite fields*, arXiv:1806.11387 (first public version 2018-06-29), https://arxiv.org/abs/1806.11387.
3. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (first public version 2024-05-26), https://arxiv.org/abs/2405.16647.
