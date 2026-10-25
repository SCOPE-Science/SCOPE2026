# Conjugacy classes and centralizers of involutions in free class-two Lie automorphism groups

## Finding
Let \(q\) be an odd prime power, \(n\geq3\), \(V=\mathbb F_q^n\), and \(L=V\oplus\bigwedge^2V\) with \([v+w,v'+w']=v\wedge v'\). Put \(W=\bigwedge^2V\) and \(m=\binom n2\). For each \(0\leq r\leq n\), define \(t=n-r\), \(a_r=\binom r2+\binom t2\), and \(b_r=rt\). Every order-dividing-two automorphism \(\varphi\) of \(L\) has a unique parameter \(r=\dim\ker(\bar\varphi-I)\) for its action on \(L/W\). **All such automorphisms with the same \(r\) form one conjugacy class**, whose representative acts by \(+I\) on an \(r\)-dimensional subspace of \(V\), by \(-I\) on its \(t\)-dimensional complement, and by the exterior-square representation on \(W\). Its centralizer in \(\operatorname{Aut}(L)\) has order
\[
C_{n,q}(r)=|\operatorname{GL}_r(\mathbb F_q)|\,|\operatorname{GL}_t(\mathbb F_q)|\,q^{r a_r+t b_r}.
\]
Its conjugacy-class size is
\[
I_{n,q}(r)={n\brack r}_q\,q^{rt+r b_r+t a_r}.
\]
The classes \(r=0,\ldots,n-1\) consist of genuine order-two automorphisms; \(r=n\) is the identity. In particular, the group has exactly \(n\) conjugacy classes of nonidentity involutions and an exact total involution count \(\sum_{r=0}^{n-1}I_{n,q}(r)\). The entire result is valid for all odd field orders, including fields of odd nonprime order.

For fixed odd \(q\), a uniformly selected automorphism among those satisfying \(\varphi^2=I\) belongs, with probability tending to one as \(n\to\infty\), to the \(r=0\) class, whose induced action on the abelianization is \(-I\) while it fixes the derived ideal pointwise. Explicitly, with \(K_q=\prod_{j\geq1}(1-q^{-j})^{-1}\) and \(n\geq20\),
\[
0\leq1-\frac{q^{n\binom n2}}{\sum_{r=0}^n I_{n,q}(r)}\leq\frac{K_q q^{-n^2/4}}{1-q^{-n^2/4}}.
\]

## Assumptions and scope
An involution here means an automorphism of exact order two, except that counting \(\varphi^2=I\) includes the identity explicitly. Every automorphism of the free class-two Lie algebra induces an invertible map on \(V=L/[L,L]\). The quotient rank parameter \(r\) is invariant under conjugation. The classification is of **actual conjugacy classes in the full Lie automorphism group**, not gradings modulo arbitrary equivalence. Odd characteristic is essential to the conjugacy argument; no assertion is made about involutions in characteristic two.

## Proof
**Automorphism coordinates.** The canonical vector-space decomposition \(L=V\oplus W\), together with the free bracket, gives every automorphism uniquely in the form \(\varphi_{A,f}(v+w)=Av+f(v)+(\bigwedge^2A)w\), with \(A\in\operatorname{GL}(V)\) and \(f\in\operatorname{Hom}(V,W)\). Composition gives \(\varphi_{A,f}^2=I\) if and only if
\[
A^2=I,\qquad fA+(\bigwedge^2 A)f=0.
\]
Since \(q\) is odd, \(A\) is diagonalizable with \(V=U\oplus T\), eigenvalues \(+1\) and \(-1\), and dimensions \(r,t\). The exterior-square action \(B=\bigwedge^2A\) has \(+1\)-eigenspace \(W_+=\bigwedge^2U\oplus\bigwedge^2T\) of dimension \(a_r\), and \(-1\)-eigenspace \(W_-=U\wedge T\) of dimension \(b_r\). Thus the displayed involution equation is equivalent to \(f(U)\subseteq W_-\), \(f(T)\subseteq W_+\), with precisely \(q^{r b_r+t a_r}\) solutions for each \(A\).

**Conjugacy and class size.** Fix \(A\). For any solution \(f\), let \(h:V\to W\) equal \(-\frac12 fA\); conjugation by the central shear \(\sigma_h(v+w)=v+h(v)+w\) replaces the central component by \(f+hA-Bh\), which vanishes for this choice because \(Bf=-fA\) and \(A^2=I\). Hence each involution is conjugate to \(\varphi_{A,0}\). Every matrix involution with \(r\)-dimensional \(+1\)-eigenspace is conjugate in \(\operatorname{GL}(V)\) to \(\operatorname{diag}(I_r,-I_t)\), and conjugation lifts to \(\operatorname{Aut}(L)\). Conversely, conjugation preserves \(r\). There are \({n\brack r}_q q^{rt}\) choices for \(A\), since the eigenspaces are ordered complementary subspaces. Multiplication by the independently counted \(f\)'s gives the class size \(I_{n,q}(r)\).

**Centralizer.** A centralizing automorphism has linear part \(P\in\operatorname{GL}(V)\) commuting with \(A\), hence \(P\in\operatorname{GL}(U)\times\operatorname{GL}(T)\). Its central component \(g:V\to W\) obeys \(gA=Bg\), equivalent to \(g(U)\subseteq W_+\), \(g(T)\subseteq W_-\). This vector space has dimension \(r a_r+t b_r\), so the centralizer order is \(C_{n,q}(r)\). This also independently confirms the class size because the full automorphism group has order \(|\operatorname{GL}_n(\mathbb F_q)|q^{nm}\).

**Limiting concentration.** Write \(E_{n,r}=rt+r^2t+t(\binom r2+\binom t2)\). Then direct simplification gives \(nm-E_{n,r}=\frac r2(3n^2-6nr+4r^2-3n+2r)\). Using \(4r^2-6nr+3n^2=4(r-3n/4)^2+3n^2/4\) and \({n\brack r}_q\leq K_q q^{r(n-r)}\), for each \(r\geq1\) and \(n\geq20\), \(I_{n,q}(r)/I_{n,q}(0)\leq K_q q^{-r n^2/4}\). Sum the geometric majorant and divide by the total, which is at least \(I_{n,q}(0)=q^{nm}\). The \(r=0\) model fixes all of \(W\) because \(\bigwedge^2(-I)=I\). Thus the exact bound and asserted limit hold.

## Verification
The standalone `verify_involutions.py` directly enumerates all \(n\)-square matrices over the tested prime fields, keeps those with \(A^2=I\), builds the exterior-square action from \(2\times2\) minors, and computes the nullity of the linear system \(fA+(\bigwedge^2A)f=0\) without assuming the claimed decomposition. It independently finds the \(+1\)-eigenspace dimension of each \(A\) and matches the resulting complete class-size vector. The observed vectors indexed by \(r\) are \((9,36,1)\) for \((n,q)=(2,3)\), \((25,150,1)\) for \((2,5)\), and \((19683,9477,28431,1)\) for \((3,3)\). At \((3,3)\), it also checks all centralizer/class-size identities against \(|\operatorname{Aut}(L)|\). The rank-two cases are structural boundary checks, not part of the claimed new rank range. Execute `python verify_involutions.py`; the final line is `ALL_INVOLUTION_CHECKS_OK`. The general theorem follows from the proof, not from finite tests.

## Relationship to prior work
Benito and Roldán-López describe structural automorphism coordinates for free nilpotent Lie algebras. Cagliero, Gutiérrez Frez and Szechtman work with the same free class-two exterior-square model but examine uniserial representations. Hakavuori et al. study grading structures over characteristic-zero fields, up to equivalence. Eick and Moede study parity gradings of **simple** modular Lie algebras rather than full conjugacy classes and centralizers of automorphisms in this free class-two family. Prior counts of composition-idempotent derivations in characteristic two have a related Gaussian polynomial but involve a different operator equation and do not establish conjugacy or centralizer orders for **odd-characteristic involutive automorphisms**. The claimed contribution is the entire odd-characteristic involution conjugacy and centralizer distribution and its concentration law, not the familiar semidirect-product description of the automorphism group.

## Limitations
Only odd-characteristic finite fields and free class-two algebras are treated, not proper central quotients or characteristic-two involutions. The concentration bound is sufficient rather than optimal. The conjugacy-counting argument assumes labels \(+1,-1\) distinguish eigenspaces, hence fails in characteristic two. Unknown equivalent involution classifications in semidirect-product or representation-stabilizer terminology remain a publication-priority risk. No independent audit has been performed.

## References
1. P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897v1, first public November 5, 2019. https://arxiv.org/abs/1911.01897
2. L. Cagliero, L. Gutiérrez Frez and F. Szechtman, *Free 2-step nilpotent Lie algebras and indecomposable modules*, arXiv:1703.06214v1, first public March 17, 2017. https://arxiv.org/abs/1703.06214
3. E. Hakavuori, V. Kivioja, T. Moisala and F. Tripaldi, *Gradings for nilpotent Lie algebras*, arXiv:2011.06871v1, first public November 13, 2020. https://arxiv.org/abs/2011.06871
4. B. Eick and T. Moede, *Computing subalgebras and \(\mathbb Z_2\)-gradings of simple Lie algebras over finite fields*, arXiv:2205.03155v1, first public May 6, 2022. https://arxiv.org/abs/2205.03155
