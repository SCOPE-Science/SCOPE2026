# Compatible square-zero elements in modular generalized dihedral group algebras

## Finding

Let \(H\) be an abelian group of odd order \(h\ge3\) and \(k=\mathbb F_q\) a finite field of characteristic two. Set \(G=H\rtimes\langle s\rangle\), where \(s^2=1\) and \(shs=h^{-1}\) for \(h\in H\), and let \(A=kG\). For a square-zero element \(x\in A\), the left-regular operator is \(L_x(a)=xa\). An ordered \(r\)-tuple \((x_1,\ldots,x_r)\) is *compatible* when \(x_i^2=0\) and \(x_ix_j=x_jx_i\) for all indices.

Let \(\widehat H=\operatorname{Hom}(H,\overline k^\times)\), and let \(\mathcal O\) be the set of orbits of the \(q\)-power Frobenius on the unordered pairs \(\{\chi,\chi^{-1}\}\) for \(\chi\ne1\). Write \(d_\omega=|\omega|\), \(Q_\omega=q^{d_\omega}\), so \(\sum_\omega d_\omega=(h-1)/2\).

For **every integer** \(r\ge1\), the full multivariate rank-enumerator is
\[
\boxed{\mathcal F_{H,q,r}(T_1,\ldots,T_r)
=\prod_{i=1}^r[1+(q-1)T_i]\prod_{\omega\in\mathcal O}
\left[1+(Q_\omega+1)\left(\prod_{i=1}^r(1+(Q_\omega-1)T_i^{2d_\omega})-1\right)\right].}
\]
The coefficient of \(T_1^{a_1}\cdots T_r^{a_r}\) is the number of compatible tuples with \(\operatorname{rank}_k L_{x_i}=a_i\) for every \(i\). In particular their total number is
\[
\boxed{C_r(H,q)=q^r\prod_{\omega\in\mathcal O}[1+(Q_\omega+1)(Q_\omega^r-1)].}
\]

There is a rigidity statement independent of enumeration: **two square-zero elements commute if and only if their product is zero**. Every inclusion-maximal \(k\)-linear subspace all of whose members are pairwise commuting square-zero elements has dimension \((h+1)/2\); the exact number of these subspaces is \(\prod_{\omega\in\mathcal O}(Q_\omega+1)\). The map \(W\mapsto1+W\) bijects them with maximal elementary abelian \(2\)-subgroups of \(A^\times\), each having order \(q^{(h+1)/2}\).

For \(r\ge1\), the *reduced* affine variety of compatible tuples is geometrically irreducible of dimension
\[
\boxed{r+\frac{h-1}{2}(r+1).}
\]
No reducedness is asserted for the original polynomial equation scheme.

The commuting-pair count distinguishes kernels of equal cardinality even though their individual square-zero counts agree. Over \(\mathbb F_2\), the groups \(H=C_9\) and \(H=C_3\times C_3\) both yield \(512\) square-zero elements, but the numbers of ordered compatible pairs are respectively \(22{,}720\) and \(40{,}000\). Their maximal compatible-subspace counts are respectively \(27\) and \(81\).

## Assumptions and scope

The group \(H\) must be finite abelian of odd order at least three; the coefficient field has order \(q=2^f\), where \(f\ge1\). The involution acts by inversion. Frobenius orbits are taken on **unordered** inverse-character pairs, not individual characters, and multiplicities are retained. A rank is that of left multiplication on the full \(2h\)-dimensional \(k\)-vector space \(A\). An inclusion-maximal subspace means maximal by containment, not merely maximum dimension. A maximal elementary abelian \(2\)-subgroup is maximal by containment in the unit group.

The reduced tuple variety is the underlying reduced variety of the polynomial equations defining compatibility after base change to an algebraic closure; this does not assess infinitesimal or nonreduced structure. The tuple count includes the all-zero tuple and all repeated elements. All enumerations are of labeled ordered tuples, not conjugacy classes.

## Proof

**1. Decomposition into one local factor and matrix blocks.** Because \(h\) is odd, \(B=kH\) is a finite étale, commutative \(k\)-algebra. Over \(\overline k\), its primitive idempotents are indexed by \(\widehat H\). The inversion automorphism sends the primitive idempotent at \(\chi\) to the one at \(\chi^{-1}\). The trivial character produces a component \(k[C_2]\cong k[t]/(t^2)\), with \(t=s+1\). Every nontrivial inverse-character pair produces \(M_2(\overline k)\). Descending under Frobenius yields a matrix factor \(M_2(\mathbb F_{q^{d_\omega}})\) for every orbit \(\omega\): the center is the field of cardinality \(q^{d_\omega}\), and every finite-dimensional central simple algebra over a finite field is split. Thus
\[
A\cong k[t]/(t^2)\times\prod_{\omega\in\mathcal O}M_2(\mathbb F_{Q_\omega}).\tag{1}
\]
The dimension check is \(2+4\sum_\omega d_\omega=2h\). This decomposition is antecedent structural information, not a newly claimed discovery; see the first reference and its Theorem 3.1 and equation (3.2).

**2. Local square-zero geometry and rank.** In \(k[t]/(t^2)\), the square-zero elements are precisely \(at\), with \(a\in k\). If \(a\ne0\), \(L_{at}\) has rank one over \(k\).

Over any field \(K\) of characteristic two, a nonzero matrix \(N\in M_2(K)\) with \(N^2=0\) necessarily has \(\operatorname{rank}_K N=1\) and \(\operatorname{im}N=\ker N=\ell\) for a unique line \(\ell\subset K^2\). Conversely, for any \(\ell\in\mathbb P^1(K)\), the matrices with this image and kernel form the one-dimensional \(K\)-vector space \(\operatorname{Hom}_K(K^2/\ell,\ell)\); it has \(|K|-1\) nonzero elements. The matrix \(L_N\) acts independently on the two columns of \(M_2(K)\) and has \(K\)-rank \(2\). If \(K=\mathbb F_{q^d}\), its \(k\)-rank is \(2d\).

**3. Compatibility is zero-product.** If \(N\ne0\) is square-zero, a change of basis sends it to \(\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\). Its full centralizer consists of \(aI+bN\). If \((aI+bN)^2=0\), characteristic two gives \(a^2I=0\), hence \(a=0\). Thus *every square-zero matrix commuting with \(N\) is a scalar multiple of \(N\)*, and its product with \(N\) vanishes. The assertion also holds if the first matrix is zero. In the local dual-number factor, any two square-zero elements are multiples of \(t\) and have zero product. Apply (1) componentwise to conclude, for all \(x,y\in A\) with \(x^2=y^2=0\),
\[
xy=yx\quad\Longleftrightarrow\quad xy=yx=0.
\]
The reverse implication is immediate. In particular all products between entries of a compatible tuple vanish.

**4. Multivariate rank count.** In each matrix factor over \(K=\mathbb F_Q\), a compatible tuple is either all zero, or has a unique common image/kernel line \(\ell\in\mathbb P^1(K)\), followed by an ordered \(r\)-tuple of scalars in \(K\), not all zero, multiplying a fixed nonzero generator of \(\operatorname{Hom}(K^2/\ell,\ell)\). There are \(Q+1\) choices of \(\ell\); each nonzero coordinate of a scalar tuple has \(Q-1\) choices and contributes \(k\)-rank \(2d\). The factor's generating polynomial is exactly
\[
1+(Q+1)\left(\prod_{i=1}^r(1+(Q-1)T_i^{2d})-1\right).
\]
The local dual-number factor independently contributes \(\prod_i(1+(q-1)T_i)\). Multiplying independent factors yields \(\mathcal F_{H,q,r}\). Setting each \(T_i=1\) yields \(C_r(H,q)\). Every tuple, including zero entries, is counted exactly once, and the formula holds for every integer \(r\ge1\).

**5. Maximal spaces and elementary abelian groups.** A \(k\)-linear space of pairwise commuting square-zero matrices in a factor \(M_2(K)\) is contained in the scalar \(K\)-line of any nonzero member, by Step 3. Its maximal choices are exactly the \(Q+1\) distinct full \(K\)-lines corresponding to \(\ell\in\mathbb P^1(K)\). A maximal compatible linear space in a finite direct product must be the product of maximal compatible spaces in each factor: otherwise it can be enlarged by an element supported only in one factor, or to the product of its coordinate projections. The local factor has the unique maximal space \(kt\). Thus every maximal compatible \(k\)-space has dimension \(1+\sum_\omega d_\omega=(h+1)/2\), and their number is \(\prod_\omega(Q_\omega+1)\).

For a commuting square-zero family, Step 3 gives \((1+x)(1+y)=1+(x+y)\), so \(1+W\) is an elementary abelian \(2\)-subgroup for every compatible linear subspace \(W\). Conversely, if \(E\le A^\times\) is elementary abelian of exponent two, every \(u-1\), \(u\in E\), is square-zero; any two such elements commute, hence multiply to zero. Their \(k\)-linear span is therefore compatible and contains the set \(E-1\). If \(E\) was maximal, equality forces its span to be maximal compatible. This proves the bijection and the group order.

**6. Reduced geometric dimension.** Over \(\overline k\), all nontrivial inverse-character pairs split individually, producing \((h-1)/2\) copies of \(M_2(\overline k)\) and one copy of the dual numbers. The compatible \(r\)-tuple locus of one matrix factor is the affine cone over the image of \(\mathbb P^1\times\mathbb P^{r-1}\) under the Segre–Veronese embedding of bidegree \((2,1)\): a nonzero tuple is a nonzero scalar-vector times one rank-one nilpotent matrix, and the nilpotent projective directions form a Veronese conic. Its reduced locus is geometrically irreducible of dimension \(r+1\). The dual-number tuple locus is \(\mathbb A^r\). Taking products gives a geometrically irreducible reduced locus of dimension \(r+(h-1)(r+1)/2\). This argument is set-theoretic and does not claim scheme-theoretic reducedness.

## Verification

The two accompanying standard-library-only Python programs reconstruct the multiplication of \(G\) and the coefficient fields directly. Run `python verify_group_ring.py` and then `python verify_compatible_differentials.py` in a directory containing both files. The latter enumerates all square-zero elements and independently evaluates products and regular-representation ranks, comparing the complete commuting-pair rank-vector histogram with the displayed polynomial in six configurations: \(H=C_3,C_5,C_7,C_3\times C_3,C_9\) over \(\mathbb F_2\), and \(H=C_3\) over \(\mathbb F_4\). It independently verifies all compatible triples in the two smallest binary configurations. The first script additionally verifies the univariate square-zero rank spectrum for seven configurations. The output file `verification_output.txt` contains the exact executed check results.

The direct checks report \(40\) and \(1{,}216\) compatible ordered pairs for \(H=C_3\) at field orders two and four, respectively; \(304\) for \(C_5\) at field order two; \(2{,}272\) for \(C_7\); \(22{,}720\) for \(C_9\); and \(40{,}000\) for \(C_3\times C_3\), all at field order two. All tested full rank-vector histograms agree with the formula. Finite tests support but do not replace the infinite-family proof.

## Relationship to prior work

The 2014 paper of Makhijani, Sharma and Srivastava, particularly Theorem 3.1 and equation (3.2), already determines the unit group and semisimple blocks of modular generalized dihedral group algebras with odd abelian kernel. The decomposition in Step 1, the exact number of *individual* square-zero elements, and the existence of unipotent subgroups are therefore not asserted as new. Indeed, the univariate count \(q^h\) follows immediately from their blocks and elementary \(2\times2\) nilpotent enumeration. Our assessed statement is instead the simultaneous all-arity compatibility constraint, its **complete multivariate left-rank census**, zero-product rigidity, and its precise maximal compatible-subspace classification. These are not stated by that structural decomposition alone, although that decomposition is an essential ingredient and limits the independent conceptual novelty.

Ngo and Šivic's 2013 preprint, and earlier general nilpotent commuting-variety literature, study geometric properties of unrestricted commuting nilpotent matrix tuples. Their arbitrary-matrix results do not give finite-field rank-vector polynomials for square-zero elements of these modular group algebras, nor the maximal compatible-subspace count. The geometric irreducibility of the local \(2\times2\) matrix-tuple cone is regarded as antecedent mathematical context rather than a freestanding novelty claim. Britnell and Wildon study commuting similarity-class types over finite fields, again a different invariant.

No exhaustive publication-priority certification is claimed. A general theorem covering compatible nilpotents across direct products of matrix factors could subsume this result; such a theorem was not identified in the checked sources. The core novelty assessment is therefore provisional and should be independently reviewed.

## Limitations

The odd-order and abelian assumptions on \(H\), and characteristic two for \(k\), are essential to the stated decomposition and enumeration; even-order or nonabelian kernels are not addressed. This counts left multiplication by square-zero elements, **not** derivations. It counts ordered tuples of elements, not orbits under the unit group, except for the explicit maximal elementary abelian subgroup count. It does not classify arbitrary nilpotent elements or the nonreduced scheme of solutions. The proof is complete for the stated objects, but historical priority and external validation are not certified.

## References

1. N. Makhijani, R. K. Sharma and J. B. Srivastava, *The unit group of finite group algebra of a generalized dihedral group*, Asian-European Journal of Mathematics 7 (2014), 1450034, DOI `10.1142/S179355711450034X`, first published June 18, 2014; full text: `https://web.iitd.ac.in/~rksharma/Research%20Publications/Journal/neha_aejm.pdf`.
2. N. V. Ngo and K. Šivic, *On varieties of commuting nilpotent matrices*, preprint `arXiv:1308.4438`, initially posted August 20, 2013; revised March 26, 2014.
3. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, Journal of the London Mathematical Society 83 (2011), 470–492, DOI `10.1112/jlms/jdq088`.
