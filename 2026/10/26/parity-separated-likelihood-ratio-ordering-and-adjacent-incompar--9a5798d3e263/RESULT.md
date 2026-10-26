# Parity-separated likelihood-ratio ordering and adjacent incomparability for random chord degrees

## Finding
Fix an integer \(n\ge3\). Choose a perfect matching uniformly from the \((2n-1)!!\) matchings of \(2n\) cyclically ordered, individually labeled endpoints. Let \(c\) be the chord containing endpoint \(1\), and let \(L\in\{0,\ldots,n-1\}\) be the number of endpoints strictly between the endpoints of \(c\) along its *shorter* arc. Let \(D_k\) denote the number of chords crossing \(c\), conditional on \(L=k\).

For \(0\le k\le n-1\), write \(N=2n-2\). The conditional mass function, for integers \(0\le h\le k\) with \(h\equiv k\pmod2\), is
\[
 p_{n,k}(h)=\frac{k!(N-k)!}{(N-1)!!\,h!\,2^{(N-2h)/2}\,((k-h)/2)!\,((N-k-h)/2)!}.
\]
All other masses vanish, and \((-1)!!=1\). For every \(0\le k\le n-3\), the two-step comparison has exact likelihood ratio
\[
 \frac{p_{n,k+2}(h)}{p_{n,k}(h)}
 =\frac{(k+2)(k+1)(N-k-h)}{(N-k)(N-k-1)(k+2-h)},
 \qquad h=k,k-2,\ldots, k\bmod2.
\]
This ratio increases strictly with \(h\) whenever the common support has two or more values, and the longer-chord law has additional positive mass at \(k+2\). Therefore \(D_{k+2}\) strictly dominates \(D_k\) in likelihood-ratio order and in first-order stochastic order. In particular, every subsequence indexed by one parity is strictly ordered.

In sharp contrast, for every \(1\le k\le n-2\), the adjacent laws \(D_k\) and \(D_{k+1}\) are **incomparable** in first-order stochastic order. The only adjacent exception is \(D_0=0<D_1=1\) almost surely. Yet the means increase strictly at *every* step:
\[
 \mathbb ED_k=\frac{k(N-k)}{N-1},\qquad
 \mathbb ED_{k+1}-\mathbb ED_k=\frac{N-2k-1}{N-1}>0,
 \quad 0\le k\le n-2.
\]

Thus higher mean degree does not generally entail even a one-sided comparison of crossing-count tails, while parity-preserving increments yield the stronger likelihood-ratio order.

## Assumptions and scope
All endpoints are distinct and carry a fixed cyclic order. Each perfect matching is equally likely. Conditional on \(L=k\), the location of the other endpoint of \(c\) may have one or two reflected possibilities; both induce the same conditional degree law. The word *crossing* means alternating chord endpoints around the circle. First-order stochastic domination means \(X\le_{\mathrm{st}}Y\) if \(\Pr(X\ge t)\le\Pr(Y\ge t)\) for all real \(t\). Likelihood-ratio ordering means the ratio of the two mass functions, with natural conventions at zeros, is nondecreasing on their ordered union of supports; the two distributions here share a parity lattice.

## Proof
Condition on the two endpoints of \(c\). Their removal leaves \(N=2n-2\) endpoints, with \(k\) on the shorter side and \(N-k\) on the other. There are \((N-1)!!\) equiprobable matchings of these remaining endpoints. Exactly \(h\) pairs cross \(c\) precisely when \(h\) endpoints on each side are matched across the cut. Select them in \(\binom{k}{h}\binom{N-k}{h}\) ways, pair them with a bijection in \(h!\) ways, and match the remaining points internally in \((k-h-1)!!(N-k-h-1)!!\) ways. This is possible exactly when \(h\equiv k\pmod2\). Simplifying the count gives the displayed normalized conditional mass function. This is an identity for every \(n,k,h\), not a limiting approximation.

For \(0\le k\le n-3\), divide the two factorial formulas. The factorial ratios simplify exactly to the displayed \(p_{n,k+2}(h)/p_{n,k}(h)\). Treating \(h\) temporarily as a real variable, the only varying factor is \((N-k-h)/(k+2-h)\), whose derivative has numerator \(N-2k-2>0\). Hence likelihood ratios increase strictly along the shared parity lattice whenever at least two common points exist. At the new maximum \(k+2\), \(p_{n,k+2}\) has positive mass while \(p_{n,k}\) has none. The likelihood-ratio order is therefore strict even at \(k=0,1\), where the shared support is a singleton. Standard finite-sum cross-multiplication, or equivalently the single-crossing sign pattern of the two probability differences, yields strict first-order stochastic dominance. Transitivity yields ordering for every two lengths of the same parity.

Now take \(1\le k\le n-2\). If \(k\) is odd, \(D_k\ge1\) always but \(\Pr(D_{k+1}=0)>0\), preventing \(D_k\le_{\mathrm{st}}D_{k+1}\). Also \(\Pr(D_{k+1}=k+1)>0\) whereas \(D_k\le k\) always, preventing the reverse domination. If \(k\) is even (so \(k\ge2\)), \(\Pr(D_k=0)>0\) but \(D_{k+1}\ge1\) always, preventing \(D_{k+1}\le_{\mathrm{st}}D_k\). At the other extreme, using the probability formula,
\[
 \frac{\Pr(D_{k+1}=k+1)}{\Pr(D_k=k)}
 =\frac{N-2k}{N-k}<1.
\]
The tail at threshold \(k\) is therefore strictly smaller for \(D_{k+1}\) than for \(D_k\), so \(D_k\le_{\mathrm{st}}D_{k+1}\) fails as well. Both parity cases establish incomparability. At \(k=0\), all remaining chords lie on one side and \(D_0=0\); at \(k=1\), that endpoint must match across and \(D_1=1\).

Lastly, each of the \(k\) endpoints on the shorter side matches across with probability \((N-k)/(N-1)\). By indicator linearity, \(\mathbb ED_k=k(N-k)/(N-1)\), yielding the asserted strictly positive adjacent mean gap because \(k\le n-2\).

## Verification
The standalone standard-library script `verify.py` evaluates the factorial probability formula exactly with `fractions.Fraction`, checks the two-step likelihood ratios and mean identities, tests the stochastic orders and non-orders, and independently enumerates **every** perfect matching of up to \(14\) labeled endpoints. Execution reported `VERIFIED: 128 checks, including exhaustive matchings through 14 endpoints`. The finite enumeration is corroboration; the preceding counting and inequality arguments prove the unrestricted theorem.

For example, at \(n=5\), \(D_1=1\) almost surely but \(D_2\) equals \(0\) with probability \(1/7\) and \(2\) with probability \(6/7\). Hence its mean is \(12/7>1\) while its distribution is not first-order comparable to that of \(D_1\).

## Relationship to prior work
Acan's 2013 thesis, Chapter 3.1, and Acan's January 7, 2015 preprint, Section 2, introduce precisely this distinguished-chord length and conditional crossing degree. They derive conditional expectations and variances and the asymptotic marginal degree law. Those inspected passages do not state or imply via a given stochastic-order theorem the finite-sample likelihood-ratio order within parities or the adjacent incomparability result. The exact conditional mass formula here is a direct elementary matching count; novelty is claimed only for its order-theoretic consequences, not the counting technique itself. Acan and Pittel's 2014 preprint addresses global crossings and giant-component formation, not this conditional order. Previously reported exact moments, inverse covariance, and functional limits for cut-crossing counts concern a related matching-cut process, but its moment and limit statements alone do not entail the current finite-sample distribution comparisons.

## Limitations
The result concerns one distinguished chord in a **uniform** random matching at fixed size, not joint dependence among degrees of several chords, nonuniform matchings, or general circle-graph models. The claim does not classify arbitrary comparisons between nonadjacent **opposite-parity** lengths. The exact probabilities follow from elementary enumerations; an unlocated older treatment may have observed the same order properties. No independent audit or historical-priority certification is asserted.

## References
1. H. Acan, *An Enumerative-Probabilistic Study of Chord Diagrams*, PhD thesis, The Ohio State University (2013), Chapter 3.1. Open full text: https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1373310487&disposition=inline
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, first posted 2015-01-07, Section 2. https://arxiv.org/abs/1501.01489
3. H. Acan and B. Pittel, *Formation of a giant component in the intersection graph of a random chord diagram*, arXiv:1406.2867v1 (2014). https://arxiv.org/abs/1406.2867
