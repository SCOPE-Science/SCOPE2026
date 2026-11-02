# A unique corridor-investment reversal in a four-patch landscape

## Finding

For a connected, undirected four-patch chain, compare two mutually exclusive restoration interventions: a new corridor from patch 1 to patch 3, or one from patch 2 to patch 4. Their Perron-eigenvalue ranking is *completely determined*, at every positive investment level, by a one-dimensional sign rule. In particular, when the per-unit corridor efficiency favors one choice but its infinitesimal spectral benefit favors the other, the preferred restoration has **exactly one** positive investment threshold at which it reverses. This is a global theorem, not a small-perturbation approximation.

Write the baseline weights on successive edges as \(a,b,c>0\), the two corridor efficiencies as \(\alpha,\beta>0\), and total effort as \(t>0\). Let \(\Lambda_A(t)\) and \(\Lambda_B(t)\) be the Perron eigenvalues of the two resulting landscape matrices specified below. Define

\[
D=\alpha^2-\beta^2,\qquad H=a\alpha-c\beta.
\]

Then, with \(\operatorname{sgn}(0)=0\),

\[
\boxed{\operatorname{sgn}(\Lambda_A(t)-\Lambda_B(t))
=\operatorname{sgn}\bigl(Dt\Lambda_B(t)+2bH\bigr).}
\]

If \(DH<0\), there is exactly one \(t_*>0\), implicitly but uniquely determined by

\[
\boxed{t_*\Lambda_B(t_*)=-\frac{2bH}{D}.}
\]

The choice favored at small positive investment has the sign of \(H\), and the choice favored at sufficiently large investment has the sign of \(D\). Thus \(D>0>H\) means choose corridor B below \(t_*\) and corridor A above it; \(D<0<H\) means the reverse. If \(DH\geq0\) with \((D,H)\neq(0,0)\), there is no positive crossing, and the sign law classifies all effort levels. If \(D=H=0\), the capacities tie for all \(t>0\).

## Assumptions and scope

Four equal-area patches are numbered \(1,2,3,4\). The baseline landscape is an undirected path with symmetric positive connection weights \(a,b,c\). An intervention adds exactly one previously absent bidirectional corridor, with weight proportional to effort. The candidates are

\[
M_A(t)=\begin{pmatrix}
0&a&\alpha t&0\\
a&0&b&0\\
\alpha t&b&0&c\\
0&0&c&0
\end{pmatrix},\qquad
M_B(t)=\begin{pmatrix}
0&a&0&0\\
a&0&b&\beta t\\
0&b&0&c\\
0&\beta t&c&0
\end{pmatrix}.
\]

All six parameters \(a,b,c,\alpha,\beta,t\) are strictly positive real numbers, without upper bounds. \(\Lambda_J(t)=\rho(M_J(t))\) denotes the positive simple Perron eigenvalue of \(M_J(t)\). The capacity proxy is the leading eigenvalue of a symmetric nonnegative landscape matrix; it is not a general claim about a full spatially heterogeneous ecological stochastic process. Identical species-specific thresholds cancel from a **ranking** of these two matrices when the simple metapopulation-capacity interpretation is appropriate.

## Proof

Let \(P_J(x,t)=\det(xI-M_J(t))\). Direct determinant expansion yields, with \(S=a^2+b^2+c^2\),

\[
\begin{aligned}
P_A(x,t)&=x^4-(S+\alpha^2t^2)x^2-2ab\alpha tx+a^2c^2,\\
P_B(x,t)&=x^4-(S+\beta^2t^2)x^2-2bc\beta tx+a^2c^2,
\end{aligned}
\]

so that the **exact factorization** is

\[
P_A(x,t)-P_B(x,t)=-tx\bigl(Dtx+2bH\bigr).\tag{1}
\]

Let \(\lambda_1(M_A)\geq\lambda_2(M_A)\geq\lambda_3(M_A)\geq\lambda_4(M_A)\) be its ordered *real* eigenvalues. Delete row and column 3 of \(M_A\); the remaining principal submatrix has eigenvalues \(a,0,-a\). Cauchy interlacing gives \(\lambda_2(M_A)\leq a\). The connected nonnegative matrix \(M_B\) strictly contains a weighted edge of size \(a\), so by Perron monotonicity (or the positive Rayleigh/Perron vector) \(\Lambda_B(t)>a\). Consequently,

\[
P_A(\Lambda_B(t),t)
=(\Lambda_B(t)-\Lambda_A(t))
\prod_{j=2}^{4}(\Lambda_B(t)-\lambda_j(M_A(t)))
\]

has the same sign as \(\Lambda_B-\Lambda_A\), because the three factors in the product are strictly positive. But \(P_B(\Lambda_B,t)=0\), so (1) gives

\[
P_A(\Lambda_B,t)=-t\Lambda_B\bigl(Dt\Lambda_B+2bH\bigr).
\]

Since \(t\Lambda_B>0\), comparison of signs proves the boxed ranking rule, including equality.

For uniqueness, \(t\mapsto\Lambda_B(t)\) is continuous and strictly increasing. Indeed, \(M_B(t_2)\) strictly increases its (2,4) and (4,2) entries for \(t_2>t_1\), and its strictly positive Perron vector gives a strict Rayleigh-quotient increase. Hence \(t\Lambda_B(t)\) increases strictly and continuously from zero at \(t\downarrow0\) to infinity at \(t\to\infty\); the latter follows from \(\Lambda_B(t)\geq\beta t\). The linear function of this quantity, \(D t\Lambda_B(t)+2bH\), vanishes at exactly one positive effort if and only if \(DH<0\). The remaining sign cases follow immediately. This proves the classification for every admissible parameter tuple, without treating numerical eigenvalue samples as a proof.

## Verification

In the concrete landscape \(a=b=1\), \(c=3\), \(\alpha=2\), \(\beta=1\), the small-effort criterion favors B although A has twice the corridor efficiency. Here \(D=3\), \(H=-1\), and equality means \(t\Lambda_B(t)=2/3\). Substitution into the exact characteristic polynomial gives

\[
369t^4-396t^2+16=0.
\]

The physically admissible root is

\[
\boxed{t_*=\sqrt{\frac{66-10\sqrt{37}}{123}}\approx0.2050654207930308.}
\]

The second positive root of the quartic in \(t\) does **not** satisfy the required Perron-eigenvalue branch and must not be counted as another crossover; the monotonicity proof independently excludes it. The common capacity at the admissible crossover is about \(3.250995043867111\). At effort \(t=0.1\), the respective Perron values are approximately \(3.2078132026\) for A and \(3.2132632119\) for B. At \(t=0.5\), they are approximately \(3.4380693992\) for A and \(3.3685974137\) for B.

A standalone reproducibility program `verify.py` uses Python 3.10+, SymPy and NumPy. Executing `python verify.py` yields `PASS: 2577 symbolic, exact-rational, and numeric checks`. Its SymPy phase derives both general characteristic polynomials; 1,700 independent rational determinant expansions validate them at varied positive weights, and 850 numerical eigenvalue comparisons probe the exact sign rule. The checker also verifies the exact algebraic example and several boundary cases. These computations corroborate—but do not substitute for—the preceding analytic proof.

## Relationship to prior work

Hanski and Ovaskainen (2000) established metapopulation capacity as a leading-eigenvalue measure for fragmented landscapes. Their ecological concept and the general matrix–persistence link are not claimed as new. Ovaskainen and Hanski (2001) develop this theory for patch networks. Tambosi and coauthors (2014) study biodiversity-restoration prioritization and connectivity, but their accessible abstract addresses a different connectivity objective. Milanese, Sun and Nishikawa (2010), whose nine-page open-access preprint was inspected including perturbation formulas, numerical examples and references, calculate **approximate** eigenvalue impacts and edge rankings. Noschese and Reichel (2025), whose complete open-access article was inspected, analyze Perron sensitivity and edge-removal rankings. The new statement here is the exact **all-effort comparison** of two alternative restoration edges on a weighted four-patch path, with an if-and-only-if existence condition and unique investment crossover. In particular, first-order rankings alone do not establish the finite-effort reversal. General spectral formulas and interlacing are used as known tools, not claimed as new inventions.

Accessible research records and prior claims were compared for the same graph, eigenvalue and investment-ranking implications. No examined source provided the stated four-patch all-parameter crossover, but absence in search results does not prove historical priority. The original 2000 ecological article and some restoration literature could not be read in full; those are explicit residual risks.

## Limitations

The statement concerns **one of two mutually exclusive added edges**, fixed original weights, proportional effort, symmetric bidirectional connections, no self loops, and exactly four patches. It ranks spectral-radius capacity proxies; it does not imply that extinction probability, abundance, recovery speed or management utility have exactly the same order under every spatial ecological model. Physical distances and corridor cost functions must be justified before applying the weights to real landscapes. No independent mathematical audit or exhaustive historical-priority certification has occurred.

## References

1. I. Hanski and O. Ovaskainen, “The metapopulation capacity of a fragmented landscape,” *Nature* 404, 755–758 (2000), publicly dated 13 April 2000. https://doi.org/10.1038/35008063.
2. O. Ovaskainen and I. Hanski, “Spatially structured metapopulation models: global and local assessment of metapopulation capacity,” *Theoretical Population Biology* 60, 281–302 (2001). https://doi.org/10.1006/tpbi.2001.1548.
3. A. Milanese, J. Sun and T. Nishikawa, “Approximating Spectral Impact of Structural Perturbations in Large Networks” (2010), arXiv:1001.1431. https://arxiv.org/abs/1001.1431.
4. S. Noschese and L. Reichel, “Sensitivity of Perron and Fiedler Eigenpairs to Structural Perturbations of a Network,” *Numerical Linear Algebra with Applications* (2025). https://doi.org/10.1002/nla.70041.
5. L. R. Tambosi and colleagues, “A Framework to Optimize Biodiversity Restoration Efforts Based on Habitat Amount and Landscape Connectivity,” *Restoration Ecology* (2014; first online 2013). https://doi.org/10.1111/rec.12049.
