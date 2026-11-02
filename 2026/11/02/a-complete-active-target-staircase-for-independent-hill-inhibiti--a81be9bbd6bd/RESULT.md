# A complete active-target staircase for independent Hill inhibition under a shared dose budget

## Finding

Fix an integer \(n\ge2\), a Hill exponent \(h>0\), a common dose scale \(K>0\), and a total available dose \(B>0\). Allocate doses \(x_i\ge0\) with \(\sum_{i=1}^{n}x_i=B\) to \(n\) independent inhibitory mechanisms. Assume that the survival fraction at mechanism \(i\) is \(s_i(x_i)=[1+(x_i/K)^h]^{-1}\), and that total surviving fraction is the product \(S(x)=\prod_{i=1}^{n}s_i(x_i)\). We minimize \(S\), equivalently maximize \(\sum_i\log[1+(x_i/K)^h]\).

For \(0<h\le1\), the **unique** optimum is equal dosing of all \(n\) mechanisms, \(x_i=B/n\).

For \(h>1\), **every** global optimum gives an equal positive dose to some \(k\) mechanisms and zero to the remaining \(n-k\). Every support size \(k\in\{1,\ldots,n\}\) becomes uniquely optimal (up to permutation) over a nonempty dose-budget interval, in the strict order \(1,2,\ldots,n\) as the budget increases. There are exactly \(n-1\) distinct transition budgets; no support size is skipped and no nonadjacent support sizes tie.

More precisely, let \(b=B/K\), define \(F_k(b)=k\log[1+(b/k)^h]\), and let \(u_h>0\) be the unique positive solution of
\[
\frac{h u_h^h}{1+u_h^h}=\log(1+u_h^h).
\]
For each \(1\le k<n\), there is exactly one \(\theta_k\in(k u_h,(k+1)u_h)\) satisfying \(F_k(\theta_k)=F_{k+1}(\theta_k)\), and
\[
0<\theta_1<\theta_2<\cdots<\theta_{n-1}.
\]
With the conventions \(\theta_0=0\) and \(\theta_n=+\infty\), for \(\theta_{k-1}<b<\theta_k\) the optima are precisely the permutations of \((B/k,\ldots,B/k,0,\ldots,0)\), with \(k\) positive entries. At \(b=\theta_k\), precisely the \(k\)- and \((k+1)\)-support equal-dose allocations tie. In particular,
\[
\boxed{\theta_1=2(2^h-2)^{1/h}}.
\]

## Assumptions and scope

The probabilities are deterministic idealized Hill response functions, with the *same* exponent and dose scale across all mechanisms, independent combination of survival events, nonnegative real doses, an exactly fixed aggregate dose, and no efficacy/toxicity or cross-mechanism constraints. Dose is normalized by \(K\), so all thresholds \(\theta_k\) are dimensionless and the corresponding physical thresholds are \(K\theta_k\). The theorem is global for every real \(h>0\), every integer \(n\ge2\), and every positive \(B,K\). It addresses the idealized optimal allocation, not uncertainty in fitted Hill parameters or clinical treatment decisions.

## Proof

**1. Reduction and the concave regime.** Put \(z_i=x_i/K\), so \(\sum_i z_i=b\), and \(f(z)=\log(1+z^h)\). Since
\[
f''(z)=\frac{h z^{h-2}[(h-1)-z^h]}{(1+z^h)^2},\qquad z>0,
\]
\(f\) is strictly concave on \((0,\infty)\) for \(0<h\le1\). Strict Jensen inequality (with continuity at zero) gives the unique all-equal optimum.

**2. Unequal positive doses cannot maximize when \(h>1\).** For \(h>1\),
\[
f'(z)=\frac{h z^{h-1}}{1+z^h}
\]
is positive and first increases and then decreases, changing direction at \(z=(h-1)^{1/h}\). At a putative maximum, any pair of strictly positive coordinates must have equal derivatives (transfer a small amount between them). Suppose the pair is \(x<y=rx\), with \(r>1\), and write \(v=f'(x)=f'(y)\). The derivative equality gives
\[
x^h=\frac{r^{h-1}-1}{r^{h-1}(r-1)},\qquad xv=\frac{h(r^{h-1}-1)}{r^h-1}.
\]
Since \(f''(z)=f'(z)[(h-1)/z-f'(z)]\), the second derivative along that pairwise transfer is
\[
f''(x)+f''(y)=v\left[(h-1)\left(\frac1x+\frac1y\right)-2v\right].
\]
This is **strictly positive**: with \(r=e^{2t}\), \(t>0\), clearing positive factors reduces the required inequality to
\[
(h-1)\sinh((h+1)t)>(h+1)\sinh((h-1)t),
\]
which follows from the strict increase of \(\sinh w/w\) on \(w>0\). Thus any unequal stationary pair gives a strict local *minimum* along a feasible perturbation, contradicting global maximality. Hence all positive coordinates of any maximizer are equal.

**3. A single peak controls every support comparison.** If exactly \(k\) coordinates are positive, they each equal \(b/k\) in normalized units and give objective \(F_k(b)\). Write
\[
g(t)=\frac{\log(1+t^h)}{t},\qquad F_k(b)=b\,g(b/k).
\]
The numerator of \(t^2g'(t)\) is \(\psi(t^h)\), where
\[
\psi(y)=\frac{hy}{1+y}-\log(1+y),\qquad
\psi'(y)=\frac{h-1-y}{(1+y)^2}.
\]
For \(h>1\), \(\psi\) rises from zero to a positive maximum and then decreases to \(-\infty\), so it has a unique positive zero. Therefore \(g\) is strictly increasing up to a unique peak \(u_h\) and strictly decreasing afterward.

Fix adjacent support sizes \(k\) and \(k+1\). At \(b=k u_h\), \(F_k(b)>F_{k+1}(b)\); at \(b=(k+1)u_h\), the inequality reverses. Inside this bracket, \(g(b/k)\) strictly decreases as \(b\) grows while \(g(b/(k+1))\) strictly increases. Exactly one crossing \(\theta_k\) exists. The intervals \((k u_h,(k+1)u_h)\) for consecutive \(k\) are disjoint, hence \(\theta_k<\theta_{k+1}\). Below \(\theta_k\), \(F_k>F_{k+1}\); above it, \(F_{k+1}>F_k\). Chaining adjacent inequalities proves the claimed unique optimal support size, ties, and absence of skipped sizes. For \(k=1\), the equality \(1+b^h=[1+(b/2)^h]^2\) yields the explicit \(\theta_1\).

## Verification

The attached standard-library program `check.py` tests the analytical conclusions without being substituted for the proof. It compares the predicted global optimum against 52,569 exact rational grid allocations for integer exponents \(h=2,3,4\), checks 21,600 random real-exponent allocations, and brackets 56 adjacent-support transitions for eight real exponents. It also independently verifies the explicit first switching threshold numerically. Its finite tests are not a proof of the universal theorem. The derivations above establish the arbitrary-dimensional and real-parameter assertions.

For example, at \(n=3\), \(h=2\), \(K=1\), \(B=4\), exactly two mechanisms receive dose \(2\), because the survival values for one, two, and three active mechanisms are respectively \(1/17\), \(1/25\), and \(729/15625\). Thus an intermediate support is genuinely globally optimal.

## Relationship to prior work

Bliss-independent combination of inhibitory responses and Hill-type monotherapy curves are established models; this finding does not claim those models as new. Zhao et al. (2014) give a Bliss response-surface methodology, Tang, Wennerberg, and Aittokallio (2015) contrast Bliss and Loewe reference models, and Di Veroli et al. (2015) explicitly use multiple independent Hill-type response processes for dose-response fitting. None of their inspected accounts contains the **fixed-total-dose global equal-support and sharp all-support staircase** asserted here.

Separable nonconcave resource allocation is an established mathematical subject. Vicentini (1970) addresses S-shaped resource allocation. Ginsberg (1974) gives a complete solution for identical plants with general convex-concave production functions, according to its accessible abstract; that may already cover part of the equal-positive allocation reduction. Zipkin (1980) gives broad ranking algorithms for nonlinear separable allocation. The accessible accounts do not state the strict **Hill-specific no-skipping staircase**, the unique adjacent thresholds with explicit brackets, or the analytic first threshold proved here; nor does a general candidate-enumeration principle by itself imply these restrictions. However, the 1970, 1974 and 1980 full texts could not be examined, so stronger prior coverage remains a material historical-priority risk, not a uniqueness certification. The later open-access discussion by Westerink-Duijzer et al. (2020) confirms the general S-shaped allocation setting and references the Ginsberg work; it does not claim the present specialized thresholds.

## Limitations

This is a structural theorem for a deliberately idealized independent-effects benchmark. It does not cover unequal potencies, distinct Hill exponents, toxicity ceilings, target interactions, correlated survival events, uncertainty, discrete administered dose units, or pharmacokinetic coupling. Bliss independence is a model assumption rather than a claim that real medical combinations obey independence. No empirical efficacy or safety conclusion follows. Priority remains provisional because earlier general nonconcave resource-allocation texts, especially the identical-plant Ginsberg (1974) paper, were inaccessible in full; independent review is not performed.

## References

1. F. M. Vicentini, *On the Resource Allocation Problem with S-Shaped Utility Functions*, Technical Memorandum 201, Case Western Reserve University (1970-08-01), https://commons.case.edu/wsom-ops-reports/370/ . Bibliographic record and abstract accessible; complete PDF inaccessible.
2. P. H. Zipkin, *Simple Ranking Methods for Allocation of One Resource*, Management Science 26 (1980), 34–43, https://doi.org/10.1287/mnsc.26.1.34 . Abstract accessible; complete PDF inaccessible.
3. W. Zhao et al., *A New Bliss Independence Model to Analyze Drug Combination Data*, Journal of Biomolecular Screening 19 (2014), 817–821; first online 2014-02-03, https://doi.org/10.1177/1087057114521867 . Full accessible article inspected.
4. J. Tang, K. Wennerberg, T. Aittokallio, *What is synergy? The Saariselkä agreement revisited*, Frontiers in Pharmacology 6 (2015), 181; published 2015-09-01, https://doi.org/10.3389/fphar.2015.00181 . Full accessible review inspected.
5. G. Y. Di Veroli et al., *An automated fitting procedure and software for dose-response curves with multiphasic features*, Scientific Reports 5 (2015), 14701; published 2015-10-01, https://doi.org/10.1038/srep14701 . Full accessible article inspected.
6. W. Ginsberg, *The multiplant firm with increasing returns to scale*, Journal of Economic Theory 9 (1974), 283–292, https://www.econbiz.de/10002439510 . Abstract accessible, describing a complete solution for identical plants; full text not inspected.
7. L. E. Westerink-Duijzer, L. P. J. Schlicher, and M. Musegaas, *Core Allocations for Cooperation Problems in Vaccination*, Production and Operations Management 29 (2020), 1720–1737, https://doi.org/10.1111/poms.13184 . Full accessible article consulted for historical comparison; it concerns cooperative games with S-shaped returns, not the asserted Hill threshold staircase.
