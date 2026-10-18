# Rank-refined square-zero selfadjoint sum fibers for split semisimple targets

## Finding

Let \(q\) be an odd prime power, \(V\) a finite-dimensional vector space over \(\mathbb F_q\), and \(b\) a nondegenerate symmetric bilinear form on \(V\). For a \(b\)-selfadjoint, diagonalizable (over \(\mathbb F_q\)) operator \(C\), define the ordered decomposition-rank polynomial
\[
F_C(z)=\sum_{\substack{A+B=C\\A^2=B^2=0\\A^*=A,\ B^*=B}}z^{\operatorname{rank}A},
\]
where \(^*\) means adjoint with respect to \(b\). This determines the number of decompositions at each summand rank. Every decomposition has \(\operatorname{rank}A=\operatorname{rank}B\).

Write \(V_\lambda=\ker(C-\lambda I)\) for \(\lambda\in\mathbb F_q\). Distinct eigenspaces are pairwise \(b\)-orthogonal and each is nondegenerate. Choose one scalar from each nonempty pair \(\{\lambda,-\lambda\}\) with \(\lambda\ne0\). If any paired eigenspaces have unequal dimensions, or if they have the same dimension \(m_\lambda\) but
\[
\chi_q\!\left((-1)^{m_\lambda}\det(b|_{V_\lambda})\det(b|_{V_{-\lambda}})\right)=-1,
\]
then \(F_C(z)=0\). Here \(\chi_q\) is the quadratic character on nonzero field elements, and determinant square classes do not depend on basis.

Otherwise put \(M=\sum_{\{\lambda,-\lambda\}}m_\lambda\), \(V_0=\ker C\), \(d=\dim V_0\), and let \(w\) be the Witt index of \(b|_{V_0}\). Then
\[
\boxed{F_C(z)=z^M\left(\prod_{\{\lambda,-\lambda\}}|O(V_\lambda,b|_{V_\lambda})|\right)\sum_{r=0}^{w}I_r(d,\varepsilon;q)S_r(q)z^r.}
\]
The empty product equals \(1\). Here \(S_r(q)\) counts invertible symmetric \(r\)-by-\(r\) matrices, \(I_r(d,\varepsilon;q)\) counts totally isotropic \(r\)-subspaces of \((V_0,b|_{V_0})\), and both factors have the explicit product formulas below. Thus every rank from \(M\) through \(M+w\) occurs with the displayed positive multiplicity, and none other occurs. In particular, when \(C\) is invertible, every decomposition has rank \(M=\dim(V)/2\) and the number of ordered decompositions is exactly the product of orthogonal-group orders.

## Assumptions and scope

The form \(b\) is nondegenerate and symmetric, the field has odd cardinality, and the target \(C\) is \(b\)-selfadjoint and split semisimple. The theorem does not assert a corresponding formula for nonsemisimple targets or for nonsplit irreducible eigenvalue factors. The convention for zero-dimensional spaces and zero-rank matrices is that their groups and counting factors have order \(1\).

For explicit evaluation define \(\varepsilon=\chi_q((-1)^{d/2}\det(b|_{V_0}))\) when \(d\) is positive and even; in odd dimension the symbol \(\varepsilon\) is immaterial. If \(d=2k+1\) then \(w=k\). If \(d=2k>0\), then \(w=k\) when \(\varepsilon=1\) and \(w=k-1\) when \(\varepsilon=-1\); if \(d=0\), then \(w=0\).

Set \(I_0=1\). For \(1\le r\le w\), write
\[
I_r(d,\varepsilon;q)=\frac{\prod_{i=0}^{r-1}L(d-2i,\varepsilon;q)}{\prod_{j=1}^{r}(q^j-1)/(q-1)},
\]
where the isotropic-line count is
\[
L(h,\varepsilon;q)=\begin{cases}
(q^{h-1}-1)/(q-1),&h\text{ odd},\\
(q^{h-1}-1+\varepsilon(q-1)q^{h/2-1})/(q-1),&h\text{ even}.
\end{cases}
\]
The even-dimensional sign remains unchanged after quotienting by a hyperbolic plane.

Set \(S_0(q)=1\). For \(r>0\) define \(g_r=\prod_{i=0}^{r-1}(q^r-q^i)=|\operatorname{GL}_r(q)|\). Then
\[
S_r(q)=\begin{cases}
2g_r/|O_r(q)|,&r\text{ odd},\\
g_r/|O_r^+(q)|+g_r/|O_r^-(q)|,&r\text{ even}.
\end{cases}
\]
For \(r=2k+1\) the orthogonal-group order is \(2q^{k^2}\prod_{i=1}^k(q^{2i}-1)\). For \(r=2k>0\), the order of orthogonal type \(\sigma\in\{+1,-1\}\) is \(2q^{k(k-1)}(q^k-\sigma)\prod_{i=1}^{k-1}(q^{2i}-1)\). A nondegenerate even-dimensional symmetric form of dimension \(2k\) has type \(\sigma=\chi_q((-1)^k\det b)\). Thus every factor is computable from field size and the eigenspace forms.

## Proof

First, each eigenspace \(V_\lambda\) is nondegenerate and orthogonal to all other eigenspaces, since \(\lambda b(v,w)=b(Cv,w)=b(v,Cw)=\mu b(v,w)\) for eigenvectors with distinct eigenvalues.

Second, if \(A+B=C\) and \(A^2=B^2=0\), then \(CA+AC=C^2\). On the \((\lambda,\mu)\)-block, this Sylvester equation reads \((\lambda+\mu)A_{\lambda\mu}=\lambda^2\mathbf1_{\lambda=\mu}\,I\). As the characteristic is odd, every nonzero eigenvalue block has \(A_{\lambda\lambda}=\lambda I/2\), and all off-diagonal blocks vanish except possibly the blocks between \(\lambda\) and \(-\lambda\). The zero-eigenspace block \(A_{00}\) is unrestricted by this equation. Its off-diagonal interactions with nonzero eigenspaces vanish. Since \(A\) is selfadjoint, each nonzero pair block has the exact form
\[
A|_{V_\lambda\oplus V_{-\lambda}}=\begin{pmatrix}\lambda I/2&X\\X^*&-\lambda I/2\end{pmatrix}.
\]
Squaring shows that \(XX^*=X^*X=-\lambda^2 I/4\). Therefore \(X\) is invertible, the paired eigenspaces have equal dimension \(m_\lambda\), and \(T=2X/\lambda\) is an anti-isometry: \(b(Tu,Tv)=-b(u,v)\) for \(u,v\in V_{-\lambda}\), with the left form restricted to \(V_\lambda\). Conversely every such anti-isometry constructs a pair of square-zero selfadjoint summands on that block. Nondegenerate symmetric forms over an odd finite field are classified by dimension and determinant square class, so an anti-isometry exists exactly under the stated character condition. If it exists, the anti-isometries constitute a torsor for \(O(V_\lambda,b|_{V_\lambda})\), giving the precise orthogonal-group factor. The square-zero block has kernel dimension \(m_\lambda\), hence rank \(m_\lambda\), for each summand.

Third, on \(V_0\) one has \(B_0=-A_0\), where \(A_0=A_0^*\) and \(A_0^2=0\). For any such \(A_0\), its image \(U\) is totally isotropic and its kernel is \(U^\perp\) (because \(A_0=A_0^*\)). Conversely, for each totally isotropic \(r\)-plane \(U\), the maps of rank \(r\) with image \(U\), kernel \(U^\perp\), and \(A_0=A_0^*\) correspond bijectively to nonsingular symmetric linear identifications \(U^*\to U\). Relative to a basis, these are exactly the invertible symmetric \(r\)-by-\(r\) matrices, counted by \(S_r(q)\).

Finally, count isotropic \(r\)-planes using complete flags of isotropic subspaces. At a flag stage of dimension \(i\), extension by one dimension is a choice of an isotropic line in \(U_i^\perp/U_i\), a nondegenerate space of dimension \(d-2i\). The classical finite-field zero count for a nondegenerate quadratic form gives \(L(d-2i,\varepsilon;q)\) such lines. For completeness, diagonalize the quotient form as \(Q(x)=\sum_{j=1}^{h}a_jx_j^2\) and apply the additive-character identity \(\#Q^{-1}(0)=q^{-1}\sum_{t\in\mathbb F_q}\sum_x\psi(tQ(x))\). For \(t\ne0\), the inner sum is \(\chi_q(t)^h\chi_q(\prod_j a_j)G^h\), where the one-variable Gauss sum obeys \(G^2=\chi_q(-1)q\). Summing \(t\ne0\) yields \(q^{h-1}\) zeros for odd \(h\) and \(q^{h-1}+\varepsilon(q-1)q^{h/2-1}\) zeros for even \(h\), including the zero vector. Subtract one and divide by \(q-1\) to obtain the isotropic-line formula. Divide the product of these choices by the number \(\prod_{j=1}^r(q^j-1)/(q-1)\) of complete flags within an \(r\)-space. This gives \(I_r\). Counting nonsingular symmetric forms by the two congruence classes and their orthogonal stabilizers gives \(S_r\), while the classical orthogonal group orders give its explicit factors. Multiplying the independent eigenspace contributions completes the polynomial identity and the rank-support assertion.

## Verification

The standalone script `check.py` constructs finite fields \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_9\), enumerates selfadjoint matrices by symmetric matrices \(H=GA\), tests \(A^2=(C-A)^2=0\) by actual field multiplication, and computes the ranks of both factors. It independently evaluates the product formulas and compares complete rank distributions. Its fixed test set includes split and anisotropic zero targets, permitted and excluded paired-eigenvalue targets, a four-dimensional hyperbolic zero target, mixed zero/nonzero eigenspaces, and an extension-field example. A separate exhaustive batch checked all \(258\) diagonal form/target cases of dimensions at most three over \(\mathbb F_3\).

For \(q=3\), a four-dimensional split form and \(C=0\) yield \(F_C(z)=1+32z+144z^2\). On the same form, a target with diagonal eigenvalues \(1,-1,0,0\) yields \(F_C(z)=2z+8z^2\). With \(b\) the identity form in dimension four and target eigenvalues \(1,1,-1,-1\), one obtains \(F_C(z)=8z^2\); changing the determinant type on exactly one of the two eigenspaces makes the fiber vanish.

These finite computations check the stated formulas in the enumerated cases; the proof, not the enumeration, covers arbitrary odd prime powers and dimensions.

## Relationship to prior work

De Seguins Pazzis, *Sums of two square-zero selfadjoint or skew-selfadjoint endomorphisms* (arXiv:2210.03955v1, 2022), proves general existence classifications, including Theorem 1.15 and the finite-field quadratic-form conditions in Section 1.6.3. Its Sections 1.5 and 4.2 were inspected for direct implication. The present result works within the split-semisimple selfadjoint case, does not claim a new existence criterion, and refines it to exact ordered-fiber counts and the summand-rank generating polynomial.

The nonsingular symmetric-matrix orbit counts, orthogonal-group orders, and isotropic-subspace incidence counts used in the formula are classical. The rank-counting literature, including Fulman--Goldstein's work on symmetric random matrices, is background rather than an asserted novelty. The contribution asserted here is their interaction in prescribed selfadjoint square-zero sum fibers. An equivalent enumerative formulation in older quadratic-form or decomposition literature has not been ruled out absolutely.

## Limitations

The theorem requires odd characteristic, a nondegenerate symmetric form, and a split-semisimple target. It does not cover arbitrary nilpotent Jordan blocks, nonsplit eigenvalues, characteristic two, or all decompositions into unrestricted (not selfadjoint) square-zero operators. No independent mathematical validation has been performed. The primary remaining originality risk is unlocated prior enumeration under an isometry-torsor or constrained Sylvester-equation formulation.

## References

1. C. de Seguins Pazzis, *Sums of two square-zero selfadjoint or skew-selfadjoint endomorphisms*, arXiv:2210.03955v1, first submitted 2022-10-08, https://arxiv.org/abs/2210.03955 . Relevant: Sections 1.5, 1.6.3, 4.2.
2. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504, https://arxiv.org/abs/1211.0504 . Background for symmetric-matrix rank counting; the abstract alone was consulted.
3. Standard finite-orthogonal-group order and isotropic-line formulas, as derived and explicitly specified above. No external table is required for evaluating the stated polynomial.
