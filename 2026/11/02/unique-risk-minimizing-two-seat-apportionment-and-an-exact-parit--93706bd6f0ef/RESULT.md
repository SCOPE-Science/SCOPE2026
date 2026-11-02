# Unique risk-minimizing two-seat apportionment and an exact parity law

## Finding

For every integer \(n\ge3\) and every nonnegative integer \(L\), let \(n\) parties have equal positive populations and let the legislature have exactly \(H=nL+2\) seats. Each standard quota is \(L+2/n\). Fix the tie order \(1<2<\cdots<n\), and let \(S\) be the two-element subset of parties receiving their upper quotas. Among **all** quota-respecting, ex-ante proportional lotteries (each party appears in \(S\) with probability \(2/n\)), there is a **unique** distribution minimizing the variance of the total index-ordered envy count

\[
\sigma(S)=\#\{(i,j):1\le j<i\le n,\ i\notin S,\ j\in S\}.
\]

The sharp minimum is

\[
\min\operatorname{Var}[\sigma(S)] =
\begin{cases}
0,& n\text{ even},\\[2pt]
2/n,& n\text{ odd}.
\end{cases}
\]

If \(n=2h\) is even, the unique optimizer assigns probability \(2/n\) to each mirror pair \(\{i,n+1-i\}\), \(1\le i\le h\), and zero to all other pairs. Consequently \(\sigma(S)=n-2\) surely.

If \(n=2h+1\) is odd, the optimizer assigns probability \(2/n\) to each mirror pair \(\{i,n+1-i\}\) with \(1\le i<h\), and probability \(1/n\) to each of the three pairs \(\{h,h+1\}\), \(\{h,h+2\}\), and \(\{h+1,h+2\}\). The exact envy distribution has masses \(1/n,1-2/n,1/n\) at \(n-3,n-2,n-1\), respectively.

There is also a sharp **anonymity cost** under this fixed tie convention. If the lottery is invariant under all permutations of the equally entitled parties, it must be the uniform lottery on the \(\binom n2\) pairs, which has

\[
\operatorname{Var}_{\rm anonymous}[\sigma(S)]
=\frac{(n+1)(n-2)}6.
\]

In particular the anonymous and unrestricted minima agree only for \(n=3\). For every even \(n\ge4\), the unrestricted variance vanishes while the anonymous variance is positive; for odd \(n\ge5\), the ratio of the two variances is \(n(n+1)(n-2)/12\).

## Assumptions and scope

The population and house size are fixed, with equal positive party populations, \(n\ge3\), \(L\in\mathbb{Z}_{\ge0}\) and \(H=nL+2\). Every party receives exactly \(L\) or \(L+1\) seats, exactly two parties receive \(L+1\), and each party's expected seat count is \(L+2/n\). No assumption of independence between the two selected parties is made. These marginal probabilities and fixed subset cardinality are the full feasibility constraints.

For equal quotas the underlying mathematical envy definition adopts a **fixed arbitrary label order** to resolve ties; it counts an inversion when a selected lower-index party is paired with an unselected higher-index party. This is precisely the tie convention of La Commare, Tucker-Foltz, and Verdugo [1], not an assertion that a tied party with a larger label genuinely deserves more seats. Optimality and uniqueness hold for **this fixed convention**. The variance is over the randomness of the allocation \(S\), not voter sampling or a changing population.

## Proof

**Step 1 (inversion count and fixed mean).** For a selected pair \(S=\{a,b\}\) with \(a<b\), the selected index \(a\) lies below \(n-a-1\) unselected indices and \(b\) lies below \(n-b\) unselected indices. Hence

\[
\sigma(\{a,b\})=2n-a-b-1.
\]

Ex-ante proportionality gives \(\mathbb E[\sum_{j\in S}j]=(2/n)\sum_{j=1}^n j=n+1\), so \(\mathbb E\sigma(S)=n-2\). Therefore

\[
\operatorname{Var}(\sigma(S))=\sum_{a<b}p_{ab}\bigl(a+b-(n+1)\bigr)^2,
\]

where \(p_{ab}\ge0\), \(\sum_{b\ne a}p_{\min(a,b),\max(a,b)}=2/n\), and \(p_{ab}\) are the pair probabilities. Summing the marginal equations ensures that their total mass is \(1\).

**Step 2 (even populations).** When \(n=2h\), every mirror pair has sum \(n+1\). The stated \(h\)-pair distribution meets each marginal \(2/n\) exactly and makes every square above zero. Since squares are nonnegative, variance \(0\) is optimal. Any other zero-variance lottery can place mass only on pairs with sum \(n+1\). Each index has exactly one distinct such partner, so each pair probability is fixed at \(2/n\); uniqueness follows.

**Step 3 (odd populations: lower bound).** Let \(n=2h+1\) and let \(c=h+1\) be the central index. Any selected pair containing \(c\) has a distinct other member, and therefore \(\lvert a+b-(n+1)\rvert\ge1\). Thus, for every possible pair,

\[
\bigl(a+b-(n+1)\bigr)^2\ge \mathbf1\{c\in\{a,b\}\}.
\]

Taking expectation and using the fixed inclusion marginal of \(c\) gives \(\operatorname{Var}(\sigma(S))\ge\Pr(c\in S)=2/n\). This is also an exact feasible linear-programming dual certificate: a dual weight \(1\) at \(c\) and \(0\) elsewhere.

**Step 4 (odd populations: attainment and uniqueness).** The stated outer mirror pairs and central triangle have total mass \((h-1)2/n+3/n=1\). Each noncentral outer index is selected with probability \(2/n\). Each of the three central indices lies in exactly two triangle edges, each of mass \(1/n\), so all marginals are correct. Every outer mirror pair and the central cross-pair \(\{h,h+2\}\) has squared deviation \(0\); the two edges incident to \(c\) have squared deviation \(1\). Their combined probability is \(2/n\), meeting the bound.

Equality in the pointwise bound from Step 3 forces every positive-probability pair **not** containing \(c\) to have sum \(n+1\), and every positive-probability pair containing \(c\) to have its other member equal to \(h\) or \(h+2\). Thus every optimizer is supported only on the outer mirror pairs and the three central edges. The marginal of every outer index fixes its mirror-pair mass to \(2/n\). Writing the triangle masses as \(\alpha,\beta,\gamma\), the marginal equations at its three vertices require \(\alpha+\beta=\alpha+\gamma=\beta+\gamma=2/n\), so all three equal \(1/n\). This proves uniqueness and the stated three-point envy distribution, including the boundary \(n=3\).

**Step 5 (anonymous benchmark).** Under invariance to every permutation of labels, all two-element subsets have the same probability \(1/\binom n2\); this is feasible. For an unordered uniform pair \(\{A,B\}\), let \(\operatorname{Var}_{\rm pop}=(n^2-1)/12\) be the variance of one draw from the labels \(1,\dots,n\). Sampling two without replacement gives \(\operatorname{Cov}(A,B)=-\operatorname{Var}_{\rm pop}/(n-1)\), whence

\[
\operatorname{Var}(A+B)=2\operatorname{Var}_{\rm pop}\left(1-\frac1{n-1}\right)=\frac{(n+1)(n-2)}6.
\]

Since \(\sigma=2n-A-B-1\), its variance is the same. Direct comparison establishes the exact anonymity gap and the stated odd-population ratio. All steps hold for every admissible population size, not just the checked examples.

## Verification

The self-contained `verify.py` program uses Python's exact rational arithmetic to independently check the lottery weights, each marginal, the inversion-count identity, the complete three-point risk distribution, the sharp lower-bound certificate on every possible pair, and the anonymous benchmark for each \(3\le n\le100\). The command `python verify.py` passes these checks. The optional command `python verify.py --lp` additionally solves the original finite pair-probability linear program independently using SciPy/HiGHS for every \(3\le n\le18\); all computed optima match the exact formulas within the stated numerical tolerance. The proof above, not the finite checks or the numerical solver, establishes global optimality and uniqueness for all \(n\).

For orientation, at \(n=5\) the unique law puts mass \(2/5\) on \(\{1,5\}\) and \(1/5\) on each of \(\{2,3\},\{2,4\},\{3,4\}\); the minimum variance is \(2/5\), against anonymous variance \(3\).

## Relationship to prior work

La Commare, Tucker-Foltz, and Verdugo [1, Sections 2.2–2.3, 3.1, and 4.3, including Proposition 4.4] define the index-ordered envy statistic, prove that its expected total is invariant under ex-ante proportional lotteries for a common lower quota, and provide a general polynomial-time linear program to **compute** a variance-minimizing lottery. The present exact all-population parity formula, unique optimizer, full minimal-risk distribution and explicit anonymity benchmark resolve a parametric two-residual-seat case of that general algorithm; they do not claim to improve its general-purpose computational guarantee. A generic LP capable of returning an instance-specific answer does not itself state this uniform symbolic classification.

Balanced sampling [2] provides the broader conceptual framework of controlling a fixed-sample total under prescribed inclusion probabilities; the even case here is perfectly balanced on the integer labels. Monotone randomized apportionment [3] studies correlated quota-respecting lotteries with different monotonicity objectives. The present proof additionally supplies the sharp unavoidable odd-population variance and unique support, not established by the inspected material. This comparison is necessarily qualified where only an accessible abstract or preview could be examined.

## Limitations

This result applies only to equal populations with **two** residual seats and to the fixed arbitrary tie order used in [1]. The optimal law is generally **not anonymous**. If ties were instead ignored or both equal-entitlement directions were counted as envious, the statistic would change and these conclusions would not automatically transfer. No strategyproofness, inter-house-size consistency, broader fairness optimum, or other quota configurations are asserted. The generic importance of exact balancing in statistics predates this result, and an unindexed equivalent special-case theorem remains a priority risk. The accompanying finite computations are cross-checks, not an independent formal proof or external validation.

## References

[1] Francesco La Commare, Jamie Tucker-Foltz, Victor Verdugo, *Envy-Free Randomized Apportionment*, arXiv:2610.24217v1, first released 2026-10-16. https://arxiv.org/html/2610.24217v1

[2] Yves Tillé, *Balanced Sampling*, International Encyclopedia of Statistical Science, DOI:10.1007/978-3-642-04898-2_130. https://doi.org/10.1007/978-3-642-04898-2_130

[3] José Correa, Paul Gölz, Ulrike Schmidt-Kraepelin, Jamie Tucker-Foltz, Victor Verdugo, *Monotone Randomized Apportionment*, arXiv:2405.03687, first released 2024-05-06. https://arxiv.org/abs/2405.03687
