# Half-mass Poisson independence and first-order star limits on colored hypercubes

## Finding

Let \(C=\{1,\ldots,q\}\) be a fixed palette with \(q\ge2\) and strictly positive probabilities \(p_c\) summing to one. Color vertices of the \(d\)-dimensional hypercube \(Q_d\) independently with these probabilities. For every nonempty proper \(S\subset C\) and \(c\in C\), let \(X_{S,c}(d)\) count vertices of color \(c\) whose entire *open* graph neighborhood has colors in \(S\). Write \(p(S)=\sum_{c\in S}p_c\).

**Trichotomy.** If \(p(S)<1/2\), then \(X_{S,c}(d)\to0\) in probability. If \(p(S)>1/2\), then \(X_{S,c}(d)/[p_c(2p(S))^d]\to1\) in probability. For every set \(S\) with \(p(S)=1/2\), the entire collection of variables \(X_{S,c}(d)\), **simultaneously over all such sets and all center colors**, converges in total variation to mutually independent variables \(Z_{S,c}\sim\operatorname{Pois}(p_c)\).

Let \(\mathcal H=\{S\subset C:p(S)=1/2\}\), \(m=q|\mathcal H|\), and, for at least two critical sets, \(\rho=\max_{S\ne T\in\mathcal H}2p(S\cap T)\); put \(\rho=0\) if fewer than two exist. Because all palette probabilities are positive, \(0\le\rho<1\). There is a **finite-dimensional quantitative bound**, valid for every \(d\ge1\):

\[
d_{\mathrm{TV}}\!\left(\mathcal L\bigl((X_{S,c}(d))_{S\in\mathcal H,c\in C}\bigr),\ \bigotimes_{S,c}\operatorname{Pois}(p_c)\right)
\le 20m^2\left(1+d+\binom d2\right)2^{-d}+4m^2\rho^d.
\]

When \(\mathcal H=\varnothing\), the Poisson assertion is vacuous.

**First-order consequence.** In the language of hypercube adjacency \(E\) and unary color predicates \(P_c\), define \(\psi_{S,c,t}\), for any positive integer \(t\), to assert the existence of at least \(t\) distinct vertices of color \(c\) whose neighbors all have color in \(S\). Every fixed Boolean combination of these first-order sentences has a limiting probability. It is computed by replacing each \(\psi_{S,c,t}\) with false when \(p(S)<1/2\), true when \(p(S)>1/2\), and \(\{Z_{S,c}\ge t\}\) when \(p(S)=1/2\), using the independent Poisson family above. This is a complete limiting-probability evaluation procedure **for this star-threshold Boolean fragment**, not a claim about all first-order formulas on the hypercubes.

For the uniform palette, odd \(q\) has no half-mass set; hence this fragment obeys a zero–one law. Even \(q\) has \(\binom q{q/2}\) critical sets and \(q\binom q{q/2}\) independent critical Poisson variables, each of mean \(1/q\). For \(q=2\), the two assertions that some vertex has only color-1 neighbors and some vertex has only color-2 neighbors have joint limiting probability \((1-e^{-1})^2\).

## Assumptions and scope

The dimension \(d\) tends through positive integers; \(q\) and the probability vector are fixed, and every \(p_c>0\). The hypercube has exactly \(2^d\) vertices and degree \(d\). The random choices are **vertex colors**, not independently retained edges, and the neighborhood restriction excludes the center. The first-order language contains only adjacency and the disjoint unary color predicates; its structures satisfy exactly one color predicate at every vertex.

For \(t\ge1\), the sentence \(\psi_{S,c,t}\) is

\[
\exists x_1\cdots\exists x_t\,\left[\bigwedge_{i<j}x_i\ne x_j\;\wedge\;\bigwedge_{i=1}^t\left(P_c(x_i)\wedge\forall y\bigl(E(x_i,y)\longrightarrow\bigvee_{a\in S}P_a(y)\bigr)\right)\right].
\]

The statements apply to every nonempty proper palette subset, without an assumption that the color probabilities are rational.

## Proof

**1. Individual means and noncritical regimes.** Put \(\alpha=p(S)\). For each center \(x\), independence of its color from the colors of its \(d\) distinct neighbors gives

\[
\Pr\bigl(x\text{ counted by }X_{S,c}\bigr)=p_c\alpha^d,
\qquad\mathbb E X_{S,c}(d)=2^d p_c\alpha^d=p_c(2\alpha)^d.
\]

If \(\alpha<1/2\), Markov's inequality implies extinction. To treat \(\alpha>1/2\), note that two indicator events at centers of Hamming distance at least three depend on disjoint closed radius-one neighborhoods, so their covariance is zero. A vertex has \(d\) centers at distance one and \(\binom d2\) at distance two. For distinct centers at distance one or two, the joint event has probability at most \(p_c^2\alpha^{2d-2}\): at distance two their open neighborhoods overlap in exactly two vertices, while at distance one the centers constrain one another and the remaining neighbor sets are disjoint. Therefore, with \(D_d=1+d+\binom d2\),

\[
\operatorname{Var}(X_{S,c}(d))
\le2^dp_c\alpha^d+2^dD_d p_c^2\alpha^{2d-2},
\qquad
\frac{\operatorname{Var}(X_{S,c}(d))}{(\mathbb E X_{S,c}(d))^2}
\le\frac1{p_c(2\alpha)^d}+\frac{D_d}{2^d\alpha^2}\longrightarrow0.
\]

This proves concentration of every supercritical count.

**2. All critical colors and palettes at once.** Index the critical Bernoulli indicators by triples \(i=(x,S,c)\) with \(x\in\{0,1\}^d\), \(S\in\mathcal H\), and \(c\in C\). Let \(I_i\) indicate that the color of \(x\) is \(c\) and all open neighbors lie in \(S\). Each has \(\Pr(I_i=1)=p_c2^{-d}\). Declare triples dependent whenever their centers have Hamming distance at most two. Outside this dependency neighborhood the input vertex-color sets are disjoint; consequently the conditional-dependence term \(b_3\) of the Arratia–Goldstein–Gordon Poisson-process inequality is zero.

There are \(2^dm\) triples and at most \(mD_d\) dependent triples per triple. Thus, using \(p_c\le1\),

\[
b_1=\sum_i\sum_{j\in B_i}\Pr(I_i=1)\Pr(I_j=1)\le m^2D_d2^{-d}.
\]

For distinct triples sharing a center, positive intersection requires the **same center color** and **different critical palettes** \(S\ne T\). Its probability is exactly \(p_c p(S\cap T)^d\). Summing these ordered pairs of events over centers and types bounds this contribution to \(b_2\) by \(m^2\rho^d\). Strict positivity of every palette mass ensures \(\rho<1\): distinct equal-half-mass sets cannot contain one another, so their intersection has mass strictly below \(1/2\).

For different centers with distance one or two, the total number of constrained vertices is at least \(2d-2\): open neighbor sets are disjoint for adjacent centers, and overlap in exactly two points for centers at distance two. Extra restrictions from center colors can only decrease the probability. Every open-neighbor restriction has individual allowed mass \(1/2\), and intersecting two such restrictions has allowed mass at most \(1/2\); hence every such joint indicator probability is at most \(2^{-(2d-2)}\). There are at most \(2^dD_dm^2\) ordered pairs, giving

\[
b_2\le m^2\rho^d+4m^2D_d2^{-d}.
\]

Theorem 2 of Arratia, Goldstein and Gordon (1989) bounds the total variation distance from the complete dependent Bernoulli **point process** to independent Poisson variables with matching means by \(4(b_1+b_2)\) when \(b_3=0\). Summing those independent Poisson variables over all centers separately for each type \((S,c)\), and contracting total variation under this deterministic coordinate map, gives mutually independent \(\operatorname{Pois}(2^d p_c2^{-d})=\operatorname{Pois}(p_c)\) coordinates. Substitution of the bounds proves the displayed quantitative inequality. This method controls the **joint count vector** rather than only the sum of its coordinates.

**3. Logical evaluation and parity.** The sentence \(\psi_{S,c,t}\) is equivalent to \(X_{S,c}(d)\ge t\). By Step 1 every noncritical fixed threshold has deterministic limiting truth; by Step 2 the finite vector of critical counts converges in total variation, which preserves the probabilities of all threshold events and their finite Boolean combinations. A uniform palette has \(p(S)=|S|/q\), which equals \(1/2\) exactly for half-sized palettes, hence the parity classification. For \(q=2\), summing the two independent \(\operatorname{Pois}(1/2)\) center-color counts for each of the two critical neighbor sets gives two independent \(\operatorname{Pois}(1)\) totals. Their joint positivity probability is \((1-e^{-1})^2\).

## Verification

A standalone checker named `checker.py` evaluates exact joint event probabilities using rational vertex-color weights and intersection of the color constraints at every vertex, for binary cubes through dimension four, a nonuniform three-color palette, and a uniform four-color palette. It checks exact single-event probabilities, factorization for separated centers, the same-center intersection identity, and the short-distance bound used in the Poisson estimate. For the stated cases it performs **82,096 exact indicator-pair tests**. It separately enumerates all colorings for selected small dimensions and checks the exact critical count means, yielding **203 distinct observed joint count states**. Execution prints `ALL_CHECKS_OK`. Finite enumeration is not a proof of the asymptotic assertion, which follows from the independent-neighborhood calculation and the cited Poisson-process theorem.

To replay, execute `python3 checker.py` with the standard Python 3 library; no downloads are required.

## Relationship to prior work

Ghosh and Schwarzentruber (2026) study modal counting and convergence over random graph/tree models, supplying the motivating logical setting; they do not treat iid vertex colors of deterministic growing hypercubes or the simultaneous palette-star counts. Weber (1987) proved Poisson phenomena for isolated subcubes and degrees in random site/bond subgraphs of the binary cube, a particularly close precedent: the single retained-isolated-vertex count corresponds to a special two-color star event. The present finding does **not** claim that isolated-vertex Poisson approximation itself is new; its asserted increment is joint independence for every critical neighbor palette and marked center color, the sharp palette-mass trichotomy, and the induced logical-fragment classification. The complete text of Weber (1987) was unavailable for detailed theorem-by-theorem comparison, so equivalent multivariate statements remain an explicit originality risk.

Arratia, Goldstein and Gordon (1989), Theorem 2, provide the general point-process Poisson approximation used here, and their paper already includes an illustrative inward-edge-orientation Poisson law on the hypercube. That orientation model uses **independent edge directions**, not independent vertex colors. Xie and Bhattacharya (2024) establish joint laws of monochromatic hyperedge counts under other hypotheses, prominently fixed uniformity and potentially growing numbers of colors; their full-text theorems do not state this marked growing-degree vertex-neighborhood spectrum. Przykucki, Roberts and Scott (2019/2021) study reconstruction from randomly colored hypercube balls, rather than these asymptotic joint count laws. Janson, Seidler and Zeilberger (2023) study counts of **fixed-dimensional contained subcubes** and their asymptotic normality, not stars of growing degree and bounded expected count.

## Limitations

Only fixed \(q\), strictly positive palette probabilities, and independently colored vertices are covered. No convergence theorem is asserted for arbitrary first-order formulas or for growing numbers of colors. When the critical palette family is empty the first-order star fragment is deterministic in the limit; when it is nonempty the evaluation formula supplies limits but does not offer a finite closed-form enumeration of all values generated by arbitrary Boolean combinations. The quantitative bound may be numerically trivial at small dimensions. Weber's full text could not be obtained, and older specialized site-percolation literature may contain overlapping multivariate statements; independent literature review and independent proof audit have not been performed.

## References

1. A. Ghosh and F. Schwarzentruber, *On Counting Graphs for Modal Logic with Counting*, arXiv:2610.26187v1 (first posted 19 October 2026). https://arxiv.org/html/2610.26187v1
2. R. Arratia, L. Goldstein and L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen–Stein Method*, Annals of Probability 17 (1989), 9–25. https://doi.org/10.1214/aop/1176991491
3. K. Weber, *Poisson Convergence in the n-Cube*, Mathematische Nachrichten 131 (1987), 49–57. https://doi.org/10.1002/mana.19871310105 (abstract and bibliographic material inspected; complete text unavailable).
4. Y. Xie and B. B. Bhattacharya, *Joint Poisson Convergence of Monochromatic Hyperedges in Multiplex Hypergraphs*, arXiv:2412.00610v1 (2024). https://arxiv.org/abs/2412.00610
5. M. Przykucki, A. Roberts and A. Scott, *Shotgun Reconstruction in the Hypercube*, arXiv:1907.07250 (2019); Random Structures & Algorithms (2021). https://arxiv.org/abs/1907.07250
6. S. Janson, B. Seidler and D. Zeilberger, *On the Statistics of the Number of Fixed-Dimensional Subcubes in a Random Subset of the n-Dimensional Discrete Unit Cube*, preprint dated 17 February 2023. https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimPDF/subcubes.pdf
