# Exact maximal-shattering counts and a rank plateau for Johnson-graph convexity

## Finding

For integers \(n\ge2\) and \(1\le k<n\), let \(J(n,k)\) be the Johnson graph whose vertices are the \(k\)-element subsets of \([n]\), with two vertices adjacent when they differ by one exchange. Let \(\mathcal C_{n,k}\) be the family of **all geodesically convex vertex sets**, including the empty set. Membership of a Johnson-graph vertex in a convex set is the Boolean query.

**Preparatory shattered-support criterion (a restriction of the known box criterion).** A nonempty support \(S\subseteq\binom{[n]}k\) is VC-shattered by \(\mathcal C_{n,k}\) if and only if each \(X\in S\) has at least one of the following witnesses:

* a **private present coordinate** \(a\in X\) lying in no other member of \(S\); or
* a **private absent coordinate** \(b\notin X\) lying in every other member of \(S\).

The empty support is shattered as well. Consequently, the dimension is exactly
\[
\operatorname{VCdim}(\mathcal C_{n,k})
=n-\min\{2,k-1,n-k-1\}
=\begin{cases}
n,&\min\{k,n-k\}=1,\\
n-1,&\min\{k,n-k\}=2,\\
n-2,&\min\{k,n-k\}\ge3.
\end{cases}
\]

**Number of maximum-cardinality shattered supports.** Write \(E(n,k)\) for the number of distinct subsets of \(V(J(n,k))\) whose size is its VC dimension and which are shattered. Then
\[
E(n,k)=\begin{cases}
1,&\min\{k,n-k\}=1,\\
8,&n=4,\ k=2,\\
n,&\min\{k,n-k\}=2\text{ and }n\ge5,\\
\displaystyle\frac{n!}{2(k-1)!(n-k-1)!}
+\binom n2\bigl(\mathbf1_{\{k=3\}}+\mathbf1_{\{n-k=3\}}\bigr),
&3\le k\le n-3.
\end{cases}
\]
The last formula has an especially simple geometric interpretation: in the interior range \(4\le k\le n-4\), every largest shattered support comes from a uniquely determined three-part partition \([n]=P\sqcup Q\sqcup R\) with \(|P|=n-k-1\), \(|Q|=k-1\), and \(|R|=2\). Its vertices are exactly
\[
\{Q\cup\{i\}:i\in P\}
\ \cup\
\{(Q\setminus\{j\})\cup R:j\in Q\}.
\]
For example, \(J(8,4)\) has VC dimension \(6\) and exactly \(560\) maximum shattered supports; \(J(6,3)\) has VC dimension \(4\) and exactly \(120\) maximum supports.

## Assumptions and scope

All graphs are finite, simple, unweighted, and have every edge of length one. Geodesic convexity means containing **every** vertex of **every** shortest path between any two vertices of the set. The graph's domain consists of \(k\)-subsets (not points of the Boolean cube outside its constant-weight layer). A concept is a subset of this domain and queries are vertex-membership tests. Supports consist of distinct domain vertices. The formula includes every nontrivial rank \(1\le k<n\) and every \(n\ge2\); it does not assert a Littlestone-dimension formula.

For \(I\subseteq U\subseteq[n]\), define a *rank-\(k\) Boolean interval* by
\[
[I,U]_k=\{X\subseteq[n]: |X|=k,\ I\subseteq X\subseteq U\}.
\]
An empty interval is allowed. A nonempty convex set has this form; this structural fact is proved below rather than assumed from literature.

## Proof

**1. Johnson intervals and a convex-set representation.** For \(A,B\in\binom{[n]}k\), distance in \(J(n,k)\) equals \(k-|A\cap B|\). Each shortest path removes the elements of \(A\setminus B\) and inserts those of \(B\setminus A\), one exchange at a time. Therefore the set of all vertices on shortest paths from \(A\) to \(B\) is precisely \([A\cap B,A\cup B]_k\). In particular every nonempty rank-\(k\) Boolean interval is convex.

Conversely, let \(F\) be a nonempty geodesically convex family of \(k\)-sets, and set \(I=\bigcap F\), \(U=\bigcup F\). For any **distinct** \(a,b\in U\setminus I\), there is a member \(C\in F\) containing \(b\) and avoiding \(a\). Indeed, choose \(C_0\in F\) containing \(b\). If \(a\notin C_0\), take \(C=C_0\). Otherwise choose \(D\in F\) avoiding \(a\). Since \(C_0\) and \(D\) have equal cardinality, some \(y\in D\setminus C_0\) exists. The exchanged set \((C_0\setminus\{a\})\cup\{y\}\) lies on a shortest path from \(C_0\) to \(D\), hence belongs to \(F\); it still contains \(b\) and avoids \(a\).

Now take any \(k\)-set \(T\) with \(I\subseteq T\subseteq U\), and choose \(B\in F\) maximizing \(|B\cap T|\). If \(B\ne T\), pick \(a\in B\setminus T\) and \(b\in T\setminus B\). Both lie in \(U\setminus I\). The preceding observation produces \(C\in F\) containing \(b\) but not \(a\). The set \((B\setminus\{a\})\cup\{b\}\) is on a shortest \(B\)-to-\(C\) path, hence belongs to \(F\), and has larger intersection with \(T\). This is impossible. Therefore \(F=[I,U]_k\). It follows that the convex hull of any nonempty subfamily \(Y\) of vertices is exactly \([\bigcap Y,\bigcup Y]_k\).

**2. The private-coordinate criterion.** Let \(S\) be a support of at least two vertices. If \(S\) is shattered, then for each \(X\in S\), a convex hypothesis must contain every member of \(Y=S\setminus\{X\}\) and exclude \(X\). Such a hypothesis contains \([\bigcap Y,\bigcup Y]_k\); hence either \(X\not\subseteq\bigcup Y\) or \(\bigcap Y\not\subseteq X\). These two alternatives are exactly a private present or private absent coordinate, respectively.

Conversely, suppose the witness condition holds. For each nonempty \(Y\subseteq S\), choose the convex interval \([\bigcap Y,\bigcup Y]_k\). It contains all of \(Y\). Any \(X\in S\setminus Y\) with a private present coordinate has an element outside \(\bigcup Y\), and any such \(X\) with a private absent coordinate omits an element of \(\bigcap Y\). Thus the interval contains no unwanted support point. The empty trace is realized by the empty convex hypothesis. Singletons satisfy the criterion because \(k\ge1\) and are shattered; the empty support is automatic. This proves the equivalence for every support.

**3. Upper dimension bound.** Let \(S\) be a shattered support of size \(t\ge3\). Choose one witness coordinate for each point and classify it as positive (private present) or negative (private absent); write \(p\) and \(q\) for their counts. All chosen coordinates are distinct: two positive witness patterns cannot coincide, two negative ones cannot coincide, and a singleton-one column cannot equal a singleton-zero column when \(t\ge3\).

If \(q=0\), each support vertex omits the other \(t-1\) positive witness coordinates, so \(t\le n-k+1\). If \(p=0\), each support vertex contains the other \(t-1\) negative witness coordinates, so \(t\le k+1\). If \(p,q>0\), every positive-type vertex contains all \(q\) negative witness coordinates plus its own positive witness; hence \(q\le k-1\). Every negative-type vertex omits all \(p\) positive witness coordinates plus its own negative witness; hence \(p\le n-k-1\). Therefore \(t=p+q\le n-2\). Together these yield
\[
 t\le\max\{n-k+1,k+1,n-2\}.
\]
The small cases \(t\le2\) satisfy the stated bound directly.

**4. Constructions attaining the bound.** If \(k=1\) or \(n-k=1\), the Johnson graph is complete, so every vertex subset is convex and the VC dimension is \(n\). If \(k=2\), choose a fixed singleton \(C\) and take all \(k\)-sets \(C\cup\{i\}\) for \(i\notin C\): each has a private present coordinate and the support size is \(n-1\). Complementation proves the case \(n-k=2\).

For \(3\le k\le n-3\), partition the \(n\) coordinates into \(P,Q,R\) with respective sizes \(n-k-1,k-1,2\). Consider the \(n-2\) rank-\(k\) vertices
\[
S(P,Q,R)=\{Q\cup\{i\}:i\in P\}
\cup\{(Q\setminus\{j\})\cup R:j\in Q\}.
\]
Each first-type vertex has private present coordinate \(i\), and each second-type vertex has private absent coordinate \(j\). The criterion proves that this support is shattered. This proves the dimension formula.

**5. Exact enumeration of maximum supports.** In rank \(1\) or corank \(1\), the unique maximum support is the entire \(n\)-vertex graph. For rank \(2\) with \(n\ge5\), attaining \(n-1\) forces all chosen witnesses to be positive, because all-negative supports have size at most three and mixed supports have size at most \(n-2\). Equalities force exactly the \(n\) supports \(\{\{c,i\}:i\ne c\}\), one for each coordinate \(c\). The corank-two case follows by complementation. At \(n=4,k=2\), all-positive and all-negative constructions each give four different supports of size three, totaling eight.

Now suppose \(3\le k\le n-3\). For a maximum support of size \(t=n-2\), a mixed witness assignment must satisfy equality in both bounds of step 3, so \(p=n-k-1\) and \(q=k-1\), leaving precisely two unused coordinates \(R\). All \(q\) negative witness coordinates plus its own witness already exhaust the \(k\) ones of each positive-type vertex, which must therefore be \(Q\cup\{i\}\). Similarly the \(p\) positive witness coordinates plus its own negative witness exhaust the \(n-k\) zeros of each negative-type vertex, so that vertex must be \((Q\setminus\{j\})\cup R\). The support therefore has exactly the displayed mixed form.

This representation is unique. In its column-by-support incidence matrix, the coordinates in \(P\) occur in exactly one support vertex; those in \(Q\) occur in exactly \(t-1\) support vertices; and those in \(R\) occur in exactly \(q\) support vertices. Since \(p,q\ge2\), the integers \(1,q,t-1\) are pairwise different, making \(P,Q,R\) intrinsic to the support. Thus mixed maximum supports are counted by
\[
\binom{n}{n-k-1,\ k-1,\ 2}=
\frac{n!}{2(n-k-1)!(k-1)!}.
\]
An all-positive maximum support requires \(n-k+1=n-2\), or \(k=3\). The unused \(k-1=2\) coordinates then occur in every vertex, so each such support is the full collection of rank-three vertices containing a particular two-set; there are \(\binom n2\) choices. Dually an all-negative maximum support requires \(n-k=3\) and gives another \(\binom n2\) choices. These supports do not coincide with the mixed families (or one another). Summing the disjoint classes gives the stated enumeration.

## Verification

The included `verify_johnson_convexity.py` uses only Python's standard library. Run `python3 verify_johnson_convexity.py` in the directory containing the file. The program constructs Johnson vertices as bitsets, computes graph distances from symmetric differences, and independently checks geodesic convexity against every excluded vertex for every possible concept on \(J(3,1)\), \(J(4,2)\), and \(J(5,2)\). The resulting convex families agree exactly with all generated rank-\(k\) Boolean intervals.

For \(J(6,3)\), it constructs the \(304\) distinct interval concepts and checks the private-coordinate criterion against direct Boolean trace shattering for all \(21{,}700\) supports of sizes zero through five. It also enumerates maximum supports for every \(3\le n\le7\) and every nontrivial rank, comparing their counts with the closed formula. Finally it verifies the mixed constructions and absence of duplicate outputs for parameters \((n,k)=(8,4),(8,3),(9,4),(10,5)\), yielding respectively \(560,420,1260,3150\) supports of the mixed form. The universal statements rely on the proof above, not on finite extrapolation.

## Relationship to prior work

Adler, Benediktsson, and Macpherson (first public preprint 31 July 2020, arXiv:2007.16042) study the VC dimension of **open neighborhoods**, i.e. the graph edge relation on Johnson and Hamming graphs. Their Theorem 3.6 proves the universal upper bound four for Johnson open-neighborhood VC dimension, a different hypothesis class from all convex vertex subsets. No open-neighborhood bound implies the present rank-dependent convexity formula or complete support criterion.

Chepoi (first public preprint 13 May 2024, arXiv:2405.07512), particularly Section 7.1 and Proposition 18, studies geodesic-convex halfspaces, semispaces, and the \(S_3\) separation property in partial Johnson graphs. The result concerns separation structure, not the traces of all convex sets on arbitrary supports. Thiessen and Gärtner (ECML PKDD 2022, DOI 10.1007/978-3-031-26412-2_22) study online mistake bounds for graph-convex classes in general. Their public abstract does not state this Johnson-specific VC classification; the full text was not accessible in this investigation, which remains a historical-priority limitation.

The interval representation is an older structural observation, not claimed as novel. Furthermore, the private-coordinate support criterion is a restriction of the general Hamming-box criterion: intersect all binary-coordinate boxes with the constant-weight layer. That criterion is used as a preparatory tool, not claimed as new. The **new claim** is the sharp rank-dependent VC-dimension formula, the exact all-parameter number of maximal shattered supports, and the exhaustive mixed/pure extremal structure. The unrestricted Hamming-box theorem does not by itself evaluate these extremal parameters on the constant-weight layer. Earlier exact enumerations under the equivalent language of Boolean subcube ranges on a fixed-weight slice remain a historical-priority risk.

## Limitations

The theorem addresses ordinary VC shattering, not adaptive Littlestone dimension, VC density of unrelated neighborhood classes, efficient graph learning, or arbitrary matroid basis graphs. The proof is finite, exact, and constructive, but independent mathematical audit and comprehensive priority verification have not been performed. The full text of the graph-convex online-learning paper of Thiessen and Gärtner (2022) was unavailable; the publicly accessible abstract supports only the stated comparison. The included code exhausts small parameter cases and selected constructions; it does not exhaust all support families for unbounded parameters.

## References

1. I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1, first posted 2020-07-31; journal DOI 10.1016/j.dam.2021.09.017.
2. V. Chepoi, *Separation axiom S3 for geodesic convexity in graphs*, arXiv:2405.07512v1, first posted 2024-05-13, especially Section 7.1 and Proposition 18.
3. M. Thiessen, T. Gärtner, *Online Learning of Convex Sets on Graphs*, ECML PKDD 2022, DOI 10.1007/978-3-031-26412-2_22; full-text accessibility limitation noted above.
