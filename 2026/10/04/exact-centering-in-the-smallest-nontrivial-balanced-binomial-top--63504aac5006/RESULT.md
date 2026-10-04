# Exact centering in the smallest nontrivial balanced binomial top-selection case
## Finding
For the balanced slippage-family top-two selection problem with four independent Bernoulli populations, two with success probability \(p\) and two with success probability \(p+\delta\), where each population is sampled exactly twice, \(0<\delta<1\), and \(0\le p\le1-\delta\), selecting the two largest success counts with uniform tie-breaking has probability of correct selection \(P_\delta(p)\) uniquely minimized at \(p=(1-\delta)/2\). More precisely, with \(h=p-(1-\delta)/2\), \(P_\delta(p)-P_\delta((1-\delta)/2)=\delta h^2 G_\delta(h^2)/24\), where \(G_\delta(u)=29+64\delta+38\delta^2-3\delta^4-(84-12\delta^2)u-16u^2>0\) throughout \(0\le u\le(1-\delta)^2/4\).

This is the first balanced case beyond the two-population problem: \(k=4\), \(t=2\), and the smallest even sample size \(n=2\). It proves one concrete finite-sample case of the all-even-sample centering conjecture posed for balanced binomial top-selection.

## Assumptions and scope
There are four independent populations. Populations 1 and 2 have Bernoulli success probability \(p\); populations 3 and 4 have success probability \(q=p+\delta\), with \(0<\delta<1\) and \(0\le p\le1-\delta\). Each population is sampled exactly twice. The procedure selects the two populations having the largest success counts and resolves every tie uniformly among tied populations.

The probability of correct selection \(P_\delta(p)\) means the probability that both populations with parameter \(q\) are selected. The theorem is only for \(k=4,t=2,n=2\); it does not assert the full even-sample conjecture or any odd-sample statement.

## Proof
Uniform tie-breaking can be represented exactly by adding independent \(U(0,1)\) jitters to the integer success counts. If \(X\sim\operatorname{Bin}(2,p)\) and \(Y\sim\operatorname{Bin}(2,q)\), correct selection is then the event that the larger of the two jittered low-population scores is below the smaller of the two jittered high-population scores.

For \(r\in\{0,1,2\}\), put \(a_r(x)=\Pr(\operatorname{Bin}(2,x)=r)\) and \(A_r(x)=\Pr(\operatorname{Bin}(2,x)<r)\). Explicitly,
\[
a_0(x)=(1-x)^2,\qquad a_1(x)=2x(1-x),\qquad a_2(x)=x^2,
\]
and
\[
A_0(x)=0,\qquad A_1(x)=(1-x)^2,\qquad A_2(x)=1-x^2.
\]
On the jitter interval \(r+u\), \(0\le u\le1\), the low-score distribution function is \(A_r(p)+a_r(p)u\), while the high-score survival probability is \(1-A_r(q)-a_r(q)u\). Therefore
\[
P_\delta(p)=2\sum_{r=0}^2 a_r(q)\int_0^1
\bigl(A_r(p)+a_r(p)u\bigr)^2
\bigl(1-A_r(q)-a_r(q)u\bigr)\,du.
\]
This is an exact finite polynomial identity, not an asymptotic approximation.

Set \(h=p-(1-\delta)/2\). Direct expansion of the integral gives
\[
\begin{aligned}
96P_\delta(p)={}&\delta^7-17\delta^5-32\delta^4+7\delta^3+64\delta^2+57\delta+16\\
&+(-12\delta^5+152\delta^3+256\delta^2+116\delta)h^2\\
&+(48\delta^3-336\delta)h^4-64\delta h^6.
\end{aligned}
\]
Consequently
\[
P_\delta(p)-P_\delta((1-\delta)/2)
=\frac{\delta h^2}{24}G_\delta(h^2),
\]
where
\[
G_\delta(u)=29+64\delta+38\delta^2-3\delta^4-(84-12\delta^2)u-16u^2.
\]
Because \(0<\delta<1\), the derivative \(G_\delta'(u)=-(84-12\delta^2)-32u\) is strictly negative for \(u\ge0\). The allowed parameter interval gives \(0\le h^2\le(1-\delta)^2/4\). Hence
\[
G_\delta(h^2)\ge G_\delta((1-\delta)^2/4)
=7+110\delta+14\delta^2-2\delta^3-\delta^4>0.
\]
For the last inequality, \(2\delta^3+\delta^4<3\delta\) on \(0<\delta<1\), so the displayed quantity exceeds \(7+107\delta+14\delta^2\). Thus the difference from the centered value is zero exactly when \(h=0\), proving unique minimization at \(p=(1-\delta)/2\).

## Verification
A standalone symbolic checker independently constructs \(P_\delta(p)\) in two ways: by enumerating all \(3^4\) success-count vectors with exact uniform tie probabilities, and by evaluating the jitter integral above. It verifies equality of the two expressions, the centered factorization, the endpoint formula for \(G_\delta\), and several exact rational spot checks. Its successful terminal message is `VERIFY_OK`.

The proof itself is analytic and finite; the checker is a reproducibility aid rather than evidence for any unproved infinite assertion.

## Relationship to prior work
Wu and Chen study the same slippage-family location problem and prove that, for fixed \(k,t,\delta\), exact eventual centering occurs precisely in the balanced case \(k=2t\). They also prove exact centering for the two-population problem and explicitly conjecture that every balanced problem has the symmetric center as its unique least-favorable location for every even \(n\ge2\). The result here proves the smallest unresolved balanced instance, \(k=4,t=2,n=2\), by an exact finite calculation.

Tovey proves a broad least-favorable slippage theorem for two alternatives; that result does not imply a four-population select-two location theorem. Wang studies exact binomial ranking-and-selection procedures and least-favorable configurations in a control-comparison framework; the accessible description does not state the four-population centered-location identity proved here.

## Limitations
This result is deliberately narrow. It does not prove the balanced conjecture for \(n\ge4\), for larger \(t\), or for odd sample sizes. Its conclusion depends on uniform tie-breaking. The motivating paper's full text was not available through the inspected direct rendering route, so the originality comparison uses its public abstract together with an indexed quotation of its explicit conclusion conjecture; this leaves a residual risk that an unindexed source contains the same special case. The 2023 dissertation was identified as close literature, but only its public abstract-level description was available in this review.

## References
1. Y. Wu and P. Chen, *Least-Favorable Location for Binomial Top-\(t\) Selection*, arXiv:2609.03466v1, first public 2026-09-03.
2. C. A. Tovey, *The Slippage Configuration Is Always the Least Favorable Configuration for Two Alternatives*, Sequential Analysis 33(4), 509–518, 2014, DOI 10.1080/07474946.2014.961854.
3. M. Wang, *On Selecting the \(t\) Best of \(k\) Binomial Populations*, PhD dissertation, Syracuse University, 2023.
