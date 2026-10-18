# A sharp failure of budget nesting in two-habitat biodiversity sampling

## Finding

Suppose two finite habitats contain individuals of finitely many identifiable species. For each integer survey budget \(m\), one chooses nonnegative integers \(x,y\) with \(x+y=m\), draws \(x\) individuals uniformly without replacement from habitat A and \(y\) independently and uniformly without replacement from habitat B, and maximizes the **expected number of distinct species in the union**. Call an optimal allocation *extendable* to the next budget when one can add a draw to one habitat without retracting earlier habitat commitments.

**Theorem (sharp nonnesting and unbounded redesign).** In every two-habitat finite census with at most five individuals, one can select optimal allocations for *all* budgets so that each successive allocation adds exactly one draw in one habitat. With six individuals the property can fail. Up to relabelling of habitats and species, precisely three six-individual abundance configurations lack such a globally nested optimum sequence; among them precisely one already has two **consecutive budgets with no compatible optimal allocations**. That configuration has A-species abundances \((1,1,0)\), B-species abundances \((2,1,1)\). At budget \(m=2\), taking both draws in A is uniquely optimal; at budget \(m=3\), taking all three draws in B is uniquely optimal.

The displacement is unbounded. For **every** integer \(r\ge2\), and **every** integer \(K\ge r+2\), there is a census of \(r+K\) individuals in which budget \(r\) uniquely requires all \(r\) draws in A, while budget \(r+1\) uniquely requires all \(r+1\) draws in B. Thus a one-unit increase in survey budget can require abandoning arbitrarily many earlier allocations, when plans are independently reoptimized. Conversely, when the two habitats have disjoint species sets, nested optimal allocations exist for every budget and census size.

## Assumptions and scope

Species are indexed by \(s\), with nonnegative integer abundances \(a_s,b_s\), not both zero. The habitats each contain at least one individual, \(A=\sum_s a_s\ge1\) and \(B=\sum_s b_s\ge1\), and \(N=A+B\). All individuals within a habitat are equally likely to be sampled, sampling is without replacement **within** that habitat, the samples in the habitats are independent, and species labels are recognized without error. All draws have equal cost; the abundance census is known at planning time. No adaptivity to observed sample outcomes is assumed.

For \(0\le x\le A\), \(0\le y\le B\), write \(F(x,y)\) for expected union richness. Set \(\binom{t}{j}=0\) when \(j>t\), and let \(\mathcal O_m=\arg\max_{\max(0,m-B)\le x\le\min(m,A)} F(x,m-x)\). A nested sequence is a choice \(x_m\in\mathcal O_m\) at all \(0\le m\le N\) with \(x_0=0\) and \(x_{m+1}-x_m\in\{0,1\}\). Two adjacent budgets are *incompatible* if no \(x\in\mathcal O_m\), \(z\in\mathcal O_{m+1}\) satisfy \(z\in\{x,x+1\}\). A lack of a globally nested sequence is a weaker condition than an incompatible adjacent pair.

## Proof

### Exact expectation

For each species \(s\), absence from the A-sample occurs with probability \(\binom{A-a_s}{x}/\binom Ax\), and analogously in B. Independence of the two habitat samples and linearity of expectation give the exact formula

\[
F(x,y)=\sum_s\left[1-
\frac{\binom{A-a_s}{x}}{\binom Ax}
\frac{\binom{B-b_s}{y}}{\binom By}\right].\tag{1}
\]

This formula is the familiar hypergeometric rarefaction principle; only its two-habitat allocation consequences below are at issue here.

### Disjoint-species control case

If \(a_sb_s=0\) for every species, (1) decomposes as \(F(x,y)=f(x)+g(y)\), the sum of the two single-habitat expected-richness curves. For a species of abundance \(a>0\) in a habitat of size \(A\), the contribution to the marginal gain \(f(x+1)-f(x)\) is

\[
\frac aA\frac{\binom{A-a}{x}}{\binom{A-1}{x}},
\]

with the natural zero convention at the boundary. The ratio of successive nonzero terms equals \((A-a-x)/(A-1-x)\le1\), so the marginal gains decrease with sample size. The same holds for \(g\). Selecting the next largest available marginal gain from either habitat greedily produces an optimal allocation for **every** budget and gives a nested sequence. This establishes the stated positive control without requiring a search.

### Exact sharp boundary through six individuals

The lower bound and initial classification are finite and exhaustive. For each total \(N\le6\), enumerate all multisets of nonzero integer pairs \((a_s,b_s)\) with \(\sum_s(a_s+b_s)=N\); require both habitat totals positive and identify multisets under species permutation and exchange of the two habitats. These are all possible censuses: each species is uniquely described by its two counts. For each resulting profile, evaluate (1) at *every* feasible pair of sample sizes, exactly as a rational number; compute all maximizing \(\mathcal O_m\); and use the reachability recurrence

\[
R_0=\{0\},\qquad
R_{m+1}=\{z\in\mathcal O_{m+1}:z\in R_m\ \text{or}\ z-1\in R_m\}.
\]

A nested optimal sequence exists exactly when \(R_N\ne\varnothing\). The full exact enumeration, reproduced by the included standalone program, gives the following complete census:

| Total individuals | Habitat-exchange equivalence classes | Classes lacking a globally nested optimum | Classes with an incompatible adjacent pair |
|---:|---:|---:|---:|
| 2 | 2 | 0 | 0 |
| 3 | 4 | 0 | 0 |
| 4 | 14 | 0 | 0 |
| 5 | 28 | 0 | 0 |
| 6 | 69 | 3 | 1 |

The three first nonnesting classes, expressed as multisets of species' ordered A/B abundances (with habitat exchange permitted), are

\[
\begin{gathered}
\{(0,1),(0,3),(1,1)\},\\
\{(0,1),(1,1),(1,2)\},\\
\{(0,2),(1,1),(1,1)\}.
\end{gathered}
\]

Only the middle class has an incompatible adjacent pair, at budgets two and three. Written with A counts \((1,1,0)\) and B counts \((2,1,1)\), the exact objective comparisons are

\[
\begin{array}{c|ccc}
\text{budget }2 &(x,y)=(0,2)&(1,1)&(2,0)\\\hline
F(x,y)&11/6&13/8&2
\end{array}
\]

and

\[
\begin{array}{c|ccc}
\text{budget }3 &(x,y)=(0,3)&(1,2)&(2,1)\\\hline
F(x,y)&5/2&13/6&9/4.
\end{array}
\]

All inequalities are strict. The enumeration proof is exhaustive because all species-count multisets with the specified total are generated, all allocations at all budgets are evaluated, and the recurrence checks *entire budget chains*, not just adjacent pairs. The 117 classes of totals two through six were checked by two independent implementations of each expected value: (1), and direct averaging over all pairs of labeled subsets. The latter method yielded agreement at 1,462 distinct feasible allocation values. The program contains the enumeration itself, rather than relying on an undocumented table.

### Arbitrarily large forced reallocations

Fix \(r\ge2\) and \(K\ge r+2\). Habitat A has one individual each of species \(s_1,\ldots,s_r\). Habitat B has two of \(s_1\), one each of \(s_2,\ldots,s_r\), and \(K-r-1\) individuals of additional species, each appearing once and absent from A. Thus A has \(r\) individuals and B has \(K\).

At budget \(m=r\), allocating all \(r\) draws to A observes exactly \(r\) species. Every allocation using at least one B draw has a positive probability of a repeated species: a B draw can coincide with a sampled species of A if any A draws are taken, while an all-B draw of size \(r\ge2\) can contain the duplicate \(s_1\). Hence \(x=r\) is the unique maximizer.

For budget \(m=r+1\), put \(y=r+1-x\), so \(0\le x\le r\). In B, the only intra-habitat species repetition is the pair of \(s_1\) individuals, which are both sampled with probability \(y(y-1)/[K(K-1)]\). Conditional on a uniformly chosen A sample of \(x\) distinct species, the expected number of their species detected in B is \(x/r\) times the expected number of B-detected species belonging to the \(r\) shared species. The latter is \((r+1)y/K-y(y-1)/[K(K-1)]\). Therefore the exact distinct-species *deficit* from the ideal \(r+1\) discoveries is

\[
D(x,y):=r+1-F(x,y)
=\left(1-\frac xr\right)\frac{y(y-1)}{K(K-1)}
+\frac{x(r+1)y}{rK}.\tag{2}
\]

At \(x=0\) this equals \(r(r+1)/[K(K-1)]\). For every \(1\le x\le r\), the first term in (2) is nonnegative, while \(xy=x(r+1-x)\ge r\). Hence

\[
D(x,r+1-x)\ge\frac{r+1}{K}
>\frac{r(r+1)}{K(K-1)}=D(0,r+1),
\]

where the strict inequality uses \(K\ge r+2\). Thus \(x=0\) is the unique maximizing allocation at budget \(r+1\). Since \(r\) is arbitrary, the forced reallocation jump between consecutive optimal budgets is unbounded. This simultaneously gives the smallest six-individual witness at \(r=2,K=4\).

## Verification

Run `python verify_non_nested_rarefaction.py` with a standard Python 3 interpreter; the program uses only the standard library. It enumerates all 117 census classes with total size at most six, performs the full dynamic-programming nesting test, and recomputes all 1,462 allocation values by **direct enumeration of labeled sample subsets**, independently of formula (1). It also verifies the explicit infinite-family formulas and unique maxima for 117 finite parameter pairs with \(2\le r\le14\) and \(r+2\le K\le r+10\). Successful execution prints `All exact verification checks passed.` The unrestricted family and disjoint-species propositions are established by the preceding arguments, not by those finite checks.

## Relationship to prior work

Classical hypergeometric rarefaction supplies expectation (1) and is not claimed as new: Heck, van Belle and Simberloff (1975) provide a foundational single-community calculation. Chao and Jost (2012) study size- and coverage-standardized richness curves and their interpretation. MacKenzie and Royle (2005) address optimal repeat surveys for **occupancy-estimator precision**, rather than maximizing union richness with a prescribed split of finite individual samples. Carvalho and collaborators (first published in 2015) optimize **monitoring-site selection** to achieve species/stratum coverage targets. Moore and McCarthy (2016) optimize **single-species detection** across sites under variable effort and travel costs. These are relevant but distinct objectives and sampling spaces; the accessible full texts do not provide the exact six-individual budget-chain classification or equation (2)'s arbitrary reallocation family.

General combinatorial maximum-coverage problems can have nonnested optimal solutions; this observation alone neither supplies the sharp census boundary in the specified hypergeometric two-habitat model nor the explicit unbounded family with unique optimizers. No general novelty claim about maximum coverage or rarefaction itself is made.

## Limitations

The mathematical model presumes known integer abundance profiles, error-free and equal-cost individual detection, and uniform-without-replacement sampling within each independent habitat. It optimizes unconditional **expected union species richness** at each total budget, not estimation error, detection of a fixed target species, data-dependent adaptive surveying, or actual ecological population responses. The six-individual uniqueness concerns incompatible consecutive optimal allocations, not all globally nonnesting profiles (three exist at that census). The finite classification is exhaustive only through six individuals; no full higher-census classification is claimed. No assertion is made that the detected allocation pattern is absent from every possible formulation in older conservation, sampling, or discrete-optimization literature.

## References

1. Heck, K. L. Jr., van Belle, G., and Simberloff, D. (1975). Explicit calculation of the rarefaction diversity measurement and the determination of sufficient sample size. *Ecology* 56, 1459–1461. DOI: 10.2307/1934716. First published 1975-10-01.
2. MacKenzie, D. I., and Royle, J. A. (2005). Designing occupancy studies: general advice and allocating survey effort. *Journal of Applied Ecology*. DOI: 10.1111/j.1365-2664.2005.01098.x.
3. Chao, A., and Jost, L. (2012). Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size. *Ecology* 93, 2533–2547. DOI: 10.1890/11-1952.1.
4. Carvalho, S. B., Gonçalves, J., Guisan, A., and Honrado, J. P. (2015/2016). Systematic site selection for multispecies monitoring networks. *Journal of Applied Ecology* 53, 1305–1316. DOI: 10.1111/1365-2664.12505. First published 2015-08-30.
5. Moore, A. L., and McCarthy, M. A. (2016). Optimizing ecological survey effort over space and time. *Methods in Ecology and Evolution* 7, 891–899. DOI: 10.1111/2041-210X.12564. First published 2016-03-25.
