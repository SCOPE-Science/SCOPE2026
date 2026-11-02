# A sharp horizon reversal for Gauss–Seidel ordering on positive-definite arrowhead systems

## Finding
For a strictly positive-definite real arrowhead matrix with at least two nonzero leaf couplings, the cyclic Gauss–Seidel sweep ordering that is best in worst-case squared energy **after one sweep** becomes strictly worse than a hub-first or hub-last ordering after **every fixed number of at least two sweeps**. In fact, every order has exactly the same asymptotic spectral radius.

Write the normalized squared coupling total as \(R\in(0,1)\). For an ordering let \(s\) be the squared coupling total of the leaves appearing before the hub and put \(p=s(R-s)\). If \(P\) is the one-sweep error operator, and \(\|x\|_A^2=x^{\mathsf T}Ax\), the exact worst-case squared-energy factors are
\[
\begin{aligned}
\rho(P)&=R,\\
\|P\|_A^2&=\frac{R+p+\sqrt{(R+p)^2-4p}}{2},\\
\|P^m\|_A^2&=R^{2m-4}\bigl(R^3+(1-R)^2p\bigr)\qquad(m\ge 2).
\end{aligned}
\]
The first-sweep factor decreases strictly with \(p\), whereas every later factor increases strictly with \(p\). Thus the first-sweep optimum is exactly a partition of leaves whose total squared coupling comes closest to \(R/2\); the later-sweep optimum puts the hub first or last. If all leaf couplings are nonzero, these are disjoint types of orderings. All orderings with the same partition total are tied.

## Assumptions and scope
Let \(\ell\ge2\) and
\[
 A=\begin{pmatrix}a&v^{\mathsf T}\\v&\operatorname{diag}(d_1,\ldots,d_\ell)\end{pmatrix},
 \quad a>0,\quad d_i>0,\quad v_i\ne0.
\]
Define \(c_i=v_i/\sqrt{ad_i}\) and \(R=\sum_{i=1}^\ell c_i^2\). Assume \(0<R<1\), equivalently \(A\) is strictly positive definite. A sweep means exact scalar Gauss–Seidel coordinate minimization once at each vertex, in a permutation \(\pi\); the **same** permutation is used at every subsequent sweep. Each expression above concerns the induced worst-case \(A\)-energy norm over all nonzero initial errors, not the energy of a particular initial vector. No relaxation, numerical rounding, changing permutations, or randomized orders are included.

## Proof
**Diagonal normalization and compression.** Let \(D=\operatorname{diag}(\sqrt a,\sqrt{d_1},\ldots,\sqrt{d_\ell})\). The change of variables \(y=Dx\) transforms the energy to the form with matrix \(\widetilde A=D^{-1}AD^{-1}=\bigl(\begin{smallmatrix}1&c^{\mathsf T}\\c&I\end{smallmatrix}\bigr)\); it conjugates each exact coordinate relaxation. By the Schur complement, its positive definiteness is equivalent to \(R<1\).

Partition the leaves into those before and after the hub, with normalized coupling subvectors \(c_B,c_C\) and squared lengths \(s=\|c_B\|_2^2\), \(t=\|c_C\|_2^2=R-s\). Within either group all leaf updates commute. Leaf-vector directions perpendicular to the coupling vector in their group are \(\widetilde A\)-orthogonal to the active space and are annihilated in one sweep, so they cannot contribute to the operator norm. For nonempty groups, normalized aggregate coordinates reduce the active energy matrix and the sweep to
\[
 H=\begin{pmatrix}1&u&w\\u&1&0\\w&0&1\end{pmatrix},\qquad
 P=\begin{pmatrix}u^2&0&-w\\-u&0&0\\-u^2w&0&w^2\end{pmatrix},
 \quad u^2=s,\ w^2=t.
\]
The coordinate ordering here is (hub, aggregate before hub, aggregate after hub). The displayed operator is obtained by first replacing the before-hub coordinate by \(-u\) times the old hub value, next updating the hub, and last updating the after-hub coordinate. The formulas extend continuously to an empty group. The orthogonal complement is killed by the sweep and therefore contributes zero singular values, justifying exact equality of the full and reduced energy operator norms.

**Spectral and energy calculations.** Direct matrix multiplication, or the characteristic polynomial, gives
\[
\det(\lambda I-P)=\lambda^2(\lambda-R),\qquad P^3=RP^2.
\]
Thus \(\rho(P)=R\). The squared energy singular values are the eigenvalues of \(H^{-1}P^{\mathsf T}HP\). Their characteristic polynomial is
\[
 \lambda\left[\lambda^2-(R+st)\lambda+st\right].
\]
The larger root is exactly the one-sweep formula. Separately, \(P^2\) has rank one, and exact multiplication gives
\[
 \operatorname{tr}\left(H^{-1}(P^2)^{\mathsf T}HP^2\right)
 =R^3+(1-R)^2st.
\]
Since that trace is the sole nonzero squared singular value and \(P^m=R^{m-2}P^2\) for every integer \(m\ge2\), the claimed all-horizon formula follows. These polynomial identities can be independently checked by the included symbolic and direct-matrix verifier.

**Sharp optimization.** Put \(p=st\). The larger quadratic root \(F_1\) is strictly below \(1\) for \(R\in(0,1)\), since a complete exact-coordinate sweep strictly contracts the energy of any nonzero error for a strictly positive-definite matrix. Differentiating its characteristic equation gives
\[
 \frac{dF_1}{dp}=\frac{F_1-1}{\sqrt{(R+p)^2-4p}}<0.
\]
For \(m\ge2\), \(dF_m/dp=R^{2m-4}(1-R)^2>0\). Because \(p=s(R-s)=R^2/4-(s-R/2)^2\), the minimum one-sweep factor is attained by leaf subsets closest to half the total; the minimum for every later horizon is attained exactly at \(s=0\) or \(s=R\) when every \(v_i\ne0\). The discrete permutation choices impose no additional restriction beyond the subset totals, because leaves commute within their groups.

**Unbounded ordering-regret example.** Take two equal nonzero couplings, \(a=d_1=d_2=1\), \(c_1^2=c_2^2=R/2\), with \(0<R<1\). The balanced hub-middle order has \(p=R^2/4\); either endpoint order has \(p=0\). The latter has \(F_1=R\) and \(F_2=R^3\), whereas the balanced order has strictly smaller \(F_1\) but
\[
\frac{F_2(\text{balanced})}{F_2(\text{endpoint})}
=1+\frac{(1-R)^2}{4R}\longrightarrow\infty\quad(R\downarrow0).
\]
For the explicit rational instance \(c_1=c_2=1/4\), \(R=1/8\), the balanced order gives \(F_1=(33+\sqrt{65})/512\) versus endpoint \(1/8\), but \(F_2=81/16384\) versus endpoint \(32/16384\).

## Verification
Run `python verification/verify_star.py` with the packages specified in `requirements.txt`. The checker verifies the reduced symbolic characteristic polynomials, the cubic identity, the rank-one second-power norm, and, on several dimensions and permutations, independently constructs the full Gauss–Seidel matrix and computes the induced energy norm using Cholesky factors. Exact symbolic identities support the theorem; finite enumerations merely cross-check implementation and sample boundary cases. The unbounded ratio and sharp ordering conclusions are algebraic deductions, not inferred from numerical experiments.

## Relationship to prior work
Frommer and Szyld (arXiv:2209.03757, first posted 2022-09-08) analyze randomized/greedy Gauss–Seidel relaxation and convergence estimates for general linear systems; their paper also defines cyclic sequential relaxation. They do not state this star-specific exact repeated-order finite-horizon energy-norm phase reversal. O'Leary (1984) develops orderings for mesh-based Gauss–Seidel/SOR and analyzes spectral convergence and parallel processing. Its ordering and spectral-radius results do not specify the exact \(A\)-energy singular values for all repeated permutations on an arrowhead matrix. Lee and Wright (arXiv:1607.08320, 2016) study cyclic and random-permutation coordinate descent for dense permutation-invariant diagonal-plus-rank-one Hessians, unlike star-sparse fixed-order finite-horizon sharp norms. The classical algebra of spectral radii and positive-definite quadratic coordinate descent is presumed known, and only the combined sharp all-horizon classification is advanced here. This is an independently unreviewed research claim; priority requires further specialized comparison.

## Limitations
The theorem assumes a real strictly positive-definite arrowhead, exact unrelaxed Gauss–Seidel and a fixed order reused at each sweep; it compares worst-case energy after complete sweeps, not runtime, mean performance, pointwise dominance for every starting vector, adaptive orderings, spectral perturbations, or general sparse graphs. Finding the optimum one-sweep subset can still require a weighted partition search. The self-review does not substitute for independent peer review or an exhaustive novelty search.

## References
1. A. Frommer and D. B. Szyld, *On the Convergence of Randomized and Greedy Relaxation Schemes for Solving Nonsingular Linear Systems of Equations*, arXiv:2209.03757 (first public 2022-09-08); https://arxiv.org/abs/2209.03757 ; https://doi.org/10.1007/s11075-022-01431-7 .
2. C.-P. Lee and S. J. Wright, *Random Permutations Fix a Worst Case for Cyclic Coordinate Descent*, arXiv:1607.08320 (2016); https://arxiv.org/abs/1607.08320 .
3. D. P. O'Leary, *Ordering Schemes for Parallel Processing of Certain Mesh Problems*, SIAM J. Sci. Stat. Comput. 5 (1984), 620–632; https://doi.org/10.1137/0905044 ; author-hosted text: https://www.cs.umd.edu/users/oleary/reprints/j18.pdf .
