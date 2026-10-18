# The intrinsic John ball of a regular bipartite perfect-matching polytope with uniform edge resistance

## Finding
Let \(G=(U\sqcup W,E)\) be any connected simple \(d\)-regular bipartite graph, with \(|U|=|W|=n\) and \(d\ge2\), and put \(m=nd\) and \(D=m-2n+1\). Equip its perfect-matching polytope, in edge coordinates, with the intrinsic Euclidean metric:
\[
Q_G=\operatorname{conv}\{\mathbf1_M:M\subseteq E\text{ a perfect matching}\}
=\{x\in\mathbb R^E:x_e\ge0,\ \sum_{e\ni v}x_e=1\ (v\in U\sqcup W)\}.
\]
Assume every edge has the same effective resistance in the unit-resistance electrical network on \(G\). Equivalently, the orthogonal projection \(P\) onto the real cycle space of \(G\) has a constant diagonal. This hypothesis holds for **every edge-transitive** connected regular bipartite graph; vertex transitivity is not necessary.

Then the **unique maximum-volume inscribed ellipsoid** (intrinsic John ellipsoid) of \(Q_G\) is the Euclidean ball
\[
\boxed{\mathcal J_G=\left\{\frac1d\mathbf1_E+z:z\in\ker B,\ \|z\|_2\le\sqrt{\frac{n}{d(nd-2n+1)}}\right\},}
\]
where \(B\) is any signed vertex-edge incidence matrix with its columns oriented from \(U\) to \(W\). In particular its intrinsic dimension and radius are
\[
\boxed{D=n(d-2)+1,\qquad r=\sqrt{\frac{n}{dD}}.}
\]
Its center is also the unique maximum-radius inball center. **Every edge-coordinate hyperplane** \(x_e=0\) is a supporting hyperplane tangent to the John ball, and the contact normals admit the uniform positive John decomposition
\[
\boxed{\lambda_e=\frac Dm\quad(e\in E).}
\]
The contact points are not asserted to be all distinct (for cycles, different edge hyperplanes can meet the same contact).

The formula holds for structurally forbidden matrix entries, not merely for the classical complete bipartite Birkhoff polytope. For the crown graph \(G=K_{n,n}\setminus M\) obtained by deleting a fixed perfect matching, \(n\ge3\),
\[
\boxed{\dim Q_G=n^2-3n+1,\quad r^2=\frac{n}{(n-1)(n^2-3n+1)}.}
\]
For the \(k\)-dimensional cube graph, \(k\ge2\), the number of vertices in each color class is \(2^{k-1}\), and
\[
\boxed{r^2=\frac{2^{k-1}}{k[2^{k-1}(k-2)+1]}.}
\]

## Assumptions and scope
A connected \(d\)-regular bipartite graph has two vertex classes of equal size. The edge coordinate space is \(\mathbb R^E\) with the standard Euclidean norm; the metric is not a graph shortest-path metric. Positive solutions to all the displayed vertex-sum equalities have the affine tangent space \(T=\ker B\), of dimension \(m-(2n-1)=D\). The uniform point \(c=\mathbf1_E/d\) is positive and hence lies in the relative interior. Bipartite matching integrality gives the displayed equality between the convex hull and the nonnegative equality-feasible set. For \(d=2\) the graph is an even cycle, and \(D=1\); all assertions include this boundary case.

The electrical resistance \(R_{\mathrm{eff}}(e)\) uses unit resistance on each edge. Its relation to \(P\) is \(P_{ee}=1-R_{\mathrm{eff}}(e)\); equality of all effective resistances is a hypothesis, not a general property of arbitrary regular bipartite graphs. A sufficient, strictly more elementary hypothesis for the geometric conclusion is simply that all \(P_{ee}\) are equal.

## Proof
**1. Rank, projection, and equal leverage.** Orient each edge from \(U\) to \(W\), so that \(B\in\mathbb R^{2n\times m}\) has a \(+1\) and a \(-1\) in each column. Since \(G\) is connected, \(\operatorname{rank}B=2n-1\), so \(T=\ker B\) has dimension \(D=m-2n+1>0\). If \(P\) is orthogonal projection onto \(T\), then the projected normal to the restricted coordinate hyperplane \(x_e=0\) is \(P\varepsilon_e\), with squared norm \(P_{ee}\). The standard incidence-Laplacian projection identity gives
\[
P=I-B^{\mathsf T}(BB^{\mathsf T})^+B,
\qquad P_{ee}=1-b_e^{\mathsf T}(BB^{\mathsf T})^+b_e=1-R_{\mathrm{eff}}(e).
\]
Under the constant-resistance assumption, all \(P_{ee}\) coincide. Taking the trace shows, without any numerical spectral approximation,
\[
\boxed{P_{ee}=\kappa^2=\frac{\operatorname{tr}P}{m}=\frac Dm>0.}
\]
This is also Foster's trace identity: each edge has \(R_{\mathrm{eff}}(e)=(2n-1)/m\).

**2. A uniformly tangent Euclidean ball.** Put \(c=\mathbf1_E/d\) and \(r=(d\kappa)^{-1}\). All coordinate inequalities \(x_e\ge0\) hold on the intrinsic ball \(c+rB_T\), because for \(\|z\|_2\le r\) in \(T\),
\[
(c+z)_e\ge\frac1d-r\|P\varepsilon_e\|_2=\frac1d-r\kappa=0.
\]
The equalities \(B(c+z)=Bc\) are automatic. The contact point for coordinate \(e\) is
\[
y_e=c-\frac{r}{\kappa}P\varepsilon_e=c-\frac1{d\kappa^2}P\varepsilon_e.
\]
It belongs to \(Q_G\), lies on \(x_e=0\), and has intrinsic distance \(r\) from \(c\). Hence all \(m\) coordinate supporting hyperplanes touch this ball, possibly with repeated physical contact points. Substitution \(m=nd\) gives \(r^2=n/(dD)\).

**3. A complete positive John contact certificate.** Map \(c+rB_T\) to the Euclidean unit ball in \(T\). The inward-to-outward unit normals at its contacts are
\[
u_e=-\frac{P\varepsilon_e}{\kappa}\in T,\qquad \|u_e\|_2=1.
\]
Give them weights \(\lambda_e=\kappa^2=D/m>0\). Since \(\mathbf1_E\in\operatorname{im}B^{\mathsf T}\) (the bipartition potentials take values \(+1/2\) and \(-1/2\)), \(P\mathbf1_E=0\). Therefore
\[
\sum_{e\in E}\lambda_eu_e=-\kappa P\mathbf1_E=0.
\]
Moreover, using \(P^2=P\) and the standard edge basis,
\[
\sum_{e\in E}\lambda_eu_eu_e^{\mathsf T}
=\sum_{e\in E}(P\varepsilon_e)(P\varepsilon_e)^{\mathsf T}
=P^2=P=I_T.
\]
These are **both** equations of John's characterization of a maximum-volume inscribed ellipsoid. The contained Euclidean ball is consequently the global John ellipsoid of \(Q_G\), including against arbitrarily translated and anisotropic competitors, and it is unique by the uniqueness part of John's theorem. Coincident contacts can be combined by adding their weights; neither equation changes.

**4. Uniqueness of the Euclidean incenter.** If any intrinsic ball of radius at least \(r\), centered at some \(a\in Q_G\), is contained in \(Q_G\), the coordinate inequalities require \(a_e\ge r\kappa=1/d\) for every edge. But the vertex sums imply \(\sum_e a_e=n=m/d\); therefore equality holds in every coordinate, forcing \(a=c\). No ball of radius larger than \(r\) can satisfy the same sum constraint. Thus the incenter is unique, independently of the John uniqueness argument.

**5. Explicit graphs and volume.** Every edge-transitive graph has constant edge resistance because automorphisms preserve the graph Laplacian and its pseudoinverse. The crown graph is \((n-1)\)-regular and edge-transitive, and the cube graph has degree \(k\) and \(2^{k-1}\) vertices in each bipartition class; substitution proves the displayed examples. The exact intrinsic ellipsoid volume is
\[
\boxed{\operatorname{vol}_{D}(\mathcal J_G)=\frac{\pi^{D/2}}{\Gamma(D/2+1)}\left(\frac{n}{dD}\right)^{D/2}.}
\]

## Verification
The included standalone Python 3 checker `check_john.py` uses exact rational Gaussian elimination for incidence Gram matrices and the cycle-space projection. In the performed run it passed the six graphs `C6`, `K33`, `C8`, `crown4=Q3`, `crown5`, and `Q4`, respectively of intrinsic dimensions \(1,4,1,5,11,17\). For each, it verified the projection is idempotent, all diagonal entries equal \(D/m\), the all-one vector is killed, the stated squared radius holds, and the proposed tangent points satisfy every nonnegativity and every vertex-sum constraint with exact fractions. The output terminates with `EXACT_RATIONAL_CHECKS_PASS`. The finite cases are checks; the general result follows from the preceding projection algebra and exact John certificate.

## Relationship to prior work
Torres's 2023 theorem identifies the fractional and integral \(k\)-matching polytopes of bipartite graphs and supplies the \(H\)-representation used here; its normality and face-combinatorics conclusions do not supply the intrinsic maximum-volume ellipsoid. Paffenholz studies combinatorial faces of Birkhoff polytopes, not their John ellipsoids. Bauschke–Singh–Wang examine orthogonal projection onto complete prescribed-row/column-sum affine spaces rather than graph-specific positive coordinate cones.

The previously available exact Euclidean inradius and center theorem for **acyclic flow polytopes** applies after orienting all bipartite edges from one class to the other. Thus **the scalar inradius and incenter formulas are not claimed as separate novel discoveries**. The new statement is the considerably stronger exact **maximum-volume ellipsoid**, including an all-facet positive John contact design, its shape and its volume for arbitrary uniform-resistance regular bipartite supports. A prior complete-support transportation inradius theorem includes the Birkhoff specialization, but expressly excludes structural zeros. A separate earlier John-ellipsoid theorem for full-dimensional **fractional matching polytopes** uses degree upper inequalities and analyzes an ellipsoid in \(\mathbb R^E\); it does not imply the John ellipsoid in the lower-dimensional perfect-matching equality face. Restricting an optimum ellipsoid to an affine face does not, in general, preserve John optimality.

## Limitations
The formula is conditional on equal edge effective resistances (equivalently constant cycle-space diagonal), and does not claim that every regular bipartite graph satisfies this. It concerns perfect-matching equality faces, not full-dimensional fractional matching relaxations. It does not characterize the entire directional contact multiplicity beyond the \(m\) coordinate supporting hyperplanes; distinct edges can produce the same point in dimension one. The finite checker is corroborative, not an exhaustive classification. The bibliographic comparison is finite, and an earlier formulation via isotropic contact designs, graph orbit geometry, or optimal experimental design is a remaining priority risk. Independent validation has not been carried out.

## References
1. J. C. Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910v1, first public 2023-06-20, especially Section 3 and Theorem 3.1; primary MSC2020 52B11.
2. A. Paffenholz, *Faces of Birkhoff Polytopes*, arXiv:1304.3948v1 (2013), Electronic Journal of Combinatorics 22 (2015), P1.67, DOI 10.37236/4499.
3. H. H. Bauschke, S. Singh and X. Wang, *Projecting onto Rectangular Matrices with Prescribed Row and Column Sums*, arXiv:2105.12222 (2021).
4. *Euclidean inradius of acyclic flow polytopes as an effective-resistance cut ratio*, public research record, `2026/10/11/SCOPE-euclidean-inradius-of-acyclic-flow-polytopes-as-an-effective-res--9a80040abd60`.
5. *Exact intrinsic Euclidean inradius and centers of transportation polytopes*, public research record, `2026/10/11/SCOPE-exact-intrinsic-euclidean-inradius-and-centers-of-transportation--dbb208ea5834`.
6. *Spectral John ellipsoids of vertex-and-edge-transitive fractional matching polytopes*, public research record, `2026/10/11/SCOPE-spectral-john-ellipsoids-of-vertex-and-edge-transitive-fractiona--443f302b065c`.
7. F. John, *Extremum Problems with Inequalities as Subsidiary Conditions*, Studies and Essays Presented to R. Courant (1948), 187–204.
