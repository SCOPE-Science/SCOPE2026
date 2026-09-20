# Review: sharp zero-forcing metric-dimension gap for trees

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof separates into two independently checkable inequalities.

First, for a non-path tree \(T\) with \(\ell\) leaves and \(e\) exterior major
vertices, the standard identity \(\dim(T)=\ell-e\) and the tree identity
\(Z(T)=P(T)\) reduce the problem to bounding the minimum path cover. Let \(H\) be
the forest induced by the major vertices and let \(F\) be a maximum matching of
\(H\). Deleting every edge of \(F\), together with
\(d(v)-2-\varepsilon_v\) additional non-\(F\) edges at each major vertex \(v\),
leaves maximum degree at most two. The number of distinct deleted edges is at
most
\[
(\ell-2)-\nu(H),
\]
using \(\sum_{d(v)\ge3}(d(v)-2)=\ell-2\). This yields
\[
P(T)\le\ell-1-\nu(H)
\]
and hence
\[
Z(T)-\dim(T)\le e-1-\nu(H).
\]

Second, because \(H\) is bipartite, a minimum vertex cover has size \(\nu(H)\).
Removing that cover from the exterior major vertices leaves an independent set
\(S\) of at least \(e-\nu(H)\) degree-at-least-three vertices. Their incident
edge sets are disjoint, so
\[
n-1\ge3|S|\ge3(e-\nu(H)).
\]
This gives the claimed order bound.

The sharpness construction has \(m\) independent degree-\(3\) major vertices,
\(m+2\) leaves, metric dimension \(2\), and path-cover number \(m+1\). The lower
bound on its path-cover number follows because every degree-\(3\) major vertex
must lose an incident edge in any spanning path forest, while no deleted edge
can serve two major vertices. A matching explicit deletion set attains the
bound.

The equality analysis for \(n=3m+1\) was checked step by step. Equality forces
an independent set of \(m\) exterior degree-\(3\) major vertices incident with
every edge. Any additional exterior or interior major vertex contradicts either
terminality or the absence of major-major edges. Suppression of degree-\(2\)
vertices then gives a path, forcing the stated unique tree.

A direct enumeration of all nonisomorphic trees through order \(17\) agrees with
the formula and with uniqueness in the tested orders \(7,10,13,16\).

## Originality

**PASS, to the best of our knowledge.**

The full text of Eroh--Kang--Yi was inspected. It proves
\(\dim(T)\le Z(T)\), records the formulas
\(\dim(T)=\ell(T)-e(T)\) and \(Z(T)=P(T)\), characterizes equality, and exhibits
families with an unbounded positive gap. No maximum of
\(Z(T)-\dim(T)\) among trees of a fixed order, no
\(\lfloor(n-4)/3\rfloor\) formula, and no matching refinement of the form
\(e-1-\nu(H)\) was found there.

The full arXiv preprint of Davila--Henning was inspected because it directly
studies matching and path covers of trees. Its main results concern total
forcing, matching, trimming, and path-cover structure; the present
zero-forcing/metric-dimension order extremum was not found.

Searches also covered later sparse-graph metric-dimension/zero-forcing work,
recent distance- and path-covering work, exact formula searches, and synonymous
phrases involving path cover, metric dimension, exterior major vertices, and
tree order. No equivalent theorem was located.

Residual originality risk remains from unindexed sources or a result stated
solely in specialized path-partition terminology. No concrete accessible source
found during the search gives substantial evidence that the claimed theorem is
already covered.

## Value

**PASS.**

The result turns the previously known qualitative fact that the tree gap can be
arbitrarily large into an exact fixed-order extremal theorem. It also gives a
stronger structural inequality involving a matching in the major-vertex forest,
constructs sharp examples for every order, and uniquely identifies the
extremizer for the infinite congruence class \(n\equiv1\pmod3\).

## Limitations

- Originality is asserted only to the best of our knowledge.
- Unindexed or differently phrased path-partition results remain a residual risk.
- The theorem concerns trees, ordinary zero forcing, and ordinary metric dimension.
- The uniqueness characterization is proved only for \(n\equiv1\pmod3\), \(n\ge7\);
  multiple extremizers occur in the other congruence classes.
