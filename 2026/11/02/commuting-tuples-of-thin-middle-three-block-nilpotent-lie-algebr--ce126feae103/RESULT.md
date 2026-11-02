# Commuting tuples of thin-middle three-block nilpotent Lie algebras

## Finding

For integers \(a,c\ge1\), every field \(k\), and \(m\ge1\), the reduced \(m\)-fold pairwise-commuting variety of the two-step nilpotent three-block Lie algebra \(\mathfrak n_{a,1,c}(k)\) is explicitly a union of a determinantal cone and at most two linear spaces, times an unconstrained central space. In particular, for \(m\ge2\), there are exactly
\[
1+\mathbf1_{a\ge2}+\mathbf1_{c\ge2}
\]
geometrically irreducible components; for \(m=1\), there is one. The components are described explicitly below. The finite-field ordered-tuple count, valid also for \(m=0\), is
\[
T_m(q;a,c)=q^{acm}\left[q^{am}+q^{cm}-1+
\frac{(q^a-1)(q^c-1)(q^m-1)}{q-1}\right].
\]
The corresponding three-block unitriangular group has precisely the same commuting-tuple count. As a further intrinsic classification, the maximal \(k\)-linear abelian subalgebras and their finite-field number are determined below.

## Assumptions and scope

Fix positive integers \(a,c\), any field \(k\), and ordered tuple length \(m\). Define the Lie algebra to have elements
\[
X(u,v,z)=\begin{pmatrix}
0_{a\times a}&u&z\\
0&0&v\\
0&0&0_{c\times c}
\end{pmatrix},
\quad u\in k^a,\quad v\in (k^c)^*,\quad z\in k^{a\times c},
\]
with bracket \([X,Y]=XY-YX\). A tuple commutes when every pairwise bracket is zero. Geometric components refer to the reduced algebraic set over an algebraic closure; no conclusion about the nonreduced commuting scheme is asserted. For point counting, \(k=\mathbb F_q\) is any finite field, without characteristic restriction. Let \(U_{a,1,c}(k)=I+\mathfrak n_{a,1,c}(k)\) with matrix multiplication.

## Proof

**1. Bracket and central coordinates.** Direct block multiplication gives
\[
[X(u,v,z),X(u',v',z')]=X(0,0,uv'-u'v).
\]
All central \(z\) coordinates are arbitrary; over every field the full center is the \(ac\)-dimensional \(z\)-block (indeed, every nonzero \(u\) brackets with a suitably chosen \(v'\), and conversely). Write the noncentral tuple as \((u_i,v_i)_{i=1}^m\), and form its \((a+c)\)-by-\(m\) matrix of columns \(w_i=(u_i,v_i)\).

**2. Exhaustive three-way decomposition.** Define
\[
A_m=\{v_1=\cdots=v_m=0\},\qquad
B_m=\{u_1=\cdots=u_m=0\},\qquad
D_m=\{\operatorname{rank}(w_1,\ldots,w_m)\le1\}.
\]
Each of these consists of commuting tuples. Conversely, suppose \(u_i v_j=u_jv_i\) for every pair and the tuple belongs to neither coordinate side. Choose \(i\) with \(u_i\ne0\) and \(j\) with \(v_j\ne0\). Since \(u_iv_j\ne0\), the equality \(u_i v_j=u_jv_i\) forces both \(u_j\ne0\) and \(v_i\ne0\). Fix this mixed index \(i\). For each \(h\), the equality \(u_i v_h=u_hv_i\), with \(u_i,v_i\ne0\), implies \(u_h=t_hu_i\) and \(v_h=t_hv_i\) for the **same** scalar \(t_h\). This is immediate by taking a nonzero entry of \(u_i\), respectively \(v_i\), then substituting. Hence every column \(w_h\) is proportional to \(w_i\), so the tuple lies in \(D_m\). We have proved the set-theoretic identity
\[
\mathcal C_m(\mathfrak n_{a,1,c})_{\mathrm{red}}
\cong k^{acm}\times(A_m\cup B_m\cup D_m).
\]
All three pieces are Zariski closed over the ground field, so the equality also holds after extension to an algebraic closure and describes the reduced locus.

**3. Components and dimensions.** The coordinate spaces \(A_m,B_m\) are irreducible of dimensions \(am,cm\). The rank-at-most-one cone \(D_m\) is geometrically irreducible because it is the closure of matrices \(wt^T\) with \(w\in k^{a+c}\setminus\{0\}\) and \(t\in k^m\setminus\{0\}\); its nonzero locus is parametrized with one-dimensional rescaling fibers, giving dimension \(a+c+m-1\). At \(m=1\), \(D_m\) is the entire noncentral ambient space. For \(m\ge2\), \(D_m\) cannot be contained in either coordinate space because it contains mixed columns. Also, \(A_m\subset D_m\) exactly when \(a=1\): if \(a\ge2\), use two linearly independent \(u\)-columns. Likewise \(B_m\subset D_m\) exactly when \(c=1\). Neither coordinate side contains the other. Thus the irreducible components are exactly those claimed, with the additional \(acm\) free central dimensions.

**4. Exact finite-field count.** The union of the two coordinate sides has \(q^{am}+q^{cm}-1\) points. Every remaining commuting tuple is a rank-one matrix \(wt^T\) with both the first \(a\) coordinates and last \(c\) coordinates of \(w\) nonzero, and \(t\ne0\). There are \((q^a-1)(q^c-1)(q^m-1)\) parameter triples, with exactly \(q-1\) parametrizations per nonzero matrix under \((w,t)\mapsto(\lambda w,\lambda^{-1}t)\). Multiplying by the \(q^{acm}\) unrestricted central tuples yields the displayed formula. For \(m=0\), direct convention gives one empty tuple and the same formula evaluates to one. In the group \(I+\mathfrak n\), \((I+X)(I+Y)=(I+Y)(I+X)\) is equivalent to \(XY=YX\), so the formula applies unchanged.

**5. All maximal linear abelian subalgebras.** Any maximal \(k\)-linear abelian subalgebra must contain the full center, since adjoining it preserves abelianity. Its image in \(k^a\oplus(k^c)^*\) is a pairwise bracket-zero \(k\)-linear subspace. If this image contains a mixed point \((u,v)\) with both entries nonzero, the equality of outer products from Step 2 shows that every other image vector is proportional to that point; thus it is precisely its one-dimensional span. If it contains no mixed point, any linear subspace mixing nonzero pure-u and nonzero pure-v points would contain their sum, a contradiction; hence the image lies entirely in one coordinate side, and maximality forces the whole coordinate side. Conversely all listed subalgebras are maximal by the same centralizer argument. Over \(\mathbb F_q\), mixed lines are in bijection with the mixed nonzero vectors modulo scalar rescaling, totaling \((q^a-1)(q^c-1)/(q-1)\); with the two pure-side spaces, the count is
\[
2+\frac{(q^a-1)(q^c-1)}{q-1}.
\]
The maximal subalgebra dimensions are \(ac+a\), \(ac+c\), and \(ac+1\), respectively.

## Verification

`verify_thin_middle.py` is a standalone Python 3 standard-library checker. Run `python3 verify_thin_middle.py`; successful output ends in `THIN_MIDDLE_COMMUTING_GEOMETRY_OK 13 2`. It exhaustively checks, for 13 finite-field configurations over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), the pairwise commutativity equations against the three-way geometric decomposition and checks the resulting complete point count. It also enumerates all linear subspaces and tests the maximal abelian classification for two small fields and block configurations. For instance, with \((q,a,c,m)=(2,2,2,2)\), there are 58 noncentral commuting pairs, and with arbitrary central blocks there are \(58\cdot2^8=14848\) commuting pairs. The finite computations corroborate but do not replace the characteristic-free proofs above.

## Relationship to prior work

Lampret and Vavpetič (2015, arXiv:1504.07743v1) study cohomology of poset Lie algebras, including strictly block-upper triangular examples; their results do not state the all-arity commuting-locus decomposition or the finite-field tuple census. Goddard and Goodwin (2016, arXiv:1606.02262v1) analyze the commuting variety of **the full parabolic Lie algebra for pairs**, whereas the present theorem concerns tuples in a fixed **nilradical** with a one-dimensional middle block. Kaur, Sharma and Singh (2020, arXiv:2006.01493v1) compute branching and commuting probabilities for low-dimensional unitriangular groups in bounded tuple lengths; this already covers some \(a=c=1\) Heisenberg specializations but neither arbitrary outer dimensions nor the component classification. Li (2024, arXiv:2403.13953) studies full upper-triangular matrix commuting schemes; the restriction and geometric component result here are different. The standard rank-one determinantal geometry is used as a proof tool, not claimed new. Complete publication priority remains unverified.

## Limitations

The geometry is for **reduced** loci, not scheme multiplicities, singular schemes, or normalization. Only Lie-algebra **linear** maximal abelian subalgebras are enumerated; the result does not classify all additive subgroups of the finite group when \(q\) is nonprime. Arbitrary block sizes \((a,b,c)\) with \(b>1\) are not covered. The underlying Heisenberg case \(a=c=1\) is classical; novelty is assessed for the uniform outer-block family and geometric-plus-arithmetic package. A more general theorem on two-step nilpotent commuting varieties may subsume the classification; this remains a specific priority risk. No independent mathematical audit has been performed.

## References

1. L. Lampret and A. Vavpetič, *(Co)Homology of Poset Lie Algebras*, arXiv:1504.07743v1 (public 2015-04-29), https://arxiv.org/abs/1504.07743.
2. R. Goddard and S. M. Goodwin, *On commuting varieties of parabolic subalgebras*, arXiv:1606.02262v1 (public 2016-06-07), https://arxiv.org/abs/1606.02262.
3. M. Kaur, U. Sharma and A. Singh, *Branching Rules and Commuting Probabilities for Triangular and Unitriangular Matrices*, arXiv:2006.01493v1 (public 2020-06-02), https://arxiv.org/abs/2006.01493.
4. G. Li, *Commuting Schemes of Upper Triangular Matrices and Representation Homology*, arXiv:2403.13953 (public 2024-03-20), https://arxiv.org/abs/2403.13953.
