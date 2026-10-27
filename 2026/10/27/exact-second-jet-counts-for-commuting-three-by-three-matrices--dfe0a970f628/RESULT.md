# Exact second-jet counts for commuting three-by-three matrices

## Finding
Let \(q\) be any prime power, \(k=\mathbb F_q\), and \(R=k[t]/(t^3)\). Define \(J_2(q)\) to be the number of ordered pairs \((A(t),B(t))\in M_3(R)^2\) satisfying \([A(t),B(t)]=0\). Write
\[
L=(q^2+q+1)^2,\quad S=q(q-1)L,\quad
T=q^{10}+Sq^5+(q^9-q-S)q^3,\quad
U=q^2(q^2-1)L,\quad V=T-U-q^2.
\]
Then the **exact second-jet point count**, valid without any characteristic restrictions, is
\[
\boxed{J_2(q)=Vq^{24}+Uq^{23}(q^3+q^2-1)+Tq^{20}.}
\]
More precisely, the commuting-pair equation scheme \(\mathcal C=\operatorname{Spec}k[a_{ij},b_{ij}]/([A,B]_{ij})\) has exactly three geometric Jacobian-tangent strata. For a base pair \((A_0,B_0)\in\mathcal C(k)\), the common centralizer dimension is \(d\in\{3,5,9\}\), and the corresponding tangent dimension is \(9+d\). There are exactly \(V,U,q^2\) such base pairs with \(d=3,5,9\), respectively. The numbers of commuting second-order lifts *per fixed base pair* are, respectively,
\[
\boxed{q^{24},\qquad q^{23}(q^3+q^2-1),\qquad q^{18}T.}
\]
The non-smooth locus of the **equation scheme** has reduced support equal to the closure of the set of pairs
\[
(A_0,B_0)=(\alpha I_3+uN,\,\beta I_3+vN),
\quad \operatorname{rank}(N)=1,\quad (u,v)\ne(0,0),
\]
together with scalar pairs. It is irreducible, rational, of dimension \(8\), and has exactly \(U+q^2\) rational points. Its non-scalar part is birational to a product of a two-dimensional affine space and the nonzero affine cone over the Segre variety \(\mathbb P^1\times\mathbb P^2\times\mathbb P^2\). These geometric assertions concern the defining scheme's Jacobian-tangent behavior and do **not** assert a description of the singular scheme structure or identify the reduced variety's scheme-theoretic singular locus.

## Assumptions and scope
All matrices are \(3\times3\); all field orders \(q=p^f\) and all characteristics, including \(2\) and \(3\), are allowed. A second-order jet means a pair
\[
A(t)=A_0+tA_1+t^2A_2,\qquad B(t)=B_0+tB_1+t^2B_2
\]
with coefficients in \(M_3(k)\), satisfying the three coefficient equations
\[
[A_0,B_0]=0,\qquad
[A_0,B_1]+[A_1,B_0]=0,\qquad
[A_0,B_2]+[A_1,B_1]+[A_2,B_0]=0.
\]
Here \([X,Y]=XY-YX\), the centralizer of a pair means the \(k\)-vector space \(\{Z:[Z,A_0]=[Z,B_0]=0\}\), and its dimension is denoted \(d\). Counts refer to actual finite-field points, not orbit counts or nonreduced scheme lengths. The underlying commuting variety is known to be irreducible of dimension \(12\).

## Proof
**1. Common-centralizer stratification.** A non-scalar \(3\times3\) matrix is either cyclic (its minimal polynomial has degree \(3\)) or has the form \(\alpha I_3+N\) with \(\operatorname{rank}N=1\). In the latter case \(\alpha\) is unique: if two different scalar shifts had rank at most one, the rank inequality would force their nonzero scalar difference times \(I_3\) to have rank at most two, a contradiction. The first case has centralizer dimension \(3\); the second has centralizer dimension \(5\); scalar matrices have centralizer dimension \(9\). These cases follow from rational canonical form, or from the two forms for rank-one matrices: a rank-one idempotent up to nonzero scaling if its trace is nonzero, and \(E_{12}\) if its trace is zero.

For \(N\) of rank one, let \(D=C_{M_3(k)}(N)\), a five-dimensional algebra. In the nonzero-trace case, \(D\cong M_2(k)\oplus k\); its center has dimension \(2\), and every element outside its center has centralizer in \(D\) of dimension \(3\). In the trace-zero case, take \(N=E_{12}\) and write
\[
D=\left\{\begin{pmatrix}a&b&c\\0&a&0\\0&d&e\end{pmatrix}:a,b,c,d,e\in k\right\}.
\]
Its center consists of \(aI_3+bE_{12}\). If \(B\in D\) has parameters \((a,b,c,d,e)\), then the conditions for \(X\in D\) to commute with \(B\), written for the three coordinates \((X_{13},X_{32},X_{11}-X_{33})\), have coefficient matrix
\[
\begin{pmatrix}d&-c&0\\ e-a&0&c\\0&a-e&-d\end{pmatrix}.
\]
It has rank \(0\) precisely when \(c=d=e-a=0\), and rank \(2\) otherwise; the determinant always vanishes, and a nonzero square among its two-by-two minors proves rank at least two in the latter case. Thus \(\dim C_D(B)\) is \(5\) for \(B\in Z(D)\) and \(3\) otherwise. This also verifies the characteristic-two boundary.

For a commuting pair with a non-scalar noncyclic entry \(A_0=\alpha I_3+N\), the common centralizer is \(C_D(B_0)\). It has dimension \(5\) precisely when \(B_0\in kI_3+kN\), and dimension \(3\) otherwise. If one entry is scalar the same statement follows from the other entry; if both are scalar, \(d=9\). Hence the noncentral \(d=5\) pairs are exactly the linearly dependent rank-one directions claimed above. There are no other common-centralizer dimensions.

The trace form \((X,Y)\mapsto\operatorname{tr}(XY)\) is nondegenerate in every characteristic. For the Jacobian map
\[
\Phi_{A_0,B_0}(X,Y)=[X,B_0]+[A_0,Y]
\]
its image has annihilator precisely \(C(A_0,B_0)\), giving \(\dim\ker\Phi=18-(9-d)=9+d\). Since the underlying commuting variety has local dimension \(12\), this determines the smooth and non-smooth points of the defining equation scheme. The non-smooth support is irreducible of dimension \(8\): its non-scalar part is dominated by the irreducible space obtained from the scalar parameters \((\alpha,\beta)\) and nonzero rank-one tensors of shape \(2\times3\times3\). It is rational: on a dense open set with three suitable off-diagonal entries nonzero, a rank-one minor gives the repeated scalar eigenvalue rationally, for example \(\alpha=A_{kk}-A_{ik}A_{kj}/A_{ij}\) for distinct \(i,j,k\), and then \(\beta\) is obtained from the proportional off-diagonal entries of \(B\). The projective tensor base is \(\mathbb P^1\times\mathbb P^2\times\mathbb P^2\), of dimension \(5\); the affine cone has dimension \(6\), giving \(8\) after adding scalar parameters. The closedness follows alternatively from the determinantal condition \(d\ge5\).

**2. Counts of base pairs.** The number of projective lines of rank-one matrices in \(M_3(k)\) is
\[
L=\left(\frac{q^3-1}{q-1}\right)^2=(q^2+q+1)^2.
\]
Uniqueness of the scalar shift shows that the number of non-scalar noncyclic matrices is \(S=q(q-1)L\). The other \(q^9-q-S\) non-scalar matrices are cyclic. Summing the number of commuting partners, respectively \(q^9,q^5,q^3\), yields \(T\). A non-scalar \(d=5\) pair is determined uniquely by two scalar shifts, a rank-one *projective* matrix line, and a nonzero ordered coefficient pair, giving \(U=q^2L(q^2-1)\). Exactly \(q^2\) pairs are scalar in both entries. The remaining \(V=T-U-q^2\) have \(d=3\).

**3. Second-jet fibers.** Above any smooth \(d=3\) base pair, the equation scheme is smooth of relative dimension \(12\) over the perfect field \(k\). Consequently every first-order lift has exactly \(q^{12}\) second-order lifts and there are \(q^{12}\) first-order lifts, giving \(q^{24}\).

Any non-scalar \(d=5\) base pair is changed by scalar translations, an invertible \(2\times2\) linear change of the two matrix variables, and a similarity transformation to \((N,0)\), with \(N\) a nonzero rank-one matrix. These operations preserve all truncated commutation equations. At this base pair, the first-order equation is \([N,B_1]=0\). Put \(D=C(N)\). For any \(B_1\in D\), the second-order equation is solvable in \(B_2\) precisely when
\[
[A_1,B_1]\in\operatorname{im}(\operatorname{ad}_N)=D^\perp
\]
for the trace pairing. As \(A_1\) varies, the obstruction has rank
\[
\dim[B_1,D]=5-\dim C_D(B_1)=
\begin{cases}0,& B_1\in Z(D),\\2,&B_1\notin Z(D).\end{cases}
\]
There are \(q^2\) elements in \(Z(D)\), and \(q^5-q^2\) outside. For each \(B_1\), the number of admissible \(A_1\) is respectively \(q^9\) or \(q^7\). Every admissible pair \((A_1,B_1)\) has \(q^5\) choices for \(B_2\) and \(q^9\) arbitrary choices for \(A_2\). Therefore each non-scalar \(d=5\) base has exactly
\[
q^{14}\bigl(q^2q^9+(q^5-q^2)q^7\bigr)=q^{23}(q^3+q^2-1)
\]
second-order lifts. This is the nontrivial rank-two obstruction contribution.

Above a scalar pair \((\alpha I_3,\beta I_3)\), all first-order coefficients are free, while the second-order equation reduces to \([A_1,B_1]=0\). There are \(T\) such pairs, and \(A_2,B_2\) are arbitrary, yielding \(q^{18}T\) lifts. Multiplying the three fiber sizes by the corresponding \(V,U,q^2\) base counts proves the formula.

## Verification
The standalone Python file `verify_jet3.py` supplies independently implemented finite-field arithmetic, matrix multiplication, Gaussian elimination, and centralizer enumeration. It checks both distinct rank-one similarity types in characteristics \(2,3,5\) and over the nonprime field \(\mathbb F_4\). In characteristic two it exhausts all \(512\) matrices \(A_0\), all commuting partners \(B_0\), the resulting joint-centralizer strata, and *every* obstruction test over the two rank-one representatives for each \((A_1,B_1)\) satisfying the first-order equation. Over \(\mathbb F_3\) it also exhausts all \(19683\) possible individual base matrices to verify the cyclic/noncyclic census. The script computes all finite-field totals directly from these checks and prints `VERIFY_OK_SECOND_JET_GL3_ALL_FOUR_FIELDS` only on success. Sample outputs: \(J_2(2)=177234509824\) and \(J_2(3)=268084657893593529\). Finite tests corroborate the proof and do not establish the universal formula by themselves.

## Relationship to prior work
Gerstenhaber's classical commuting-pair theorem supplies the dimension \(12\) of the underlying variety. Popov, *Irregular and singular loci of commuting varieties* (arXiv:0801.3074; first posted 20 January 2008), studies irregular and singular loci in characteristic zero and establishes codimension-four irregular components. Sethuraman and Šivic, *Jet schemes of the commuting matrix pairs scheme* (arXiv:0902.3467; posted 19 February 2009), prove irreducibility of every finite-order jet scheme for \(3\times3\) commuting pairs, but the inspected paper does not supply an all-\(q\) count of the second jet. Britnell and Wildon (arXiv:1001.0811) investigate matrix centralizer class types over finite fields. Sharma, *Simultaneous similarity classes of commuting matrices over a finite field* (arXiv:1409.2698; first posted 7 September 2014), gives complete branching rules in size three, including dimensions of common centralizers and the number of orbit types. These rules substantially overlap with the **base-pair** classification here and are not claimed as new. The specific contribution is the uniform second-order obstruction calculation across both rank-one centralizer types and the resulting arithmetic count of jets over the truncated polynomial ring. The full priority claim remains subject to comparison with additional literature on commuting matrices over finite local rings.

## Limitations
The exact count is for jets through degree two and matrices of order three, not all jet orders or general matrix sizes. It is a count of points of a scheme, not its scheme length or a computation of Hilbert-series multiplicities. The irreducible dimension-eight locus describes non-smooth points of the *equation scheme* via its Jacobian; no claim is made about scheme-theoretic defining equations for that locus or about radicality of the original commuting ideal. The statement has been checked mathematically in this report but has not received independent mathematical validation. Historical priority remains uncertain, especially if prior finite-local-ring work contains an implicit equivalent enumerator.

## References
1. M. Gerstenhaber, *On dominance and varieties of commuting matrices*, Ann. Math. 73 (1961), 324–348.
2. V. L. Popov, *Irregular and singular loci of commuting varieties*, arXiv:0801.3074, https://arxiv.org/abs/0801.3074.
3. B. A. Sethuraman and K. Šivic, *Jet schemes of the commuting matrix pairs scheme*, arXiv:0902.3467, https://arxiv.org/abs/0902.3467.
4. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, https://arxiv.org/abs/1001.0811.
5. U. B. Sharma, *Simultaneous similarity classes of commuting matrices over a finite field*, arXiv:1409.2698, https://arxiv.org/abs/1409.2698.
