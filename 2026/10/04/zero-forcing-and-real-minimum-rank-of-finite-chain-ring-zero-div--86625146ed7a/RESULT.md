# Zero forcing and real minimum rank of finite chain-ring zero-divisor graphs

## Finding

Let \(R\) be a finite commutative chain ring with maximal ideal \(\mathfrak m=(\pi)\), residue-field order \(q=|R/\mathfrak m|\), and nilpotency length \(\ell\ge2\). For the standard zero-divisor graph \(\Gamma(R)\) on the nonzero zero-divisors, put \(N=q^{\ell-1}-1\). If \((q,\ell)=(2,2)\), then \(\Gamma(R)=K_1\), so \(Z(\Gamma(R))=M(\Gamma(R))=1\) and \(\operatorname{mr}(\Gamma(R))=0\). In every other case, over the real symmetric minimum-rank model, \[Z(\Gamma(R))=M(\Gamma(R))=q^{\ell-1}-\ell=N-(\ell-1),\qquad \operatorname{mr}(\Gamma(R))=\ell-1.\] Thus, outside the one-vertex boundary, the real minimum rank of the zero-divisor graph is exactly one less than the nilpotency length.

In particular, a graph inverse-eigenvalue invariant recovers the Loewy length:
\[
\ell=\operatorname{mr}(\Gamma(R))+1
\]
outside the one-vertex boundary.

## Assumptions and scope

Let \(R\) be a finite commutative chain ring. Thus \(R\) is local, its maximal ideal is principal,
\[
\mathfrak m=(\pi),
\]
and for some integer \(\ell\ge2\),
\[
\mathfrak m^\ell=0,\qquad \mathfrak m^{\ell-1}\ne0.
\]
Write
\[
q=|R/\mathfrak m|.
\]
The vertices of \(\Gamma(R)\) are the nonzero zero-divisors, namely
\[
\mathfrak m\setminus\{0\}.
\]

For \(1\le i\le\ell-1\), let
\[
V_i=\mathfrak m^i\setminus\mathfrak m^{i+1}.
\]
Every vertex lies in exactly one \(V_i\), and
\[
|V_i|=(q-1)q^{\ell-i-1}.
\]
If \(x\in V_i\) and \(y\in V_j\), then
\[
xy=0
\quad\Longleftrightarrow\quad
i+j\ge\ell.
\tag{1}
\]

For a finite simple graph \(G\), let \(\mathcal S(G)\) be the real symmetric matrices whose off-diagonal nonzero pattern is exactly \(G\). Then
\[
\operatorname{mr}(G)=\min_{A\in\mathcal S(G)}\operatorname{rank}A,
\qquad
M(G)=|V(G)|-\operatorname{mr}(G).
\]
The standard zero forcing inequality is
\[
M(G)\le Z(G).
\]

## Proof

The number of vertices is
\[
N=|\mathfrak m|-1=q^{\ell-1}-1.
\]

First assume \((q,\ell)\ne(2,2)\). Put
\[
m=\ell-1.
\]
Define the \(m\times m\) symmetric matrix
\[
H_{ij}=
\begin{cases}
1,&i+j\ge\ell,\\
0,&i+j<\ell,
\end{cases}
\qquad 1\le i,j\le m.
\]
After reversing the order of its columns, \(H\) becomes triangular with every diagonal entry equal to \(1\). Hence
\[
\operatorname{rank}H=m.
\tag{2}
\]

Let \(P\) be the \(m\times N\) layer-incidence matrix: the column of a vertex in \(V_i\) is the \(i\)-th standard basis vector. Set
\[
A=P^\mathsf{T}HP.
\]
If \(x\in V_i\) and \(y\in V_j\) are distinct, then
\[
A_{xy}=H_{ij},
\]
so by (1)
\[
A_{xy}\ne0
\quad\Longleftrightarrow\quad
xy=0.
\]
Therefore
\[
A\in\mathcal S(\Gamma(R)).
\]
Every layer is nonempty, so \(P\) has row rank \(m\). Since \(H\) is nonsingular, (2) gives
\[
\operatorname{rank}A=m=\ell-1.
\]
Consequently
\[
M(\Gamma(R))\ge N-(\ell-1).
\tag{3}
\]

We now exhibit a zero forcing set of exactly this size. Initially leave one representative
\[
u_i\in V_i
\]
white for each \(1\le i\le\ell-1\), and color every other vertex blue.

For each
\[
1\le i\le\ell-2,
\]
the layer \(V_i\) has at least two vertices because
\[
|V_i|=(q-1)q^{\ell-i-1}\ge2.
\]
Choose a blue vertex \(x_i\in V_i\).

The blue vertex \(x_1\) is adjacent, among the white representatives, only to \(u_{\ell-1}\), so
\[
x_1\longrightarrow u_{\ell-1}.
\]
After \(u_{\ell-1},\ldots,u_{\ell-i+1}\) have been forced blue, the vertex \(x_i\) has exactly one remaining white neighbor, namely \(u_{\ell-i}\). Thus successively
\[
x_i\longrightarrow u_{\ell-i}
\qquad(1\le i\le\ell-2).
\]
At this point only \(u_1\) remains white. The now-blue vertex \(u_{\ell-1}\) is adjacent to every layer, so it forces \(u_1\).

Hence
\[
Z(\Gamma(R))\le N-(\ell-1).
\tag{4}
\]
Combining (3), (4), and \(M(G)\le Z(G)\),
\[
N-(\ell-1)
\le
M(\Gamma(R))
\le
Z(\Gamma(R))
\le
N-(\ell-1).
\]
Therefore
\[
Z(\Gamma(R))=M(\Gamma(R))=N-(\ell-1)=q^{\ell-1}-\ell
\]
and
\[
\operatorname{mr}(\Gamma(R))=\ell-1.
\]

It remains to check the boundary \((q,\ell)=(2,2)\). Then
\[
|\mathfrak m\setminus\{0\}|=1,
\]
so \(\Gamma(R)=K_1\). Its unique vertex must initially be blue, hence
\[
Z(K_1)=1.
\]
The zero \(1\times1\) matrix belongs to \(\mathcal S(K_1)\), so
\[
\operatorname{mr}(K_1)=0,\qquad M(K_1)=1.
\]

## Verification

The accompanying `verify.py` constructs the valuation-layer graph directly from the layer sizes and the rule \(i+j\ge\ell\).

For representative pairs
\[
(q,\ell)\in
\{(2,2),(3,2),(5,2),(2,3),(3,3),(2,4),(3,4),(2,5)\},
\]
it verifies the complete off-diagonal pattern of the matrix \(P^\mathsf{T}HP\), computes the witness rank exactly over rational arithmetic, and replays the explicit forcing construction. Whenever the graph has at most \(15\) vertices, it exhaustively enumerates all subsets to verify the exact zero forcing number independently.

Exact replay output:

```text
q=2, ell=2: K1 boundary, Z=1, mr=0
q=3, ell=2: n=2, exhaustive Z=1, min_sets=2, witness_rank=1, forces=1
q=5, ell=2: n=4, exhaustive Z=3, min_sets=4, witness_rank=1, forces=1
q=2, ell=3: n=3, exhaustive Z=1, min_sets=2, witness_rank=2, forces=2
q=3, ell=3: n=8, exhaustive Z=6, min_sets=12, witness_rank=2, forces=2
q=2, ell=4: n=7, exhaustive Z=4, min_sets=8, witness_rank=3, forces=3
q=3, ell=4: n=26, constructed Z=23, witness_rank=3, forces=3
q=2, ell=5: n=15, exhaustive Z=11, min_sets=64, witness_rank=4, forces=4
VERIFY_OK
```

The finite computations are corroborative only. The arbitrary-\((q,\ell)\) theorem follows from the valuation-layer description, the anti-triangular rank witness, the explicit forcing sequence, and the general inequality \(M(G)\le Z(G)\).

## Relationship to prior work

Spiroff and Wickham study zero-divisor graphs through annihilator-equivalence classes and list primary Mathematics Subject Classification \(13A15\). Their full public text develops annihilator compression and basic zero-divisor-graph structure; searches of the inspected PDF found no occurrence of “zero forcing” or “minimum rank.”

Rattanakangwanwong and Meemark study adjacency-matrix rank, determinant, and eigenvalues of zero-divisor graphs of finite chain rings and principal ideal rings. Their published abstract uses “rank” in the ordinary adjacency-matrix sense. The present minimum-rank statement is different: the diagonal and nonzero edge weights vary over all real symmetric matrices with the same graph pattern.

The general inequality \(M(G)\le Z(G)\) and the graph minimum-rank model come from the AIM Minimum Rank — Special Graphs Work Group. The ring-specific contribution here is the exact rank-\((\ell-1)\) pattern matrix and the matching forcing process.

## Limitations

The theorem concerns finite commutative chain rings. It does not claim the same formula for arbitrary finite local rings or nonlocal principal ideal rings.

The minimum rank is over real symmetric matrices. Other coefficient fields can behave differently.

The graph \(K_1\) arising from \((q,\ell)=(2,2)\) is a genuine boundary because its minimum rank is \(0\), not \(\ell-1\).

The proof determines the minimum zero forcing number but does not classify all minimum zero forcing sets.

A plausible later source on adjacency spectra of finite chain-ring zero-divisor graphs was identifiable only through bibliographic and abstract material in the available access path. That source does not state a graph minimum-rank result in its abstract, but the unavailable full text remains a residual comparison risk.

## References

1. S. Spiroff and C. Wickham, “A zero divisor graph determined by equivalence classes of zero divisors,” arXiv:0801.0086, first posted 29 December 2007; later published in *Communications in Algebra* 39 (2011), 2338–2348. DOI: 10.1080/00927872.2010.488675.
2. J. Rattanakangwanwong and Y. Meemark, “Eigenvalues of zero divisor graphs of principal ideal rings,” *Linear and Multilinear Algebra* 70 (2022), 5445–5459. DOI: 10.1080/03081087.2021.1917501.
3. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
