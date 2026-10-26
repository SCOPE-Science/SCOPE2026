# Finite-field fixed-point-free automorphism counts for standard filiform Lie algebras

## Finding

Let \(q\) be any prime power and \(n\ge4\). Define \(L_n(q)\) over \(\mathbb F_q\) with basis \(e_1,\ldots,e_n\) and brackets
\[
[e_1,e_i]=e_{i+1}\qquad(2\le i<n),
\]
with all other basis brackets zero except those forced by alternation. Let \(F_n(q)\) be the number of automorphisms \(\sigma\) satisfying \(\ker(\sigma-I)=0\). Writing \(\phi\) for Euler's totient function,
\[
\boxed{F_n(q)=q^{2n-3}\sum_{\substack{d\mid q-1\\d>1}}\phi(d)\bigl(q-1-\min\{d,n-1\}\bigr).}
\]
The exact existence boundary is
\[
F_n(q)>0\quad\Longleftrightarrow\quad n<q\ \text{or}\ q-1\ \text{is composite}.
\]
For the four-dimensional case this simplifies to
\[
F_4(q)=\begin{cases}q^5(q-3)^2,&q\text{ odd},\\q^5(q-2)(q-4),&q\text{ even}.\end{cases}
\]

## Assumptions and scope

The bracket table defines a Lie algebra over every finite field, including characteristic two. The claim concerns only the standard filiform family \(L_n(q)\) with \(n\ge4\); it does not claim a count for the three-dimensional Heisenberg algebra, for the even-dimensional family \(Q_n\), or for nonstandard filiform deformations. Fixed-point-free means that the zero vector is the only vector fixed by the automorphism.

## Proof

The only nonzero brackets involve \(e_1\) and one basis vector \(e_i\) with \(i\ge2\); brackets between vectors in \(\langle e_2,\ldots,e_n\rangle\) vanish. The Jacobi identity follows directly from these relations, including in characteristic two. The lower central series is \(L_n^k=\langle e_{k+1},\ldots,e_n\rangle\) for \(2\le k<n\).

Let \(\sigma\) be an automorphism. Initially write
\[
\sigma(e_1)=a e_1+c_2e_2+\cdots+c_ne_n,
\qquad
\sigma(e_2)=u e_1+b e_2+d_3e_3+\cdots+d_ne_n.
\]
The induced map on \(L_n/L_n^2\) is invertible, so \(\Delta=ab-c_2u\ne0\). Since \(\sigma(e_3)=[\sigma(e_1),\sigma(e_2)]\), its leading \(e_3\)-coefficient is \(\Delta\). The relation \([e_2,e_3]=0\) gives \([\sigma(e_2),\sigma(e_3)]=0\); its \(e_4\)-coefficient is \(u\Delta\). Because \(n\ge4\) and \(\Delta\ne0\), we obtain \(u=0\). Thus \(a,b\ne0\).

Conversely, choose any \(a,b\in\mathbb F_q^\times\), any \(c_2,\ldots,c_n\in\mathbb F_q\), and any \(d_3,\ldots,d_n\in\mathbb F_q\). The displayed assignments, extended recursively by \(\sigma(e_{i+1})=[\sigma(e_1),\sigma(e_i)]\), preserve every defining bracket. Their matrices are triangular with nonzero diagonal, so they are automorphisms. This parametrization is unique. There are \(n-1\) free coefficients among the \(c_i\) and \(n-2\) among the \(d_i\), so
\[
|\operatorname{Aut}(L_n(q))|=q^{2n-3}(q-1)^2.
\]
The diagonal entries of every such automorphism are
\[
a,\ b,\ ab,\ a^2b,\ldots,a^{n-2}b.
\]
A triangular matrix has no eigenvalue equal to \(1\) exactly when none of these entries equals \(1\). Therefore \(a\ne1\), and for fixed \(a\), the forbidden values of \(b\) are
\[
1,a^{-1},a^{-2},\ldots,a^{-(n-2)}.
\]
If \(a\) has multiplicative order \(d\), these values have exactly \(\min\{d,n-1\}\) distinct members. Hence there are \(q-1-\min\{d,n-1\}\) admissible values of \(b\). For each divisor \(d>1\) of \(q-1\), exactly \(\phi(d)\) elements of \(\mathbb F_q^\times\) have order \(d\). Multiplying the resulting pair count by the \(q^{2n-3}\) choices of the free coefficients proves the boxed formula.

For positivity, a summand is positive precisely when \(\min\{d,n-1\}<q-1\). If \(n<q\), then \(n-1<q-1\) and a positive summand exists. If \(n\ge q\), then the condition becomes the existence of a proper divisor \(d\) of \(q-1\) with \(d>1\), which is equivalent to \(q-1\) being composite. This proves the stated boundary, including \(q=2\), where the sum is empty. For \(n=4\), put \(m=q-1\). If \(m\) is even, the divisor \(d=2\) contributes \(m-2\), and all other nontrivial divisors contribute \(m-3\); using \(\sum_{d\mid m,\ d>1}\phi(d)=m-1\) gives the divisor sum \((m-2)^2\). If \(m\) is odd, every nontrivial divisor is at least \(3\), so the sum is \((m-1)(m-3)\). Substituting \(m=q-1\) yields the displayed \(F_4(q)\) formulas.

## Verification

The standalone file `verification/check_formula.py` checks the divisor-sum identity against a separate enumeration of admissible exponent pairs in a cyclic group of order \(q-1\). It checks the positivity criterion for \(243\) pairs \((q,n)\), using prime powers \(q\le64\) and \(4\le n\le12\), and checks the \(n=4\) simplification for all \(27\) prime powers in that range. Its output is `CHECK_OK`. These are arithmetic consistency checks; the universal claim is proved symbolically above, not by finite enumeration of all automorphisms.

## Relationship to prior work

Bahturin, Goze, and Remm define the standard filiform family \(L_n\) and describe its triangular automorphisms and diagonal torus weights in *Group gradings on filiform Lie algebras* (arXiv:1308.2396v1, first public on 2013-08-11). Their paper studies gradings over algebraically closed fields of characteristic different from two; it does not give a fixed-point-free automorphism census over finite fields. The direct argument above handles all finite characteristics.

Burde and Dekimpe prove a characteristic-zero existence criterion for fixed-point-free automorphisms of complex filiform Lie algebras in arXiv:2604.27916v1. That criterion concerns existence over \(\mathbb C\), not the exact number over \(\mathbb F_q\). The closest related finite-field count inspected concerns the three-dimensional Heisenberg algebra, a different bracket structure; its opaque record identifier is `17f0de4cb789`. Another inspected result gives adjoint-rank spectra and element commutativity degrees for \(L_n(q)\), not automorphism fixed-point counts; its opaque record identifier is `48cdbeaf7d86`. Neither result implies the divisor-sum formula above.

## Limitations

The formula is only for the explicitly defined standard filiform family with \(n\ge4\). It does not classify fixed-point-free automorphisms by order, conjugacy class, or fixed-space dimension, and it does not treat arbitrary filiform deformations. The arithmetic checker is not an independent proof of the automorphism parametrization.

## References

1. Y. Bahturin, M. Goze, and E. Remm, *Group gradings on filiform Lie algebras*, arXiv:1308.2396v1, first public 2013-08-11. https://arxiv.org/abs/1308.2396
2. D. Burde and K. Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras*, arXiv:2604.27916v1, first public 2026-04-30. https://arxiv.org/abs/2604.27916
3. *Fixed-point-free automorphism count for the three-dimensional Heisenberg Lie algebra*, opaque record ID `17f0de4cb789` (different algebra).
4. *Adjoint-rank spectra of two maximal-class filiform Lie algebras*, opaque record ID `48cdbeaf7d86` (different invariant).
