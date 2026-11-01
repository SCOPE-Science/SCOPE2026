# Sharp generic circular-view count for quadratic-bandlimited convex bodies

## Finding
For every integer \(n\ge 3\), the sharp number of generic planar projections needed to recognize a ball among convex bodies with support function of spherical-harmonic degree at most two is
\[
 m_n=\left\lceil\frac{n(n+1)-2}{4}\right\rceil.
\]
More precisely, there exist \(m_n\) two-dimensional linear subspaces of \(\mathbb R^n\), and a full-measure open dense set of such \(m_n\)-tuples, for which **all** projected bodies being Euclidean disks (their radii and centers need not agree) forces the original body to be a Euclidean ball. For any selection of fewer than \(m_n\) planes there exists a smooth strictly convex nonball, arbitrarily close to the unit ball, having disk projections onto every selected plane. The sharp budgets begin \(3,5,7,10,14\) for dimensions \(3,4,5,6,7\).

## Assumptions and scope
A convex body means a compact convex subset of \(\mathbb R^n\) with nonempty interior. Its support function is \(h_K(u)=\max_{x\in K}\langle x,u\rangle\) for \(u\in S^{n-1}\). The hypothesis of degree at most two means exactly
\[
 h_K(u)=R+\langle a,u\rangle+u^{\mathsf T}Qu,
 \quad Q=Q^{\mathsf T},\quad \operatorname{tr}Q=0,
\]
with \(R\in\mathbb R\), \(a\in\mathbb R^n\) and the stated function an actual support function. The trace normalization is unique; it absorbs any scalar quadratic term into \(R\). Let \(\mathcal S_0^n\) be the real vector space of trace-free symmetric matrices, of dimension \(D=n(n+1)/2-1\). A plane \(P\in\operatorname{Gr}(2,n)\) has a linear two-component measurement \(T_P:\mathcal S_0^n\to\mathcal S_0(P)\) equal to the trace-free part of its quadratic-form restriction (computed in any orthonormal basis of \(P\)). All genericity statements refer to the product Haar measure and usual real-analytic topology on the Grassmannian.

## Proof
**Disk criterion.** The support function of the orthogonal projection onto \(P\) is \(h_K\) restricted to \(S^{n-1}\cap P\). For an orthonormal frame \(e,f\) of \(P\), put \(u(\theta)=e\cos\theta+f\sin\theta\). Then \(u(\theta)^{\mathsf T}Qu(\theta)\) has a constant term and exactly the angular modes of frequency two, with coefficients \((e^{\mathsf T}Qe-f^{\mathsf T}Qf)/2\) and \(e^{\mathsf T}Qf\). Translation contributes only first harmonics. Consequently the projected convex body is a disk if and only if \(T_P(Q)=0\). A disk may have a center and radius depending on \(P\); neither affects this test. Each \(T_P\) has codomain dimension two.

**Two-dimensional separation lemma.** Let \(A,B\in\mathcal S_0^n\) be linearly independent. There is a plane \(P\) for which \(T_P(A)\) and \(T_P(B)\) are linearly independent. Suppose the contrary: these two images are dependent for every plane. Diagonalize the nonzero nonscalar matrix \(A\). If \(e\) is any unit eigenvector of \(A\) with eigenvalue \(\lambda\), and \(v\perp e\) is a unit vector for which \(v^{\mathsf T}Av\ne\lambda\), the compression of \(A\) to \(\operatorname{span}\{e,v\}\) has zero off-diagonal entry and unequal diagonal entries. Dependence of the two trace-free compressions forces \(e^{\mathsf T}Bv=0\). Because \(A\) is nonscalar, the condition \(v^{\mathsf T}Av\ne\lambda\) defines a dense open subset of the unit sphere in \(e^\perp\). Continuity therefore gives \(e^{\mathsf T}Bv=0\) for every \(v\perp e\). Thus **every** eigenvector of \(A\) is an eigenvector of \(B\). On every repeated-eigenvalue space of \(A\), this forces \(B\) to act as a scalar, so an orthonormal basis simultaneously diagonalizes both and \(B\)'s diagonal values are constant on each eigenvalue class of \(A\).

Write their diagonal entries as \((a_i)\) and \((b_i)\). If every three points \((a_i,b_i)\) were collinear, \(B=\alpha A+\beta I\) for some scalars. Trace-freeness then gives \(\beta=0\), contradicting independence. Hence there are indices \(i,j,k\) with noncollinear triples. Choose orthonormal vectors
\[
 u=(e_i+e_j)/\sqrt2,\qquad v=(e_i-e_j+2e_k)/\sqrt6.
\]
For any diagonal matrix \(C\) with diagonal entries \((c_l)\), the two trace-free compression coordinates, taken as \((u^{\mathsf T}Cu-v^{\mathsf T}Cv,2u^{\mathsf T}Cv)\), are
\[
 \left(\frac{c_i+c_j-2c_k}{3},\frac{c_i-c_j}{\sqrt3}\right).
\]
The determinant of these two coordinates for \(A,B\) is nonzero exactly when the three points \((a_i,b_i),(a_j,b_j),(a_k,b_k)\) are noncollinear. This is a contradiction, proving the lemma. The case of a single nonzero \(A\) is immediate from two eigenvectors with distinct eigenvalues: some plane satisfies \(T_P(A)\ne0\).

**Exact construction.** Start with \(W_0=\mathcal S_0^n\), of dimension \(D\). As long as the kernel space \(W_j\) has dimension at least two, select independent \(A,B\in W_j\) and use the separation lemma to choose a plane whose restricted measurement has rank exactly two on \(W_j\); define \(W_{j+1}=W_j\cap\ker T_{P_j}\). Its dimension is two less than that of \(W_j\). If the remaining space has dimension one, choose a plane detecting a nonzero element and reduce its dimension to zero. Thus \(\lceil D/2\rceil\) planes yield a combined map \(Q\mapsto(T_{P_j}(Q))_j\) of rank \(D\). Every relevant maximal-rank minor depends real-analytically on the planes. A minor nonzero at the constructed tuple is not identically zero on the connected Grassmannian product, so its nonvanishing locus is open, dense, and of full Haar measure. For each tuple there, all projected bodies being disks forces \(Q=0\) and hence \(h_K(u)=R+\langle a,u\rangle\), the support function of a translated Euclidean ball.

**Optimality for every prescribed shorter collection.** Given fewer than \(\lceil D/2\rceil\) planes, their combined measurement has rank at most twice the plane count, hence a nonzero tracefree symmetric \(Q\) lies in its kernel. For small nonzero \(\varepsilon\), let \(h_\varepsilon(u)=1+\varepsilon u^{\mathsf T}Qu\). The standard support-function curvature matrix on the sphere is
\[
 \nabla_S^2h_\varepsilon+h_\varepsilon I
 =I+\varepsilon\left(2Q|_{u^\perp}-(u^{\mathsf T}Qu)I\right).
\]
Every eigenvalue is at least \(1-3|\varepsilon|\|Q\|_{\mathrm{op}}>0\) whenever \(0<|\varepsilon|<1/(3\|Q\|_{\mathrm{op}})\). It is therefore the support of a smooth strictly convex body. Because \(Q\ne0\) is tracefree, the support has a nontrivial degree-two harmonic and the body is not a ball. Nevertheless, \(T_{P_j}(Q)=0\) for every measured plane, so every corresponding projected body is a disk. Moreover \(h_\varepsilon\to1\) uniformly as \(\varepsilon\to0\), proving arbitrary Hausdorff proximity to the unit ball. This establishes sharpness.

## Verification
A standalone Python checker, `verify_quadratic_views.py`, constructs rational (integer-coordinate) spanning pairs of planes, writes the two corresponding compression constraints for every basis matrix of \(\mathcal S_0^n\), and computes exact modular ranks modulo the prime \(1000003\). The supplied deterministic tests verify full rank in each dimension \(3\le n\le12\); the respective rank values are \(5,9,14,20,27,35,44,54,65,77\), with plane counts \(3,5,7,10,14,18,22,27,33,39\). Full modular rank certifies rational full rank in those finite cases. This does not establish the statement for all dimensions; that conclusion rests on the separation lemma and induction above. The quadratic compression determinant and strict-curvature bound have also been checked algebraically.

## Relationship to prior work
Myroshnychenko, Ryabogin and Saroglou, *On convex bodies with rotationally symmetric planar projections* (first publicly posted September 23, 2026, arXiv:2609.27192), prove that requiring the relevant rotational symmetry on **every** two-plane projection forces ball rigidity in arbitrary dimensions, with a cubic exception at order three. Their paper explicitly identifies projection support functions with great-circle restrictions and the roles of Fourier modes. It does not give the number of **finite** views sufficient or necessary for the degree-two class. Kiderlen's *Determination of a Convex Body from Minkowski Sums of its Projections* (2004) studies projections averaged over whole Grassmannians, not tests that finitely many individual projected shapes are disks. Earlier finite circular-shadow work in dimension three and degree three identifies a cubic residual after three special coordinate views and a resolving fourth diagonal view; it does not settle the present sharp all-dimensional quadratic measurement count.

## Limitations
The theorem concerns the finite-dimensional class of bodies with support-harmonic degree at most two. For arbitrary smooth convex bodies, finitely many prescribed projections cannot in general force spherical rigidity. The theorem proves generic sufficiency and unconditional minimality, not that every tuple of \(m_n\) planes works. It asserts exact disks, not noise-robust recovery bounds. The originality assessment is relative to accessible indexed and inspected literature; a historical result in unindexed finite-rank tomography could provide an equivalent algebraic formulation. No independent mathematical audit is claimed.

## References
1. S. Myroshnychenko, D. Ryabogin, C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192v1 (first posted 2026-09-23), https://arxiv.org/abs/2609.27192.
2. M. Kiderlen, *Determination of a Convex Body from Minkowski Sums of its Projections*, Journal of the London Mathematical Society 70 (2004), 529–544, DOI:10.1112/S0024610704005551.
3. R. J. Gardner, *Geometric Tomography*, second edition, Cambridge University Press (2006), standard background on support functions and projection geometry.
