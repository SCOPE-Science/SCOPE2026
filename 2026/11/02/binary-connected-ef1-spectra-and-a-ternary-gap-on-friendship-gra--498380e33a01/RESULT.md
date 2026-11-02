# Binary connected EF1 spectra and a ternary gap on friendship graphs

## Finding

For every integer \(k\ge3\), let the friendship graph \(F_k\) consist of \(k\) edge-disjoint triangles with one common hub and no other shared vertices. For each integer \(1\le n\le2k+1\), consider all \(n\) agents having the **same additive valuation**, with each vertex valued in \(\{0,1\}\). There is a partition of the vertices into \(n\) nonempty connected bundles satisfying ordinary envy-freeness up to one vertex (EF1) for *every* such valuation **if and only if**
\[
 n=1\quad\text{or}\quad k\le n\le 2k+1.
\]
The positive assertion is constructive for all \(k\) and all binary valuations. The lower interval \(2\le n<k\) fails for a single explicit binary valuation.

The binary qualification is substantive. For every \(k\ge4\), a common additive valuation taking values in \(\{0,1,2\}\) can fail to admit a connected ordinary EF1 allocation into **exactly \(k\)** nonempty bundles. Thus the binary guarantee at the sharp threshold does not automatically extend to three-level identical valuations.

## Assumptions and scope

Write \(h\) for the hub and \(P_j=\{a_j,b_j\}\), \(1\le j\le k\), for the paired outer vertices, with exactly the edges \(ha_j,hb_j,a_jb_j\). A bundle is nonempty and induces a connected subgraph. An allocation partitions all \(2k+1\) vertices into \(n\) bundles. The common additive valuation is \(v(S)=\sum_{x\in S}w(x)\). Ordinary EF1 means that, for all bundles \(B,C\), there is an item \(x\in C\) such that \(v(B)\ge v(C\setminus\{x\})\); deleting \(x\) need **not** preserve connectivity. This is distinct from \(\mathrm{EF1}_{\mathrm{outer}}\).

For a nonnegative common additive valuation, EF1 is equivalent to
\[
 \min_B v(B)\ge \max_C\bigl(v(C)-\max_{x\in C}w(x)\bigr).
\]
For binary valuations it suffices to give bundles whose numbers of marked vertices differ by at most one.

## Proof

**1. Necessity for \(2\le n<k\).** Let the hub be marked, and mark exactly one vertex in each petal; all remaining vertices have weight zero. Every connected bundle omitting the hub lies entirely in one petal and has value at most one. Since at most \(n-1\) petals can be assigned to bundles omitting the hub, the bundle containing the hub receives value at least \(1+k-(n-1)=k-n+2\ge3\). Removing any single marked vertex leaves value at least two, which is strictly greater than the value of a nonhub bundle. Hence no connected EF1 allocation exists. A single bundle is always EF1.

**2. Constructing \(k\) connected binary-EF1 bundles.** Classify the petals according to their number \(0,1,2\) of marked vertices. Let \(r_0,r_1,r_2\) be their counts; write \(b=w(h)\in\{0,1\}\) and \(W=b+r_1+2r_2\). A whole petal is a connected pair; a split petal contributes its two singleton vertices. The following constructions all use exactly \(k\) connected bundles.

- **\(W<k\).** Set \(s=r_0-r_2-1\ge0\). Give the hub and all but \(s\) zero-mark petals to one bundle. Give each of the \(s\) remaining zero-mark petals its own bundle, give each one-mark petal its own bundle, and split every two-mark petal into singleton bundles. There are \(1+s+r_1+2r_2=k\) bundles and each has value zero or one.
- **\(k\le W<2k\), \(r_0=0\).** Put the hub with a one-mark petal when \(b=1\), which exists since \(W<2k\); when \(b=0\), use any petal. Keep all other petals intact. The hub bundle and every other bundle have value one or two.
- **\(k\le W<2k\), \(r_0\ge1\), \(b=1\).** Put the hub and all zero-mark petals together, keep one-mark petals intact, split \(r_0-1\) two-mark petals and keep the remaining two-mark petals intact. The condition \(W\ge k\) gives \(r_2\ge r_0-1\). There are \(k\) bundles, each valued one or two.
- **\(k\le W<2k\), \(r_0\ge1\), \(b=0\), \(r_1\ge1\).** Put the hub, all zero-mark petals, and one one-mark petal together. Keep the other one-mark petals intact, split \(r_0\) two-mark petals, and retain the rest intact. Since \(W\ge k\), \(r_2\ge r_0\). All \(k\) bundles have value one or two.
- **\(k\le W<2k\), \(r_0\ge1\), \(b=0\), \(r_1=0\).** Put the hub, all zero-mark petals, and one marked vertex from a two-mark petal together; give that petal's other vertex its own bundle. Split \(r_0-1\) of the remaining two-mark petals and retain the rest intact. Here \(r_2\ge r_0\). All \(k\) bundles have value one or two.
- **\(W=2k\).** If \(b=0\), every petal has two marks; attach any petal to the hub. If \(b=1\), exactly one petal has one mark and all others have two; attach that one-mark petal to the hub. In either case keep the other petals intact, obtaining \(k\) bundles valued two each.
- **\(W=2k+1\).** Every vertex is marked. Attach one petal to the hub and keep the remaining petals intact, yielding one bundle valued three and \(k-1\) bundles valued two; this is EF1.

**3. Refinement to every \(k<n\le2k+1\).** If \(W=2k+1\), first split the sole three-mark bundle into its hub singleton and two-vertex petal. Otherwise all initial bundles already have at most two marks. As long as a two-mark bundle exists, split it into two connected nonempty sets each with exactly one mark: a spanning tree of the bundle has an edge separating the two marked vertices, and deleting that edge provides the required partition. Once every bundle has at most one mark, any connected nonsingleton bundle can be split along a spanning-tree edge, preserving that upper bound. These operations preserve ordinary EF1 because the resulting mark counts remain in \(\{1,2\}\), or in \(\{0,1\}\), respectively. Each split increases the bundle count by one and can continue until every vertex is a singleton. This establishes all positive cases.

**4. Ternary failure at \(n=k\ge4\).** Assign the hub weight one, assign one vertex of each of the first \(k-1\) petals weight one and its partner zero, and assign both vertices of the last petal weight two. Total value is \(k+4\). Suppose a connected EF1 partition into \(k\) nonempty bundles exists, and let \(u,v\) be the two vertices of weight two.

If \(u,v\) lie in one bundle, that bundle has value at least four and retains at least two after deleting any one item. Every other bundle must consequently have value at least two. The total would be at least \(4+2(k-1)=2k+2>k+4\) for \(k\ge3\), a contradiction.

Otherwise \(u,v\) lie in distinct bundles. If the hub belongs to one of those bundles, the other weight-two vertex is a singleton (its only neighbors are the hub and its partner). Every remaining nonhub bundle is contained in one of the first \(k-1\) petals and has value at most one. There are only \(k-2\) such bundles, forcing at least one unit-weight vertex from those petals into the hub's bundle. The hub bundle then has value at least \(1+2+1=4\), and after deleting one item retains at least two, contradicting EF1 with a nonhub bundle of value at most one.

Finally, if neither weight-two vertex is in the hub's bundle, both are singleton bundles. Among the remaining \(k-2\) bundles, the \(k-3\) not containing the hub can capture at most \(k-3\) of the \(k-1\) unit-valued petal vertices. The hub bundle therefore has value at least \(1+2=3\), retains at least two after any one deletion, and violates EF1 against one of these \(k-3\) nonhub bundles, which exists for \(k\ge4\) and has value at most one. All cases contradict EF1.

## Verification

The standalone standard-library Python program `verify_friendship.py` constructs the binary allocation and refines it for every choice of \(0/1\) vertex weights for \(k=3,4,5\), testing all \(k\le n\le2k+1\). It checked \(18{,}048\) allocation instances. Separately, it enumerates every connected partition in the indicated small instances, confirming no EF1 allocation for binary lower-spectrum witnesses at \(k=3,4,5\) or the ternary threshold witnesses at \(k=4,5\). These finite tests independently corroborate, but do not replace, the all-parameter proof above. Execute: `python verify_friendship.py`.

## Relationship to prior work

Chen and Zwicker's 2024 study introduces graph-cutset obstructions and spectra of connected EF1 and \(\mathrm{EF1}_{\mathrm{outer}}\) guarantees, proving some general existence results at high agent counts and specific spectra of stars and other small graphs. Its hub-cutset method covers the negative range \(2\le n<k\) qualitatively, and its high-agent theorem covers part of the positive range; those consequences are credited, not asserted as new. The new contribution here is the **exact binary threshold at \(n=k\) for every friendship graph and the three-level common-valuation obstruction at that threshold**. The distinction is not merely EF1 versus \(\mathrm{EF1}_{\mathrm{outer}}\): our positive binary construction works for ordinary EF1, while the negative ternary example excludes ordinary EF1 and hence also excludes \(\mathrm{EF1}_{\mathrm{outer}}\).

Igarashi and Zwicker (2021) study connected fair division of graphs/tangles and different positive conditions, principally for stronger \(\mathrm{EF1}_{\mathrm{outer}}\) and continuous settings. Bousquet et al. (2026) address \(\mathrm{EF1}_{\mathrm{outer}}\) beyond traceable graphs and complexity; their existence and hardness results do not, from the inspected material, establish the identical-binary sharp spectrum with its ternary boundary. Equivalence in uninspected specialist results remains a publication-priority risk.

## Limitations

The guarantee is for **identical binary additive valuations**, not heterogeneous valuations, general nonnegative weights, or the stronger \(\mathrm{EF1}_{\mathrm{outer}}\) fairness criterion. The ternary negative result holds for \(k\ge4\); it does not classify all ternary valuations at \(k=3\), nor the full spectrum for arbitrary additive valuations. Exactly \(n\) nonempty bundles are required, so \(n\le2k+1\). Computational tests are finite. No independent audit has been performed.

## References

1. J. Chen and W. S. Zwicker, *Cutsets and EF1 Fair Division of Graphs*, arXiv:2402.05884v1 (first public release 2024-02-08). https://arxiv.org/abs/2402.05884
2. A. Igarashi and W. S. Zwicker, *Fair division of graphs and of tangled cakes*, arXiv:2102.08560v1 (2021-02-17). https://arxiv.org/abs/2102.08560
3. N. Bousquet, F. Connor, A. Totschnig, and S. Zeitoun, *Fair Division of Graphs: Beyond Traceability*, arXiv:2608.29902v1 (2026-08-30). https://arxiv.org/abs/2608.29902
