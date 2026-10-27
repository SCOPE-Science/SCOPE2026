# Optimal distributed pinning creates exact central plateaus in discrete Dirichlet Sobolev inequalities

## Finding
Let \(d\geq1\) be an integer and \(\Lambda\geq0\). For \(w_j\geq0\) with \(\sum_{j=1}^{d}w_j=\Lambda\), define the sharp squared constant \(C_d(w)^2\) in
\[
\sum_{j=1}^{d}|a_j|\leq C_d(w)\left(\sum_{j=1}^{d+1}|a_j-a_{j-1}|^2+\sum_{j=1}^{d}w_j|a_j|^2\right)^{1/2},\quad a_0=a_{d+1}=0,
\]
for all complex \(d\)-tuples. The minimizer over all such pinning budgets is unique. Its strictly positive pinning coordinates form a centered contiguous block; the optimal Green (torsion) vector is constant on that block and a discrete parabola elsewhere. The block grows through explicitly known thresholds as the budget increases.

More precisely set \(M=\lfloor(d+1)/2\rfloor\), \(t_1=+\infty\), \(t_{M+1}=0\), and for \(2\le m\le M\) set
\[
t_m=\frac{2(d+2-2m)}{m(m-1)}.
\]
For \(\Lambda\geq0\), choose any integer \(1\le m\le M\) such that \(t_{m+1}\le\Lambda\le t_m\). At a shared threshold either adjacent choice yields the same minimizer and constant. Write \(H=(d+1-m)/(\Lambda+2/m)\). Then
\[
\boxed{\min_{w_j\ge0,\ \sum w_j=\Lambda} C_d(w)^2
=\frac{m(m^2-1)}6+\frac{(d+1-m)^2}{\Lambda+2/m}.}
\]

The unique optimal weights are explicit. Set \(g_0=g_{d+1}=0\) and for \(1\le j\le d\), with \(i=\min\{j,d+1-j\}\), put
\[
g_j=\begin{cases}\dfrac{i(m-i)}2+\dfrac{iH}{m},&i<m,\\[3pt]H,&i\ge m.\end{cases}
\qquad
\boxed{w_j=\frac{1-2g_j+g_{j-1}+g_{j+1}}{g_j}.}
\]
These weights are nonnegative, sum to \(\Lambda\), and vanish off \(m\le j\le d+1-m\). Within this central interval, some endpoint weights may vanish exactly at transition budgets. The optimizing sequence in the sharp inequality has constant complex phase and magnitudes proportional to \(g_j\).

For example, with \(d=3\), the squared sharp constant is \(1+4/(\Lambda+1)\) for \(0\le\Lambda\le1\) (only the middle coordinate is pinned for positive budgets) and \(9/(\Lambda+2)\) for \(\Lambda\ge1\) (the outer coordinates become pinned above the threshold). The zero-budget identity is \(C_d(0)^2=d(d+1)(d+2)/12\); for \(\Lambda\ge d-2\) the optimal Green vector is flat everywhere and the squared constant is \(d^2/(\Lambda+2)\).

## Assumptions and scope
The lattice is the unweighted finite path of \(d\) interior sites with two zero Dirichlet boundary values; both boundary difference terms are present. The budget is the sum of nonnegative real onsite quadratic penalties. The inequality concerns complex sequences, with no restriction on phases, and the optimization is over *all* such nonnegative penalties, not only symmetric ones. No claim is made about higher differences, other graphs, or nonquadratic energies.

## Proof
**1. Exact inverse representation.** Let \(L\) denote the positive Dirichlet path matrix with diagonal entries \(2\) and nearest-neighbor entries \(-1\), and put \(A_w=L+\operatorname{diag}(w)\). It is positive definite. Its inverse is entrywise strictly positive: if \(A_wx=f\) with \(f\ge0\), the minimum principle implies \(x\ge0\), and irreducibility propagates strict positivity for nonzero \(f\). In particular \(g=A_w^{-1}{\bf1}\) has \(g_j>0\).

By duality for the \(\ell^1\) norm and Cauchy--Schwarz in the \(A_w\) inner product,
\[
C_d(w)^2=\max_{|\zeta_j|=1}\zeta^*A_w^{-1}\zeta={\bf1}^*A_w^{-1}{\bf1}=\sum_{j=1}^{d}g_j.
\]
Entrywise positivity gives the middle equality. Equality is realized by \(a=g\), up to a common phase and nonzero scale.

**2. Strict convexity and the optimality conditions.** Define \(F(w)={\bf1}^*A_w^{-1}{\bf1}\). Matrix differentiation, justified because \(A_w\) remains positive definite, gives
\[
\partial_{w_i}F=-g_i^2,\qquad
\nabla^2 F=2\operatorname{diag}(g)A_w^{-1}\operatorname{diag}(g).
\]
The Hessian is strictly positive definite because every \(g_i>0\), so \(F\) is strictly convex on the nonnegative orthant. The fixed-budget simplex is compact; its minimizer therefore exists and is unique. Reflection invariance makes it reflection-symmetric. If \(\Lambda>0\), the Karush--Kuhn--Tucker conditions state that for some \(H>0\),
\[
w_i>0\implies g_i=H,\qquad w_i=0\implies g_i\le H.
\]
(The scalar multiplier of the budget constraint equals \(H^2\).) These conditions are sufficient by convexity.

**3. A connected central plateau.** Suppose two positively pinned coordinates enclose an unpinned coordinate. On each gap of unpinned sites the equation \((Lg)_j=1\) makes \(g\) strictly discretely concave, so a sequence whose endpoints equal \(H\) lies strictly *above* \(H\) in the gap. This contradicts the KKT inequality. Thus positive pinning sites form one contiguous interval. Reflection invariance forces it to be centered. On the unpinned tails, the boundary condition \(g_0=0\), the equality \(g_m=H\), and \((Lg)_j=1\) give, uniquely,
\[
g_j=\frac{j(m-j)}2+\frac{jH}{m}\quad(0\le j<m).
\]
Reflection yields the opposite tail. The Green vector must equal \(H\) on the central interval.

**4. Recovering budget and locating transitions.** On the central plateau set \(w_j=[1-(Lg)_j]/H\); it is zero off the plateau. Summing \(A_wg={\bf1}\) over interior sites, using \(\sum_{j=1}^{d}(Lg)_j=g_1+g_d=2g_1\), gives \(\Lambda H=d-2g_1\). Since \(g_1=(m-1)/2+H/m\), this is exactly
\[
H=\frac{d+1-m}{\Lambda+2/m}.
\]
The last unpinned site is at most \(H\) if and only if \(H\ge m(m-1)/2\), equivalently \(\Lambda\le t_m\) when \(m\ge2\). Nonnegativity of the first plateau pin is equivalent to \(H\le m(m+1)/2\) whenever there are at least two plateau sites, equivalently \(\Lambda\ge t_{m+1}\). When the plateau is a single center site (odd \(d\), \(m=M\)), the condition instead is \(H\le m^2/2\), equivalent to \(\Lambda\ge0=t_{M+1}\). For \(m=1\) there are no unpinned sites and the only restriction is \(\Lambda\ge t_2=d-2\) when \(d\ge3\); the same formula works for \(d=1,2\). Thus these explicit formulae satisfy every KKT condition and therefore uniquely solve the global optimization.

**5. Sharp value and transitions.** The quadratic tails contribute \(m(m^2-1)/6\) to \(\sum_jg_j\). The remaining plateau and tail boundary interpolation together contribute \((d+1-m)H\), yielding the boxed constant. At \(t_m\), direct substitution shows adjacent candidate profiles coincide. At zero budget, the unique optimal vector has no onsite penalty and the stated unpinned constant follows by summing its discrete parabola. These identities prove the classification for every integer \(d\ge1\), every real \(\Lambda\ge0\), and arbitrary complex sequences.

## Verification
The accompanying `CHECKER.py` independently assembles and inverts the finite Dirichlet matrices and compares the formulas with computed torsion profiles and nonlinear constrained optimizations for dimensions \(1\) through \(19\), including both sides of every internal budget threshold. It passed \(2,261\) finite diagnostic assertions. The computer tests are checks of calculations, not a substitute for the exact convexity/KKT proof, which works uniformly for every finite dimension and continuous budget.

## Relationship to prior work
Hindov, Nitzan, Olsen and Rydhe (arXiv:2610.19010v1, October 13, 2026) prove the unpinned discrete \(\ell^1\)-to-difference-\(\ell^2\) inequality for all orders and provide its exact constant; specializing their result to first differences recovers this theorem's \(\Lambda=0\) case. The *optimization of spatially allocated quadratic pinning under a total budget*, its exact rational value, and the central-plateau growth thresholds are separate from that unpinned theorem. Work on graph pinning by Liu et al. (arXiv:1804.10818) and Wang et al. (arXiv:2110.12576) optimizes grounded-Laplacian eigenvalue or vertex selection rather than the inverse-Laplacian \(\ell^1\) embedding constant under a continuous pinning budget. The general matrix inverse-derivative principle is classical; the claimed contribution is its complete special-path, all-budget solution, not the principle itself.

## Limitations
The result applies to first differences with fixed Dirichlet endpoints and linear penalty budget; no higher-order or multidimensional classification is asserted. The proof establishes strict convexity and uniqueness *within the stated model*, but does not assert bibliographic uniqueness. Prior literature on optimal compliance, torsional rigidity and point interactions may contain related or equivalent all-budget formulations; independent priority and mathematical review are still required. Computer diagnostics do not certify an infinity of dimensions and are not used as such.

## References
- R. Hindov, S. Nitzan, J.-F. Olsen and E. Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1 (first public October 13, 2026), https://arxiv.org/html/2610.19010v1.
- Y. Liu et al., *Optimizing Pinning Control of Complex Dynamical Networks*, arXiv:1804.10818 (2018), https://arxiv.org/abs/1804.10818.
- X. Wang et al., *Maximizing the Smallest Eigenvalue of Grounded Laplacian Matrix*, arXiv:2110.12576 (2021), https://arxiv.org/abs/2110.12576.
- D. Bucur, G. Buttazzo and B. Velichkov, *Spectral Optimization Problems for Potentials and Measures*, SIAM J. Math. Anal. 46 (2014), 2956--2986, DOI:10.1137/130939808 (related potential-optimization context; not asserted to be entirely inspected).
