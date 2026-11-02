# Two-sided fluctuation bounds for acyclic color classes in critical random digraphs

## Finding
Let \(s\ge 2\) and \(r\ge 2\). Choose independently and uniformly a color in \(\{1,\ldots,s\}\) for every edge of the \(s\)-ary de Bruijn digraph of neighborhood length \(r\). Let \(M_{s,r}\) be the number of colors with no monochromatic directed cycle, equivalently the number of constant configurations absent from the image of the corresponding random cellular automaton. Put
\[
q_{s,r}=\Pr(\text{a fixed color has no directed cycle}),\quad
 a_s=(1-1/s)^s,\quad b_s=(1-2/s)^s,
\]
and
\[
 V_s=s a_s+s(s-1)b_s-s^2a_s^2.
\]
**Theorem.** The \(s\) missing-color indicators are negatively associated. For each \(s\ge2\), \(r\ge2\),
\[
 \frac{q_{s,r}^2}{a_s^2}V_s\ \le\ \operatorname{Var}(M_{s,r})\ \le\ sq_{s,r}(1-q_{s,r}). \tag{1}
\]
For any \(0<\varepsilon<1\),
\[
 \Pr\bigl(|M_{s,r}-sq_{s,r}|\ge\varepsilon sq_{s,r}\bigr)
 \le 2\exp(-\varepsilon^2sq_{s,r}/3). \tag{2}
\]
For neighborhood length \(r=2\), write \(c_*\) for the positive Airy-integral constant in Gravner--Kulhanek's one-color asymptotic, \(c_*\approx 0.4887367\). Then
\[
\liminf_{s\to\infty}\frac{\operatorname{Var}(M_{s,2})}{s^{1/3}}
\ge(e-2)c_*^2\approx0.1715714,
\qquad
\limsup_{s\to\infty}\frac{\operatorname{Var}(M_{s,2})}{s^{2/3}}
\le c_* . \tag{3}
\]
In particular,
\[
 \frac{M_{s,2}}{s^{2/3}}\longrightarrow c_*
\]
in \(L^2\) and almost surely for any coupling of the models for different \(s\). The lower bound isolates a nonzero, explicitly quantified source of fluctuations arising solely from random labels on the \(s\) self-loops. No claim that either variance exponent in (3) is optimal is made.

## Assumptions and scope
The \(s\)-ary de Bruijn digraph has vertices the words of length \(r-1\) over \(\{1,\dots,s\}\), and one directed edge for each word of length \(r\), going from its prefix to its suffix. All \(s^r\) edge labels are independent and uniformly sampled from \(s\) colors. A directed cycle includes a one-edge self-loop. A color is missing if no cycle uses exclusively edges of that color; this is equivalent to absence of the corresponding constant output configuration, by the de Bruijn encoding of the cellular automaton. There are exactly \(s\) self-loops (the constant words).

## Proof
**1. Negative association.** Recall that binary variables \(Z_i\) are negatively associated when for disjoint coordinate sets \(I,J\) and nondecreasing functions \(F,G\), the covariance of \(F((Z_i)_{i\in I})\) and \(G((Z_j)_{j\in J})\) is nonpositive. For a single edge let \(X_c\) be its one-hot color indicators. Any nondecreasing function on coordinates in \(I\) has the form \(F(0)+\sum_{c\in I}a_cX_c\) on the one-hot support, with \(a_c\ge0\). For disjoint \(I,J\), the covariance with an analogous \(G\) is exactly \(- (\sum_{c\in I}a_c/s)(\sum_{d\in J}b_d/s)\le0\). Thus a single edge's one-hot vector is negatively associated.

An independent union of negatively associated families remains negatively associated. For completeness, induct on the families: condition the covariance of two increasing functions on the last family. Conditional covariance is nonpositive by association of the first families, while covariance of the conditional means is nonpositive by association of the last family, since the means are increasing in its respective disjoint coordinates. Therefore all edge-color indicator variables are negatively associated.

For each color \(c\), let \(B_c\) be the indicator that its monochromatic subgraph is acyclic. It is a nonincreasing function only of the variables \((X_{e,c})_e\). These coordinate sets are disjoint as \(c\) varies. Negative association is preserved under a collection of coordinatewise nonincreasing transformations on disjoint coordinate blocks: to test two nonincreasing functions, negate both to apply the nondecreasing definition. Hence the vector \((B_c)_{c=1}^s\) is negatively associated. Consequently, pairwise covariances are nonpositive and
\[
\operatorname{Var}\Bigl(\sum_c B_c\Bigr)\le\sum_c\operatorname{Var}(B_c)
=sq_{s,r}(1-q_{s,r}).
\]
Moreover, for every real \(t\), products of the positive functions \(e^{tB_c}\), all monotone in a common direction, satisfy
\[
\mathbb E e^{t\sum B_c}\le\prod_c\mathbb Ee^{tB_c}=(1-q_{s,r}+q_{s,r}e^t)^s.
\]
The standard exponential Markov argument for Bernoulli sums (with the same bound for negative \(t\)) proves (2).

**2. Loop-occupancy variance obstruction.** Let \(\mathcal L\) be the sigma-field of the labels on the \(s\) self-loops. Let \(Z_s\) be the number of colors absent from those labels. Their labels form \(s\) independent balls thrown into \(s\) boxes. Thus \(\mathbb EZ_s=sa_s\) and, using the probability \(b_s\) that two distinct boxes are empty,
\[
\operatorname{Var}(Z_s)=sa_s+s(s-1)b_s-s^2a_s^2=V_s.
\]
The non-self-loop edge labels are independent of \(\mathcal L\). For each color absent from the self-loops, the probability that its non-self-loop subgraph is acyclic is the common number \(q_{s,r}/a_s\); for a color present on a loop, the probability of being absent from the image is zero. Therefore the exact conditional expectation is
\[
 \mathbb E(M_{s,r}\mid\mathcal L)=(q_{s,r}/a_s)Z_s.
\]
The law of total variance gives the lower inequality of (1).

**3. Asymptotics.** Gravner and Kulhanek prove for \(r=2\) that \(q_{s,2}\sim c_*s^{-1/3}\). Elementary expansions give
\[
 a_s\longrightarrow e^{-1},\qquad V_s/s\longrightarrow e^{-1}-2e^{-2}.
\]
Substitution into (1) yields (3), since \((e^{-1}-2e^{-2})e^2=e-2\). The variance upper bound and the exact mean \(\mathbb E M_{s,2}=sq_{s,2}\) establish \(L^2\) convergence of \(M_{s,2}/s^{2/3}\) to \(c_*\). Since \(sq_{s,2}\sim c_*s^{2/3}\), (2) supplies a summable bound for fixed relative deviations. Borel--Cantelli then gives the almost-sure convergence for any joint realization across different \(s\), without any assumption of independence across sizes.

## Verification
The standalone standard-library program `check.py` exhaustively enumerates every uniform assignment of colors to the edges of the two-vertex and three-vertex complete directed graphs (\(16\) and \(19683\) assignments). It computes exact distributions and verifies both variance bounds, pairwise negative covariances and representative Laplace transform bounds. Executing `python check.py` reproduces the results in `check_output.txt`. These finite tests are diagnostic only; the infinite-dimensional assertions follow from the preceding proof. In particular, for \(s=2\), the exact variance is \(15/64\) and the loop-only lower bound is \(9/64\); for \(s=3\), these quantities are \(14396210/43046721\) and \(6396416/43046721\), respectively.

## Relationship to prior work
Gravner and Kulhanek (2026, Theorem 3 and Proposition 48) identify the one-color acyclicity probability and the asymptotic expectation of the missing count for \(r=2\); their result \(N_s/s\to1\) is on the larger \(s\) scale. Joag-Dev and Proschan (1983) establish classical closure properties of negative association for multinomial and other variables; these methods underlie the upper bound. The result here combines the coloring-specific negative-association structure with a separate, exact loop-occupancy variance decomposition, yielding two-sided variance information and concentration at the natural missing-color scale. The one-color Airy constant is inherited from the former paper rather than newly evaluated. Neither classical negative association alone nor the one-color asymptotic by itself yields the loop-occupancy lower bound.

## Limitations
The bounds in (3) have different powers and do not determine the sharp variance exponent, a central limit theorem, or the distribution of centered fluctuations. The exact concentration inequality is derived from standard negative-association methods. Historical coverage by general dependent-occupancy theorems cannot be excluded. The asymptotic statement is specific to neighborhood length two; for other fixed lengths only the exact finite-size inequalities (1)--(2) are asserted. The self-loop obstruction is a variance lower bound, not a typical-fluctuation lower-tail probability.

## References
1. J. Gravner and T. Kulhanek, *Random Cellular Automata and deBruijn Graphs* (2026), arXiv:2610.31764v1, https://arxiv.org/html/2610.31764v1, especially Theorem 3 and Proposition 48; publicly posted 2026-10-22.
2. K. Joag-Dev and F. Proschan, *Negative Association of Random Variables with Applications*, Annals of Statistics 11 (1983), 286--295, https://doi.org/10.1214/aos/1176346079.
