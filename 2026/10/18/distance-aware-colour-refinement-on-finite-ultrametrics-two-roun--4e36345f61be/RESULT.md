# Distance-aware colour refinement on finite ultrametrics: two rounds suffice and eight points first defeat one

## Finding

Fix distinct positive distance values \(\delta_1<\cdots<\delta_h\), with \(h\geq1\). In the class of nonempty finite ultrametric spaces whose nonzero distances belong to this fixed labelled alphabet, distance-aware one-dimensional colour refinement, initialized with one vertex colour, distinguishes any two nonisometric spaces by the global colour histogram after at most \(h-1\) rounds.

For \(h=3\), two rounds therefore suffice. One round distinguishes every pair of nonisometric spaces having at most seven points. Among the \(223\) isometry types on eight points (using an alphabet of three distances, not necessarily all realized), exactly one pair has equal one-round colour histograms. The two members of this pair have the following nested ball partitions. Each brace denotes a ball at radius \(\delta_2\), and the integers inside a brace are the sizes of its constituent radius-\(\delta_1\) balls:

\[
U=\{(2,1,1),(2,1,1)\},\qquad V=\{(2,2),(1,1,1,1)\}.
\]

Both spaces have two four-point radius-\(\delta_2\) balls; each has four points in two-point radius-\(\delta_1\) balls and four singleton radius-\(\delta_1\) balls. They are not isometric, and their two-round histograms are different.

## Assumptions and scope

An ultrametric on a finite nonempty set \(X\) is a symmetric distance function with \(d(x,y)=0\) precisely when \(x=y\) and satisfying \(d(x,z)\leq\max\{d(x,y),d(y,z)\}\). Fix the named distances \(\delta_1<\cdots<\delta_h\), permitting some of them to be unused. Let \(E_0\) be equality; for \(1\leq j\leq h\), let \(E_j(x,y)\) mean \(d(x,y)\leq\delta_j\). The \(E_j\) are nested equivalence relations, with \(E_h\) universal. Two spaces are isometric only when the named distances are preserved.

The initial colour is \(c_0(x)=*\). Define the refinement recursively by treating the displayed signature itself as a canonical colour:

\[
c_{r+1}(x)=\big(c_r(x), (\operatorname{multiset}\{c_r(y):d(x,y)=\delta_j\})_{j=0}^{h}\big),
\]

where \(\delta_0=0\), and the zero-distance multiset contains only \(x\). Comparisons between different spaces use the same recursive signatures, not independently numbered local colour classes. The global histogram at round \(r\) is \(H_r(X)=\operatorname{multiset}\{c_r(x):x\in X\}\). "Distinguishes" means inequality of these histograms. The statement is **relative to the ultrametric class**: it does not assert that the resulting colour histogram characterizes a space among all arbitrarily edge-coloured complete graphs.

## Proof

**1. The nested-ball decoding lemma.** For each integer \(r\) with \(0\leq r\leq h-1\), the colour \(c_r(x)\) determines the isometry type of the \(E_r\)-equivalence class of \(x\), including its named internal distances. At \(r=0\) this class is a singleton. Suppose the statement holds for \(r\). From \(c_{r+1}(x)\) we obtain, by adding the distance-specific neighbour multisets for distances \(\delta_0,\ldots,\delta_{r+1}\), the multiset of previous-round colours of all points in the \(E_{r+1}\)-class \(B\) of \(x\). By induction, every such previous-round colour determines the type \(T\) of its point's \(E_r\)-class. Let \(m_T\) be the total number of points of \(B\) whose previous-round colours decode to \(T\). Then the number of \(E_r\)-classes of type \(T\) contained in \(B\) is exactly \(m_T/|T|\). Since distinct \(E_r\)-classes within one \(E_{r+1}\)-class lie at mutual distance exactly \(\delta_{r+1}\), the multiset of their types determines \(B\) up to isometry. This completes induction. The colours need not be constant on an \(E_r\)-class; only their decoded types are used.

**2. Completeness in \(h-1\) rounds.** The preceding lemma at \(r=h-1\) makes the global histogram \(H_{h-1}(X)\) determine, for each type \(T\), the total number \(m_T\) of points in \(E_{h-1}\)-classes of type \(T\). Their number is \(m_T/|T|\). These classes partition all of \(X\), and distinct classes lie at distance exactly \(\delta_h\). Thus this multiset determines \(X\) up to isometry. When \(h=1\), the uniform zeroth-round histogram already determines the equilateral space by its cardinality.

**3. The one-round profile for three levels.** Take \(h=3\). A point in a radius-\(\delta_1\) ball of size \(p\) inside a radius-\(\delta_2\) ball of size \(q\), in a space of size \(n\), has exact-distance counts

\[
(1,\ p-1,\ q-p,\ n-q).
\]

Its first colour is therefore determined by \((p,q,n)\), and vice versa. Consequently \(H_1\) determines, for every \(q\), the number of radius-\(\delta_2\) balls of size \(q\) and the aggregate counts of their radius-\(\delta_1\) subball sizes, weighted by subball cardinality.

**4. Minimality and uniqueness of the first collision.** If \(q\leq3\), the possible partitions of \(q\) into radius-\(\delta_1\) subball sizes are \((1)\) for \(q=1\); \((2)\), \((1,1)\) for \(q=2\); and \((3)\), \((2,1)\), \((1,1,1)\) for \(q=3\). For each fixed \(q\leq3\), their aggregate weighted size counts determine the multiset of these partitions: the number of size-\(3\) subballs fixes the \((3)\) count; the size-\(2\) count fixes the \((2,1)\) count; the remaining number of radius-\(\delta_2\) balls fixes the all-singleton count. The cases \(q=1,2\) are simpler.

On at most seven points there can be at most one radius-\(\delta_2\) ball of each size \(q\geq4\). In that event its partition into radius-\(\delta_1\) balls is immediately recovered from the one-round size counts. Hence \(H_1\) uniquely determines the isometry type for \(n\leq7\).

At eight points, any nonuniqueness must therefore involve two radius-\(\delta_2\) balls of size at least four, so there are exactly two of size four and no other radius-\(\delta_2\) balls. The possible partitions of four are \((4)\), \((3,1)\), \((2,2)\), \((2,1,1)\), and \((1,1,1,1)\). Aggregate size-\(4\) and size-\(3\) point counts fix the numbers of the first two types. Write \(a,b,c\) for the counts of the last three types. Their number and aggregated counts of size-\(2\) subballs give

\[
a+b+c=\text{constant},\qquad 2a+b=\text{constant}.
\]

Thus any change between two solutions has form \((\Delta a,\Delta b,\Delta c)=(t,-2t,t)\), for an integer \(t\). There are only two balls, so the only nonzero possibility up to exchanging the two solutions is \(t=1\), converting two copies of \((2,1,1)\) into one \((2,2)\) plus one \((1,1,1,1)\). This is the displayed pair \(U,V\). Their one-round profiles coincide, but their radius-\(\delta_2\) ball types differ, so they are not isometric. Step 2 forces two-round separation; directly, in \(U\) every radius-\(\delta_2\) ball has two singleton and two non-singleton points, whereas in \(V\) one ball has four of each kind separately.

The cases above prove uniqueness of the entire first ambiguous isometry pair, without relying on finite enumeration.

## Verification

The standalone standard-library script `verify_ultrametric.py` generates every isometry type of a three-level ultrametric on \(n\) points for \(1\leq n\leq8\) as a multiset of integer partitions, constructs the complete distance matrix, and computes globally comparable recursive colour signatures for rounds one and two. Run `python3 verify_ultrametric.py` from the directory containing this document and the script.

The independent finite census gives total numbers of isometry types \(1,3,6,14,27,58,111,223\) for sizes one through eight, no one-round ambiguity through size seven, exactly the displayed unordered ambiguous pair at size eight, and no two-round ambiguity through size eight. The analytic proof, not the finite computation, establishes the assertion for all cardinalities and arbitrary alphabet length \(h\).

## Relationship to prior work

Carlsson and Mémoli (2010, arXiv:1011.5270), especially their nested partition/dendrogram formalism, motivates the use of threshold-equivalence classes. Gurvich and Vyalyi (2012) provide a canonical nested-graph presentation of finite ultrametrics. Neither the hierarchy representation alone nor the general distance-space theory yields the round-sensitive one-dimensional colour histograms or the exact first ambiguity layer as stated here.

Scheidt and Schweikardt (2024/2025, arXiv:2407.16022) give an algorithm and logical and homomorphism-count characterizations for relational colour refinement in arbitrary relational signatures. Their Theorem A establishes broad expressivity equivalences rather than an exact round bound or the first same-colour collision for three-level ultrametrics.

Kiefer, Schweitzer and Selman (2015, arXiv:1503.08792) give broad criteria and inversion machinery for two-variable counting logic on coloured relational structures. In particular their characterization concerns global identification among all finite relational structures, which is different from identification *within the ultrametric subclass*. Their results supply the ambient formalism but do not state this within-class reconstruction theorem or the sharp one-round eight-point obstruction. Equality of these colour histograms is the usual counting-logic indistinguishability in the signature of named distances, with the refinement-depth bound established here directly.

## Limitations

The distance alphabet and the interpretation of each distance predicate must be fixed across the compared spaces. The two-round assertion is specific to alphabets of three positive distances. No general optimality claim is made for the upper bound \(h-1\) when \(h>3\). One-dimensional refinement is complete here only **relative to ultrametrics**; unrelated edge-coloured complete graphs may share their colour histograms. An earlier equivalent observation or unindexed small enumeration cannot be ruled out definitively; the cited sources establish context, not independent priority certification.

## References

1. G. Carlsson and F. Mémoli, *Classifying Clustering Schemes*, arXiv:1011.5270, first publicly submitted 2010-11-24. https://arxiv.org/abs/1011.5270
2. V. Gurvich and M. Vyalyi, *Characterizing (quasi-)ultrametric finite spaces in terms of (directed) graphs*, Discrete Applied Mathematics 160 (2012), 1742–1756, doi:10.1016/j.dam.2012.03.034. https://doi.org/10.1016/j.dam.2012.03.034
3. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792 (2015), https://arxiv.org/abs/1503.08792
4. B. Scheidt and N. Schweikardt, *Color Refinement for Relational Structures*, arXiv:2407.16022 (first released 2024), https://arxiv.org/abs/2407.16022. Conference version: MFCS 2025, doi:10.4230/LIPIcs.MFCS.2025.88.
