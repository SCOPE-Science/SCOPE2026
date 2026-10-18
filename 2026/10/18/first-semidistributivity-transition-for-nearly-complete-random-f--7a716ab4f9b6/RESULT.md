# First semidistributivity transition for nearly complete random formal contexts

## Finding

Fix \(\alpha>0\). For each positive integer \(n\), let \(\mathcal K_n=(O_n,A_n,I_n)\) be a random formal context with \(|O_n|=n\), \(|A_n|=m_n=\lfloor\alpha n\rfloor\), and independent incidence entries, each present with probability \(1-q_n\). Write \(\mathcal L_n\) for its finite formal-concept lattice and \(S_n\) for the event that \(\mathcal L_n\) is both join- and meet-semidistributive.

**Theorem (first sparse semidistributivity window).** The scale of the first loss of semidistributivity is \(q_n\asymp n^{-7/6}\). Precisely:

1. If \(q_n=o(n^{-7/6})\), then \(\Pr(S_n)\to1\).
2. If \(q_n=t n^{-7/6}\) with fixed \(t>0\), then
   \[
   \Pr(S_n)=\exp\!\left[-\frac{\alpha^3+\alpha^4}{2}t^6\right]+O_{\alpha,t}(n^{-1/6}).
   \]
   More generally, if \(n^{7/6}q_n\to t\in(0,\infty)\), the corresponding probability has the same limit, without an asserted rate. In the exact window, the number of connected components isomorphic to the seven-vertex path in the bipartite graph of *missing* incidences converges in total variation to \(\operatorname{Poisson}((\alpha^3+\alpha^4)t^6/2)\).
3. If \(n^{7/6}q_n\to\infty\) while \(nq_n\to0\), then \(\Pr(S_n)\to0\).

The finite obstruction underlying the theorem is exact: **among all bipartite trees with at most seven vertices, only the seven-vertex path has a nonsemidistributive concept lattice of its bipartite complement**. Here the original incidence relation contains every object–attribute pair except the edges of the tree. This is a first-sparse-window theorem, not a claim about every larger missing-incidence density.

## Assumptions and scope

For a context \((O,A,I)\), define derivations for \(X\subseteq O\) and \(Y\subseteq A\) by
\[
X'=\{a\in A:\forall o\in X,\ (o,a)\in I\},\qquad
Y'=\{o\in O:\forall a\in Y,\ (o,a)\in I\}.
\]
Its concepts are pairs \((X,Y)\) with \(X'=Y\) and \(Y'=X\). Ordered by extent inclusion, its concept lattice has meet \(X\wedge Y=X\cap Y\) and join \(X\vee Y=(X\cup Y)''\), treating concepts as their closed extents.

A lattice is join-semidistributive if \(x\vee y=x\vee z\) implies \(x\vee(y\wedge z)=x\vee y\). It is meet-semidistributive if \(x\wedge y=x\wedge z\) implies \(x\wedge(y\vee z)=x\wedge y\). Semidistributivity means both properties. The bipartite missing-incidence graph \(H\) has parts \(O,A\), with an edge exactly when \((o,a)\notin I\). Its isolated vertices are retained.

All asymptotics have fixed \(\alpha\); constants in the stated rate may also depend on fixed \(t\). No assertion is made for \(nq_n\) bounded away from zero.

## Proof

**1. Complement-graph decomposition.** A concept \((X,Y)\) is a maximal rectangle entirely contained in the incidence relation. Equivalently, \(X\cup Y\) is a maximal independent vertex set in \(H\). If \(H\) has vertex-disjoint components \(H_1,\ldots,H_r\), the derivation \(X'\) and double derivation \(X''\) act componentwise: outside the component of an object, all incidence pairs are present. Therefore the concept lattice of the full context is the direct product of the concept lattices of the complementary component contexts. Isolated components contribute one-element factors. The two semidistributive quasi-identities hold in a direct product exactly when they hold in every factor.

**2. Exact seven-vertex tree certificate.** The accompanying standard-library program `verify_semidistributivity.py` enumerates each labelled tree on \(v\) vertices for \(1\le v\le7\) via all Prüfer sequences. The Prüfer bijection gives exactly \(v^{v-2}\) labelled trees for \(v\ge2\). It two-colors each tree, makes those edges the absent incidences, and independently constructs all double-derivation-fixed object extents from the full Boolean domain. It then evaluates both semidistributive quasi-identities for **every** ordered triple of closed extents. The counts of labelled trees failing at orders one through seven are respectively \(0,0,0,0,0,0,2520\); the total trees at order seven are \(16807\), and the \(2520=7!/2\) failures are exactly the labelled seven-vertex paths. This is an exhaustive finite certificate, not a sample or an appeal to unverified enumeration.

For a direct witness, take four objects \(o_0,o_1,o_2,o_3\) and three attributes \(a_0,a_1,a_2\) with missing pairs
\[
(o_0,a_0),\ (o_1,a_0),\ (o_1,a_1),\ (o_2,a_1),\ (o_2,a_2),\ (o_3,a_2).
\]
These form the seven-vertex path. Its closed object extents are precisely
\[
\varnothing,\ \{o_0\},\ \{o_3\},\ \{o_0,o_1\},\ \{o_0,o_3\},\ \{o_2,o_3\},\ O.
\]
Put \(x=\{o_0,o_3\}\), \(y=\{o_0,o_1\}\), \(z=\{o_2,o_3\}\). Then \(x\vee y=x\vee z=O\), but \(y\wedge z=\varnothing\) and \(x\vee(y\wedge z)=x\ne O\). Thus this component fails join-semidistributivity. Every alternative tree with at most seven vertices passes both identities by the exhaustive certificate.

**3. Absence of larger components and cycles at criticality.** Set \(q_n=t n^{-7/6}\). A connected missing-incidence component of order at least eight contains a tree on eight vertices; the expected number of such embedded trees is at most \(C_\alpha n^8q_n^7=O_{\alpha,t}(n^{-1/6})\). The expected number of cycles of length at least four is bounded by a constant times \(\sum_{\ell\ge4}(C_\alpha nq_n)^\ell=O_{\alpha,t}(n^{-2/3})\). Therefore, except with probability \(O_{\alpha,t}(n^{-1/6})\), every component is a tree of order at most seven. By Step 2, on this event semidistributivity holds precisely when there is no seven-vertex path component.

**4. Critical Poisson approximation.** Let \(Z_n\) count unordered copies of the seven-vertex path as an edge subgraph of \(H\), not initially requiring them to be isolated components. Its exact expectation is
\[
\mu_n=\frac{q_n^6}{2}\left[(n)_4(m_n)_3+(n)_3(m_n)_4\right]
\longrightarrow\lambda=\frac{\alpha^3+\alpha^4}{2}t^6,
\]
where \((r)_s=r(r-1)\cdots(r-s+1)\). The factor \(1/2\) divides out reversal of the path. The Bernoulli indicator of each particular path edge-set is independent of indicators using disjoint edge-sets, even when their vertex sets intersect. Two distinct paths sharing \(s\ge1\) missing edges have at least \(s+1\) shared vertices and necessarily \(s\le5\). In the dependency-graph Poisson bound, their joint-probability contribution divided by the square of the bounded mean is at most a constant multiple of
\[
\sum_{s=1}^5n^{-(s+1)}q_n^{-s}
=O_{\alpha,t}(n^{-1/6}).
\]
The product-probability contribution is smaller. Hence the total-variation distance from \(\operatorname{Poisson}(\mu_n)\) is \(O_{\alpha,t}(n^{-1/6})\). A given path has at most \(C_\alpha n\) potential additional incident edges, so the expected number of non-isolated copies is at most \(C_\alpha nq_n\mu_n=O_{\alpha,t}(n^{-1/6})\). We may consequently replace path copies by path **components**, with the same asymptotic error. Combining Steps 2–4 proves the exact-window formula. The unrestricted finite-positive-\(t\) convergence follows by the same estimates and convergence of the mean.

**5. Below and above the first window.** If \(q_n=o(n^{-7/6})\), then \(\mathbb E Z_n=O_\alpha(n^7q_n^6)=o(1)\); the preceding tree-and-cycle bounds with seven in place of eight ensure no larger component with probability tending to one. Therefore the lattice is semidistributive with probability tending to one.

If instead \(n^{7/6}q_n\to\infty\) and \(nq_n\to0\), then \(\mu_n\to\infty\). The same overlap counting yields
\[
\frac{\operatorname{Var}(Z_n)}{\mu_n^2}
\le \frac1{\mu_n}+C_\alpha\sum_{s=1}^{5}\frac{1}{n^{s+1}q_n^s}\longrightarrow0.
\]
Indeed \(n^{s+1}q_n^s=n^{1-s/6}(n^{7/6}q_n)^s\to\infty\) for each \(s\le5\). Thus \(Z_n/\mu_n\to1\) in probability. The expected fraction of path copies with additional incident edges is \(O_\alpha(nq_n)=o(1)\), so with probability tending to one at least one seven-vertex path is an isolated component. Its factor violates semidistributivity, proving the supercritical assertion.

## Verification

Run the embedded pure-Python verifier using a standard Python 3 interpreter:

```text
python3 verify_semidistributivity.py
```

Expected output:

```text
TREE_CENSUS [(1, 1, 0, 0), (2, 1, 0, 1), (3, 3, 0, 3), (4, 16, 0, 12), (5, 125, 0, 60), (6, 1296, 0, 360), (7, 16807, 2520, 2520)]
P7_EXTENTS [0, 1, 3, 8, 9, 12, 15]
MIS_FCA_EQUIVALENCE 576
VERIFY_OK
```

The certificate visits \(18249\) labelled trees. An independent finite cross-check visits all \(576\) missing-edge patterns on the indicated two-by-three and three-by-three domains and verifies that the closed extents coincide with the object parts of maximal independent sets. These finite calculations certify the finite lemma and representation checks; the all-\(n\) probability statements require the analytic estimates of Steps 3–5.

## Relationship to prior work

Felde, Hanika, and Stumme (2020) study coin-toss and other null models for formal contexts, supplying a natural independent-entry setting. Sakurai (2021) studies the expected number of concepts under a related random-context model, not semidistributive lattice properties. Craig, Haviar, and São João (2022) characterize semidistributive lattices abstractly using dual digraphs and minimal closure systems; their general representation is not the present forbidden-tree certificate or random-context limit. Defant and Williams (2021/2023) develop broader semidistrim lattice structures, not the path-component transition in random formal contexts.

Both classical finite-tree enumeration and Poisson approximation for rare fixed subgraphs are standard tools and are not claimed as independent contributions. The specific first semidistributivity obstruction in the missing-incidence component setting, together with the sharp exponent and limiting probability, is the assessed contribution. A known general forbidden-context theorem could potentially subsume parts of this combination, and no exhaustive publication-priority certification is claimed.

## Limitations

Only binary contexts with independent, identically distributed incidence variables and fixed positive rectangular aspect ratio are treated. The zero-probability statement is confined to the first sparse regime \(nq_n\to0\), not arbitrary denser contexts. The quantitative \(O(n^{-1/6})\) rate is asserted when \(q_n=t n^{-7/6}\) exactly. Numerical finite checks do not independently certify the probabilistic asymptotics. Semidistributivity is strictly weaker than distributivity; a distributivity transition alone does not imply this theorem. Priority beyond the inspected literature remains uncertain.

## References

1. M. Felde, T. Hanika, and G. Stumme, *Null Models for Formal Contexts*, Information 11(3), 135 (published 2020-02-28). DOI: 10.3390/info11030135. https://doi.org/10.3390/info11030135
2. T. Sakurai, *On formal concepts of random formal contexts*, arXiv:2101.11023v1 (first posted 2021-01-26). https://arxiv.org/abs/2101.11023
3. A. Craig, M. Haviar, and J. São João, *Dual digraphs of finite semidistributive lattices*, CUBO 24(3), 369–392 (2022). DOI: 10.56754/0719-0646.2403.0369. https://www.scielo.cl/pdf/cubo/v24n3/0719-0646-cubo-24-03-369.pdf
4. C. Defant and N. Williams, *Semidistrim Lattices*, arXiv:2111.08122 (first posted 2021-11-15); Forum of Mathematics, Sigma 11, e50 (2023). https://arxiv.org/abs/2111.08122
