# A universal contact threshold and curvature jump for weighted-wheel Lipschitz ellipsoids

## Finding
Let \(m\ge 3\) be an integer and \(t\ge\tfrac12\). Anchor real-valued Lipschitz functions at the hub of the wheel graph with \(m\) cyclic rim vertices, rim-edge lengths \(1\), and spoke lengths \(t\). In the resulting rim-coordinate Euclidean space, their unit ball is
\[
Q_{m,t}=\{x\in\mathbb R^m:|x_i|\le t,\ |x_i-x_{i+1}|\le1\ (1\le i\le m)\},
\]
with cyclic indices. Put \(\tau=1/\sqrt2\), \(\kappa_m=\pi^{m/2}/\Gamma(1+m/2)\), and let \(L_m\) be the Laplacian of the unit cycle on the rim vertices.

**Exact John ellipsoid and contact transition.** For \(\tfrac12\le t\le\tau\), the unique maximum-volume inscribed ellipsoid is
\[
E_{m,t}=\{x:x^{\mathsf T}(t^{-2}I)x\le1\},\qquad \operatorname{vol}_m(E_{m,t})=\kappa_m t^m.
\]
For \(t>\tau\), there is a unique \(q=q_m(t)\in(0,1)\) satisfying
\[
2t^2(1-q)(1-q^{m-1})=1+q^m.
\]
Define
\[
\alpha=\frac{2(1-q)^2(1-q^{m-1})}{(1+q)(1-q^m)},\qquad
\beta=\frac{2q(1-q^{m-1})}{(1+q)(1-q^m)}.
\]
Then the unique maximum-volume inscribed ellipsoid is
\[
E_{m,t}=\{x:x^{\mathsf T}(\alpha I+\beta L_m)x\le1\},
\]
and its exact anchored-coordinate volume is
\[
\boxed{\operatorname{vol}_m(E_{m,t})=
\kappa_m\left(\frac{1+q}{2}\right)^{m/2}
\left(\frac{1-q^m}{1-q^{m-1}}\right)^{m/2}\frac1{1-q^m}.}
\]
For \(t<\tau\), exactly the \(2m\) signed spoke inequalities touch the ellipsoid. At \(t=\tau\), and for every \(t>\tau\), all \(4m\) signed spoke and rim inequalities touch it.

**Sharp volume-regularity transition.** The function \(F_m(t)=\log(\operatorname{vol}_m(E_{m,t})/\kappa_m)\), defined for \(t\ge\tfrac12\), is continuously differentiable at \(\tau\) but not twice differentiable there. In fact,
\[
F_m'(\tau^-)=F_m'(\tau^+)=\sqrt2\,m,
\qquad F_m''(\tau^-)=-2m,
\qquad F_m''(\tau^+)=-10m.
\]
The second-derivative jump is the universal value \(-8m\), independent of other wheel parameters.

**High-dimensional volume rate.** For every fixed \(t\ge\tfrac12\),
\[
\lim_{m\to\infty}\frac1m\log\frac{\operatorname{vol}_m(E_{m,t})}{\kappa_m}
=\begin{cases}
\log t,&\tfrac12\le t\le\tau,\\[2pt]
\tfrac12\log\left(1-\frac1{4t^2}\right),&t>\tau.
\end{cases}
\]
The limiting function retains the same nonzero curvature jump at \(\tau\).

## Assumptions and scope
The wheel is the shortest-path metric with strictly positive edge lengths \(t\ge\tfrac12\) on spokes and length one on rim edges. These restrictions make the stated edge constraints sufficient: every distance constraint along any shortest path follows from the spoke and rim inequalities. Volumes and ellipsoids are taken in the standard Euclidean norm of the \(m\) rim values after fixing hub value zero. They are **not** asserted to equal intrinsic volumes in a different zero-sum normalization. An ellipsoid of center \(c\) and covariance \(S\succ0\) is \(\{c+S^{1/2}u:\|u\|_2\le1\}\), with volume \(\kappa_m\sqrt{\det S}\). The Laplacian has diagonal entries two, off-diagonal entries minus one for the two cyclic neighbors, and eigenvalues \(\lambda_j=2-2\cos(2\pi j/m)\) for \(0\le j<m\).

## Proof
**1. A feasible two-orbit precision certificate.** Write \(y=t^2\). Seek a positive-definite precision matrix
\[
A=\alpha I+\beta L_m,\qquad \alpha>0,\quad\beta\ge0,\qquad \alpha y+\beta=1.
\]
This last identity is the exact weighted sum of the two types of supporting constraints. When \(y\le\tfrac12\), take \(\alpha=1/y\), \(\beta=0\). Then \(A^{-1}=yI\) has spoke-coordinate variance \(y\) and rim-difference variance \(2y\le1\); thus the radius-\(t\) Euclidean ball lies in \(Q_{m,t}\).

For \(y>\tfrac12\), let \(q\in(0,1)\) solve the scalar equation displayed above. It is unique because
\[
\frac{1+q^m}{2(1-q)(1-q^{m-1})}
\]
is continuous, strictly increasing from \(\tfrac12\) to infinity as \(q\) increases from zero to one. The explicit formulas give \(\alpha>0\), \(\beta>0\), and direct simplification gives \(\alpha y+\beta=1\).

**2. Exact cyclic inverse and all contact equalities.** Let \(C\) denote the cyclic shift on \(\mathbb R^m\). The definitions imply
\[
A=\frac\beta q\bigl((1+q^2)I-q(C+C^{\mathsf T})\bigr).
\]
Expanding the two geometric series, or multiplying directly by \(A\), gives for cyclic distance \(d\in\{0,\ldots,m-1\}\)
\[
(A^{-1})_{i,i+d}=
\frac q\beta\frac{q^d+q^{m-d}}{(1-q^2)(1-q^m)}.
\]
At \(d=0\) the diagonal is
\[
(A^{-1})_{ii}=
\frac{1+q^m}{2(1-q)(1-q^{m-1})}=t^2.
\]
At \(d=1\), subtraction shows
\[
(e_i-e_{i+1})^{\mathsf T}A^{-1}(e_i-e_{i+1})=1.
\]
Consequently the centered ellipsoid \(\{x:x^{\mathsf T}Ax\le1\}\) is feasible and meets **every** signed spoke and rim hyperplane. At the boundary \(y=\tfrac12\), the first construction has both spoke and rim contacts, and below it only the spoke contacts.

**3. Global optimality among all ellipsoids.** Let any inscribed ellipsoid have center \(c\) and covariance \(S\succ0\), without any symmetry assumption. Containment in both opposing spoke halfspaces implies
\[
S_{ii}+c_i^2\le t^2,
\]
and containment in the corresponding signed rim halfspaces implies
\[
(e_i-e_{i+1})^{\mathsf T}S(e_i-e_{i+1})+(c_i-c_{i+1})^2\le1.
\]
(The inequalities follow by averaging the squares of the two extremal support values.) Multiply the spoke bounds by \(\alpha\), the rim bounds by \(\beta\), and sum over all \(m\) vertices and edges. As \(\alpha t^2+\beta=1\), this yields
\[
\operatorname{tr}(AS)+c^{\mathsf T}Ac\le m.
\]
The arithmetic-geometric mean inequality for the positive eigenvalues of \(A^{1/2}SA^{1/2}\) now gives
\[
(\det A\,\det S)^{1/m}\le\frac{\operatorname{tr}(AS)}m\le1.
\]
Therefore \(\det S\le(\det A)^{-1}\), attained by the proposed centered covariance \(S=A^{-1}\). Equality forces \(c=0\) and \(S=A^{-1}\), proving global uniqueness and not merely optimality in a symmetric ansatz.

**4. Determinant and volume.** For \(q>0\), factor the eigenvalues of the cyclic precision matrix using the \(m\)-th roots of unity. Since
\[
\prod_{j=0}^{m-1}(1-qe^{2\pi ij/m})=1-q^m,
\]
one obtains
\[
\det A=(\beta/q)^m(1-q^m)^2.
\]
Substituting the displayed formula for \(\beta\) and \(\operatorname{vol}_m(E)=\kappa_m/\sqrt{\det A}\) proves the exact volume formula. Its \(q\downarrow0\) limit agrees with \(\kappa_m\tau^m\), so the two branches join continuously.

**5. The contact threshold is the sharp curvature singularity.** Set \(y=t^2\) and \(b=\beta\). Along the feasible precision family, \(A(y,b)=((1-b)/y)I+bL_m\) for \(0\le b<1\). Its determinant logarithm is
\[
H_m(y,b)=\sum_{j=0}^{m-1}\log\bigl(1+b(y\lambda_j-1)\bigr)-m\log y.
\]
It is strictly concave in \(b\), tending to minus infinity as \(b\uparrow1\). Its derivative at \(b=0\) equals \(m(2y-1)\). Thus its unique maximizing parameter is \(b=0\) for \(y\le\tfrac12\), and is strictly positive for \(y>\tfrac12\); by the contact identities, this maximizing parameter is the \(\beta\) already constructed.

The cyclic spectral moments are \(\sum_j\lambda_j=2m\) and \(\sum_j(\lambda_j-2)^2=2m\). At \((y,b)=(\tfrac12,0)\), direct differentiation therefore gives
\[
H_{yy}=4m,\quad H_{yb}=2m,\quad H_{bb}=-m/2,
\]
so the right-hand interior optimal parameter has \(db/dy=-H_{yb}/H_{bb}=4\). The optimized \(H_m\) has one-sided second \(y\)-derivatives \(4m\) and \(12m\), respectively. Since \(F_m=-(1/2)\max_bH_m\), the chain rule \(y=t^2\) gives the asserted values \(-2m\) and \(-10m\) of \(F_m''\). The first derivatives agree and equal \(\sqrt2\,m\). In particular the lack of twice differentiability is proved, not inferred from a numerical plot.

**6. Large-dimensional limit.** At a fixed \(t>\tau\), let \(q_m\) be the unique root. The scalar equation and monotonicity show \(q_m\to1-(2t^2)^{-1}<1\). Hence \(q_m^m\to0\) and \(q_m^{m-1}\to0\). Dividing the exact volume logarithm by \(m\) gives \(\tfrac12\log((1+q_m)/2)+o(1)\), which yields the second branch. The first branch is immediate from the exact Euclidean ball. Differentiating these explicit limiting branches verifies the same \(C^1\) but not \(C^2\) threshold.

## Verification
Two standalone scripts accompany this result. `verify.py` uses only the Python standard library to independently evaluate the cycle eigenvalues, coordinate and rim-edge contact variances, determinant identity and boundary spectral moments over 276 parameter configurations and 47 boundary-moment tests. Executing `python3 verify.py` returned `VERIFY_OK 276 parameter configurations and 47 boundary-moment identities`. `verify_unrestricted.py` requires NumPy and SciPy and optimizes a full symmetric positive-definite matrix, without imposing a circulant form, in 20 small-dimensional cases. Executing `python3 verify_unrestricted.py` returned `UNRESTRICTED_OK 20 full symmetric-matrix optimizations`. These sampled checks corroborate the exact argument but cannot prove an infinite family; proof steps 1–6 do so.

## Relationship to prior work
D’Alì, Delucchi and Michałek (2019), *Many Faces of Symmetric Edge Polytopes*, develop the wheel symmetric edge polytope and its combinatorial and lattice geometry (especially Section 4.3); its polar is the relevant unweighted Lipschitz ball. Alexander, Fradelizi, García-Lirola and Zvavitch (2019) provide the general finite Lipschitz-free geometry and volume-product framework. Suliman and Weinstein (2023) connect graph effective resistances and optimal ellipsoid design. A separately published mathematical record, *The exact Löwner ellipsoid and exponential edge-weight stabilization for wheel symmetric edge polytopes*, determines the enclosing ellipsoid of the **unweighted wheel symmetric edge polytope**, equivalently the dual ellipsoid problem only at the unweighted parameter \(t=1\). It is expressly acknowledged as covering that special case. None of these inspected statements gives the weighted-spoke Lipschitz John ellipsoid for all \(t\), its universal contact threshold \(\tau\), or the exact \(C^1\)-but-not-\(C^2\) volume law. Facet descriptions of wheel symmetric edge polytopes by Chen, Davis and Korchevskaia address a different invariant. No uniqueness claim is made merely from searches: an unindexed equivalent weighted formulation remains possible.

## Limitations
The conclusion is specific to uniformly weighted spokes of a wheel and rim lengths one, with \(t\ge\tfrac12\). It does not give a formula for arbitrary nonuniform spoke weights, for graph families beyond wheels, or for intrinsic zero-sum Euclidean normalization. The originality assessment is limited to the inspected records and primary texts; the universal optimal-design background is prior mathematics, not a new contribution. The nonlinear solver checks are finite, subject to floating-point tolerance, and not independent mathematical certification. No independent scientific audit has been performed.

## References
1. A. D’Alì, E. Delucchi and M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193v1, first public October 11, 2019, https://arxiv.org/abs/1910.05193 .
2. S. Alexander, M. Fradelizi, L. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642v1, first public November 24, 2019, https://arxiv.org/abs/1911.10642 .
3. A. Suliman and O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966v1, first public February 12, 2023, https://arxiv.org/abs/2302.05966 .
4. T. Chen, R. Davis and E. Korchevskaia, *Facets and Facet Subgraphs of Symmetric Edge Polytopes*, arXiv:2107.12315v1, first public July 26, 2021, https://arxiv.org/abs/2107.12315 .
5. *The exact Löwner ellipsoid and exponential edge-weight stabilization for wheel symmetric edge polytopes*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-exact-l-wner-ellipsoid-and-exponential-edge-weight-stabiliza--39d62ea47ea0 .
