# Sharp Lipschitz constants and nonexpansivity for every planar \(\ell_p\) cone

## Finding

Fix a real exponent \(1<p<\infty\) and its Hölder conjugate \(q=p/(p-1)\). For a nonzero real vector \(w=(w_1,w_2)\), set
\[
R_p(w)=\frac{(|w_1|^p+|w_2|^p)^{1/p}\bigl(|w_1|^{q(q-1)}+|w_2|^{q(q-1)}\bigr)^{1/q}}{|w_1|^q+|w_2|^q}.
\]
Let \(u,v\in\mathbb R^2\) be nonzero and linearly independent and \(C=\{su+tv:s,t\ge0\}\). For each \(x\in\mathbb R^2\), let \(P_{p,C}(x)\) minimize \(\|x-y\|_p\) over \(y\in C\). The **exact global Lipschitz constant** is
\[
\boxed{\operatorname{Lip}(P_{p,C})=\max\{1,R_p(u),R_p(v)\}.}
\]
Consequently the map is nonexpansive precisely for \(p=2\), or for \(p\ne2\) when **each** of the boundary rays points along a coordinate axis or one of the two diagonals. Equivalently, both rays must lie in the union of the four lines \(x_1=0\), \(x_2=0\), \(x_1=x_2\), \(x_1=-x_2\).

## Assumptions and scope

All vectors and scalars are real, \(1<p<\infty\), and the ambient norm is \(\|(a,b)\|_p=(|a|^p+|b|^p)^{1/p}\). The generators are linearly independent; thus \(C\) is a closed, pointed, solid convex cone, with exactly two boundary rays, and conversely every closed, pointed, solid planar convex cone has this representation. The generators may have arbitrary signs and unequal coordinate magnitudes. The global Lipschitz norm means the supremum over all distinct pairs of ambient inputs, not a single local derivative. Strict convexity and coercivity give existence and uniqueness of the metric projection.

## Proof

**1. The line metric projection is linear in dimension two.** Define \(J_q(w)=(\operatorname{sgn}(w_i)|w_i|^{q-1})_{i=1}^2\) and
\[
\varphi_w(x)=\frac{J_q(w)\cdot x}{|w_1|^q+|w_2|^q},\qquad \Pi_w x=w\varphi_w(x).
\]
For \(w=(a,b)\), the functional \(h=(b,-a)\) annihilates the line \(L=\mathbb Rw\). Hölder duality gives \(\inf_{y\in L}\|x-y\|_p=|h\cdot x|/\|h\|_q\). Its unique minimizing residual is \((h\cdot x)J_q(h)/\|h\|_q^q\), so the minimizing point equals \(x-(h\cdot x)J_q(h)/\|h\|_q^q=\Pi_wx\). Thus the full-line nearest-point map is the displayed rank-one *linear* operator. Its exact norm, by rank-one duality, is
\[
\|\Pi_w\|_{p\to p}=\|w\|_p\|\varphi_w\|_q=R_p(w).
\]
The identity \(\Pi_w w=w\) gives \(R_p(w)\ge1\).

**2. Four-map selection.** The projection point onto \(C\) either equals the input (if the input is feasible), is the vertex \(0\), or lies in the relative interior of a boundary ray. In the last case, varying along that ray in both directions near the minimizing point is permissible, so it is the full-line minimizer \(\Pi_u x\) or \(\Pi_v x\). Hence at every input,
\[
P_{p,C}(x)\in\{x,0,\Pi_u x,\Pi_v x\}.
\]
The selection is continuous: if \(x_j\to x\), any cluster point of the bounded minimizers minimizes the limit distance by continuity and fixed feasible comparisons, so uniqueness forces convergence to \(P_{p,C}(x)\).

**3. Global upper estimate.** A continuous selection \(F\) of finitely many linear maps \(A_1,\ldots,A_k\) on a finite-dimensional normed space satisfies \(\operatorname{Lip}(F)\le\max_i\|A_i\|\). Indeed, restrict to any affine segment \(z(t)=x+t(y-x)\). For each distinct pair, the vector equality \(A_i z(t)=A_j z(t)\) either holds identically or at at most one parameter \(t\). Between the finitely many nonidentical crossings, the continuous selection cannot switch between unequal maps, so on each resulting interval its increment is one fixed linear increment. Summing the interval bounds yields \(\|F(y)-F(x)\|\le(\max_i\|A_i\|)\|y-x\|\). With the four maps above, this proves \(\operatorname{Lip}(P_{p,C})\le\max\{1,R_p(u),R_p(v)\}\).

**4. Sharpness on both boundary rays.** Fix \(w=u\) and set the other generator to \(v\); the argument for \(w=v\) is identical. Select a nonzero linear functional \(h\) satisfying \(h\cdot u=0\) and \(h\cdot v<0\). Define \(r=J_q(h)\), and take \(x_0=u+r\). Since \(J_p(r)=h\), the convex KKT variational inequality for minimizing \(\|x_0-y\|_p^p/p\) on \(C\) is satisfied strictly in the \(v\) direction at \(y=u\), and with equality in the \(u\) direction. Therefore \(P_{p,C}(x_0)=u\). Moreover, for all sufficiently small changes in \(x_0\), the full-line projection onto \(\mathbb Ru\) has a **positive** ray coefficient, and its residual duality functional remains strictly negative on \(v\); the same KKT conditions imply that the cone projection coincides with \(\Pi_u\) on a neighborhood of \(x_0\). Every direction is available for local perturbation there. Thus \(\operatorname{Lip}(P_{p,C})\ge\|\Pi_u\|=R_p(u)\), and analogously it is at least \(R_p(v)\). Since \(P_{p,C}(x)=x\) throughout the nonempty interior of \(C\), its Lipschitz constant is at least one. These lower bounds prove the displayed exact formula.

**5. Nonexpansivity classification.** For any nonzero \(w\), Hölder's inequality gives \(1=\varphi_w(w)\le\|\varphi_w\|_q\|w\|_p=R_p(w)\). Equality holds precisely when \(\varphi_w\) is an \(\ell_p\)-norming functional for \(w\). The unique norming functional has coordinate magnitudes proportional to \(|w_i|^{p-1}\), while \(\varphi_w\) has coordinate magnitudes proportional to \(|w_i|^{q-1}\). If both coordinates are nonzero, equality therefore requires either \(p=q=2\) or \(|w_1|=|w_2|\). If only one coordinate is nonzero, equality holds for every exponent. Applying this to both boundary generators and the exact formula completes the classification.

## Verification

The accompanying `verify_wedge.py` is a standalone numerical check using Python, NumPy and SciPy. Running `python verify_wedge.py` compares the four-map projection against independent constrained optimization on many randomly oriented cones and tests pairwise Lipschitz bounds, near-boundary sharpness, and the exceptional axis/diagonal directions. It reports `VERIFY_OK independent_optimizations=3675 global_pair_checks=3150 boundary_sharpness_checks=210 max_solver_difference=9.36e-07` with its pinned deterministic seed and ordinary double precision. The proof above is analytic for all real parameters; numerical checks cannot certify uncountably many cases.

## Relationship to prior work

Classical convex projection theory guarantees nonexpansivity in Hilbert geometry. Ivanov's study of convex-hull deviation relates geometric constants to norms of projections onto *hyperplanes*, not onto arbitrary two-dimensional solid cones. Barrios–Ferreira–Németh analyze algorithms and convergence for Euclidean projections onto simplicial cones. Németh–Németh classify order-isotonicity conditions for Euclidean conic projections; this differs from global \(\ell_p\) Lipschitz constants. Domokos–Marsh give algebraic characterizations of conic metric projections in Banach spaces and a supporting-functional criterion; their inspected results do not evaluate the sharp global Lipschitz constant for arbitrary planar wedges. The familiar coordinate orthant and symmetric-wedge cases are included as strict special cases of the two-generator formula, not counted as separate findings.

## Limitations

The statement excludes degenerate single-ray, line-containing, or zero-dimensional cones, higher dimensions, complex scalars and \(p=1,\infty\), for which uniqueness or linearity of the relevant projection can change. It concerns Lipschitz continuity of the nearest-point map, not isotonicity, algorithmic complexity, or optimal **linear** projections. A fully exhaustive historical equivalence search is impossible; the possibility of an older equivalent planar formula remains a bibliographic risk.

## References

- G. Ivanov, *Convex hull deviation and contractibility*, arXiv:1501.02596 (first public version 12 January 2015), especially the link between hyperplane projection Lipschitz constants and convex-hull deviation.
- J. Barrios, O. P. Ferreira and S. Z. Németh, *Projection onto simplicial cones by Picard's method*, arXiv:1503.02757 (first public version 10 March 2015), especially the Euclidean projection model and the associated algorithms.
- A. B. Németh and S. Z. Németh, *Isotonic regression and isotonic projection*, arXiv:1503.08458 (first public version 29 March 2015), particularly the distinctions between projection isotonicity and norm nonexpansivity.
- A. Domokos and M. M. Marsh, *Projections onto cones in Banach spaces*, *Fixed Point Theory* **19** (2018), 167–178, DOI: 10.24193/fpt-ro.2018.1.12, especially the supporting-normal characterization and algebraic conic-projection theorems.
