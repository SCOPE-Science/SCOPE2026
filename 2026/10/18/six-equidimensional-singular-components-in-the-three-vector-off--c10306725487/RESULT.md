# Six equidimensional singular components in the three-vector off-diagonal Gram zero fiber

## Finding
For every integer \(M\geq3\), consider the complex affine variety
\[
X_M=\{(v_1,v_2,v_3)\in(\mathbb C^M)^3:\langle v_1,v_2\rangle=\langle v_1,v_3\rangle=\langle v_2,v_3\rangle=0\},
\]
with the standard nondegenerate symmetric bilinear form \(\langle u,v\rangle=\sum_{a=1}^M u_av_a\). The variety \(X_M\) is an integral complete intersection of dimension \(3M-3\). Its **reduced singular locus** has exactly six irreducible components, all of dimension \(M\):

* Three linear spaces \(L_{ij}=\{v_i=v_j=0\}\), for \(1\leq i<j\leq3\), each of degree \(1\).
* Three isotropic rank-one loci
\[
Q_i=\{v_i=0,\ \operatorname{rank}[v_j\ v_k]\leq1,\ \langle v_j,v_j\rangle=\langle v_k,v_k\rangle=\langle v_j,v_k\rangle=0\},
\]
where \(\{i,j,k\}=\{1,2,3\}\), each of degree \(2(M-1)\).

The projectivization of each \(Q_i\) is the Segre variety \(\mathbb P^1\times Q^{M-2}\) embedded by \(\mathcal O(1,1)\), where \(Q^{M-2}\subset\mathbb P^{M-1}\) is the smooth isotropic quadric. In particular, the singular locus is pure-dimensional and
\[
\boxed{\deg(\operatorname{Sing}(X_M)_{\mathrm{red}})=6M-3.}
\]
At a general closed point of **each** of the six components, the completed analytic germ is a product of an \(M\)-dimensional smooth factor with an ordinary quadratic hypersurface singularity in \(2M-2\) variables. More precisely, there is a completed-local-ring isomorphism
\[
\widehat{\mathcal O}_{X_M,p}\cong
\mathbb C[[t_1,\ldots,t_M,z_1,\ldots,z_{2M-2}]]
\big/\left(\sum_{a=1}^{2M-2}z_a^2\right)
\]
for all points in a dense Zariski-open subset of each component. No assertion about the local normal form at intersections of components is intended.

## Assumptions and scope
The base field is \(\mathbb C\), and \(M\) is an arbitrary integer at least \(3\). Degree means the ordinary projective degree of the affine cone in \(\mathbb A^{3M}\), equivalently the degree of its projectivization in \(\mathbb P^{3M-1}\). The singular locus is taken with its reduced scheme structure; no claim is made that the full Jacobian singular scheme is reduced. The three quadratic equations generate the scheme-theoretic zero-fiber ideal.

The integrality and complete-intersection assertion follows directly from Xie's sharp FRS theorem applied with three vectors: its threshold is \(M>2\). The singular-component classification and transverse normal forms below are proved directly and do not infer them merely from rational singularities.

## Proof
**1. Jacobian criterion and the rank-one restriction.** Let \(V=[v_1\ v_2\ v_3]\) denote the \(M\)-by-\(3\) matrix of columns. A linear relation among the differentials of the three defining quadrics is specified by scalars \(a,b,c\) and the symmetric hollow matrix
\[
\Lambda=\begin{pmatrix}0&a&b\\a&0&c\\b&c&0\end{pmatrix}.
\]
The relation vanishes precisely if \(V\Lambda=0\). Every nonzero such \(\Lambda\) has rank at least two: a rank-one symmetric matrix in characteristic zero has the form \(\lambda uu^{\mathsf T}\), and its zero diagonal then forces \(u=0\). Thus a point with \(\operatorname{rank}(V)\geq2\) is smooth because \(\dim\ker V\leq1\) cannot contain the image of a rank-at-least-two matrix \(\Lambda\).

For a nonzero rank-one matrix write \(V=w(c_1,c_2,c_3)\), with \(w\ne0\). The coefficient matrix for \(\Lambda(c_1,c_2,c_3)^{\mathsf T}=0\), in the unknowns \((a,b,c)\), is
\[
\begin{pmatrix}c_2&c_3&0\\c_1&0&c_3\\0&c_1&c_2\end{pmatrix};
\qquad \det=-2c_1c_2c_3.
\]
Consequently, this rank-one point is singular if and only if at least one \(c_i\) vanishes. When exactly one coefficient is nonzero, the point belongs to a linear \(L_{ij}\). When exactly two coefficients are nonzero, the off-diagonal equations force \(\langle w,w\rangle=0\), and the point belongs to the corresponding isotropic \(Q_i\). The zero matrix belongs to all six loci. Conversely, every point on these loci is singular by the same matrix criterion. This proves the claimed equality of underlying closed sets.

**2. Irreducible components and degrees.** Each \(L_{ij}\) is an \(M\)-dimensional affine linear space. The projective rank-one locus in the two nonzero column blocks has Segre parametrization \(([a:b],[w])\mapsto[aw:bw]\), restricted by the single nondegenerate quadric \(\langle w,w\rangle=0\). For \(M\geq3\), the quadric \(Q^{M-2}\) is smooth and irreducible. Therefore \(Q_i\) is an irreducible affine cone of dimension \(M\), with projectivization \(\mathbb P^1\times Q^{M-2}\). Its hyperplane class is the sum of the two natural hyperplane classes. Since \(\dim(\mathbb P^1\times Q^{M-2})=M-1\), its degree is
\[
\int_{\mathbb P^1\times Q^{M-2}}(H_1+H_2)^{M-1}
=(M-1)\int_{\mathbb P^1}H_1\int_{Q^{M-2}}H_2^{M-2}=2(M-1).
\]
All six components are distinct (a general point of one fails the defining properties of each of the other five). As they all have dimension \(M\), none contains another, and the degree of their reduced union is the sum of their degrees: \(3+3\cdot2(M-1)=6M-3\).

**3. Transverse normal form on a linear component.** It suffices by symmetry to consider \(L_{12}\) at a point \((0,0,w)\) with \(\langle w,w\rangle\ne0\). Near that point the two equations \(\langle v_1,v_3\rangle=\langle v_2,v_3\rangle=0\) solve uniquely for the two components of \(v_1,v_2\) parallel to \(v_3\). The remaining defining equation is the nondegenerate pairing \(\langle v_1,v_2\rangle\) on the two copies of \(v_3^\perp\), each of dimension \(M-1\). Over \(\mathbb C\) this quadratic form is equivalent to a sum of \(2M-2\) squares. The \(M\) varying coordinates of \(v_3\) are smooth parameters. This gives the displayed completed local normal form on a dense open subset of \(L_{12}\).

**4. Transverse normal form on an isotropic rank-one component.** By symmetry consider a point \((0,w,cw)\) in \(Q_1\), with \(w\ne0\), \(\langle w,w\rangle=0\), and \(c\ne0\). Choose a linear functional \(\ell\) with \(\ell(w)\ne0\). In a neighborhood write \(u=v_1\), \(w'=v_2\), and \(v_3=c'w'+y\), where \(c'=\ell(v_3)/\ell(w')\) and \(y\in\ker\ell\). The three equations are equivalent to
\[
\langle u,w'\rangle=0,\qquad
c'\langle w',w'\rangle+\langle w',y\rangle=0,\qquad
\langle u,y\rangle=0.
\]
The first two have independent differentials at the specified point: the first has nonzero differential in \(u\); the second has nonzero differential in \(w'\), since \(c\ne0\) and \(w\ne0\). By the formal implicit-function theorem they eliminate one coordinate of \(u\) and one coordinate of \(w'\). The remaining equation has vanishing first derivatives and normal Hessian equal to the pairing
\[
(w^\perp)\times\ker\ell\longrightarrow\mathbb C,
\qquad (u,y)\longmapsto\langle u,y\rangle.
\]
This pairing is nondegenerate: its annihilator on the second side would lie in \((w^\perp)^\perp=\mathbb Cw\), whose intersection with \(\ker\ell\) is zero; both spaces have dimension \(M-1\). Equivalently, the quadratic normal part has rank \(2M-2\), and the local critical locus has the required smooth \(M\)-dimensional tangent directions. The formal Morse lemma with parameters yields the same nondegenerate quadratic hypersurface, times \(M\) smooth parameters. The set with \(w\ne0\), \(c\ne0\) and \(\ell(w)\ne0\) is dense in \(Q_1\). This completes the proof.

## Verification
The companion standalone \(\texttt{verify.py}\) uses exact symbolic arithmetic. For \(M=3,4,5,6\) and explicit generic points of both component types, it verifies that all three defining quadrics vanish, that their Jacobian has rank \(2\), and that the Hessian of the dependent equation restricted to the Jacobian tangent space has rank exactly \(2M-2\). It also checks both determinant identities and the component degree arithmetic. Executing the packaged script with Python and SymPy returned \(\texttt{VERIFY\_OK}\). These finite checks are independent numerical corroboration, not a proof for all \(M\); the universal argument is Steps 1–4.

## Relationship to prior work
Xie's *Sharp FRS and singularity thresholds for off-diagonal Gram maps* (arXiv:2610.02585v1, submitted 1 October 2026), Theorem 1.1, identifies the FRS/rational-singularity threshold and proves integrality of fibers. For three vectors the threshold is precisely \(M\geq3\); the inspected paper does not give the six components, their degrees, or their generic completed-local types. Casabella and Sammartano's *The variety of orthogonal frames* (arXiv:2512.25058v1), especially Sections 6–7, proves general component and smoothness criteria, and analyzes the three-vector four-dimensional case for factoriality. Its inspected statements do not identify this exact singular-locus decomposition or the all-dimension degree and transverse node formulas. Conca and Welker's *Lovász–Saks–Schrijver ideals and coordinate sections of determinantal varieties* (arXiv:1801.07916) supplies earlier structural background on orthogonality ideals. General Jacobian and Segre-degree tools underlie the proof, but the specific six-stratum geometry is a specialization requiring its own rank-one analysis.

## Limitations
This theorem classifies the reduced singular locus, not the full possibly nonreduced Jacobian singular scheme. The ordinary quadratic normal form holds on dense open subsets of the six components, not at their intersections or at the cone vertex. No assertion is made about global resolutions, monodromy, or higher numbers of vectors. A broader unindexed singular-stratification result might imply the formulas; the literature comparison is not a proof of absolute priority. Independent mathematical review has not been performed.

## References
1. Y. Xie, *Sharp FRS and singularity thresholds for off-diagonal Gram maps*, arXiv:2610.02585v1 (1 October 2026), https://arxiv.org/html/2610.02585v1.
2. L. Casabella and A. Sammartano, *The variety of orthogonal frames*, arXiv:2512.25058v1 (31 December 2025), https://arxiv.org/abs/2512.25058.
3. A. Conca and V. Welker, *Lovász–Saks–Schrijver ideals and coordinate sections of determinantal varieties*, arXiv:1801.07916, https://arxiv.org/abs/1801.07916.
