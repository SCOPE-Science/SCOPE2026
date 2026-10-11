# Exact generalized-radii witnesses for common-facet parallelotopes
## Finding
Let \(K,L\subset\mathbb R^3\) be origin-symmetric parallelotopes with corresponding facets parallel and equal volume. After a common invertible linear map, write
\[
L=Q(1,1,1),\qquad K=Q(a_1,a_2,a_3),\qquad Q(c_1,c_2,c_3)=\prod_{q=1}^3[-c_q,c_q],
\]
where \(a_q>0\) and \(a_1a_2a_3=1\). For every two distinct indices \(i,j\), the pair \((t_1,t_2)=(a_i,a_j)\) lies in Xi's set \(\mathcal B_3(K,L)\), and both inequalities defining \(\mathcal B_3(K,L)\) are equalities. If
\[
M_0=\frac12\cdot K+_0\frac12\cdot L,\qquad M_1=\frac{K+L}{2},
\]
and
\[
\lambda_q=\frac12\left(\sqrt{a_q}+\frac1{\sqrt{a_q}}\right),
\]
then the same pair also makes both inequalities in Xi's three-dimensional generalized-radii conjecture equalities. Thus the conjectural mechanism is exactly sharp on the full common-facet parallelotope family, not merely its log-Brunn--Minkowski conclusion.

There is also a sharp-witness classification: if a positive pair \((t_1,t_2)\) makes both defining inequalities of \(\mathcal B_3(K,L)\) equalities, then, up to order and multiplicity, \(t_1,t_2\) are two of \(a_1,a_2,a_3\).
## Assumptions and scope
The result is three-dimensional. The bodies are centrally symmetric parallelotopes having the same normal fan (equivalently, corresponding facets are parallel), and their volumes are equal. The generalized-radius set and the two conjectural inequalities are those introduced in Section 3 of Xi's 2026 preprint. No assertion is made for arbitrary origin-symmetric bodies or for parallelotopes with unrelated facet directions.

All statements are affine invariant under one common invertible linear map, because volumes and mixed volumes acquire the same determinant factor and the logarithmic Wulff combination commutes with such a map. Hence it is enough to use the displayed box normalization.
## Proof
Put \(A=a_1+a_2+a_3\) and \(B=a_1a_2+a_1a_3+a_2a_3\). Since \(a_1a_2a_3=1\), the Minkowski polynomial is
\[
|K+sL|=8\prod_{q=1}^3(a_q+s)=8\bigl(1+Bs+As^2+s^3\bigr).
\]
Comparing with
\[
|K+sL|=|K|+3sV(K,K,L)+3s^2V(K,L,L)+s^3|L|
\]
gives
\[
3V(K,K,L)=8B,\qquad 3V(K,L,L)=8A,
\]
while \(|K|=|L|=8\).

Choose, for example, \((t_1,t_2)=(a_1,a_2)\); the other choices are identical. Because \(a_3=1/(a_1a_2)\),
\[
\frac{|K|}{t_1t_2}+(t_1+t_2)|L|=8(a_3+a_1+a_2)=3V(K,L,L),
\]
and
\[
\left(\frac1{t_1}+\frac1{t_2}\right)|K|+t_1t_2|L|=8(a_2a_3+a_1a_3+a_1a_2)=3V(K,K,L).
\]
Thus \((a_1,a_2)\in\mathcal B_3(K,L)\) and both defining inequalities are sharp.

Next determine \(M_0\) exactly. Define
\[
Q_0=Q(\sqrt{a_1},\sqrt{a_2},\sqrt{a_3}).
\]
For \(u\in\mathbb R^3\), weighted Cauchy--Schwarz gives
\[
h_{Q_0}(u)^2=\left(\sum_q\sqrt{a_q}|u_q|\right)^2\le\left(\sum_q a_q|u_q|\right)\left(\sum_q|u_q|\right)=h_K(u)h_L(u).
\]
Therefore \(Q_0\subseteq M_0\). Conversely, the defining half-space inequalities for \(M_0\) in the coordinate directions give \(|x_q|\le\sqrt{a_q}\), so \(M_0\subseteq Q_0\). Hence
\[
M_0=Q_0,\qquad |M_0|=8.
\]
Also
\[
M_1=Q\left(\frac{a_1+1}{2},\frac{a_2+1}{2},\frac{a_3+1}{2}\right)
=Q(\sqrt{a_1}\lambda_1,\sqrt{a_2}\lambda_2,\sqrt{a_3}\lambda_3).
\]
Since \(\prod_q\sqrt{a_q}=1\),
\[
|M_1|=8\lambda_1\lambda_2\lambda_3
\]
and the mixed-volume polynomial for \(M_0+sM_1\) gives
\[
3V(M_0,M_0,M_1)=8(\lambda_1+\lambda_2+\lambda_3).
\]
For \((t_1,t_2)=(a_1,a_2)\), Xi's associated parameters are exactly \(\lambda_1,\lambda_2\). Thus the right side of the first conjectural inequality is
\[
(\lambda_1+\lambda_2)|M_0|+\frac{|M_1|}{\lambda_1\lambda_2}=8(\lambda_1+\lambda_2+\lambda_3),
\]
and because \(\sqrt{|K||L|}=|M_0|=8\), the right side of the second conjectural inequality is the same number. Both therefore equal \(3V(M_0,M_0,M_1)\).

Finally, suppose a positive pair \((t_1,t_2)\) makes both defining inequalities of \(\mathcal B_3(K,L)\) equalities. Set \(t_3=1/(t_1t_2)\). The two equalities say
\[
t_1+t_2+t_3=A,\qquad t_1t_2+t_1t_3+t_2t_3=B,
\]
and by definition \(t_1t_2t_3=1\). Hence \(t_1,t_2,t_3\) are the roots, with multiplicity, of
\[
z^3-Az^2+Bz-1,
\]
which is also the monic cubic with roots \(a_1,a_2,a_3\). Therefore the two multisets coincide, proving the classification.
## Verification
The proof is symbolic and uses only the Minkowski polynomial of boxes, one weighted Cauchy--Schwarz inequality, and elementary symmetric polynomials. The bundled `artifacts/verify.py` performs exact rational consistency checks on several nontrivial equal-volume box pairs for all three choices of generalized-radius witnesses and prints `VERIFY_OK`. Those finite checks are supplementary; the universal statement is proved by the algebra above.
## Relationship to prior work
Xi introduced \(\mathcal B_3(K,L)\) and proposed the two three-dimensional inequalities in Section 3 of the September 2026 preprint *A very short unified proof of Dar's conjecture and Log-Brunn--Minkowski in the plane*. The paper proves the planar theory and observes only that \(\mathcal B_3(K,L)\) is nonempty in general; it does not treat boxes or parallelotopes in the three-dimensional conjecture. The present calculation supplies explicit generalized radii for a full non-homothetic equality family and shows that all four relevant inequalities are simultaneously sharp.

The 2016 Xi--Leng paper proves the planar Dar and log-Brunn--Minkowski inequalities and their equality cases, but it predates the new three-dimensional generalized-radii mechanism and does not imply an explicit witness pair for that mechanism.
## Limitations
This does not prove Xi's conjecture for general three-dimensional origin-symmetric convex bodies. It exploits a common normal fan: if the parallelotopes do not have corresponding parallel facets, the logarithmic Wulff combination need not reduce to coordinatewise geometric means. The classification concerns pairs that make both defining inequalities of \(\mathcal B_3(K,L)\) equalities; it does not classify every generalized-radius pair that may satisfy the conjectural inequalities non-sharply.
## References
1. Dongmeng Xi, *A very short unified proof of Dar's conjecture and Log-Brunn--Minkowski in the plane*, arXiv:2609.08495v1, 2026.
2. Dongmeng Xi and Gangsong Leng, *Dar's conjecture and the log-Brunn--Minkowski inequality*, Journal of Differential Geometry 103 (2016), 145--189, DOI:10.4310/jdg/1460463565.
