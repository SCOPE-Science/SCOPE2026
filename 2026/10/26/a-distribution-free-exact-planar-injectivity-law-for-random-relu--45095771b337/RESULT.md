# A distribution-free exact planar injectivity law for random ReLU layers

## Finding
Let \(m\ge4\) and let \(W\in\mathbb R^{m\times2}\) have independent random rows \(w_1,\dots,w_m\). Each row has a centrally symmetric distribution, \(w_i\overset d=-w_i\), and assume almost surely every row is nonzero and no two rows are collinear. The row laws need not be identical or rotationally invariant. For \(F_W:\mathbb R^2\to\mathbb R^m\) given by \(F_W(x)=\bigl(\max(0,w_i\cdot x)\bigr)_{i=1}^m\),
\[
\boxed{\Pr\{F_W\text{ is globally injective}\}=1-\frac{m(m-2)}{2^{m-1}}.}
\]
For \(m\le3\) the probability is zero. In particular, among nondegenerate continuously distributed independent symmetric rows, width five is the first width with positive injectivity probability (\(1/16\)); widths six and eight have probabilities \(1/4\) and \(5/8\), respectively. The exact conditional number of successful orientation assignments for *every deterministic configuration* of \(m\) distinct unoriented lines is
\[
\boxed{2^m-2m(m-2).}
\]
This last statement is a geometric counting theorem, not merely a Gaussian-specific distributional identity.

## Assumptions and scope
The domain is the whole \(\mathbb R^2\), the activation is coordinatewise zero-bias ReLU, and \(m\) is an integer. The probability law is over the independent rows, whose centrally symmetric distributions may differ. No density or moment assumption is needed beyond almost-sure nonvanishing and absence of pairwise collinearity. For the auxiliary circular-spacing calculation only, rows have independent uniform angular directions, for example independent isotropic Gaussian rows. The output is not restricted to a compact domain or cone. Scaling rows by positive nonzero factors and scaling all preactivations by a fixed positive constant leave injectivity unchanged.

## Proof
**1. Exact injectivity criterion.** Fix a deterministic matrix with nonzero, pairwise noncollinear rows. If some open angular chamber of input directions has fewer than two rows with positive inner product, the ReLU layer has rank less than two on an open cone and is not injective. Conversely, suppose every such chamber has at least two positive rows. At a boundary ray precisely one row has zero inner product. Its positive-row count equals that of the adjacent chamber where this row is negative, and is still at least two. If \(F_W(a)=F_W(b)\), let \(z=(a+b)/2\). Every row with \(w_i\cdot z\ge0\) annihilates \(a-b\): if its two outputs are positive then the two preactivations coincide; if both outputs vanish and the midpoint preactivation is nonnegative, both preactivations are zero. Any two such rows are linearly independent, hence \(a=b\). For \(z=0\), all rows have zero midpoint and independently span \(\mathbb R^2\) for \(m\ge2\), so the same conclusion holds. This argument also handles boundary rays; it reconstructs the elementary geometric criterion used in the cited injectivity literature.

The positive-row count in direction \(u\) equals the number of row directions within the open semicircle centered on \(u\). Therefore injectivity is equivalent, in general position, to every open semicircle containing at least two row directions.

**2. Configuration-independent sign law.** Condition on each unoriented line spanned by a row. Central symmetry and independence make the orientation of each row an independent fair sign. Rotate a test input direction through an angle \(\pi\), starting at a generic direction. Each of the \(m\) distinct row-normal lines is crossed exactly once, in some order. Write \(b_j\in\{0,1\}\) for whether the row crossing at step \(j\) is initially active. These \(b_j\) are independent fair bits. The successive active-row counts are
\[
H_k=\sum_{j\le k}(1-b_j)+\sum_{j>k}b_j,\qquad k=0,\ldots,m.
\]
During the complementary half-turn the counts are \(m-H_k\). Hence the injectivity event is exactly \(2\le H_k\le m-2\) for every \(k\). Its conditional probability depends only on the uniform word \((b_1,\dots,b_m)\), not the line angles. Consequently the conditional probability, and the number of good orientation assignments, are deterministic functions of \(m\). It suffices to compute that probability for isotropically distributed rows.

**3. Exact circular-spacing evaluation.** For independent uniform angles, list them in circular order and let \(g_1,\dots,g_m>0\) be consecutive normalized angular gaps summing to one. Their joint distribution is \(\operatorname{Dirichlet}(1,\dots,1)\). Almost surely no pair of sample angles is antipodal. Every open semicircle contains at least two sample points exactly when
\[
g_i+g_{i+1}<\tfrac12\quad\text{for every cyclic }i.
\]
Let \(A_i=\{g_i+g_{i+1}>1/2\}\). For \(m\ge4\), two nonadjacent bad events cannot both occur: their respective pairs of gaps are disjoint and would sum to more than one. Therefore no triple of bad events can occur, and the only nonzero pairwise intersections are those between adjacent indices. By the beta marginal law,
\[
\Pr(A_i)=\Pr\{\operatorname{Beta}(2,m-2)>1/2\}=\frac{m}{2^{m-1}}.
\]
To calculate adjacent overlap, condition on the shared gap \(x=g_{i+1}\), whose density is \((m-1)(1-x)^{m-2}\). When \(x\ge1/2\) both inequalities hold. For \(0<x<1/2\), the remaining normalized gaps have a uniform Dirichlet law, so the conditional joint probability is \((x/(1-x))^{m-2}\). Consequently
\[
\begin{aligned}
\Pr(A_i\cap A_{i+1})
&=2^{-(m-1)}+(m-1)\int_0^{1/2}x^{m-2}\,dx\\
&=2^{-(m-2)}.
\end{aligned}
\]
There are precisely \(m\) singleton events and \(m\) adjacent pairs. Inclusion-exclusion (which terminates at pairs, not as an approximation) yields
\[
\Pr\Bigl(\bigcup_i A_i\Bigr)
=m\frac{m}{2^{m-1}}-m\frac1{2^{m-2}}
=\frac{m(m-2)}{2^{m-1}}.
\]
Taking complements proves the probability formula. Since independent fair orientations realize every one of \(2^m\) possibilities equiprobably, the universal deterministic good-orientation count is \(2^m\) times this probability, namely \(2^m-2m(m-2)\). For \(m<4\), no general-position ReLU layer can be globally injective because fewer than twice the input dimension rows cannot meet the chamber criterion. For \(m=4\), the displayed formula already yields zero.

## Verification
The standalone standard-library script `verification/verify_planar.py` exhaustively enumerates the independent sign-word criterion for every \(4\le m\le13\) and checks the exact integer counts. It also enumerates orientations for 24 deterministic line configurations (including tightly clustered directions), independently compares the gap criterion with direct semicircle-point counts in 16,000 random configurations, and performs four Monte Carlo diagnostics. Run from the package root: `python verification/verify_planar.py`. The included `verification/verification_output.txt` records its actual output. These finite checks are supplemental; the preceding Dirichlet calculation and conditional-sign argument prove the infinite family.

## Relationship to prior work
Puthawala et al. (2022) prove deterministic injectivity criteria and Gaussian high-dimensional bounds. Maillard et al. (first preprint 2023) formulate Gaussian-layer injectivity through random subspaces and high-dimensional statistical mechanics. Xie (first public October 5, 2026) proves a sharp large-dimensional threshold and a global positive-row-count criterion. The present finding applies this criterion in the *fixed two-dimensional input setting* to evaluate an exact finite-width law and shows a distribution-free conditional sign-count universality even for non-identically distributed centrally symmetric rows. Wendel's classical formula treats the existence of a semicircle containing *all* sample directions (zero depth), not the two-per-semicircle property needed here. The above comparison concerns mathematical statements, not merely their titles.

## Limitations
The formula requires independent centrally symmetric rows and general position; it does not extend as stated to dependent signs, rows supported on a common line, biased layers, or input dimension three or larger. The count is specific to the threshold of two active rows. Prior work on higher-order circular coverage or random halfspace-depth distributions might contain an equivalent formula under different terminology; its full historical exclusion is not claimed. The proof establishes a probability, not an injectivity condition number. No independent mathematical audit has been performed.

## References
1. X. Xie, *The injectivity threshold of a Gaussian ReLU layer*, arXiv:2610.07492v1, first posted 2026-10-05, https://arxiv.org/abs/2610.07492 .
2. M. Puthawala, K. Kothari, M. Lassas, I. Dokmanić and M. de Hoop, *Globally Injective ReLU Networks*, Journal of Machine Learning Research 23(105), 2022, https://www.jmlr.org/papers/v23/21-0282.html .
3. A. Maillard, A. S. Bandeira, D. Belius, I. Dokmanić and S. Nakajima, *Injectivity of ReLU networks: perspectives from statistical physics*, arXiv:2302.14112 (first posted 2023-02-27), https://arxiv.org/abs/2302.14112 .
4. J. G. Wendel, *A problem in geometric probability*, Mathematica Scandinavica 11 (1962), 109–111, https://doi.org/10.7146/math.scand.a-10655 .
