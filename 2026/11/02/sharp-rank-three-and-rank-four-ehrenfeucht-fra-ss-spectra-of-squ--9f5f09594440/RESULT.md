# Sharp rank-three and rank-four Ehrenfeucht–Fraïssé spectra of squared cycles

## Finding

Let \(G_n=C_n^2\), for every integer \(n\ge3\), be the simple undirected graph on \(\mathbb Z/n\mathbb Z\) in which distinct vertices are adjacent exactly when their cyclic distance is at most two. Work in the first-order language containing equality and one binary adjacency predicate, with no designated vertices and no circular-order predicate. Write \(G_m\equiv_qG_n\) when these graphs satisfy the same first-order sentences of quantifier rank at most \(q\).

The complete rank-three classification is
\[
G_m\equiv_3G_n\iff
\bigl(3\le m,n\le5\bigr)\ \text{or}\ 
\bigl(m=n\in\{6,7,8,9,10\}\bigr)\ \text{or}\
\bigl(m,n\ge11\bigr).
\]
The complete rank-four classification is
\[
G_m\equiv_4G_n\iff
\bigl(m=n=3\bigr)\ \text{or}\
\bigl(4\le m,n\le5\bigr)\ \text{or}\
\bigl(m=n\in\{6,7,\ldots,18\}\bigr)\ \text{or}\
\bigl(m,n\ge19\bigr).
\]
In particular the exact stabilization thresholds are eleven at rank three and nineteen at rank four. Notice that \(G_3,G_4,G_5\) are complete graphs, so their small-rank behavior is exceptional. This is a statement about logical equivalence, not graph isomorphism: distinct sizes at or above a threshold are not isomorphic.

## Assumptions and scope

The graph \(C_n\) is the simple cycle with vertices \(0,\ldots,n-1\) and edges between cyclically consecutive vertices; for \(n=3\) this is a triangle. Its square adds edges between vertices at graph distance two. The quantifier rank of an atomic formula is zero, and a quantifier increases rank by one. Repeated choices of vertices in Ehrenfeucht–Fraïssé games are allowed. There are no constants, counting quantifiers, linear orders, or successor relations in the logical vocabulary.

## Proof

**1. A finite exact type recurrence.** Fix a graph \(G\), an ordered tuple \(\bar a\) of already selected vertices (possibly with repetitions), and a nonnegative integer \(r\). Its atomic diagram \(D_G(\bar a)\) records every equality and adjacency relation among entries of the tuple. Define recursively
\[
T_0(G,\bar a)=D_G(\bar a),\qquad
T_{r+1}(G,\bar a)=\Big(D_G(\bar a),\{T_r(G,\bar a\mathbin{\|}v):v\in V(G)\}\Big).
\]
Here \(\bar a\mathbin{\|}v\) is the tuple obtained by appending \(v\), and the braces denote an ordinary set (not a multiset). Then the two positions \((G,\bar a)\) and \((H,\bar b)\) are equivalent for \(r\) further Ehrenfeucht–Fraïssé rounds if and only if their \(T_r\)-types agree. Inductively, equality of sets of one-point extension types is exactly the requirement that every move in either structure admit a matching response in the other; the atomic diagram supplies the terminal condition. In a nonempty structure, the prefix atomic diagram can also be recovered from every child type, so an implementation may omit the redundant diagram at positive depths.

**2. A uniform large-cycle strategy.** We prove the useful bound that, for \(q\ge1\), all squared cycles of sizes \(n,m\ge3\cdot 2^{q-1}\) are \(q\)-equivalent. For each \(r\ge0\), put \(t_r=3\cdot2^r-1\). Then \(t_0=2\) and \(t_r=2t_{r-1}+1\) for \(r\ge1\).

After the first vertex is selected in each cycle, fix the cyclic orientation arbitrarily. Duplicator preserves the cyclic order of all *distinct* selected vertices and requires the numbers of unselected vertices in corresponding successive cyclic gaps to be either equal and smaller than \(t_r\), or both at least \(t_r\), where \(r\) is the number of rounds remaining. Initially there is one gap with \(n-1\) or \(m-1\) unselected vertices. Because \(n,m\ge 3\cdot2^{q-1}=t_{q-1}+1\), this initial invariant holds.

If Spoiler repeats a selected vertex, Duplicator repeats its partner. Otherwise Spoiler splits a gap of size \(\ell\) into two gaps \(a,b\ge0\) with \(a+b=\ell-1\). If \(\ell<t_r\), the equal corresponding gap can be split at the same position. If both gaps have at least \(t_r=2t_{r-1}+1\) vertices, at most one of \(a,b\) can be smaller than \(t_{r-1}\). Match any such smaller side exactly, leaving the other side at least \(t_{r-1}\); if neither side is smaller, split the partner gap into two sides both at least \(t_{r-1}\). This maintains the invariant, and the symmetric argument works regardless of which cycle Spoiler chooses.

At the end, \(r=0\), so corresponding gaps agree when their lengths are zero or one, and otherwise are both at least two. Equality of selected vertices is preserved. Adjacency in \(G_n\) is cyclic distance one or two. Between selected vertices, such a short route crosses at most two successive cyclic gaps, and whether its length is at most two is determined by which gaps have zero or one unselected vertex. Thus all adjacency facts are preserved. This proves the stated uniform bound, giving \(n,m\ge12\) for rank three and \(n,m\ge24\) for rank four.

**3. Exact finite bridge and sharpness.** The accompanying executable verifiers evaluate the recurrence from part 1 on every \(G_n\) with \(3\le n\le24\), at ranks three and four. Every ordered tuple of four vertices, including repetitions, is enumerated for the rank-four base diagrams. Each higher type is the exact set of all child types, globally interned across graph sizes. No candidate moves, graph vertices, or assignment patterns are sampled or omitted. The two programs independently implement the recurrence with different tuple representations and exact set equality.

Both return precisely the following equivalence classes of sizes:

* Rank three: \(\{3,4,5\}\), the five singleton classes \(\{6\},\ldots,\{10\}\), and \(\{11,12,\ldots,24\}\).
* Rank four: \(\{3\}\), \(\{4,5\}\), the thirteen singleton classes \(\{6\},\ldots,\{18\}\), and \(\{19,20,\ldots,24\}\).

The uniform large-cycle strategy connects the last rank-three class to every size at least twelve and the last rank-four class to every size at least twenty-four. The finite bridge includes \(11\sim_3 12\) and \(19\sim_4 24\); transitivity therefore extends both classifications to **every** cycle size. All other pairs of size-classes are separated by the exact type computation, and by the finite-model Ehrenfeucht–Fraïssé theorem therefore differ on a sentence of the asserted rank. This proves both claims and the sharpness of each stabilization threshold.

## Verification

Run `python3 verify_rank4.py` using Python 3 standard library only. Independently compile `verify_independent.cpp` with a conforming C++17 compiler and run the resulting binary. Both generate and compare the full rank-three and rank-four partitions for sizes \(3\) through \(24\); they do not rely on reference output files, random seeds, numerical tolerances, or probabilistic hashes. The Python program enumerates tuples directly; the C++ program indexes tuples by base-\(n\) integers. The universal bound is proved in part 2 and does not rest on extrapolation from these computations.

## Relationship to prior work

Fagin, Lenchner, Regan, and Vyas develop Ehrenfeucht–Fraïssé and multi-structural games, especially logical distinguishing resources for linear orders. The result here concerns the *ordinary* quantifier-rank game on squares of cycles, not the minimum total number of quantifiers.

Brown and Hoshino establish a complete description of these games on **ordinary paths and ordinary cycles**. Their graph classes have maximum degree two, whereas \(C_n^2\) has degree four for \(n\ge6\). Applying their ordinary-cycle theorem through the one-quantifier interpretation of squared-cycle adjacency gives only a substantially weaker eventual-equivalence bound and does not determine the sharp rank-three and rank-four partitions above. Hng investigates powers of paths and cycles from extremal graph theory, not logical indistinguishability. The present work supplies an exact logical classification for the first nontrivial cycle power.

## Limitations

Only the third and fourth quantifier ranks are classified; the statement does not assert an all-rank formula or quantify the minimum *total number of quantifiers*. The finite bridge is computationally exhaustive and deterministic, but independently written scientific scrutiny remains desirable. Searches of accessible literature cannot establish absolute historical priority, especially under equivalent descriptions such as circulants \(\operatorname{Cay}(\mathbb Z/n\mathbb Z,\{\pm1,\pm2\})\) or four-regular ring lattices.

## References

- E. K. Hng, *Minimum degree conditions for powers of cycles and paths*, Acta Mathematica Universitatis Comenianae **88** (2019), 795–800; first public date verified 2019-07-30, https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/view/1274.
- R. Fagin, J. Lenchner, K. W. Regan, and N. Vyas, *Multi-Structural Games and Number of Quantifiers*, preprint initially posted 2021-04-30, arXiv:2104.14709; later journal version, *Logical Methods in Computer Science* **21** (2025), 10:1–10:37, https://arxiv.org/abs/2104.14709.
- J. Brown and R. Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles*, *Ars Combinatoria* **83** (2007), 193–212, https://combinatorialpress.com/ars-articles/volume-083-ars-articles/the-ehrenfeucht-fraisse-game-for-paths-and-cycles/.
