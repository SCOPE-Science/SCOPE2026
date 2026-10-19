# Robust equilibrium–cycle bistability from density-dependent dispersal in two identical patches

## Finding
An explicit two-patch model with **identical, individually globally attracting Beverton–Holt recruitment** and smooth, strictly positive, density-dependent dispersal fractions has **two distinct locally attracting population outcomes**: a synchronized positive equilibrium and a positive antiphase orbit of least period two. The construction admits 50% post-recruitment dispersal loss and persists under sufficiently small admissible parameter changes. In contrast, replacing the density dependence by any constant dispersal fractions while keeping the same recruitment and total retention forces global convergence to the synchronized equilibrium for every positive initial condition.

Specifically, with \(f(z)=5z/(1+z)\), retention \(s=1/2\), emigration proportion
\[
 p(z)=\frac{14z^2+1}{14(1+z^2)},\qquad h(z)=1-p(z)=\frac{13}{14(1+z^2)},
\]
and the post-recruitment map \(F:\mathbb R_{\ge0}^2\to\mathbb R_{\ge0}^2\)
\[
 F(x,y)=\frac12\begin{pmatrix}
 h(x)f(x)+p(y)f(y)\\
 p(x)f(x)+h(y)f(y)
 \end{pmatrix},
\]
the point \(E=(3/2,3/2)\) is a locally asymptotically stable fixed point, while
\[
 A=(2,2/3),\qquad B=(2/3,2),\qquad F(A)=B,\quad F(B)=A
\]
form a distinct, locally asymptotically stable prime period-two orbit. In each isolated patch, \(z\mapsto f(z)\) instead converges to its positive fixed point \(4\) from every positive initial state.

## Assumptions and scope
Time is discrete, population densities are nonnegative real numbers, recruitment precedes dispersal, and 50% of the recruited individuals survive the dispersal/retention stage. The fraction staying in its natal patch is \(s h(z)\) and that arriving in the other patch is \(s p(z)\). These fractions are continuously differentiable, strictly between zero and one for each finite \(z\ge0\), and their sum is the strict subunit constant \(s\). This is a lossy density-dependent analogue of the constant-dispersal two-patch Beverton–Holt system studied by Grumbach and collaborators (2023), within the bounded-Kolmogorov-recruitment, costly density-dependent dispersal class developed by McGrane-Corrigan, Mason, and de Andrade Moral (2024). There is no Allee effect and no intrinsic overcompensation: \(f\) is strictly increasing, strictly concave for positive densities, bounded above by \(5\), and \(f(0)=0\).

An attracting fixed point and an attracting period-two orbit mean local asymptotic stability under the one-step map and the two-step return map, respectively. No assertion is made that these are the only attractors or that their basins exhaust the positive quadrant.

## Proof
**1. Admissibility and isolated dynamics.** For finite \(z\ge0\), \(0<h(z)<1\), \(0<p(z)<1\), and \(h(z)+p(z)=1\). Thus all four entries of the dispersal matrix are positive and each column sums to \(1/2<1\). The regional recruitment function \(f\) is positive on positive densities, bounded, smooth, and of Kolmogorov form \(z\,[5/(1+z)]\). It is strictly increasing. Its only positive fixed point is \(4\); monotonicity together with the sign of \(f(z)-z=z(4-z)/(1+z)\) proves convergence to \(4\) from every \(z>0\).

**2. Synchronized sink.** Since \(h(z)+p(z)=1\), the diagonal is invariant and evolves by \(g(z)=f(z)/2=5z/[2(1+z)]\), with positive fixed point \(z=3/2\). The Jacobian at \(E\) is
\[
 DF(E)=\begin{pmatrix}-128/455&62/91\\62/91&-128/455\end{pmatrix}.
\]
Its symmetric and antisymmetric eigenvalues are respectively \(2/5\) and \(-438/455\). Both lie strictly inside the unit disk; therefore \(E\) is locally asymptotically stable in the full two-dimensional state space, not only on the invariant diagonal.

**3. Exact prime two-cycle.** The dispersal fractions at the candidate points are
\[
 h(2)=13/70,\quad p(2)=57/70,\quad
 h(2/3)=9/14,\quad p(2/3)=5/14.
\]
Since \(f(2)=10/3\) and \(f(2/3)=2\), direct substitution gives
\[
 F(2,2/3)=\left(\frac12\left[\frac{13}{70}\frac{10}{3}+\frac5{14}\,2\right],
 \frac12\left[\frac{57}{70}\frac{10}{3}+\frac9{14}\,2\right]\right)
 =(2/3,2).
\]
Exchange symmetry then gives \(F(2/3,2)=(2,2/3)\). The two states are distinct and strictly positive.

**4. Exact two-step stability certificate.** For compact notation set \(w(z)=z/(1+z)\), \(u(z)=[h(z)w(z)]'\), and \(v(z)=[p(z)w(z)]'\). Differentiation gives
\[
 DF(x,y)=\frac52\begin{pmatrix}u(x)&v(y)\\v(x)&u(y)\end{pmatrix}.
\]
At \(A\) and \(B\), respectively, these matrices are
\[
 J_A=\begin{pmatrix}-247/1260&333/364\\199/420&-27/1820\end{pmatrix},
 \qquad
 J_B=\begin{pmatrix}-27/1820&199/420\\333/364&-247/1260\end{pmatrix}.
\]
The two-step derivative \(M=DF^2(A)=J_BJ_A\) equals
\[
 M=\begin{pmatrix}
 20057/88200&-34119/1656200\\
 -72029/264600&1390929/1656200
 \end{pmatrix},
\]
with exact trace and determinant
\[
 T=\operatorname{tr}M=\frac{7953997}{7452900},\qquad
 \Delta=\det M=\frac{3837681}{20702500}.
\]
The strict second-order Schur/Jury inequalities are verified by
\[
 1-T+\Delta=\frac{423302}{3583125}>0,\qquad
 1+T+\Delta=\frac{209855777}{93161250}>0,\qquad
 1-\Delta=\frac{16864819}{20702500}>0.
\]
Hence both eigenvalues of the return derivative are strictly within the unit disk, and the prime two-cycle is locally asymptotically stable. Its open attraction neighborhood is disjoint from an open attraction neighborhood of \(E\).

**5. Robustness.** Both attracting objects are hyperbolic. The implicit-function theorem applies to the fixed-point equations \(F(z)=z\) near \(E\) and \(F^2(z)=z\) near \(A\), because the respective derivatives minus the identity are invertible. The resulting distinct equilibrium and two-cycle remain positive and attracting under sufficiently small \(C^1\) perturbations within the smooth admissible recruitment-and-dispersal class. Exchange symmetry, if maintained, retains the exact antiphase form; it is not required for persistence of the prime two-cycle.

**6. Fixed-dispersal contrast.** If \(p(z)\) is replaced by any constant \(q\in[0,1]\), and \(h(z)=1-q\), then both new coordinates are convex combinations of \(g(x)\) and \(g(y)\). The function \(g(z)=5z/[2(1+z)]\) is strictly increasing and has globally attracting positive fixed point \(3/2\). Starting from positive \(x,y\), let \(m\) and \(M\) be their minimum and maximum. By induction, both coordinates after \(t\) iterations lie between \(g^t(m)\) and \(g^t(M)\), which both converge to \(3/2\). Thus every positive trajectory with constant dispersal converges to \(E\); no positive prime periodic orbit survives that replacement.

## Verification
The attached `verify_exact.py` uses standard-library rational arithmetic, reconstructs the orbit, computes both Jacobians analytically, multiplies them, and checks every displayed trace, determinant, eigenvalue, and strict Jury inequality exactly. Run `python verify_exact.py`. These finite rational identities certify the stated explicit example; the convergence and perturbation assertions rely on the analytic arguments above, not on finite experimentation.

## Relationship to prior work
Grumbach, Reurik, Segura, Franco, and Hilker (2023, Theorem/Lemma 1 and equation (1)) show global attraction to a positive equilibrium for two-patch Beverton–Holt recruitment with constant symmetric dispersal and no dispersal loss. The present example uses exactly the same compensated Beverton–Holt recruitment in two identical patches, but changes both the emigration fraction to a strictly increasing density-dependent Hill function and overall retention to a constant \(1/2\). The Grumbach model does not include these features, and its globally attracting equilibrium cannot imply the new equilibrium–cycle coexistence. The new fixed-dispersal contrast proves the same global-convergence behavior even with retention loss in this concrete family.

Huang and Chen (arXiv:2302.01814, 2023) obtain delay-driven Hopf bifurcations in continuous-time patch population systems with loss. Their model uses continuous delayed logistic equations rather than a discrete Beverton–Holt map with density-dependent emigration; the theorem here demonstrates a different, delay-free, bistable mechanism.

McGrane-Corrigan, Mason, and de Andrade Moral (arXiv:2405.04505, first posted 2024-05-07) introduce a general density-dependent, costly-dispersal metapopulation model and present numerical period-two behavior in an asymmetric Ricker/Hassell source-sink setting. Their theoretical results principally concern extinction, positive equilibria, and persistence. The present construction is an exact **simultaneous fixed-point and two-cycle sink** in **identical globally stable Beverton–Holt patches**, and is accompanied by an exact return-matrix certificate and a fixed-dispersal impossibility comparison. Neither the numerical period-two observation nor the general persistence theorems imply the claimed coexistence of locally stable outcomes.

The earlier Silva–de Castro–Justo paper (2001) studies instability caused by density-dependent emigration and could contain related examples. Chow–Jang–Yeh (2018) studies a different two-patch/refuge model; its abstract gives global positive-equilibrium stability with Beverton–Holt growth and reports periodicity in its Allee-effect regime. Full texts of those two plausible comparisons were not accessible in this inspection; their precise contents remain originality risks rather than established noncoverage. Existing literature on dispersal-induced oscillations makes the general qualitative phenomenon non-novel; the proposed contribution is the fully specified, certified **bistability in compensatory identical recruitment with strictly positive costly dispersal**, not the mere existence of periodic dispersal dynamics.

## Limitations
The result is an explicit structural counterexample, not a global bifurcation classification or a claim of universal bistability. It does not identify exact basin boundaries, global attractors, or stochastic persistence. The smooth density dependence is specifically \(p(z)=(14z^2+1)/[14(1+z^2)]\); robustness is local in parameter/function space, without a numerically specified maximal neighborhood. Only a self-review has been performed; independent validation is outstanding. Full-document comparisons with the inaccessible 2001 and 2018 papers remain a residual novelty risk.

## References
1. C. Grumbach, F. N. Reurik, J. Segura, D. Franco, and F. M. Hilker, *The effect of dispersal on asymptotic total population size in discrete- and continuous-time two-patch models*, Journal of Mathematical Biology **87**, article 60 (first publicly published 2023-09-21), doi:10.1007/s00285-023-01984-8.
2. D. Huang and S. Chen, *Dynamics of a delayed population patch model with the dispersion matrix incorporating population loss*, arXiv:2302.01814 (first posted 2023-02-03), European Journal of Applied Mathematics **34** (2023), 870–895.
3. B. McGrane-Corrigan, O. Mason, and R. de Andrade Moral, *A density-dependent metapopulation model: Extinction, persistence and source-sink dynamics*, arXiv:2405.04505 (first publicly posted 2024-05-07), https://arxiv.org/abs/2405.04505.
4. J. A. L. Silva, M. L. de Castro, and D. A. R. Justo, *Stability in a metapopulation model with density-dependent dispersal*, Bulletin of Mathematical Biology 63 (2001), 485–506, doi:10.1006/bulm.2000.0221.
5. Y. Chow, S. R.-J. Jang, and N.-S. Yeh, *Dynamics of a population in two patches with dispersal*, Journal of Difference Equations and Applications 24 (2018), 543–563, doi:10.1080/10236198.2018.1428962.
6. G. Ruxton and P. Rohani, *Fitness-dependent dispersal in metapopulations and its consequences for persistence and synchrony*, Journal of Animal Ecology 68 (1999), doi:10.1046/j.1365-2656.1999.00300.x.
