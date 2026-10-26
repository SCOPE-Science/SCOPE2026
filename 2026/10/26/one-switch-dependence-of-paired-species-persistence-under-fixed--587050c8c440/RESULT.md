# One-switch dependence of paired species persistence under fixed-quota partner loss

## Finding

**Theorem (sharp one-switch co-survival law).** Let \(U\) contain \(N\ge2\) potential mutualistic partners and let \(A,B\subseteq U\) be nonempty, proper neighbor sets of two dependent species. Put \(a=|A|\), \(b=|B|\), \(h=|A\cap B|\). For every \(q\in\{0,\ldots,N\}\), retain a uniformly chosen \(q\)-subset \(T_q\subseteq U\), and let \(X_A(q)=\mathbf{1}\{T_q\cap A\ne\varnothing\}\) and similarly \(X_B(q)\). Thus a dependent species persists if it retains at least one original partner. With \(\binom{r}{q}=0\) for integers \(q>r\ge0\),

\[
\operatorname{Cov}(X_A(q),X_B(q))=\frac{\binom{N-a-b+h}{q}\binom Nq-\binom{N-a}{q}\binom{N-b}{q}}{\binom Nq^2}. \tag{1}
\]

For the **nondegenerate range** \(1\le q\le Q:=N-\max\{a,b\}\), its sign has a complete classification:

- If \(h=0\), the covariance is strictly negative.
- If \(h=\min\{a,b\}\), the covariance is strictly positive.
- If \(0<h<\min\{a,b\}\) and \(Nh<ab\), it is strictly negative at every such \(q\). At \(Nh=ab\), it is zero for \(q=1\) and strictly negative for all \(q\ge2\) in the range.
- If \(0<h<\min\{a,b\}\) and \(Nh>ab\), it is positive at \(q=1\), becomes negative before the nondegenerate range ends, and changes sign **at most once**, in the direction positive to negative. At most one intermediate integer value of \(q\) can have zero covariance. More precisely, its positive, zero (if any), and negative values occur in that order with no gaps between phases.

When \(q>Q\), at least one of the two survival indicators is identically one, so covariance is zero. The smallest possible partner pool exhibiting a positive-to-negative reversal is \(N=5\). A sharp witness is \(A=\{1,2\}\), \(B=\{2,3\}\) in \(U=\{1,2,3,4,5\}\): the covariance at \(q=1,2,3,4\) is respectively \(1/25,1/100,-1/100,0\).

The same two neighbor sets under independent Bernoulli partner survival with common probability \(p\in(0,1)\) instead satisfy

\[
\operatorname{Cov}(X_A,X_B)=(1-p)^{a+b-h}\bigl(1-(1-p)^h\bigr), \tag{2}
\]

which is positive whenever \(h>0\). Thus a fixed restoration/survival quota, rather than habitat-partner sharing alone, can reverse the direction of pairwise co-persistence dependence.

## Assumptions and scope

The network is finite, simple, bipartite, and fixed throughout the experiment. Only the \(N\) vertices in the primary partner guild are initially selected; exactly \(q\) of them survive and every \(q\)-subset is equally likely. The two dependent species survive if and only if at least one of their original partner vertices survives. No further trophic cascades, density response, compensatory rewiring, asymmetric selection, or stochastic interaction effectiveness is modeled. The theorem applies whether or not other dependent species are present. We assume \(1\le a,b\le N-1\) and \(\max\{0,a+b-N\}\le h\le\min\{a,b\}\). There are no claims about correlation coefficients when a variance vanishes.

## Proof

**1. Exact covariance.** Let \(Y_A=1-X_A\), the event of losing all members of \(A\). Because a uniform \(q\)-subset avoids a fixed \(d\)-subset with probability \(\binom{N-d}{q}/\binom Nq\),

\[
\mathbb EY_A=\frac{\binom{N-a}{q}}{\binom Nq},\quad
\mathbb EY_B=\frac{\binom{N-b}{q}}{\binom Nq},\quad
\mathbb E(Y_AY_B)=\frac{\binom{N-a-b+h}{q}}{\binom Nq}.
\]

Since \(\operatorname{Cov}(1-Y_A,1-Y_B)=\operatorname{Cov}(Y_A,Y_B)\), subtraction proves (1), including zero-probability boundary cases.

**2. A discrete likelihood ratio.** Set \(d=N-a-b+h\) and \(Q=N-\max\{a,b\}\). For \(0\le q\le d\), define

\[
R_q=\frac{\binom dq\binom Nq}{\binom{N-a}{q}\binom{N-b}{q}}.
\]

The denominator is positive here; \(R_0=1\), and the covariance sign is the sign of \(R_q-1\). For \(0\le q<d\), direct cancellation gives

\[
\frac{R_{q+1}}{R_q}
=\frac{(d-q)(N-q)}{(N-a-q)(N-b-q)},\qquad
\operatorname{sgn}\biggl(\frac{R_{q+1}}{R_q}-1\biggr)
=\operatorname{sgn}\bigl(h(N-q)-ab\bigr). \tag{3}
\]

All denominators in (3) are positive. The quantity \(h(N-q)-ab\) decreases with \(q\) (strictly when \(h>0\)); consequently \(R_q\) first increases, then decreases, with either phase possibly empty and a possible flat step at the turning point. For \(d<q\le Q\), set \(R_q=0\): then the numerator of (1) is zero while both factors in its subtracted term remain positive, hence covariance is negative. If \(d<Q\), the transition \(R_d>0\) to \(R_{d+1}=0\) is decreasing.

**3. Complete sign classification.** For disjoint neighborhoods \(h=0\), (3) is strictly negative at every available step, and the case \(d=0\) has \(R_1=0\); covariance is negative at all \(1\le q\le Q\). If the sets are nested, say \(A\subseteq B\), then \(X_A\le X_B\), and

\[
\operatorname{Cov}(X_A,X_B)=\mathbb P(X_A=1)\mathbb P(X_B=0)>0
\]

for all \(1\le q\le Q\), as \(a,b<N\). For strict partial overlap, \(0<h<\min\{a,b\}\) implies \(d<Q\). If \(Nh\le ab\), (3) is nonpositive from the outset; equality is possible only for \(R_1=1\) at \(Nh=ab\), because the subsequent signed differences are strictly negative. If \(Nh>ab\), (3) gives \(R_1>R_0=1\), whereas \(R_{d+1}=0<1\) with \(d+1\le Q\). Unimodality of \(R_q\) therefore forces precisely one possible boundary from covariance-positive to covariance-negative values, allowing exactly one integer tie at that boundary. This proves every quantified sign assertion.

**4. Sharp minimum.** A reversal requires strict partial overlap and \(Nh>ab\). Hence \(h\ge1\), \(a,b\ge h+1\), and \(ab\ge(h+1)^2\ge4h\). If \(N\le4\), then \(Nh\le4h\le ab\), impossible. At \(N=5\), the stated two neighborhoods have \(a=b=2\), \(h=1\), and \(Nh=5>4=ab\); direct substitution in (1) yields the four rational values displayed above.

**5. Independent survival comparison.** When partner survival is independent with probability \(p\), the two avoidance events have probabilities \((1-p)^a\), \((1-p)^b\), and \((1-p)^{a+b-h}\) jointly. Their covariance gives (2).

## Verification

The accompanying `verify.py` uses Python 3's standard library. It verifies (1) against explicit enumeration of all uniform retained subsets for all valid neighborhood cardinalities through \(N=8\), verifies the sign classification by exact-rational binomial evaluation for every valid cardinality quadruple through \(N=50\), and reproduces the five-partner sharp example. Execute `python verify.py` and compare the resulting JSON with `certificate.json`. The recorded run checked 311150 cardinality cases, 4624790 nondegenerate sign instances, and 51192 explicitly enumerated retained subsets. These finite checks do not prove the unrestricted theorem; Steps 1–5 do.

## Relationship to prior work

Memmott, Waser and Price (2004) model coextinction in pollination networks under random removal without replacement and present aggregate attack-tolerance results, providing the primary ecological setting. Burgos, Ceva, Hernandez and Perazzo (2008) analyze nested mutualistic networks and robustness under random and degree-ordered attacks. Joag-Dev and Proschan (1983) establish negative association for sampling without replacement, which explains the disjoint-neighborhood case but does not by itself provide the overlapping-neighborhood one-switch law. The present result is an exact pairwise sign-phase theorem for uniformly fixed-size partner pools, with a sharp five-partner reversal and an explicit contrast to independent primary survival. Published coverage of an equivalent formulation under other terminology remains a bibliographic risk.

## Limitations

Only a simple one-step coextinction rule is studied. In particular, primary losses are **uniform at fixed count**, not independent Bernoulli losses; the sign reversal need not survive weighted partner-selection schemes. The result controls pairwise covariance, not the entire distribution or variance of total species richness, and it does not supply an estimator from finite ecological survey data. Literature equivalence under reliability/correlation inequalities remains possible and independent review has not been performed.

## References

1. Joag-Dev, K., and Proschan, F. (1983), “Negative Association of Random Variables with Applications,” *Annals of Statistics* 11, 286–295. DOI: 10.1214/aos/1176346079. https://doi.org/10.1214/aos/1176346079
2. Memmott, J., Waser, N. M., and Price, M. V. (2004), “Tolerance of pollination networks to species extinctions,” *Proceedings of the Royal Society B* 271, 2605–2611. First published online 2004-12-06. DOI: 10.1098/rspb.2004.2909. https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf
3. Burgos, E., Ceva, H., Hernandez, L., and Perazzo, R. P. J. (2008), “Understanding and characterizing nestedness in mutualistic bipartite networks,” arXiv:0809.3681, first posted 2008-09-22. https://arxiv.org/abs/0809.3681
