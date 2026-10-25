# Isolation covariance reverses sign across three bipartite edge-sampling ensembles

## Finding

Let \(a,b\ge2\), \(N=ab\), and let \(X\) and \(Y\) be the numbers of degree-zero vertices in the left and right classes, respectively, of a bipartite graph on fixed labeled classes of sizes \(a\) and \(b\). Three standard ways to sample edges give opposite or vanishing signs for the same pair of statistics.

**Fixed-distinct-edge model.** Choose exactly \(m\in\{0,\ldots,N\}\) distinct potential edges uniformly. Put \(h_m(s)=\binom{s}{m}/\binom{N}{m}\), with \(\binom{s}{m}=0\) for \(s<m\). Then
\[
\operatorname{Cov}(X,Y)=ab\left[h_m((a-1)(b-1))-h_m((a-1)b)h_m(a(b-1))\right].
\]
Its sign is strictly negative for every \(2\le m\le N-\max\{a,b\}\), and exactly zero for the remaining permissible \(m\).

**Independent-edge model.** Include every potential edge independently with probability \(p\in(0,1)\). Then
\[
\operatorname{Cov}(X,Y)=abp(1-p)^{a+b-1}>0.
\]
Moreover, if \(E\) is the total number of edges, the following exact rank-one covariance identity holds:
\[
\operatorname{Cov}(X,Y)=\frac{\operatorname{Cov}(X,E)\operatorname{Cov}(Y,E)}{\operatorname{Var}(E)}.
\]
This identity is about ordinary covariances; it does not assert that conditioning on \(E\) leaves zero covariance.

**With-replacement model.** Draw \(m\ge0\) independently uniform ordered pairs of left and right endpoints (repeated pairs permitted); isolated means incident to no drawn pair. Then \(X\) and \(Y\) are independent, so \(\operatorname{Cov}(X,Y)=0\).

**Sparse constant.** If \(a/n\to\alpha>0\), \(b/n\to\beta>0\), and the integer count \(m/n\to\gamma>0\) as \(n\to\infty\), then, for uniform fixed-distinct-edge sampling,
\[
\operatorname{Cov}(X,Y)\longrightarrow
-\frac{\gamma^2}{2\alpha\beta}
\exp\!\left[-\gamma\left(\frac1\alpha+\frac1\beta\right)\right].
\]
For the matched independent-edge choice \(p=m/(ab)\), whose expected edge number is also \(m\),
\[
\frac{\operatorname{Cov}(X,Y)}n\longrightarrow
\gamma\exp\!\left[-\gamma\left(\frac1\alpha+\frac1\beta\right)\right].
\]
In particular, with \(a=b=n\) and \(m/n\to c>0\), the fixed-edge covariance converges to \(-\tfrac12c^2e^{-2c}\), while the independent-edge covariance grows as \(cn e^{-2c}\). These are not equivalent ensembles at the covariance scale, notwithstanding the matching expected edge number.

## Assumptions and scope

Vertex classes are labeled, every potential cross-edge is distinct, and no edges within a class are allowed. In the fixed-distinct-edge and independent-edge models the graph is simple. With-replacement sampling uses endpoint pairs with multiplicity for sampling but only the event of at least one incident draw matters for isolation. The exact results hold for every integer \(a,b\ge2\); \(0\le m\le ab\) in the fixed-distinct model, any \(m\ge0\) in the with-replacement model, and \(0<p<1\) in the independent-edge model. The sparse statement assumes the displayed convergence with positive constants and integer-valued dimensions and counts.

## Proof

Denote \(R=(a-1)b=N-b\), \(C=a(b-1)=N-a\), and \(J=(a-1)(b-1)=N-a-b+1\). In the fixed-distinct model, a specified left vertex is isolated precisely when all selected edges avoid its \(b\) incident cells, an event of probability \(h_m(R)\). A specified right vertex has isolation probability \(h_m(C)\); both are isolated iff all edges fall among the \(J\) cells avoiding both, of probability \(h_m(J)\). Sum the covariance of their two isolation indicators over all \(ab\) cross-class vertex pairs. This establishes the exact formula.

If \(m\le J\), division by the positive product of the two marginal probabilities gives
\[
\frac{h_m(J)}{h_m(R)h_m(C)}
=\prod_{t=0}^{m-1}\frac{(J-t)(N-t)}{(R-t)(C-t)}
=\prod_{t=0}^{m-1}\left(1-\frac{t}{(R-t)(C-t)}\right),
\]
where the second equality follows from the elementary identity \((R-t)(C-t)-(J-t)(N-t)=t\). The factor for \(t=0\) is one; when \(m\ge2\), the factor for \(t=1\) is strictly less than one and every remaining factor lies in \((0,1]\). Thus the covariance is negative for \(2\le m\le J\), and zero for \(m=0,1\). If \(J<m\le\min\{R,C\}\), the joint isolation event is impossible while both marginals are possible, again giving strict negativity. If \(m>\min\{R,C\}=N-\max\{a,b\}\), at least one class has no isolated vertices with probability one, so the covariance is zero. This proves the complete finite sign classification.

In the independent-edge model let \(q=1-p\). A specified left vertex is isolated with probability \(q^b\), a right vertex with probability \(q^a\), and the pair jointly with probability \(q^{a+b-1}\), since their edge stars share exactly one cell. Their covariance is \(pq^{a+b-1}\), establishing the stated formula. For the edge count \(E\), linearity over incident edge indicators gives
\[
\operatorname{Cov}(X,E)=-abp q^b,\qquad
\operatorname{Cov}(Y,E)=-abp q^a,\qquad
\operatorname{Var}(E)=abpq.
\]
Substitution proves the rank-one identity. For the with-replacement model, the entire sequence of sampled left endpoints is independent of the entire sequence of sampled right endpoints, so the numbers of labels missed in these two sequences are independent.

For the sparse limit, the hypotheses imply \(N=\Theta(n^2)\), \(R,C,J=\Theta(n^2)\), and \(m=O(n)\). Taking logarithms in the exact falling-factorial ratios yields
\[
\log h_m(R)=-\frac{m}{a}+O(n^{-1}),\qquad
\log h_m(C)=-\frac{m}{b}+O(n^{-1}).
\]
The product identity and a uniformly valid Taylor expansion yield
\[
\log\frac{h_m(J)}{h_m(R)h_m(C)}
=-\frac{m(m-1)}{2N^2}+O(n^{-3}).
\]
Indeed, each factor has decrement \(t/((R-t)(C-t))=O(n^{-3})\), and summing its leading term produces \(m(m-1)/(2N^2)\) with total error \(O(n^{-3})\). Therefore
\[
\operatorname{Cov}_{\mathrm{fixed}}(X,Y)
=ab h_m(R)h_m(C)\left[-\frac{m(m-1)}{2N^2}+O(n^{-3})\right],
\]
which tends to the negative constant claimed. Finally, insert \(p=m/N\) into the independent-edge exact formula and use \(p=\Theta(n^{-1})\) and \((a+b-1)p\to\gamma(1/\alpha+1/\beta)\).

## Verification

A standalone standard-library Python program, `verify.py`, enumerates fixed-edge graphs for \(2\le a,b\le4\) and all admissible edge counts (90 strata), independent-edge graphs for four small rectangle sizes and three rational probabilities (12 cases), and replacement-draw sequences for four rectangle sizes and four counts (16 cases). It uses exact fractions for finite identities. It also evaluates the balanced sparse limit at six increasing sizes. Running `python3 verify.py` produces the `VERIFY_OK` terminal line. The finite checks do not constitute an infinite proof; the preceding combinatorial identities and asymptotic expansions do.

## Relationship to prior work

Bohman, Warnke and Zhu (arXiv:2401.10486; first posted 2024-01-19) analyze isolated-vertex counts in a **binomial** random bipartite graph to prove a Poisson-type approximation for a domination-number problem; their variance calculations are in the independent-edge ensemble. Blasiak and Durrett's *Random Oxford Graphs* explicitly use random endpoint draws **with replacement**, for which the left and right endpoint-label sequences are independent. Glebov, Luria and Simkin (arXiv:1805.06944) study the disappearance of isolated vertices during random bipartite edge exposure to obtain matching hitting-time results. These sources respectively overlap with the motivation, the zero-covariance case, and the fixed-edge sampling setting; their inspected primary text does not establish the stated all-parameter opposite-class fixed-edge covariance sign and its nonzero sparse limit. The Bernoulli and with-replacement formulas above are included for comparison, not asserted independently as first discoveries.

## Limitations

The fixed-edge formulas concern **one** left-side and **one** right-side aggregate, not arbitrary vectors of degree statistics or all subgraph correlations. The exact sign classification does not state stochastic negative dependence for their full joint distribution. The sparse limit fixes positive linear class sizes and edge counts and does not extend automatically to unbalanced or dense scales. The logarithmic expansion's constants depend on the limiting positive parameters. The source comparisons cannot exclude a historically earlier presentation of an equivalent hypergeometric calculation; the priority assessment is based on inspected relevant primary sources and search evidence, not an exhaustive claim across all literature. No independent audit has been performed.

## References

1. T. Bohman, L. Warnke and E. Zhu, *Two-Point Concentration of the Domination Number of Random Graphs*, arXiv:2401.10486 (publicly posted 2024-01-19), https://arxiv.org/abs/2401.10486 .
2. J. Blasiak and R. Durrett, *Random Oxford Graphs*, Stochastic Processes and their Applications 115 (2005), DOI 10.1016/j.spa.2005.03.008; author-hosted full text https://sites.math.duke.edu/~rtd/RG/rndgr0604.pdf .
3. R. Glebov, Z. Luria and M. Simkin, *Perfect Matchings in Random Subgraphs of Regular Bipartite Graphs*, arXiv:1805.06944, https://arxiv.org/abs/1805.06944 .
