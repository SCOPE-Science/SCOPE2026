# The symmetric Burkhardt model in characteristic three is a cone over a 15-nodal K3 quartic

## Finding
Let \(k\) be an algebraically closed field of characteristic \(3\), and let \(e_j\) denote the elementary symmetric polynomial of degree \(j\) in six coordinates. Consider the **literal reduction** of the integral symmetric quartic model
\[
B=\{e_1(x_1,\ldots,x_6)=e_4(x_1,\ldots,x_6)=0\}\subset\mathbf P^5_k.
\]
This threefold is the projective cone with vertex \(V=[1:1:1:1:1:1]\) over the quartic surface
\[
S=\left\{\sum_{i=1}^{5}x_i=0,\quad e_4(x_1,\ldots,x_5)=0\right\}\subset\mathbf P^4_k.
\]
The ambient hyperplane \(\sum_{i=1}^{5}x_i=0\) is isomorphic to \(\mathbf P^3_k\).
The surface \(S\) is geometrically integral and normal, with exactly \(15\) ordinary double points, all defined over \(\mathbf F_3\). They are indexed by unordered pairs \(\{i,j\}\subset\{1,\ldots,6\}\): on the quotient \(\{e_1=0\}/k(1,\ldots,1)\), each is represented by \([\varepsilon_i-\varepsilon_j]\), where \(e_i\) here denotes the \(i\)-th **coordinate basis vector** (not the symmetric polynomial). The minimal resolution of \(S\) is a K3 surface and its Picard number is at least \(16\).

The **reduced** singular locus of \(B\) is exactly the union of the \(15\) pairwise distinct projective lines
\[
L_{ij}=\mathbf P\bigl(k(1,\ldots,1)+k(\varepsilon_i-\varepsilon_j)\bigr),\qquad 1\le i<j\le6,
\]
where \(\varepsilon_i\) are the coordinate basis vectors. All lines meet at \(V\); transverse to each line away from \(V\) the singularity is an ordinary double point, while the cone vertex has multiplicity \(4\). Over \(\mathbf F_3\),
\[
\#S(\mathbf F_3)=25,\qquad \#B(\mathbf F_3)=76.
\]
For every \(q=3^m\), \(m\ge1\), the cone gives the exact relation \(\#B(\mathbf F_q)=1+q\#S(\mathbf F_q)\).

## Assumptions and scope
All geometric assertions are over an algebraic closure of \(\mathbf F_3\). The base variety \(S\) is the hyperplane section obtained by choosing the linear complement \(x_6=0\) to the diagonal vector; the stated projective equivalence is over \(\mathbf F_3\). The object here is the literal integral **six-coordinate symmetric model** in characteristic \(3\). It is *not* the termwise reduction of a different five-coordinate equation whose equivalence to this symmetric model requires inverting \(3\). Singular-locus assertions concern geometric support, not an asserted scheme-theoretic primary decomposition of the Jacobian ideal.

## Proof
**(1) Cone identity.** Set \(v=(1,\ldots,1)\). The elementary-symmetric translation formula in six variables is
\[
e_4(x+tv)=e_4(x)+3te_3(x)+6t^2e_2(x)+10t^3e_1(x)+15t^4.
\]
In characteristic \(3\) this simplifies to \(e_4(x+tv)=e_4(x)+t^3e_1(x)\). Also \(e_1(x+tv)=e_1(x)+6t=e_1(x)\). Hence \(e_4\) is constant along the diagonal direction on the hyperplane \(H=\{e_1=0\}\). Since \(v\in H\), the direct sum \(H=kv\oplus\{e_1=x_6=0\}\) gives the claimed homogeneous projective cone over \(S\).

**(2) All singular points.** The constrained hypersurface in \(\mathbf P(H)\) is singular at a nonzero \(x\in H\) precisely when the six partial derivatives of \(e_4\) have the same value. The identity
\[
\frac{\partial e_4}{\partial x_i}=e_3-x_i e_2+x_i^2e_1-x_i^3
\]
shows, after translating to \(x_6=0\) and using \(e_1=0\), that singularity is equivalent to \(x_i^3+e_2(x)x_i=0\) for every \(i\). If \(e_2(x)=0\), the field property gives \(x=0\), so at a nonvertex singular point \(e_2\ne0\). Choose \(r\ne0\) with \(r^2=-e_2\). Every coordinate is then one of \(0,r,-r\).

Let \(n_+\) and \(n_-\) be the multiplicities of \(r\) and \(-r\), and let \(n=n_++n_-\le5\) because \(x_6=0\). The equations \(e_1=0\) and \(e_2=-(1/2)\sum x_i^2\) give
\[
n_+-n_-\equiv0\pmod3,\qquad n\equiv2\pmod3.
\]
Thus \(n=2\) or \(n=5\). For \(n=2\) one has \((n_+,n_-)=(1,1)\), yielding a vector \(r(\varepsilon_i-\varepsilon_j)\). For \(n=5\), the possibilities \((4,1)\) or \((1,4)\) become such a vector by translating all six coordinates by \(\mp r\). Therefore every singular point is on one of the \(15\) proposed lines. Conversely these lines lie in \(B\), and the derivative condition holds along them by the translation identity. They are distinct because their images in \(H/kv\) are distinct projective points, as seen explicitly in the section \(x_6=0\). The vertex itself is singular since the cone equation has degree \(4\).

**(3) Node classification.** The fifteen points of \(S\) split into two orbits under permutations of its five displayed coordinates: ten represented by \([1:-1:0:0:0]\) and five by \([1:1:1:1:-1]\). On the affine chart \(x_1=1\), put \(x_2=a+u,\ x_3=b+v,\ x_4=c+w,\ x_5=-1-x_2-x_3-x_4\). The quadratic terms of the local quartic at the two representatives are respectively
\[
Q_{10}=uv+uw+v^2+vw+w^2,\qquad Q_5=-uv-uw-vw.
\]
Their Hessian determinants are both \(1\) in \(\mathbf F_3\), so each singularity has nondegenerate quadratic tangent cone, hence is an ordinary double point of type \(A_1\). This also proves that \(S\) is reduced and has isolated singularities. A reducible projective surface in \(\mathbf P^3\) has component intersections of positive dimension, which would be singular; hence \(S\) is geometrically integral. Being a hypersurface with only isolated singularities, it is normal by Serre's criterion.

**(4) K3 resolution and Picard bound.** Rational double points are crepant and rational. Adjunction on the quartic surface yields trivial dualizing sheaf, and the hypersurface exact sequence \(0\to\mathcal O_{\mathbf P^3}(-4)\to\mathcal O_{\mathbf P^3}\to\mathcal O_S\to0\) yields \(H^1(S,\mathcal O_S)=0\). Both properties pass to the minimal resolution; it is a smooth K3 surface. Its fifteen exceptional disjoint \((-2)\)-curves are linearly independent, and the pullback of a hyperplane class is nonzero and orthogonal to all exceptional curves with self-intersection \(4\), giving Picard number at least \(16\).

**(5) Threefold transverse type, vertex, and counts.** Locally away from the vertex the projective cone is a product of an affine-line direction with a chart of \(S\); therefore each singular line has transverse \(A_1\) type. At the vertex, in affine cone coordinates the equation is a nonzero homogeneous quartic, so the Hilbert–Samuel multiplicity is \(4\). For a field \(\mathbf F_q\), projection of the cone away from the vertex to \(S\) has an affine-line fiber of \(q\) points, yielding \(\#B(\mathbf F_q)=1+q\#S(\mathbf F_q)\).

## Verification
Run `python3 verify.py` in the same directory. It uses Python's standard library only and carries out exact \(\mathbf F_3\) projective enumeration, checking \(25\) base-surface points, \(15\) geometric node representatives already rational over \(\mathbf F_3\), \(76\) threefold points, \(46\) singular rational points on the predicted fifteen lines, the pair-orbit Hessian determinants, the translation identity at every \(\mathbf F_3\)-point, and the cone count identity. Its expected final line is `VERIFY_OK`. The exhaustive \(\mathbf F_3\) calculation does not prove the statement over algebraic closures; that follows from the root classification in step (2).

## Relationship to prior work
Bruin–Nasserden (2017, arXiv:1705.09006) study the Burkhardt quartic and its arithmetic over characteristics **different from three**. Bruin–Filatov (2022, arXiv:2207.04393) expressly display the symmetric model \(e_1=e_4=0\) and study twists away from characteristics \(2,3,5\). Their characteristic-zero analysis of fifteen rational singular points of one twist should not be confused with the present characteristic-three **positive-dimensional** singular locus. Dolgachev (2019, arXiv:1906.12295) studies the broad geometry of fifteen-nodal quartic surfaces, primarily in characteristic zero and typically excluding three. Those general facts do not identify the particular characteristic-three special fiber as a fifteen-nodal cone. The novelty claim concerns the complete geometry and explicit singular-line configuration of this **particular integral model's** reduction, not the discovery of fifteen-nodal quartics or the classical Burkhardt quartic itself.

## Limitations
The statements do not describe the reduction of every birationally or projectively equivalent model over characteristic zero, do not assert a flat simultaneous resolution, and do not give the zeta polynomial of the K3 surface. Exhaustive finite-field verification was performed only over \(\mathbf F_3\), not for all extensions. Literature overlap is possible in older or unindexed treatments of this exact reduction; no independent external audit has been performed.

## References
1. N. Bruin and B. Nasserden, *Arithmetic aspects of the Burkhardt quartic threefold* (first public 2017-05-25), arXiv:1705.09006, https://arxiv.org/abs/1705.09006.
2. N. Bruin and E. Filatov, *Twists of the Burkhardt quartic threefold* (first public 2022-07-10), arXiv:2207.04393, https://arxiv.org/abs/2207.04393.
3. I. Dolgachev, *15-nodal quartic surfaces. Part I: Quintic del Pezzo surfaces and congruences of lines in projective 3-space* (2019), arXiv:1906.12295, https://arxiv.org/abs/1906.12295.
4. A. J. de Jong, N. I. Shepherd-Barron and A. Van de Ven, *On the Burkhardt quartic* (1990), historical background; the complete primary text was not accessible during comparison, so no negative-coverage assertion is made about it.
