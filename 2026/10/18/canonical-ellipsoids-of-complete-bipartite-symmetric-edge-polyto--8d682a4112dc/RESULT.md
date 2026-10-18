# Canonical ellipsoids of complete-bipartite symmetric edge polytopes

## Finding

Let \(2\le a\le b\) be integers, \(N=a+b\), \(d=N-1\), and \(G=K_{a,b}\), with graph Laplacian \(L\). In the Euclidean zero-sum space
\[
H=\{x\in\mathbb R^N:\sum_i x_i=0\},
\]
consider the symmetric edge polytope
\[
P_G=\operatorname{conv}\{\pm(e_i-e_j):1\le i\le a<j\le N\}.
\]
Its unique maximum-volume inscribed (John) ellipsoid and unique minimum-volume enclosing (Löwner) ellipsoid are both centered at the origin, with shape operators on \(H\)
\[
\boxed{\Sigma_J=\frac{L}{ab},\qquad \Sigma_L=\frac{dL}{ab}=d\Sigma_J.}
\]
Here the ellipsoid of positive-definite shape operator \(\Sigma\) is \(\mathcal E(\Sigma)=\{x\in H:\langle x,\Sigma^{-1}x\rangle\le1\}\); the inverse is restricted to \(H\). Every facet of \(P_G\) touches \(\mathcal E(\Sigma_J)\), and every vertex touches \(\mathcal E(\Sigma_L)\). Consequently the sharp symmetric John containment is attained:
\[
\mathcal E(\Sigma_J)\subset P_G\subset\sqrt d\,\mathcal E(\Sigma_J),
\]
with equality in the outer radius at all \(2ab\) vertices.

The squared principal semiaxes of the John ellipsoid are \(1/a\) with multiplicity \(a-1\), \(1/b\) with multiplicity \(b-1\), and \(N/(ab)\) with multiplicity one. Writing \(\kappa_d\) for the Euclidean unit-ball volume, the intrinsic volumes satisfy
\[
\operatorname{vol}_d(\mathcal E(\Sigma_J))
=\kappa_d\sqrt{\frac{N}{a^a b^b}},\qquad
\frac{\operatorname{vol}_d(\mathcal E(\Sigma_L))}{\operatorname{vol}_d(\mathcal E(\Sigma_J))}
=d^{d/2}.
\]

## Assumptions and scope

All norms, volumes, projections, and ellipsoids use the standard inner product on \(H\subset\mathbb R^N\), not an unspecified coordinate identification of \(H\) with \(\mathbb R^d\). Edges of \(K_{a,b}\) join the first \(a\) to the last \(b\) vertices. The graph Laplacian is \(L=\sum_{i\le a<j}(e_i-e_j)(e_i-e_j)^{\mathsf T}\). Its nullspace is the constants and it is positive definite on \(H\). The result includes the already familiar \(K_{2,2}\) cube case, but the claim covers the genuinely non-cactus graphs \(K_{a,b}\) with \(ab>4\) as well.

## Proof

**1. Facet normals and polarity.** Identify \(H\) with its Euclidean dual and let \(\pi\) be orthogonal projection onto \(H\). The polar polytope is
\[
P_G^\circ=\{y\in H:|y_i-y_j|\le1\ (1\le i\le a<j\le N)\}.
\]
A feasible \(y\) is a vertex precisely when its graph of tight edges \(\{ij:|y_i-y_j|=1\}\) is connected: the tight edge differences span \(H\) exactly in that case. For a feasible labeling, a positive tight difference must join a largest first-part label to a smallest second-part label, and a negative tight difference joins the opposite extremes. If both parts have nonconstant labels, these two types form disjoint tight subgraphs, preventing connectedness. If one part is constant, connectedness forces every label on the other part to differ from it by exactly one. It follows that the complete polar vertex set, with repetitions removed, is
\[
\{\pi(s,0_b):s\in\{-1,1\}^a\}
\ \cup\
\{\pi(0_a,t):t\in\{-1,1\}^b\}.
\]
There are \(2^a+2^b-2\) distinct vertices. This also directly reconstructs the complete-bipartite facet description in Higashitani--Jochemko--Michałek, Proposition 3.4 [1]. Every such normal \(y\) satisfies \(|y_i-y_j|=1\) on all graph edges, hence
\[
\langle y,\Sigma_Jy\rangle
=\frac1{ab}\sum_{i\le a<j}(y_i-y_j)^2=1.
\]
Thus \(\mathcal E(\Sigma_J)\subset P_G\) and *every* supporting facet touches it, at \(\Sigma_Jy\).

**2. Optimality of the inscribed ellipsoid.** Because \(P_G\) is centrally symmetric, both canonical ellipsoids are centered at zero. Under polarity, a maximum-volume origin-centered ellipsoid in \(P_G\) corresponds to a minimum-volume origin-centered ellipsoid containing \(P_G^\circ\). We exhibit an exact isotropic contact measure for the enclosing polar ellipsoid
\[
E^\circ=\{y\in H:\langle y,\Sigma_Jy\rangle\le1\}.
\]
Write \(H=U_A\oplus U_B\oplus\mathbb Rz\), where \(U_A\) and \(U_B\) are zero-sum vectors supported on the respective parts and
\[
z=\sqrt{\frac b{aN}}\,1_A-\sqrt{\frac a{bN}}\,1_B.
\]
These spaces have dimensions \(a-1\), \(b-1\), and one. The shape \(\Sigma_J\) has eigenvalues \(1/a\), \(1/b\), and \(N/(ab)\) on these spaces.

Let \(u_a\) equal zero for even \(a\) and one for odd \(a\); define \(u_b\) likewise. Draw a uniformly random sign vector \(s\in\{-1,1\}^a\) conditioned on \(|\sum_i s_i|=u_a\), and set \(Y_A=\pi(s,0_b)\). Define \(Y_B\) analogously. Their distributions are centrally symmetric. Their covariance on \(U_A\), respectively \(U_B\), is scalar with values
\[
c_a=\frac{a^2-u_a^2}{a(a-1)},\qquad
c_b=\frac{b^2-u_b^2}{b(b-1)}.
\]
The remaining variance of \(Y_A\) along \(z\) is \(bu_a^2/(aN)\), and that of \(Y_B\) is \(au_b^2/(bN)\). Cross-covariances vanish by permutation and sign symmetry. The pure-direction polar vertices \(Y_Z=\pm\pi(1_A,0_b)\), chosen with equal probability, have covariance \((ab/N)zz^{\mathsf T}\).

Define positive mixing coefficients
\[
p_A=\frac{a^2(a-1)}{d(a^2-u_a^2)},\quad
p_B=\frac{b^2(b-1)}{d(b^2-u_b^2)},\quad
p_Z=\frac1d-\frac{p_Au_a^2}{a^2}-\frac{p_Bu_b^2}{b^2}.
\]
Indeed \(p_Z>0\), since each nonzero subtraction is at most \(1/[d(a+1)]\) or \(1/[d(b+1)]\); also \(p_A+p_B+p_Z=1\). The centrally symmetric probability measure assigning masses \(p_A,p_B,p_Z\) to these three distributions satisfies the exact matrix identity
\[
\mathbb E[YY^{\mathsf T}]=\frac1d\Sigma_J^{-1}\quad\text{on }H.
\]
All points in its support are polar vertices on the boundary of \(E^\circ\), by Step 1. Transforming by \(\Sigma_J^{1/2}\) gives unit contact vectors of mean zero and covariance \(I_H/d\). The Löwner contact criterion proves that \(E^\circ\) uniquely minimizes enclosing ellipsoid volume. Polarity now proves the claimed John ellipsoid and its uniqueness.

**3. Optimality of the enclosing ellipsoid.** There are \(ab\) unoriented edges; choose an edge uniformly and give \(v=e_i-e_j\) either sign with equal probability. The covariance is exactly \(L/(ab)=\Sigma_J\). Since the automorphism group is transitive on the \(2ab\) signed vertices and preserves \(\Sigma_L\), all their squared \(\Sigma_L^{-1}\)-norms are identical. Their average is
\[
\operatorname{tr}_H\bigl(\Sigma_L^{-1}\Sigma_J\bigr)=d/d=1,
\]
so each is one. It follows that \(P_G\subset\mathcal E(\Sigma_L)\). Its transformed vertex contacts have mean zero and covariance \(I_H/d\), proving global Löwner optimality and uniqueness by the same contact criterion.

**4. Determinant and radii.** The complete-bipartite Laplacian has nonzero eigenvalues \(b\) (multiplicity \(a-1\)), \(a\) (multiplicity \(b-1\)), and \(N\) (multiplicity one). Hence the intrinsic determinant of \(\Sigma_J\) is \(N/(a^ab^b)\). The stated semiaxes, volumes and exact \(\sqrt d\) containment follow.

## Verification

The accompanying dependency-free `verify.py` uses exact rational arithmetic. For \(2\le a\le5\) and \(a\le b\le7\), it constructs the Laplacian pseudoinverse, checks every polar facet-normal contact, every signed edge-vertex contact, and the complete isotropic covariance certificate. For \(a\le4\), \(b\le5\), it additionally enumerates all feasible bounded integer potential labelings, tests tight-graph connectivity, and compares the resulting exhaustive facet-normal set with the formula. Run with `python3 verify.py` from the extracted package directory. Finite checks do not establish the infinite-parameter theorem, which is proved above.

## Relationship to prior work

Higashitani--Jochemko--Michałek [1] give the complete-bipartite facet labels and study Ehrhart and face invariants; their Proposition 3.4 is the sharp combinatorial precursor used and independently reconstructed here. Chen--Davis--Korchevskaia [2] study facet subgraphs, and D'Alì--Delucchi--Michałek [3] connect symmetric edge polytopes with Kantorovich--Rubinstein and Lipschitz polytopes. D'Alì--Juhnke-Kubitzke--Koch [4] generalize facet descriptions to regular matroids. The inspected texts do not identify either canonical ellipsoid, their homothety, or their universal contacts for \(K_{a,b}\). The already known cube case \(K_{2,2}\) does not cover the two-parameter family with \(ab>4\).

## Limitations

The assertion concerns the intrinsic standard edge-coordinate Euclidean metric. It establishes John and Löwner ellipsoids and the exact sharpness of the corresponding John containment, **not** an optimal Banach--Mazur distance under arbitrary linear reparameterization, nor a classification for arbitrary bipartite graphs. Full independent publication-priority verification has not been performed; an equivalent calculation in the finite-metric-space or Banach-space literature remains a residual bibliographic risk. The finite verifier is corroboration only.

## References

[1] A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (2018), especially Proposition 3.4 and Section 4. https://arxiv.org/abs/1807.07678

[2] T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (2021), Theorem 3. https://arxiv.org/abs/2107.12315

[3] A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (2019), Sections 2 and 4. https://arxiv.org/abs/1910.05193

[4] A. D'Alì, M. Juhnke-Kubitzke, M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933v1 (2023), Section 5, Theorem 5.8 and Proposition 5.12. https://arxiv.org/abs/2307.04933
