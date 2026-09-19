# Exact forced-colouring polynomials of paths

Let \(P_n=v_1\cdots v_n\) be the path on \(n\ge2\) vertices. For a positive integer \(\lambda\), let \(\operatorname{FC}_\lambda(G;p)\) be the forced \(\lambda\)-colouring polynomial: each vertex independently receives each one of the \(\lambda\) colours with probability \(p\), remains uncoloured with probability \(1-\lambda p\), and an uncoloured vertex is repeatedly forced when exactly \(\lambda-1\) distinct colours occur on its coloured neighbours. Let \(\operatorname{fcol}(G,k;\lambda)\) count forcing partial assignments whose initial domain has size \(k\), and write
\[
\operatorname{FCGP}_\lambda(G,x)=\sum_k \operatorname{fcol}(G,k;\lambda)x^k.
\]

## Main theorem

For every \(n\ge2\),
\[
\boxed{
\operatorname{FCGP}_3(P_n,x)
=3\sum_{j=0}^{\lfloor (n-1)/2\rfloor}
2^{\,n-j-1}\binom{n-1-j}{j}x^{n-j}.}
\]
Equivalently,
\[
\boxed{
\operatorname{fcol}(P_n,n-j;3)
=3\,2^{\,n-j-1}\binom{n-1-j}{j}}
\]
for \(0\le j\le\lfloor(n-1)/2\rfloor\), and all other coefficients vanish. Therefore
\[
\boxed{
\operatorname{FC}_3(P_n;p)
=3\sum_{j=0}^{\lfloor (n-1)/2\rfloor}
2^{\,n-j-1}\binom{n-1-j}{j}
 p^{n-j}(1-3p)^j.}
\]

Together with the already known bipartite \(\lambda=2\) formula and the general maximum-degree observation for \(\lambda\ge4\), this gives the full forced-colouring function of every nontrivial path:
\[
\boxed{
\operatorname{FC}_\lambda(P_n;p)=
\begin{cases}
0, & \lambda=1,\\[1mm]
2\big((1-p)^n-(1-2p)^n\big), & \lambda=2,\\[1mm]
3\displaystyle\sum_{j=0}^{\lfloor (n-1)/2\rfloor}
2^{n-j-1}\binom{n-1-j}{j}p^{n-j}(1-3p)^j, & \lambda=3,\\[3mm]
\lambda(\lambda-1)^{n-1}p^n, & \lambda\ge4.
\end{cases}}
\]

## Proof of the new \(\lambda=3\) formula

Fix a partial 3-assignment \(f\) of \(P_n\) that eventually forces a 3-colouring, and let \(U\) be the set of vertices initially left uncoloured.

First, \(v_1,v_n\notin U\): a path endpoint has only one neighbour, so it can never see the two distinct neighbour colours required for 3-forcing. Second, \(U\) is independent. Indeed, if the initially uncoloured vertices contained a consecutive block of length at least two, then no vertex of that block could be the first one forced: every vertex in the block has an uncoloured neighbour, while a degree-two path vertex needs both neighbours coloured before it can see two distinct colours. Hence such a block can never start to fill.

Let \(g\) be the unique full 3-colouring eventually forced by \(f\). Since \(U\) is independent, both neighbours of every \(v_i\in U\) are initially coloured. Thus \(v_i\) is forced exactly when
\[
g(v_{i-1})\ne g(v_{i+1}).
\]
Conversely, if \(U\subseteq\{v_2,\ldots,v_{n-1}\}\) is independent and a proper 3-colouring \(g\) has distinct colours on the two neighbours of every vertex of \(U\), then restricting \(g\) to \(V(P_n)\setminus U\) immediately forces every vertex of \(U\). Therefore successful partial assignments are in bijection with such pairs \((U,g)\).

There are
\[
\binom{n-1-j}{j}
\]
independent \(j\)-subsets of the \(n-2\) internal vertices. Fix one such \(U\). Identify the three colours with \(\mathbb Z_3\). A proper 3-colouring is determined by \(g(v_1)\) and by the edge differences
\[
\varepsilon_i=g(v_{i+1})-g(v_i)\in\{+1,-1\}\subset\mathbb Z_3,
\qquad 1\le i<n.
\]
For \(v_i\in U\), the condition \(g(v_{i-1})\ne g(v_{i+1})\) is equivalent to
\[
\varepsilon_{i-1}=\varepsilon_i.
\]
Because \(U\) is independent, these \(j\) equality constraints involve disjoint adjacent pairs of edge-difference variables, so they are independent and reduce the \(2^{n-1}\) possible sign sequences by a factor \(2^j\). After the three choices of \(g(v_1)\), the number of compatible full colourings is therefore
\[
3\,2^{n-1-j}.
\]
Multiplying by the number of choices for \(U\) proves the coefficient formula, and the probability formula follows by weighting an assignment with \(j\) initially uncoloured vertices by \(p^{n-j}(1-3p)^j\). \(\square\)

## Fibonacci-type recurrence and forcing certificates

Put \(G_n(x)=\operatorname{FCGP}_3(P_n,x)\). The coefficient formula yields
\[
G_2(x)=6x^2,\qquad G_3(x)=6x^2+12x^3,
\]
and, for \(n\ge4\),
\[
\boxed{G_n(x)=2x\big(G_{n-1}(x)+G_{n-2}(x)\big).}
\]
Using the standard relation between \(\operatorname{FCGP}\) and \(\operatorname{FC}\), the probability polynomials satisfy
\[
F_2=6p^2,\qquad F_3=6p^2(1-p),
\]
\[
\boxed{F_n=2pF_{n-1}+2p(1-3p)F_{n-2}\qquad(n\ge4),}
\]
where \(F_n=\operatorname{FC}_3(P_n;p)\).

The smallest possible initial domain of a forcing partial 3-colouring has size
\[
\boxed{\left\lceil\frac{n+1}{2}\right\rceil.}
\]
Moreover, the number of minimum-domain forcing assignments is
\[
\boxed{
\begin{cases}
3t\,2^t,&n=2t,\\
3\,2^t,&n=2t+1.
\end{cases}}
\]
At \(x=1\), the total number \(N_n\) of forcing partial 3-assignments obeys
\[
N_2=6,\qquad N_3=18,\qquad N_n=2N_{n-1}+2N_{n-2},
\]
so \(N_n\) grows on the exponential scale \((1+\sqrt3)^n\). Consequently, under the uniform four-state experiment \(p=1/4\), the probability of forcing a 3-colouring decays on the exponential scale \(((1+\sqrt3)/4)^n\).

## A correction to the three-vertex example

The current arXiv version of Farr's *The forced colouring function of a graph* gives, in Proposition 6(10),
\[
\operatorname{FC}_3(K_{1,2};p)=6p^2(1-2p).
\]
Since \(K_{1,2}=P_3\), the theorem above gives instead
\[
\boxed{\operatorname{FC}_3(K_{1,2};p)=6p^2(1-p).}
\]
This can also be checked without the general theorem: there are six successful initial assignments with exactly two coloured vertices and twelve proper total 3-colourings, hence
\[
6p^2(1-3p)+12p^3=6p^2(1-p).
\]
There is also an internal consistency check. At \(p=1/3\) there are no uncoloured vertices, so the defining identity gives
\[
\operatorname{FC}_3(P_3;1/3)=\frac{P(P_3;3)}{3^3}=\frac{12}{27}=\frac49.
\]
The displayed \(6p^2(1-2p)\) evaluates to \(2/9\), while the corrected formula evaluates to \(4/9\). Thus the discrepancy is an apparent error in that displayed special case, not a difference of conventions.

The same source's four-vertex path value
\[
\operatorname{FC}_3(P_4;p)=24p^3(1-2p)
\]
is recovered by the general path formula.

## Verification

A standalone definition-level verifier enumerates every partial 3-assignment of \(P_n\) for \(2\le n\le8\), executes the forcing rule, groups successful assignments by initial domain size, and compares the resulting coefficient vector with the closed formula above. All seven path orders agree. In particular, for \(P_3\) the enumerated counts are six successful assignments of domain size two and twelve of domain size three.

The finite check supports but does not replace the proof.

## Literature context and originality

The forced colouring function was introduced by Farr and Morgan in their 2024 preprint / 2025 book chapter on graph polynomials. Their accessible preprint develops the general definition and reduction framework but does not give a path-family formula.

Farr's 2026 paper develops fundamental properties of the forced colouring function, proves a general formula for bipartite graphs when \(\lambda=2\), gives the maximum-degree simplification for sufficiently many colours, and tabulates all connected graphs on at most four vertices. The accessible current version contains no occurrence of a general path \(P_n\) formula. The new theorem above fills exactly the remaining nontrivial colour count \(\lambda=3\) for paths and thereby determines \(\operatorname{FC}_\lambda(P_n;p)\) for every positive integer \(\lambda\).

Targeted searches for forced/forcing 3-colouring of paths, forced colouring polynomials of paths, chromatic forcing on paths, and equivalent partial-colouring formulations found no prior coefficient formula or recurrence matching the theorem above.

The most relevant residual originality risk is G. E. Farr, *On Problems with Short Certificates*, Acta Informatica 31 (1994), 479--502. The 2026 paper cites that work for the result that deciding whether a given partial 3-colouring forces a full 3-colouring is logspace-complete for P. Bibliographic records and that later description were inspected, but the full 1994 article was not inspected here. It could contain path-specific structural observations, although no evidence located in the searches indicates the enumerative path formula above. Unindexed recent work or literature using substantially different terminology remains another residual risk. Originality is therefore asserted only to the best of our knowledge.

## References

1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1 (2026). https://arxiv.org/abs/2609.17108
2. G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746; later published in *Model Theory, Computer Science, and Graph Polynomials* (2025). https://arxiv.org/abs/2406.15746
3. G. E. Farr, *On Problems with Short Certificates*, Acta Informatica 31 (1994), 479--502. Bibliographic record: https://dblp.org/rec/journals/acta/Farr94
