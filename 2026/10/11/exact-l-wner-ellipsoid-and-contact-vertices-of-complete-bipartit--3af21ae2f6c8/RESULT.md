# Exact Löwner ellipsoid and contact vertices of complete-bipartite graphical zonotopes

## Finding

Let \(p,q\ge 2\) be integers, put \(d=p+q-1\) and \(m=pq\), and let \(B\) be any oriented vertex-edge incidence matrix of the complete bipartite graph \(K_{p,q}\), with its \(p\) first vertices in one class and its \(q\) last vertices in the other. In the Euclidean hyperplane \(H=\mathbf1^\perp\subset\mathbb R^{p+q}\) define the centered graphical zonotope
\[
Z_{p,q}=\left\{\tfrac12B\varepsilon:\varepsilon\in[-1,1]^{pq}\right\}.
\]
Write \(L=BB^\mathsf T\) for the graph Laplacian and \(L^+\) for its Moore--Penrose inverse on \(\mathbb R^{p+q}\). Then the unique minimum-volume ellipsoid enclosing this polytope *in its affine span* is
\[
\boxed{\ \mathcal E_{p,q}=\left\{z\in H:z^\mathsf TL^+z\le\frac{pq}{4}\right\}.\ }
\]
The centered ellipsoid's positive shape operator on \(H\) is \(Q=(pq/4)L|_H\). Its semiaxis squares are \(pq^2/4\) with multiplicity \(p-1\), \(p^2q/4\) with multiplicity \(q-1\), and \(pq(p+q)/4\) with multiplicity one. Its exact intrinsic Euclidean volume is
\[
\boxed{\ \kappa_d\left(\frac{pq}{4}\right)^{d/2}
q^{(p-1)/2}p^{(q-1)/2}\sqrt{p+q},\ }
\]
where \(\kappa_d\) is the volume of the unit Euclidean \(d\)-ball.

Exactly \(2^p+2^q-2\) zonotope vertices contact \(\mathcal E_{p,q}\). Relative to the canonical edge orientation from the first class to the second, these are precisely the images of \(\varepsilon\in\{\pm1\}^{p\times q}\) that are **constant along every row** or **constant down every column**. Every other point of the zonotope lies strictly inside the ellipsoid.

## Assumptions and scope

All edges have unit generator length, and all intrinsic volumes are computed using the Euclidean metric inherited from the coordinate hyperplane \(H\); neither nonuniform weights nor noncomplete bipartite graphs are asserted. Edge orientation affects the sign parametrization but not the zonotope. The pseudoinverse acts by inversion of \(L\) on \(H\) and by zero on the constants. Throughout the proof, the expressions \(p\) and \(q\) denote positive integers at least two; the parity indicators are \(h_p=p\bmod2\) and \(h_q=q\bmod2\).

## Proof

**1. The universal enclosing ellipsoid and its equality condition.** Let \(V=B/2\), so \(Z_{p,q}=V[-1,1]^m\), and define \(Q=mVV^\mathsf T|_H=(m/4)L|_H\). Connectivity makes \(Q\) positive definite on \(H\). Let \(\Pi=V^\mathsf T(VV^\mathsf T)^+V\), the orthogonal projection in the edge space onto the row space of \(V\). For each sign vector \(\varepsilon\in\{\pm1\}^m\),
\[
(V\varepsilon)^\mathsf TQ^{-1}(V\varepsilon)
=\frac{\varepsilon^\mathsf T\Pi\varepsilon}{m}
\le\frac{\|\varepsilon\|_2^2}{m}=1.
\]
Equality holds **if and only if** \(\varepsilon\) belongs to the incidence row space. Because every point in the cube is a convex combination of sign vectors, convexity of the ellipsoid proves \(Z_{p,q}\subset\mathcal E_{p,q}\).

For the canonical orientation, membership of a sign matrix in the incidence row space is equivalent to the existence of real potentials \(a_i,b_j\) satisfying \(\varepsilon_{ij}=a_i-b_j\). Equivalently every two-by-two alternating sum vanishes:
\[
\varepsilon_{ij}-\varepsilon_{i\ell}-\varepsilon_{kj}+\varepsilon_{k\ell}=0
\quad\text{for all admissible indices}.
\]
If any two rows differ, their coordinatewise difference is a nonzero constant in \(\{-2,2\}\). Consequently one row is entirely \(+1\), the other entirely \(-1\), and every remaining row is constant. Otherwise all rows are identical. Thus precisely the sign matrices constant in each row, or identical across all rows (constant down each column), are incidence-row-space signs. These two families have respectively \(2^p\) and \(2^q\) members, with two common all-constant matrices.

The linear map \(V\) is injective on its row space, so all \(2^p+2^q-2\) images are distinct. Because the enclosing ellipsoid is strictly convex, a boundary point of it belonging to the zonotope cannot be an interior point of any proper zonotope segment, hence every contact is a zonotope vertex. Conversely, equality in the preceding projection inequality forces each boundary sign vector to be a row-space sign. A nontrivial convex combination of distinct ellipsoid points is strictly internal, so there are no other contact points.

**2. Exact supporting contact measure.** The two independent permutation groups within the bipartition and simultaneous sign inversion preserve the ellipsoid and the zonotope. Set
\[
\begin{split}
 d&=p+q-1,\quad h_p=p\bmod2,\quad h_q=q\bmod2,\\
 \alpha&=\frac{p^2(p-1)}{d(p^2-h_p)},\\
 \beta&=\frac{q^2(q-1)}{d(q^2-h_q)},\\
 \gamma&=\frac1d\left(1-\frac{(p-1)h_p}{p^2-h_p}-\frac{(q-1)h_q}{q^2-h_q}\right).
\end{split}
\]
These numbers are positive and sum to one. Indeed, the relevant parity term vanishes in even dimension and, for any odd integer at least three, obeys \((k-1)/(k^2-1)=1/(k+1)\le1/4\); thus \(\gamma>0\). The normalization follows directly from
\[
\alpha=\frac{p-1}{d}\left(1+\frac{h_p}{p^2-h_p}\right),\qquad
\beta=\frac{q-1}{d}\left(1+\frac{h_q}{q^2-h_q}\right).
\]
Construct a discrete distribution on contact points by mixing the following three experiments:

1. With probability \(\alpha\), choose a uniformly random sign vector \(a\in\{\pm1\}^p\) conditioned on \((\sum_i a_i)^2=h_p\), then set \(\varepsilon_{ij}=a_i\).
2. With probability \(\beta\), choose a uniformly random sign vector \(b\in\{\pm1\}^q\) conditioned on \((\sum_j b_j)^2=h_q\), then set \(\varepsilon_{ij}=b_j\).
3. With probability \(\gamma\), choose equally between the two matrices with all entries \(+1\) and all entries \(-1\).

Every selected sign matrix is a contact sign by part 1. Sign-reversal invariance yields mean zero for the resulting random vector \(z=V\varepsilon\).

**3. Isotropy of the contact measure.** Orthogonally decompose \(H\) into the subspace \(U\) of first-class contrasts (dimension \(p-1\)), the subspace \(W\) of second-class contrasts (dimension \(q-1\)), and the one-dimensional between-class contrast \(T\). On \(U,W,T\), the matrix \(Q\) acts by the respective eigenvalues
\[
 \lambda_U=\frac{pq^2}{4},\quad
 \lambda_W=\frac{p^2q}{4},\quad
 \lambda_T=\frac{pq(p+q)}{4}.
\]
A uniform near-balanced \(k\)-sign vector \(a\) has pairwise covariance
\[
\mathbb E(a_i a_j)=\frac{h_k-k}{k(k-1)}\quad (i\ne j),
\]
and therefore covariance \((k^2-h_k)/(k(k-1))\) times the identity on its contrast subspace. In the first experiment, the projection of \(z\) onto \(U\) is \((q/2)\) times that contrast vector, so the mixture contribution to \(\operatorname{Cov}(z)|_U\) equals
\[
 \alpha\frac{q^2}{4}\frac{p^2-h_p}{p(p-1)}
 =\frac{pq^2}{4d}=\frac{\lambda_U}{d}.
\]
Analogously the second experiment gives \(\lambda_W/d\) on \(W\). The constant-sign contact (the positive pole) has squared length \(\lambda_T\). The projections onto \(T\) of the first and second experiments are respectively \((\sum a_i/p)\) and \((\sum b_j/q)\) times that pole, up to an irrelevant common sign convention. Their squared factors are \(h_p/p^2\) and \(h_q/q^2\). Hence the total \(T\) variance is
\[
\lambda_T\left(\alpha\frac{h_p}{p^2}+
\beta\frac{h_q}{q^2}+\gamma\right)=\frac{\lambda_T}{d}.
\]
All cross-covariance blocks vanish by independent within-class permutations and sign symmetry. Therefore the constructed contact-point distribution satisfies the *exact matrix identity*
\[
 \boxed{\mathbb E z=0,\qquad\mathbb E(zz^\mathsf T)=Q/d.}
\]

**4. Global ellipsoid optimality and uniqueness.** Let any full-dimensional competing enclosing ellipsoid in \(H\) have center \(b\) and positive shape operator \(S\). Averaging its defining containment inequality over the contact distribution from part 3 yields
\[
\frac1d\operatorname{tr}(S^{-1}Q)+b^\mathsf TS^{-1}b\le1.
\]
The arithmetic-geometric mean inequality on the positive eigenvalues of \(S^{-1/2}QS^{-1/2}\) gives
\[
\left(\frac{\det Q}{\det S}\right)^{1/d}
\le\frac1d\operatorname{tr}(S^{-1}Q)\le1.
\]
Thus \(\det S\ge\det Q\), and intrinsic ellipsoid volume is proportional to the square root of this determinant. In case of equality, both inequalities are equalities, forcing \(b=0\), \(S^{-1/2}QS^{-1/2}=I_H\), and hence \(S=Q\). This proves the claimed unique minimum-volume ellipsoid, not merely local optimality.

Finally, the standard complete-bipartite Laplacian has nonzero eigenvalues \(q\) repeated \(p-1\) times, \(p\) repeated \(q-1\) times, and \(p+q\) once. Their product multiplied by \((pq/4)^d\) equals \(\det_H Q\), yielding the displayed exact volume and semiaxes.

## Verification

The standalone Python standard-library script `verify.py` implements the gauge using the above orthogonal decomposition, exactly enumerates all edge-sign choices in eleven small bipartite graphs, checks strict contact membership and the exact contact count, and separately reconstructs the full contact-distribution covariance entry by entry using rational arithmetic for 64 parameter pairs. Invoke `python3 verify.py` with Python 3. No computer experiment is needed for the all-parameter proof: its critical infinite claims are the row-space characterization and explicit symbolic covariance identity displayed above.

## Relationship to prior work

Padrol, Pilaud, and Poullot study the combinatorics and deformation cones of graphical zonotopes, including their acyclic-orientation vertex correspondence [1]. Chapoton and Pilaud explicitly identify the complete-bipartite graphical zonotope as the shuffle of two point polytopes and study its combinatorial structure [2]. Their results do not furnish the minimum-volume enclosing ellipsoid or its full contact set. Gaßmann and Althoff discuss enclosing-ellipsoid constructions for general zonotopes [3]; the generator-covariance shape is a natural initial enclosure, but their general conversion method does not imply that it is minimum-volume for this specific family. Barvinok and Blekherman's orbit-ellipsoid method [4] gives general symmetry tools, but the explicit mixed contact distribution here must still be established. The new result is specifically the exact optimized affine ellipsoid plus its complete contact-vertex classification, not an assertion that the use of Laplacians or general ellipsoid optimality certificates is new.

## Limitations

The theorem is confined to complete bipartite unit-weight graphical zonotopes and the intrinsic Euclidean structure; it is not a classification of all bipartite zonotopes or a claim about arbitrary edge weights. A literature search, including the primary full texts in [1]--[4], did not locate an identical specialization, but unexamined equivalent formulations, particularly through projected cubes or graph-incidence covariance ellipsoids, remain possible. Independent assessment has not been performed.

## References

[1] A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first version November 24, 2021, https://arxiv.org/abs/2111.12422.

[2] F. Chapoton, V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896, first version January 18, 2022, https://arxiv.org/abs/2201.06896.

[3] V. Gaßmann, M. Althoff, *Scalable Zonotope-Ellipsoid Conversions Using the Euclidean Zonotope Norm*, American Control Conference (2020), DOI:10.23919/ACC45564.2020.9147938.

[4] A. Barvinok, G. Blekherman, *Convex Geometry of Orbits*, arXiv:math/0312268, https://arxiv.org/abs/math/0312268.
