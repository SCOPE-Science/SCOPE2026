# Exact Hilbert distance of the cubic conjugate Day--James plane

## Finding
Let \(X=(\mathbb R^2,\|\cdot\|_{3,3/2})\), where
\[
\|(x,y)\|_{3,3/2}=\begin{cases}
(|x|^3+|y|^3)^{1/3},&xy\ge0,\\
(|x|^{3/2}+|y|^{3/2})^{2/3},&xy\le0.
\end{cases}
\]
Then
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2=\frac{2^{5/3}}{3},\qquad
d_{\mathrm{BM}}(X,\ell_2^2)=\frac{2^{5/6}}{\sqrt3}.
\]
An optimal Euclidean pullback norm, up to a positive scalar factor, is
\[
|(x,y)|_*^2=\frac{5x^2-2xy+5y^2}{4}.
\]

## Assumptions and scope
All spaces and linear maps are real. The Day--James norm above is the standard \(\ell_3-\ell_{3/2}\) plane: it uses the \(\ell_3\) norm when the coordinate product is nonnegative and the \(\ell_{3/2}\) norm when it is nonpositive. On an axis the two formulas agree. The Banach--Mazur distance is the infimum of \(\|T\|\,\|T^{-1}\|\) over linear isomorphisms from \(X\) onto \(\ell_2^2\).

## Proof
Put
\[
u=\frac{x+y}{\sqrt2},\qquad v=\frac{x-y}{\sqrt2}.
\]
The coordinate swap \((x,y)\mapsto(y,x)\) is an isometry of \(X\), and in \((u,v)\)-coordinates it sends \((u,v)\) to \((u,-v)\). If a positive quadratic form \(Q\) satisfies
\[
m\|z\|_{3,3/2}^2\le Q(z)\le M\|z\|_{3,3/2}^2,
\]
then averaging \(Q\) with its pullback by the coordinate swap preserves the same two bounds. Hence an optimal ellipsoid may be taken swap-invariant. After scaling, it therefore has the form
\[
Q_\rho(u,v)=u^2+\rho v^2,\qquad \rho>0.
\]
For such a form, if \(M_\rho\) and \(m_\rho\) are the supremum and infimum of \(Q_\rho(z)/\|z\|_{3,3/2}^2\), then the squared Banach--Mazur distortion equals \(M_\rho/m_\rho\).

Write \(A=2^{1/3}\). In the region \(|u|\ge|v|\), set \(t=|v/u|\in[0,1]\). Direct substitution gives
\[
r_+(t)=\frac{Q_\rho(u,v)}{\|(x,y)\|_{3,3/2}^2}
=\frac{2(1+\rho t^2)}{(2+6t^2)^{2/3}}.
\]
In the region \(|v|\ge|u|\), set \(s=|u/v|\in[0,1]\). Then
\[
r_-(s)=\frac{2(\rho+s^2)}{\big((1+s)^{3/2}+(1-s)^{3/2}\big)^{4/3}}.
\]
For a lower bound valid for every \(\rho\), evaluate these ratios at three fixed directions:
\[
r_+(0)=A,
\qquad
r_+\!\left(\frac1{\sqrt3}\right)=\frac{3+\rho}{3A},
\qquad
r_-\!\left(\frac{\sqrt3}{2}\right)=\frac{A(4\rho+3)}9.
\]
If \(\rho\le3/2\), then
\[
\frac{r_+(0)}{r_+(1/\sqrt3)}
=\frac{3A^2}{3+\rho}
\ge\frac{2A^2}{3}.
\]
If \(\rho\ge3/2\), then
\[
\frac{r_-(\sqrt3/2)}{r_+(1/\sqrt3)}
=\frac{A^2(4\rho+3)}{3(3+\rho)}
\ge\frac{2A^2}{3}.
\]
Therefore every Euclidean pullback satisfies
\[
\frac{M_\rho}{m_\rho}\ge\frac{2A^2}{3}=\frac{2^{5/3}}3.
\]

It remains to show equality. Take \(\rho=3/2\). For the positive-product branch,
\[
r_+(t)=\frac{2(1+3t^2/2)}{(2+6t^2)^{2/3}}.
\]
The logarithmic derivative has the sign of \(t(3t^2-1)\). Hence the minimum occurs at \(t=1/\sqrt3\), while the maximum occurs at an endpoint. The values are
\[
\min r_+=\frac{3}{2^{4/3}},
\qquad
\max r_+=2^{1/3}.
\]
For the negative-product branch let
\[
S(s)=(1+s)^{3/2}+(1-s)^{3/2}.
\]
The logarithmic derivative of \(r_-(s)\) has the sign of
\[
sS(s)-(3/2+s^2)\big(\sqrt{1+s}-\sqrt{1-s}\big).
\]
Writing \(a=\sqrt{1+s}\), \(b=\sqrt{1-s}\), and using \(ab=\sqrt{1-s^2}\), this sign reduces to that of \(\sqrt{1-s^2}-1/2\). Thus \(r_-\) increases up to \(s=\sqrt3/2\) and then decreases. At \(\rho=3/2\),
\[
\min r_-=\frac{3}{2^{4/3}},
\qquad
\max r_-=2^{1/3}.
\]
Consequently
\[
\frac{M_{3/2}}{m_{3/2}}=
\frac{2^{1/3}}{3/2^{4/3}}=rac{2^{5/3}}3,
\]
which matches the lower bound. Since \(Q_{3/2}=u^2+(3/2)v^2=(5x^2-2xy+5y^2)/4\), the stated pullback is optimal.

## Verification
The proof is analytic and does not rely on a finite search. The bundled `verify.py` recomputes the special values, the claimed constant, and a dense numerical sanity check of the two one-variable ratios for \(\rho=3/2\). Its sampling is supplementary only; the derivative calculations above establish the global extrema.

## Relationship to prior work
Alonso's 2011 paper gives the Day--James \(\ell_p-\ell_q\) definition and recalls that James used the conjugate pair \(q=p'\) as a non-Hilbert example with symmetric Birkhoff orthogonality. Mitani and Saito's later full-text survey studies von Neumann--Jordan constants of Day--James spaces by comparison with two-dimensional Hilbert norms. Its exact Banach--Mazur identity in Remark 1 is stated only under the parameter hypothesis of Theorem 5; the pair \((p,q)=(3,3/2)\) violates that hypothesis. No exact Euclidean Banach--Mazur value for this conjugate cubic case appears in the inspected survey, and targeted searches did not locate one.

## Limitations
The result concerns only the real plane \(\ell_3-\ell_{3/2}\). It does not determine the distance for all conjugate Day--James pairs, classify every optimal linear map, or compute the von Neumann--Jordan constant. A residual bibliographic risk remains that an unindexed source may contain the same exact distance; the highly relevant 2018 primary paper on von Neumann--Jordan constants was not directly available in the bounded full-text check, although its theorem and hypotheses are reproduced in the inspected 2019 survey.

## References
J. Alonso, *Any two-dimensional Normed space is a generalized Day-James space*, Journal of Inequalities and Applications 2011, article 2, published 15 June 2011, DOI 10.1186/1029-242X-2011-2.

K.-I. Mitani and K.-S. Saito, *Geometrical constants of Day-James spaces*, RIMS Kôkyûroku 2143 (2019), 147--153, full text at the Kyoto University repository.
