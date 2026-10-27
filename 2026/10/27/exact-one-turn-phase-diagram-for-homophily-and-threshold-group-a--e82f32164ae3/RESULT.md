# Exact one-turn phase diagram for homophily and threshold group adoption

## Finding

Fix integers \(n\ge2\) and \(1\le m\le n\), and an intrinsic active-type proportion \(0<p<1\). In the two-binomial homophily composition law defined below, let \(F_{n,m,p}(h)\) be the proportion of groups with at least \(m\) active types, for homophily \(0\le h\le1\). Set \(a=m-1\), \(b=n-m\), and \(p_c=a/(n-1)\). Its complete shape classification is:

* If \(a>b\), then \(F\) is strictly increasing on \((0,1)\) when \(p\le p_c\); for \(p>p_c\), it decreases to a **unique strict interior minimum** and then increases.
* If \(a<b\), then \(F\) is strictly decreasing on \((0,1)\) when \(p\ge p_c\); for \(p<p_c\), it increases to a **unique strict interior maximum** and then decreases.
* If \(a=b\), then \(F\) is strictly increasing when \(p<1/2\), strictly decreasing when \(p>1/2\), and identically \(1/2\) when \(p=1/2\).

The endpoints are \(F(0)=\Pr\{\operatorname{Bin}(n,p)\ge m\}\) and \(F(1)=p\). When an interior extremum exists, write \(t=h/(1-h)\); its position is the unique solution \(t>0\) of
\[
(1+t/p)^a=(1+t/(1-p))^b,\qquad h=t/(1+t).
\]
A nonmonotone response is impossible for group sizes at most three, but occurs already for size four. For the three-of-four adoption rule and \(p=4/5\), the unique minimizing homophily is \(h=8/13\), and
\[
F(0)=\frac{512}{625},\qquad F(8/13)=\frac{8704}{10985},\qquad F(1)=\frac45.
\]
The strict interior extremum survives as a local extremum for all sufficiently steep **finite** versions of the smooth conformity response used in the motivating model, provided the response threshold does not coincide with a grid fraction \(k/n\).

## Assumptions and scope

The group-type composition model is the two-binomial mixture of Ribordy et al. (2026), equation (1). Put \(q=1-p\). A group's count \(K\in\{0,\ldots,n\}\) of intrinsically active members is drawn according to
\[
\Pr(K=k)=p\binom nk(p+qh)^k[q(1-h)]^{n-k}
+q\binom nk[p(1-h)]^k(q+ph)^{n-k}.
\]
Equivalently, conditionally on a latent group label taking values \(+\) and \(-\) with probabilities \(p\) and \(q\), \(K\) is binomial with success parameters \(p_+(h)=p+qh\) and \(p_-(h)=p(1-h)\), respectively. Homophily \(h\) varies over \([0,1]\). The **hard-threshold** behavioral rule adopts protection if and only if \(K\ge m\), hence
\[
F_{n,m,p}(h)=p\,T_{n,m}(p_+(h))+q\,T_{n,m}(p_-(h)),\quad
T_{n,m}(z)=\sum_{k=m}^n\binom nk z^k(1-z)^{n-k}.
\]
These are probabilities for group-level behavior, not infection prevalence, an epidemic threshold, or a finite-population realization of an interaction network. The two-binomial mixture and hard-threshold group behavior are model assumptions. No population-level dynamical conclusion is asserted.

For comparison with the motivating paper's finite-steepness response, take \(\tau\in((m-1)/n,m/n)\), set \(r=-\log 2/\log\tau\), and define
\[
R_\sigma(u)=\frac{u^{r\sigma}}{(1-u^r)^\sigma+u^{r\sigma}},\quad 0\le u\le1,\quad \sigma>0,
\]
with the continuous endpoint convention. The corresponding group-adoption probability is \(F_\sigma(h)=\sum_{k=0}^n\Pr(K=k)R_\sigma(k/n)\). The theorem's **global monotonicity classification** concerns the limiting hard-threshold rule, not all finite \(\sigma\).

## Proof

**1. Exact derivative.** The binomial-tail identity
\[
T_{n,m}'(z)=n\binom{n-1}{m-1}z^{m-1}(1-z)^{n-m}
\]
follows by termwise differentiation and telescoping. Therefore, with \(a=m-1\), \(b=n-m\),
\[
F'(h)=npq\binom{n-1}{m-1}
\{p_+(h)^a[1-p_+(h)]^b-p_-(h)^a[1-p_-(h)]^b\}.
\]
For every \(0<h<1\), both Bernoulli parameters lie strictly between zero and one, so the sign is precisely the sign of the logarithm of the ratio of the two braced factors.

**2. The one-turn lemma.** Substitute \(t=h/(1-h)>0\). Direct algebra gives
\[
p_+=\frac{p+t}{1+t},\quad p_-=\frac p{1+t},\quad
1-p_+=\frac q{1+t},\quad 1-p_-=\frac{q+t}{1+t}.
\]
Consequently, the sign of \(F'(h)\) is the sign of
\[
L(t)=a\log(1+t/p)-b\log(1+t/q).
\]
It satisfies \(L(0)=0\) and
\[
L'(t)=\frac{a}{p+t}-\frac b{q+t}
=\frac{a-(n-1)p+(a-b)t}{(p+t)(q+t)}.
\]
The numerator is affine in \(t\). If \(a>b\), then \(L(t)\to+\infty\) as \(t\to\infty\). If \(p\le p_c\), its derivative is positive for all \(t>0\), giving \(L(t)>0\). If \(p>p_c\), \(L\) first decreases, then increases to \(+\infty\), crossing zero exactly once for \(t>0\); this is a unique change of \(F'\) from negative to positive. The \(a<b\) case reverses all signs: \(L(t)\to-\infty\), and when \(p<p_c\) there is exactly one change from positive to negative. When \(a=b\), the sign of \(L(t)=a\log[(1+t/p)/(1+t/q)]\) equals the sign of \(q-p\), except that it is identically zero at \(p=q\). All stated cases and uniqueness follow.

**3. Minimal group size and exact example.** For \(n\le3\), every interior threshold has either \(a=0\), \(b=0\), or \(a=b\), so no interior strict extremum is possible. For \(n=4,m=3\), elementary polynomial differentiation yields
\[
F'(h)=12p(1-p)h(1-h)
\left[(3p^2-3p+1)h+p(2-3p)\right].
\]
Thus, for \(p>2/3\), the unique minimum is at
\[
h_* =\frac{p(3p-2)}{3p^2-3p+1}.
\]
At \(p=4/5\), this is \(8/13\); direct substitution into the original binomial mixture gives the three exact values stated in the finding. In particular \(F(8/13)<F(1)<F(0)\).

**4. Finite-steepness persistence.** For \(\tau\notin\{0,1/n,\ldots,1\}\), the finitely many response values \(R_\sigma(k/n)\) converge as \(\sigma\to\infty\) to the indicators of \(k\ge m\). Hence the polynomials \(F_\sigma\) and their first two derivatives converge uniformly on \([0,1]\) to \(F\) and its first two derivatives. At the hard-threshold interior extremum, the crossing of \(L\) occurs where \(L'\ne0\), so \(F''(h_*)\ne0\). Thus for all sufficiently large finite \(\sigma\) there exists a nondegenerate local extremum of the same type close to \(h_*\). This establishes persistence, not the global finite-steepness phase diagram.

## Verification

Run `python3 verify.py` with Python 3 and its standard library; no data files or external packages are required. The program constructs the group-adoption polynomial directly from its mixture definition, differentiates that polynomial independently of the analytic binomial-tail formula, and compares the resulting values with the analytic derivative over rational test points. It also checks the derivative-sign identity, all asserted sample classifications, the four-person exact optimum, and nonexistence of interior reversals for sizes two and three. The supplied execution passed 23,097 exact-rational equality/shape checks. The exhaustive quantifiers in the theorem are justified by the preceding proof, not by the finite program.

## Relationship to prior work

Ribordy, Granell, St-Onge, Hébert-Dufresne, Arenas and Allard (2026) introduce precisely this mixture in equation (1), describe a sigmoid group-conformity response in equation (2), and express active group fractions as mixture averages in equation (9). Their Appendix B obtains asymptotic large-group bounds in the hard-threshold limit, while section III.1 analyzes the **epidemic threshold** and conditional passive-type participation under homophily. These do not give the all-finite-group-size critical proportion \((m-1)/(n-1)\), the exact one-turn classification of **unconditional group adoption**, or the minimal four-member reversal and its exact optimizer. Those are distinct statements; neither general epidemic-threshold nonmonotonicity nor large-group limits imply this finite-\(n\) phase diagram.

Burgio, Gómez and Arenas (2023) study a related context-dependent spreading model with a different multi-parameter hypergraph assortativity construction; their reproduction-number and group-context results do not establish this two-binomial one-parameter derivative classification. Veldt, Benson and Kleinberg (2021) study hypergraph homophily affinity scores and combinatorial impossibility theorems for two classes, not the present group-response probability as a function of a latent mixture parameter.

## Limitations

The threshold is **group behavioral adoption**, not epidemiological invasion, epidemic size, or optimal public-health policy. Groups use a specified two-binomial composition mixture, independent conditional draws, and a uniform integer-count response threshold. The hard-threshold phase diagram need not hold globally for the smooth finite-steepness model, for other mixture families, or for dynamically changing group composition. Although the closest identified literature does not state an implication-equivalent result, a broader binomial-mixture variation theorem could subsume it; historical priority has not been independently established.

## References

1. O. Ribordy, C. Granell, G. St-Onge, L. Hébert-Dufresne, A. Arenas, and A. Allard, *The impact of behavioral homophily and conformity on epidemic spreading in networks with large groups*, arXiv:2605.25875, first submitted 25 May 2026, particularly equations (1), (2), (9), section III, and Appendix B. https://arxiv.org/html/2605.25875v1
2. G. Burgio, S. Gómez, and A. Arenas, *Spreading dynamics in networks under context-dependent behavior*, arXiv:2211.00435 (2022), Phys. Rev. E 107, 064304 (2023). https://arxiv.org/abs/2211.00435
3. N. Veldt, A. R. Benson, and J. Kleinberg, *Combinatorial Characterizations and Impossibilities for Higher-order Homophily*, arXiv:2103.11818 (2021). https://arxiv.org/abs/2103.11818
