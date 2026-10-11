# An affine \( (n-1) \)-cube of Euclidean incenters for square Monge polytopes

## Finding
For each integer \(n\ge 2\), the **square Monge polytope** is
\[
\mathcal M_n=\left\{C=(c_{ij})\in\mathbb R_{\ge0}^{n\times n}:\sum_{i,j=1}^n c_{ij}=1,\quad c_{ij}+c_{i+1,j+1}\le c_{i,j+1}+c_{i+1,j}\ (1\le i,j<n)\right\}.
\]
In the Frobenius metric induced on its \((n^2-1)\)-dimensional affine span, put
\[
\alpha_n=\sqrt{1-n^{-2}},\quad T_n=\frac{n^2(n^2-1)}{12},\quad
\rho_n=\frac1{n^2\alpha_n+2T_n}.
\]
Then the exact Euclidean inradius is \(\rho_n\). The **complete incenter locus** consists of the matrices
\[
\boxed{\quad c_{ij}=\rho_n\bigl[\alpha_n+(j-i)(j-i-1)+2(u_i-u_j)\bigr]\quad(1\le i,j\le n),\quad}
\]
where the \(n-1\) independent parameters \(\delta_k=u_k-u_{k+1}\) range through \([0,1]\) for \(1\le k<n\); adding a common constant to all \(u_i\) is immaterial. Consequently the incenter locus is affinely isomorphic to \([0,1]^{n-1}\), has dimension \(n-1\), and has exactly \(2^{n-1}\) vertices. In particular \(\rho_n\sim6n^{-4}\).

Every Monge-type facet is tangent to the ball centered at any incenter. At an incenter with parameters \(\delta\), the number of tangent facets is precisely
\[
(n-1)^2+n+\#\{k:1\le k<n,\ \delta_k\in\{0,1\}\}.
\]
For interior parameters this is \(n^2-n+1\), while at each of the \(2^{n-1}\) incenter-locus vertices it is \(n^2\).

## Assumptions and scope
The entries and affine sum-one normalization are part of the geometric definition; row/column permutations, arbitrary linear isomorphisms, and other scalings need not preserve the Frobenius inradius. No matrix symmetry \(C=C^T\) is imposed. The four-term constraints are the adjacent Monge inequalities, which are equivalent to all Monge inequalities; together with nonnegativity they are precisely the facets, as proved for arbitrary rectangular sizes by Erickson and Kretschmann, Theorem 5.3, arXiv:2311.07522v2. All norms and tangent distances below are **intrinsic to the sum-one affine hyperplane**.

## Proof
**1. Facet distances.** The affine tangent space is \(H=\{X:\sum X_{ij}=0\}\). The orthogonal projection of a coordinate normal \(E_{ij}\) to \(H\) is \(E_{ij}-n^{-2}\mathbf 1\), of norm \(\alpha_n\). An adjacent Monge normal \(E_{ij}+E_{i+1,j+1}-E_{i,j+1}-E_{i+1,j}\) already belongs to \(H\) and has Frobenius norm \(2\). Thus a closed radius-\(r\) ball centered at \(C\in H+\mathbf1/n^2\) lies in \(\mathcal M_n\) exactly when
\[
c_{ij}\ge\alpha_n r\quad(1\le i,j\le n),\qquad
c_{i,j+1}+c_{i+1,j}-c_{ij}-c_{i+1,j+1}\ge2r\quad(1\le i,j<n).
\]

**2. A sharp nonnegative Monge-array inequality.** If \(D=(d_{ij})\ge0\) and all its adjacent Monge slacks are at least \(1\), then
\[
\boxed{\ \sum_{i,j=1}^n d_{ij}\ge T_n=\frac{n^2(n^2-1)}{12}.\ }
\]
Moreover equality holds exactly when
\[
d_{ij}=\tfrac12(j-i)(j-i-1)+u_i-u_j,\qquad
0\le u_k-u_{k+1}\le1\ (1\le k<n).
\]
To prove this, set \(d^0_{ij}=\frac12(j-i)(j-i-1)\). For integral \(i,j\), \(d^0_{ij}\ge0\), and every adjacent Monge slack of \(D^0\) is exactly \(1\). The difference \(E=D-D^0\) satisfies the ordinary Monge inequalities. Its identity assignment is minimum among permutation assignments: whenever a permutation has an inversion, exchanging the two inverted columns weakly decreases the assignment sum, by the Monge inequality. Averaging over all permutations gives
\[
\frac1n\sum_{i,j}E_{ij}\ge\sum_iE_{ii}=\sum_i d_{ii}\ge0.
\]
Also
\[
\sum_{i,j}d^0_{ij}=\frac12\sum_{i,j}(j-i)^2=\frac{n^2(n^2-1)}{12}=T_n,
\]
since \(\sum_{i,j}(j-i)=0\). This proves the bound. At equality all \(d_{ii}\) vanish and every permutation assignment of \(E\) has the same cost as the identity (each is at least the identity and their average is equal to it). Comparing permutations differing by a swap of any two assigned columns forces every two-by-two cross difference of \(E\) to be zero; hence \(E_{ij}=a_i+b_j\). The diagonal equations \(E_{ii}=0\) then force \(b_i=-a_i\). Thus \(E_{ij}=u_i-u_j\). The inequalities \(d_{i,i+1}\ge0\) and \(d_{i+1,i}\ge0\) become respectively \(u_i-u_{i+1}\ge0\) and \(u_i-u_{i+1}\le1\). Conversely, these adjacent bounds imply all other entries nonnegative: for \(j>i\), \(d^0_{ij}\ge0\) and \(u_i-u_j\ge0\); for \(i>j\), with \(h=i-j\), one has \(d^0_{ij}=h(h+1)/2\) and \(u_i-u_j\ge-h\), leaving \(d_{ij}\ge h(h-1)/2\ge0\). All slacks remain exactly \(1\), and the added row-minus-column terms sum to zero. This proves both directions of the equality classification.

**3. Inradius and every center.** At any feasible center of a radius-\(r>0\) ball, put \(D=(C-\alpha_n r\mathbf1)/(2r)\). By step 1, \(D\ge0\) and its Monge slacks are at least \(1\), so step 2 gives
\[
1=\sum c_{ij}=n^2\alpha_n r+2r\sum d_{ij}\ge r(n^2\alpha_n+2T_n).
\]
Thus \(r\le\rho_n\). Conversely, set \(r=\rho_n\) and choose any \(u\) with \(\delta_k\in[0,1]\). The equality arrays from step 2 are feasible and have the necessary sum, so they define ball centers of radius \(\rho_n\). Equality in the upper bound forces the full classification from step 2, proving no additional incenters exist. The parameters can be recovered uniquely from \(c_{i,i+1}=\rho_n(\alpha_n+2\delta_i)\), proving that the locus is an affine \((n-1)\)-cube. Its cube-vertex count and asymptotic inradius follow directly.

**4. Tangent facets.** At every center above, all \((n-1)^2\) adjacent Monge slacks equal \(2\rho_n\). A coordinate facet is tangent exactly when \(d_{ij}=0\). All diagonal entries vanish. For \(j=i+1\), \(d_{i,i+1}=\delta_i\); for \(i=j+1\), \(d_{i+1,i}=1-\delta_i\). Entries farther from the diagonal are strictly positive, since for \(j\ge i+2\), \(d_{ij}\ge (j-i)(j-i-1)/2>0\), and for \(i\ge j+2\), \(d_{ij}\ge(i-j)(i-j-1)/2>0\). The stated tangency formula follows.

## Verification
The standalone Python checker `verify_monge_square.py` uses only the standard library and verifies the quadratic mixed-difference identity, exact sum \(T_n\), every cube-vertex inequality and predicted tangent facet count for \(2\le n\le10\), and all permutation-assignment comparisons for \(2\le n\le6\). A separate numerical linear-programming check with SciPy/HiGHS optimized the full intrinsic inball problem for each \(2\le n\le11\); all values matched the formula (absolute error below \(2\cdot10^{-8}\)). It also independently optimized adjacent superdiagonal coordinates over the optimal face through \(n=7\), confirming the predicted interval endpoints. Finite tests corroborate, but do not replace, the proof of the theorem for every \(n\ge2\).

## Relationship to prior work
Erickson and Kretschmann, arXiv:2311.07522v2, define this normalized Monge polytope and prove its complete irredundant facet system (Theorem 5.3), its vertices/edges, and the two-row normalized-volume formula (Theorem 5.6). These results give the **inequalities used here**, not the Euclidean inradius, the equality classification for the minimum-sum slack array, the full incenter locus, or its tangency counts. Their Section 4 treats distinct symmetric and hollow-symmetric Monge simplices; the present theorem concerns nonsymmetric square matrices. Rudolf and Woeginger (1995) characterize the extreme rays of the nonnegative Monge cone, another combinatorial description that does not directly imply Euclidean balls or their centers. Erickson and Jones, arXiv:2609.09508 (September 2026), study volume and Ehrhart series of the same general Monge family; the available abstract concerns lattice-path/Stanley decompositions rather than Euclidean inballs. The inequality here instead uses the Monge optimal-assignment property and its equality case.

## Limitations
The claim is restricted to the **square** normalized nonsymmetric Monge family with the inherited Frobenius metric; no formula for arbitrary rectangular aspect ratio or non-Frobenius norms is asserted. The result characterizes largest contained balls, not maximum-volume ellipsoids or minimum enclosing balls. The 2026 Erickson–Jones full text could not be inspected, so an undiscovered Euclidean statement in that source remains a low but nonzero coverage risk.

## References
- W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522, first posted 2023-11-13, especially Sections 1, 2, 5 and Theorem 5.3; https://arxiv.org/html/2311.07522v2.
- R. Rudolf and G. J. Woeginger, *The cone of Monge matrices: Extremal rays and applications*, Math. Methods Oper. Res. 42 (1995), 161–168, DOI:10.1007/BF01415751.
- W. Q. Erickson and N. B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508, first posted 2026-09-08 (abstract inspected).
