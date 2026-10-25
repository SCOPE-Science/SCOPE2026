# Exact two-level Hessian spectrum and sharp stability of inscribed regular simplices

## Finding
For every integer \(d\ge2\), set \(N=d+1\) and let \(\mathcal M=(S^{d-1})^N\) carry the product of the standard round metrics. For \(X=(x_1,\ldots,x_N)\in\mathcal M\), put
\[
V(X)=\operatorname{vol}_d\operatorname{conv}\{x_1,\ldots,x_N\},\qquad
V_*=\frac{N^{N/2}}{d!\,d^{d/2}}.
\]
Fix any ordered regular simplex \(U=(u_i)_{i=1}^N\) with \(u_i\cdot u_j=-1/d\) for distinct indices. The set \(\mathcal O\) of all maximizers is exactly its orthogonal orbit \(\{(Qu_i)_{i=1}^N:Q\in O(d)\}\). At any point of \(\mathcal O\), the full Riemannian Hessian of the deficit \(V_*-V\) has spectrum
\[
\boxed{\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\
0&d(d-1)/2\\
V_*&d\\
2dV_*/(d+1)&(d+1)(d-2)/2
\end{array}}
\]
with the last branch absent for \(d=2\). The nullspace is precisely the tangent space to \(\mathcal O\); hence the orbit is a Morse–Bott nondegenerate manifold of global maxima.

Writing \(r=\operatorname{dist}_{\mathcal M}(X,\mathcal O)\), as \(r\downarrow0\) the sharp uniform distance bounds are, for \(d\ge3\),
\[
\frac{V_*}{2}r^2-O_d(r^3)\le V_*-V(X)\le
\frac{dV_*}{d+1}r^2+O_d(r^3).
\]
Both leading coefficients are attained as directional limits along suitable normal geodesics. For \(d=2\) both sharp coefficients are \(V_*/2\). In particular the complete local volume-rigidity spectrum has only two nonzero levels in every dimension.

## Assumptions and scope
Each vertex is constrained separately to the Euclidean unit sphere, with labels retained and distances measured in the Riemannian product of round spheres. The dimension \(d\) is fixed, and the statement is local near the complete labelled maximizing orbit, not a bound with a specified radius for every configuration. At a degenerate simplex its volume is continuous but its determinant expression may change sign; the differential statements use only a neighborhood of \(\mathcal O\), where a fixed sign gives smoothness.

## Proof
**Global maximum and its equality set.** Form the \(d\)-by-\(N\) matrix \(X\) with the vertices as columns. Orthogonally change its column coordinates so that the last basis vector is \(N^{-1/2}(1,\ldots,1)\); write the transformed matrix as \((Y,c)\), with \(Y\) square of order \(d\). Expanding the augmented affine determinant gives
\[
d!\,V(X)=\sqrt N\,|\det Y|\le\sqrt N\bigl(\|Y\|_F^2/d\bigr)^{d/2}
\le\sqrt N(N/d)^{d/2}.
\]
The first inequality is arithmetic–geometric mean for the singular values, and the second uses \(\|Y\|_F^2+\|c\|^2=\sum_i\|x_i\|^2=N\). Equality demands \(c=0\) and \(YY^{\mathsf T}=(N/d)I\), which is equivalent to the Gram matrix of a regular simplex. Thus the maximizing set is exactly \(\mathcal O\), of dimension \(d(d-1)/2\).

**Coordinates on the tangent space.** At \(U\), let \(P_i=I-u_iu_i^{\mathsf T}\). Because
\[
\sum_i u_i=0,\qquad \sum_i u_iu_i^{\mathsf T}=\frac Nd I,
\]
every tangent array \(w_i\perp u_i\) is uniquely of the form
\[
w_i=A u_i+P_iS u_i,
\]
where \(A^{\mathsf T}=-A\), \(S^{\mathsf T}=S\), and \(\operatorname{tr}S=0\). Indeed, the map from trace-free real matrices \(T\) to \((P_iTu_i)_i\) is injective: a matrix preserving each vertex ray has all its vertex eigenvalues equal, since \(\sum_i u_i=0\) is their unique linear dependence with every coefficient nonzero. Dimension equality proves surjectivity. The skew and symmetric components are perpendicular for the product-sphere metric; skew components are the infinitesimal rotations.

Put \(q_i=u_i^{\mathsf T}Su_i\). Then \(\sum_iq_i=0\), and for the symmetric modes the squared metric norm is
\[
G(S,S)=\sum_i\|P_iSu_i\|^2
=\frac Nd\operatorname{tr}(S^2)-\sum_iq_i^2.
\]

**Exact second variation.** Define the \(N\)-by-\(N\) augmented matrix \(M(U)\) with rows \((1,u_i^{\mathsf T})\). Its inverse has \(i\)-th column \((1/N,(d/N)u_i)\). Along the product-sphere geodesic with velocity \(w_i\), the acceleration at zero is \(-\|w_i\|^2u_i\). Differentiating \(-\log|\det M|\) twice and using \(u_i\cdot w_i=0\) gives
\[
D^2(-\log V)[w,w]=\frac dN\sum_i\|w_i\|^2+
\left(\frac dN\right)^2\sum_{i,j}(u_i\cdot w_j)(u_j\cdot w_i).
\]
For \(w_i=P_iSu_i\), write \(K=\sum_i u_iw_i^{\mathsf T}=(N/d)S-\sum_i q_i u_iu_i^{\mathsf T}\). The regular-simplex Gram matrix gives
\[
\operatorname{tr}(K^2)=\left(\frac Nd\right)^2
\left(\operatorname{tr}(S^2)-\sum_iq_i^2\right).
\]
Therefore the Hessian bilinear form, by polarization, is
\[
H(S,T)=2\operatorname{tr}(ST)-\frac{2d+1}{N}
\sum_i (u_i^{\mathsf T}Su_i)(u_i^{\mathsf T}Tu_i).
\]
The orbital directions have zero Hessian and, by rotational invariance at a critical point, no cross term with the symmetric directions.

**Diagonalization without a numerical spectral assumption.** The map \(S\mapsto(q_i)_i\) on trace-free symmetric matrices has rank \(d\), since its adjoint is spanned by \(E_i=u_iu_i^{\mathsf T}-I/d\), whose only linear relation is \(\sum_iE_i=0\). On its Frobenius-orthogonal kernel, \(G=(N/d)\operatorname{tr}(S^2)\) and \(H=2\operatorname{tr}(S^2)\), giving eigenvalue \(2d/N\) and multiplicity \((d+1)(d-2)/2\). On the \(d\)-dimensional span of the \(E_i\), direct use of \(u_i\cdot u_j=-1/d\) yields
\[
\sum_iq_i^2=\frac{N(d-1)}{d^2}\operatorname{tr}(S^2),
\qquad G=H=\frac N{d^2}\operatorname{tr}(S^2).
\]
This gives eigenvalue \(1\) with multiplicity \(d\). Since \(V\) is critical at \(U\), the Hessian of \(V_*-V\) is \(V_*\) times the Hessian of \(-\log V\). This proves every eigenvalue and multiplicity.

**Sharp distance stability.** The compact embedded orbit has a smooth tubular neighborhood in \(\mathcal M\). At points \(X=\exp_U(n)\) with \(n\) normal and sufficiently small, \(r=\|n\|\), uniformly in \(U\). Taylor's theorem, compactness, and the computed transverse spectrum give
\[
V_*-V(X)=\tfrac12\operatorname{Hess}_U(V_*-V)[n,n]+O_d(r^3).
\]
The minimum normal eigenvalue is \(V_*\) and the maximum is \(2dV_*/N\) (or \(V_*\) when \(d=2\)); unit eigenvectors and their normal geodesics attain the corresponding quadratic limits.

## Verification
A reproducible numerical checker is included as `verify.py` (run `python verify.py` after installing `requirements.txt`). It constructs orthonormal regular simplices numerically, computes the Gram and log-volume second-variation forms directly, and checks all generalized eigenvalues and multiplicities for \(d=2,3,4,5,6\). It also compares the analytic quadratic form against central finite differences of the determinant along independently sampled unit-sphere geodesics. These finite checks do **not** prove the all-dimensional theorem: the analytic rank, Gram, and Hessian calculations above do.

## Relationship to prior work
Horváth and Lángi (2014) identify the regular simplex as the volume maximizer among inscribed simplices (Corollary 1) and develop first-order optimality conditions for more-vertex polytopes. Medgyes (2026) proves maximality for seven- and eight-vertex four-polytopes by exact certificates. Neither analyzed the complete product-sphere Hessian at the \(d+1\)-vertex simplex or its two nonzero spectral levels. Grote, Kabluchko, and Thäle (2017) derive extensive spherical random-simplex volume laws and moments; these concern the marginal scalar volume distribution, not the orientation-resolved geometric Hessian or sharp local distance-to-orbit constants. The result is a differential refinement of established maximum-volume geometry, not a new claim of the maximum itself or of a random-volume law.

## Limitations
The improvement concerns the intrinsic Riemannian metric on the product of spheres; coefficients change with a different metric or normalization. The neighborhood size and the cubic-error constant are not explicit. No global quadratic modulus is asserted. Numerical checks are finite-dimensional corroboration only; complete historical priority cannot be guaranteed by a finite literature search. The claim does not assert an independently certified proof.

## References
1. C. Medgyes, *Inscribed 4-polytopes of maximal volume with seven and eight vertices*, arXiv:2610.26886v1 (public 2026-10-12), https://arxiv.org/abs/2610.26886.
2. Á. G. Horváth and Z. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496v3 (2014), https://arxiv.org/abs/1402.6496.
3. J. Grote, Z. Kabluchko and C. Thäle, *Limit theorems for random simplices in high dimensions*, arXiv:1708.00471v1 (2017), https://arxiv.org/abs/1708.00471.
