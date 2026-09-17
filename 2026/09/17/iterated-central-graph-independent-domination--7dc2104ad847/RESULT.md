# Independent domination of higher iterated central graphs

## Statement

Let \(\mathtt C(G)\) denote the central graph of a finite, simple, connected graph \(G\): every edge of \(G\) is subdivided once, and every pair of nonadjacent original vertices is joined. Write
\[
\mathtt C^0(G)=G,\qquad \mathtt C^{r+1}(G)=\mathtt C(\mathtt C^r(G)).
\]

**Theorem.** Let \(G\) be a nontrivial connected graph. For every integer \(k\ge 3\),
\[
\boxed{\,i(\mathtt C^k(G))=2\,|E(\mathtt C^{k-2}(G))|\,},
\]
where \(i(H)\) is the independent domination number of \(H\).

Thus, from the third central iterate onward, the independent domination number is determined exactly by the edge count two iterates earlier.

If
\[
n_r=|V(\mathtt C^r(G))|,\qquad m_r=|E(\mathtt C^r(G))|,
\]
then
\[
n_{r+1}=n_r+m_r,\qquad
m_{r+1}=m_r+\binom{n_r}{2},
\]
and consequently
\[
\boxed{\,i(\mathtt C^k(G))=2m_{k-2}
      =2(n_{k-1}-n_{k-2})\qquad(k\ge3).\,}
\]
In particular, if \(G\) has order \(n\ge3\) and size \(m\), then
\[
i(\mathtt C^3(G))
=2m+n(n-1).
\]

## Independence number of a central graph

The key structural fact is the following.

**Lemma.** If \(H\) is a connected graph of order \(N\ge3\) and size \(M\), then
\[
\boxed{\alpha(\mathtt C(H))=M.}
\]

**Proof.**
The \(M\) subdivision vertices introduced from the edges of \(H\) are pairwise nonadjacent in \(\mathtt C(H)\), so
\[
\alpha(\mathtt C(H))\ge M.
\]

Let \(I\) be any independent set of \(\mathtt C(H)\), and put
\[
X=I\cap V(H).
\]
Two original vertices are adjacent in \(\mathtt C(H)\) exactly when they are nonadjacent in \(H\). Hence \(X\) induces a clique in \(H\).

A subdivision vertex corresponding to an edge \(uv\in E(H)\) is adjacent to the original vertices \(u\) and \(v\). Therefore every subdivision vertex in \(I\) corresponds to an edge of \(H-X\), and
\[
|I|\le |X|+|E(H-X)|.
\tag{1}
\]

It remains to show that the number of edges of \(H\) incident with \(X\) is at least \(|X|\).

If \(X=\varnothing\), this is immediate. If \(|X|=1\), connectedness gives at least one incident edge. Suppose \(2\le |X|<N\). Since \(X\) is a clique, it contains \(\binom{|X|}{2}\) internal edges; because \(H\) is connected and \(X\ne V(H)\), there is also at least one edge from \(X\) to \(V(H)\setminus X\). Hence the number of edges incident with \(X\) is at least
\[
\binom{|X|}{2}+1\ge |X|.
\]
Finally, if \(X=V(H)\), then \(H\) is complete and
\[
M=\binom N2\ge N=|X|
\]
because \(N\ge3\).

Thus
\[
|X|+|E(H-X)|\le M.
\]
Together with (1), this gives \(|I|\le M\), proving the lemma. \(\square\)

## Proof of the theorem

Cabrera-Martínez, López-Carmona, Rios-Villamar and Serrano-Díaz proved in Theorem 2.12 of arXiv:2609.16357v1 that if a connected graph \(H\) has order \(N\ge3\), size \(M\), and independence number \(\alpha(H)\), then
\[
i(\mathtt C^2(H))
=
M+\binom N2
+\frac{\alpha(H)^2-\alpha(H)(2N-3)}2.
\tag{2}
\]

First assume that either \(|V(G)|\ge3\), or \(k\ge4\). Put
\[
J=\mathtt C^{k-3}(G)
\quad\text{and}\quad
H=\mathtt C(J).
\]
Write
\[
a=|V(J)|,\qquad b=|E(J)|.
\]
In the cases presently under consideration, \(a\ge3\). The lemma gives
\[
\alpha(H)=b.
\tag{3}
\]
By the definition of the central graph,
\[
N:=|V(H)|=a+b
\tag{4}
\]
and
\[
M:=|E(H)|
=2b+\left(\binom a2-b\right)
=b+\binom a2.
\tag{5}
\]

Applying (2) to \(H\), and using (3)--(5),
\[
\begin{aligned}
i(\mathtt C^k(G))
&=i(\mathtt C^2(H))\\
&=M+\binom{a+b}{2}
+\frac{b^2-b(2a+2b-3)}2.
\end{aligned}
\]
The last two terms simplify to
\[
\binom{a+b}{2}
+\frac{b^2-b(2a+2b-3)}2
=
\binom a2+b
=M.
\]
Therefore
\[
i(\mathtt C^k(G))=2M
=2|E(H)|
=2|E(\mathtt C^{k-2}(G))|.
\]

It remains only the boundary case \(G\cong K_2\), \(k=3\). Here
\[
\mathtt C(K_2)\cong P_3.
\]
Applying (2) to \(P_3\), for which \(N=3\), \(M=2\), and \(\alpha(P_3)=2\), gives
\[
i(\mathtt C^3(K_2))
=i(\mathtt C^2(P_3))
=4
=2|E(P_3)|.
\]
This completes the proof. \(\square\)

## Consequences

For a starting graph of order \(n\ge3\) and size \(m\),
\[
m_1=m+\binom n2,
\]
so the first new case beyond the second iterate is
\[
\boxed{i(\mathtt C^3(G))=n(n-1)+2m.}
\]

At the next iterate,
\[
m_2=m+\binom n2+\binom{n+m}{2},
\]
hence
\[
\boxed{
i(\mathtt C^4(G))
=
2m+n(n-1)+(n+m)(n+m-1).
}
\]

More generally, the entire tail
\[
i(\mathtt C^3(G)),i(\mathtt C^4(G)),\ldots
\]
depends on the starting graph only through its order and size, because the recurrence for \((n_r,m_r)\) depends only on \((n_0,m_0)\). In particular, any two connected graphs with the same order and size have identical independent-domination numbers at every central iterate \(k\ge3\), even if their independence numbers and other finer structure differ.

## Context and comparison with prior work

The recent paper

A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar, A. Serrano-Díaz, *Independent domination in central graphs*, arXiv:2609.16357v1 (14 September 2026),

develops formulas and bounds for \(i(\mathtt C(G))\) and concludes with the exact second-iterate formula (2). The paper explicitly introduces the notation \(\mathtt C^2(G)\), but its stated results stop at the second iterate.

The theorem above combines that second-iterate formula with the structural identity
\[
\alpha(\mathtt C(H))=|E(H)|\qquad(|V(H)|\ge3)
\]
to make all subsequent iterates collapse to the edge-count identity
\[
i(\mathtt C^k(G))=2|E(\mathtt C^{k-2}(G))|.
\]

Searches for the exact formula, higher iterates, synonymous “iterated central graph” formulations, and the independence-number identity did not locate a prior statement implying this all-iterate result. The originality claim is therefore only to the best of our knowledge. The elementary independence-number lemma may have appeared separately in older central-graph literature; the claimed contribution is centered on the higher-iterate independent-domination identity and its consequences.

## Limitations

The theorem concerns finite simple connected starting graphs for which the central-graph operator is defined. It does not classify the minimum independent dominating sets achieving the stated cardinalities.

The proof uses Theorem 2.12 of arXiv:2609.16357v1 as an input. Since that preprint is very recent, not-yet-indexed or unpublished parallel work remains a residual originality risk.

No independent validation is asserted.

## Reference

1. Abel Cabrera-Martínez, José Luis López-Carmona, Ismael Rios-Villamar, Alejandro Serrano-Díaz, *Independent domination in central graphs*, arXiv:2609.16357v1 (2026), especially Theorem 2.12. https://arxiv.org/abs/2609.16357
