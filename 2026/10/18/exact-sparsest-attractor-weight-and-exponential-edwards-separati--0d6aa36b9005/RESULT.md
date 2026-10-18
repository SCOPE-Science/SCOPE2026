# Exact sparsest-attractor weight and exponential Edwards separation in the Riviera deposition model

## Finding

For every integer \(k\geq1\), run the random sequential Riviera deposition process on the open chain of \(4k\) sites, initially empty, with uniformly random first-visit order. Write \(Q_{4k}\) for the number of houses in its final jammed configuration. Then

\[
\boxed{\Pr(Q_{4k}=2k)=6^{-k}.}
\]

The unique final configuration realizing \(Q_{4k}=2k\) is the word \((0110)^k\); no jammed configuration has fewer than \(2k\) houses. Its attracting-permutation count is exactly

\[
\boxed{W((0110)^k)=(4k)!\,6^{-k}.}
\]

In particular, the **exact minimum-coverage dynamical endpoint rate** along this subsequence is

\[
\boxed{-\lim_{k\to\infty}\frac{1}{4k}\log\Pr(Q_{4k}=2k)=\frac{\log 6}{4}.}
\]

Let \(\Pr_{\rm flat}\) denote the *full*, not fixed-coverage, uniform distribution over all jammed configurations of length \(4k\). A quantitative separation between the physical deposition law and this flat blocked-state ensemble is

\[
\boxed{\frac{\Pr(Q_{4k}=2k)}{\Pr_{\rm flat}(Q_{4k}=2k)}\leq\left(\frac{27}{32}\right)^k.}
\]

Thus the dynamical probability of the sparsest blocked state is exponentially smaller than its full flat-ensemble probability. No general large-deviation principle away from this endpoint is asserted.

## Assumptions and scope

Sites \(1,\ldots,N\) form an open path. At any time a site is either vacant (symbol \(0\)) or permanently occupied (symbol \(1\)). External boundary sites are treated as vacant. A proposed occupation is accepted *only* if the resulting configuration contains no run of three adjacent occupied sites. Equivalently, every already occupied site retains a vacant neighbor, possibly outside the boundary. A rejected attempt never changes the configuration. Initially all sites are vacant. Each site is proposed at its first visit, with the \(N!\) possible first-visit permutations equally likely; subsequent proposals are irrelevant. The process ends after every site has been visited, and its terminal configuration is jammed (no legal vacancy remains). This is the original global sunlight-preserving Riviera constraint, not an alternative rule testing only the newly deposited house.

The result concerns \(N=4k\), \(k\ge1\), exact minimum coverage, and the open-boundary convention. The comparator is the uniform measure on **all** jammed configurations of that same length, without conditioning on the number of houses. No statement is made about periodic boundaries, unequal site-arrival rates, or near-minimum coverage densities.

## Proof

**1. Identify the only sparsest jammed state.** Let \(J_{n,m}\) denote the number of jammed binary words of length \(n\) with \(m\) occupied sites under the same open boundary convention. The established static transfer-matrix enumeration [1, 2] gives

\[
\mathcal Z(x,y)=\sum_{n,m\ge0}J_{n,m}x^my^n
=\frac{1+xy+x(x-1)y^2+x^2y^3-x^3y^5}
{1-xy^2-x^2(y^3+y^4)+x^3y^6}.
\]

The substitution \(x=u^2\), \(y=z/u\) yields the formal series

\[
\mathcal Z(u^2,z/u)=
\frac{1-z^2+u(z+z^3-z^5)+u^2z^2}
{(1-z^2)(1-z^4)-uz^3}.
\]

Its denominator has constant term one in the bivariate formal variables, and its numerator contains no negative power of \(u\). Therefore \(J_{n,m}=0\) whenever \(2m<n\). Moreover the coefficient of \(u^0\) is exactly

\[
[u^0]\mathcal Z(u^2,z/u)=\frac{1}{1-z^4}
=\sum_{j\ge0}z^{4j}.
\]

Consequently \(J_{4k,2k}=1\). The explicit word \(w_k=(0110)^k\) is permissible (it has no run \(111\)), and is jammed because each vacant site has two consecutive occupied sites immediately on its interior side within its own four-site block. Hence \(w_k\) is the unique jammed word with \(2k\) houses.

**2. Compute its entire dynamical basin.** Realize the uniformly random first-visit order by independent continuous identically distributed priorities \(T_1,\ldots,T_{4k}\). In block \(B_j=(4j+1,4j+2,4j+3,4j+4)\), with \(0\leq j<k\), the two intended houses are the middle sites; the two intended vacancies are the outer sites.

A final state equal to \(w_k\) requires both middle sites of each block to have been visited before either outer site: a vacancy at the left edge could only have been rejected because the next two middle sites were already occupied, and likewise for a vacancy at the right edge. No other triple of final occupied sites contains that vacancy, so the precedence condition is necessary. Conversely, when this condition holds blockwise, all intended houses are accepted (their partial occupation remains a subset of the permissible word \(w_k\)), and every intended vacancy is rejected after both of its blocking houses have arrived. Thus the condition is sufficient as well.

For four independent continuous priorities, the probability that the two designated middle priorities both precede the two designated outer priorities is

\[
\frac{2!\,2!}{4!}=\frac16.
\]

These within-block events are independent across the \(k\) disjoint blocks, even though their visits may be interleaved globally. Therefore \(\Pr(w_k)=6^{-k}\). As this word is the unique sparsest jammed state, the claimed exact probability and permutation weight follow. Taking the logarithm gives the endpoint rate.

**3. Quantify the departure from the full flat ensemble.** Write \(J_n=\sum_m J_{n,m}\) for the total number of jammed words. The same published generating function implies [2]

\[
J_n=J_{n-2}+J_{n-3}+J_{n-4}-J_{n-6}\quad(n\ge6),
\]

with \((J_0,J_1,J_2,J_3,J_4,J_5)=(1,1,1,3,3,4)\). Since all \(J_j\) are nonnegative and

\[
(3/2)^{-2}+(3/2)^{-3}+(3/2)^{-4}=\frac{76}{81}<1,
\]

induction gives \(J_n\le(3/2)^n\) for every \(n\ge0\), including the six initial values. Since there is exactly one sparsest jammed word, \(\Pr_{\rm flat}(Q_{4k}=2k)=1/J_{4k}\). It follows that

\[
\frac{\Pr(Q_{4k}=2k)}{\Pr_{\rm flat}(Q_{4k}=2k)}
=\frac{J_{4k}}{6^k}
\le\left(\frac{(3/2)^4}{6}\right)^k
=\left(\frac{27}{32}\right)^k.
\]

All assertions hold for every positive integer \(k\), without a finite-size cutoff.

## Verification

Run `python3 CHECKER.py` with the Python 3 standard library. The included checker reproduces the coefficients of the published jammed-state generating function through length 80, enumerates every jammed binary word at lengths 4, 8, 12 and 16, and enumerates all \(4!\) and \(8!\) arrival orders independently. It verifies the published weights \(W(0110)=4\) and \(W(01100110)=1120\), the two minimal-state uniqueness claims at these finite sizes, and the exact exponential formulas. In the completed check, all 1,560 assertions passed. These finite tests corroborate the proof; they are not a substitute for the formal generating-function argument and blockwise-order equivalence.

## Relationship to prior work

Došlić, Puljiz, Šebek and Žubrinić [1] introduced the open-boundary Riviera constraint and its static exact enumerations. Their work focuses on static configurations rather than dynamical basin probabilities. Krapivsky and Luck [2] established the same static generating function and the first-visit-permutation description of the stochastic process. Their dynamical-weight table explicitly includes \(W(0110)=4\) and \(W(01100110)=1120\); these are the \(k=1,2\) cases of the theorem, **not** new results. Their reported thermodynamic Riviera dynamics is otherwise obtained numerically. The new result here is the all-length exact *dynamical* minimum-coverage event and its exponential comparison with the full flat ensemble. The static uniqueness and enumeration are cited premises, not claimed as original discoveries.

Viot [3] studies an approximate kinetic hierarchy and jammed-density observables for periodic Riviera systems, a different boundary setting and observable from the finite open-chain minimum-coverage basin. The existing flat-versus-dynamical distinction [2] is known; the quantitative rare-event endpoint estimate here addresses a more specific question.

## Limitations

The result is exact only for the original global sunlight-preserving deposition constraint on open paths whose length is a multiple of four, with uniformly random first-visit order. It does not compute the full distribution of final coverage, any large-deviation function away from its sparsest endpoint, or finite-size corrections for other congruence classes. The upper bound \((27/32)^k\) is an explicit rigorous comparison, not an optimal constant or a claim about the measure conditioned on fixed coverage. Priority relative to mathematically equivalent statements in uninspected literature remains subject to independent scholarly assessment. Scientific correctness and priority are distinct questions; numerical checks cannot establish either originality or the all-length theorem by themselves.

## References

[1] T. Došlić, M. Puljiz, S. Šebek, and J. Žubrinić, *On a variant of Flory model*, arXiv:2210.12411v1 (first public 2022-10-22), https://arxiv.org/abs/2210.12411 .

[2] P. L. Krapivsky and J. M. Luck, *Jamming and metastability in one dimension: from the kinetically constrained Ising chain to the Riviera model*, arXiv:2211.12815v1 (first public 2022-11-23), https://arxiv.org/html/2211.12815v1 . See Section 3.2.2, equations (68)–(71), Section 3.3, and Table 2.

[3] P. Viot, *Convergence to the exact kinetics of the one-dimensional Riviera model*, arXiv:2607.28419 (first public 2026-07-30), https://arxiv.org/abs/2607.28419 .
