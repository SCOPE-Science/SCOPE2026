# Exact forced-colouring functions at maximum degree two

## Statement

For an integer \(\lambda\ge 1\), let \(\mathrm{FC}_\lambda(G;p)\) be the forced-colouring function: independently at each vertex, each specific colour has probability \(p\), the vertex is left uncoloured with probability \(1-\lambda p\), and then the local forcing rule repeatedly colours an uncoloured vertex when exactly \(\lambda-1\) distinct colours occur on its neighbours.

The nontrivial case for graphs of maximum degree at most two is \(\lambda=3\). Put
\[
F_n(p)=\mathrm{FC}_3(P_n;p).
\]
Then
\[
F_1=3p,\qquad F_2=6p^2,
\]
and, for every \(n\ge3\),
\[
\boxed{F_n=2pF_{n-1}+2p(1-3p)F_{n-2}.}
\]

For cycles define two auxiliary sequences by
\[
A_0=2,\quad A_1=2p,\qquad
A_n=2pA_{n-1}+2p(1-3p)A_{n-2},
\]
and
\[
B_0=2,\quad B_1=-p,\qquad
B_n=-pB_{n-1}-p(1-3p)B_{n-2}.
\]
Then, for every \(n\ge3\),
\[
\boxed{\mathrm{FC}_3(C_n;p)=A_n+2B_n.}
\]
In particular,
\[
\mathrm{FC}_3(P_3;p)=6p^2(1-p),
\]
\[
\mathrm{FC}_3(C_3;p)=6p^2(3-8p),\qquad
\mathrm{FC}_3(C_4;p)=6p^2(2-8p+9p^2).
\]

Consequently the forced-colouring function is explicit for every graph \(G\) with \(\Delta(G)\le2\) and every positive integer \(\lambda\). If the components have orders \(n_1,\dots,n_k\), then:

1. \(\lambda=1\): \(\mathrm{FC}_1(G;p)=1\) if \(G\) is edgeless, and \(0\) otherwise.
2. \(\lambda=2\): if \(G\) is not bipartite, then \(\mathrm{FC}_2(G;p)=0\); if \(G\) is bipartite, then
   \[
   \boxed{\mathrm{FC}_2(G;p)=2^k\prod_{i=1}^k\left((1-p)^{n_i}-(1-2p)^{n_i}\right).}
   \]
   This formula includes isolated vertices.
3. \(\lambda=3\): multiply the path and cycle factors above over the components.
4. \(\lambda\ge4\):
   \[
   \mathrm{FC}_\lambda(G;p)=P(G;\lambda)p^{|V(G)|},
   \]
   with \(P(P_n;\lambda)=\lambda(\lambda-1)^{n-1}\) and \(P(C_n;\lambda)=(\lambda-1)^n+(-1)^n(\lambda-1)\).

Thus evaluation on maximum-degree-two graphs is linear in the number of vertices once the component lengths are known, despite the recent general \(\#P\)-hardness theorem for every fixed \(\lambda\ge3\) and every fixed \(p\in(0,\lambda^{-1}]\).

There is also an exact minimum-domain consequence. Among partial 3-assignments that force a 3-colouring, the minimum possible domain size is
\[
\boxed{\left\lfloor\frac n2\right\rfloor+1\quad\text{for }P_n,}
\qquad
\boxed{\left\lceil\frac n2\right\rceil\quad\text{for }C_n.}
\]
For a disjoint union, these minima add over the components.

## Proof

### 1. Successful partial 3-assignments on paths and cycles

Fix a proper 3-colouring \(g\) of a path or cycle. If a vertex of degree two is initially uncoloured, then it can be forced exactly when its two neighbours are coloured with two distinct colours. An endpoint of a path can never be forced with three available colours, so both endpoints must initially be coloured.

Moreover, two adjacent initially uncoloured vertices can never initiate forcing: each lacks one of its two coloured neighbours. Hence a partial assignment forces \(g\) precisely when it is obtained by deleting an independent set \(U\) of eligible degree-two vertices from \(g\), where eligibility means that the two neighbours of the deleted vertex have distinct colours. All vertices of \(U\) are then forced immediately. Therefore successful partial assignments are counted without multiplicity by pairs \((g,U)\) of this type.

Write colours as elements of \(\mathbb Z_3\). Along each oriented edge of a proper 3-colouring let
\[
s_i=g(v_{i+1})-g(v_i)\in\{+1,-1\}.
\]
An internal vertex \(v_i\) is eligible exactly when
\[
s_{i-1}=s_i.
\]
Indeed, its two neighbours have the same colour exactly when \(s_{i-1}+s_i=0\) in \(\mathbb Z_3\), which is the opposite-sign case.

Put
\[
z=\frac{1-3p}{p}.
\]
After factoring out \(p^n\), each deleted vertex contributes a factor \(z\).

### 2. Paths

For a sign word of length \(k\), let \(R_k(z)\) be the total weight of independent subsets of equality positions \(i\) with \(s_{i-1}=s_i\), weighting each selected position by \(z\), summed over all sign words with the first sign fixed. Directly exposing the last sign gives
\[
R_0=1,\qquad R_1=2,
\]
and
\[
R_k=2R_{k-1}+2zR_{k-2}\qquad(k\ge2).
\]
There are three choices for the initial colour, so
\[
F_n=3p^nR_{n-1}\!\left(\frac{1-3p}{p}\right).
\]
Multiplying the recurrence by the appropriate power of \(p\) yields
\[
F_n=2pF_{n-1}+2p(1-3p)F_{n-2}.
\]

### 3. Cycles

For a cycle, a sign word \((s_1,\ldots,s_n)\in\{\pm1\}^n\) comes from a proper 3-colouring exactly when
\[
\sum_{i=1}^n s_i\equiv0\pmod3.
\]
The selected equality positions must also form an independent set cyclically.

Use states \((s_i,u_i)\in\{+1,-1\}\times\{0,1\}\), where \(u_i=1\) means that the vertex between signs \(s_{i-1}\) and \(s_i\) is deleted. A transition to \(u_i=1\) is permitted exactly when the preceding deletion bit is zero and the two signs agree. With state order \((+,0),(+,1),(-,0),(-,1)\), the transfer matrix is
\[
M_t=
\begin{pmatrix}
 t&tz&t^{-1}&0\\
 t&0&t^{-1}&0\\
 t&0&t^{-1}&t^{-1}z\\
 t&0&t^{-1}&0
\end{pmatrix}.
\]
Its characteristic polynomial is
\[
x^2\left[x^2-(t+t^{-1})x-z\big((t+t^{-1})^2-2\big)\right].
\]
Let \(\omega^3=1\), \(\omega\ne1\). A root-of-unity filter enforces the closure condition \(\sum s_i\equiv0\pmod3\). The three choices of starting colour cancel the factor \(1/3\) in that filter, giving
\[
\mathrm{FC}_3(C_n;p)
=p^n\left(\operatorname{tr}M_1^n+\operatorname{tr}M_\omega^n+\operatorname{tr}M_{\omega^2}^n\right).
\]
For \(t=1\), \(t+t^{-1}=2\), so the nonzero-eigenvalue power sum satisfies
\[
L_n=2L_{n-1}+2zL_{n-2},\quad L_0=2,\ L_1=2.
\]
For \(t=\omega\) or \(\omega^2\), \(t+t^{-1}=-1\), giving
\[
L_n=-L_{n-1}-zL_{n-2},\quad L_0=2,\ L_1=-1.
\]
Restoring the powers of \(p\) gives exactly the stated \(A_n\) and \(B_n\) recurrences.

### 4. All values of \(\lambda\) when \(\Delta\le2\)

Multiplicativity over disjoint unions reduces the problem to connected paths and cycles. For \(\lambda=1\), the statement is immediate. For \(\lambda=2\), a connected bipartite component is forced exactly when at least one vertex is initially coloured consistently with one of its two 2-colourings. Therefore a component of order \(m\), including \(m=1\), contributes
\[
2\left((1-p)^m-(1-2p)^m\right).
\]
An odd cycle contributes zero. For \(\lambda\ge4\), every vertex has degree less than \(\lambda-1\), so no initially uncoloured vertex can ever be forced; only total proper colourings contribute, yielding \(P(G;\lambda)p^n\).

### 5. Minimum forcing domains

On \(P_n\), both endpoints must be initially coloured and the uncoloured vertices form an independent subset of the \(n-2\) internal vertices, so at most \(\lceil(n-2)/2\rceil\) vertices can be omitted. This bound is attained by taking all edge signs equal and choosing a maximum independent set of eligible internal vertices. Hence the minimum domain has size
\[
n-\left\lceil\frac{n-2}{2}\right\rceil=\left\lfloor\frac n2\right\rfloor+1.
\]
On \(C_n\), at most \(\lfloor n/2\rfloor\) vertices can be omitted. A maximum independent set of vertices can be made eligible by a proper 3-colouring: in sign language, require equal signs across each omitted vertex and choose the remaining signs so their total is \(0\) modulo \(3\). Such a choice exists for every \(n\ge3\). Thus the minimum domain has size \(\lceil n/2\rceil\).

## Relation to the recent literature

Farr's 15 September 2026 preprint introduces a systematic study of \(\mathrm{FC}_\lambda\), proves basic identities and examples, and proves that evaluation is \(\#P\)-hard for each fixed \(\lambda\ge3\) and \(p\in(0,\lambda^{-1}]\). The earlier Farr--Morgan work introduced the polynomial and singled out \(\mathrm{FC}_3\) for study. Neither inspected source gives path/cycle family formulae or the maximum-degree-two classification above.

There are two consistency corrections worth recording. Farr--Morgan's earlier paper gives
\[
\mathrm{FC}_3(K_{1,2};p)=6p^2(1-p),
\]
which agrees with the path recurrence. Proposition 6 of arXiv:2609.17108v1 instead displays \(6p^2(1-2p)\); that displayed value also conflicts with the same paper's identity \(3^n\mathrm{FC}_3(G;1/3)=P(G;3)\). Likewise, Theorem 7 of that v1 gives a zero branch for bipartite graphs having an isolated vertex. Multiplicativity and \(\mathrm{FC}_2(K_1;p)=2p\) show that the product formula above extends across isolated components instead.

## Verification

`artifacts/verify_fc3_degree2.py` independently enumerates every partial assignment and simulates forcing from the definition for paths through order 8 and cycles through order 8. It reconstructs each polynomial from the successful-domain counts, compares it with the recurrences, and checks the specialization \(3^n\mathrm{FC}_3(G;1/3)=P(G;3)\). It also checks the corrected \(\lambda=2\) formula on connected and disconnected bipartite examples including isolated vertices. The recorded output is in `artifacts/verification.txt`.

Finite verification supports but does not replace the general proof.

## Originality and limitations

To the best of our knowledge, the exact path and cycle recurrences, the resulting all-\(\lambda\) classification for maximum-degree-two graphs, and the minimum-domain formulae above have not appeared previously. Searches included `forced colouring function`, `forced 3-colouring polynomial`, `forced 3-coloring polynomial`, `path`, `cycle`, and `maximum degree 2`, together with the two primary sources and their terminology. The 2025 Springer chapter corresponding to the 2024 Farr--Morgan preprint was identified by DOI but was not separately checked line-by-line; the open preprint's forced-colouring section was inspected. If the final chapter added family formulae absent from that version, the originality assessment would need revision. The invariant is recent, so unindexed parallel work remains a residual risk.

The result is restricted to maximum degree two. It does not provide a tractable algorithm for the general \(\lambda=3\) problem.

## References

1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, 15 September 2026. https://arxiv.org/abs/2609.17108
2. G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746; published in *Model Theory, Computer Science, and Graph Polynomials*, Trends in Mathematics, Springer, 2025, Chapter 18. https://arxiv.org/abs/2406.15746
3. G. Farr and K. Morgan, published chapter DOI: https://doi.org/10.1007/978-3-031-86319-6_18
