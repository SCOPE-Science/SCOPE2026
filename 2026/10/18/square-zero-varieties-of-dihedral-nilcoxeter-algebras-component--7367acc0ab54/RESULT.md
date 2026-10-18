# Square-zero varieties of dihedral nilCoxeter algebras: component counts and modular dimension jump

## Finding
Let \(k\) be a field and \(m\ge3\). Let \(N_m\) be the nilCoxeter algebra of the finite dihedral Coxeter system \(I_2(m)\), and set \(X_m=\{x\in N_m:x^2=0\}_{\mathrm{red}}\), meaning the geometric reduced square-zero locus. The numbers of geometrically irreducible components and its dimension are determined for every \(m\) and every characteristic.

If \(m=2d+1\) is odd, then \(\dim X_m=m\) and the number of geometric components is \(1+2\lceil d/2\rceil\), in every characteristic. If \(m=2d\) is even and \(\operatorname{char}k\ne2\), then \(\dim X_m=m\) and the component number is \(2+2\lfloor d/2\rfloor\). If \(m=2d\) and \(\operatorname{char}k=2\), then \(\dim X_m=m+1\) and the component number is exactly \(d\). Thus **the dimension jumps by one precisely when the braid length is even and the characteristic is two**.

More precisely, there is an explicit finite stratification. For odd \(m=2d+1\), the square-zero locus is the disjoint union of the linear space \(J^{d+1}\cong\mathbb A^m\) and two strata isomorphic to \(\mathbb G_m\times\mathbb A^{m-1}\) for each odd \(r\) with \(1\le r\le d\). For even \(m=2d\), there are two strata for each odd \(r<d\), each \(\mathbb G_m\times\mathbb A^{m-1}\) when the characteristic is not two and \(\mathbb G_m\times\mathbb A^m\) in characteristic two. The remaining closed stratum is
\[
C_d\cong\{(a,b)\in\mathbb A^2:F_d(a,b)=0\}_{\mathrm{red}}\times\mathbb A^{m-1},\quad
F_d(a,b)=\begin{cases}2ab,&d\text{ odd},\\ a^2+b^2,&d\text{ even}.\end{cases}
\]
These disjoint pieces exhaust all geometric points and are defined over \(k\).

In particular, for every finite field \(\mathbb F_q\), letting \(M_m(q)=\#X_m(\mathbb F_q)\), the counts are:
\[
M_{2d+1}(q)=q^{2d}\left[q+2\left\lceil\frac d2\right\rceil(q-1)\right].
\]
For \(m=2d\), set \(K=\lfloor d/2\rfloor\). If \(q\) is odd, then
\[
M_{2d}(q)=q^{2d-1}\left[2K(q-1)+E_d(q)\right],\qquad
E_d(q)=\begin{cases}2q-1,&d\text{ odd or }q\equiv1\pmod4,\\1,&d\text{ even and }q\equiv3\pmod4.\end{cases}
\]
If \(q\) is even, then
\[
M_{2d}(q)=q^{2d-1}\left[2Kq(q-1)+\begin{cases}q^2,&d\text{ odd},\\q,&d\text{ even}\end{cases}\right].
\]

## Assumptions and scope
The algebra \(N_m=k\langle u,v\rangle/(u^2,v^2,\operatorname{alt}_m(u,v)-\operatorname{alt}_m(v,u))\) has \(k\)-basis \(1\), the two alternating words \(U_i,V_i\) of length \(i\) for \(1\le i<m\), and the common longest word \(W\) of length \(m\). It has dimension \(2m\). The radical \(J\) is spanned by its positive-length words. Products of alternating words concatenate when the boundary letters differ and the total length does not exceed \(m\), vanish when the boundary letters agree or the total length exceeds \(m\), and at length \(m\) yield the same basis word \(W\) from both orientations. Every square-zero element belongs to \(J\), since its scalar component must square to zero in a field.

Throughout, *irreducible component* means a component after base change to an algebraic closure and passage to reduced support. No scheme-theoretic reducedness is asserted. There are no perfectness or characteristic assumptions other than those explicitly stated.

## Proof
Write uniquely
\[
x=\sum_{i=1}^{m-1}(a_iU_i+b_iV_i)+cW.
\]
The coefficient \(c\) never enters \(x^2\), because \(WJ=JW=0\). For \(2\le n<m\), denote by \(A_n,B_n\) the coefficients of \(U_n,V_n\) in \(x^2\). Direct word concatenation gives
\[
A_n=\sum_{i=1}^{n-1}a_i\begin{cases}b_{n-i},&i\text{ odd},\\a_{n-i},&i\text{ even},\end{cases}\qquad
B_n=\sum_{i=1}^{n-1}b_i\begin{cases}a_{n-i},&i\text{ odd},\\b_{n-i},&i\text{ even}.\end{cases}
\]
At degree \(m\), the only coefficient is \(A_m+B_m\), with the same convolution notation. Thus \(x^2=0\) if and only if \(A_n=B_n=0\) for \(2\le n<m\) and \(A_m+B_m=0\).

For odd \(n\), pair the terms with their reversed decompositions to obtain the exact identities
\[
A_n=\sum_{\substack{i+j=n\\i\text{ odd},\,j\text{ even}}}a_i(a_j+b_j),\qquad
B_n=\sum_{\substack{i+j=n\\i\text{ odd},\,j\text{ even}}}b_i(a_j+b_j).
\]
For even \(n\), the odd--odd convolution is the same in \(A_n\) and \(B_n\), and
\[
A_n-B_n=\sum_{\substack{i+j=n\\i,j\text{ even}}}(a_i a_j-b_i b_j).
\]
These three identities are polynomial identities, including in characteristic two.

Let \(r\) be the least index with \((a_r,b_r)\ne(0,0)\). Suppose first that \(2r<m\). If \(r\) is even, the degree-\(2r\) equations read \(a_r^2=b_r^2=0\), an impossibility. If \(r\) is odd, the equations read \(a_rb_r=0\), so exactly one of \(a_r,b_r\) is nonzero. By swapping the two Coxeter generators it suffices to treat \(a_r\ne0,b_r=0\).

Now solve the equations in increasing total length \(n=2r,\ldots,m-1\). The degree-\(2r\) equation uniquely solves \(b_r=0\). At odd \(n\), assuming all earlier even-index sums \(a_j+b_j\) have vanished, \(A_n=0\) uniquely solves \(a_{n-r}+b_{n-r}=0\) using the invertible coefficient \(a_r\). The equation \(B_n=0\) is then automatic. At even \(n>2r\), the earlier even-index sums imply \(A_n=B_n\), and \(A_n=0\) uniquely solves \(b_{n-r}\), again with coefficient \(a_r\); its remaining terms involve previously determined coordinates. This induction is valid over any field, and each solved coordinate is a regular function of the freely chosen coordinates and \(a_r^{-1}\).

At the longest degree \(n=m\) there is just the equation \(A_m+B_m=0\). If \(m\) is odd, this equation uniquely solves the remaining even-index sum \(a_{m-r}+b_{m-r}\), since its leading coefficient is \(a_r\). If \(m\) is even, the preceding solved equations give \(A_m=B_m\), so the final equation is \(2A_m=0\). It uniquely solves \(b_{m-r}\) when \(2\ne0\) and is identically satisfied when \(2=0\). Counting the \(2(m-r)+1\) coordinates at indices \(r,\ldots,m-1\) and the independent socle coordinate, the \(m-2r\) lower-degree constraints and the possible one final constraint leave \(m\) parameters (or \(m+1\) for even \(m\) in characteristic two). One parameter \(a_r\) must be nonzero. Hence each branch is precisely the asserted \(\mathbb G_m\)-times-affine stratum.

It remains to handle \(2r\ge m\). If \(m=2d+1\), this means \(r\ge d+1\); all products have length at least \(2d+2>m\), so the remaining locus is the entire linear subspace \(J^{d+1}\), of dimension \(m\). If \(m=2d\), it means \(r\ge d\) and the only potentially nonzero quadratic product is the length-\(m\) product of the degree-\(d\) coefficients. Its coefficient is exactly \(F_d(a_d,b_d)\) as displayed, while the other \(m-1\) coordinates are free. This proves the complete stratification.

The point-count formulas follow because each noncentral branch has \((q-1)q^{m-1}\) points, or \((q-1)q^m\) in the even-braid characteristic-two case. For the central piece, the plane equation \(2ab=0\) has \(2q-1\) solutions when \(q\) is odd and is identically zero when \(q\) is even. The equation \(a^2+b^2=0\) has \(2q-1\) solutions if \(-1\) is a square in an odd finite field, one if it is nonsquare, and exactly \(q\) solutions in characteristic two. Multiply each central count by \(q^{m-1}\). The formulas follow.

Finally, each displayed branch is irreducible and locally closed, and the entire variety is their finite union with its central piece. For odd \(m\), all pieces have dimension \(m\), with the central piece irreducible, so their closures are precisely the geometrically irreducible components. For even \(m\) in characteristic not two, the central plane equation factors into two distinct lines over \(\bar k\), yielding two distinct central components of dimension \(m\); all noncentral branches also have dimension \(m\). For even \(m=2d\) in characteristic two, the branches each have dimension \(m+1\). If \(d\) is odd the entire central piece \(J^d\) is an additional linear component of dimension \(m+1\). If \(d\) is even its reduced support has dimension only \(m\) and satisfies \(b_d=a_d\); it lies in the closure of the branch with leading index \(r=d-1\) and \(a_{d-1}\ne0\). Indeed, add \(tU_{d-1}\) to any such central element, retaining all other coefficients: the only new square coefficients below degree \(2d\) are multiples of \(t(a_d+b_d)=0\), and the top-degree contributions involving \(t\) cancel in characteristic two. This gives an explicit degeneration as \(t\to0\). Consequently the central piece contributes no new component in this case. Distinct branches have distinct closures: each is a dense locally closed subset of dimension equal to its closure, while closures of branches at different first indices or orientations cannot coincide, as one lies in the closed condition that lower coordinates vanish. The component and dimension formulas are proved.

## Verification
The independent `verify.py` enumerates the coefficients of every alternating word below length \(m\) over finite fields, checks the square using the raw concatenation law (not the triangular solution), then includes the independent free coefficient of the longest word. It checks \(m=3,\ldots,9\) in characteristic two; \(m=3,\ldots,6\) at selected odd prime fields; and extension fields \(\mathbb F_4\) and \(\mathbb F_9\). All fifteen configurations pass the formula, with the final output `VERIFY_OK`. The provided code does not check geometrically irreducible components, which follow from the explicit algebraic strata in the proof.

## Relationship to prior work
The Coxeter-word basis, length-additive multiplication, and nilradical of nilCoxeter algebras are established background; see Khare, arXiv:1601.04775 and arXiv:1601.08231. Their main subjects are the PBW formalism, finite-dimensional generalized nilCoxeter algebras, and the Coxeter-word basis, not the quadratic square-zero geometry. Benson, arXiv:2407.21175, Sections 2 and 7, gives the exact dihedral presentations and analyzes the \(\operatorname{Ext}\) algebra of type \(I_2(m)\); its characteristic-two and braid-parity phenomena concern a different invariant. In particular the published \(\operatorname{Ext}\) computations do not imply the geometry and arithmetic of the internal square-zero locus. The present conclusion is only relative to examined sources, not a claim of exhaustive literature uniqueness.

## Limitations
This concerns reduced geometric loci and rational solutions, not multiplicities or reducedness of the original quadratic equation schemes. The finite-field formulas count elements, not conjugacy classes or isomorphism classes of complexes. For nonsplit \(-1\) in odd characteristic, some geometric components of the central cone are not individually defined over the ground field; the stated component counts are geometric and the point counts correctly distinguish the nonsplit case. The result does not address higher-rank nilCoxeter algebras or higher power-zero equations. A hidden equivalent classification in unlocated specialized literature remains possible.

## References
1. Apoorva Khare, *Generalized nil-Coxeter algebras, cocommutative algebras, and the PBW property*, arXiv:1601.04775 (first submitted 19 January 2016), particularly Sections 1, 5, and 6. https://arxiv.org/abs/1601.04775
2. Apoorva Khare, *Generalized nil-Coxeter algebras over discrete complex reflection groups*, arXiv:1601.08231 (first submitted 29 January 2016), particularly Section 1 and Definition 1.1. https://arxiv.org/abs/1601.08231
3. David J. Benson, *The cohomology of the nilCoxeter algebra*, arXiv:2407.21175 (first submitted 30 July 2024), particularly Sections 2 and 7, including Examples 7.3--7.4. https://arxiv.org/abs/2407.21175
