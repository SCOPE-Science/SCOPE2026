# Stable integral Cartan forms under singular equivalence of centralizer matrix algebras

## Statement

Let \(k\) be a field, let \(c\in M_n(k)\), and write
\[
A=S_n(c,k)=\{x\in M_n(k):xc=cx\}.
\]
Let \(C_A\) be the Cartan matrix of \(A\), equivalently of a basic algebra Morita equivalent to \(A\), and define the Cartan group
\[
G(A):=\operatorname{coker}\!\left(C_A:\mathbb Z^r\to\mathbb Z^r\right).
\]

For each irreducible polynomial \(f\) occurring in the minimal polynomial of \(c\), let
\[
T_f(c)=\{t_1>\cdots>t_s\}
\]
be the set of distinct exponents for which \(f^{t_i}\) occurs as an elementary divisor of \(c\), and put
\[
H(T_f(c))=\{\!\{t_1-t_2,\ldots,t_{s-1}-t_s,t_s\}\!\}.
\]
Let \(U_c\) be the multiset union of all \(H(T_f(c))\) after deleting every occurrence of \(1\).

Then:

1. **Explicit stable integral Cartan form.**
   If \(r\) is the number of simple \(A\)-modules, then \(C_A\) is integrally congruent to
   \[
   \operatorname{diag}(U_c,1,\ldots,1),
   \]
   with \(r-|U_c|\) trailing \(1\)'s. Consequently
   \[
   G(A)\simeq \bigoplus_{u\in U_c}\mathbb Z/u\mathbb Z.
   \]

2. **Singular-equivalence invariance.**
   If \(B=S_m(d,k)\) is another centralizer matrix algebra and
   \[
   \mathscr D_{sg}(A)\simeq\mathscr D_{sg}(B)
   \]
   as triangulated \(k\)-categories, then \(C_A\) and \(C_B\) are stably integrally congruent: after adjoining enough \(1\times1\) identity blocks to the smaller Cartan matrix, the two matrices are congruent over \(\mathbb Z\). In particular,
   \[
   G(A)\simeq G(B).
   \]
   Thus the entire Cartan group, not only the Cartan determinant, is an invariant of singular equivalence within the class of centralizer matrix algebras.

3. **Universal realization.**
   Every finite abelian group occurs as the Cartan group of a nilpotent centralizer matrix algebra over every field.

## Proof

The primary decomposition of the \(k[x]\)-module \(k^n\) decomposes \(A\) as a product of primary endomorphism algebras. Replacing each primary module by its basic module does not change the Morita class or Cartan matrix up to simultaneous permutation of rows and columns.

For one primary component with distinct exponents
\[
T=\{t_1>\cdots>t_s\},
\]
the Cartan matrix is
\[
C_T=(\min(t_i,t_j))_{1\le i,j\le s}
 =
\begin{pmatrix}
t_1&t_2&\cdots&t_s\\
t_2&t_2&\cdots&t_s\\
\vdots&\vdots&\ddots&\vdots\\
t_s&t_s&\cdots&t_s
\end{pmatrix}.
\]
This is the Cartan-matrix formula of Dubey--Prasad--Singla, in the arbitrary-field form recorded by Chen--Xi. Successive simultaneous integral row and column differences give a unimodular matrix \(P_T\) such that
\[
P_T^{\,T}C_TP_T
 =
\operatorname{diag}(t_1-t_2,\ldots,t_{s-1}-t_s,t_s).
\]
The same integral congruence is stated explicitly in Li--Xi, Lemma 2.18. Taking the block sum over the primary components proves (1); entries equal to \(1\) contribute trivial cyclic summands to the cokernel.

Chen--Xi classify singular equivalences of centralizer matrix algebras by \(Sg\)-equivalence. In their notation, \(Sg\)-equivalent matrices have the same multiset \(\mathcal U\), which is exactly the union of the above gap multisets after deleting all \(1\)'s. Hence singular equivalence gives
\[
U_c=U_d.
\]
By (1), \(C_A\) and \(C_B\) therefore become the same diagonal integral form after adding enough unit diagonal entries. This proves stable integral congruence. Since left and right multiplication by unimodular integer matrices does not change the cokernel, \(G(A)\simeq G(B)\), proving (2).

For (3), let
\[
G\simeq\bigoplus_{i=1}^s\mathbb Z/d_i\mathbb Z
\qquad(d_i\ge2)
\]
be any nontrivial finite abelian group. Define
\[
t_i=d_i+d_{i+1}+\cdots+d_s
\]
and take
\[
N:=t_1+\cdots+t_s,\qquad c=J_{t_1}(0)\oplus\cdots\oplus J_{t_s}(0)\in M_N(k).
\]
Then \(t_1>\cdots>t_s\) and
\[
H(T)=\{\!\{d_1,\ldots,d_s\}\!\},
\]
so (1) yields
\[
G(S_N(c,k))\simeq G.
\]
The trivial group is realized by a one-block semisimple example. This works over an arbitrary field.

## Strict refinement of the determinant invariant

Take
\[
c=J_4(0)\oplus J_2(0),\qquad
d=J_5(0)\oplus J_1(0).
\]
Their basic Cartan matrices are
\[
C_c=\begin{pmatrix}4&2\\2&2\end{pmatrix},
\qquad
C_d=\begin{pmatrix}5&1\\1&1\end{pmatrix}.
\]
Both determinants equal \(4\), but
\[
G(S_6(c,k))\simeq \mathbb Z/2\mathbb Z\oplus\mathbb Z/2\mathbb Z,
\qquad
G(S_6(d,k))\simeq \mathbb Z/4\mathbb Z.
\]
Hence equality of Cartan determinants cannot recover the new invariant, and these two centralizer matrix algebras cannot be singularly equivalent.

## Relation to prior work

Dubey, Prasad and Singla computed the Cartan matrices of centralizer algebras and their determinants. Li and Xi later used the integral congruence class of these Cartan matrices in their classification of derived equivalences. Chen and Xi classified singular equivalences and proved that the Cartan determinant is preserved under them. The result above combines the integral Cartan form with the singular-equivalence classification to retain the full stable integral form and Cartan cokernel.

The Cartan group \(G(A)=\operatorname{coker}C_A\) is a standard invariant of finite-dimensional algebras; Mendoza, Sáenz and Marcos studied it systematically and proved, among other results, that every finite abelian group can occur for a standardly stratified algebra. The realization above places that universality inside the much more concrete class of nilpotent one-matrix centralizer algebras.

## Limitations

- The singular-equivalence invariance is asserted only for centralizer matrix algebras; no analogous statement is claimed for arbitrary finite-dimensional algebras.
- The integral diagonalization itself is not new: it appears explicitly in Li--Xi. The contribution here is the stable form and Cartan-group consequence for the weaker singular equivalence, together with the nilpotent-centralizer realization.
- Originality is to the best of our knowledge. Searches for the exact result and synonymous formulations involving Cartan cokernels, Cartan groups, Smith normal forms, and stable integral congruence did not locate an earlier centralizer-specific statement. An equivalent observation could exist under different terminology.

## References

1. U. V. Dubey, A. Prasad, P. Singla, *The Cartan Matrix of a Centralizer Algebra*, Proc. Indian Acad. Sci. Math. Sci. 122 (2012), 67--73. Preprint: https://arxiv.org/abs/math/0611897
2. X. Li, C. Xi, *Derived and stable equivalences of centralizer matrix algebras*, arXiv:2312.08794. https://arxiv.org/abs/2312.08794
3. Z. Chen, C. Xi, *Singular equivalences and homological conjectures*, arXiv:2603.20643v2 (2026). https://arxiv.org/abs/2603.20643
4. O. Mendoza, C. Sáenz, E. N. Marcos, *Cokernels of the Cartan Matrix and Stratifying Systems*, Comm. Algebra 47 (2019). https://arxiv.org/abs/1804.01168
