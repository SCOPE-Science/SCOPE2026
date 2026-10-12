# Minimum double outer-independent dominating sets of crown graphs
## Finding
Let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph for \(n\ge4\), with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and deleted perfect matching
\[
M=\{a_i b_i:1\le i\le n\}.
\]
Then
\[
\gamma_d^{oi}(\operatorname{Cr}_n)=n+2.
\]

For every \(n\ge5\), the minimum double outer-independent dominating sets are exactly
\[
B\cup\{a_i,a_j\}
\quad\text{and}\quad
A\cup\{b_i,b_j\},
\qquad 1\le i<j\le n.
\]
Thus there are exactly
\[
2\binom n2=n(n-1)
\]
minimum sets.

For \(n=4\), these twelve sets are joined by
\[
V(\operatorname{Cr}_4)\setminus\{a_i,b_i\},
\qquad 1\le i\le4,
\]
so \(\operatorname{Cr}_4\) has exactly \(16\) minimum sets.

## Assumptions and scope
A set \(D\subseteq V(G)\) is double outer-independent dominating when
\[
|N[v]\cap D|\ge2
\]
for every \(v\in V(G)\), and
\[
V(G)\setminus D
\]
is independent. The minimum cardinality is \(\gamma_d^{oi}(G)\).

The theorem begins at \(n=4\). The graph \(\operatorname{Cr}_3\) is \(C_6\), so its scalar value is already covered by the known cycle formula.

## Proof
Put
\[
I=V(\operatorname{Cr}_n)\setminus D.
\]
Because \(I\) is independent, either it lies entirely in one bipartition class or, if it meets both classes, it is exactly one deleted matching pair.

First suppose
\[
I\subseteq A.
\]
Then \(B\subseteq D\). Write
\[
k=|D\cap A|.
\]
If \(k=0\), every \(b_j\) has only itself in \(N[b_j]\cap D\), so double domination fails. If \(k=1\), say \(D\cap A=\{a_i\}\), then \(b_i\) is not adjacent to \(a_i\) and again
\[
|N[b_i]\cap D|=1.
\]
Hence
\[
k\ge2,
\]
so
\[
|D|\ge n+2.
\tag{1}
\]
Conversely, every
\[
B\cup\{a_i,a_j\},
\qquad i\ne j,
\]
is feasible: each \(b_r\) has itself and at least one of \(a_i,a_j\) in its closed neighborhood, while every \(a_r\) has all \(n-1\) vertices of \(B\) except its unmatched partner as neighbors. The symmetric family with the roles of \(A\) and \(B\) reversed is feasible as well. Thus
\[
\gamma_d^{oi}(\operatorname{Cr}_n)\le n+2.
\tag{2}
\]

Now suppose \(I\) meets both classes. If \(a_i,b_j\in I\), independence forces \(i=j\), since \(a_i\) is adjacent to every \(b_j\) except \(b_i\). No third vertex can join this pair, because every other \(A\)-vertex is adjacent to \(b_i\) and every other \(B\)-vertex is adjacent to \(a_i\). Therefore
\[
I=\{a_i,b_i\}
\]
and
\[
|D|=2n-2.
\tag{3}
\]
Such a set is feasible for \(n\ge3\): an omitted vertex has \(n-1\) selected neighbors, while a selected vertex has itself plus at least \(n-2\) selected neighbors in the opposite class.

Hence
\[
\gamma_d^{oi}(\operatorname{Cr}_n)=\min\{n+2,2n-2\}.
\]
For \(n\ge4\) this equals \(n+2\). If \(n\ge5\), the inequality is strict, so only the one-side-complement families are minimum, yielding \(2\binom n2\) sets. At \(n=4\), both expressions equal \(6\), so the four deleted-matching-pair complements also attain the minimum.

## Verification
The included checker constructs \(\operatorname{Cr}_n\) for
\[
3\le n\le8
\]
and exhaustively tests every vertex subset against the defining conditions. It compares both the minimum cardinality and the complete minimum-set family with the piecewise theorem.

## Relationship to prior work
The invariant was introduced in 2017. The introducing paper gives
\[
\gamma_d^{oi}(K_{p,q})=
\begin{cases}
q+1,&p=1,\\
p+1,&2\le p\le q,
\end{cases}
\]
so in particular
\[
\gamma_d^{oi}(K_{n,n})=n+1.
\]
It also proves that deleting one edge changes the parameter by at most one, but that local statement does not determine the cumulative effect of deleting a perfect matching.

A 2018 primary paper proves that double and total outer-independent domination coincide when the minimum degree is at least two, and gives a general upper bound for bipartite graphs. Those results apply to crown graphs but do not determine the exact crown value or its minimum sets. Targeted searches in the full text found no crown treatment.

Thus the crown result identifies the exact perfect-matching-deletion effect:
\[
n+1\longrightarrow n+2,
\]
and completely classifies equality, including the \(n=4\) boundary tie.

## Limitations
The theorem treats balanced crown graphs, not arbitrary matching deletions from \(K_{p,q}\).

The finite verification through \(n=8\) is corroborative only; the all-orders proof is the independent-complement classification above.

A differently phrased or non-indexed crown-graph treatment may exist.

## References
1. M. Krzywkowski, “Double outer-independent domination in graphs,” Ars Combinatoria 134 (2017), 193–207; public journal record dated 31 July 2017.
2. D. A. Mojdeh, I. Peterin, B. Samadi, I. G. Yero, “On three outer-independent domination related parameters in graphs,” arXiv:1812.10946v1, 28 December 2018; Discrete Applied Mathematics 294 (2021), 115–124.
3. A. Cabrera Martínez, “Double outer-independent domination number of graphs,” Quaestiones Mathematicae 44 (2021), 1835–1850, DOI 10.2989/16073606.2020.1834001.
