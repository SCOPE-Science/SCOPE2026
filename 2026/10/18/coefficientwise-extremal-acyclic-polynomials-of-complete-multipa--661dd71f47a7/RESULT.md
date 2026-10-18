# Coefficientwise extremal acyclic polynomials of complete multipartite graphs and the unique 16-vertex log-concavity threshold

## Finding
Let \(G=K_{n_1,\ldots,n_r}\), with \(r\ge2\), all \(n_i\ge1\), and \(N=\sum_i n_i\). Define the vertex-induced acyclic polynomial \(A_G(z)=\sum_{S\subseteq V(G):\,G[S]\text{ is a forest}}z^{|S|}\).

**Coefficientwise extremal theorem.** Among complete \(r\)-partite graphs of order \(N\), the balanced Turán graph uniquely minimizes every acyclic-polynomial coefficient simultaneously, while \(K_{N-r+1,1,\ldots,1}\) uniquely maximizes them simultaneously, with uniqueness up to graph isomorphism. More precisely, for every admissible \(G\) and every integer \(k\ge0\),
\[
[z^k]A_{T_{N,r}}(z)\le[z^k]A_G(z)\le[z^k]A_{K_{N-r+1,1,\ldots,1}}(z).
\]
When \(G\) is not balanced (respectively not concentrated), at least one inequality is strict. Both extrema are consequently unique for evaluation at any real \(z>0\). For \(r\ge3\), the cubic coefficient already distinguishes every nontrivial balancing step; for \(r=2\), the quartic coefficient does so.

**Sharp finite log-concavity transition.** Every complete multipartite graph with at most \(15\) vertices has a log-concave induced-acyclic coefficient sequence. At order \(16\), precisely one isomorphism type fails log-concavity:
\[
K_{4,1,1,1,1,1,1,1,1,1,1,1,1}=K_{12}+\overline{K}_4.
\]
Here \(+\) denotes graph join and \(\overline{K}_4\) is the independent four-vertex graph. Its polynomial is
\[
1+16z+120z^2+76z^3+49z^4+12z^5,
\]
whose cubic coefficient violates \(76^2\ge120\cdot49\), with deficit \(120\cdot49-76^2=104\). Every \(K_{4,1^s}\) with \(s\ge12\) also has a non-log-concave acyclic polynomial. The sharp lower-order classification is an *exhaustive finite result for this graph family*, not a claim about arbitrary graphs.

The complete polynomial and inclusion-maximal forest polynomial, useful for proving both claims, are respectively
\[
A_G(z)=1+Nz+\binom N2z^2+\sum_{k=3}^{N}\left[\sum_{i=1}^{r}\left(\binom{n_i}{k}+(N-n_i)\binom{n_i}{k-1}\right)\right]z^k
\]
and
\[
M_G(z)=\binom{s}{2}z^2+\sum_{i:n_i\ge2}(N-n_i)z^{n_i+1},
\]
where \(s=|\{i:n_i=1\}|\), and \(M_G\) enumerates inclusion-maximal induced forests. The general acyclic polynomial also follows from the earlier cograph join recurrence of Barton, Brown and Pike; its mere existence is **not** claimed as new.

## Assumptions and scope
All graphs are finite, simple, undirected. Distinct positive integer part sizes define the complete multipartite graph; parts are unordered up to isomorphism. \(T_{N,r}\) has \(r\) part sizes differing by at most \(1\). Throughout \(2\le r\le N\). A vertex-induced forest is an induced subgraph with no cycles, including the empty graph. The acyclic polynomial counts vertex subsets, **not spanning edge forests**. Coefficients vanish outside the polynomial's degree. A finite nonnegative sequence with no internal zero is log-concave when \(a_k^2\ge a_{k-1}a_{k+1}\) at every internal index.

## Proof
**Step 1: complete vertex-subset characterization.** Every chosen vertex subset of size at most two is acyclic. A set of size at least three that meets three distinct parts contains a triangle. A set meeting two parts in at least two vertices apiece contains a four-cycle. Conversely, a set wholly inside one part is independent, and a set choosing one vertex from one part together with any positive number from another part induces a star. Hence, for \(k\ge3\), all acyclic sets are counted uniquely either by \(\binom{n_i}{k}\) within some part \(i\), or by \((N-n_i)\binom{n_i}{k-1}\) for a star with at least two leaves in part \(i\) and its center outside. This proves the polynomial expression.

A forest of size at least three is inclusion-maximal exactly when it contains a whole part \(i\) of size at least two and precisely one vertex outside that part: a missing vertex in the large part could otherwise be added, and a second outside vertex creates a triangle or four-cycle. An acyclic set with two vertices from different parts is maximal exactly when both occupied parts are singletons; adding any further vertex then creates a triangle, while if an occupied part were larger one could add its missing vertices. No smaller set is maximal. This proves the formula for \(M_G\).

**Step 2: elementary concentration inequality.** Fix \(N\) and \(r\). Select two parts of sizes \(a\ge b\ge2\), and form a new graph by transferring one vertex from the smaller to the larger part. Put \(q=N-a-b\), \(y=b-1\), and \(t=k-2\ge1\). Substitution into the coefficient formula and the binomial identities \(\binom{u+1}{j}-\binom uj=\binom{u}{j-1}\), \(\binom u t=\frac ut\binom{u-1}{t-1}\), give the exact difference
\[
\begin{aligned}
\Delta_k={}&q\left(\binom a t-\binom y t\right)\\
&+\frac{ay}{t}\left(\binom{a-1}{t-1}-\binom{y-1}{t-1}\right)\ge0.
\end{aligned}
\]
All binomial coefficients with out-of-range lower indices are defined as zero. Because \(a\ge y+1\), both bracketed differences are nonnegative; the first two coefficients are invariant. For \(r\ge3\), \(q\ge1\) and at \(k=3\), \(\Delta_3=q(a-b+1)>0\). For \(r=2\), \(q=0\), and at \(k=4\), \(\Delta_4=\frac{a(b-1)}2(a-b+1)>0\). Every nonconcentrated positive-integer partition can be converted by such steps to \((N-r+1,1,\ldots,1)\), increasing the polynomial coefficientwise and strictly at a fixed coefficient. Conversely, every nonbalanced partition can be balanced by reversing one such admissible step, decreasing the polynomial coefficientwise and strictly. The order-independent endpoint descriptions establish the inequalities and uniqueness. For \(r=N\) and \(r=N-1\), only one part-size multiset is possible; the uniqueness assertion is then tautological.

**Step 3: the infinite log-concavity obstruction.** For \(s\ge1\), take the part profile \((4,1^s)\), or equivalently the join of a clique of order \(s\) with an independent set of order four. Step 1 gives
\[
A(z)=1+(s+4)z+\binom{s+4}{2}z^2+(4+6s)z^3+(1+4s)z^4+sz^5.
\]
At the internal index \(3\), the log-concavity defect is
\[
\begin{aligned}
a_2a_4-a_3^2
&=\binom{s+4}{2}(1+4s)-(4+6s)^2\\
&=\frac{4s^3-43s^2-41s-20}{2}.
\end{aligned}
\]
It equals \(104\) for \(s=12\). Its forward difference is \(6s^2-37s-40>0\) for all \(s\ge12\). Thus every \(s\ge12\) gives a strict violation, and \(s=12\) yields the displayed order-sixteen counterexample.

**Step 4: exhaustive lower cutoff and uniqueness.** Every complete multipartite graph with \(N\) vertices has exactly one nondecreasing positive part-size sequence summing to \(N\), with at least two parts. The attached stand-alone `verify.py` recursively enumerates *all* these integer partitions for \(2\le N\le16\). It computes the exact coefficient formula from Step 1 using integer binomial arithmetic and checks *every* inequality \(a_k^2-a_{k-1}a_{k+1}\ge0\) through the full degree. Across all \(898\) profiles, the only violation is at \(N=16\) with parts \((1^{12},4)\); its minimum slack is \(-104\). The program contains the complete search and checked assertions and executes to completion. In particular every multipartite graph on at most fifteen vertices is log-concave, and exactly one sixteen-vertex type fails. This is a finite exhaustive proof of the cutoff, not a sample extrapolation.

## Verification
Run `python3 verify.py` with the Python standard library. Its recorded stdout is `verification_output.txt`. First, independent adjacency-and-cycle enumeration checks all forest coefficients and maximal-forest multiplicities directly for each of the \(183\) multipartite profiles with orders \(2\) through \(11\), totaling \(177{,}556\) vertex subsets. Separately, exact integer-partition enumeration checks coefficientwise extremality and log-concavity for all \(898\) multipartite profiles through order \(16\). The complete integer arithmetic includes trailing coefficient trimming but does not disregard internal terms. A parameter sweep corroborates the infinite obstruction for \(1\le s\le80\); Step 3 proves it for all \(s\ge12\). The general concentration theorem is established by Step 2, not by finite enumeration.

## Relationship to prior work
Barton, Brown and Pike's 2020 preprint develops the **same** vertex-induced acyclic polynomial, and its Theorem 1.3 computes polynomials of graph joins. Since complete multipartite graphs are cographs built from joins of independent sets, their theorem already implies the explicit \(A_G\) coefficient formula used here. Their Lemma 2.21 handles the related substitution \(G[K_k]\) for complete multipartite \(G\); that result is also prior. Section 3.1 constructs **nonunimodal** acyclic polynomials for the joins \(K_m+\overline K_6\) with \(m\ge20\). These prior theorems do **not** state the fixed-\((N,r)\) coefficientwise extremal order, nor the sharp first failure of **log-concavity** within all complete multipartite graphs at \(N=16\). In particular, the displayed sixteen-vertex polynomial is unimodal despite its log-concavity failure, so the two claims are not equivalent. This work's contribution is the **extremal order plus sharp log-concavity boundary**, not rediscovery of the acyclic polynomial itself.

Makowsky and Rakita study real-rootedness and almost-sure unimodality for hereditary-property polynomials; these neither determine the fixed-\((N,r)\) multipartite coefficient inequalities nor imply log-concavity through order fifteen. A related published result on complete multipartite **dissociation** polynomials supplies coefficientwise Turán extremizers in a different counting model. Dissociation requires maximum induced degree at most one and excludes induced stars with three leaves that are included here; its formula therefore cannot be substituted for the acyclic polynomial, nor does it settle this log-concavity cutoff. Published work on **rook-graph** induced forests concerns a Cartesian-product graph family rather than a complete multipartite graph.

## Limitations
The coefficientwise inequalities are asserted only for complete multipartite graphs with both \(N\) and \(r\) fixed. The sixteen-vertex sharpness assertion ranges **only** over complete multipartite graphs; it says nothing about earlier counterexamples among arbitrary graphs. The finite cutoff relies on a finite, exact, exhaustively enumerated certificate, not a closed-form inequality for every graph of smaller order. Existing join recurrences cover the general polynomial formula, and their prior authorship is retained. Independent expert evaluation and exhaustive bibliographic priority review have not occurred; differently described equivalent extremal or cutoff results could exist.

## References
1. C. Barton, J. I. Brown, D. A. Pike, *Acyclic polynomials of graphs*, arXiv:2011.01735v1, first public 3 November 2020; Australasian Journal of Combinatorics 82 (2022), 146–181. Theorem 1.3; Lemma 2.21; Section 3.1. https://arxiv.org/abs/2011.01735
2. J. A. Makowsky and V. Rakita, *Almost Unimodal and Real-Rooted Graph Polynomials*, arXiv:2102.00268v1, first public 30 January 2021; European Journal of Combinatorics 108 (2023), 103637. https://arxiv.org/abs/2102.00268
3. *Dissociation polynomials of complete multipartite graphs and their coefficientwise extremizers*, publicly available mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-dissociation-polynomials-of-complete-multipartite-graphs-and-the--6b754da5643b (different induced-subgraph constraint).
