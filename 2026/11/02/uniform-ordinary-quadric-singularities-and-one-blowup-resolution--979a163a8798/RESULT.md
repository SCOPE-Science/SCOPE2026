# Uniform ordinary-quadric singularities and one-blowup resolution of constant-rank pencil base loci

## Finding

Let \(k\) be an algebraically closed field of characteristic zero, let \(r\geq3\), and let \(\boldsymbol r=(r_1,\ldots,r_h)\) be any partition of \(r\) into positive integers. Let \(X_{\boldsymbol r}\subset\mathbb P^{2r+h-1}_k\) be the base locus of the nondegenerate rank-\(2r\) pencil of quadrics of Kronecker type \(\boldsymbol r\), defined explicitly below. Its singular **scheme**, not just its underlying singular set, is the reduced smooth rational normal scroll
\[
S_{\boldsymbol r}\cong\mathbb P_{\mathbb P^1}\!\left(\bigoplus_{i=1}^{h}\mathcal O_{\mathbb P^1}(r_i)\right),\qquad\dim S_{\boldsymbol r}=h.
\]
At every geometric point of this scroll, the pair \((X_{\boldsymbol r},S_{\boldsymbol r})\) has a Zariski-local model of the form
\[
\left(\mathbb A^h\times\{\textstyle\sum_{j=1}^{r-1}U_jV_j=0\},\quad\mathbb A^h\times\{U_1=V_1=\cdots=U_{r-1}=V_{r-1}=0\}\right).
\]
In particular the transverse hypersurface singularity is a nondegenerate ordinary quadratic cone of dimension \(2r-3\), independently of the partition. The complete intersection \(X_{\boldsymbol r}\) is irreducible, normal, Gorenstein, terminal and Fano. Blowing up its reduced singular scroll gives a smooth variety; its exceptional divisor is irreducible and is a smooth quadric bundle over \(S_{\boldsymbol r}\), with fibres \(Q^{2r-4}\) and discrepancy exactly \(2r-5\). The scheme-theoretic singularity and resolution statements are valid simultaneously for all partitions.

The rank-four boundary \(r=2\) has the same local formula with transverse equation \(U_1V_1=0\). It is a normal-crossings degeneration and is excluded from the irreducible/terminal assertion; the global reducibility in this boundary is known in the motivating paper.

## Assumptions and scope

Throughout, \(k\) is algebraically closed of characteristic zero; the conclusions apply to pencils over \(\mathbb C\) and to their base extensions. Set \(r=\sum_i r_i\), with each \(r_i\ge1\). For every block \(i\), introduce \(u_{i,j}\) for \(0\le j<r_i\) and \(v_{i,j}\) for \(0\le j\le r_i\). Thus there are \(r\) coordinates of type \(u\) and \(r+h\) of type \(v\). Define
\[
q_0=\sum_{i=1}^{h}\sum_{j=0}^{r_i-1}u_{i,j}v_{i,j},\qquad
q_1=\sum_{i=1}^{h}\sum_{j=0}^{r_i-1}u_{i,j}v_{i,j+1},\qquad X_{\boldsymbol r}=V(q_0,q_1).
\]
The associated symmetric pencil has constant rank \(2r\), no fixed kernel, and ambient dimension \(2r+h-1\). By the Kronecker classification, every nondegenerate pencil of constant rank \(2r\) is equivalent to one of these, with a uniquely determined partition up to permutation; the classification itself is **prior work**. We use the scheme-theoretic singular locus defined by the maximal minors of the Jacobian matrix of the two equations, in addition to \(q_0=q_1=0\). The exceptional divisor discrepancy is defined by \(K_{\widetilde X}=\pi^*K_X+a(E,X)E\).

## Proof

**1. The complete intersection and its singular support.** The two forms are independent and \(q_0\) is an irreducible quadric (its bilinear rank is \(2r\ge6\)); hence they form a regular sequence and \(X\) is an equidimensional complete intersection of dimension \(2r+h-3\). For any nonzero vector of \(u\)-coordinates, the two linear forms \(q_0,q_1\) in the \(v\)-variables are linearly independent: a dependence \(a q_0+b q_1\) would require \(u\) to be in the left kernel of every block matrix \((aI,bI)\), but each such \(r_i\)-by-\((r_i+1)\) Kronecker matrix has full row rank for \((a,b)\ne(0,0)\). Therefore the locus \(u\ne0\) in \(X\) is an irreducible affine-bundle chart family over \(\mathbb P^{r-1}\). Its complement \(u=0\) is \(\mathbb P^{r+h-1}\), of codimension \(r-2\ge1\) inside \(X\). Since a complete intersection is pure-dimensional, no extra component lies in this complement: \(X\) is irreducible.

The Jacobian can drop rank only when some nontrivial linear combination \(a\nabla q_0+b\nabla q_1\) vanishes. The \(v\)-derivatives force all \(u_{i,j}=0\) by the full-row-rank observation. At \(u=0\), the remaining equations are precisely
\[
a v_{i,j}+b v_{i,j+1}=0\qquad(0\le j<r_i,\ 1\le i\le h).
\]
For each \([a:b]\in\mathbb P^1\) the solution has one free scalar per block, and its projectivization is \(\mathbb P^{h-1}\). These kernels assemble into the smooth scroll \(S_{\boldsymbol r}\) described in the motivating work; in particular the reduced singular set is exactly \(S_{\boldsymbol r}\).

**2. Exact Zariski charts at every singular point.** Fix any block \(i_*\). On a chart where \(v_{i_*,r_{i_*}}=1\), introduce the parameter \(\alpha=v_{i_*,r_{i_*}-1}\). Write \(*\) for \((i_*,r_{i_*}-1)\). In \(q_1=0\), the coefficient of \(u_*\) is one, so eliminate \(u_*\). The remaining equation is exactly
\[
\sum_{(i,j)\ne *}u_{i,j}\,z_{i,j}=0,
\qquad z_{i,j}:=v_{i,j}-\alpha v_{i,j+1}.
\]
These are genuine polynomial coordinates: for each block, keep its top coordinate \(v_{i,r_i}\) as an auxiliary variable and recover lower coordinates recursively by \(v_{i,j}=z_{i,j}+\alpha v_{i,j+1}\). For the pivot block its top coordinate is one and its last \(z\)-coordinate is zero by the definition of \(\alpha\). Thus the chart is **isomorphic**, not merely formally equivalent, to \(\mathbb A^h\times V(\sum_{j=1}^{r-1}u_jz_j)\), with free variables \(\alpha\) and the \(h-1\) nonpivot top coordinates.

Dually, on a chart where \(v_{i_*,0}=1\), set \(\alpha=v_{i_*,1}\), pivot at \(*=(i_*,0)\), and eliminate \(u_*\) using \(q_0=0\). The residual equation is
\[
\sum_{(i,j)\ne *}u_{i,j}\,z_{i,j}=0,
\qquad z_{i,j}:=v_{i,j+1}-\alpha v_{i,j}.
\]
Now recover the other coordinates forward by \(v_{i,j+1}=z_{i,j}+\alpha v_{i,j}\), retaining the \(h-1\) nonpivot bottom coordinates. This too is an exact polynomial product chart.

To see that these charts cover \(S_{\boldsymbol r}\), at any scroll point choose the nonzero pair \([a:b]\) in the kernel equations from Step 1. If \(a\ne0\), all bottom-to-top recursions imply that a nonzero block has nonzero *top* coordinate. If \(b\ne0\), a nonzero block has nonzero *bottom* coordinate. Since at least one of \(a,b\) is nonzero, an appropriate chart always exists. The same product equations show that their singular ideals are exactly the reduced ideals \((u_1,\ldots,u_{r-1},z_1,\ldots,z_{r-1})\); away from the scroll the Jacobian has full rank. This proves the **scheme-theoretic** singular-locus statement.

**3. Normality, terminality, and resolution.** Each transverse quadratic form is nondegenerate of rank \(2r-2\). The scroll has codimension \(2r-3\ge3\) in \(X\); \(X\) is Cohen--Macaulay as a complete intersection and regular in codimension one, hence normal by Serre's criterion. Since it is a complete intersection in a smooth ambient projective space, it is Gorenstein. The local charts are products with ordinary quadratic singularities of dimension \(2r-3\ge3\).

Blow up the ideal \((u_1,\ldots,u_{r-1},z_1,\ldots,z_{r-1})\) in each chart. On any blowup chart the strict transform of \(\sum u_jz_j=0\) is an equation linear in a coordinate paired with the chosen exceptional coordinate, so it is smooth. The exceptional hypersurface in \(\mathbb P^{2r-3}\) is the smooth split quadric \(\sum U_jZ_j=0\) of dimension \(2r-4\). Since each such quadric is geometrically irreducible for \(r\ge3\) and the scroll is connected, the global exceptional divisor is irreducible. These local blowups glue to \(\operatorname{Bl}_{S_{\boldsymbol r}}X\), which is smooth and resolves all singularities.

The ordinary quadratic cone is a multiplicity-two hypersurface in smooth affine space of dimension \(2r-2\), blown up at its origin. The ambient blowup canonical formula and adjunction give
\[
a(E,X)=(2r-2)-1-2=2r-5>0.
\]
Any further divisor above the smooth resolution has positive discrepancy, so all discrepancies over \(X\) are positive: \(X\) is terminal. Finally, adjunction for the intersection of two quadrics in \(\mathbb P^{2r+h-1}\) gives \(-K_X\cong\mathcal O_X(2r+h-4)\), which is ample; hence \(X\) is Fano.

**4. Rank-four boundary.** With \(r=2\), the same exact coordinate transformations give \(u_1z_1=0\). The transverse quadratic splits into two hyperplanes, explaining the known reducible boundary and showing why the irreducible quadric-bundle resolution and terminality require \(r\ge3\).

## Verification

The standalone Python 3 script `verify_pencil_normal_forms.py` uses only the standard library. It symbolically verifies the elimination identities and both polynomial-coordinate inverses for every positive-integer partition of each \(2\le r\le8\) and every possible pivot block, totalling 432 exact checks. It also exhaustively enumerates projective points and Jacobian singular supports over \(\mathbb F_3\) for seven representative partitions, comparing them with the parametrized scroll and independently counting base-locus points. The expected success terminator is `ALL_CANONICAL_PENCIL_TESTS_PASS`. These finite checks are reproducibility aids only; the universally quantified assertions follow from the explicit algebraic proofs above.

## Relationship to prior work

Boralevi and Mezzetti [1], especially Theorem 2.3 and Section 3, classify the nondegenerate constant-rank pencils by partitions, give canonical blocks, and identify the **set-theoretic** singular locus of the base intersection as the associated rational normal scroll. Their paper also records reducibility for rank four. These results are acknowledged and are not presented as new. The additional result here is a uniform *exact Zariski-local singularity normal form* for all ranks and partitions; it determines the nonreduced-versus-reduced Jacobian scheme question and the blowup's geometry and discrepancy, which do not appear in the inspected original article.

Wang [2] studies maximal linear spaces in base loci of pencils admitting nondegenerate quadrics, including singular **regular** pencils. The present nondegenerate-in-the-sense-of-no-common-kernel constant-rank pencils have **no nonsingular quadric member**, so Wang's regular-pencil hypotheses do not apply. More broadly, a quadratic-cone blowup is standard once a quadratic normal form is known; its specific uniform occurrence along every partition scroll, with exact coordinates and singular scheme, is the geometric content established here.

## Limitations

The theorem is for algebraically closed characteristic zero and nondegenerate pencils of constant rank \(2r\), \(r\ge3\). Degenerate pencils with fixed kernel, nonconstant-rank pencils, and possible characteristic-two phenomena are not classified. The blowup is a resolution; no claim is made that it is crepant, small or the unique resolution. The Fano designation means that the anticanonical bundle is ample; no assertion of \(\mathbb Q\)-factoriality is made. This analysis does not classify the global isomorphism type of the exceptional quadric bundle beyond its local smooth fibres. Originality is assessed against the inspected primary article, relevant accessible regular-pencil literature, mathematical-record searches and accessible historical claims; unindexed earlier work, especially classical geometric literature, might contain equivalent local observations. No independent external audit or validation has been performed.

## References

[1] Ada Boralevi and Emilia Mezzetti, *Pencils of singular quadrics of constant rank and their orbits*, arXiv:2206.00503v1 (public 2022-06-01), Sections 2--4; DOI:10.13137/2464-8728/34102. https://arxiv.org/html/2206.00503v1

[2] Xiaoheng Wang, *Maximal linear spaces contained in the base loci of pencils of quadrics*, Algebraic Geometry **5** (2018), 359--397; arXiv:1302.2385. https://arxiv.org/abs/1302.2385
