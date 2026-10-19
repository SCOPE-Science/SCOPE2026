# Three-component commuting-tuple varieties of three-block nilradicals

## Finding

Consider the nilradical \(\mathfrak u_{r,s}(k)\) of the standard parabolic Lie algebra in \(\mathfrak{gl}_{r+s+1}(k)\) with consecutive diagonal-block sizes \((r,1,s)\). For every field \(k\), every pair of integers \(r,s\ge 2\), and every tuple length \(t\ge 2\), the *reduced* variety of pairwise-commuting ordered \(t\)-tuples has **exactly three geometrically irreducible components**. Their dimensions, without multiplicities, are
\[
trs+tr,\qquad trs+ts,\qquad trs+t+r+s-1.
\]
The first two are coordinate-linear components. The third is a rank-at-most-one determinantal component, with the middle upper-right blocks unrestricted. In this entire parameter family, the commuting-tuple variety is equidimensional if and only if \((r,s,t)=(2,2,3)\); otherwise it is not equidimensional.

For a finite field \(k=\mathbb F_q\), the number of labeled ordered pairwise-commuting tuples is exactly
\[
\boxed{C_t(q;r,s)=q^{rst}\left(q^{rt}+q^{st}-1+\frac{(q^r-1)(q^s-1)}{q-1}(q^t-1)\right).}
\]
This formula applies to every prime power \(q\), with no restriction on characteristic, and every \(r,s,t\ge 2\).

## Assumptions and scope

Write elements of \(\mathfrak u_{r,s}(k)\) uniquely as
\[
X(u,v,Z)=\begin{pmatrix}0_{r\times r}&u&Z\\0&0&v\\0&0&0_{s\times s}\end{pmatrix},
\quad u\in k^r,\ v\in (k^s)^*,\ Z\in M_{r\times s}(k).
\]
Here vectors \(u\) are columns and \(v\) are rows. We take the Lie bracket \([X,Y]=XY-YX\), including in characteristic two. Let \(\mathcal C_t(\mathfrak u_{r,s})\) denote the affine zero set of all equations \([X_i,X_j]=0\) for \(1\le i<j\le t\), endowed in the finding with its **reduced algebraic-variety structure**. The three component descriptions and the equidimensionality assertion are geometric statements after arbitrary field extensions, in particular over an algebraic closure. No assertion is made that the original polynomial-equation *scheme* is reduced.

For a tuple, set \(U=(u_1^\top,\ldots,u_t^\top)^\top\in M_{t\times r}(k)\), \(V=(v_1^\top,\ldots,v_t^\top)^\top\in M_{t\times s}(k)\), and \(W=(U\ V)\in M_{t\times(r+s)}(k)\). The three closed subsets, all times the full affine space of \(t\) central matrices \(Z_i\), are
\[
\mathcal X_U=\{V=0\},\qquad
\mathcal X_V=\{U=0\},\qquad
\mathcal X_D=\{\operatorname{rank}(W)\le1\}.
\]
The geometry is not a classification of simultaneous conjugacy orbits, of all nilpotent matrices, or of higher-block parabolic nilradicals.

## Proof

**1. Reduction to rank-one tensor equalities.** Multiplying the block matrices gives
\[
X(u,v,Z)X(u',v',Z')=X(0,0,uv'),
\]
where this identity denotes the matrix whose only potentially nonzero block is \(uv'\) in position \((1,3)\). Thus a tuple commutes pairwise if and only if
\[
u_iv_j-u_jv_i=0\in M_{r\times s}(k)\qquad(1\le i<j\le t).
\]
The \(Z_i\) do not occur in these equations and give a factor \(\mathbb A_k^{rst}\).

**2. Tensor-rigidity lemma.** Suppose one tuple member has both \(u_i\ne0\) and \(v_i\ne0\). For any index \(j\), the identity \(u_iv_j=u_jv_i\) implies the existence of a *single* scalar \(\lambda_j\in k\) with \(u_j=\lambda_ju_i\) and \(v_j=\lambda_jv_i\). To see this, choose \(a\) with \((u_i)_a\ne0\), so the \(a\)-th matrix row gives \(v_j=\lambda_jv_i\) with \(\lambda_j=(u_j)_a/(u_i)_a\). Because \(v_i\ne0\), the original matrix identity now forces \(u_j=\lambda_ju_i\). Hence all rows of \(W\) are multiples of row \(i\) and \(\operatorname{rank}(W)\le1\).

If there is no index with both \(u_i\ne0\) and \(v_i\ne0\), then the presence of an \(u\)-only nonzero member and a \(v\)-only nonzero member would give a nonzero outer-product commutator, impossible over any field. Therefore all \(v_i\) vanish or all \(u_i\) vanish. Conversely, each of these two conditions trivially implies pairwise commutation, and any rank-at-most-one \(W\) gives commutation because \((u_i,v_i)=\lambda_i(u,v)\) for all \(i\). The point-set equality is therefore
\[
\mathcal C_t(\mathfrak u_{r,s})_{\mathrm{red}}
=\mathcal X_U\cup\mathcal X_V\cup\mathcal X_D.
\]
The same reasoning applies over every extension of \(k\).

**3. Geometric irreducible components.** The first two subsets are affine linear spaces of dimensions \(rst+tr\) and \(rst+ts\). The third is the product of \(\mathbb A^{rst}\) with the determinantal variety \(\operatorname{rank}(W)\le1\). The rank-one locus is the image of the polynomial map \((a,b)\mapsto ab^\top\) from \(k^t\times k^{r+s}\), including the zero matrix. Over an algebraic closure it is irreducible; its dense nonzero locus has a one-dimensional scaling redundancy, so its dimension is \(t+r+s-1\). Hence \(\mathcal X_D\) is geometrically irreducible with the claimed dimension.

The three closed irreducible sets are pairwise noncontained when \(r,s,t\ge2\): a tuple with two independent nonzero rows in \(U\) and \(V=0\) belongs only to \(\mathcal X_U\); a tuple with two independent rows in \(V\) and \(U=0\) belongs only to \(\mathcal X_V\); a rank-one tuple with a nonzero mixed row belongs only to \(\mathcal X_D\). Thus they are exactly the three maximal irreducible closed subsets. No further components exist because the union is the entire reduced commuting variety.

**4. Equidimensionality exception.** Equal dimensions require \(tr=ts=t+r+s-1\). Hence \(r=s=d\ge2\) and
\[
t(d-1)=2d-1,\qquad t=2+\frac1{d-1}.
\]
The only integral solution with \(d,t\ge2\) is \(d=2,t=3\). In that instance all three components have dimension \(18\), since the free central factor has dimension \(12\). Every other parameter choice is non-equidimensional.

**5. Finite-field enumeration.** Over \(\mathbb F_q\), the pure-\(U\) locus has \(q^{tr}\) possibilities for \(W\), and the pure-\(V\) locus has \(q^{ts}\); they meet only in the zero matrix, yielding \(q^{tr}+q^{ts}-1\) distinct pure tuples. All remaining commuting \(W\) have a nonzero mixed row and rank one. Such a matrix determines its unique row line \(\ell\subset\mathbb F_q^{r+s}\) that is not contained in either coordinate summand. The number of mixed lines is
\[
L=\frac{(q^r-1)(q^s-1)}{q-1},
\]
since a mixed vector is a choice of nonzero vector in each summand, modulo the free action of \(\mathbb F_q^\times\). For any fixed mixed line, there are \(q^t-1\) nonzero ordered \(t\)-row matrices whose rows lie in that line. Different lines produce disjoint nonzero matrices. Adding pure and mixed counts and multiplying by \(q^{rst}\) choices of unrestricted central blocks proves the displayed formula.

## Verification

The accompanying standalone Python 3 program `verify.py` constructs the first superdiagonal block vectors over prime fields and an explicitly implemented field of four elements. It independently checks every outer-product commutation equation for every ordered tuple in the stated finite test configurations, classifies every commuting tuple by the three closed conditions, and matches the exact counting formula. The nine tested parameter quadruples \((q,r,s,t)\) are
\[
(2,2,2,2),(2,2,2,3),(2,2,2,4),(2,2,3,3),(2,3,2,3),
(3,2,2,2),(3,2,2,3),(4,2,2,2),(5,2,2,2).
\]
The terminal marker is `VERIFY_OK_THREE_BLOCK_COMMUTING_TUPLES`. In particular, the computed counts including central blocks are \(14{,}848\) for \((2,2,2,2)\), \(778{,}240\) for \((2,2,2,3)\), and \(1{,}216{,}468{,}449\) for \((3,2,2,3)\). These are finite consistency checks; the all-field geometry and all-prime-power count follow from the proof above rather than the finite experiments.

## Relationship to prior work

Goodwin and Röhrle studied commuting varieties of nilradicals, proving general structural results for Borel nilradicals and exhibiting a two-component parabolic boundary example arising from a flag with consecutive block sizes \((1,1,m)\) in Remark 3.1. That edge family is not claimed as new here. Restricting *both* endpoint blocks to sizes at least two changes the component picture, and allowing arbitrary tuple length reveals the isolated equidimensional case. Goddard and Goodwin study commuting pairs in the entire parabolic Lie algebra, a different ambient space. Bulois and Evain study commuting nilpotent matrices in parabolic subalgebras, a larger space containing nilpotents in Levi blocks, while Boos and Bulois investigate parabolic-conjugation orbit questions. None of these specific inspected statements provides the simultaneous component description and exact point count of the stated three-block nilradical family.

The proof uses standard rank-one determinantal geometry; neither irreducibility of rank-one determinantal varieties nor elementary projective-line counting is claimed as a new general result. The contribution is the precise three-component decomposition, the unique equidimensional parameter, and uniform all-arity finite-field count for the specified Lie nilradical. An independently located equivalent classification of this exact family could revise the originality assessment.

## Limitations

The classification is for the **reduced variety**; nilpotent embedded components, scheme-theoretic reducedness, local intersection multiplicities, and singularities are not determined. Only block types \((r,1,s)\) with \(r,s\ge2\), tuple lengths \(t\ge2\), and labeled tuples are covered. For arbitrary fields, the component dimensions are geometric; the counting formula is for finite fields. It does not count simultaneous-conjugacy orbits. Prior Borel and boundary parabolic results are not independently new. Literature coverage is bounded and independent mathematical audit has not been performed.

## References

1. Simon M. Goodwin and Gerhard Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras*, arXiv:1209.1289v1 (first public version 2012-09-06), especially Remark 3.1.
2. Russell Goddard and Simon M. Goodwin, *On commuting varieties of parabolic subalgebras*, arXiv:1606.02262 (first public version 2016-06-07), Sections 1–2.
3. Michaël Bulois and Laurent Evain, *Nested punctual Hilbert schemes and commuting varieties of parabolic subalgebras*, arXiv:1306.4838 (first public version 2013-06-20).
4. M. Boos and M. Bulois, *Parabolic conjugation and commuting varieties*, arXiv:1606.08840 (first public version 2016-06-28).
