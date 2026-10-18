# Fibonacci components and exact singular points of adjacent-Plücker Grassmann sections

## Finding
Let \(k\) be algebraically closed, of any characteristic, and \(n\ge4\). Define the closed subscheme
\[
X_n=\operatorname{Gr}(2,n)\cap V(p_{12},p_{23},\ldots,p_{n-1,n})
\]
in the Plücker embedding. The section is **reduced and a local complete intersection**, has pure dimension \(n-3\), and has precisely \(F_n-1\) irreducible components, where \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). Its degree and dualizing sheaf are
\[
\deg X_n=\frac1{n-1}\binom{2n-4}{n-2},\qquad \omega_{X_n}\simeq\mathcal O_{X_n}(-1).
\]
For an arbitrary point, choose a rank-two \(2\times n\) representative matrix with columns \(v_1,\dots,v_n\in k^2\). Then the *complete pointwise smoothness test* is
\[
\boxed{\ X_n\text{ smooth at the point}\ \Longleftrightarrow\ \begin{cases}
(v_i,v_{i+1})\ne(0,0)&(1\le i<n),\\
\det(v_{j-1},v_{j+1})\ne0&\text{for every }2\le j\le n-1\text{ with }v_j=0.
\end{cases}}
\]
A zero column is an intrinsic property of the represented row plane, so this test is independent of the representative. At a generic point with exactly two adjacent zero columns in interior positions, the completed germ is an ordinary crossing of two smooth branches.

## Assumptions and scope
All schemes and dimensions are over an algebraically closed field \(k\); there is no characteristic restriction. In Plücker coordinates \(p_{ab}\) denotes the \(2\times2\) determinant of columns \(a,b\) in a representative rank-two matrix. The projective Grassmannian \(\operatorname{Gr}(2,n)\) is smooth of dimension \(2n-4\) and \(\omega_{\operatorname{Gr}(2,n)}=\mathcal O(-n)\). A nonempty subset \(S\subseteq\{2,\ldots,n-1\}\) is **independent** if it contains no pair of consecutive integers. Removing its positions leaves \(|S|+1\) nonempty consecutive blocks of indices.

The irreducible component \(C_S\) is the closure in \(\operatorname{Gr}(2,n)\) of planes represented by matrices satisfying: columns indexed by \(S\) are zero; columns in each remaining block are all nonzero and proportional; and all the block directions together span \(k^2\). This description specifies an irreducible locally closed stratum, not an assertion that the component is smooth or normal.

## Proof
**1. Block stratification and dimensions.** For any rank-two matrix obeying the consecutive minors, let \(Z\) be its exact zero-column index set, and let \(B_1,\ldots,B_r\) be the nonempty consecutive blocks of the complement. Every block has proportional columns, since all consecutive determinants within it vanish. Necessarily \(r\ge2\), or the matrix has rank at most one. Choose for each block a line in the corresponding coordinate subspace, parametrized by \(\mathbb P^{|B_s|-1}\). A rank-two row plane inside the direct sum of those \(r\) lines is a point of a relative \(\operatorname{Gr}(2,r)\); restricting to the open part where no block disappears recovers the exact-zero stratum. Its dimension is therefore
\[
\sum_{s=1}^r(|B_s|-1)+2(r-2)=n-|Z|+r-4.
\]
The parameter space is irreducible. For a path, \(r\le|Z|+1\), with equality precisely when \(Z\) is an independent subset of interior indices. Thus every stratum has dimension at most \(n-3\); equality holds exactly for the nonempty independent interior sets. There are finitely many zero patterns, so \(\dim X_n=n-3\), and all top-dimensional strata are irreducible and have distinct closures. The count of such subsets is \(F_n-1\), by the standard include/exclude-first-vertex recursion for independent sets of a path of length \(n-2\).

**2. Scheme structure.** The ambient smooth Grassmannian has dimension \(2n-4\), while \(X_n\) is defined by exactly \(n-1\) hyperplanes and has underlying dimension \(n-3\). By the height criterion for complete intersections in a regular local ring, these hyperplanes form a regular sequence locally: the scheme is a local complete intersection and is Cohen–Macaulay. On each top-dimensional stratum choose the directions of consecutive surviving blocks to be distinct. The differential calculation in Step 3 proves that the \(n-1\) equations have independent differentials there, so the scheme is generically reduced. A Cohen–Macaulay scheme that is generically reduced is reduced (the \(S_1+R_0\) reducedness criterion). Therefore the closures of the top-dimensional strata are *all* irreducible components, without multiplicities. The adjunction formula gives \(\omega_{X_n}=\mathcal O(-n+n-1)=\mathcal O(-1)\). Its degree is the Plücker degree of \(\operatorname{Gr}(2,n)\), since regular hyperplane sections preserve degree. The classical Grassmann degree formula yields the displayed Catalan number.

**3. Exact tangent-space test.** Lift the point locally to the open rank-two locus of \(2\times n\) matrices. This map to the Grassmannian is a smooth \(\operatorname{GL}_2\)-torsor; smoothness and the rank of the defining differential system are detected upstairs. For \(f_i=\det(v_i,v_{i+1})\), the differential is
\[
df_i=\det(dv_i,v_{i+1})+\det(v_i,dv_{i+1}).
\]
If two consecutive columns vanish, their common edge equation has zero differential, so the Jacobian rank is below \(n-1\). Suppose instead all zeros are isolated. Inside a block of consecutive nonzero columns, its edge differentials are linearly independent (eliminate successively the perturbations of the last column). An edge meeting a zero column involves *only* perturbations of that zero column, while internal-block differentials involve only nonzero columns, so the ranks add. A zero endpoint gives a single nonzero linear form; an interior zero gives two forms on its two-dimensional perturbation space. These two forms are independent exactly when the two neighboring nonzero columns are linearly independent. Hence the complete differential system has rank \(n-1\) precisely under the displayed criterion. Since the scheme is a local complete intersection of that codimension, the Jacobian criterion proves the smoothness equivalence.

**4. Transverse node stratum.** Fix \(2\le j\le n-2\) and take a point with \(v_j=v_{j+1}=0\), every other column nonzero, columns left of the pair proportional to one direction \(L\), and columns right proportional to an independent direction \(R\). After choosing a local gauge and solving the edge equations entirely within the left and right blocks, the equations adjacent to the missing pair force the two variable columns to be \(v_j=aL\) and \(v_{j+1}=bR\). Their connecting determinant becomes \(ab\det(L,R)=0\), with \(\det(L,R)\) a unit. All remaining coordinates are regular parameters. Because the singular stratum has dimension \(n-4\), the completion is
\[
k[[t_1,\ldots,t_{n-4},a,b]]/(ab).
\]
This is a generic local statement on these specified strata, not a claim about arbitrary multiple-zero intersections.

## Verification
The accompanying standalone `verify.py` enumerates row-reduced rank-two representatives over \(\mathbb F_2\) for \(n=4,5,6,7\), and over \(\mathbb F_3\) for \(n=4,5\). It independently computes the full \((n-1)\times 2n\) Jacobian rank of consecutive determinants and checks it against the zero-column smoothness criterion for **every** solution point in those finite Grassmannians. It also enumerates the independent interior cut sets. The script prints `VERIFY_OK` after all checks. These finite-field checks illustrate the characteristic-free proof but are not its substitute.

## Relationship to prior work
Hoşten–Sullivant, *Ideals of Adjacent Minors* (first public arXiv posting 23 June 2003), and Herzog–Hibi–Hreinsdóttir–Kahle–Rauh, *Binomial Edge Ideals and Conditional Independence Statements* (first posting 25 September 2009, Example 3.5), give the primary decomposition and cut-set description of the **affine** adjacent-minor ideal. In particular the independent-set indexing is an existing combinatorial phenomenon, not presented here as a newly discovered affine primary decomposition. The rank-two Grassmannian section is related by passing to the rank-two locus and taking the row-operation quotient, which removes the all-proportional affine component.

Damadi–Rahmati, *Smoothness in Binomial Edge Ideals* (2016), treats a graph-level condition for singular irreducible components of the affine binomial-edge varieties. Its componentwise edge-smoothness definition and existential graph criterion differ from the complete **pointwise smooth/singular test for the projective Grassmannian intersection** established here. General smoothness criteria for individual positroid varieties (Billey–Weaver, 2022) provide related background but do not, in the inspected abstract, supply this reducible path-section calculation. The explicit scheme properties, all-characteristic smooth-point criterion, and ordinary-crossing neighborhood give the projective-geometric refinement.

## Limitations
The criterion classifies the smooth locus and thereby determines the reduced singular locus set-theoretically, but this result does **not** claim a primary decomposition of its Jacobian singular scheme, a count of all irreducible components of that singular support, or formal local models at all nongeneric intersections. The decomposition of the affine adjacent-minor ideal is established prior art. Possible implicit translations of earlier binomial-edge ideal geometry or later positroid smoothness results are a residual originality risk. No independent audit is asserted.

## References
1. S. Hoşten and S. Sullivant, *Ideals of Adjacent Minors*, arXiv:math/0306318, first posted 2003-06-23; Journal of Algebra 277 (2004), 615–642. https://arxiv.org/abs/math/0306318
2. J. Herzog, T. Hibi, F. Hreinsdóttir, T. Kahle and J. Rauh, *Binomial Edge Ideals and Conditional Independence Statements*, arXiv:0909.4717, first posted 2009-09-25, Example 3.5. https://arxiv.org/abs/0909.4717
3. H. Damadi and F. Rahmati, *Smoothness in Binomial Edge Ideals*, Mathematics 4 (2016), 37. https://doi.org/10.3390/math4020037
4. S. Billey and J. Weaver, *A Pattern Avoidance Characterization for Smoothness of Positroid Varieties*, arXiv:2204.09013 (2022). https://arxiv.org/abs/2204.09013
