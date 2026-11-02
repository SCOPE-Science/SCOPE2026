# Monotone likelihood-ratio ordering of bridge return times by total zero contacts

## Finding
For a nearest-neighbor random-walk bridge of length \(2n\), the time of its \(r\)-th return to zero decreases in **monotone likelihood-ratio order** when the total number of returns increases. The result holds at every finite size, for all return ranks and for any fixed nondegenerate up-step probability.

Write \(K\) for the number of returns to zero at strictly positive times, including the terminal time, and \(T_r\) for half the time of the \(r\)-th return. Define
\[
a_{m,j}=\frac{j}{2m-j}\binom{2m-j}{m-j}\qquad(1\le j\le m).
\]
For integers \(n\ge2\), \(1\le r<k\le n\), and \(r\le t\le n-k+r\), the exact conditional law is
\[
\Pr(T_r=t\mid K=k)
=\frac{a_{t,r}a_{n-t,k-r}}{a_{n,k}}.
\]
For \(r<k<n\), put \(q=k-r\) and \(u=n-t\). On the common support of the two consecutive conditional laws,
\[
\frac{\Pr(T_r=t\mid K=k+1)}{\Pr(T_r=t\mid K=k)}
=\frac{k(2n-k-1)}{(k+1)(n-k)}
\frac{q+1}{q}\frac{u-q}{2u-q-1}.
\]
This ratio is nonincreasing in \(t\), strictly decreasing at distinct common-support points when \(q\ge2\), and constant when \(q=1\). The law with \(K=k+1\) has no mass at the largest possible \(T_r\) under \(K=k\). Hence for all \(r\le k<k'\le n\),
\[
T_r\mid(K=k')\ <_{\mathrm{st}}\ T_r\mid(K=k)
\]
in the strict first-order sense (with \(T_k=n\) deterministically when \(K=k\)). In particular, the conditional expectation of every strictly increasing function of the return time strictly decreases with the total number of returns, whenever the function is integrable on the finite support.

There is an exact exceptional truncation law. When \(r=k-1\), \(2\le k<n\),
\[
\mathcal L(T_{k-1}\mid K=k+1)
=\mathcal L(T_{k-1}\mid K=k,\ T_{k-1}\le n-2),
\]
and the total-variation distance between these two (untruncated) conditional laws is exactly
\[
\frac{n(k-1)}{k(2n-k-1)}.
\]

## Assumptions and scope
Take independent increments \(X_i\in\{-1,1\}\), each with \(\Pr(X_i=1)=p\in(0,1)\), and condition on \(\sum_{i=1}^{2n}X_i=0\). Every resulting bridge path has \(n\) upward and \(n\) downward steps, and all such paths have the same conditional probability \(\binom{2n}{n}^{-1}\). Thus the laws in the finding are independent of \(p\). Returns are counted at times \(2,4,\ldots,2n\); in particular \(1\le K\le n\). When \(r=k\), \(T_r=n\) on \(K=k\). All strict likelihood-ratio claims require two distinct common-support points; the strict stochastic order also holds in boundary cases with singleton common support.

## Proof
An excursion of semilength \(j\ge1\) is a walk from zero to zero with no intervening zero. Its number of possibilities is \(2C_{j-1}\), where \(C_i=\binom{2i}{i}/(i+1)\) is a Catalan number; the factor two specifies its sign. Put
\[
F(z)=\sum_{j\ge1}C_{j-1}z^j=\frac{1-\sqrt{1-4z}}2.
\]
The identity \(F=z+F^2\), equivalently \(F=z/(1-F)\), and Lagrange inversion give
\[
[z^m]F(z)^j=\frac{j}{m}\binom{2m-j-1}{m-j}
=\frac{j}{2m-j}\binom{2m-j}{m-j}=a_{m,j}.
\]
Thus the number of bridges with exactly \(k\) excursions is \(2^k a_{n,k}\). To have the \(r\)-th return at time \(2t\), the first \(r\) excursions have total semilength \(t\) and the remaining \(k-r\) have total semilength \(n-t\). Their signs are arbitrary, so there are \(2^k a_{t,r}a_{n-t,k-r}\) such bridges, proving the stated probability.

For positive \(q\) and \(u\ge q+1\), elementary factorial cancellation yields
\[
\frac{a_{u,q+1}}{a_{u,q}}
=\frac{q+1}{q}\frac{u-q}{2u-q-1}.
\]
Applying the same identity to \(a_{n,k+1}/a_{n,k}\) gives the adjacent conditional likelihood ratio in the finding. For \(u\ge q+1\), its only \(t\)-dependent factor \((u-q)/(2u-q-1)\) has derivative \((q-1)/(2u-q-1)^2\) in \(u\). Thus it increases with \(u=n-t\) for \(q>1\), and is constant for \(q=1\). At the final point \(t=n-q\) supported when \(K=k\), the conditional law with \(K=k+1\) is zero. Consequently the ratio, extended by zero at the rightmost point, is nonincreasing. This is monotone likelihood-ratio ordering; normalization implies first-order stochastic ordering, strict because the smaller-\(K\) law assigns positive mass to a rightmost point that the larger-\(K\) law cannot attain. Repeated adjacent comparisons prove the ordering for arbitrary \(k<k'\), including the deterministic endpoint \(r=k\).

For \(r=k-1\), the ratio is constant on \(t\le n-2\), and vanishes at \(t=n-1\). Normalization therefore gives the claimed exact truncation identity. The removed probability is
\[
\Pr(T_{k-1}=n-1\mid K=k)
=\frac{a_{n-1,k-1}}{a_{n,k}}
=\frac{n(k-1)}{k(2n-k-1)}.
\]
For a probability measure and its restriction conditioned on an event, total-variation distance equals the removed mass. This completes the proof.

## Verification
The standalone Python program `verification.py` independently enumerates every balanced nearest-neighbor bridge through semilength ten, checks the exact excursion and return-time counts, and checks likelihood-ratio monotonicity and the sharp boundary identity using integer arithmetic. It also checks the closed formula, normalization, strict stochastic order and the exact exceptional truncation formula for additional finite sizes. These computations are finite consistency checks; the proof above establishes the statements for all admissible integers.

## Relationship to prior work
Lindell and Holst (2007) analyze the distribution of the longest excursions in tied-down random walks and Brownian bridges, and give the first-return generating function and joint excursion-length machinery. Voss (October 17, 2007) derives the marginal distribution of the total number of bridge returns. Those ingredients are acknowledged; the result here is the *entire finite-size likelihood-ratio hierarchy of the chronological return times conditional on their total count*, including the exact last-return truncation and its total-variation distance. The cited primary study treats ranked longest excursions rather than chronological return times conditioned on their number. The known excursion enumerations are inputs to the new comparison, not independently claimed contributions.

## Limitations
The theorem concerns finite nearest-neighbor bridges with a fixed endpoint; it does not assert a corresponding monotone likelihood-ratio order for Brownian-bridge local times, for longest-excursion lengths, or for walks with arbitrary increment laws. Existing enumerative formulae make the new inequality short to prove, so historical priority could be affected by a previously unnoticed equivalent formulation.

## References
1. A. Lindell and L. Holst, *Distributions of the longest excursions in a tied down simple random walk and in a Brownian bridge*, Journal of Applied Probability **44** (2007), 1056–1067, https://doi.org/10.1239/jap/1197908824.
2. J. Voss, *Random walk bridges*, dated 2007-10-17, https://www.seehuhn.de/blog/6.html.
3. W. Feller, *An Introduction to Probability Theory and Its Applications*, Vol. 1, 3rd edition (1968), cited for classical first-return/Catalan enumeration.
