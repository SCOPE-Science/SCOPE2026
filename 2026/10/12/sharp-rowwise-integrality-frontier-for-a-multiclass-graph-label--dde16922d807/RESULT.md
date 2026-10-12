# Sharp rowwise integrality frontier for a multiclass graph-label penalty

## Finding
Consider the penalty-based, product-of-simplices multiclass graph segmentation objective from Faccio, Porcelli, Rinaldi and Stoll [1]. Its global spectral concavity condition can be replaced by a **sharp, easily evaluated rowwise condition** that ensures local minima are hard labelings. An exact independent-rounding identity simultaneously controls the soft-to-hard energy gap and reaches the nonstrict boundary.

Define \(q_i=(L_s)_{ii}+\omega_i\) and \(M=\max_i q_i\). Whenever \(0<\varepsilon<2/M\), **every** local minimizer is a strict one-hot labeling and the relaxed and hard global-minimizer sets agree. At \(\varepsilon=2/M\), some binary global minimizer still exists, although fractional local minimizers can already occur. For connected graphs with no isolated vertices, \(M=1+\max_i\omega_i\). The uniform coefficient \(2/M\) cannot be increased, even for a connected two-vertex graph with a genuinely labeled vertex and at least three classes.

## Assumptions and scope
Let \(n\ge2\), \(K\ge3\), and let \(L_s\in\mathbb R^{n\times n}\) be the symmetric normalized Laplacian of a finite undirected, nonnegatively weighted graph without isolated vertices. Thus \((L_s)_{ii}=1\). Let \(\omega_i\ge0\) be fixed fidelity weights (equal to a positive common weight on supervised vertices and zero otherwise), and let \(\widehat u_i\) be a specified one-hot label at each supervised vertex. On unsupervised vertices \(\widehat u_i\) is arbitrary because its fidelity weight is zero. The feasible set is \(\Sigma=\prod_{i=1}^n\Delta_{K-1}\), with \(\Delta_{K-1}=\{z\in\mathbb R^K:z_j\ge0,\;\sum_j z_j=1\}\). Let \(u_i\) be row \(i\) of \(U\) and define
\[
E(U)=\frac12\operatorname{tr}(U^\top L_s U)+\frac1\varepsilon\sum_i(1-\|u_i\|_2^2)+\frac12\sum_i\omega_i\|u_i-\widehat u_i\|_2^2.
\]
A **hard labeling** means every row is a standard basis vector. The hard-label objective is the restriction of \(E\) to hard labelings; its penalty is identically zero. Claims about local minima use the usual relative Euclidean topology of \(\Sigma\). The sharpness statement concerns a threshold uniform over all graph instances with the indicated maximum diagonal \(M\), not an exact bifurcation threshold for each individual instance. No algorithmic convergence property is asserted.

## Proof
**1. Strict rowwise concavity forces integrality.** Holding all rows other than row \(i\) fixed, the Hessian with respect to row \(i\) is
\[
\nabla^2_{u_i u_i}E=q_i I_K-2\varepsilon^{-1}I_K.
\]
If \(\varepsilon<2/M\), then this is negative definite for every row. Were a local minimizer to have a row with two positive coordinates, moving a small amount in either direction \(e_a-e_b\) would remain feasible. The affine term would have to vanish by the local first-order condition, while the strictly negative second derivative gives a smaller energy, contradiction. Hence every local minimizer is a hard labeling.

In fact it is **strict**. At a hard-label vertex \(U^*\), every outgoing simplex-edge direction must have a strictly positive first directional derivative: a zero derivative would lead to an energy decrease by its strictly negative rowwise quadratic term. There are finitely many such edge directions. Their positive minimum controls the linear increase for every feasible displacement from \(U^*\) within the tangent cone, and the quadratic remainder is of smaller order. Therefore a sufficiently small nonzero feasible displacement strictly increases \(E\). Global minima exist by compactness; all are hard. Conversely a hard-label global minimizer has the same minimum energy as the relaxed problem, since the latter already attains its minimum at a hard labeling. The minimizer sets coincide.

**2. Exact categorical-rounding identity.** Given any \(U\in\Sigma\), sample the rows of \(V\) independently with \(\mathbb P(V_i=e_j)=(u_i)_j\). Then \(\mathbb EV_i=u_i\), \(\mathbb E\|V_i\|_2^2=1\), and \(\mathbb E(V_i^\top V_j)=u_i^\top u_j\) for \(i\ne j\). Consequently the off-diagonal graph terms are unchanged, the diagonal graph terms gain \(\frac12(L_s)_{ii}(1-\|u_i\|_2^2)\), the fidelity terms gain \(\frac12\omega_i(1-\|u_i\|_2^2)\), and the nonnegative impurity penalty disappears. Thus
\[
\mathbb E E(V)=E(U)-\sum_{i=1}^{n}\left(\varepsilon^{-1}-\frac{q_i}{2}\right)(1-\|u_i\|_2^2). \tag{1}
\]
Some realized hard labeling has energy no greater than the displayed expectation; the standard finite conditional-expectation argument makes the same bound deterministic. If \(E_{\rm hard}^*\) denotes the minimum hard-label energy, then whenever \(0<\varepsilon\le2/M\),
\[
E(U)-E_{\rm hard}^*\ge\sum_i\left(\varepsilon^{-1}-q_i/2\right)(1-\|u_i\|_2^2)\ge0.
\]
Therefore at equality \(\varepsilon=2/M\) at least one relaxed global minimizer is hard. For strict inequality the coefficient on the right is uniformly positive, giving an explicit impurity-based suboptimality certificate. This is an identity for the specified quadratic penalty model, not a claim for arbitrary graph-segmentation regularizers.

**3. Sharp supervised two-vertex boundary.** Let \(n=2\), \(K\ge3\), the graph consist of one unit-weight edge, and set
\[
L_s=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad (\omega_1,\omega_2)=(1,0),\qquad\widehat u_1=e_1.
\]
Then \(M=2\). Let \(x^*=(e_1+e_2)/2\), \(y^*=e_2\), and \(U^*=(x^*,y^*)\). Direct substitution, holding the second row fixed, gives the exact identity
\[
E(x,e_2)=\varepsilon^{-1}+(1-\varepsilon^{-1})\|x\|_2^2+\sum_{j=3}^{K}x_j.
\]
Since \(x^*\) minimizes the squared norm among probability vectors supported on the first two classes, this implies
\[
E(x,e_2)-E(x^*,e_2)=(1-\varepsilon^{-1})\|x-x^*\|_2^2+\varepsilon^{-1}\sum_{j=3}^{K}x_j.
\]
The outward first-order cost for moving the second row from \(e_2\) toward \(e_1\) at \(U^*\) is \(2/\varepsilon-1\); for moving it toward each \(e_j\), \(j\ge3\), it is \(2/\varepsilon-1/2\). Both are positive for \(1\le\varepsilon<2\). By continuity they remain positive uniformly for first rows near \(x^*\). The bounded second-row quadratic remainder then guarantees \(E(x,y)>E(x,e_2)\) whenever \(y\ne e_2\) is sufficiently close and \(x\) is sufficiently close to \(x^*\). Together with the exact first-row identity, this proves that \(U^*\) is a local minimizer throughout \(1\le\varepsilon<2\), strict for \(1<\varepsilon<2\). At \(\varepsilon=1\), the first-row energy is constant as \(x\) varies on the segment from \(e_1\) to \(e_2\), so the minimum is not strict.

Finally, \(E(U^*)=\frac12+\frac{1}{2\varepsilon}>0\), while the hard labeling \((e_1,e_1)\) has energy \(0\). Thus the exhibited fractional local minima are **nonglobal**, not merely alternate global optima. For this graph, the source paper's bound is \(\varepsilon<4/(3+\sqrt5)\), versus the new sharp uniform bound \(\varepsilon<1\). At \(\varepsilon=4/5\), the full \(2\times2\) Hessian factor \(L_s+D_\omega-2\varepsilon^{-1}I\) has negative determinant \(-1/4\), so this improvement cannot be obtained merely by applying the paper's full strict-concavity argument.

## Verification
The accompanying standard-library script `verify_exact.py` tests the categorical-rounding identity in exact fractions for a range of soft two-vertex inputs and penalty values; enumerates all nine hard two-vertex, three-class labelings in its witness instance; verifies local first-order gaps, the equality-boundary flat segment and the spectral-Hessian gap; and prints `VERIFY_OK`. These finite checks are independent corroboration of selected calculations, not a substitute for the analytic proof of the universal statements. For more than three classes, the proof uses identical computations for each additional class.

## Relationship to prior work
Faccio et al. [1, Theorem 2.3, Appendix C] use global strict concavity of the full quadratic energy to obtain one-hot local/global minimizers under \(\varepsilon<2/\lambda_{\max}(L_s+D_\omega)\). The present analysis exploits the independent row-simplex constraints, replaces the full spectral threshold with a larger coordinatewise one, quantifies rounding error, and supplies a supervised equality-boundary obstruction. The global concavity bound is sufficient but not necessary for local integrality. Earlier exact quadratic relaxations and diagonal curvature tests appear in Hager and Krylyuk [2, Theorems 2.1 and 6.1, Corollary 6.2] and in Holtz et al. [3, Proposition 3.2]. Their models impose prescribed class cardinalities/column sums and use different quadratic objective matrices; those results establish the background integrality strategy, but do not state this energy-specific bound, rounding identity, or two-vertex boundary witness. The elementary possibility of rowwise perturbations and categorical rounding is not itself claimed as new.

## Limitations
This is a theorem about energy minimizers of the precise unconstrained-row (other than simplex) quadratic labeling relaxation, not a guarantee that an iterative solver reaches a local minimizer, and not a guarantee of good classification accuracy. It does not cover prescribed nontrivial class-size or balance constraints that couple rows. The sharpness is instance-uniform with fixed \(M\); individual graphs may retain binary local minima above the threshold. The claimed originality concerns the concrete strengthened threshold, quantitative identity and sharp supervised witness, not generic diagonal-concavity reasoning; unseen equivalent prior work is an acknowledged possibility.

## References
[1] C. Faccio, M. Porcelli, F. Rinaldi, M. Stoll, *Fast and Simple Multiclass Data Segmentation: An Eigendecomposition and Projection-Free Approach*, arXiv:2508.09738v1 (public 2025-08-13); SIAM J. Math. Data Sci. 8 (2026), 495–519, DOI 10.1137/25M1787719. Relevant full-text material: equations (2.7)–(2.12), Theorem 2.3, Appendix C.

[2] W. W. Hager and Y. Krylyuk, *Graph Partitioning and Continuous Quadratic Programming*, SIAM J. Discrete Math. 12 (1999), 500–523, DOI 10.1137/S0895480199335829. Relevant full-text material: Theorems 2.1 and 6.1, Corollary 6.2, pp. 502–504 and 517–521.

[3] C. Holtz, P. Chen, Z. Wan, C.-K. Cheng, G. Mishne, *Continuous Partitioning for Graph-Based Semi-Supervised Learning*, NeurIPS 37 (2024), DOI 10.52202/079017-0182. Relevant full-text material: Proposition 3.2 and its proof.
