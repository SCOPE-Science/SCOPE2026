# Two exact sign reversals between isolated edge components and maximal edges in binomial random graphs

## Finding

Let \(G\sim G(n,p)\) be the binomial random graph on \(n\) labelled vertices with independent edge probability \(0<p<1\). Let \(I_n\) be the number of connected components on exactly two vertices, and let \(M_n\) be the number of edges lying in no triangle. Equivalently, \(M_n\) counts maximal cliques of order two, whereas every edge counted by \(I_n\) is counted by \(M_n\).

For every integer \(n\ge3\), put \(b_n=\binom n2\), \(a_n=\binom{n-2}2\), and \(q=1-p^2\). Then

\[
\operatorname{Cov}(I_n,M_n)
=b_np(1-p)^{2n-4}\left[1-pq^{n-4}\bigl(b_nq^2-a_n\bigr)\right].
\]

The factor \(q^{n-4}\) is interpreted ordinarily for \(n=3\), where the bracket simplifies to \(1-3p(1-p^2)\). For **every integer \(n\ge3\)** there are exactly two distinct critical probabilities \(0<p_{n,-}<p_{n,+}<1\) satisfying

\[
p(1-p^2)^{n-4}\left[\binom n2(1-p^2)^2-\binom{n-2}2\right]=1.
\]

The covariance is strictly positive for \(0<p<p_{n,-}\), strictly negative for \(p_{n,-}<p<p_{n,+}\), and strictly positive for \(p_{n,+}<p<1\). At the two critical probabilities it is zero. The two-vertex boundary has \(I_2=M_2\sim\operatorname{Bernoulli}(p)\), hence positive covariance \(p(1-p)\) and no transition.

The two critical probabilities have **different asymptotic scales**:

\[
np_{n,-}\longrightarrow\tfrac12,
\qquad
\sqrt n\,p_{n,+}\longrightarrow\sqrt2
\qquad(n\to\infty).
\]

Furthermore, for fixed \(c>0\),

\[
\lim_{n\to\infty}\frac1n\operatorname{Cov}
\bigl(I_n,M_n\bigr)\Big|_{p=c/n}
=\frac c2e^{-2c}(1-2c).
\]

## Assumptions and scope

All graphs are finite, simple, undirected, and have labelled vertices. Distinct potential edges appear independently with common probability \(p\); no conditioning on the number of edges or components occurs. An *isolated edge component* is an edge whose two endpoints have graph degree exactly one. A *maximal edge* is an existing edge not contained in any triangle, regardless of its endpoints' other neighbors. The covariance is with respect to the full \(G(n,p)\) measure. The exact formula and complete sign classification hold for all integers \(n\ge3\) and every real \(0<p<1\); the asymptotic claims hold for increasing integers \(n\) with the indicated scaling. The two critical roots need not be given by radicals.

## Proof

**1. Exact mixed moments.** Index the \(b_n=\binom n2\) candidate unordered vertex pairs by \(e\). Let \(A_e\) indicate that \(e\) forms an isolated two-vertex component, and let \(B_e\) indicate that \(e\) is present and belongs to no triangle. Then \(I_n=\sum_e A_e\), \(M_n=\sum_e B_e\), and

\[
\mathbb E A_e=p(1-p)^{2n-4},\qquad
\mathbb E B_e=p(1-p^2)^{n-2}.
\]

The second identity requires the edge to be present, and then excludes a common neighbor at each of the \(n-2\) other vertices; these exclusion events involve disjoint pairs of edges.

Fix \(e\) and classify the pair \(f\) in \(\mathbb E[A_eB_f]\). If \(f=e\), then \(A_e\) implies \(B_e\), so the joint probability is \(\mathbb E A_e\). If \(f\ne e\) and shares one endpoint with \(e\), the joint probability is zero, because isolation of \(e\) forbids \(f\). If \(f\) has disjoint endpoints from \(e\), then isolation of \(e\) already forbids all four cross edges joining their endpoints. Conditional on \(A_e\), the probability that \(f\) is maximal is therefore \(p(1-p^2)^{n-4}\). There are \(a_n=\binom{n-2}2\) such pairs, and \(2(n-2)\) pairs sharing exactly one endpoint. Thus

\[
\mathbb E[I_nM_n]=b_np(1-p)^{2n-4}
\left[1+a_np(1-p^2)^{n-4}\right].
\]

Subtracting the product of the two marginal means yields the stated covariance identity. This identity also holds for \(n=3\): there are no disjoint candidate edges, and the term containing \(a_n\) is zero. The simplification for \(n=3\) is performed before using any endpoint limit at \(p=1\).

**2. Exactly two crossings.** Because the prefactor \(b_np(1-p)^{2n-4}\) is strictly positive on the open probability interval, the covariance sign equals the sign of \(1-F_n(p)\), where

\[
F_n(p)=p(1-p^2)^{n-4}\left[b_n(1-p^2)^2-a_n\right].
\]

For \(n=3\), this becomes \(F_3(p)=3p(1-p^2)\), which is zero at both endpoints, has a unique maximum at \(p=1/\sqrt3\), and satisfies \(F_3(1/2)=9/8>1\). Hence exactly two crossings occur.

For \(n\ge4\), set \(p_0=\sqrt{1-\sqrt{a_n/b_n}}\), which lies in \((0,1]\). The function \(F_n\) is strictly positive on \((0,p_0)\), vanishes at its two endpoints, and is nonpositive on \([p_0,1)\). Put \(x=p^2\). On \(0<x<p_0^2\), logarithmic differentiation gives

\[
\frac{d}{dx}\log F_n(\sqrt x)
=\frac1{2x}-\frac{n-4}{1-x}
-\frac{2b_n(1-x)}{b_n(1-x)^2-a_n}.
\]

Every term on the right is nonincreasing in \(x\), and the first and last are strictly decreasing: indeed the derivative in \(x\) of the last positive quotient inside its negative sign is strictly positive because \(b_n(1-x)^2>a_n\). The logarithmic derivative therefore decreases strictly from \(+\infty\) to \(-\infty\). Thus \(F_n\) has exactly one positive-domain maximum.

It remains to show that maximum exceeds one. For \(n=4\), \(F_4(1/4)=547/512>1\). For every \(n\ge5\), Bernoulli's inequality and \((n-4)/n^2\le1/16\) yield

\[
(1-n^{-2})^{n-4}\ge1-\frac{n-4}{n^2}\ge\frac{15}{16}.
\]

Direct algebra gives

\[
\frac1n\bigl[b_n(1-n^{-2})^2-a_n\bigr]
=2-\frac4n+\frac1{n^2}+\frac{n-1}{2n^4}
>2-\frac4n\ge\frac65.
\]

Consequently \(F_n(1/n)> (15/16)(6/5)=9/8>1\). For \(n\ge4\), both sides of this strict witness belong to the positive domain, because its bracket is positive. Continuity and strict unimodality give exactly two roots of \(F_n(p)=1\) in \((0,p_0)\), with no others on \((0,1)\). This proves the full sign classification, including nonvanishing covariance away from the roots.

**3. Separated scaling limits.** For fixed \(c>0\), an elementary expansion shows

\[
F_n(c/n)\longrightarrow 2c.
\]

Because \(F_n(1/n)>1\) for \(n\ge4\), the smaller root lies below \(1/n\) and the larger root above it. Bracketing the smaller root with \(c/n\) for any \(c<1/2\) and any \(c>1/2\) proves \(np_{n,-}\to1/2\).

For fixed \(0<t<\sqrt2\), direct expansion gives

\[
\frac{F_n(t/\sqrt n)}{\sqrt n}
\longrightarrow t(2-t^2)e^{-t^2}>0.
\]

Thus \(F_n(t/\sqrt n)>1\) eventually, forcing \(p_{n,+}>t/\sqrt n\) by uniqueness of the larger root. On the other hand, \(p_{n,+}<p_0\), and

\[
\sqrt n\,p_0
=\sqrt{n\left(1-\sqrt{\frac{(n-2)(n-3)}{n(n-1)}}\right)}
\longrightarrow\sqrt2.
\]

Letting \(t\uparrow\sqrt2\) establishes \(\sqrt n\,p_{n,+}\to\sqrt2\). Finally, substituting \(p=c/n\) into the exact covariance formula, using \(b_n/n^2\to1/2\), \((1-c/n)^{2n-4}\to e^{-2c}\), and \(F_n(c/n)\to2c\), proves the stated sparse-regime covariance density.

## Verification

The standalone `verify.py` reconstructs all labelled graphs on \(3\), \(4\), \(5\), and \(6\) vertices and evaluates their exact rational probabilities for five distinct rational choices of \(p\). It independently computes the two statistics from graph adjacency, verifies both marginals and the exact mixed covariance, then tests the strict finite-size witnesses and their rational inequalities at additional integer orders. It uses only the Python standard library; run `python verify.py`. In the completed package it passed 454 deterministic assertions. Finite enumeration is a diagnostic check; the proofs above establish the full infinite range.

## Relationship to prior work

The 1990 paper *Small cliques in random graphs* by Barbour, Janson, Karoński, and Ruciński studies counts of maximal cliques in binomial random graphs. Its publisher abstract and bibliographic details were accessible, but its full primary text was not; the covariance classification here cannot be asserted to be absent from its full contents. Palmer's older book *Graphical Evolution* includes an exercise on the second moment of edges belonging to no triangle, as documented in a dated public mathematical discussion. That discussion establishes the marginal expectation of the maximal-edge statistic but does not compute its covariance with isolated edge components. The later full-text article *Maximal cliques in scale-free random graphs* investigates maximal cliques in a different random-graph model. The isolated component statistic and maximal-edge statistic have different structural meanings; known marginal results alone do not imply the mixed covariance or the two-root theorem.

Comparisons of published mathematical research records for isolated components, maximal edges, triangle-free edges, and joint covariance found no directly covering statement. This is a best-knowledge originality assessment rather than a proof of historical uniqueness. The inaccessible 1990 primary paper and older book remain material historical-priority risks.

## Limitations

This result concerns only independent-edge binomial random graphs. It says nothing about fixed-edge-count ensembles, dependent-edge models, or covariance of nontrivial higher clique orders. The theorem does not provide elementary closed forms for the two finite-size root locations. It establishes a limiting covariance density only for the sparse scale \(p=c/n\); no nondegenerate covariance normalization is claimed at the larger transition scale. Exact historical priority remains contingent on examination of inaccessible earlier full text. Independent scientific validation has not been performed.

## References

1. A. D. Barbour, S. Janson, M. Karoński, A. Ruciński, *Small cliques in random graphs*, Random Structures & Algorithms 1 (1990), 403–434, DOI: 10.1002/rsa.3240010403. Publisher dates the release only to Winter 1990.
2. E. M. Palmer, *Graphical Evolution: An Introduction to the Theory of Random Graphs*, Wiley, 1985, p. 27, second-moment exercise on edges not contained in triangles. Exact initial public release day not verified.
3. Mathematics Stack Exchange, *Square of the expectation of number of edges not in a triangle in random graph*, question and answer dated 2013-08-27, https://math.stackexchange.com/questions/477180/square-of-the-expectation-of-number-of-edges-not-in-a-triangle-in-random-graph. This is the earliest relevant source with verified precise day in the accessible material.
4. T. Bläsius, P. Katzmann, C. Stegehuis, *Maximal cliques in scale-free random graphs*, arXiv:2309.02990 (2023); Network Science (2024). Relevant full-text comparison for a different random-graph model.
