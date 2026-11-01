# Exact cherry–Sackin covariance and sharp decorrelation in uniform phylogenetic trees

## Finding
Let \(T_n\) be uniformly distributed over rooted, ordered, full binary trees with exactly \(n\) leaves. Write \(C_n\) for the number of cherries (internal vertices whose two children are leaves), and \(S_n\) for the sum of the root-to-leaf edge depths, with the root at depth zero. Define
\[
q_n=\frac{4^{n-1}}{\binom{2n-2}{n-1}}.
\]
For every integer \(n\geq 2\),
\[
\boxed{\operatorname{Cov}(C_n,S_n)
=\frac{n}{2n-3}\left(n-1-\frac{nq_n}{4}\right).}
\]
The covariance is zero at \(n=2,3\), and **strictly negative for every \(n\geq4\)**. In particular,
\[
\operatorname{Cov}(C_n,S_n)\sim-\frac{\sqrt\pi}{8}n^{3/2}.
\]
The exact variance of cherry count for \(n\geq3\) is
\[
\operatorname{Var}(C_n)=\frac{n(n-1)(n-2)(n-3)}{2(2n-5)(2n-3)^2}.
\]
Using the established uniform-model Sackin variance asymptotic, the correlation has the **sharp rate and constant**
\[
\boxed{\sqrt n\,\operatorname{Corr}(C_n,S_n)
\longrightarrow-\frac{\sqrt\pi}{2\sqrt{10/3-\pi}}.}
\]
This correlation is defined for \(n\geq4\). The same shape-statistic statements hold under the uniform labeled rooted phylogenetic (PDA) model after left–right ordering is forgotten.

## Assumptions and scope
All trees are finite, rooted and fully binary: an internal vertex has exactly two children. Every ordered shape with \(n\) leaves has equal probability \(1/\mathrm{Cat}_{n-1}\), where \(\mathrm{Cat}_{n-1}=\binom{2n-2}{n-1}/n\). The single-leaf tree has zero cherries and zero depth sum. A cherry is defined by the children being leaves, not by labeling or branch lengths.

For a non-ordered unlabelled shape with \(a\) independent mirror-symmetric internal vertices, the number of ordered realizations is \(2^{n-1-a}\), whereas the number of distinct assignments of \(n\) labels to its leaves is \(n!/2^a\). Their ratio is constant across shapes, so both sampling laws induce the same distribution for every shape-dependent statistic. This establishes the PDA interpretation without treating the Yule model as equivalent.

## Proof
**Step 1: exact mixed generating function.** Work with formal power series in \(x\), so no analytic convergence assumption is required. Let \(T(x)\), \(C(x)\), \(S(x)\) and \(M(x)\) sum, respectively, \(1\), cherry count, Sackin depth sum and their product over every ordered full binary tree, with weight \(x\) per leaf. Put \(s=\sqrt{1-4x}\), the formal square root with constant term \(1\). Root decomposition gives
\[
T=x+T^2=\frac{1-s}{2},\qquad C=2TC+x^2=\frac{x^2}{s}.
\]
As joining two subtrees adds one to the depth of every leaf,
\[
S=2TS+x\frac{d}{dx}T^2
=\frac{x(1-s)}{s^2}.
\]
For the product, expand
\[
(C_L+C_R+I)(S_L+S_R+n),
\]
where \(I=1\) only when both child subtrees are single leaves. Accounting for contributions from the two descendant subtrees, cross-products, the new depths and the two-leaf tree gives
\[
M=2TM+2CS+x\frac{d}{dx}(2TC)+2x^2.
\]
Since \(2TC=C-x^2\), this reduces to
\[
M=\frac{2CS+xC'}{s}
=\frac{2x^2}{s^2}+\frac{4x^3}{s^4}-\frac{2x^3}{s^3}.
\]
Every identity follows coefficientwise from disjoint root decompositions; in particular the final term \(2x^2\) in the recurrence handles the cherry at the root of the unique two-leaf tree.

**Step 2: coefficient extraction.** For \(n\geq3\), using binomial-series identities,
\[
\begin{aligned}
[x^n]T&=\frac1n\binom{2n-2}{n-1},\\
[x^n]C&=\binom{2n-4}{n-2},\\
[x^n]S&=4^{n-1}-\binom{2n-2}{n-1},\\
[x^n]M&=n4^{n-2}-2(2n-5)\binom{2n-6}{n-3}.
\end{aligned}
\]
For \(n=2\), these moment sums are \(1\), \(1\), \(2\), \(2\), respectively. Dividing by the Catalan count and simplifying yields for every \(n\geq2\)
\[
\begin{aligned}
\mathbb E C_n&=\frac{n(n-1)}{2(2n-3)},\\
\mathbb E S_n&=n(q_n-1),\\
\mathbb E(C_nS_n)&=\frac{n^2q_n}{4}-\frac{n(n-1)(n-2)}{2(2n-3)}.
\end{aligned}
\]
Subtracting the product of expectations proves the displayed covariance identity.

**Step 3: its sign for every size.** For \(n=2,3\), the number of cherries is deterministic and the covariance is zero. For \(n\geq3\) compare \(q_n\) with \(a_n=4(n-1)/n\). At \(n=3\), \(q_3=a_3=8/3\). Their exact consecutive ratios are
\[
\frac{q_{n+1}}{q_n}=\frac{2n}{2n-1},\qquad
\frac{a_{n+1}}{a_n}=\frac{n^2}{n^2-1}.
\]
The first ratio is strictly greater when \(n>2\), because this inequality is equivalent to \(n(n-2)>0\). Thus \(q_n>a_n\) for all \(n\geq4\), proving strict negativity, with no omitted intermediate sizes.

**Step 4: exact variance and sharp decorrelation.** Mark each cherry by \(y\). The bivariate counting series satisfies \(T(x,y)=x+T(x,y)^2+(y-1)x^2\). At \(y=1\), its first and second derivatives are \(x^2/s\) and \(2x^4/s^3\). Taking coefficients gives the second factorial moment and the displayed exact variance of \(C_n\). Therefore \(\operatorname{Var}(C_n)\sim n/16\). Also \(q_n\sim\sqrt{\pi n}\) by the central-binomial asymptotic, so the mixed covariance is asymptotic to \(-\sqrt\pi n^{3/2}/8\). For the same uniform tree model, Blum, François and Janson established
\[
\operatorname{Var}(S_n)\sim(10/3-\pi)n^3.
\]
Dividing the covariance by both standard deviations gives the asserted correlation limit. Both variances are strictly positive for \(n\geq4\): cherry variance by its exact formula and Sackin variance because there are shapes of different total depth.

## Verification
The accompanying standalone `verify.py` checks all rooted ordered binary shapes with \(2\leq n\leq11\) leaves by exact fractions and independently checks root-composition raw-moment recurrences through \(n=120\). It also tests the sign for \(121\leq n\leq200\) and the covariance asymptotic at four larger values; it reports **868 successful assertions**. Exhaustive checking stops at \(n=11\); the infinite statements rest entirely on the formal-series identities, exact comparison of consecutive ratios and established Sackin variance asymptotic, not on finite numerical evidence.

To reproduce: run `python verify.py` using Python 3 with no nonstandard packages.

## Relationship to prior work
Blum, François and Janson (2007 preprint, originally published 2006) establish the uniform-tree Sackin variance and its Airy limit, jointly with the Colless index; their results do not state a cherry–Sackin covariance. Chang and Fuchs (2009 preprint) provide means, variances and limit laws for fixed fringe-tree patterns, including cherries, but not the mixed covariance with global leaf-depth sum. Janson (2013) provides conditioned-Galton–Watson fringe-functional central limit theory, not this mixed finite-sample identity. Wu and Choi (2015) study the joint number of cherries and pitchforks, not their covariance with Sackin depth. A later multivariate generating-function framework (Norton, 2025) formally marks cherry and Sackin statistics together, but no explicit evaluated mixed coefficient, universal strict-sign theorem or sharp correlation constant was located in that text. These comparisons are statements of inspected coverage, not a claim of exhaustive historical priority.

## Limitations
The covariance sign addresses linear dependence only, not stochastic ordering, independence, or higher-dimensional joint laws. The correlation asymptotic invokes the published Sackin variance theorem; its constant is not independently rederived here. At \(n=2,3\), cherry count is deterministic, so correlation is undefined. Other tree distributions such as Yule–Harding need not satisfy the same formulas. A historically equivalent result could exist under alternative names; no independent external audit has been conducted.

## References
- M. G. B. Blum, O. François and S. Janson, *The mean, variance and limiting distribution of two statistics sensitive to phylogenetic tree balance*, arXiv:math/0702415v1 (public preprint 2007-02-14), especially Theorem 3 and Remark 3. https://arxiv.org/abs/math/0702415
- H. Chang and M. Fuchs, *Limit theorems for patterns in phylogenetic trees*, preprint dated 2009-04-13; DOI: 10.1007/s00285-009-0275-6. https://web.math.nccu.edu.tw/mfuchs/parameters_pt_rev.pdf
- S. Janson, *Asymptotic normality of fringe subtrees and additive functionals in conditioned Galton–Watson trees*, arXiv:1312.1211v1 (2013-12-04). https://arxiv.org/abs/1312.1211
- T. Wu and K. P. Choi, *On joint subtree distributions under two evolutionary models*, manuscript 2015-11-05, DOI: 10.1016/j.tpb.2015.11.004. https://ueaeprints.uea.ac.uk/id/eprint/55603/
- C. Norton, *A Unified Generating Function Framework for Tree Invariants*, publicly available text (2025). https://github.com/CharlesCNorton/unified-tree-theory
