# A fifth-degree blind spot in tetrahedral tangential harmonic sampling

## Finding
Let \(u_0=(1,1,1)/\sqrt3\), \(u_1=(1,-1,-1)/\sqrt3\), \(u_2=(-1,1,-1)/\sqrt3\), and \(u_3=(-1,-1,1)/\sqrt3\). Let \(\mathcal H_\ell\) be the complex spherical harmonics of exactly degree \(\ell\) on \(S^2\). At each \(u_i\), sample both independent tangent components of the intrinsic gradient \(\nabla_{S^2}f(u_i)\). The resulting linear map \(T_\ell:\mathcal H_\ell\to\bigoplus_{i=0}^3T_{u_i}S^2\otimes\mathbb C\) has rank
\[
\operatorname{rank}T_\ell=\begin{cases}
0,&\ell=0,\\
3,&\ell=1,\\
5,&\ell=2,\\
6,&\ell=3,\\
8,&\ell=4,\\
5,&\ell=5,\\
8,&\ell\ge6.
\end{cases}
\]
In particular, all eight independent tangent data are achievable at degree four, only five at degree five, and all eight again at every degree at least six. The three missing fifth-degree measurements are given explicitly below.

## Assumptions and scope
The tetrahedron is regular and inscribed in the unit sphere, and all four vertices are measured. Gradients are **intrinsic**, not ambient unconstrained derivatives. The degree is a single, exact spherical-harmonic degree, not a cumulative low-pass band. All ranks are over \(\mathbb C\); their values agree over \(\mathbb R\). Tangent-vector coordinates may use any bases: the rank is basis independent.

For an explicit coordinate version, write the unnormalized sign vector of vertex \(i\) as \((a_i,b_i,c_i)\), and choose tangent directions \(v_{i,0}=(b_i,-a_i,0)\), \(v_{i,1}=(c_i,0,-a_i)\). These vectors are independent and perpendicular to \(u_i\). Order the eight scalar data as \(y=(y_{0,0},y_{0,1},y_{1,0},y_{1,1},y_{2,0},y_{2,1},y_{3,0},y_{3,1})\), where \(y_{i,j}=v_{i,j}\cdot\nabla_{S^2} f(u_i)\). The attainable degree-five data are exactly the solutions of
\[
 y_{0,0}+y_{1,1}+y_{2,0}+y_{2,1}=0,\qquad
 y_{0,0}+y_{1,0}+y_{2,0}+y_{3,0}=0,\qquad
 -y_{0,0}+y_{0,1}-y_{2,0}+y_{3,1}=0.
\]
For degree three, the two independent constraints are
\[
 y_{0,0}-y_{1,0}-y_{2,0}+y_{3,0}=0,\qquad
 -y_{0,1}+y_{1,1}-y_{2,1}+y_{3,1}=0.
\]

## Proof
The scalar spherical-harmonic addition theorem gives, for an orthonormal basis of \(\mathcal H_\ell\), the reproducing kernel \((2\ell+1)P_\ell(u\cdot w)/(4\pi)\), with \(P_\ell\) the Legendre polynomial normalized by \(P_\ell(1)=1\). Differentiating in tangent directions \(v\perp u\) and \(z\perp w\) gives, after dropping the positive factor \((2\ell+1)/(4\pi)\), the Gram entry
\[
 P_\ell'(u\cdot w)(v\cdot z)+P_\ell''(u\cdot w)(v\cdot w)(u\cdot z).
\]
This is a positive-semidefinite Gram matrix of the eight derivative-evaluation functionals, so its rank equals \(\operatorname{rank}T_\ell\). The off-diagonal vertex inner products equal \(-1/3\). On the diagonal, the second term vanishes and \(P_\ell'(1)=\ell(\ell+1)/2\).

Put \(d_\ell=\ell(\ell+1)/2\), \(x_\ell=P_\ell'(-1/3)\), \(z_\ell=P_\ell''(-1/3)\). In the explicitly specified eight tangent directions, the Gram matrix \(G_\ell\) has diagonal \((i=j)\) blocks \(d_\ell[v_{i,h}\cdot v_{i,k}]_{h,k}\) and off-diagonal blocks
\[
 [x_\ell(v_{i,h}\cdot v_{j,k})+z_\ell(v_{i,h}\cdot u_j)(u_i\cdot v_{j,k})]_{h,k}.
\]
Direct exact determinant expansion, with \(d,x,z\) treated as independent indeterminates, gives the universal factorization
\[
 \det G=-\frac{(-3d+3x-4z)^2(-3d+3x+4z)^3(9d+15x+4z)^3}{2187}.
\]
The standalone checker derives this factorization symbolically from the displayed Gram-entry rule; no numerically fitted identity is used.

For degrees zero through twelve, exact rational Legendre recurrence and rational-matrix row reduction give the ranks
\[
 (0,3,5,6,8,5,8,8,8,8,8,8,8).
\]
The first factor vanishes at degree three, the second at degrees two and five, and both at degree one; for all degrees six through twelve, none vanish. At degree zero all gradient data vanish. The checker also constructs independent homogeneous harmonic-polynomial bases for degrees one through six by solving the exact polynomial Laplace equation; the resulting gradient-evaluation ranks agree, establishing the low-degree kernel dimensions independently of determinant factorization. Exact nullspace elimination yields the constraints in the preceding section.

It remains to prove that the determinant cannot vanish at any degree \(\ell\ge13\). The classical Bernstein bound (DLMF 18.14.3 specialized to Legendre polynomials), at \(t=-1/3\), implies \(|P_m(t)|\le 1/\sqrt m\) for every integer \(m\ge1\). From \((1-t^2)P_\ell'(t)=\ell(P_{\ell-1}(t)-tP_\ell(t))\), one obtains
\[
 \frac{|x_\ell|}{d_\ell}\le X_\ell:=\frac9{4(\ell+1)}\left(\frac1{\sqrt{\ell-1}}+\frac1{3\sqrt\ell}\right).
\]
The Legendre differential equation \((1-t^2)P_\ell''(t)-2tP_\ell'(t)+\ell(\ell+1)P_\ell(t)=0\) yields
\[
 \frac{|z_\ell|}{d_\ell}\le\frac34X_\ell+\frac9{4\sqrt\ell}.
\]
For every \(\ell\ge13\), monotonicity and elementary rational-square comparisons give \(X_\ell<1/16\) and \(3/\sqrt\ell<5/6\). Consequently
\[
 \frac{|3x_\ell\pm4z_\ell|}{d_\ell}\le6X_\ell+9/\sqrt\ell<3,\qquad
 \frac{|15x_\ell+4z_\ell|}{d_\ell}\le18X_\ell+9/\sqrt\ell<9.
\]
All three determinant factors are therefore nonzero. This completes the proof for **every** integer degree, not just the finitely computed degrees.

## Verification
Run `python3 verify_tetra.py` in a directory containing the included standalone checker; it requires Python 3 and SymPy. The checker reconstructs all coordinates, factors the generic symbolic Gram determinant, obtains exact rational ranks through degree twelve, and independently computes the degree-one through degree-six gradient maps from homogeneous harmonic polynomials. It checks the rational-square inequalities used in the tail proof. The observed output is `VERIFY_OK` with rank list `[0, 3, 5, 6, 8, 5, 8, 8, 8, 8, 8, 8, 8]`. The classical Bernstein bound is a cited analytic input; its truth is not inferred from a numerical check.

## Relationship to prior work
Differentiated spherical-harmonic addition identities and tangential vector spherical harmonics are classical. Weniger (2005) develops tensor gradients and addition theorems; Bouzas (2011) develops spherical-harmonic projection and tensor identities. Both supply foundational machinery but do not classify the eight tetrahedral derivative measurements by exact degree. Sun, Dong and Huang (2026) study tangential vector-field interpolation through positive-multiplier matrix-valued kernels and smoothness estimates for scattered nodes, not the rank of a single isolated Legendre-degree kernel on these four vertices. Scalar evaluation on a truncated tetrahedral orbit samples different functionals at twelve different nodes and does not imply the present rank law. The exceptional drop at degree five and permanent full rank after degree six are the distinguishing conclusions.

## Limitations
This is a theorem for four tetrahedral vertices, two tangent components per vertex, and a single exact harmonic degree. It does not classify other nodal configurations, give uniform conditioning across degrees, or assert novelty over every unindexed historical calculation. The rank says whether arbitrary tangent data are interpolable, not that a harmonic input is uniquely recoverable when its dimension exceeds eight. No independent external mathematical audit is claimed.

## References
1. E. J. Weniger, *The Spherical Tensor Gradient Operator*, arXiv:math-ph/0505018v1, publicly dated 2005-05-06, especially Sections 2 and 7.
2. A. O. Bouzas, *Addition theorems for spin spherical harmonics. I. Preliminaries*, arXiv:1103.2982v1, publicly dated 2011-03-15, especially the angular-momentum projector and addition-theorem discussion.
3. Z. Sun, L. Dong and B. Huang, *Divergence-free interpolation of tangential vector fields via matrix-valued kernels*, arXiv:2608.05547v1, 2026-08-06, especially Sections 2, 4 and 5.
4. NIST Digital Library of Mathematical Functions, §18.14(i), equation 18.14.3 (classical Bernstein-type inequality for Jacobi/Legendre polynomials), https://dlmf.nist.gov/18.14.E3.
