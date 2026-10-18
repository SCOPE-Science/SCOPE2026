# Perfect-square first-variation rigidity for skew Schäffer means on real \(L^4\)

## Finding
Let \(X=L^4(\Omega,\mu;\mathbb R)\) contain two disjointly supported nonzero vectors. For every fixed \(1\le t<4\), define
\[
\mathcal S_{X,t}(\tau)=\inf_{\|x\|_4=\|y\|_4=1}
\left(\frac{\|x+\tau y\|_4^t+\|\tau x-y\|_4^t}{2}\right)^{1/t},\qquad \tau\ge0.
\]
Then the dimension-independent endpoint law is
\[
\boxed{\mathcal S_{X,t}(\tau)=1-\frac{\tau}{2\sqrt2}+O_t(\tau^2)\quad(\tau\downarrow0).}
\]
More precisely, put
\[
Q(x,y)=xy+\frac{x^2-y^2}{\sqrt2},\qquad
F_t(x,y;\tau)=\left(\frac{\|x+\tau y\|_4^t+\|\tau x-y\|_4^t}{2}\right)^{1/t}.
\]
Uniformly over all real unit pairs \((x,y)\),
\[
\boxed{F_t(x,y;\tau)=1-\frac{\tau}{2\sqrt2}
+\frac{\tau}{2\sqrt2}\|Q(x,y)\|_2^2+O_t(\tau^2).}
\]
The **primary structural finding** is the exact sum-of-squares deficit and its complete equality class; the numerical slope itself follows from previously known matched-exponent information combined with uniform comparison of nearby power means. All fixed unit pairs attaining the first-order minimum are precisely
\[
x=af+bg,\qquad y=-bf+ag,
\quad a^4=\frac{2+\sqrt3}{4},\quad b^4=\frac{2-\sqrt3}{4},\quad a,b>0,
\]
where \(f,g\in X\) are disjointly supported unit vectors (with arbitrary real signs). For any family of unit pairs \((x_\tau,y_\tau)\), asymptotic minimality
\[
F_t(x_\tau,y_\tau;\tau)-\mathcal S_{X,t}(\tau)=o(\tau)
\]
is equivalent to \(\|Q(x_\tau,y_\tau)\|_2\to0\). In particular, an excess at most \(\varepsilon\tau\) forces
\[
\|Q(x,y)\|_2^2\le 2\sqrt2\,\varepsilon+C_t\tau
\]
for a constant \(C_t\) independent of \((\Omega,\mu)\) and of the pair, when \(\tau\) is sufficiently small.

## Assumptions and scope
The scalar field is **real**, the underlying measure space is arbitrary, and its \(L^4\)-space has at least two disjoint nonzero elements. The skew parameter satisfies \(\tau\ge0\) and approaches zero from above; the *outer* power-mean exponent \(t\) is fixed in \([1,4)\), independent of the inner exponent \(4\). Both vectors have \(L^4\) norm exactly one, and all integrals are with respect to \(\mu\). The products \(xy\), \(x^2\) and \(y^2\) belong to \(L^2\), so every displayed expression is well-defined. The statement does not assert the finite-parameter profile away from \(\tau=0\) or stability in \(L^4\)-distance to the set of extremizers.

## Proof
**1. Uniform first variation.** For a unit pair \(x,y\), Hölder's inequality bounds all fourth-order mixed moments by one. Expansion of the fourth powers gives
\[
\begin{aligned}
\|x+\tau y\|_4^4
 &=1+4\tau\!\int x^3y+6\tau^2\!\int x^2y^2+4\tau^3\!\int xy^3+\tau^4,\\
\|\tau x-y\|_4^4
 &=1-4\tau\!\int xy^3+6\tau^2\!\int x^2y^2-4\tau^3\!\int x^3y+\tau^4.
\end{aligned}
\]
For \(0\le\tau\le1/4\), the two norms lie in \([3/4,5/4]\) by the triangle inequality. The fourth root has bounded second derivative on the corresponding compact interval of fourth powers, so, **uniformly in the unit pair**, 
\[
\|x+\tau y\|_4=1+\tau\!\int x^3y+O(\tau^2),\qquad
\|\tau x-y\|_4=1-\tau\!\int xy^3+O(\tau^2).
\]
For every fixed \(1\le t<\infty\), the power mean is twice continuously differentiable in a neighborhood of \((1,1)\), with both first partial derivatives equal to \(1/2\). Consequently, with
\[
D(x,y)=\int xy(x^2-y^2),
\]
we have the uniform expansion
\[
F_t(x,y;\tau)=1+\frac{\tau}{2}D(x,y)+O_t(\tau^2).
\]

**2. Exact fourth-power defect.** Directly expanding a nonnegative square and using \(\int x^4=\int y^4=1\) gives the **exact identity**
\[
\begin{aligned}
\|Q(x,y)\|_2^2
&=\int x^2y^2+\frac12\int(x^2-y^2)^2
+\sqrt2\int xy(x^2-y^2)\\
&=1+\sqrt2 D(x,y).
\end{aligned}
\]
Thus \(D(x,y)\ge-1/\sqrt2\), with equality if and only if \(Q(x,y)=0\) almost everywhere. Substituting
\(D=(\|Q\|_2^2-1)/\sqrt2\) into the expansion in step 1 proves the claimed uniform sum-of-squares formula, and in particular the universal lower slope.

**3. Attainment and complete equality classification.** Define positive constants
\[
a=\left(\frac{2+\sqrt3}{4}\right)^{1/4},\qquad
b=\left(\frac{2-\sqrt3}{4}\right)^{1/4}.
\]
They obey \(a^4+b^4=1\) and \(a^2-b^2=\sqrt2\,ab\). Choose any two disjoint unit vectors \(f,g\in X\). The vectors \(x=af+bg\) and \(y=-bf+ag\) both have norm one, and the preceding algebra shows \(Q(x,y)=0\) separately on the supports of \(f\) and \(g\). This attains the lower first-order coefficient and proves the sharp asymptotic formula after taking the infimum over all pairs (the error is uniform).

Conversely, suppose a unit pair has \(Q(x,y)=0\) almost everywhere. The pointwise equation
\[
x^2+\sqrt2\,xy-y^2=0
\]
forces \(x=y=0\) wherever either coordinate is zero. On the remaining support it forces exactly one of the two signed ratios
\[
\frac{x}{y}=\frac{\sqrt3-1}{\sqrt2}=\frac ba,
\qquad
\frac{x}{y}=-\frac{\sqrt3+1}{\sqrt2}=-\frac ab.
\]
Partition the support into the two measurable ratio sets \(E_+\) and \(E_-\). Put \(f=x/a=-y/b\) on \(E_-\), zero elsewhere, and \(g=x/b=y/a\) on \(E_+\), zero elsewhere. These have disjoint supports, and the representation \(x=af+bg\), \(y=-bf+ag\) follows. If \(U=\|f\|_4^4\), \(V=\|g\|_4^4\), then the unit norms give
\[
a^4U+b^4V=1,\qquad b^4U+a^4V=1.
\]
Since \(a^4\ne b^4\) and \(a^4+b^4=1\), they imply \(U=V=1\), completing the classification.

**4. Uniform quantitative near-rigidity.** There exists a constant \(K_t\), independent of the measure space and unit pair, such that
\[
\left|F_t(x,y;\tau)-1+\frac{\tau}{2\sqrt2}-\frac{\tau}{2\sqrt2}\|Q(x,y)\|_2^2\right|\le K_t\tau^2.
\]
The sharp value of the infimum differs from \(1-\tau/(2\sqrt2)\) by at most \(K_t\tau^2\). Subtracting the two expansions yields
\[
\left|\frac{F_t(x,y;\tau)-\mathcal S_{X,t}(\tau)}\tau
-\frac{\|Q(x,y)\|_2^2}{2\sqrt2}\right|\le 2K_t\tau
\]
for \(0<\tau\le1/4\). This both proves the equivalence for asymptotically minimizing families and yields the stated \(\varepsilon\)-stability with \(C_t=4\sqrt2 K_t\). No compactness of the measure space or finite-dimensional reduction is used.

## Verification
The algebraic certificate in step 2 is an identity, not a numerical approximation; step 3 reconstructs every zero of its nonnegative quadratic integrand. A separate executable `verify.py` performs symbolic expansion of the defect polynomial, verifies the exact two-band parameters, tests the expansion on finite-dimensional real \(\ell_4\) samples, and checks the endpoint coefficient numerically for several outer means. Those finite checks corroborate the arithmetic only; all infinite-dimensional and uniform assertions follow from the proof.

## Relationship to prior work
Xu and Liu, *Skew Schäffer Type Constants* (arXiv:2610.03050v1, 2 October 2026), introduce exactly this infimal invariant, prove the full \(L^p\) formula **when the outer exponent equals \(p\)** (their Theorem 3.2), and give general inequalities, rather than an exact answer, when the two exponents differ (their discussion following Corollary 3.6). Their matched \(L^4\) formula at \(t=4\), **together with a uniform second-order comparison of power means near the equal output norms**, already implies the same numeric first-order coefficient for every fixed finite \(t\). Specifically, for \(a,b\in[1-\tau,1+\tau]\), one has \(\mathcal M_t(a,b)-\mathcal M_4(a,b)=O_t((a-b)^2)=O_t(\tau^2)\). **The scalar slope is not claimed as new.** The additional, distinct claim here is the exact *pairwise* nonnegative-square first-variation defect, its complete algebraic two-band equality classification, and the uniform quantitative if-and-only-if criterion for asymptotically minimizing pairs. The published formula for the *infimum* and its exhibited witnesses do not establish these claims for all pairs.

Ni, Liu and Zhou's 2025 *Some aspects of new skew geometric constants in Banach spaces* studies **supremal** skew constants. The published formula *Exact skew geometric mean constant of \(\ell_4\)* likewise computes the supremum of an arithmetic mean of two skew chord norms, not this infimum with the mixed outer mean. The separately published *A sharp small-skew phase transition in the Banaś–Frączek plane* finds a first-order coefficient for a different, nonsmooth two-dimensional norm; its pointwise quadratic-branch comparison cannot supply the stated real \(L^4\) result. Searches for exact pairwise skew first-variation defects, equality rigidity, and the algebraic ratio zero set did not locate the proposed structural statement. A published source containing a stronger equivalent formulation outside indexed search remains a priority risk.

## Limitations
The asymptotic is at the small-skew endpoint only, with fixed finite outer exponent \(1\le t<4\). It does not determine the exact value for arbitrary positive \(\tau\), the minimizing pairs at each nonzero \(\tau\), the complex-scalar problem, or norm-distance stability toward a specific minimizer. The explicit sum-of-squares formula uses the quartic power and does not directly extend to general \(L^p\). Novelty is evaluated against the identified literature, not certified against all unpublished or unindexed work; no independent validation has been performed.

## References
1. Y. Xu and Q. Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1, publicly posted 2 October 2026, https://arxiv.org/html/2610.03050v1.
2. Q. Ni, Q. Liu and Y. Zhou, *Some aspects of new skew geometric constants in Banach spaces*, Mathematical Inequalities & Applications 28 (2025), 327–342, DOI:10.7153/mia-2025-28-22.
3. *Exact skew geometric mean constant of \(\ell_4\)*, publicly available mathematical research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-skew-geometric-mean-constant-of-ell-4--7a18ef79086d.
4. *A sharp small-skew phase transition in the Banaś–Frączek plane*, publicly available mathematical research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-small-skew-phase-transition-in-the-bana-fr-czek-plane--4c730d387d65.
