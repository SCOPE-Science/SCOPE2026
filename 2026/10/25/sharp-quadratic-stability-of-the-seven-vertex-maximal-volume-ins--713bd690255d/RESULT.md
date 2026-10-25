# Sharp quadratic stability of the seven-vertex maximal-volume inscribed four-polytope

## Finding

Let \(\mathcal M=(S^3)^7\), equipped with the product of the standard round metrics, and define
\[
V(P)=\operatorname{vol}_4\bigl(\operatorname{conv}\{p_0,\ldots,p_6\}\bigr).
\]
Take the seven **ordered** unit vectors
\[
\begin{aligned}
p_0&=(1,0,0,0),\\
p_1&=(-1/2,\sqrt3/2,0,0),\\
p_2&=(-1/2,-\sqrt3/2,0,0),\\
p_3&=(0,0,1,0),\quad p_4=(0,0,-1,0),\\
p_5&=(0,0,0,1),\quad p_6=(0,0,0,-1).
\end{aligned}
\]
Write \(P_*=(p_0,\ldots,p_6)\). The sharp global maximum \(V(P_*)=\sqrt3/4\) and the geometry of its maximizers are established in the literature [1,2].

**Theorem.** The Riemannian Hessian \(H=\operatorname{Hess}_{P_*}V\), on the \(21\)-dimensional tangent space of \(\mathcal M\), has the following complete spectrum:

| Eigenvalue | Multiplicity |
|---|---:|
| \(-7\sqrt3/24\) | \(4\) |
| \(-\sqrt3/4\) | \(3\) |
| \(-\sqrt3/6\) | \(2\) |
| \(-\sqrt3/8\) | \(6\) |
| \(0\) | \(6\) |

The kernel is precisely the tangent space to the \(SO(4)\)-orbit of \(P_*\). For ordered configurations \(P\) sufficiently close to this orbit, define
\[
\delta(P)=\min_{R\in SO(4)}\left(\sum_{i=0}^{6}\|p_i-Rp_i^*\|_2^2\right)^{1/2}.
\]
Then, as \(\delta(P)\downarrow0\),
\[
V(P_*)-V(P)\ \ge\ \bigl(\sqrt3/16-o(1)\bigr)\,\delta(P)^2.
\]
The coefficient is optimal: the ratio of the volume deficit to \(\delta(P)^2\) converges to \(\sqrt3/16\) along a smooth family of noncongruent deformations.

## Assumptions and scope

All seven input vectors lie on the unit \(3\)-sphere in \(\mathbb R^4\), with labels fixed. The near-equality statement is **local** near the rotation orbit of \(P_*\); no effective radius of this neighborhood or global stability modulus is asserted. The Hessian uses the product round metric, not a metric on unlabelled vertex sets. The proof also uses exact, finite \(21\times21\) symbolic linear algebra; `verify.py` independently rebuilds that matrix from the geometric definition.

## Proof

**1. Facets and volume formula.** The reference polytope is the free sum of an equilateral triangle and two perpendicular unit line segments. Its twelve facets are the tetrahedra indexed by
\[
\mathcal F=\{(i,i+1\pmod3,j,k):i=0,1,2,\ j\in\{3,4\},\ k\in\{5,6\}\}.
\]
Every nonincident reference vertex lies strictly on the inner side of the corresponding facet hyperplane. Consequently this simplicial face structure persists in a neighborhood of \(P_*\). The origin is interior, and the coherently oriented facet-determinant formula [1, Section 3.1] therefore gives, in that neighborhood,
\[
V(P)=\frac1{24}\sum_{I\in\mathcal F}\epsilon_I\det(p_{i_1},p_{i_2},p_{i_3},p_{i_4}),
\qquad \epsilon_I=\operatorname{sgn}\det(p_{i_1}^*,p_{i_2}^*,p_{i_3}^*,p_{i_4}^*).
\]
Each determinant at \(P_*\) has absolute value \(\sqrt3/2\); thus the twelve facets give \(V(P_*)=12(\sqrt3/2)/24=\sqrt3/4\).

**2. Exact tangent-coordinate Hessian.** Let \(e_0,e_1,e_2,e_3\) be the standard basis of \(\mathbb R^4\), and choose orthonormal tangent bases \(b_{i,1},b_{i,2},b_{i,3}\) at each vertex. At triangle vertices \(p_i=(x_i,y_i,0,0)\), choose
\[
(b_{i,1},b_{i,2},b_{i,3})=((-y_i,x_i,0,0),e_2,e_3);
\]
at the two \(\pm e_2\) vertices use \((e_0,e_1,e_3)\); at the two \(\pm e_3\) vertices use \((e_0,e_1,e_2)\). For \(z_i\in\mathbb R^3\), use the smooth chart
\[
p_i(z_i)=\frac{p_i^*+\sum_a z_{ia}b_{i,a}}{\sqrt{1+\|z_i\|_2^2}}.
\]
The derivative of this chart is an isometry at the origin. If \(D_I\) is the reference determinant of facet \(I\), multilinearity and the denominator expansion yield the entries of the Hessian indexed by vertex \(i\) and tangent coordinate \(a\):
\[
H_{ia,ia}=-\frac1{24}\sum_{I\ni i}|D_I|,
\]
\[
H_{ia,jb}=\frac1{24}\sum_{I\supset\{i,j\}}\epsilon_I\det\bigl(P_I^*[i\mapsto b_{i,a},j\mapsto b_{j,b}]\bigr)
\quad(i\ne j),
\]
and \(H_{ia,ib}=0\) when \(a\ne b\). Here the determinant notation means the indicated two columns are replaced. The gradient consists of the analogous single-column replacement sums and vanishes identically.

**3. Spectrum, checked by exact determinant identity.** Substituting the twelve explicitly listed facets and seven tangent bases gives the symmetric matrix \(H\) with entries in \(\mathbb Q(\sqrt3)\). Exact symbolic computation, reproducible from the displayed formulas by `verify.py`, yields the polynomial identity
\[
\boxed{\det(\lambda I_{21}-H)=
\lambda^6(\lambda+\sqrt3/8)^6(\lambda+\sqrt3/6)^2
(\lambda+\sqrt3/4)^3(\lambda+7\sqrt3/24)^4.}
\]
This verifies all stated eigenvalues with algebraic (not floating-point) arithmetic. There are six linearly independent infinitesimal simultaneous rotations \((Ap_i^*)_i\), with \(A^T=-A\), and their Hessian images vanish because \(V\) is invariant under rotations and the gradient is zero. The above identity shows the zero eigenvalue has multiplicity exactly six, hence the kernel is precisely these infinitesimal rotations.

**4. Sharp local gap.** The smooth compact orbit \(SO(4)\cdot P_*\) has a normal tubular neighborhood in \(\mathcal M\). Its normal Hessian is negative definite; the smallest eigenvalue of \(-H\) on that normal bundle is \(\sqrt3/8\). Taylor expansion in nearest-orbit normal coordinates, uniformly along this compact orbit, gives
\[
V(P_*)-V(P)\ge\tfrac12(\sqrt3/8-o(1))\,d_{\mathcal M}(P,SO(4)P_*)^2.
\]
The ambient squared Euclidean chord distance defining \(\delta(P)^2\) differs from this squared Riemannian distance by a relative \(1+o(1)\), proving the claimed \(\sqrt3/16\) coefficient. Conversely, let \(v\) be a unit eigenvector of \(H\) for \(-\sqrt3/8\) (necessarily perpendicular to the orbit tangent space), and move along the geodesic \(\exp_{P_*}(tv)\). Then \(V(P_*)-V=\sqrt3 t^2/16+o(t^2)\) and \(\delta=t+o(t)\), proving sharpness.

## Verification

Run `python verify.py` with the packages in `requirements.txt`. It checks all twelve facet determinants and the initial volume, constructs every first and second derivative by exact symbolic determinants, verifies the complete factored characteristic polynomial and the six-dimensional rotational kernel, and independently compares the second-order expansion against random small four-dimensional convex hulls computed by a separate hull algorithm. The finite exact matrix identity is the reproducible certificate for the spectrum. Numerical hull comparisons are consistency tests, not proofs of local stability; the last step follows from the normal-slice Taylor theorem.

## Relationship to prior work

Medgyes [1], dated 12 October 2026, proves that the global seven-vertex maximum for unit-sphere-inscribed four-polytopes is \(\sqrt3/4\), using the non-cyclic classification of Horváth and Lángi [2]. Their geometry of the optimizer and the oriented-facet determinant identity are taken as established background, not presented as discoveries here. The added information is the **entire constrained second-variation spectrum**, the exact rotational nullspace and the **sharp local stability constant**. The accessible inspected primary texts do not provide these local statements. Research on volume stability of *different* polytopes does not imply this spectrum or coefficient. Possible older or unindexed second-variation calculations remain a priority risk; database nonmatches do not establish uniqueness.

## Limitations

No effective finite-radius estimate, global quadratic inequality, unlabelled optimal-matching bound, or higher-dimensional analogue is proved. The symbolic determinant identity is an exact finite calculation that readers can replay; it is not a formal proof in a theorem prover. The novelty assessment has not received independent expert review.

## References

[1] Csaba Medgyes, *Inscribed 4-polytopes of maximal volume with seven and eight vertices*, arXiv:2610.26886v1, first posted 2026-10-12. https://arxiv.org/html/2610.26886v1

[2] Ákos G. Horváth and Zsolt Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496, first posted 2014-02-26; published in Monatshefte für Mathematik 181 (2016), 341–354. https://arxiv.org/abs/1402.6496
