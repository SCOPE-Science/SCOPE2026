# An additive Minkowski-asymmetry law for generalized Pitman–Stanley polytopes

## Finding
For integers \(n\ge1\), \(m\ge2\) and positive real numbers \(a_1,\ldots,a_n\), let \(A_i=\sum_{k=1}^i a_k\) and
\[
P=\{x\in\mathbb R_{\ge0}^{n\times m}:0\le X_{i,m}\le\cdots\le X_{i,1}\le A_i\ (1\le i\le n)\},\qquad X_{i,j}=\sum_{k=1}^i x_{kj}.
\]
This is the straight-shape generalized Pitman–Stanley polytope \(\operatorname{PS}_n^m(\mathbf a,\mathbf0)\). Set
\[
r_i=\frac{\sum_{k=1}^i A_k}{A_i},\qquad \rho=\max_{1\le i\le n}r_i,\qquad T=\{i:r_i=\rho\},\qquad L=\max T.
\]
Its exact Minkowski asymmetry, an explicit minimizing center, and the dimension of the complete minimizing-center set are
\[
\boxed{s(P)=m-1+\rho},\qquad
\boxed{c_{kj}=\frac{A_k+(m-j)a_k}{m+\rho}},\qquad
\boxed{\dim\operatorname{aff}\mathcal M(P)=nm-L-(m-1)|T|}.
\]
The complete minimizing-center set, not only its dimension, is
\[
\mathcal M(P)=\left\{\frac{y}{m+\rho}: y_{kj}\ge A_k,\quad Y_{i,j}-Y_{i,j+1}\ge A_i\ (j<m),\quad Y_{i,1}\le(m-1+\rho)A_i\right\},
\]
where \(Y_{i,j}=\sum_{k=1}^i y_{kj}\). All displayed inequalities run over \(1\le k,i\le n\) and valid column indices.

When every \(a_k=1\), one gets \(\rho=(n+1)/2\) and therefore
\[
s(P)=\frac{n+2m-1}{2},\qquad\dim\operatorname{aff}\mathcal M(P)=(n-1)(m-1).
\]
The value can be nonintegral: \(s(\operatorname{PS}_2^2((1,1),\mathbf0))=5/2\). At \(n=3,m=2\), the data \(\mathbf a=(1,1,4)\) and \(\mathbf a=(1,1,98)\) both give \(s(P)=5/2\) but yield center-set dimensions \(1\) and \(3\), respectively. The maximizing-prefix set, not merely the scalar asymmetry, controls the center geometry.

## Assumptions and scope
All entries \(a_k\) are strictly positive, including those defining the cumulative ceilings \(A_i\). The parameter \(m\) counts dominance-chain columns and is at least two. The polytope is full-dimensional in \(\mathbb R^{nm}\): sufficiently small positive constant entries make each nonnegativity, prefix-chain, and top-prefix inequality strict. Its affine geometry uses the original matrix coordinates. The minimization convention is
\[
s(P)=\min_{c\in\operatorname{int}P}\min\{s\ge1:-(P-c)\subseteq s(P-c)\}.
\]
Strict positivity is essential to the stated relative-interior witness and dimension formula. The nonzero-lower-bound/skew-shape generalization is not included.

## Proof
**1. Exactly sharp extremal right-hand sides.** Write the complete halfspace system as (i) \(-x_{kj}\le0\), (ii) \(X_{i,j+1}-X_{i,j}\le0\) for \(j<m\), and (iii) \(X_{i,1}\le A_i\). The minimum values of the corresponding left-hand linear forms over \(P\) are respectively \(-A_k\), \(-A_i\), and \(0\). Indeed, \(0\le x_{kj}\le X_{k,j}\le A_k\), while the difference between adjacent column prefixes has magnitude at most \(A_i\). Equality is realized by placing an amount \(A_k\) at matrix row \(k\) in the first \(j\) columns (and zero elsewhere), or an amount \(A_i\) at row \(i\) in the first \(j\) columns, respectively; the zero matrix realizes the remaining minimum. All these test matrices satisfy every prefix constraint because \(A_i\) increases with \(i\). Thus these are genuine support extrema, not merely estimates.

**2. Reflection feasibility.** For a general halfspace \(\ell(x)\le b\) having minimum \(h\) on \(P\), the condition \(c-(x-c)/s\in P\) for every \(x\in P\) is equivalent to \((s+1)\ell(c)\le sb+h\). Put \(y=(s+1)c\). Applying this identity to all the inequalities in step 1 yields exactly
\[
y_{kj}\ge A_k,\quad Y_{i,j}-Y_{i,j+1}\ge A_i\ (j<m),\quad Y_{i,1}\le sA_i.\tag{1}\]
The system is necessary and sufficient because the listed halfspaces define \(P\), whether or not any of them is redundant.

**3. Exact optimal scale and center.** From (1), for each \(i\),
\[
sA_i\ge Y_{i,1}\ge Y_{i,m}+(m-1)A_i\ge\sum_{k=1}^i A_k+(m-1)A_i.
\]
Hence \(s\ge m-1+\rho\). For \(s=m-1+\rho\) set \(y_{kj}=A_k+(m-j)a_k\). The column-prefix differences are exactly \(A_i\), the coordinate floors are satisfied, and
\[
Y_{i,1}=\sum_{k=1}^i A_k+(m-1)A_i\le sA_i.
\]
This attains the lower bound and establishes the center formula. The center is interior because each coordinate \(c_{kj}>0\), each adjacent-prefix gap is \(A_i/(s+1)>0\), and every top-prefix inequality has strictly positive slack at \(c\): \(X_{i,1}(c)\le sA_i/(s+1)<A_i\).

**4. All optimal centers and exact dimension.** System (1) at the sharp scale is the displayed description of \(\mathcal M(P)\). For every \(i\in T\), the three bounds in step 3 are equalities. Since each \(y_{k,m}\ge A_k\), the largest tight index \(L\) forces \(y_{k,m}=A_k\) for every \(k\le L\). Moreover, for every \(i\in T\) and \(j<m\), it forces \(Y_{i,j}-Y_{i,j+1}=A_i\). These \(L+(m-1)|T|\) affine equalities are independent: the invertible triangular coordinate change
\[
(y_{kj})\longleftrightarrow\bigl(u_k=y_{k,m},\ d_{i,j}=Y_{i,j}-Y_{i,j+1}\bigr)
\]
turns them into constraints fixing distinct coordinates.

To prove there are no further universal affine equalities, define \(h_i=0\) for \(i\in T\) and \(h_i=1\) otherwise, with \(h_0=0\). For sufficiently small \(\varepsilon>0\), prescribe
\[
u_k=A_k+\varepsilon\mathbf1_{\{k>L\}},\qquad d_{i,j}=A_i+\varepsilon h_i.
\]
Invert the triangular coordinate change to obtain \(y_{k,m}=u_k\) and
\[
y_{k,j}=u_k+\sum_{\ell=j}^{m-1}(d_{k,\ell}-d_{k-1,\ell}),\qquad d_{0,\ell}=0.
\]
For all sufficiently small positive \(\varepsilon\), every non-forced coordinate lower bound is strict: the unperturbed first \(m-1\) entries in row \(k\) exceed \(A_k\) by at least \(a_k>0\); for the last column the coordinates \(k>L\) gain \(\varepsilon\). The non-tight column gaps gain \(\varepsilon\), and the non-tight top-prefix upper bounds retain their original positive slack \(A_i(\rho-r_i)\). Every forced equality remains exact because a tight index is no greater than \(L\) and has \(h_i=0\). Thus this feasible point lies in the relative interior of the intersection of the forced affine equalities. Its dimension is exactly \(nm-L-(m-1)|T|\).

## Verification
Run the standalone Python 3 standard-library script `verify_ps.py` from the same package. It performs exact rational elimination and independently enumerates every vertex of ten small positive-parameter instances, then compares all sharp halfspace extrema, checks every reflected vertex against every defining inequality, and tests a relative-interior center witness. Recorded successful run: 10 parameter choices, 210 distinct vertices in total, and 2,376 reflected-vertex/halfspace comparisons. These finite cases verify the computations in those cases but do not constitute the proof for arbitrary dimensions or parameters; the preceding argument establishes the full theorem.

## Relationship to prior work
Dugan, Hegarty, Morales, and Raymond introduced and studied the generalized dominance-chain polytope and its flow/plane-partition interpretations (arXiv:2307.09925, first public 19 July 2023). The inspected primary text treats vertices, faces, generating functions, and flow realizations, rather than Minkowski asymmetry or optimal-center loci. Pitman and Stanley studied the original one-column family; this finding concerns the new multichain regime \(m\ge2\), and makes no priority claim for \(m=1\). Work on marked order polytopes and generalized permutahedra provides related combinatorial geometry, but a classification of their lattice structures or Minkowski-sum decompositions does not imply the scalar reflection-containment equation or center-dimension phase law established here. Publication-priority checks cannot rule out all equivalent formulations under other terminology.

## Limitations
The result assumes strictly positive ceiling increments and zero lower-bound vector; it does not settle arbitrary skew-shape input, zero increments, or all flow polytopes. The theorem concerns Minkowski asymmetry and its optimal centers, not Euclidean inradii, volumes, or lattice-point counts. Finite exact enumerations corroborate but are not a general-dimensional certificate. Independent literature-priority and independent scientific validation have not been performed.

## References
Dugan, W. T., Hegarty, M., Morales, A. H., and Raymond, A., *Generalized Pitman–Stanley polytope: vertices and faces*, arXiv:2307.09925, first submitted 2023-07-19; https://arxiv.org/abs/2307.09925 and https://arxiv.org/html/2307.09925v2.

Pitman, J., and Stanley, R., *A polytope related to empirical distributions, plane trees, parking functions, and the associahedron*, Discrete & Computational Geometry 27 (2002), 603–634; https://statistics.berkeley.edu/tech-reports/560.

Fang, X., Fourier, G., and Pegel, C., *The Minkowski property and reflexivity of marked poset polytopes*, arXiv:1807.03970. The phrase “Minkowski property” there concerns Minkowski addition, not the asymmetry invariant considered here.
