# An exact one-link trophic-incoherence law for rooted food webs
## Finding
Consider any rooted directed tree \(T\) with \(n\ge3\) vertices and every original arc oriented from a resource toward its consumer, away from the root. The root is basal. Each other vertex has one original prey.

If one new, previously absent arc \(u\to v\) is added without deleting an original link, assuming the target \(v\) is nonbasal and \(u\ne v\), then the augmented network has exactly \(n\) directed edges. The ordinary ecological trophic levels are obtained by assigning the basal root level \(1\) and requiring at each other vertex that the level equal one plus the arithmetic mean of its predecessors' levels.

Write \(d(x)\) for depth in the original rooted tree, and let \(q\) be classical unweighted trophic incoherence (standard deviation of trophic differences). Two exhaustive cases occur.

**Acyclic additional link.** If \(v\) is *not* a proper ancestor of \(u\), then
\[
q^2=\frac{\bigl(d(v)-d(u)-1\bigr)^2}{2n}.
\]

**Feedback additional link.** If \(v\) *is* a proper ancestor of \(u\), then the new link closes exactly one directed cycle. With
\[
\ell=d(u)-d(v)\ge1,
\]
its squared incoherence is
\[
q^2=\frac{2(\ell+1)^2}{n}.
\]

Both formulas are independent of the tree's branching structure and of the location of the modified vertices except through the stated depths and ancestry.

In particular, any feedback addition costs at least
\[
q^2\ge\frac8n,
\]
with equality if and only if \(u\) is a child of the nonbasal \(v\). Every acyclic addition that changes coherence has
\[
q^2\ge\frac1{2n},
\]
and this lower bound is attainable at every order \(n\ge3\). Thus the **minimum nonzero squared cost** for feedback is sixteen times the minimum nonzero squared cost for acyclic additions, when the minima are taken over the class of all rooted trees of that order. This does *not* say that every cyclic addition costs more than every acyclic one.

There are also genuinely coherence-preserving new links. If \(a_h\) counts original vertices at depth \(h\), their exact number is
\[
\sum_{h\ge1} a_h\bigl(a_{h-1}-1\bigr).
\]

## Assumptions and scope
The network is finite, directed, simple, unweighted, and rooted. Original links are the arcs of an out-arborescence: one basal root and exactly one prey for every other species. At most one directed edge may occur from a given source to a given target. Reciprocal links are permitted but self-links are not.

The modification adds exactly one previously absent arc \(u\to v\), where \(v\) is not basal and \(u\ne v\). The requirement that \(v\) not be basal prevents removing the only basal species. Repeating an existing parent-to-child link is not an allowed new edge.

The convention is *classical Johnson-type trophic level*: for each vertex \(w\) with at least one incoming edge,
\[
s_w=1+\frac{1}{\deg^-(w)}\sum_{x\to w}s_x.
\]
The root has \(s=1\). Each arc \(x\to y\) has trophic difference \(s_y-s_x\), whose arithmetic mean over all arcs is exactly \(1\). With \(L=n\) augmented edges,
\[
q^2=\frac1L\sum_{x\to y}(s_y-s_x)^2-1
=\frac1n\sum_{x\to y}(s_y-s_x-1)^2.
\]

The findings concern this specific metric. The alternative symmetric-Laplacian definition of directedness introduced by MacKay, Johnson, and Sansom is not interchangeable with these formulas.

## Proof
**1. Baseline and solvability.** In the original rooted tree, every vertex at depth \(h\) has level \(h+1\), and every original trophic difference equals \(1\). All vertices remain reachable from the basal root after adding the arc. The trophic-level linear equations therefore have a unique solution (equivalently, the finite Markov averaging recurrence can be solved because the basal root is accessible from every vertex by reverse paths).

Only the target \(v\) changes indegree, from one to two. All original tree equations below \(v\) remain single-parent recurrences, so every descendant of \(v\) receives the same additive level shift as \(v\). All vertices outside the descendant subtree of \(v\) retain their baseline levels.

Let \(p=p(v)\). On the original tree,
\[
s_p=d(v),\qquad s_v^{(0)}=d(v)+1.
\]
All augmented original arcs except \(p\to v\) continue to have trophic difference \(1\). Only \(p\to v\) and the new arc \(u\to v\) contribute to the squared incoherence.

The target-level equation says the sum of the differences on these two incoming links is exactly \(2\); therefore the two deviations of their differences from \(1\) are negatives of each other.

**2. No directed cycle.** Suppose \(v\) is not an ancestor of \(u\). Then \(u\) lies outside the shifted descendant subtree, and
\[
s_u=d(u)+1.
\]
The target equation yields
\[
s_v=1+\frac{s_p+s_u}{2}
=\frac{d(v)+d(u)+3}{2}.
\]
Set
\[
k=d(v)-d(u).
\]
The two exceptional trophic differences are
\[
s_v-s_p=\frac{3-k}{2},\qquad
s_v-s_u=\frac{k+1}{2}.
\]
Their deviations from \(1\) are respectively
\[
\frac{1-k}{2},\qquad \frac{k-1}{2}.
\]
Consequently,
\[
q^2=\frac1n\left[\left(\frac{1-k}{2}\right)^2+\left(\frac{k-1}{2}\right)^2\right]
=\frac{(k-1)^2}{2n}.
\]
The same formula holds when \(u\) is an ancestor of \(v\): this is a forward shortcut, not a cycle, and its source remains outside the descendant subtree of \(v\).

**3. One feedback cycle.** Suppose \(v\) is a proper ancestor of \(u\). The unique original directed path from \(v\) to \(u\) has length
\[
\ell=d(u)-d(v)\ge1.
\]
The newly added reverse arc closes precisely that path into a directed cycle. Every original tree edge on this path still raises the level by exactly \(1\), so
\[
s_u=s_v+\ell.
\]
The target equation now gives
\[
2s_v=2+s_p+s_u
=2+d(v)+s_v+\ell,
\]
whence
\[
s_v=d(v)+\ell+2.
\]
The two exceptional differences are
\[
s_v-s_p=\ell+2,\qquad s_v-s_u=-\ell.
\]
They deviate from \(1\) by respectively \(\ell+1\) and \(-\ell-1\). Hence
\[
q^2=\frac{2(\ell+1)^2}{n}.
\]
Since \(\ell\ge1\), the smallest feedback value is \(8/n\), attained precisely at \(\ell=1\) when the target is a nonbasal parent of the source.

**4. Sharp positive acyclic bound and zero-cost classification.** In the acyclic case, \(k\) is an integer. Either \(k=1\), so \(q=0\), or the nonzero integer \(k-1\) has squared absolute value at least \(1\), giving \(q^2\ge1/(2n)\). A path with at least three vertices admits the additional forward shortcut from the root to the grandchild, with \(k=2\); attaching extra vertices extends the witness to every larger \(n\).

Coherence is unchanged precisely when
\[
d(v)=d(u)+1.
\]
For every target \(v\) at depth \(h\ge1\), there are \(a_{h-1}\) source vertices at the previous depth. Exactly one of them is already linked to \(v\), namely its original parent. None is a descendant of \(v\). Thus there are exactly \(a_{h-1}-1\) allowed zero-cost new links into \(v\). Summing over the \(a_h\) targets at each depth proves
\[
\#\{\text{new arcs with }q=0\}
=\sum_{h\ge1} a_h(a_{h-1}-1).
\]

## Verification
The complete standalone package includes `verify_single_edge_trophic.py`. Run with Python 3:

`python3 verify_single_edge_trophic.py`

Its exact arithmetic does not hard-code trophic levels. An independent Gaussian-elimination solver constructs the full network linear system and computes all trophic differences before comparing them with the theorem's formulas.

Every labeled rooted tree (with root label fixed by relabeling symmetry) of orders \(3\) through \(6\) is generated by its Prüfer code; all allowed additional arcs are tested. There are also reproducibly seeded samples of larger trees of orders \(7\), \(8\), and \(9\). In all, the verifier tests \(1,740\) rooted-tree instances and \(40,322\) allowed arc additions, including \(29,303\) acyclic and \(11,019\) feedback cases. It checks the exact zero-cost counting formula on every sampled tree. Output includes `VERIFY_OK`.

The proof, not this finite computation, establishes the claim for every \(n\ge3\).

## Relationship to prior work
Johnson, Domínguez-García, Donetti, and Muñoz introduced trophic coherence as a food-web structural measure and defined trophic levels from prey averages. Their theory studies coherence and dynamical stability rather than a complete one-edge perturbation law for arbitrary rooted food-web trees.

Johnson and Jones developed a coherence ensemble linking incoherence to network cycles and spectra. Their main results concern ensemble predictions for loop counts and eigenvalues; they do not state the exact two-case per-edge formulas or enumerate all coherence-preserving added links on a rooted tree.

MacKay, Johnson, and Sansom later developed a different, symmetric-Laplacian measure that is well-defined more generally. It cannot be substituted for classical trophic incoherence here; the proof concerns the older trophic-level averaging definition.

The result supplies an exact finite motif calibration: a nonparent link that connects consecutive original trophic layers can leave perfect coherence intact, while a feedback cycle of length \(\ell+1\) has a strictly positive cost quadratic in its length, independent of unrelated branching.

## Limitations
The theorem assumes equal unweighted prey contributions and a rooted arborescence before exactly one additional link. Weighted feeding, multiple additional edges, disconnected webs, multiple basal roots, and arbitrary network structures require different analysis.

The index is a structural statistic, not a model-independent stability guarantee. In particular, a large value of \(q\) does not by itself prove a given population-dynamics model unstable.

The independent solver provides exact finite verification; it is not an independent scientific audit, and no mathematical theorem is inferred merely from enumeration.

## References
1. S. Johnson, V. Domínguez-García, L. Donetti, and M. A. Muñoz, “Trophic coherence determines food-web stability,” *Proceedings of the National Academy of Sciences* 111 (2014), 17923–17928, doi:10.1073/pnas.1409077111; first public preprint arXiv:1404.7728, 30 April 2014.
2. S. Johnson and N. S. Jones, “Looplessness in networks is linked to trophic coherence,” *Proceedings of the National Academy of Sciences* 114 (2017), 5618–5623, doi:10.1073/pnas.1613786114; first public preprint arXiv:1505.07332, 20 May 2015.
3. R. S. MacKay, S. Johnson, and B. Sansom, “How directed is a directed network?”, *Royal Society Open Science* 7 (2020), article 201138, doi:10.1098/rsos.201138.
4. V. Domínguez-García, S. Johnson, and M. A. Muñoz, “Intervality and coherence in complex networks,” *Chaos* 26 (2016), 065308, doi:10.1063/1.4953163; arXiv:1603.03767.
