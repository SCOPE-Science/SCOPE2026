# Closed-form uniqueness for the minimal antipodal \(L_p\) Minkowski problem

## Finding
Let \(n\ge 2\), \(p<0\), and let \(u_1,\ldots,u_n\in S^{n-1}\) be linearly independent unit vectors. Prescribe positive masses \(\alpha_i^+,\alpha_i^-\) at the antipodal normals \(\pm u_i\), and write
\[
\mu=\sum_{i=1}^n\bigl(\alpha_i^+\delta_{u_i}+\alpha_i^-\delta_{-u_i}\bigr),\qquad q=1-p.
\]
Let \(U\) be the matrix whose \(i\)-th row is \(u_i^T\), set \(d=|\det U|\), and define
\[
b_i=(\alpha_i^+)^{1/q}+(\alpha_i^-)^{1/q},\qquad B_i=b_i^{q/(q-1)},
\]
\[
\lambda=\left(\frac{d}{\prod_{j=1}^nB_j}\right)^{1/(n-p)}.
\]
Then there is exactly one convex body \(K\) containing the origin in its interior with \(S_p(K,\cdot)=\mu\). It is the parallelotope
\[
K=\{x\in\mathbb R^n:-a_i^-\le \langle x,u_i\rangle\le a_i^+,\ 1\le i\le n\},
\]
where
\[
w_i=\lambda B_i,\qquad a_i^\pm=w_i\frac{(\alpha_i^\pm)^{1/q}}{b_i}.
\]
In particular, equal opposite masses give an origin-symmetric solution, whereas unequal opposite masses determine its translation as part of the same formula.

## Assumptions and scope
The normals are unit vectors and form a basis of \(\mathbb R^n\); every prescribed mass is strictly positive; and \(p<0\). The result concerns the smallest antipodal support that can span \(\mathbb R^n\), namely \(n\) independent normal pairs. It does not claim uniqueness for larger discrete supports.

For a polytope \(P\) containing the origin in its interior, the discrete \(L_p\) surface-area mass at a facet normal \(u\) is
\[
S_p(P,\{u\})=h_P(u)^{1-p}a_P(u),
\]
where \(a_P(u)\) is the Euclidean \((n-1)\)-area of the corresponding facet.

## Proof
Any solution with the displayed discrete measure is a polytope whose facet-normal support is exactly \(\{\pm u_1,\ldots,\pm u_n\}\). Hence it has the form
\[
-a_i^-\le \langle x,u_i\rangle\le a_i^+,
\]
with \(a_i^\pm>0\). Under the invertible map \(y=Ux\), this becomes an axis-aligned box with side widths
\[
w_i=a_i^++a_i^-.
\]

Let \(A_i\) denote the Euclidean area of either facet with normal \(\pm u_i\). The map \(U^{-1}\) sends the coordinate facet orthogonal to the \(i\)-th axis to that facet. Its \((n-1)\)-Jacobian on the coordinate hyperplane is
\[
|\det U|^{-1}|U^Te_i|=d^{-1},
\]
because \(U^Te_i=u_i\) is a unit vector. Therefore
\[
A_i=d^{-1}\prod_{j\ne i}w_j.
\]

Since \(q=1-p\), the prescribed masses satisfy
\[
\alpha_i^\pm=(a_i^\pm)^qA_i.
\]
Taking positive \(q\)-th roots and adding the two equations gives
\[
w_i=b_iA_i^{-1/q}.
\]
Thus
\[
a_i^\pm=w_i\frac{(\alpha_i^\pm)^{1/q}}{b_i}.
\]
Substituting the facet-area formula into the width equation and writing \(W=\prod_jw_j\) yields
\[
w_i^{1-1/q}=b_i(d^{-1}W)^{-1/q}.
\]
Hence all widths have the form
\[
w_i=\lambda B_i
\]
for one common positive scalar \(\lambda\). Multiplying over \(i\) gives
\[
\lambda^{n+q-1}=\frac{d}{\prod_jB_j}.
\]
Because \(n+q-1=n-p>0\), this equation has exactly one positive solution, namely the displayed \(\lambda\). The formulas then uniquely determine every \(a_i^\pm\). Substitution back into \(\alpha_i^\pm=(a_i^\pm)^qA_i\) verifies existence, and the deductions above prove uniqueness.

## Verification
The accompanying `verify.py` independently evaluates the closed formulas for two nonorthogonal examples, one in dimension \(2\) with \(p=-1\) and one in dimension \(3\) with \(p=-2\). It reconstructs the facet areas and all prescribed masses and checks the width splits numerically to floating-point precision. These finite computations are consistency checks only; the proof above establishes the all-dimensional statement analytically.

## Relationship to prior work
Shan's 2026 theorem proves existence for negative \(p\) when the support consists of antipodal pairs whose representatives span the ambient space. It also proves that a discrete solution has exactly the prescribed facet-normal support. The theorem does not state a closed-form inverse or uniqueness in the minimal case of exactly \(n\) independent antipodal pairs; its proof is topological rather than this explicit reduction.

Zhu's earlier negative-\(p\) existence theorem assumes the measure has no essential subspace. An antipodal pair already creates such a one-dimensional essential subspace, so that theorem does not cover the present support. The classical discrete \(L_p\) polytope theorem of Hug, Lutwak, Yang and Zhang concerns \(p>1\), a disjoint exponent range.

## Limitations
The argument relies essentially on having exactly \(n\) independent antipodal normal pairs. With more normals, the image under \(U\) is no longer a box and the scalar width reduction disappears. No claim is made about uniqueness for general negative-\(p\) discrete data. The determinant and facet-area formulas also use the stated unit-normal normalization.

## References
J. Shan, *The Discrete \(L_p\) Minkowski Problem for Negative \(p\)*, arXiv:2609.01429v1, 2026.

G. Zhu, *The \(L_p\) Minkowski Problem for Polytopes for Negative \(p\)*, arXiv:1602.07774v3; Indiana Univ. Math. J. 66 (2017).

D. Hug, E. Lutwak, D. Yang, G. Zhang, *On the \(L_p\) Minkowski Problem for Polytopes*, Discrete Comput. Geom. 33 (2005), DOI:10.1007/s00454-004-1149-8.
