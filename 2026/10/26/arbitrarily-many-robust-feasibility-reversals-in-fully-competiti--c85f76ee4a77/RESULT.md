# Arbitrarily many robust feasibility reversals in fully competitive Lotka–Volterra communities

## Finding

For every integer \(n\ge2\), there is an **open set of completely interacting competitive communities** whose positive equilibrium alternately exists and does not exist as the uniform strength \(\alpha>0\) of self-limitation increases. If \(k=\lfloor n/2\rfloor\), the feasible parameter set has **at least \(k+1\) connected components** and is separated by at least \(k\) open infeasible intervals. Each of the first \(k\) feasible witnesses supports a hyperbolically unstable positive equilibrium, while the final witness supports an equilibrium that attracts every strictly positive initial population state.

The number of feasible components thus grows without bound with the number of species even when **all off-diagonal competition coefficients are strictly positive**, and even after perturbing those coefficients in an open neighborhood. The result concerns *existence* of positive equilibria (feasibility), not stability throughout whole feasible intervals.

## Assumptions and scope

The system consists of \(n\ge2\) interacting populations with densities \(x_i(t)>0\):
\[
\dot x_i=x_i\left(1-\alpha x_i-\sum_{j\ne i}B_{ij}x_j\right),\qquad i=1,\ldots,n.
\]
Here \(\alpha>0\), \(B_{ii}=0\), and \(B_{ij}>0\) whenever \(i\ne j\). Uniform intrinsic growth \(1\) is chosen for the stability statement; feasibility is unaffected if each right side is multiplied by any fixed positive intrinsic growth rate. A *feasible equilibrium* means a vector \(x^*\) with **every coordinate strictly positive** satisfying
\[
(\alpha I+B)x^*=\mathbf1.
\]
A *feasibility component* means a connected component in the one-dimensional parameter set \(\{\alpha>0: (\alpha I+B)x=\mathbf1\text{ for some }x>0\}\). We assert a lower bound on its number, not an upper bound or a complete interval census for perturbed matrices.

## Proof

**Step 1: a paired-community identity.** For \(0<c<b\), the positive-equilibrium equations on a two-species block are
\[
\begin{pmatrix}\alpha&b\\c&\alpha\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
=\begin{pmatrix}1\\1\end{pmatrix}.
\]
When \(\alpha^2\ne bc\), their sole solution is
\[
(x,y)=\left(\frac{\alpha-b}{\alpha^2-bc},\frac{\alpha-c}{\alpha^2-bc}\right).
\]
It is positive for \(0<\alpha<c\) and for \(\alpha>b\); it is **not** positive for \(c\le\alpha\le b\). At the two endpoints a coordinate vanishes. At the singular parameter \(\alpha=\sqrt{bc}\), the equations are inconsistent because the second row is \(c/\alpha\) times the first row, whereas their right sides are both \(1\) and \(c/\alpha\ne1\). At all other interior gap values the solution has mixed coordinate signs. Thus the pair alone undergoes feasible–infeasible–feasible re-entry.

**Step 2: concatenate disjoint gaps.** Write \(n=2k+r\) with \(r\in\{0,1\}\). Let \(B^0\) be block diagonal, with \(k\) blocks
\[
\begin{pmatrix}0&b_j\\c_j&0\end{pmatrix},
\qquad c_j=4j-3,\quad b_j=4j-2,\quad 1\le j\le k,
\]
and, when \(r=1\), one singleton block \((0)\). Define the increasing *feasible* test parameters
\[
a_0=\tfrac12,\quad a_j=\tfrac{b_j+c_{j+1}}2=4j-\tfrac12\ (1\le j<k),\quad a_k=b_k+1=4k-1,
\]
and the increasing *infeasible* parameters
\[
\beta_j=\tfrac{c_j+b_j}2=4j-\tfrac52,\qquad1\le j\le k.
\]
They interlace: \(a_0<\beta_1<a_1<\dots<\beta_k<a_k\). At every \(a_j\), each earlier pair is in its \(\alpha>b_\ell\) feasible regime, while each later pair is in its \(\alpha<c_\ell\) feasible regime. An optional singleton has abundance \(1/a_j>0\). At each \(\beta_j\), the coordinate numbered \(2j-1\) is negative, since \(\beta_j-b_j<0\) and \(\beta_j^2-b_jc_j=(b_j-c_j)^2/4>0\). These statements concern unique nonsingular solutions at all the chosen test parameters.

**Step 3: make every competition strictly positive and prove robustness.** For all off-block pairs of distinct species put \(B^\varepsilon_{ij}=\varepsilon>0\), retaining the within-pair coefficients, and keep the diagonal zero. The matrix \(aI+B^0\) is nonsingular for every test \(a\), and its solution depends continuously on the matrix coefficients at each such \(a\). There are finitely many positive and negative *strict* coordinate inequalities in Step 2. Hence, for sufficiently small \(\varepsilon>0\), all these inequalities, together with the invertibility of the test matrices, persist. Each \(B^\varepsilon\) has all off-diagonal entries strictly positive. The same inequalities also persist under sufficiently small arbitrary perturbations of all off-diagonal coefficients. Each positive witness has a neighborhood of feasibility; each negative witness has a neighborhood of infeasibility. Because the test parameters interlace, no connected feasible subset of the real line can join two consecutive positive witnesses through an intervening negative witness. There are therefore at least \(k+1\) separate feasible components on an open set of strictly competitive matrices.

An explicit rational bound for preserving the signs makes the construction reproducible. Let \(T\) be the finite set of the \(2k+1\) witnesses. Put \(C_a=(aI+B^0)^{-1}\), \(M=\max_{a\in T}\lVert C_a\rVert_\infty\), and let \(\delta>0\) be the minimum of all coordinates of \(C_a\mathbf1\) at positive witnesses and the absolute values of the designated negative coordinates at the gap witnesses. Both are effectively computable rationals. It is sufficient for sign preservation to take
\[
0<\varepsilon\le\min\left\{\frac1{8M(n-1)},\frac{\delta}{16M^2(n-1)}\right\}.
\]
Indeed \(\lVert B^\varepsilon-B^0\rVert_\infty\le(n-1)\varepsilon\), and the resolvent identity with the Neumann bound gives
\[
\lVert(aI+B^\varepsilon)^{-1}\mathbf1-C_a\mathbf1\rVert_\infty
\le\frac{M^2(n-1)\varepsilon}{1-M(n-1)\varepsilon}<\delta/2.
\]
Shrinking \(\varepsilon\) further below does not harm feasibility and permits the spectral argument in Step 4.

**Step 4: instability of earlier feasible witnesses.** At a feasible test \(a_j\) with \(j<k\), at least one pair has \(a_j<c_\ell<b_\ell\). The Jacobian of its isolated two-species population equations at equilibrium is
\[
-\operatorname{diag}(x^*_{2\ell-1},x^*_{2\ell})
\begin{pmatrix}a_j&b_\ell\\c_\ell&a_j\end{pmatrix}.
\]
Its determinant is \(x^*_{2\ell-1}x^*_{2\ell}(a_j^2-b_\ell c_\ell)<0\). Hence the equilibrium has a positive real eigenvalue. All other isolated pair blocks have nonzero real-part eigenvalues at the chosen tests: for \(a_j>b_\ell\) they have negative trace and positive determinant; for \(a_j<c_\ell\) they have determinant negative. An optional singleton also has a negative eigenvalue. Thus each early equilibrium is hyperbolic with an unstable direction. Hyperbolicity, and the sign of an unstable eigenvalue, persist under sufficiently small positive cross-pair coupling and further perturbations. These claims concern parameter neighborhoods of the witnesses, not necessarily the entirety of each feasible component.

**Step 5: global attraction in the final band.** At \(a_k=b_k+1\), all pairs have \(a_k>b_\ell\), and the equilibrium is feasible. Shrink the cross-pair coupling so that \((n-2)\varepsilon<1/2\) when \(n>2\). Then the symmetric part \(S=(a_kI+B^\varepsilon+(a_kI+B^\varepsilon)^{\mathsf T})/2\) is strictly diagonally dominant with positive diagonal, hence positive definite. This remains true under small perturbations. For any such matrix and its positive equilibrium \(x^*\), consider the relative-entropy Lyapunov function
\[
V(x)=\sum_{i=1}^n\left(x_i-x_i^*-x_i^*\log\frac{x_i}{x_i^*}\right),\qquad x_i>0.
\]
The dynamics imply the exact strict identity
\[
\dot V=-(x-x^*)^{\mathsf T}(a_kI+B)(x-x^*)
=-(x-x^*)^{\mathsf T}S(x-x^*)<0\quad(x\ne x^*).
\]
The positive orthant is invariant, and level sets of \(V\) are compact within it because \(V\to\infty\) as any coordinate tends to \(0\) or \(+\infty\). Standard strict Lyapunov convergence proves global asymptotic attraction of \(x^*\) for every strictly positive initial state. The same argument holds on a neighborhood of \(a_k\) while feasibility and positive definiteness persist.

## Verification

The accompanying self-contained `reentrant_verify.py` uses `fractions.Fraction` and exact Gauss–Jordan inversion. It constructs the block matrices, evaluates every feasibility/infeasibility witness, calculates the rational perturbation bound, verifies the resulting complete positive interaction matrices, and checks final symmetric diagonal dominance for \(n=2,3,\ldots,11\). It yields ten passing finite examples. The proof above, including the Neumann estimate and hyperbolicity argument, covers **all** integer \(n\ge2\); finite checks alone do not establish the unlimited assertion. Execute `python reentrant_verify.py` with Python 3 and no third-party packages.

## Relationship to prior work

Lechón-Alonso, Kundu, Lemos-Costa, Capitán and Allesina (2026) establish general high-dimensional random-community feasibility/stability patterns and exhibit finite-size nonmonotone feasibility (their Fig. 2). They also prove that feasibility is guaranteed for all sufficiently large \(\alpha\). The present statement is different: it gives **unbounded worst-case complexity** (at least linear in species count), in a full-dimensional open set of **strictly positive, all-to-all competition coefficients**, together with an instability/global-attraction contrast at selected feasible witnesses. Their finite illustrative reversals and asymptotic random-matrix results, alone, do not imply this unbounded robust family.

AlAdwani and Saavedra (2022) give general parameter-feasibility techniques for polynomial ecological dynamics, but the located abstract and methodology excerpt do not assert the quantitative re-entrant component lower bound or fully positive constructive family here. General solvability of polynomial inequalities is not itself a construction with a growing number of distinct feasible components.

## Limitations

Feasibility is an algebraic existence notion; the first \(k\) exhibited feasible regimes are **unstable**, so they do not imply durable multispecies coexistence. The theorem gives a **lower bound**, not the exact maximum number of components for arbitrary competitive matrices, and does not characterize all transitions for the perturbed matrices. The interaction family is structured and lies near weakly coupled two-species modules; no probability is asserted for sampling such matrices at random. The electronic supplementary information to the closest 2026 paper could not be inspected in full, leaving historical-priority uncertainty about its treatment of arbitrary finite communities. No independent scientific audit has been performed.

## References

1. P. Lechón-Alonso, S. Kundu, P. Lemos-Costa, J. A. Capitán and S. Allesina, *Robust coexistence in competitive ecological communities*, Nature Communications **17**, 2637 (2026), https://doi.org/10.1038/s41467-026-69151-3 (first journal release 2026-02-11). A dated public research seminar presenting this topic occurred 2026-01-16: https://www.ebd.csic.es/index.php/divulgacion/agenda/robust-coexistence-ecological-competitive-communities.
2. M. AlAdwani and S. Saavedra, *Feasibility conditions of ecological models: Unfolding links between model parameters*, Ecological Modelling **466**, 109900 (2022), https://doi.org/10.1016/j.ecolmodel.2022.109900.
