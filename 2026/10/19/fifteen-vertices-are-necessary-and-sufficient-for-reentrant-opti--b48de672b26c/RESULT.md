# Fifteen vertices are necessary and sufficient for reentrant optimal information seeding on trees

## Finding

**Theorem (sharp minimum for strict reentry).** Let \(T\) be a finite simple unweighted tree. Every edge independently carries a message with common success probability \(p\in(0,1)\). For a selected origin \(v\), a vertex receives the message exactly when every edge of the unique path from \(v\) to it succeeds. Write \(F_v(p)\) for the expected number of receiving vertices, including the origin. Call \(v\) *strictly reentrant* when it uniquely maximizes \(F_w(p)\) over all origins \(w\) on two disjoint open parameter intervals but fails to maximize on a nonempty open interval separating them.

No tree of order at most \(14\) has a strictly reentrant origin. There exists a tree of order \(15\) with a strictly reentrant origin and exactly two changes in its unique optimal origin as \(p\) increases through \((0,1)\). Consequently \(15\) is the sharp minimum order. This claim concerns global optimum reentry, *not* merely a change of some pairwise vertex ranking.

One witness uses vertices \(0,1,\ldots,14\) and undirected edges

\[
\{(0,11),(0,1),(1,2),(1,9),(1,10),(2,3),(2,7),
(3,4),(3,5),(3,6),(7,8),(11,12),(12,13),(13,14)\}.
\]

The only globally competitive origins are \(1\) and \(2\), with

\[
\begin{aligned}
F_1(p)&=1+4p+3p^2+5p^3+p^4+p^5,\\
F_2(p)&=1+3p+7p^2+p^3+p^4+p^5+p^6,\\
F_1(p)-F_2(p)&=p(1-p)\bigl(p^4+p^3+p^2-3p+1\bigr).
\end{aligned}
\]

Let \(a<b\) be the two roots in \((0,1)\) of \(q(p)=p^4+p^3+p^2-3p+1\); numerically \(a\approx0.436911127214511\) and \(b\approx0.719739963708202\). Origin \(1\) uniquely maximizes spread on \((0,a)\cup(b,1)\), while origin \(2\) uniquely maximizes on \((a,b)\). At \(a\) and \(b\), origins \(1,2\) tie strictly above all other origins.

## Assumptions and scope

The tree is connected, undirected, finite, unweighted and has no cycles. Each edge's transmission success is an independent Bernoulli event with the same parameter \(p\). Transmission may proceed along all successful edges; there are no deadlines, competing sources, node failures, behavioral responses or repeated retries. The objective is the **expected** total number receiving from a *single* origin, not the probability of reaching a prescribed target or maximizing a realization. The originating vertex counts as reached; omitting this universal additive constant does not affect optimal origins.

For vertices \(v,w\) at distance \(d_T(v,w)\), the unique path succeeds with probability \(p^{d_T(v,w)}\). By linearity of expectation,

\[
F_v(p)=\sum_{w\in V(T)}p^{d_T(v,w)}.
\]

Thus maximizing expected reach coincides with maximizing the established decay-centrality index, up to the constant \(1\). The theorem's new object is the *disconnectedness of a vertex's global-maximum parameter set* and its sharp smallest tree order.

## Proof

**1. Exact distance polynomials.** For an \(n\)-vertex tree let \(c_{v,j}=|\{w:d_T(v,w)=j\}|\) for \(j\in\{0,\ldots,n-1\}\), with \(c_{v,0}=1\) and \(\sum_j c_{v,j}=n\). Then \(F_v(p)=\sum_jc_{v,j}p^j\). For any ordered vertices \(u,v\), the difference vanishes at both endpoints \(p=0,1\). It therefore has a unique integral-coefficient quotient

\[
F_u(p)-F_v(p)=p(1-p)q_{uv}(p).
\]

Its coefficients can be computed by successive cumulative sums of the coefficients of \(F_u-F_v\); `quotient` in `verify_reentry.py` implements this exact identity and checks the final coefficient.

**2. Exact dominance and the one-crossing reduction.** Suppose \(q(p)=\sum_{j=0}^d a_jp^j\). Substitute \(p=z/(1+z)\), which bijects \((0,\infty)\) with \((0,1)\), and form

\[
Q(z)=(1+z)^d q\bigl(z/(1+z)\bigr)
=\sum_{k=0}^d\left(\sum_{j=0}^{k}a_j\binom{d-j}{k-j}\right)z^k.
\]

Since \(p(1-p)>0\) and \((1+z)^d>0\), the signs of \(F_u-F_v\) and \(Q(z)\) agree. Descartes' rule of signs implies that a nonzero coefficient list for \(Q\) with no sign variations has fixed strict sign for all \(p\in(0,1)\); with at most one sign variation, its sign can change at most once. A vertex dominated by a fixed-sign comparison can never be globally optimal. If every comparison among the remaining vertices has at most one sign change, each inequality \(F_v(p)\ge F_w(p)\) restricts \(p\) to an interval (possibly empty), and the intersection defining the global optimality region of \(v\) is an interval. This precludes strict reentry.

**3. Complete lower-bound census.** The accompanying exact checker enumerates every nonisomorphic unlabelled tree with \(2\le n\le14\). It verifies the standard tree-shape counts

\[
(1,1,2,3,6,11,23,47,106,235,551,1301,3159)
\]

for orders \(2,\ldots,14\). It constructs the full integer distance profile of each vertex by breadth-first search, removes only vertices certified strictly dominated for every \(p\in(0,1)\), and applies step 2. All remaining comparisons have at most one sign variation except in precisely \(6\) tree shapes of order \(13\) and \(17\) shapes of order \(14\) (\(6\) and \(18\) exceptional surviving pairs respectively).

For each of these \(23\) exceptional shapes, every surviving pair difference is factored over \(\mathbb Q\), and **all** its distinct roots in \((0,1)\) are isolated into disjoint rational intervals using exact Sturm root isolation. Across these shapes the checker processes \(60\) such root cells. It evaluates all candidate polynomials at exact rational points in every gap between successive isolated roots and verifies that each vertex's global-optimality membership occupies contiguous gaps. Because no candidate pair difference vanishes within a gap, these are complete interval descriptions, not numerical mesh samples. A single isolated root can change the winner only across the two adjacent gaps, so it cannot conceal a separate open region of global optimality. This excludes strict reentry on all these shapes. The one-vertex tree is trivial.

The census is finite and exhaustive subject to the correctness of the openly supplied nonisomorphic-tree generator; the checked counts agree with the standard unlabelled-tree sequence, but that agreement alone is not treated as a proof of generator correctness. The algorithm and exact arithmetic certificate are provided for replay.

**4. The explicit fifteen-vertex witness.** Breadth-first profiles give

\[
\begin{aligned}
(c_{1,0},\ldots,c_{1,6})&=(1,4,3,5,1,1,0),\\
(c_{2,0},\ldots,c_{2,6})&=(1,3,7,1,1,1,1).
\end{aligned}
\]

This yields the displayed factorization. For every other vertex \(v\notin\{1,2\}\), compute \(q_{1v}\) and the transformed polynomial \(Q_{1v}\) in step 2. All coefficients of \(Q_{1v}\) are nonnegative and at least one is positive; the exact lists are reconstructed and asserted in the supplied checker. Hence \(F_1(p)>F_v(p)\) for every \(p\in(0,1)\). There are therefore no competing optimizers besides \(1\) and \(2\).

Finally, \(q(0)=q(1)=1\), \(q(1/2)=-1/16\), and \(q''(p)=12p^2+6p+2>0\) throughout \((0,1)\). Strict convexity gives precisely two simple roots \(a<b\), with positive sign outside and negative inside. Together with global dominance of origin \(1\) over every other vertex, this establishes both winner intervals and both strict reversals.

## Verification

The complete reproducibility package contains `verify_reentry.py` and `requirements.txt`. Install the dependencies and run `python verify_reentry.py` using Python 3.10 or newer. All decisive arithmetic involving tree distance counts, polynomial coefficients, rational test points, factorizations, candidate dominance and root isolation is exact. The checker reports the thirteen tree-shape counts, the \(23\) exceptional tree shapes, \(60\) root cells, witness factorization, rational root brackets and global dominance inequalities. It does not rely on an unproved numerical extrapolation or randomized sampling.

## Relationship to prior work

Tsakas (2016) studies maximal decay centrality as attenuation changes, proves endpoint relationships to degree and closeness, and documents primarily one-threshold behavior in simulations. Coroničová Hurajová, Gago and Madaras (2018) show a seven-vertex tree where the top decays rankings exchange **once** and, more generally, construct trees with prescribed **pairwise** decay-crossing patterns. They also enumerate decay-*stable* trees up to order \(20\). Their construction and table do not themselves state that a formerly globally optimal origin can reenter, nor the sharp minimal order for *global reentry*. The distance-profile polynomial formula and basic dominance comparisons are acknowledged as prior knowledge, not new results.

Riveros, Salas and Skibski (2023) analyze which centralities can root trees and potential functions; this is a different property from the dependence of a global maximizer on the attenuation parameter. Rupnik Poklukar and Žerovnik (2025) study partial-order criteria for complete decay-ranking stability and counterexamples for products of paths, rather than disconnected global-optimum regions. Their 2026 paper concerns typical decay instability and the construction of decay-stable trees; its abstract was accessible but the complete article was not. The resulting residual overlap risk is discussed in the accompanying scientific review. These comparisons are statement-level and do not assert that failure to find a matching title establishes originality.

## Limitations

This is a smallest-order theorem specifically for **trees** and **strict global reentry** of the expected-reach objective. It is not a classification of arbitrary pairwise rank crossings, the number of switches in larger trees, or the minimum for general graphs with cycles. It assumes homogeneous independent edge success and one seed; empirical social networks, heterogeneous networks and finite-sample estimation are not covered. The lower bound uses exhaustive exact computation on finite tree classes, with no external or independent formal certification claimed. A plausible relevant 2026 article could not be reviewed in full; a stronger uninspected theorem could subsume the finding. Independent assessment is not yet performed.

## References

1. N. Tsakas, *On Decay Centrality*, Working Paper 04-2016, University of Cyprus, dated 19 April 2016, https://papers.econ.ucy.ac.cy/RePEc/papers/04-16.pdf .
2. J. Coroničová Hurajová, S. Gago and T. Madaras, *On Decay Centrality in Graphs*, Mathematica Scandinavica 123 (2018), 39–50, https://journals.msp.org/mscand/article/download/263/262/291 .
3. C. Riveros, J. Salas and O. Skibski, *How Do Centrality Measures Choose the Root of Trees?*, ICDT (2023), https://doi.org/10.4230/LIPIcs.ICDT.2023.12 .
4. D. Rupnik Poklukar and J. Žerovnik, *Generalized Closeness and Decay Stability of Some Graphs*, Mathematics 13 (2025), 939, https://doi.org/10.3390/math13060939 . Open preprint: https://www.preprints.org/manuscript/202502.2148 .
5. D. Rupnik Poklukar and J. Žerovnik, *Almost All Trees Are Decay-Unstable*, Mathematica Scandinavica 132 (2026), abstract accessible at https://journals.msp.org/mscand/article/view/2963 ; complete text not verified.
6. R. Otter, *The Number of Trees*, Annals of Mathematics 49 (1948), 583–599, https://doi.org/10.2307/1969046 .
