# Reduced neutral components force square-zero graded radicals and a graded Wedderburn complement

## Finding

Let \(F=\mathbb F_q\) have characteristic \(2\), and let \(A=A_0\oplus A_1\) be a finite-dimensional associative \(\mathbb Z/2\mathbb Z\)-graded \(F\)-algebra, not necessarily unital. Assume that \(A_0\) is reduced, meaning that it has no nonzero nilpotent elements. Then its graded Jacobson radical \(J=J_{\mathrm{gr}}(A)\) satisfies

\[
J_0=0,\qquad J^2=0,
\]

and there is a graded subalgebra \(B\subseteq A\) such that

\[
A=B\oplus J\quad\text{as }F\text{-vector spaces},\qquad B\cong A/J
\]

as graded algebras. The graded-semisimple algebra \(B\) (that is, \(J_{\mathrm{gr}}(B)=0\)) is a direct sum of graded-simple components of the following four forms, where \(K\) ranges over finite extensions of \(F\):

1. \(K\) concentrated in degree zero;
2. \(K[C_2]=K\oplus Ku\), with \(u\) of degree one and \(u^2=1\);
3. \(M_2(K)\) with the elementary grading \(C_0=KE_{11}\oplus KE_{22}\), \(C_1=KE_{12}\oplus KE_{21}\);
4. \(M_2(K)\) with the field grading: writing \(L=\mathbb F_{q^{2d}}\), \(K=\mathbb F_{q^d}\), and \(\sigma(x)=x^{q^d}\), identify \(M_2(K)\cong\operatorname{End}_K(L)\); then \(C_0\) is the multiplication-operator copy of \(L\), and \(C_1=L\sigma\).

The extension-field types and the fourth type are genuine additional components when the degree-zero algebra is allowed to be reduced rather than required to satisfy \(x^q=x\) for every degree-zero element.

## Assumptions and scope

A grading means \(A_iA_j\subseteq A_{i+j\bmod 2}\). Reducedness is imposed on the degree-zero subalgebra, not on all of \(A\). The statement is over a finite base field of characteristic two. The field extensions in the component list are finite and separable automatically. No assertion is made for arbitrary infinite base fields, for other grading groups, or for nonassociative algebras.

## Proof

First, a finite-dimensional reduced algebra over a finite field is a finite product of finite fields: its Jacobson radical is nilpotent and hence zero, and any matrix factor of size greater than one would contain a nonzero nilpotent matrix. Thus \(A_0\) is commutative semisimple and separable over \(F\).

Let \(J=J_{\mathrm{gr}}(A)\). For a finite-dimensional graded algebra, the graded radical is a nilpotent graded ideal. Hence \(J_0=J\cap A_0\) is a nilpotent ideal of the reduced algebra \(A_0\), so \(J_0=0\). Therefore \(J=J_1\), and grading gives \(J^2\subseteq J_0=0\).

Suppose first that \(A\) is unital. The algebra \(A_0\otimes_F A_0^{\mathrm{op}}\) is semisimple, because \(A_0\) is a product of finite separable field extensions. Consequently the sub-bimodule \(J_1\subseteq A_1\) has an \(A_0\)-bimodule complement \(C_1\): \(A_1=C_1\oplus J_1\). Set \(B=A_0\oplus C_1\). Bimodule stability gives \(A_0C_1+C_1A_0\subseteq C_1\), and the grading gives \(C_1C_1\subseteq A_0\); hence \(B\) is a graded subalgebra. The quotient map \(A\to A/J\) restricts to a bijective graded algebra homomorphism on \(B\), proving the complement assertion. For nonunital \(A\), its unitization has reduced degree-zero component; applying the unital case and intersecting the resulting complement with \(A\) gives the same conclusion. The graded radical of the unitization equals \(J_{\mathrm{gr}}(A)\), since both are nilpotent graded ideals and the unitization's graded radical has no scalar component.

The same unitization argument gives \(J_{\mathrm{gr}}(B)=0\). The finite-dimensional graded Wedderburn decomposition therefore expresses \(B\) as a direct sum of graded-simple components. It remains to identify those components: let \(C=C_0\oplus C_1\) be one of them. Since \(C_0\) is reduced, write \(C_0=\prod_{i=1}^r K_i e_i\) with finite fields \(K_i\) and orthogonal primitive idempotents \(e_i\). Put \(M_{ij}=e_iC_1e_j\). Graded simplicity forces the nonzero off-diagonal components to occur in reverse pairs, with nonzero reverse products; otherwise one of these components would generate a proper graded ideal. Associativity and \(C_1^2\subseteq C_0\) prohibit two distinct neighbors at one vertex: if \(0\ne x\in M_{ij}\), \(0\ne y\in M_{ji}\) with \(xy\ne0\), and \(0\ne z\in M_{ik}\) for \(k\ne j\), then \((xy)z\ne0\) but \(x(yz)=0\). The graph of the \(M_{ij}\) is connected by graded simplicity, so \(r\le2\).

If \(r=2\), the diagonal degree-one corners vanish: if \(0\ne x\in M_{ii}\) and \(0\ne y\in M_{ij}\), then \(xy=yx=0\); associativity forces \(M_{ii}^2=0\), so \(M_{ii}\) would be a proper graded ideal. The two off-diagonal components pair nontrivially. Choose \(x\in M_{12}\), \(y\in M_{21}\) with \(xy=e_1\); then \(yx=e_2\). For every \(z\in M_{12}\), \(z=(zy)x=x(yz)\), so \(M_{12}=K_1x=xK_2\), forcing \(K_1\cong K_2=K\) and both off-diagonal components to be one-dimensional over \(K\). Rescaling gives matrix units. Thus \(C\cong M_2(K)\) with the elementary grading.

If \(r=1\), write \(C_0=K\). If \(C_1=0\), then \(C=K\). Otherwise every nonzero element of \(C_1\) is invertible: if an element annihilated \(C_1\) on both sides, its \(K\)-span would be a proper graded ideal; any nonzero product of two degree-one elements lies in \(K^\times\), making the first element invertible. It follows that \(C_1=Ku\) is one-dimensional over \(K\). Conjugation by \(u\) induces an automorphism \(\sigma\) of \(K\), and \(u^2\in K^\sigma\) implies \(\sigma^2=1\). If \(\sigma=1\), perfectness of the finite field lets us rescale \(u\) so \(u^2=1\), giving \(K[C_2]\). If \(\sigma\ne1\), then \(K/K^\sigma\) is quadratic; surjectivity of its norm lets us again normalize \(u^2=1\). The resulting crossed product is \(\operatorname{End}_{K^\sigma}(K)\cong M_2(K^\sigma)\), with degree-zero part \(K\) and degree-one part \(Ku\), giving type 4. This exhausts the graded-simple summands.

## Verification

The proof uses only finite-dimensionality, the reducedness of \(A_0\), separability of finite fields, and the defining multiplication rules of a grading. The included standalone checker exhaustively verifies the explicit field-grading example in \(M_2(\mathbb F_2)\), including the direct-sum decomposition and all grading-compatible products. That finite check is illustrative; the universal statement follows from the proof above.

## Relationship to prior work

Diniz, Pinto da Fonsêca, and Ramos prove a graded Wedderburn decomposition for characteristic-two \(\mathbb Z/2\mathbb Z\)-graded algebras under the stronger identity \(x^q=x\) on the neutral component; their component list is \(F\), \(F[C_2]\), and the elementary grading on \(M_2(F)\). Reducedness is strictly weaker: it allows degree-zero field extensions of \(F\), which need not satisfy \(x^q=x\). The result here replaces that polynomial-identity hypothesis with reducedness and records the extension-field components that then occur. The general classification of graded-division algebras explains the crossed-product building blocks, but does not state this radical-splitting criterion for arbitrary finite-dimensional graded algebras.

## Limitations

The theorem relies on the fact that finite fields are perfect and that the degree-zero algebra is reduced. It does not establish a corresponding result for arbitrary imperfect fields, nonassociative algebras, or grading groups other than \(\mathbb Z/2\mathbb Z\). The classification of graded-simple summands is specific to the two-component grading and the reduced neutral component.

## References

1. D. Diniz, E. Pinto da Fonsêca, and L. F. Ramos, “Graded identities for matrix algebras of order two over a finite field,” first posted 2026-05-28, arXiv:2605.30494v1, especially Theorem 21 and Theorem 6. https://arxiv.org/abs/2605.30494
2. Y. Bahturin, A. Elduque, and M. Kochetov, “Graded-division algebras over arbitrary fields,” arXiv:1912.11911, especially §§1–2. https://arxiv.org/abs/1912.11911
3. “Wedderburn–Mal'tsev theorem,” Encyclopedia of Mathematics, for the ungraded separable-complement context. https://encyclopediaofmath.org/wiki/Wedderburn-Mal%27tsev_theorem
