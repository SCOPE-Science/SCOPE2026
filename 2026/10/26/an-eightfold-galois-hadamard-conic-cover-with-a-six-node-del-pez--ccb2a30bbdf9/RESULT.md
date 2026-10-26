# An eightfold Galois Hadamard-conic cover with a six-node del Pezzo quotient

## Finding
Let \(k\) be algebraically closed of characteristic zero, and let \(C=V(x_0^2+x_1^2+x_2^2)\subset\mathbb P^2_k\). Coordinatewise multiplication defines an everywhere-defined finite morphism
\[
\mu:C\times C\longrightarrow\mathbb P^2,\qquad (x,y)\longmapsto[x_0y_0:x_1y_1:x_2y_2].
\]
The morphism has degree \(8\), and its extension of function fields is Galois with group \((\mathbb Z/2\mathbb Z)^3\). Its reduced branch divisor is the union of the four lines
\[
L_{\epsilon}:\quad z_0+\epsilon_1 z_1+\epsilon_2 z_2=0,\qquad (\epsilon_1,\epsilon_2)\in\{\pm1\}^2,
\]
which have no triple concurrence. Each line has generic ramification index \(2\). The ramification divisor on \(C\times C\) consists precisely of four graphs of coordinate-sign involutions, each with coefficient one.

Let \(V\cong(\mathbb Z/2\mathbb Z)^2\) act by simultaneous coordinate-sign changes on the two factors. The intermediate quotient \(Y=(C\times C)/V\) is the normal degree-two cover of \(\mathbb P^2\) with weighted-projective equation
\[
w^2=(z_0+z_1+z_2)(z_0+z_1-z_2)(z_0-z_1+z_2)(z_0-z_1-z_2),
\]
where the \(z_i\) have weight \(1\) and \(w\) has weight \(2\). It has precisely six \(A_1\) singularities and no others. Its anticanonical class is ample with \(K_Y^2=2\); the minimal resolution is a weak del Pezzo surface of degree \(2\), with six exceptional \((-2)\)-curves. The factor-swap involution induces the residual double covering \(Y\to\mathbb P^2\).

## Assumptions and scope
All schemes and morphisms are over an algebraically closed field of characteristic \(0\). The target projective coordinates are \([z_0:z_1:z_2]\), distinct from the source coordinates on each conic. The intermediate quotient is the geometric finite-group quotient, not a smooth resolution. The claim concerns the specific nonsingular diagonal conic; any diagonal conic with three nonzero coefficients reduces to it by rescaling source and target coordinates. No assertion is made in characteristic \(2\).

## Proof
**(1) The map is finite and degree eight.** A point of \(C\) cannot have fewer than two nonzero coordinates, because a coordinate point does not satisfy its equation. Any two subsets of at least two among three indices intersect; thus not all coordinate products vanish, and \(\mu\) is everywhere defined. Under \(C\simeq\mathbb P^1\), \(\mathcal O_C(1)\simeq\mathcal O_{\mathbb P^1}(2)\), hence \(\mu^*\mathcal O_{\mathbb P^2}(1)=\mathcal O_{\mathbb P^1\times\mathbb P^1}(2,2)\). It is ample, so no curve can be contracted. Properness gives finite image, which has dimension two, hence is the whole \(\mathbb P^2\). Intersection theory gives \(\deg\mu=(2,2)^2=2\cdot2\cdot2=8\).

**(2) The complete deck group.** Projective coordinate-sign changes preserving \(C\) form \(V=\{\operatorname{diag}(\epsilon_0,\epsilon_1,\epsilon_2)\}/\{\pm I\}\simeq(\mathbb Z/2\mathbb Z)^2\). Each \(\epsilon\in V\) acts on the product by \((x,y)\mapsto(\epsilon x,\epsilon y)\); the factor exchange \(\tau(x,y)=(y,x)\) commutes with these changes. All eight elements of \(V\times\langle\tau\rangle\) act faithfully and preserve \(\mu\). Because \(\deg\mu=8\) and characteristic is zero, this is the full Galois group of the generic function-field extension.

**(3) Exact branch support and inertia.** A nonidentity diagonal-sign involution on \(C\) fixes exactly the two points of one coordinate-hyperplane section. Its action on \(C\times C\) therefore has only four fixed points, not a divisorial fixed locus. The remaining four nonidentity group elements are \(\tau\epsilon\), whose fixed curves are the graphs \(\Gamma_\epsilon=\{(x,\epsilon x):x\in C\}\). Their images are \(\sum_i\epsilon_i z_i=0\), since \(z_i=\epsilon_i x_i^2\). These are the four displayed lines. A separable finite quotient in characteristic zero is ramified in codimension one exactly along divisorial fixed loci; the stabilizer of a general point of each graph has order two. Thus these, and no additional curves, are the reduced branch support; every generic ramification index is two. Each graph has bidegree \((1,1)\). The total ramification divisor has class \((4,4)\), agreeing with \(K_{C\times C}-\mu^*K_{\mathbb P^2}=(-2,-2)-(-6,-6)=(4,4)\).

**(4) An explicit equation for the intermediate quotient.** Set \(z_i=x_i y_i\) and
\[
w=x_0^2 y_1^2-x_1^2 y_0^2.
\]
The conic relations imply \(z_2^2=(x_0^2+x_1^2)(y_0^2+y_1^2)\), so
\[
(z_0^2+z_1^2-z_2^2)^2-4z_0^2z_1^2=w^2.
\]
Factoring the left side produces exactly the four-line product. The function \(w\) is invariant under \(V\) and changes sign under \(\tau\). Because the field extension for \(\mu\) has group \(V\times\langle\tau\rangle\), \(k(C\times C)^V=k(\mathbb P^2)(w)\) is the indicated quadratic function field. The quartic double cover defined by \(w^2=B(z)\) is normal: away from its six transverse branch crossings it is smooth, and at each crossing its local equation is \(w^2=uv\). It is finite over \(\mathbb P^2\); being the integral closure of the base in this quadratic field, it is canonically \(Y\).

**(5) Singularities and canonical class.** The four distinct lines are in general position: every three corresponding coefficient vectors have nonzero determinant \(\pm4\), so there are exactly six pairwise intersections. Locally at any intersection the branch equation is a unit times \(uv\), and after taking a square root of the unit the double cover is the ordinary \(A_1\) surface singularity \(w^2=uv\). Over smooth branch points the double cover is smooth, and off the branch divisor it is étale. The double-cover adjunction formula gives \(K_Y=\pi^*(K_{\mathbb P^2}+2H)=-\pi^*H\), hence \(-K_Y\) is ample and \(K_Y^2=2\). Resolving the six rational double points is crepant, preserving \(K^2=2\); the anticanonical divisor on the resolution is nef and big, making it a weak del Pezzo surface.

## Verification
A standalone exact-arithmetic checker verifies the quartic factorization, the defining conic parametrization, the quadratic invariant identity, and the double-cover square-root identity without numerical approximations. Its successful output is `VERIFY_OK`. The proof, not sampling, establishes the universal characteristic-zero statements. A group-theoretic and intersection-theoretic consistency test independently yields degree \(8\), six quotient nodes, and ramification class \((4,4)\).

## Relationship to prior work
Bocci–Carlini–Kileel, *Hadamard Products of Linear Spaces* (2015), introduce the projective coordinatewise product and analyze principally linear spaces; their accessible text does not present this conic's Galois cover or its intermediate quotient. Bocci–Carlini, *Hadamard Products of Hypersurfaces* (2021), study idempotence and binomial conditions; their accessible full paper does not state the eight-sheeted branched-conic calculation. The four-line double plane and its six nodes are classical features of the double-cover construction and are not claimed separately as new. The distinct contribution asserted here is their explicit identification as the intermediate quotient and branch geometry of this natural Hadamard-conic multiplication map.

## Limitations
The statement concerns characteristic zero and the specified (equivalently diagonal nondegenerate) conic. It does not classify general embedded conics in arbitrary coordinates. Possible implicit or explicit coverage in the 2024 Bocci–Carlini monograph, whose full text was not inspected, remains a significant originality risk. No independent audit has been performed.

## References
1. C. Bocci, E. Carlini, J. Kileel, *Hadamard Products of Linear Spaces*, arXiv:1504.04301, first posted 16 April 2015; https://arxiv.org/pdf/1504.04301.
2. C. Bocci, E. Carlini, *Hadamard Products of Hypersurfaces*, arXiv:2109.09548, first posted 20 September 2021; https://arxiv.org/pdf/2109.09548.
3. C. Bocci, E. Carlini, *Hadamard Products of Projective Varieties*, Birkhäuser, 2024, DOI:10.1007/978-3-031-54263-3 (bibliographic preview only; full text not inspected).
