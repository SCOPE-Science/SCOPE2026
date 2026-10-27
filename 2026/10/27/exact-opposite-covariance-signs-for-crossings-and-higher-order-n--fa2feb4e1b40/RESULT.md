# Exact opposite covariance signs for crossings and higher-order nestings in random matchings

## Finding

Let \(M\) be a uniformly random perfect matching on the ordered vertex set \([2n]\), where \(n\ge3\). Let \(C_2\) count pairs of intersecting arcs. For each \(3\le r\le n\), let \(C_r\) count subsets of \(r\) arcs whose left endpoints precede all their right endpoints in the same relative order, and let \(N_r\) count subsets with left endpoints followed by the right endpoints in reverse relative order. With \(p_r=1/(2r-1)!!\),

\[
\mathbb E C_r=\mathbb E N_r=\binom nr p_r,
\qquad
\operatorname{Cov}(C_2,C_r)=\binom nr p_r\frac{r(r-1)(n+r+1)}{3(2r+1)},
\]

\[
\operatorname{Cov}(C_2,N_r)=-\binom nr p_r\frac{r(r-1)}6.
\]

In particular the first covariance is strictly positive and the second strictly negative throughout the stated range. For \(r=3\), the latter simplifies to \(-\binom n3/15\).

## Assumptions and scope

A matching is sampled uniformly from the \((2n-1)!!\) perfect matchings of \([2n]\). Each arc is a pair \((a,b)\) with \(a<b\). Two arcs cross if their endpoints alternate, and they nest if one pair of endpoints strictly contains the other. An \(r\)-crossing consists of \(r\) mutually crossing arcs; an \(r\)-nesting has the canonical globally nested endpoint arrangement. Subsets, rather than maximum crossing or nesting sizes, are counted. All asserted covariances concern \(n\ge3\) and \(3\le r\le n\).

## Proof

**Exchangeably labeled representation.** Give \(n\) distinct arc labels two independent continuously uniform points in \((0,1)\) each; order the resulting \(2n\) points and forget arc labels. Each matching of \([2n]\) has exactly \(2^n n!\) endpoint-label realizations, so the induced matching is uniform. Restricting to any specified \(r\) arc labels gives a uniform matching on those \(2r\) points. A specified set of \(r\) arcs is an \(r\)-crossing precisely for one of the \((2r-1)!!\) pairings of its ordered endpoints; the same holds for a complete nesting. Their common probability is \(p_r\).

**A crossing against an outside arc.** Fix one arc with endpoints \(u<v\) and length \(q=v-u\). An outside independent arc crosses it with probability \(2q(1-q)\). Condition a specified \(r\)-set of arcs to be a complete crossing. Its ordered \(2r\) endpoint positions remain the order statistics of \(2r\) independent uniforms. Every arc joins positions \(j\) and \(r+j\), so its length has the beta distribution \(\mathrm{Beta}(r,r+1)\). Thus its conditional outside crossing probability is

\[
\frac{2r(r+1)}{(2r+1)(2r+2)}=\frac r{2r+1}.
\]

Condition instead on a complete nesting. The \(j\)-th outer-to-inner arc joins ordered endpoints \(j\) and \(2r+1-j\), with rank gap \(d_j=2r+1-2j\), and hence length distribution \(\mathrm{Beta}(d_j,2r+1-d_j)\). Each distinguished arc occupies each nesting rank with probability \(1/r\), so the average conditional outside-crossing probability is

\[
\frac{2}{r(2r+1)(2r+2)}\sum_{j=1}^r d_j(2r+1-d_j)
=\frac13.
\]

Indeed \(\sum_{j=1}^r (2r+1-2j)(2j)=r(r+1)(2r+1)/3\). Independently of either conditioning, a specified pair of arcs crosses with probability \(1/3\).

**Classification by overlapping arc labels.** Fix a specified \(r\)-subset \(S\) of arc labels and consider a candidate crossing pair \(P\). If \(P\cap S=\varnothing\), its crossing indicator is independent of either the crossing or nesting event on \(S\). There are \(r(n-r)\) pairs with \(|P\cap S|=1\). By the conditional probabilities above, each gives covariance \(p_r(r/(2r+1)-1/3)=p_r(r-1)/(3(2r+1))\) against the event that \(S\) crosses, and zero covariance against the event that \(S\) nests. There are \(\binom r2\) pairs \(P\subseteq S\): each is forced to cross when \(S\) crosses and forced not to cross when \(S\) nests, yielding respective contributions \(2p_r/3\) and \(-p_r/3\). Therefore linearity of covariance yields

\[
\operatorname{Cov}(C_2,C_r)=\binom nr p_r\left[\frac{r(n-r)(r-1)}{3(2r+1)}+\frac23\binom r2\right]
=\binom nr p_r\frac{r(r-1)(n+r+1)}{3(2r+1)},
\]

\[
\operatorname{Cov}(C_2,N_r)=\binom nr p_r\left[0-\frac13\binom r2\right]
=-\binom nr p_r\frac{r(r-1)}6.
\]

All probabilities are positive, and the signs follow. The statements hold for every finite admissible parameter pair.

## Verification

Run `python3 verify.py` using Python 3 standard library only. It enumerates all perfect matchings on \(2n\) points for \(3\le n\le6\) and compares exact rational covariances for every \(3\le r\le n\), including all boundary cases in that finite range. The verifier passes 54 exact identity assertions (10 parameter combinations), independently recomputing the statistics from individual matchings. This finite check supports, but does not replace, the analytic all-size proof above.

## Relationship to prior work

Chen, Deng, Du, Stanley and Yan define \(r\)-crossings and \(r\)-nestings, but their joint symmetry statements are for the **maximum present order** of crossing and nesting, not the covariance of **numbers of subconfigurations** with \(C_2\). Kasraoui and Zeng study the counts of crossings and nestings of *two* edges and their joint generating functions; their statements do not give the \(r\ge3\) covariance formulas. Acan studies the intersection graph of a uniform chord diagram and related clique/independence questions; its first-moment and asymptotic analyses do not imply the exact cross-statistic covariance contrast stated here. The \(r=2\) instance is not asserted to be new. The displayed formulas for every \(r\ge3\), particularly one-arc-overlap cancellation for nested configurations, are the claimed contribution.

## Limitations

The theorem concerns the uniform, unweighted perfect-matching model and the two indicated higher-order patterns; it does not give a joint distribution, concentration estimate or analogous statement for arbitrary partial matchings. A complete historical priority review may uncover an earlier implication through general subconfiguration-count identities. The proof and exact checks are not independent external certification.

## References

1. W. Y. C. Chen, E. Y. P. Deng, R. R. X. Du, R. P. Stanley, C. H. Yan, *Crossings and Nestings of Matchings and Partitions*, 2005, https://arxiv.org/abs/math/0501230 (first public version 2005-01-14).
2. A. Kasraoui, J. Zeng, *Distribution of crossings, nestings and alignments of two edges in matchings and partitions*, 2006, https://arxiv.org/abs/math/0601081 (first public version 2006-01-04).
3. H. Acan, *On a uniformly random chord diagram and its intersection graph*, 2015, https://arxiv.org/abs/1501.01489 (first public version 2015-01-07).
