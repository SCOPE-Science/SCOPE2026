# Exact forced-colouring functions for paths and cycles

## Statement

Let \(\mathrm{FC}_\lambda(G;p)=\mathrm{FC}(G;p,\lambda)\) be the forced colouring function of Farr, and put
\[
r=1-3p.
\]
For a graph \(G\) on \(n\) vertices, let \(N_3(G,k)\) denote the number of partial 3-assignments with exactly \(k\) coloured vertices that force a 3-colouring of \(G\). Then
\[
\mathrm{FC}_3(G;p)=\sum_{k=0}^n N_3(G,k)p^k r^{n-k}.
\]

For the path \(P_n\), \(n\ge2\),
\[
\boxed{
N_3(P_n,n-j)=3\,2^{n-1-j}\binom{n-1-j}{j}
}
\]
for \(0\le j\le\lfloor(n-1)/2\rfloor\), and the remaining coefficients vanish. Equivalently,
\[
\boxed{
\mathrm{FC}_3(P_n;p)
=3\sum_{j=0}^{\lfloor(n-1)/2\rfloor}
\binom{n-1-j}{j}2^{n-1-j}p^{n-j}(1-3p)^j.
}
\]

For the cycle \(C_n\), \(n\ge3\),
\[
\boxed{
N_3(C_n,n-j)
=\frac{n}{n-j}\binom{n-j}{j}
\bigl(2^{n-j}+2(-1)^{n-j}\bigr)
}
\]
for \(0\le j\le\lfloor n/2\rfloor\), and the remaining coefficients vanish. Hence
\[
\boxed{
\mathrm{FC}_3(C_n;p)
=\sum_{j=0}^{\lfloor n/2\rfloor}
\frac{n}{n-j}\binom{n-j}{j}
\bigl(2^{n-j}+2(-1)^{n-j}\bigr)
 p^{n-j}(1-3p)^j.
}
\]

These formulas, together with the known two-colour bipartite formula and the elementary high-colour regime, determine the forced colouring function of every path and cycle for every positive integer number of colours.

## Structural lemma

Fix a 3-colouring \(g\) of a path or cycle. Call a degree-2 vertex *tight* if its two neighbours receive distinct colours under \(g\). Let \(C\) be the initially coloured vertex set and \(U=V\setminus C\).

For a path, \(g|_C\) forces \(g\) if and only if \(U\) is an independent subset of the internal vertices and every vertex of \(U\) is tight. For a cycle, \(g|_C\) forces \(g\) if and only if \(U\) is an independent subset of tight vertices.

Indeed, a 3-forced vertex must see two distinct colours among its coloured neighbours. A path endpoint has only one neighbour and therefore can never be 3-forced. If two initially uncoloured vertices are adjacent, neither can be the first member of that adjacent uncoloured component to be forced, because each is missing a coloured neighbour; thus such a component can never disappear completely. Conversely, if \(U\) is independent and every member is tight, then both neighbours of every \(u\in U\) are already coloured and have distinct colours, so all vertices of \(U\) are immediately forced.

This lemma reduces the forcing problem on paths and cycles to counting independent sets together with compatible proper 3-colourings.

## Proof for paths

Write the colours as elements of \(\mathbb Z_3\). Every proper 3-colouring \(g\) of
\[
v_1v_2\cdots v_n
\]
is uniquely specified by \(g(v_1)\in\mathbb Z_3\) and edge increments
\[
\delta_i=g(v_{i+1})-g(v_i)\in\{+1,-1\},\qquad 1\le i\le n-1.
\]
For an internal vertex \(v_i\), its two neighbours have distinct colours exactly when
\[
\delta_{i-1}=\delta_i.
\]

Fix an independent set \(U\) of \(j\) internal vertices. Because no two selected vertices are adjacent, the \(j\) equality conditions \(\delta_{i-1}=\delta_i\) involve disjoint adjacent edge-pairs. Each removes one binary degree of freedom. Thus the number of proper 3-colourings in which all vertices of \(U\) are tight is
\[
3\,2^{n-1-j}.
\]
The number of independent \(j\)-subsets of the \((n-2)\)-vertex internal path is
\[
\binom{n-1-j}{j}.
\]
The structural lemma now gives the stated coefficient formula.

Equivalently, if \(I(H;x)\) denotes the independence polynomial, then
\[
\mathrm{FC}_3(P_n;p)
=3\,2^{n-1}p^n I\!\left(P_{n-2};\frac{1-3p}{2p}\right),
\]
interpreted through its polynomial expansion above. In particular, for \(n\ge4\),
\[
\boxed{
\mathrm{FC}_3(P_n;p)
=2p\,\mathrm{FC}_3(P_{n-1};p)
+2p(1-3p)\,\mathrm{FC}_3(P_{n-2};p),
}
\]
with \(\mathrm{FC}_3(P_2;p)=6p^2\) and \(\mathrm{FC}_3(P_3;p)=6p^2(1-p)\).

## Proof for cycles

Orient the cycle cyclically and again encode a proper 3-colouring by increments
\[
\delta_1,\ldots,\delta_n\in\{+1,-1\}.
\]
The cyclic closure condition is
\[
\delta_1+\cdots+\delta_n\equiv0\pmod3.
\]
A vertex is tight exactly when the two incident increments are equal.

Fix an independent set \(U\subseteq V(C_n)\) of size \(j\). Its tightness constraints pair \(j\) disjoint pairs of consecutive increments. If a paired value is \(s\in\{\pm1\}\), its contribution to the cyclic sum is \(2s\equiv-s\pmod3\). Replacing each constrained pair by the effective sign \(-s\) therefore gives a bijection with sign sequences of length
\[
m=n-j
\]
whose sum is \(0\pmod3\).

Let \(A_m\) be the number of \(\{\pm1\}\)-sequences of length \(m\) with sum divisible by 3. The roots-of-unity filter gives
\[
A_m=\frac{2^m+2(-1)^m}{3}.
\]
After choosing the first vertex colour in three ways, the number of proper 3-colourings for a fixed \(U\) is therefore
\[
2^{n-j}+2(-1)^{n-j}.
\]
The number of independent \(j\)-subsets of \(C_n\) is
\[
\frac{n}{n-j}\binom{n-j}{j}.
\]
Multiplication proves the cycle coefficient formula.

An independence-polynomial form is
\[
\mathrm{FC}_3(C_n;p)=p^n\left[
2^n I\!\left(C_n;\frac{1-3p}{2p}\right)
+2(-1)^n I\!\left(C_n;-\frac{1-3p}{p}\right)
\right],
\]
again understood via its finite polynomial expansion.

## Complete path/cycle classification for all colour counts

For \(n\ge2\),
\[
\mathrm{FC}_\lambda(P_n;p)=
\begin{cases}
0,&\lambda=1,\\
2\bigl((1-p)^n-(1-2p)^n\bigr),&\lambda=2,\\
\text{the path formula above},&\lambda=3,\\
\lambda(\lambda-1)^{n-1}p^n,&\lambda\ge4.
\end{cases}
\]
For \(n\ge3\),
\[
\mathrm{FC}_\lambda(C_n;p)=
\begin{cases}
0,&\lambda=1,\\
2\bigl((1-p)^n-(1-2p)^n\bigr),&\lambda=2\text{ and }n\text{ even},\\
0,&\lambda=2\text{ and }n\text{ odd},\\
\text{the cycle formula above},&\lambda=3,\\
\bigl((\lambda-1)^n+(-1)^n(\lambda-1)\bigr)p^n,&\lambda\ge4.
\end{cases}
\]
The \(\lambda=2\) expressions are the connected-bipartite formula already proved by Farr. For \(\lambda\ge4\), a path or cycle vertex has degree at most 2 and therefore cannot see the \(\lambda-1\ge3\) distinct neighbour colours required for forcing; consequently only total proper colourings contribute.

## Checks and relation to the recent literature

At \(p=1/3\), \(r=0\), so only the \(j=0\) term remains. The formulas reduce to
\[
3^{-n}P(P_n;3)
\quad\text{and}\quad
3^{-n}P(C_n;3),
\]
as required by the general endpoint identity for the forced colouring function.

For \(P_4\), the path formula gives
\[
24p^3(1-2p),
\]
matching Farr's explicit small-graph calculation. For \(C_4\), the cycle formula gives
\[
6p^2(2-8p+9p^2),
\]
again matching the listed example. For \(P_3=K_{1,2}\), the formula gives
\[
6p^2(1-p).
\]
This agrees with the earlier Farr--Morgan introduction of the polynomial. The currently posted 2026 v1 appears to contain a typographical regression in this one small example, listing \(6p^2(1-2p)\); that expression also fails the general \(p=1/3\) endpoint identity.

A direct exhaustive checker, included as `artifacts/verify.py`, enumerates every partial 3-assignment for \(P_n\) with \(2\le n\le8\) and \(C_n\) with \(3\le n\le8\). It independently verifies all coefficient formulas from the forcing rule. The general proof does not depend on this computation.

## Literature position and originality

The forced colouring function was introduced by Farr and Morgan in 2024/2025. Farr's 2026 paper develops its basic theory, proves a closed formula for connected bipartite graphs when \(\lambda=2\), lists several small examples, and establishes complexity results. The available 2026 text does not give closed \(\lambda=3\) formulas for the path or cycle families. Exact and synonymous searches for forced-colouring/forced-3-colouring formulas on paths and cycles found no prior formula equivalent to the two expressions above.

The closest earlier source is the 2025 Springer chapter corresponding to arXiv:2406.15746. Its arXiv full text was inspected and contains the defining examples, including the correct \(K_{1,2}\) value, but no path or cycle family formula was found. The final typeset Springer chapter was not independently checked page-by-page; an addition present only in that version is therefore a residual originality risk. Very recent or unindexed parallel work is another residual risk. Originality is claimed only to the best of our knowledge.

## Limitations

The result is specific to paths and cycles. The structural lemma uses maximum degree 2 in an essential way: for larger-degree graphs, adjacent initially uncoloured vertices can interact with other coloured neighbours, so the forcing dynamics need not collapse to an independent-set condition. The result does not address the computational complexity of evaluating \(\mathrm{FC}_3\) on broader graph classes.

## References

1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1 (submitted 15 September 2026). https://arxiv.org/abs/2609.17108
2. G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746; published in *Model Theory, Computer Science, and Graph Polynomials*, Trends in Mathematics, Springer (2025), pp. 265--301. https://arxiv.org/abs/2406.15746 ; https://doi.org/10.1007/978-3-031-86319-6_18
