# Compact H-operators are not an approximation-scheme ambient space

## Statement

Let \(H=\mathbb C^2\) with its Euclidean norm. In the sense used by Markus and by Aksoy--Thiong, a bounded operator \(T\in L(H)\) is an \(H\)-operator when its spectrum is real and there is \(C<\infty\) such that
\[
\|(T-\lambda I)^{-1}\|\le \frac{C}{|\operatorname{Im}\lambda|}
\qquad(\operatorname{Im}\lambda\ne0).
\]

The class of compact \(H\)-operators is not closed under addition, already on \(H=\mathbb C^2\). Consequently it cannot itself be a real or complex quasi-Banach space and therefore cannot serve as the ambient space of an approximation scheme in the standard sense.

An explicit pair is
\[
A=\begin{pmatrix}1&2\\0&-1\end{pmatrix},
\qquad
B=\begin{pmatrix}-1&0\\-2&1\end{pmatrix}.
\]
Both \(A\) and \(B\) are compact \(H\)-operators, whereas
\[
A+B=\begin{pmatrix}0&2\\-2&0\end{pmatrix}
\]
has spectrum \(\{2i,-2i\}\), so \(A+B\) is not an \(H\)-operator.

This gives a two-dimensional obstruction to Definition 5.1 and Theorem 5.5 of Aksoy--Thiong, *Approximation spaces for H-operators*, Involve 17 (2024), 709--722, as written: their Definition 3.2 requires the ambient \(X\) of an approximation scheme \((X,A_n)\) to be a quasi-Banach space, while Definition 5.1 and Theorem 5.5 take \(X\) to be the set of all compact \(H\)-operators.

There is a second, independent typing issue. The same paper defines \(H\)-operators through spectrum and the resolvent \(T-\lambda I\) for operators acting in one Banach space, but later speaks of compact \(H\)-operators "between" arbitrary Banach spaces \(X\) and \(Y\). Without an identification \(X=Y\), neither \(T-\lambda I\) nor the ordinary eigenvalue sequence \(\lambda_n(T)\) is canonically defined.

## Proof of the two-dimensional obstruction

Set
\[
S_A=\begin{pmatrix}1&-1\\0&1\end{pmatrix},
\quad
D_A=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
S_B=\begin{pmatrix}1&0\\1&1\end{pmatrix},
\quad
D_B=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]
A direct multiplication gives
\[
A=S_AD_AS_A^{-1},
\qquad
B=S_BD_BS_B^{-1}.
\]
For either real diagonal matrix \(D\in\{D_A,D_B\}\) and every nonreal \(\lambda\),
\[
\|(D-\lambda I)^{-1}\|_2
=\max_{d\in\{-1,1\}}\frac1{|d-\lambda|}
\le \frac1{|\operatorname{Im}\lambda|}.
\]
Hence
\[
\|(A-\lambda I)^{-1}\|
\le \|S_A\|\,\|S_A^{-1}\|\,|\operatorname{Im}\lambda|^{-1},
\]
and similarly for \(B\). Thus \(A\) and \(B\) are \(H\)-operators. They are compact because the space is finite-dimensional.

On the other hand,
\[
\det(tI-(A+B))=t^2+4,
\]
so \(\sigma(A+B)=\{2i,-2i\}\). The defining real-spectrum condition fails.

Therefore the compact \(H\)-operators are not additive. In particular, no quasinorm can make this set into a quasi-Banach linear space with the inherited operator addition.

## Consequence for the 2024 approximation-space construction

Aksoy--Thiong first define a quasinorm on a real or complex **linear space**, then define an approximation scheme \((X,A_n)\) with \(X\) a quasi-Banach space. Later their Definition 5.1 sets \(X\) equal to the set of all compact \(H\)-operators and asks to consider an approximation scheme \((X,A_n)\). The explicit matrices above show that these requirements are incompatible even in dimension two.

This is not only a terminological problem for the representation theorem. The proof of their Theorem 5.5 forms differences such as
\[
g_{n+2}=g_{n+1}^\ast-g_n^\ast
\]
and reconstructs \(T\) from a series \(\sum_n g_n\). Such operations require an additive ambient space; the class of \(H\)-operators does not supply one.

The set-theoretic eigenvalue estimates used in the paper can nevertheless be retained. For a compact \(H\)-operator \(T\) acting on one Banach space, Markus' estimate quoted there implies, with \(C_T\) an \(H\)-resolvent constant,
\[
\frac{1}{2\sqrt2(C_T+1)}|\lambda_n(T)|
\le \alpha_n(T)
\le 2\sqrt2\,C_T|\lambda_n(T)|.
\]
Thus, for any fixed positive weight sequence \(w_n\) and \(0<\mu\le\infty\),
\[
(w_n|\lambda_n(T)|)\in\ell^\mu
\quad\Longleftrightarrow\quad
(w_n\alpha_n(T))\in\ell^\mu.
\]
A coherent repair is therefore to place approximation theory in a genuine linear ambient operator space (for example \(K(X)\), with the finite-rank approximation scheme) and then intersect the resulting approximation class with the nonlinear set of compact \(H\)-operators. What fails is treating the \(H\)-operator class itself as the quasi-Banach ambient space.

## Relation to the 2026 follow-up

The abstract of Thiong, arXiv:2609.14381v1, describes a constructive and quasi-Banach framework for approximation spaces of compact \(H\)-operators "between Banach and quasi-Banach spaces." The obstruction above is therefore directly relevant to any formulation that again uses the class of compact \(H\)-operators itself as a linear/quasi-Banach ambient space.

Only the abstract of arXiv:2609.14381v1 was inspected for this record, so no theorem-level claim about that preprint is made. It may contain a revised definition that avoids the 2024 obstruction.

## Limitations and originality

The non-additivity argument is elementary linear algebra; the contribution here is its consequence for the published approximation-space setup and the explicit repair boundary. Searches for the 2024 title, DOI, arXiv identifier, Definition 5.1, Theorem 5.5, and combinations of "compact H-operator", "quasi-Banach", "approximation scheme", and correction/erratum terminology did not locate a prior correction or an equivalent published objection.

Originality is therefore asserted only to the best of our knowledge. The full text of the 2024 article was inspected. For the September 2026 follow-up, only the abstract was inspected, so this record does not assess whether its detailed definitions already address the issue.

## References

1. A. G. Aksoy and D. A. Thiong, *Approximation spaces for H-operators*, Involve **17** (2024), no. 4, 709--722. DOI: 10.2140/involve.2024.17.709.
2. A. S. Markus, *Some criteria for the completeness of a system of root vectors of a linear operator in a Banach space*, Mat. Sb. 70 (112) (1966), 526--561; English transl., Amer. Math. Soc. Transl. (2) 85 (1969), 51--91.
3. D. A. Thiong, *H-Operator Approximation Spaces via Delayed Riesz Means and Quasi-Banach Moduli*, arXiv:2609.14381v1 (2026).
