# Exact Löwner ball and two-class isotropic contacts of derangement matching polytopes

## Finding
For every integer \(n\ge4\), let \(\mathcal D_n\) be the convex hull of all permutation matrices \(P_\pi\) with \(\pi\in\mathfrak S_n\) having no fixed points. This is the perfect-matching polytope of the crown graph obtained by removing a diagonal perfect matching from \(K_{n,n}\). In the ordinary Frobenius metric, put
\[
C_n=\frac{\mathbf1\mathbf1^{\mathsf T}-I_n}{n-1},\quad H_n=\{Y\in\mathbb R^{n\times n}:Y_{ii}=0,\ Y\mathbf1=0,\ \mathbf1^{\mathsf T}Y=0\},\quad d_n=n^2-3n+1.
\]
The **unique minimum-volume enclosing (Löwner) ellipsoid**, measured intrinsically in the affine hull \(C_n+H_n\), is precisely the Euclidean ball
\[
\boxed{L_n=C_n+\sqrt{\frac{n(n-2)}{n-1}}\,B_{H_n}},
\qquad B_{H_n}=\{Y\in H_n:\|Y\|_F\le1\}.
\]
Every derangement permutation matrix is a boundary contact, and **no nonvertex point** of \(\mathcal D_n\) touches the ball.

The key optimality certificate uses only two conjugacy classes. Let \(\mu_0\) be uniform on the \(n\)-cycles, and let \(\mu_1\) be uniform on the cycle type consisting of \(n/2\) transpositions (even \(n\)) or one three-cycle and \((n-3)/2\) transpositions (odd \(n\)). Define
\[
w_n=\begin{cases}(n-3)/d_n,&n\text{ even},\\n/d_n,&n\text{ odd}.\end{cases}
\]
The positive mixture \(\mu=(1-w_n)\mu_0+w_n\mu_1\) satisfies
\[
\boxed{\mathbb E_\mu(P_\pi-C_n)=0,\qquad
\mathbb E_\mu[(P_\pi-C_n)\otimes(P_\pi-C_n)]=\frac{n(n-2)}{(n-1)d_n}\,I_{H_n}}.
\]
This isotropy certificate proves minimum **ellipsoid** volume, a conclusion that does not follow just from the shared vertex radius or the minimum enclosing sphere.

## Assumptions and scope
All integers \(n\ge4\) are included. The affine equations are \(X_{ii}=0\), \(X\mathbf1=\mathbf1\), \(\mathbf1^{\mathsf T}X=\mathbf1^{\mathsf T}\), with off-diagonal entries nonnegative. The support graph is connected, and the row-column incidence constraints have rank \(2n-1\) on \(n(n-1)\) variables; hence \(\dim H_n=n(n-1)-(2n-1)=d_n\). The matrix \(C_n\) is strictly positive in all allowed positions, proving full dimension relative to that affine hull. Permutation matrices, not abstract permutations or nonisometric coordinates, carry the metric.

## Proof
**1. Vertex radius and the two irreducible modes.** Every derangement vertex satisfies
\[
\|P_\pi-C_n\|_F^2=n-\frac{n}{n-1}=\frac{n(n-2)}{n-1}=:R_n^2.
\]
Thus the stated ball contains the convex hull, with every vertex as contact. To show minimum enclosing ellipsoid volume, an isotropic contact design is required, not merely containment.

Write \(H_n=H_n^+\oplus H_n^-\), the symmetric and skew-symmetric zero-margin, zero-diagonal parts, with dimensions \(d_n^+=n(n-3)/2\) and \(d_n^-=(n-1)(n-2)/2\), respectively. Under simultaneous conjugation by \(\mathfrak S_n\), these are the nonisomorphic irreducible real Specht modules indexed by partitions \((n-2,2)\) and \((n-2,1,1)\). This follows by subtracting the trivial and standard subrepresentations from the symmetric unordered-edge representation, and subtracting the standard subrepresentation from the alternating ordered-edge representation. The pair of representations is irreducible and inequivalent for all \(n\ge4\); therefore every conjugacy-invariant covariance has scalar blocks on \(H_n^+\) and \(H_n^-\).

Write \(c_2(\pi)\) for the number of transpositions in the cycle decomposition and define
\[
S_\pi=(P_\pi+P_\pi^{\mathsf T})/2-C_n,\qquad A_\pi=(P_\pi-P_\pi^{\mathsf T})/2.
\]
Their squared Frobenius norms, using \(\operatorname{tr}(P_\pi^2)=2c_2(\pi)\), are
\[
\|S_\pi\|_F^2=\frac{n(n-3)}{2(n-1)}+c_2(\pi),\qquad
\|A_\pi\|_F^2=\frac n2-c_2(\pi).
\]
**2. An exact isotropic mixture.** On the long-cycle class, \(c_2=0\). On the other class the count is \(n/2\) when \(n\) is even and \((n-3)/2\) when \(n\) is odd. Hence the displayed \(w_n\), which satisfies \(0<w_n<1\), gives
\[
\mathbb E_\mu c_2(\pi)=\frac{n(n-3)}{2d_n}.
\]
Inserting this into the preceding identities shows
\[
\mathbb E_\mu\|S_\pi\|_F^2=\frac{R_n^2d_n^{+}}{d_n},\qquad
\mathbb E_\mu\|A_\pi\|_F^2=\frac{R_n^2d_n^{-}}{d_n}.
\]
Both class measures are conjugacy-invariant, so the covariance blocks are scalar and these trace identities force both scalar eigenvalues to be \(R_n^2/d_n\). The mean equals \(C_n\), since the conjugacy action is transitive on ordered off-diagonal positions and every permutation matrix contains exactly \(n\) ones. This proves the stated first- and second-moment certificate.

**3. Global Löwner optimality and contacts.** The standard Löwner contact criterion says that a radius-\(R_n\) ball containing a full-dimensional convex body is its unique minimum-volume enclosing ellipsoid when its contacting boundary admits a probability measure with centered first moment zero and covariance \((R_n^2/d_n)I\). Step 2 supplies precisely this certificate; therefore \(L_n\) is the unique Löwner ellipsoid against all translated or rotated competitors. Every vertex lies on its boundary, while a nonvertex convex combination of distinct vertices lies strictly inside the sphere by strict convexity. 


## Verification
The standalone `verify_derangement_ellipsoids.py` reconstructs the orthogonal zero-margin projection, the relevant conjugacy classes and their weighted covariance. The numerical checker passed for \(n\in\{3,4,5,6,7\}\), with covariance residual below \(2\times10^{-14}\); the theorem itself is for \(n\ge4\), and \(n=3\) is merely a one-dimensional boundary check. The code uses Python 3 and NumPy. Finite tests cannot prove the all-order statement: the complete proof is the representation-theoretic two-class computation and the unrestricted Löwner contact criterion above.

## Relationship to prior work
Johnston, Kayll and Palmer [1] study deranged perfect matchings of the same crown graph, providing the natural object and first-public-source date but no extremal enclosing ellipsoid. Torres [2] provides the general bipartite matching-polytope fractional description; Paffenholz [3] studies face combinatorics of Birkhoff polytopes. Neither those results nor the *already established* Euclidean John (maximum-volume **inscribed**) ball for edge-transitive regular bipartite matching polytopes determines the minimum-volume **enclosing** ellipsoid. Earlier complete-assignment Löwner ellipsoids allow all diagonal entries, while earlier fixed-cardinality partial-assignment theorems explicitly exclude full saturation. Taking a proper zero-diagonal face does not preserve the Löwner ellipsoid or its induced metric optimality. The new result is specifically the exact outer ellipsoid of this face and its positive two-conjugacy-class covariance certificate, not any John-ball formula or a previously known circumsphere radius.

## Limitations
The proof treats the zero-diagonal full-matching family, not general forbidden-edge patterns. It relies on the standard irreducible decomposition of symmetric and alternating pair modules, quoted with a reference. The explicit mixture is a sufficient contact design, not claimed unique. Exact global bibliographic priority cannot be guaranteed; an unindexed theorem under restricted-permutation optimal-design or zero-diagonal transportation-ellipsoid terminology may imply the conclusion. Independent validation has not been performed.

## References
[1] D. Johnston, P. M. Kayll and C. Palmer, *Deranged matchings: proofs and conjectures*, arXiv:2209.11319, first submitted 2022-09-22, https://arxiv.org/abs/2209.11319.

[2] J. C. Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910, first submitted 2023-06-20, https://arxiv.org/abs/2306.11910.

[3] A. Paffenholz, *Faces of Birkhoff Polytopes*, Electronic Journal of Combinatorics 22(1) (2015), P1.67, https://doi.org/10.37236/4499; first arXiv version arXiv:1304.3948.

[4] G. James and A. Kerber, *The Representation Theory of the Symmetric Group*, Addison-Wesley (1981), standard pair-module decompositions.
