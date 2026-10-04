# Exact Daugavet constants on \(C(K)\) from the non-isolated core
## Finding
Let \(K\) be an infinite compact Hausdorff space and let \(K^\prime\) be its set of non-isolated points. Since \(K\) is compact Hausdorff, \(K^\prime\) is a nonempty compact set. For \(f\in B_{C(K)}\), put
\[
\beta(f)=\max_{t\in K^\prime}|f(t)|.
\]
Then
\[
\operatorname{dc}_{C(K)}(f)=1+\beta(f).
\]
Here \(\operatorname{dc}(f)\) is the pointwise Daugavet constant, equivalently the infimum over slices \(S\) of \(B_{C(K)}\) of \(\sup_{g\in S}\|f-g\|\).

For \(f\in S_{C(K)}\), the formula yields \(\operatorname{dc}(f)=2\) exactly when \(|f(t)|=1\) at some non-isolated point. As a concrete specialization, if \(K=\mathbb N\cup\{\infty\}\) is the one-point compactification, then \(C(K)=c\) and
\[
\operatorname{dc}_c(x)=1+|\lim_n x_n|.
\]

## Assumptions and scope
All scalars are real. The space \(K\) is infinite, compact, and Hausdorff. No metrizability or separability is assumed. The claim concerns the Daugavet constant only; it does not assert an analogous exact formula for the \(\Delta\)-constant, whose behavior can also depend on isolated coordinates.

## Proof
Write a slice as
\[
S(\mu,\alpha)=\{g\in B_{C(K)}:\mu(g)>1-\alpha\},
\]
where \(\mu\in S_{M(K)}\) is a regular signed measure and \(\alpha>0\).

For the lower bound, fix an arbitrary slice and \(\varepsilon>0\). Choose \(g_0\in S(\mu,\alpha)\) and set
\[
\eta=\mu(g_0)-(1-\alpha)>0.
\]
Choose \(t\in K^\prime\) with \(|f(t)|=\beta(f)\), and an open neighborhood \(U\) of \(t\) on which \(|f(s)-f(t)|<\varepsilon\). The neighborhood \(U\) is infinite. Since \(|\mu|\) is finite, only finitely many points can satisfy \(|\mu|(\{s\})\ge\eta/8\). Hence there is \(s\in U\) with \(|\mu|(\{s\})<\eta/8\). By regularity, choose an open \(W\) with \(s\in W\subset U\) and \(|\mu|(W)<\eta/4\). By normality, choose \(h\in C(K)\) with \(0\le h\le1\), \(h(s)=1\), and support contained in \(W\).

Let \(\sigma=-1\) when \(f(t)\ge0\), and \(\sigma=1\) when \(f(t)<0\), and define
\[
g=(1-h)g_0+h\sigma.
\]
Pointwise, \(g\) is a convex combination of two numbers in \([-1,1]\), so \(g\in B_{C(K)}\). Moreover,
\[
|\mu(g-g_0)|\le2|\mu|(W)<\eta,
\]
so \(g\in S(\mu,\alpha)\). At the point \(s\), the chosen sign gives
\[
|g(s)-f(s)|=|\sigma-f(s)|\ge1+|f(t)|-\varepsilon
=1+\beta(f)-\varepsilon.
\]
Thus every slice contains a point at distance at least \(1+\beta(f)-\varepsilon\) from \(f\), and therefore \(\operatorname{dc}(f)\ge1+\beta(f)\).

For the upper bound, fix \(\varepsilon>0\) and let
\[
F=\{t\in K:t\text{ is isolated and }|f(t)|>\beta(f)+\varepsilon\}.
\]
The set \(F\) is finite: otherwise compactness would give a non-isolated cluster point where continuity forces \(|f|\ge\beta(f)+\varepsilon\), contradicting the definition of \(\beta(f)\). If \(F\) is empty, then \(|f(t)|\le\beta(f)+\varepsilon\) on all of \(K\), and every \(g\in B_{C(K)}\) satisfies \(\|g-f\|\le1+\beta(f)+\varepsilon\).

Suppose \(F=\{t_1,\ldots,t_m\}\) is nonempty. Put \(\epsilon_i=\operatorname{sign}f(t_i)\) and
\[
\phi=\frac1m\sum_{i=1}^m\epsilon_i\delta_{t_i}\in S_{C(K)^*}.
\]
Choose \(0<\delta<1/m\). If \(g\in S(\phi,\delta)\), then each \(\epsilon_i g(t_i)>1-m\delta\); otherwise the average could not exceed \(1-\delta\). Consequently the values of \(g\) on \(F\) have the same signs as those of \(f\) and are uniformly close to the corresponding extreme sign. In particular, after decreasing \(\delta\) if necessary,
\[
|g(t_i)-f(t_i)|\le1+\beta(f)+\varepsilon
\quad(1\le i\le m).
\]
Outside \(F\), by definition \(|f(t)|\le\beta(f)+\varepsilon\), hence
\[
|g(t)-f(t)|\le1+\beta(f)+\varepsilon.
\]
Therefore every \(g\) in this slice satisfies \(\|g-f\|\le1+\beta(f)+\varepsilon\), proving the reverse inequality after \(\varepsilon\downarrow0\).

## Verification
The proof is analytic and uses only regularity of finite signed measures on compact Hausdorff spaces, compactness, and Urysohn separation. The two delicate points were checked explicitly: an infinite neighborhood contains a point whose atomic mass is arbitrarily small, and the finite exceptional set of isolated points can be controlled simultaneously by one average of signed evaluations. No finite computation is used as evidence for the general theorem.

## Relationship to prior work
Abrahamsen, Haller, Lima, and Pirk proved the qualitative characterization that a norm-one \(f\in C(K)\) is a Daugavet point, equivalently a \(\Delta\)-point, exactly when \(|f|\) attains its norm at a non-isolated point. Choi and Jung later introduced the quantitative Daugavet and \(\Delta\)-constants and, in their uniform-algebra section, recorded the same qualitative \(C(K)\) criterion while deriving an upper estimate for the \(\Delta\)-constant under a finite near-norming-extreme-point hypothesis. The formula above gives the exact Daugavet constant throughout the full unit ball of every infinite \(C(K)\) space and reduces the qualitative criterion to the endpoint \(\beta(f)=1\).

## Limitations
No claim is made for general uniform algebras, complex scalars, or the \(\Delta\)-constant. The originality check used targeted statement and implication comparisons; an equivalent formula under different terminology in literature not reached by those searches remains a bibliographic risk.

## References
1. T. A. Abrahamsen, R. Haller, V. Lima, K. Pirk, “Delta- and Daugavet-points in Banach spaces,” arXiv:1812.02450v1, 2018. Theorem 3.4.
2. G. Choi, M. Jung, “The Daugavet and Delta-constants of points in Banach spaces,” arXiv:2307.10647v3, 2024; first posted 2023. Section 3.3, Proposition 3.10 and Corollary 3.11.
