# Parity-averaged commuting spectra and characteristic-two component collapse for symmetric minimal nilpotents

## Finding

Fix an integer \(n\ge 2\), an integer \(t\ge 1\), and a field \(k\). Write \(X_{n,t}(k)\) for the **reduced** affine variety of ordered tuples \((A_1,\ldots,A_t)\) of \(n\times n\) matrices satisfying, for every \(i,j\),
\[
 A_i^{\mathsf T}=A_i,\qquad A_i^2=0,\qquad \operatorname{rank}(A_i)\le1,\qquad A_iA_j=A_jA_i.
\]
Here transpose is taken in the specified standard basis. Let \(m=\lfloor n/2\rfloor\) and \(r=\min(t,m)\).

**Geometric component theorem.** If \(k\) is algebraically closed, every component of \(X_{n,t}(k)\) has dimension
\[
 d_{n,t}=rt+r(n-r)-\binom{r+1}{2}.
\]
There are precisely **two** geometrically irreducible components when \(n\) is even, \(\operatorname{char}(k)\ne2\), and \(t\ge n/2\); in **all other cases** the reduced variety is irreducible. The two components in the exceptional case correspond to the two components of the maximal orthogonal isotropic Grassmannian. In particular, for each even \(n\), the two-component locus in odd characteristic becomes a single irreducible variety in characteristic two.

**Arithmetic theorem.** Let \(q\) be a prime power. Define \(G(a,b;q)={a\brack b}_q\), the Gaussian coefficient, with value zero for \(b<0\) or \(b>a\). Put
\[
 S_a(b;q)=G(a,b;q)\prod_{j=0}^{b-1}(q^{a-j}+1)
\]
when \(0\le b\le a\), and put \(S_a(b;q)=0\) otherwise. Empty products equal one. Let \(I_b(n,q)\) be the number of totally isotropic \(b\)-subspaces for the standard symmetric bilinear form \(u\cdot v=\sum_i u_iv_i\) on \(\mathbb F_q^n\). Then
\[
 \#X_{n,t}(\mathbb F_q)=\sum_{b=0}^{m}I_b(n,q)\prod_{j=0}^{b-1}(q^t-q^j).
\]
All these coefficients are explicit as follows.

* For odd \(n=2m+1\), in **every** characteristic, \(I_b(n,q)=S_m(b;q)\).
* For even \(n=2m\) and even \(q\),
\[
 I_b(n,q)=q^bS_{m-1}(b;q)+S_{m-1}(b-1;q).
\]
* For even \(n=2m\) and odd \(q\), set \(\epsilon=\chi_q((-1)^m)\), where \(\chi_q\) is the quadratic character. If \(\epsilon=1\),
\[
 I_b(n,q)=I_b^+(m,q):=G(m,b;q)\prod_{j=0}^{b-1}(q^{m-j-1}+1).
\]
If \(\epsilon=-1\),
\[
 I_b(n,q)=I_b^-(m,q):=G(m-1,b;q)\prod_{j=0}^{b-1}(q^{m-j}+1).
\]
The conventions make the latter two expressions zero outside their usual Witt ranges.

**Parity-averaging identity.** For every \(m\ge1\), \(0\le b\le m\), and every formal indeterminate \(q\),
\[
 2\bigl(q^bS_{m-1}(b;q)+S_{m-1}(b-1;q)\bigr)=I_b^+(m,q)+I_b^-(m,q).
\]
Hence, if \(N^+_{2m,t}(q)\) and \(N^-_{2m,t}(q)\) denote the two formal sums obtained by using \(I_b^+\) and \(I_b^-\), respectively, then for **every even prime power** \(q\),
\[
 \#X_{2m,t}(\mathbb F_q)=\tfrac12\bigl(N^+_{2m,t}(q)+N^-_{2m,t}(q)\bigr).
\]
The superscripts in the last formula label formal orthogonal-type polynomials; they do **not** assert the existence of two characteristic-two orthogonal forms of the same symmetric-bilinear type.

## Assumptions and scope

All matrix equations use the standard transpose and standard nondegenerate bilinear dot product. The geometric theorem concerns the reduced variety after extension to an algebraic closure; it makes no assertion that the scheme cut out by the displayed equations is reduced. The finite-field theorem counts rational matrix tuples, not similarity classes and not congruence orbits. The tuple length \(t\) is unrestricted and zero matrices are allowed. The notion of rank in the definition is ordinary matrix rank over the ground field. The empty subspace is counted as a zero-dimensional isotropic subspace.

## Proof

**1. Rank-one factorization and the commutation criterion.** If \(A\ne0\) is symmetric and rank one, its image is a line \(\langle u\rangle\), so all its columns are multiples of \(u\); symmetry forces \(A=c\,uu^{\mathsf T}\) for a unique nonzero scalar \(c\) after a choice of nonzero \(u\). Then \(A^2=c^2(u\cdot u)uu^{\mathsf T}\), so \(A^2=0\) precisely when \(u\cdot u=0\). For two nonzero such matrices \(A=c\,uu^{\mathsf T}\), \(B=d\,vv^{\mathsf T}\),
\[
 [A,B]=cd(u\cdot v)(uv^{\mathsf T}-vu^{\mathsf T}).
\]
If \(u,v\) are linearly independent, \(uv^{\mathsf T}\ne vu^{\mathsf T}\) in every characteristic (apply the two rank-one tensors to a linear functional separating the lines). If they are dependent, \(u\cdot v=0\) since both are isotropic. Thus \(A\) and \(B\) commute **if and only if** \(u\cdot v=0\). The span of the images of all tuple entries is therefore totally isotropic, and conversely any tuple of symmetric rank-at-most-one matrices whose images lie in one totally isotropic space is pairwise commuting.

**2. Count tuples with exactly prescribed image span.** Let \(U\) be a totally isotropic subspace of dimension \(b\) over \(\mathbb F_q\). For each line \(L\subseteq U\), there are exactly \(q-1\) distinct nonzero symmetric rank-one matrices having image \(L\): fix \(0\ne u\in L\) and vary \(c\in\mathbb F_q^\times\). Including the zero matrix gives
\[
 1+(q-1)\frac{q^b-1}{q-1}=q^b
\]
matrices whose image lies in \(U\). Thus the number of ordered \(t\)-tuples supported in \(U\) is \(q^{bt}\). By Möbius inversion on the lattice of subspaces of \(U\), the number whose images span precisely \(U\) is
\[
 T_{b,t}=\sum_{V\le U}\mu(V,U)q^{t\dim V}=\prod_{j=0}^{b-1}(q^t-q^j),
\]
the usual count of surjective linear maps \(\mathbb F_q^t\to U\). Summing over every totally isotropic \(U\) yields the asserted formula for \(\#X_{n,t}\).

**3. Determine isotropic-subspace coefficients.** In odd characteristic the dot product is nondegenerate and, in even dimension \(2m\), has discriminant \(1\), hence Witt sign \(\chi_q((-1)^m)\). Standard Witt decomposition and successive isotropic-flag counting yield exactly the displayed hyperbolic, elliptic, and odd-dimensional parabolic orthogonal formulas. For clarity, these can also be obtained inductively by fixing the first isotropic line and counting isotropic \((b-1)\)-planes in \(L^\perp/L\), dividing by the number \((q^b-1)/(q-1)\) of lines in a \(b\)-plane. These recurrences, with \(I_0=1\), give precisely the products above.

In characteristic two, \(u\cdot u=\sum_i u_i^2=(\sum_i u_i)^2\), so every isotropic vector lies in the hyperplane \(H=\{u:\sum_i u_i=0\}\). For odd \(n=2m+1\), the restriction of the dot product to \(H\) is a nondegenerate alternating form of dimension \(2m\); the symplectic isotropic-Grassmannian count is \(S_m(b;q)\). For even \(n=2m\), the alternating restriction on \(H\) has radical \(R=\langle(1,\ldots,1)\rangle\) and symplectic quotient \(H/R\) of dimension \(2m-2\). A totally isotropic \(b\)-plane either misses \(R\) or contains \(R\). In the first case its image in \(H/R\) is an isotropic \(b\)-plane and it is one of the \(q^b\) graphs of linear maps from this plane to \(R\). In the second case it is the full inverse image of an isotropic \((b-1)\)-plane in the quotient. This proves \(q^bS_{m-1}(b;q)+S_{m-1}(b-1;q)\), including the maximal case \(b=m\).

**4. Prove the polynomial parity average.** For \(0\le b<m\), divide the two orthogonal-type products by \(S_{m-1}(b;q)\), using the Gaussian coefficient identity. This gives
\[
 \frac{I_b^+}{S_{m-1}(b;q)}=\frac{q^m-1}{q^{m-b}-1},\qquad
 \frac{I_b^-}{S_{m-1}(b;q)}=\frac{q^m+1}{q^{m-b}+1}.
\]
Their arithmetic mean is \((q^{2m-b}-1)/(q^{2(m-b)}-1)\), whereas
\[
 \frac{S_{m-1}(b-1;q)}{S_{m-1}(b;q)}=\frac{q^b-1}{q^{2(m-b)}-1}.
\]
Therefore the mean equals \(q^b+S_{m-1}(b-1;q)/S_{m-1}(b;q)\). Clearing denominators establishes the identity as a polynomial identity. For \(b=m\), directly \(I_m^+=2S_{m-1}(m-1;q)\), \(I_m^-=S_{m-1}(m;q)=0\). This finishes the arithmetic theorem.

**5. Geometric components and dimensions.** Work over algebraically closed \(k\). A maximal image-span dimension for \(t\) rank-one entries is \(r=\min(t,\lfloor n/2\rfloor)\). Let \(\mathrm{IGr}(r,n)\) denote the reduced variety of totally isotropic \(r\)-planes for the dot product. Consider the incidence space of \((U;A_1,\ldots,A_t)\), with \(U\in\mathrm{IGr}(r,n)\), each \(A_i\) symmetric of rank at most one with image inside \(U\), and the images collectively spanning \(U\). The fiber over \(U\) is a nonempty open subset of the \(t\)-fold product of affine Veronese cones \(\{c\,uu^{\mathsf T}:u\in U\}\), each of dimension \(r\). The fiber is irreducible of dimension \(rt\); the map to \(X_{n,t}\) is injective on this stratum because \(U\) can be recovered as the span of the images. The Veronese parameterization remains irreducible in characteristic two, even though it can be inseparable.

The reduced isotropic Grassmannian has dimension
\[
 \dim\mathrm{IGr}(r,n)=r(n-r)-\binom{r+1}{2}.
\]
In odd characteristic this is the standard orthogonal dimension formula. In characteristic two, it follows from the descriptions in step 3: for odd \(n\) it is a symplectic Grassmannian in \(H\); for even \(n\) and \(r<m\), its dense radical-avoiding stratum is a rank-\(r\) vector bundle over \(\mathrm{SpIGr}(r,H/R)\); for \(r=m\), every plane contains the radical and the Grassmannian is the symplectic Lagrangian Grassmannian in \(H/R\). In the even-dimensional characteristic-two case, any radical-containing plane of dimension \(r<m\) is a limit of radical-avoiding ones: deform its radical vector to \(z+s x\), with \(z\in R\) and \(x\in U^\perp\setminus U\). Thus \(\mathrm{IGr}(r,n)\) is irreducible in characteristic two.

In odd characteristic \(\mathrm{IGr}(r,n)\) is irreducible unless \(n=2m\) and \(r=m\), when the orthogonal maximal-isotropic Grassmannian has exactly two irreducible components. In odd dimension it is irreducible also at maximal rank. Every lower-image-span tuple belongs to the closure of an \(r\)-span tuple: extend its totally isotropic image span to an \(r\)-plane, and perturb its rank-one generating vectors within that plane, allowing zero entries to acquire a factor of the deformation parameter. For even \(n\) in odd characteristic, an isotropic subspace of dimension below \(m\) extends to maximal isotropic spaces in **both** component families. Thus no extra components arise from lower ranks, and the two families survive as two distinct components when \(r=m\). Adding the fiber dimension \(rt\) proves the common component dimension and the asserted irreducibility criterion.

## Verification

The companion `verify.py` implements finite-field arithmetic directly in \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) and in \(\mathbb F_4=\mathbb F_2[x]/(x^2+x+1)\). For each reported configuration it enumerates distinct rank-at-most-one symmetric square-zero matrices, computes literal matrix products for all pairs, enumerates commuting tuples, and compares their number to the displayed product formula. It is independent of the commutation-to-orthogonality reduction in that its final commutation test uses actual matrix multiplication. Eleven complete configurations passed, including \((n,q,t)=(4,3,2)\) giving \(513\), \((4,4,2)\) giving \(1216\), and \((6,2,2)\) giving \(544\). These finite checks are corroboration, not a proof of the infinite family or of geometric irreducibility; the proofs are in steps 1–5.

## Relationship to prior work

Finite classical orthogonal and symplectic polar-space formulas, and the fact that the maximal orthogonal Grassmannian of a split even-dimensional quadratic space has two components, are classical and **not asserted to be new**. Britnell and Wildon (arXiv:1001.0811v1, 6 January 2010), inspected in full-text portions covering its introduction and main results, study which unrestricted similarity classes contain commuting representatives. Their statement neither imposes transpose symmetry and rank one nor classifies the reduced tuple variety and its characteristic-two components. Ngo (arXiv:1209.1659v1) concerns nilpotent commuting varieties in Lie algebras of small rank, rather than the present transpose-fixed rank-one locus. De Beule, Hallez, Metsch and Storme (arXiv:1202.4143v1) study blocking sets of generators in classical polar spaces, rather than matrix commutation or parity-averaged tuple counts. Panyushev's commuting-variety survey discusses unrestricted symmetric commuting matrices, not the rank-one constrained characteristic-two transition.

Prior finite-field formulas for totally isotropic subspaces and isotropic-vector tuples imply some individual summands and odd-characteristic numerical counts; those building blocks are not separately claimed as original. The contribution assessed here is the joint **geometric component theorem for symmetric minimal nilpotent tuples**, its sharp characteristic-two component collapse, and the corresponding complete matrix-tuple hierarchy with a characteristic-two parity average. An unrestricted rank-one square-zero commuting-variety classification does not by itself determine the irreducible components of its transpose-fixed locus. Pattanayak (arXiv:2610.17737v1, 13 October 2026) proves general dimension and maximal-component results for unrestricted nilpotent commuting tuples of complex symmetric pairs. Its incidence-stratification viewpoint overlaps the method used here, but it does not classify this rank-one constrained subvariety or its positive-characteristic geometry. Brennan's earlier article on normality of commuting varieties of symmetric matrices (1994, exact first-public day not verified) was located in abstract/metadata form but not inspected in full; possible specialized antecedents remain a substantive priority risk.

## Limitations

No statement is made about the potentially nonreduced matrix-equation scheme, singularities, or orbit structure. The results do not extend as stated to matrices of arbitrary rank or to nonstandard adjoints without updating the underlying bilinear form. The finite-field count uses the standard dot product and, for odd-field even dimensions, depends on the square class of \((-1)^m\). Primary-literature priority remains subject to further examination of unavailable older full texts, especially work on symmetric commuting schemes and orthogonal rank-one nilpotent varieties.

## References

1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1, first public 2010-01-06; https://arxiv.org/pdf/1001.0811.
2. N. V. Ngo, *Commuting varieties of r-tuples over Lie algebras*, arXiv:1209.1659v1, first public 2012-09-07; https://arxiv.org/pdf/1209.1659.
3. J. De Beule, A. Hallez, K. Metsch and L. Storme, *Sets of generators blocking all generators in finite classical polar spaces*, arXiv:1202.4143v1, first public 2012-02-19; https://arxiv.org/pdf/1202.4143.
4. D. Panyushev, *On the irreducibility of commuting varieties* (survey slides, 2008); https://mccme.ru/~panyush/law08-short.pdf.
5. S. Pattanayak, *Dimensions and maximal-dimensional components of higher commuting varieties of symmetric pairs*, arXiv:2610.17737v1, 2026-10-13; https://arxiv.org/pdf/2610.17737.
6. J. P. Brennan, *On the normality of commuting varieties of symmetric matrices*, Communications in Algebra (1994), DOI:10.1080/00927879408825197; abstract/metadata consulted, full text not inspected.
