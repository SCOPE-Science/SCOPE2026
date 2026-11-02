# Exact global coalition numbers of balanced complete four-partite graphs

## Finding

Let \(G_q=K_{q,q,q,q}\), with four fixed partite sets of equal size \(q\). For every integer \(q\ge 1\), its global coalition number is
\[
\boxed{GC(G_q)=\max\{2q,\,3q-3,\,4q-8\}.}
\]
Equivalently, the exact values are \(2q\) for \(1\le q\le3\), \(3q-3\) for \(4\le q\le5\), and \(4q-8\) for \(q\ge6\). In particular, this establishes the balanced four-part case of Conjecture 54 in [1].

## Assumptions and scope

Graphs are finite, undirected, simple, and labelled. A set \(D\) is *global dominating* if it dominates both a graph and its complement. Two disjoint nonempty sets are *global coalition partners* when neither is global dominating but their union is. A *global coalition partition* partitions all vertices into classes, none globally dominating, with each class having a distinct coalition partner. Its maximum number of classes is \(GC\). Classes are unordered; the result concerns the maximum class count, not enumeration of maximizing partitions.

For a class \(B\) in a vertex partition of \(G_q\), let \(S(B)\subseteq[4]\) consist of the part indices met by \(B\). Since the complement of \(G_q\) is four disjoint cliques and \(G_q\) is complete multipartite, a nonempty set is global dominating **if and only if** it meets all four parts. Consequently, every class has \(\varnothing\ne S(B)\subsetneq[4]\), and two distinct classes are coalition partners **if and only if** their supports have union \([4]\). For each index \(i\), at most \(q\) classes meet part \(i\), since those classes contain disjoint vertices of that part.

## Proof

**Lower bound.** The construction in Proposition 6 of [1] gives the following explicit partitions. For an integer \(t\in\{1,2,3,4\}\) with \(q\ge t\), choose \(t\) classes \(H_1,\ldots,H_t\), where \(H_i\) meets every part except part \(i\). In each of the first \(t\) parts, put one vertex into every \(H_i\) except \(H_j\) for the part \(j\), and leave its other \(q-t+1\) vertices as singleton classes. Distribute all vertices of every part numbered above \(t\) among the \(H_i\), giving each one at least one vertex. The \(H_i\) are pairwise coalition partners when \(t\ge2\), and each singleton in part \(i\) partners \(H_i\). The class count is
\[
t+t(q-t+1).
\]
For \(t=2\) this gives \(2q\) classes whenever \(q\ge2\); for \(t=3\), \(3q-3\) classes whenever \(q\ge3\); and for \(t=4\), \(4q-8\) classes whenever \(q\ge4\). The graph \(G_1=K_4\) has an admissible partition into two classes. Thus \(GC(G_q)\) is at least the displayed maximum for every \(q\ge1\).

**Upper bound.** Fix an arbitrary global coalition partition \(\mathcal P\), and put \(k=|\mathcal P|\). Call a class *singleton-supported* when its support has exactly one index; the class itself may contain more than one vertex. Let \(t\) be the number of different indices occurring as singleton supports, so \(0\le t\le4\). For each such index \(i\), some class must have support exactly \([4]\setminus\{i\}\), because it partners a class whose support is \(\{i\}\). Call this a *required triple*. Required triples corresponding to different indices are distinct.

If \(t=0\), every class meets at least two parts. Counting part-class incidences gives \(2k\le4q\), hence \(k\le2q\).

If \(t=1\), let \(i\) be the unique singleton-support index. Write \(x\) for the number of singleton-supported classes, \(y\) for the number of other classes meeting part \(i\), and \(z\) for the number of classes avoiding part \(i\). Since \(x+y\le q\), we have \(k=x+y+z\le q+z\). If \(y=0\), every class avoiding \(i\) must partner a singleton-supported class and therefore must meet *all three* other parts. Thus \(z\le q\), giving \(k\le2q\). If \(y>0\), one of the \(z\) classes is a required triple, while every other class avoiding \(i\) meets at least two parts (because no other singleton-support index exists). Moreover, at least one of the \(y\) classes meets a part other than \(i\). Counting incidences with the three other parts yields \(2z+2\le3q\). Therefore
\[
k\le q+\left\lfloor\frac{3q-2}{2}\right\rfloor.
\]
For \(q=2,3\) the right side is \(2q\); for \(q\ge4\) it is at most \(3q-3\). For \(q=1\), the case \(y>0\) is impossible since a singleton-supported class already meets its only vertex in part \(i\).

If \(t=2\), let the singleton-support indices be \(i,j\) and the remaining indices be \(r,s\). Let \(c_h\) be the number of non-singleton-supported classes meeting exactly \(h\) of the two parts \(i,j\), for \(h=0,1,2\), and let \(x\) be the number of singleton-supported classes. Counting incidences in parts \(i,j\) gives \(x+c_1+2c_2\le2q\), hence
\[
k=x+c_0+c_1+c_2\le2q+c_0-c_2.
\]
If \(c_0=0\), this is at most \(2q\). Otherwise, every class counted by \(c_0\) has support \(\{r,s\}\), because no singleton supports occur in those parts. Such a class needs a partner meeting both \(i\) and \(j\), so \(c_2\ge1\). The two required triples, with supports \([4]\setminus\{i\}\) and \([4]\setminus\{j\}\), each meet both parts \(r,s\). Consequently \(c_0\le q-2\), and \(k\le3q-3\).

If \(t=3\), let \(I\) be the three singleton-support indices. Every class intersects at least one part of \(I\); otherwise its support would be a singleton in the fourth part, contrary to \(t=3\). Each of the three required triples meets exactly two parts of \(I\). Thus the total number of part-class incidences restricted to \(I\) is at least \(k+3\), while at most \(3q\). Hence \(k\le3q-3\).

If \(t=4\), the four required triples each meet three parts and therefore contribute two incidences more than a class with one-part support. All remaining classes have at least one incidence. Hence the total part-class incidence count is at least \(k+8\), while at most \(4q\), so \(k\le4q-8\).

For \(q=1\), the four-vertex complete graph has \(GC=2\): no two classes of any partition into three or more classes can unite to dominate its four-vertex edgeless complement. For \(q\ge2\), the preceding cases show
\[
k\le\max\{2q,3q-3,4q-8\}.
\]
The construction attains this bound, completing the proof. \(\square\)

## Verification

The accompanying `verify.py` checks all unlabelled set partitions of the original labelled graphs for \(q=1,2\), constructs valid partitions directly for every \(1\le q\le25\), and independently solves an exact support-incidence mixed-integer optimization for those same values. The separate `verify_direct.cpp` builds original graph and complement adjacency rules, precomputes global domination directly, and exhaustively evaluates all set partitions for \(q=1,2,3\) (respectively \(15\), \(4{,}140\), and \(4{,}213{,}597\) partitions). Both verifiers pass. Compile with `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct` and execute `./verify_direct`; run `python verify.py` with NumPy/SciPy installed. These are finite checks. The preceding incidence proof establishes the formula for all \(q\).

## Relationship to prior work

The primary source [1] introduced global coalition partitions, proved the complete-bipartite and complete-tripartite values, and gave a general multipartite lower bound (Proposition 6). Its Conjecture 54 asserts that this lower bound is always sharp. The construction here is exactly that published lower bound specialized to equal four-part sizes and is **not** claimed as new. The upper bound from the five-case singleton-support analysis proves sharpness for this previously unresolved balanced four-part family. The paper's Corollary 18 identifies an equivalent problem: the classical coalition number of the disjoint union of four equal cliques. Neither Corollary 18 nor the proved three-part case implies the four-part upper bound. Search results did not identify an existing exact four-part formula, but absence from searches is not proof of historical priority.

## Limitations

The theorem covers equal part sizes and exactly four nonempty parts. It does not resolve Conjecture 54 for arbitrary unbalanced four-part graphs or for five or more parts. It counts optimal class cardinality, not the number or symmetry types of maximizing partitions. Historical priority is provisional. Independent mathematical audit has not been performed.

## References

[1] M. Anholcer, N. Besharati, D. A. Mojdeh, M. R. Samadzadeh, *Global coalitions in graphs*, arXiv:2509.15386v4, publicly posted 2026-10-25; Sections 1.2 and 7, especially Proposition 6, Theorem 7, Corollary 18 and Conjecture 54. https://arxiv.org/html/2509.15386v4

[2] N. Besharati, D. A. Mojdeh, M. R. Samadzadeh, *Global coalition sets in graphs*, first public preprint arXiv:2509.15386v1, 2025-09-18 (historical first version; later superseded). https://arxiv.org/abs/2509.15386v1
