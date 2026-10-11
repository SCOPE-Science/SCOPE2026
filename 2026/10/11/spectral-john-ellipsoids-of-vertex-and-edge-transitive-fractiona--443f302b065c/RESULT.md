# Spectral John ellipsoids of vertex-and-edge-transitive fractional matching polytopes

## Finding
Let \(G=(V,E)\) be a finite connected simple graph with \(n=|V|\), \(m=|E|\), and degree \(d\ge2\). Assume its automorphism group acts transitively **both on vertices and on edges**. Denote by \(B\in\{0,1\}^{n\times m}\) the unsigned vertex-edge incidence matrix, by \(A\) the adjacency matrix, and by \(K=BB^{\mathsf T}=dI_n+A\) the signless Laplacian. Let \(\lambda_1,\ldots,\lambda_n\ge0\) be the eigenvalues of \(K\), with multiplicity. Define
\[
V_G(t)=\frac1n\sum_{j=1}^{n}\frac{\lambda_j}{1+t\lambda_j/2}.
\]
There is exactly one \(t=t_G\in(0,1]\) solving
\[
\boxed{\frac{t(1+dt)}d V_G(t)=1.}
\]
For the full-dimensional fractional matching polytope
\[
F_G=\bigl\{x\in\mathbb R^E:x_e\ge0\ (e\in E),\ \sum_{e\ni v}x_e\le1\ (v\in V)\bigr\},
\]
its **unique** maximum-volume inscribed Euclidean ellipsoid is
\[
\boxed{\mathcal E_G=\{c+\Sigma^{1/2}y:\|y\|_2\le1\},\qquad
c=\frac{t}{1+dt}\mathbf1_m,\quad
\Sigma=\frac{t}{d(1+dt)}\bigl(I_m+\tfrac t2B^{\mathsf T}B\bigr)^{-1}.}
\]
Every one of the \(m+n\) defining facets is tangent to \(\mathcal E_G\), and the \(m+n\) contact points are distinct. With \(\eta=t/[d(1+dt)]\), the squared principal semiaxes are \(\eta/(1+t\lambda_j/2)\) for each **positive** eigenvalue \(\lambda_j\) of \(K\), together with \(\eta\) of multiplicity \(m-\operatorname{rank}(K)\). The exact volume is
\[
\boxed{\operatorname{vol}_m(\mathcal E_G)=\frac{\pi^{m/2}}{\Gamma(m/2+1)}\eta^{m/2}\prod_{j=1}^{n}(1+t\lambda_j/2)^{-1/2}.}
\]
Two explicit consequences distinguish this result from the complete-graph specialization. For the complete bipartite graph \(K_{d,d}\), \(d\ge2\),
\[
\boxed{t_{K_{d,d}}=\frac{d-2+\sqrt{d^2+12d-4}}{4d-2}.}
\]
For the cycles \(C_n\), as \(n\to\infty\), the scalar parameter converges to the golden-ratio value
\[
\boxed{\lim_{n\to\infty}t_{C_n}=\frac{1+\sqrt5}{4}.}
\]

## Assumptions and scope
All norms, eigenvalues, ellipsoid volumes, and matrix transposes refer to the standard Euclidean structure in edge coordinates \(\mathbb R^E\). The graph is simple, connected, and at least 2-regular; automorphisms must be transitive on both its vertices and edges. The method does not assert the displayed formula for arbitrary regular or merely vertex-transitive graphs. It applies, among others, to every cycle, complete graph, balanced complete bipartite graph, hypercube graph of dimension at least two, and the Petersen graph. Its ellipsoid has full dimension \(m\) because the defining inequalities admit strictly feasible positive edge vectors.

## Proof
**1. Unique spectral parameter.** The signless Laplacian \(K=BB^{\mathsf T}\) is positive semidefinite, has trace \(nd\), and has eigenvalues at most \(2d\). The continuous function
\[
\Phi(t)=\frac{t(1+dt)}{dn}\sum_j\frac{\lambda_j}{1+t\lambda_j/2}
\]
is strictly increasing for positive \(t\): each nonzero-eigenvalue summand is a positive constant times \(t(1+dt)/(1+t\lambda_j/2)\), whose derivative is positive. Moreover \(\Phi(0)=0\). Since \(\lambda_j\le2d\),
\[
V_G(1)\ge\frac{\operatorname{tr}K}{n(1+d)}=\frac d{1+d},
\]
so \(\Phi(1)\ge1\). This yields a unique root \(t\in(0,1]\).

**2. Two exact diagonal identities.** Set \(M=I_m+\frac t2 B^{\mathsf T}B\) and \(V=V_G(t)\). By vertex transitivity, every diagonal of \(BM^{-1}B^{\mathsf T}\) equals \(V\); this follows from \(BM^{-1}B^{\mathsf T}=K(I_n+tK/2)^{-1}\) and the trace formula. By edge transitivity, every diagonal of \(M^{-1}\) equals a common scalar \(L\). Taking traces of \(MM^{-1}=I_m\), and using \(2m=nd\), gives
\[
L=1-\frac td V.
\]
The root equation says \(V=d/[t(1+dt)]\), hence
\[
\boxed{L=\frac{dt}{1+dt},\qquad V=\frac d{t(1+dt)}.}
\]
Writing \(a=t/(1+dt)\) and \(\eta=t/[d(1+dt)]\), the proposed shape matrix \(\Sigma=\eta M^{-1}\) therefore satisfies
\[
\Sigma_{ee}=\eta L=a^2\quad(e\in E),\qquad
(B\Sigma B^{\mathsf T})_{vv}=\eta V=(1-da)^2\quad(v\in V).
\]

**3. Containment, facets, and contacts.** For any ellipsoid \(c+\Sigma^{1/2}B_2^m\), the minimum of coordinate \(e\) is \(c_e-\sqrt{\Sigma_{ee}}\); the maximum of the incident-edge sum at vertex \(v\) is \(b_v^{\mathsf T}c+\sqrt{b_v^{\mathsf T}\Sigma b_v}\), where \(b_v\) is row \(v\) of \(B\). The identities above make these minima equal zero and maxima equal one. Thus the proposed ellipsoid lies in \(F_G\) and touches all defining hyperplanes. These inequalities are genuine facets: for a coordinate hyperplane choose all other edge coordinates small and positive; for a vertex hyperplane set its \(d\) incident edge coordinates to \(1/d\) and all other edges sufficiently small and positive, giving strict slack at every other vertex because \(d\ge2\). Distinct facet normals cannot share a contact on a smooth strictly convex ellipsoid, so the contacts are distinct.

**4. Positive global John certificate.** Define unit contact normals after mapping the ellipsoid to the Euclidean unit ball:
\[
u_e=-\frac{\Sigma^{1/2}e_e}{a},\qquad
u_v=\frac{\Sigma^{1/2}b_v}{1-da}.
\]
Give every edge contact weight \(p=dt/(1+dt)\) and every vertex contact weight \(q=d/[2(1+dt)]\). Both are strictly positive. Since \(B^{\mathsf T}\mathbf1_n=2\mathbf1_m\), the first John identity follows from
\[
\sum_e p\nu_e+\sum_v q\nu_v=\Sigma^{1/2}\left(-\frac pa\mathbf1_m+\frac q{1-da}B^{\mathsf T}\mathbf1_n\right)=0.
\]
The second follows from the exact matrix identity
\[
\sum_e p\nu_e\nu_e^{\mathsf T}+\sum_v q\nu_v\nu_v^{\mathsf T}
=\Sigma^{1/2}\left(\frac p{a^2}I_m+\frac q{(1-da)^2}B^{\mathsf T}B\right)\Sigma^{1/2}
=\Sigma^{1/2}\Sigma^{-1}\Sigma^{1/2}=I_m.
\]
In the middle equality, \(p/a^2=\eta^{-1}\) and \(q/(1-da)^2=t/(2\eta)\). The two John identities together with containment certify that the unit ball is the unique maximum-volume inscribed ellipsoid of the normalized convex body; affine conjugation proves global optimality and uniqueness of \(\mathcal E_G\). In particular this proof excludes larger nonsymmetric or off-center competitors.

**5. Spectrum, volume, and explicit families.** The positive eigenvalues of \(B^{\mathsf T}B\) are precisely the positive eigenvalues of \(BB^{\mathsf T}=K\), including multiplicity. All other eigenvalues of \(B^{\mathsf T}B\) vanish. Applying the matrix function defining \(\Sigma\) gives the stated semiaxes and determinant, whence the Euclidean volume formula.

For \(G=K_{d,d}\), the signless Laplacian spectrum is \(2d\) once, \(d\) with multiplicity \(2d-2\), and zero once. Substitution into the spectral root equation reduces to
\[
(2d-1)t^2+(2-d)t-2=0.
\]
Its unique positive root is the displayed radical.

For the cycle \(G=C_n\), \(d=2\) and the signless-Laplacian eigenvalues are \(2+2\cos(2\pi j/n)\), with \(0\le j<n\). Their normalized sums converge, uniformly for \(t\in[0,1]\), to the corresponding continuous Fourier average. The standard integral
\[
\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{1+t+t\cos\theta}=\frac1{\sqrt{1+2t}}
\]
yields
\[
\lim_{n\to\infty}V_{C_n}(t)=\frac2t\left(1-\frac1{\sqrt{1+2t}}\right)
\]
for \(t>0\), with the continuous value \(2\) at \(t=0\). Every root lies in \((0,1]\). Uniform convergence and strict monotonicity imply convergence to the unique root of
\[
(1+2t)\left(1-\frac1{\sqrt{1+2t}}\right)=1.
\]
Putting \(z=\sqrt{1+2t}>1\) gives \(z^2-z=1\), hence \(z=(1+\sqrt5)/2\) and \(t=(1+\sqrt5)/4\).

## Verification
Execute `python verify.py` with Python 3.10 or later, NumPy and SciPy installed. The script builds 40 vertex-and-edge-transitive graphs (cycles, complete graphs, balanced complete bipartite graphs, hypercubes, Petersen, and octahedral), calculates the root independently from the signless-Laplacian spectrum, constructs the covariance matrix directly in edge space, and checks the two contact equations and both John identities. In the performed run all 40 cases passed, totaling 1,176 facet contacts (750 edge facets and 426 vertex facets). Numerical tolerance checks are not substitutes for the exact proof. The cycle limit is checked at a finite order only as a consistency test.

## Relationship to prior work
Blanchard, De Loera, and Louveaux, *On the Length of Monotone Paths in Polyhedra* (arXiv:2001.09575v1, 2020; SIAM Journal on Discrete Mathematics 2021), study monotone graph paths in matching and fractional matching polytopes rather than Euclidean maximum-volume inscribed ellipsoids. Sanità, *The diameter of the fractional matching polytope and its hardness implications* (arXiv:1806.03397v1, 2018), gives the defining relaxation and studies its combinatorial diameter. Barvinok and Blekherman, *Convex Geometry of Orbits* (arXiv:math/0312268v1, 2003), give general orbit-polar ellipsoid principles, but their one-orbit theorem does not itself specify the free center and the optimal relative weights of the two separate facet orbits here. Generic John contact theory is used rather than claimed as new. The complete-graph case is a specialization; the new graph-spectral classification covers cycles, complete bipartite graphs, hypercubes, and other vertex-and-edge-transitive examples with different spectral structures.

## Limitations
The result concerns the **fractional** matching relaxation, not the integral matching polytope on general nonbipartite graphs. Graphs that are not simultaneously vertex- and edge-transitive may have nonconstant facet-contact covariance entries and are not covered. The spectral scalar is uniquely characterized but need not have a radical expression for a general graph. The golden-ratio statement is a limit, not an exact equality for a finite cycle. The numerical verification is finite; priority relative to every possible earlier formulation, particularly via optimal design or general two-orbit polytope methods, has not been independently certified.

## References
1. M. Blanchard, J. A. De Loera, and Q. Louveaux, *On the Length of Monotone Paths in Polyhedra*, arXiv:2001.09575v1 (2020); SIAM J. Discrete Math. 35 (2021), 1746–1768, DOI:10.1137/20M1315646.
2. L. Sanità, *The diameter of the fractional matching polytope and its hardness implications*, arXiv:1806.03397v1 (2018).
3. S. Kafer, K. Pashkovich, and L. Sanità, *On the Circuit Diameter of Some Combinatorial Polytopes*, arXiv:1709.09642v1 (2017); SIAM J. Discrete Math. 33 (2019), 1–25.
4. A. Barvinok and G. Blekherman, *Convex Geometry of Orbits*, arXiv:math/0312268v1 (2003); MSRI Publications 52 (2005), 51–78.
5. F. John, *Extremum problems with inequalities as subsidiary conditions*, Studies and Essays Presented to R. Courant (1948), 187–204.
