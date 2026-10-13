# Subalgebra lattices and cubic-residue jumps for star evolution algebras

## Finding
Let \(K\) be a field, let \(m\geq1\) be an integer whose image in \(K\) is nonzero, and let \(A_m(K)\) be the evolution algebra with basis \(h,e_1,\ldots,e_m\), multiplication
\[
h^2=e_1+\cdots+e_m,\qquad e_i^2=h,\qquad he_i=e_ie_j=0\quad(i\ne j).
\]
Write \(s=\sum_i e_i\), \(U=\operatorname{span}\{e_1,\ldots,e_m\}\), \(U_0=\{\sum_i a_i e_i:\sum_i a_i=0\}\), and \(B(\sum_i a_i e_i,\sum_i b_i e_i)=\sum_i a_i b_i\). A *subalgebra* means any \(K\)-linear subspace closed under this multiplication, with no requirement of a natural basis. Put \(Z=\operatorname{span}\{s,h\}=A_m(K)^2\).

**Classification.** Every subalgebra is in exactly one of these three disjoint classes:

1. \(S\supseteq Z\), with no further constraint on \(S\).
2. \(S=K(s+ch)\oplus W\), where \(c\in K\) obeys \(c^3=m\), and \(W\subseteq U_0\) is totally isotropic for the *bilinear* form \(B\), meaning \(B(W,W)=0\).
3. \(S=W\subseteq U\), where \(B(W,W)=0\).

This holds over **every** field subject to \(m\ne0\) in \(K\), including characteristic two.

For a finite field \(K=\mathbb F_q\), write \(c_q(m)=\#\{c\in\mathbb F_q:c^3=m\}\); for a nondegenerate bilinear space \(V\), write \(I_r(V)\) for the number of totally isotropic \(r\)-dimensional subspaces, \(I(V;T)=\sum_r I_r(V)T^r\); and set \(G_d(T)=\sum_{j=0}^d {d\brack j}_q T^j\), where the bracket denotes the Gaussian binomial coefficient. The **complete subalgebra-dimension polynomial**, counting subspaces rather than isomorphism classes, is
\[
\boxed{\mathcal S_{m,q}(T)=T^2G_{m-1}(T)+c_q(m)\,T I(U_0;T)+I(U;T).}
\]
Its coefficient of \(T^d\) is the number of distinct \(d\)-dimensional subalgebras, including the zero algebra at \(d=0\).

The polar-space terms have completely explicit finite-product formulas. For odd \(q\), let \(\chi:\mathbb F_q^\times\to\{1,-1\}\) be the quadratic character and define
\[
Z_q(N,\delta)=\begin{cases}
1,&N=0,\\
q^{N-1},&N\text{ odd},\\
q^{N-1}+(q-1)q^{N/2-1}\chi((-1)^{N/2}\delta),&N>0\text{ even}.
\end{cases}
\]
For a nondegenerate symmetric form of dimension \(N\) and Gram determinant \(\delta\), its totally isotropic \(r\)-plane count is
\[
I_r(N,\delta)=\frac{\displaystyle\prod_{j=0}^{r-1}q^j\bigl(Z_q(N-2j,(-1)^j\delta)-1\bigr)}{\displaystyle\prod_{j=0}^{r-1}(q^r-q^j)}
\quad(0\le r\le\lfloor N/2\rfloor),
\]
with \(I_r=0\) for larger \(r\). Empty products are one. In the polynomial use \((N,\delta)=(m,1)\) for \(U\) and \((m-1,m^{-1})\) for \(U_0\); determinants are interpreted modulo squares.

For even \(q\), necessarily \(m\) is odd. Put \(2s=m-1\) and
\[
J_{s,q}(T)=\sum_{r=0}^s\frac{\displaystyle\prod_{j=0}^{r-1}(q^{2s-j}-q^j)}{\displaystyle\prod_{j=0}^{r-1}(q^r-q^j)}T^r.
\]
Both \(I(U;T)\) and \(I(U_0;T)\) equal \(J_{s,q}(T)\), while \(c_q(m)=\gcd(3,q-1)\). Hence the even-characteristic result simplifies to
\[
\boxed{\mathcal S_{m,q}(T)=T^2G_{m-1}(T)+\bigl(1+\gcd(3,q-1)T\bigr)J_{s,q}(T).}
\]
For example,
\[
\mathcal S_{3,2}(T)=1+4T+4T^2+3T^3+T^4,\quad
\mathcal S_{3,4}(T)=1+8T+16T^2+5T^3+T^4,
\]
and \(\mathcal S_{2,7}(T)=1+T^2+T^3\): the last algebra has **no nonzero one-dimensional subalgebra**.

## Assumptions and scope
The graph is the simple star \(K_{1,m}\) and the evolution multiplication uses its unnormalized adjacency matrix; there is one hub \(h\) and \(m\) leaves. All subalgebras are counted as distinct embedded vector subspaces. The only restriction for the structural classification is \(m\cdot1_K\ne0\). Finite-field formulas apply to every prime-power \(q\) whose characteristic does not divide \(m\). The quadratic character is only used for odd \(q\); in characteristic two, total isotropy means vanishing of the bilinear form, not merely vanishing of a quadratic form.

## Proof
**1. Multiplication and an orthogonal splitting.** Since \(s^2=mh\), \(h^2=s\), and \(sh=0\), every product belongs to \(Z\), and \(A_m(K)^2=Z\). Moreover \(B(s,s)=m\ne0\), whence \(U=Ks\oplus U_0\) orthogonally and \(B|_{U_0}\) is nondegenerate. Every \(x\in A_m(K)\) uniquely has the form \(x=as+v+bh\), with \(v\in U_0\), and direct multiplication gives
\[
(as+v+bh)(a's+v'+b'h)=(maa'+B(v,v'))h+bb's.
\tag{1}
\]

**2. Subalgebras meeting the product space in dimension two.** If \(Z\subseteq S\), (1) implies \(S^2\subseteq Z\subseteq S\). These are precisely the first class.

**3. Subalgebras meeting the product space trivially.** If \(S\cap Z=0\), then \(S^2\subseteq Z\cap S=0\). For \(x=as+v+bh\in S\), the \(s\)-coordinate of \(x^2\) is \(b^2\); since \(K\) is a field, \(b=0\). Thus \(S\subseteq U\); the \(h\)-coordinate of each product is \(B(x,y)\), so \(B(S,S)=0\). Conversely any totally isotropic subspace of \(U\) has zero product. Because \(s\) is anisotropic, such subspaces have trivial intersection with \(Z\).

**4. Subalgebras meeting the product space in a line.** Suppose \(S\cap Z=\ell\) is one-dimensional. The line \(\ell\) must itself be a subalgebra of \(Z\). For a nonzero generator \(ps+th\), squaring yields \(t^2s+mp^2h\). The cases \(p=0\) and \(t=0\) are impossible since \(m\ne0\). With \(c=t/p\), closure of \(\ell\) is equivalent to \(c^3=m\), and \(\ell=K(s+ch)\). For any \(x=as+v+bh\in S\), the element \((s+ch)x=cb\,s+ma\,h\) lies in \(\ell\). Therefore \(ma=c^2b\), or \(b=ca\), since \(c^3=m\ne0\). Hence \(S\subseteq\ell\oplus U_0\), and \(S=\ell\oplus W\) for some \(W\subseteq U_0\). Products of \(\ell\) with \(U_0\) vanish, while products of vectors of \(W\) equal \(B(v,w)h\). As \(h\notin\ell\), closure is equivalent to \(B(W,W)=0\). Conversely this condition makes every displayed \(S\) a subalgebra. The three cases are exhaustive and disjoint by \(\dim(S\cap Z)=2,0,1\).

**5. Finite-field count.** The first class is indexed by subspaces of \(A_m/Z\), which has dimension \(m-1\); a member of dimension \(d\) contributes \({m-1\brack d-2}_q\). The second class contributes \(c_q(m) I_{d-1}(U_0)\), because distinct roots give distinct intersection lines in \(Z\). The third contributes \(I_d(U)\). This proves the polynomial.

**6. Explicit isotropic-space factors.** Suppose \(q\) is odd. A nondegenerate symmetric bilinear form of dimension \(N\) and determinant class \(\delta\) has exactly \(Z_q(N,\delta)\) vectors \(x\) with \(B(x,x)=0\); this follows by diagonalization and the standard one-variable quadratic-character sum (with the dimension-zero case handled separately). After choosing a totally isotropic \(j\)-frame spanning \(W_j\), the quotient \(W_j^\perp/W_j\) is nondegenerate of dimension \(N-2j\), with determinant class \((-1)^j\delta\), since each removed hyperbolic plane has determinant class \(-1\). The number of possible next frame vectors is exactly \(q^j\bigl(Z_q(N-2j,(-1)^j\delta)-1\bigr)\); each nonzero isotropic vector of that quotient has \(q^j\) lifts. Multiplying these factors and dividing by \(|\mathrm{GL}_r(\mathbb F_q)|=\prod_{j=0}^{r-1}(q^r-q^j)\) proves the given formula. The Gram determinant on \(U\) is one, and the orthogonal direct sum \(U=Ks\perp U_0\) gives determinant class \(m^{-1}\) on \(U_0\).

If \(q\) is even, \(m\) is odd, and \(B(v,v)=(\sum_i v_i)^2\) on \(U\). Hence every totally isotropic subspace of \(U\) lies inside \(U_0\). The restriction to \(U_0\) is nondegenerate and alternating, hence symplectic of dimension \(2s=m-1\). To construct an ordered totally isotropic \(r\)-frame, the \((j+1)\)-st vector must lie in the orthogonal complement of the preceding \(j\)-space but outside that space: exactly \(q^{2s-j}-q^j\) choices. Dividing by \(|\mathrm{GL}_r(\mathbb F_q)|\) proves \(J_{s,q}\). Finally, in characteristic two the scalar \(m\) is one, and the cyclic group \(\mathbb F_q^\times\) has precisely \(\gcd(3,q-1)\) solutions of \(c^3=1\). This proves the simplified formula.

## Verification
The accompanying standalone scripts `checker.py` and `polar_check.py` require only Python 3. Running `python3 checker.py` independently enumerates every subspace by reduced row-echelon bases over selected small finite fields and checks multiplication closure against the dimension counts obtained from the classification. It checks \(13\) parameter pairs, including characteristic two and fields of four elements. Running `python3 polar_check.py` independently compares the orthogonal and symplectic product formulas against exhaustive isotropic-subspace enumeration; both return their success markers. These finite checks corroborate but do **not** replace the general algebraic proof in the preceding section.

## Relationship to prior work
Vidal, Cadavid and Rodríguez (arXiv:2111.07399v1, sections 1–3) define graph evolution algebras and analyze their relationship with random-walk/Hilbert counterparts; the star adjacency multiplication here is the finite algebraic instance of that graph construction. Cadavid, Rodiño Montoya and Rodríguez (arXiv:1710.10516v2, sections 1–3) study isomorphisms and isotopisms of graph and random-walk evolution algebras, not their full subalgebra-dimension distributions. Cabrera Casado, Siles Molina and Velasco (arXiv:1601.01832v2, section 2.1 and later decomposition results) distinguish arbitrary subalgebras from evolution subalgebras with natural bases and study ideals and decompositions. The classification above counts *all* multiplication-closed linear subspaces of this star family, including subalgebras that lack an extendible natural basis. No inspected primary statement implies the displayed cubic-root/polar-space polynomial. An equivalent calculation in another source or terminology remains a literature risk.

## Limitations
No classification is asserted when the characteristic divides \(m\): then \(s\) is isotropic and the orthogonal splitting used above fails. The count is for adjacency-defined evolution algebras of stars, not random-walk-normalized algebras or arbitrary graph evolution algebras, and it is a count of embedded subspaces rather than isomorphism classes. Finite computations test only the listed small cases; they are not an exhaustive proof for arbitrary \(m\) or \(q\).

## References
1. S. J. Vidal, P. Cadavid and P. M. Rodríguez, *On Hilbert evolution algebras of a graph*, arXiv:2111.07399v1, 14 November 2021, https://arxiv.org/html/2111.07399v1.
2. P. Cadavid, M. L. Rodiño Montoya and P. M. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516v2, https://arxiv.org/html/1710.10516v2.
3. Y. Cabrera Casado, M. Siles Molina and M. V. Velasco, *Evolution algebras of arbitrary dimension and their decompositions*, arXiv:1601.01832v2, https://arxiv.org/html/1601.01832v2.
4. L. M. Camacho, A. Kh. Khudoyberdiyev and B. A. Omirov, *On the property of subalgebras of Evolution algebras*, arXiv:1405.7126, 2014; its available abstract concerns nilpotent cases and evolution-subalgebra conditions, not an inspected proof of the star census.
