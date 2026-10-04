# Exact logical width of arbitrary complete multipartite graphs

## Finding
Let \(G\) be a finite nonempty complete multipartite graph. For each integer \(s\ge1\), let \(m_s\) be the number of parts of size \(s\), and put
\[
M=\max\!\left(\max\{s:m_s>0\},\;\max\{m_s:m_s>0\}\right).
\]
Then the ordinary first-order logical width of \(G\) is exactly
\[
W(G)=M+1.
\]
Thus the number of variable symbols needed to define a complete multipartite graph is controlled by two independent bottlenecks: the largest part and the largest multiplicity of any one part size.

## Assumptions and scope
Graphs are finite, nonempty, simple, and undirected. Logical width \(W(G)\) is the minimum number of distinct variable symbols in an ordinary first-order sentence that defines \(G\) up to isomorphism among finite graphs. Equality is available and there are no counting quantifiers. A complete multipartite graph is specified by the multiset of its part sizes.

## Proof
For vertices \(x,y\), write
\[
x\sim y \quad\Longleftrightarrow\quad (x=y)\lor\neg E(x,y).
\]
On a complete multipartite graph this is exactly the relation of belonging to the same part. Conversely, in the class of simple graphs, requiring \(\sim\) to be transitive makes it an equivalence relation and forces the graph to be complete multipartite. Transitivity needs only three variable symbols.

For \(s\ge1\), let \(C_s(x)\) say that the \(\sim\)-class of \(x\) has exactly \(s\) elements. The lower bound \(|[x]|\ge s\) uses \(x\) together with \(s-1\) further variables. The upper bound \(|[x]|\le s\) forbids \(x\) together with \(s\) further pairwise distinct vertices all equivalent to \(x\). Hence \(C_s(x)\) can be written with \(s+1\) variable symbols.

Fix a size \(s\) occurring in \(G\). To say that there are at least \(m_s\) classes satisfying \(C_s\), choose \(m_s\) pairwise inequivalent representatives and require \(C_s\) of each. To say that there are at most \(m_s\), forbid \(m_s+1\) pairwise inequivalent representatives all satisfying \(C_s\). Bound variables inside each occurrence of \(C_s\) may shadow and then release other representative names, so the whole exact-count requirement uses at most
\[
\max\{s+1,m_s+1\}=\max\{s,m_s\}+1
\]
variable symbols. Finally require every vertex to satisfy \(C_s\) for one of the finitely many sizes occurring in \(G\). This last clause uses at most one more variable than the largest part size. If \(M\ge2\), the three-variable complete-multipartite axiom also fits inside the same pool of \(M+1\) names. The sole case \(M=1\) is the one-vertex graph, which is definable with two variables. Therefore
\[
W(G)\le M+1.
\]

For the reverse inequality, use the standard infinite \(k\)-pebble game characterization of \(k\)-variable first-order equivalence and take \(k=M\).

First suppose the largest part size equals \(M\). Form \(H\) by enlarging one part of size \(M\) to size \(M+1\), leaving all other parts unchanged. Duplicator matches every unchanged part with its copy and matches the exceptional parts with each other. At any move, after the chosen pebble is lifted, at most \(M-1\) other pebbles remain in the exceptional part. Thus the side whose exceptional part has only \(M\) vertices always has a fresh matching vertex when one is needed. Equality and adjacency are preserved forever, so Duplicator wins the \(M\)-pebble game on \(G,H\).

Otherwise the largest part size is strictly below \(M\). By definition of \(M\), some size \(s<M\) occurs in exactly \(M\) parts. Form \(H\) by adding one further part of size \(s\). Duplicator maintains a bijection between currently pebbled size-\(s\) parts and matches all other parts with their identical copies. When Spoiler moves a pebble into a previously unused size-\(s\) part, at most \(M-1\) other such parts can still be represented by pebbles, so even the side with only \(M\) of them has an unused matching part. Within a matched part both sides have exactly \(s\) vertices, so equality can also be matched. Again Duplicator wins forever with \(M\) pebbles.

In both cases \(H\not\cong G\). Hence no \(M\)-variable sentence defines \(G\), so \(W(G)>M\). Together with the upper bound,
\[
W(G)=M+1.
\]

## Verification
A supplementary checker tests the lower-witness construction in two independent finite ways. For every integer partition of total size at most twelve, it computes the standard capped class-size profile at \(k=M\) and verifies that the witness has the same \(k\)-variable profile, while the profiles separate at \(M+1\). It also solves the infinite pebble game by greatest fixed point for a collection of small instances, and checks the balanced specialization on a parameter grid. The recorded output is

`VERIFY_OK profile_cases=271 pebble_cases=18 balanced_cases=64`

These computations are consistency checks only. The all-parameter proof is the symbolic argument above.

## Relationship to prior work
Finite-variable logics are a standard part of finite model theory, and graph logical width is the established invariant measuring the least number of variables in a defining first-order sentence. The standard graph-logical-complexity literature records, for example, the extremal identity \(W(K_n)=n+1\) in ordinary first-order logic. Work on first-order fragments with a built-in equivalence relation studies expressive power, satisfiability, and model properties, but the inspected sources do not state this exact finite-structure width formula.

The formula strictly extends the balanced complete multipartite case. If all \(r\) parts have size \(s\), then \(m_s=r\), giving
\[
W(K_{s,\ldots,s})=\max\{r,s\}+1.
\]
It also gives \(W(K_n)=n+1\) and \(W(\overline K_n)=n+1\), while handling arbitrary heterogeneous part multisets with the same one-line rule.

## Limitations
The theorem concerns ordinary first-order logic on finite simple graphs. It does not address counting quantifiers, formula length, quantifier rank, infinite complete multipartite graphs, or richer signatures. The originality check is necessarily limited by indexing and terminology: because the argument is elementary, an equivalent statement could exist as folklore, an exercise, or an unindexed note.

## References
1. Martin Grohe, “Finite Variable Logics in Descriptive Complexity Theory,” *Bulletin of Symbolic Logic* 4(4) (1998), 345–398. DOI: 10.2307/420954.
2. Oleg Pikhurko, Helmut Veith, and Oleg Verbitsky, “The First Order Definability of Graphs: Upper Bounds for Quantifier Rank,” arXiv:math/0311041, first posted 4 November 2003.
3. Oleg Pikhurko and Oleg Verbitsky, “Logical complexity of graphs: a survey,” *Contemporary Mathematics* 558 (2011), 129–180; arXiv:1003.4865.
4. Emanuel Kieroński and Antti Kuusisto, “Uniform One-Dimensional Fragments with One Equivalence Relation,” *CSL 2015*, LIPIcs 41, 597–615. DOI: 10.4230/LIPIcs.CSL.2015.597.
5. Ian Pratt-Hartmann, “The two-variable fragment with counting and equivalence,” *Mathematical Logic Quarterly* 61 (2015). DOI: 10.1002/malq.201400102.
