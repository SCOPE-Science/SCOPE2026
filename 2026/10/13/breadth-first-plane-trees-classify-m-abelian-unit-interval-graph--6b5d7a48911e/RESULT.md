# Breadth-first plane trees classify m-Abelian unit interval graphs

## Finding
For every integer \(n\ge1\), let an area sequence be \(a=(a_1,\ldots,a_n)\) satisfying \(a_1=0\), \(0\le a_i<i\), and \(a_i\le a_{i-1}+1\) for \(i\ge2\). It defines the graph \(\Gamma_a\) on \([n]\), with \(\{j,i\}\in E(\Gamma_a)\) for \(j<i\) if and only if \(j\ge i-a_i\). The graph is **\(m\)-Abelian** when \([n]\) admits a partition into at most \(m+1\) consecutive cliques, as in the definition of Alexandersson and Leite [1].

**Theorem.** Put \(p_i=i-a_i-1\) and give the vertex \(i\) parent \(p_i\) for \(1\le i\le n\), with root \(0\) and children arranged in increasing order. This constructs a bijection from area sequences of size \(n\) to plane rooted trees with \(n\) edges, whose vertex labels are breadth-first indices. If \(T_a\) is this tree and \(\kappa_c(\Gamma_a)\) is the least number of consecutive clique blocks, then
\[
\boxed{\kappa_c(\Gamma_a)=\alpha(\Gamma_a)=\operatorname{height}(T_a).}
\]
Consequently, the \(m\)-Abelian graphs are exactly those with \(\operatorname{height}(T_a)\le m+1\) under this bijection. Their exact number \(A_{n,m}\) satisfies, upon setting \(A_{0,m}=1\) for the empty-object generating function,
\[
\boxed{\sum_{n\ge0} A_{n,m}z^n=\frac{Q_{m+1}(z)}{Q_{m+2}(z)},\quad Q_0(z)=Q_1(z)=1,\quad Q_{h+1}(z)=Q_h(z)-zQ_{h-1}(z).}
\]
In particular, for every \(n\ge1\),
\[
\boxed{A_{n,1}=2^{n-1},\qquad A_{n,2}=F_{2n-1},\qquad A_{n,3}=\frac{3^{n-1}+1}{2},}
\]
where \(F_0=0\), \(F_1=1\), and \(F_{k+2}=F_{k+1}+F_k\). The corresponding generating functions at \(m=2\) and \(m=3\) are
\[
\frac{1-2z}{1-3z+z^2},\qquad\frac{1-3z+z^2}{1-4z+3z^2}.
\]

## Assumptions and scope
The vertices are the ordered set \([n]\) with the specific area-sequence encoding, rather than unlabeled isomorphism classes. The plane trees are rooted, with ordered children, and height is the largest edge-distance from the root \(0\). A consecutive clique block is a nonempty interval of consecutive vertex labels inducing a clique; a partition into at most \(m+1\) blocks is equivalent to the weak-cut version of the \(m\)-Abelian definition in [1]. The empty object at \(n=0\) is used only to write generating functions. The theorem concerns the size of the class, not the peak or peak-nesting statistics of its members.

## Proof
**1. The breadth-first bijection.** The area inequalities give \(0\le p_i<i\), \(p_1=0\), and
\[
p_{i+1}-p_i=1-(a_{i+1}-a_i)\ge0.
\]
Thus parents are nondecreasing along the new labels; all children of any vertex are consecutive, and the parent-index blocks appear in their increasing order. Since every parent precedes its child, this exactly says that visiting the rooted, ordered tree breadth-first gives labels \(0,1,\ldots,n\). Conversely, the parent sequence of vertices numbered in breadth-first order in an arbitrary plane rooted tree is nondecreasing and satisfies \(0\le p_i<i\) and \(p_1=0\); setting \(a_i=i-p_i-1\) recovers an area sequence. These constructions are mutually inverse.

**2. Independent sets and tree depth.** Let \(b_i\) be the maximum cardinality of an independent set of the induced graph on \([i]\) that contains vertex \(i\), with \(b_0=0\). Earlier vertices nonadjacent to \(i\) are exactly \(\{1,\ldots,p_i\}\). Therefore
\[
b_i=1+\max_{0\le j\le p_i}b_j.
\]
The upper limits \(p_i\) are nondecreasing, so the sequence \((b_i)_{i\ge0}\) is nondecreasing. Hence \(b_i=1+b_{p_i}\) for every \(i\). This is precisely the recurrence for root distance \(d_i\) in the tree: \(d_0=0\), \(d_i=1+d_{p_i}\). Consequently \(b_i=d_i\) and
\[
\alpha(\Gamma_a)=\max_{1\le i\le n}b_i=b_n=\max_{1\le i\le n}d_i=\operatorname{height}(T_a).
\]
The displayed equality \(b_n=\max b_i\) uses monotonicity and is valid for all area sequences, including disconnected cases.

**3. Consecutive clique blocks.** Any partition into \(q\) cliques intersects an independent set in at most one vertex per block, so \(\kappa_c(\Gamma_a)\ge\alpha(\Gamma_a)\). For the reverse inequality, start a block at \(s=1\), ending it just before the least \(j>s\) with \(p_j\ge s\); if no such \(j\) exists, finish at \(n\). For every vertex \(v\) in this block, \(p_v<s\), so all earlier vertices \(u\) of the same block satisfy \(u>p_v\) and therefore are adjacent to \(v\). Thus every block is a clique. The starting vertices of consecutive blocks are pairwise nonadjacent: when a new block begins at \(t\), one has \(p_t\ge s\) for the previous start \(s\); because all still earlier starts are at most \(s\), none is adjacent to \(t\). Therefore the block starts form an independent set. Their number \(q\) is at most \(\alpha\), while the clique partition gives \(q\ge\alpha\), proving \(\kappa_c=\alpha\).

**4. Enumeration.** A plane rooted tree is a possibly empty ordered sequence of subtrees attached to a root. If \(H_h(z)\) counts those of height at most \(h\) by their number of edges, then \(H_0(z)=1\) and, as formal power series,
\[
H_h(z)=\frac1{1-zH_{h-1}(z)},\qquad h\ge1.
\]
Let \(Q_0=Q_1=1\) and \(Q_{h+1}=Q_h-zQ_{h-1}\). Induction gives \(H_h=Q_h/Q_{h+1}\). Applying parts 1--3 with \(h=m+1\) gives the claimed generating function. The first cases are
\[
H_2(z)=\frac{1-z}{1-2z},\quad H_3(z)=\frac{1-2z}{1-3z+z^2},\quad H_4(z)=\frac{1-3z+z^2}{1-4z+3z^2}.
\]
Their positive-degree coefficients are, respectively, \(2^{n-1}\), \(F_{2n-1}\), and \((3^{n-1}+1)/2\). The final two follow either from the denominator recurrences and initial coefficients or from partial fractions.

In addition, taking the contour walk of the **newly constructed tree**, rather than the original Dyck path underlying the area sequence, provides an explicit bijection to Dyck paths of semilength \(n\) and maximum height at most \(m+1\). The distinction between the two Dyck-path encodings is essential: the ordinary area-sequence Dyck-path height need not equal graph independence number.

## Verification
Run `python3 verify.py` with Python 3.8 or later; no third-party packages are used. For every area sequence with \(1\le n\le9\), the program independently constructs the graph, computes its independence number by exhaustive subsets, computes its minimum contiguous-clique partition using dynamic programming, reconstructs the purported breadth-first tree, and compares the exact height distribution with bounded Dyck excursions counted by a separate walk algorithm. It also checks the continued-fraction coefficients and the closed cases for \(m=1,2,3\). The complete deterministic output is in `verification_output.txt`.

There are \(1,2,5,14,42,132,429,1430,4862\) area sequences for sizes \(1\) through \(9\). Exhaustive checks cannot prove the theorem for all sizes; the preceding induction and bijections supply that proof.

## Relationship to prior work
Alexandersson and Leite [1, Sections 3, 4, and 7] define the area-sequence graph model, show that the one-Abelian case admits two consecutive cliques, and count it as \(2^{n-1}\). Their Section 7 introduces general \(m\)-Abelian graphs and asks for further refined enumerations involving peaks and peak-nestings. The present result supplies the unweighted class cardinality uniformly for all \(m\) and identifies its exact tree-height statistic; it **does not** settle their peak-polynomial questions.

The enumeration of bounded-height Dyck paths and the rational determinant/continued-fraction recurrences are classical; Bacher [2] covers a far more general bounded-excursion enumerator. The new mathematical assertion here is the explicit graph-to-breadth-first-tree bijection that carries the minimum consecutive clique count to tree height. Thus the classical Dyck enumerator is *applied*, not claimed as a new result. Saitoh and collaborators [3] enumerate connected proper interval graphs up to isomorphism by canonical balanced-parenthesis strings; that problem and its equivalence classes differ from the ordered area-sequence count and height refinement here.

## Limitations
These counts are for canonical ordered area-sequence representations, not for isomorphism classes of graphs. No result is asserted about the joint peak/peak-nesting distributions, connected subfamily, asymptotics with growing \(m\), or any independent external validation. The classical bounded-Dyck-height part is not an originality claim. The literature comparison is not exhaustive against all historical synonyms of proper interval graphs; equivalent unindexed formulations remain possible.

## References
[1] Per Alexandersson and Leonardo Saud Maia Leite, *Peaks and peak-nestings on unit interval graphs*, arXiv:2609.38084v1, first posted 2026-09-29. https://arxiv.org/abs/2609.38084

[2] Axel Bacher, *Generalized Dyck paths of bounded height*, arXiv:1303.2724v1, first posted 2013-03-11. https://arxiv.org/abs/1303.2724

[3] T. Saitoh, K. Yamanaka, M. Kiyomi, and R. Uehara, *Random Generation and Enumeration of Proper Interval Graphs*, IEICE Transactions on Information and Systems E93-D (2010), 1816--1823, DOI:10.1587/transinf.E93.D.1816.
