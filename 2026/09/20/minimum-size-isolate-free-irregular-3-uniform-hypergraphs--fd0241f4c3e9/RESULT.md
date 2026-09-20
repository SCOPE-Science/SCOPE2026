# Minimum size of isolate-free irregular 3-uniform hypergraphs

**Same-model review: passed. Independent audit: not yet performed.**

## Result

A finite simple 3-uniform hypergraph is **irregular** if its vertex degrees are pairwise distinct. It is **isolate-free** if every vertex has positive degree.

For every integer \(n\ge 6\), the minimum number of hyperedges in an isolate-free irregular simple 3-uniform hypergraph on \(n\) vertices is
\[
\boxed{m_3^+(n)=\left\lceil\frac{n(n+1)}6\right\rceil}.
\]

More explicitly, this minimum is attained with degree set
\[
D_n=\begin{cases}
\{1,2,\ldots,n\}, & n\not\equiv 1,4\pmod 6,\\[1mm]
\{1,2,\ldots,n-2,n,n+1\}, & n\equiv 1,4\pmod 6.
\end{cases}
\]
Thus the elementary degree-sum lower bound is sharp for every admissible order, with the smallest possible divisibility correction when \(1+2+\cdots+n\) is not divisible by 3.

## Lower bound

Let \(H\) be an isolate-free irregular 3-uniform hypergraph on \(n\) vertices with \(m\) edges. Its \(n\) degrees are distinct positive integers, so
\[
\sum_{v\in V(H)} d(v)\ge 1+2+\cdots+n=\frac{n(n+1)}2.
\]
Since every edge contributes 3 to the degree sum,
\[
3m=\sum_v d(v)\ge \frac{n(n+1)}2,
\]
and hence
\[
m\ge \left\lceil\frac{n(n+1)}6\right\rceil.
\]

## Sharp construction

Write
\[
M_n=\left\lceil\frac{n(n+1)}6\right\rceil.
\]
We construct, inductively, a simple 3-uniform hypergraph \(H_n\) with \(|E(H_n)|=M_n\) and degree set \(D_n\).

### Base case

For \(n=6\), on vertices \(1,\ldots,6\), take the seven triples
\[
156,\ 246,\ 256,\ 345,\ 346,\ 356,\ 456.
\]
Their vertex degrees are exactly \(1,2,3,4,5,6\), so this is an isolate-free irregular 3-graph with \(M_6=7\) edges.

### Inductive step

Assume \(H_{n-1}\) has already been constructed. Add a new vertex \(x\). Choose a simple graph \(F\) on selected old vertices, and for every edge \(uv\in E(F)\) add the triple \(xuv\). Then
\[
d_{H_n}(x)=|E(F)|,
\qquad
d_{H_n}(v)=d_{H_{n-1}}(v)+d_F(v)
\]
for every old vertex \(v\). Because \(x\) is new and \(F\) is simple, no repeated triple is created.

Set
\[
k=M_n-M_{n-1}.
\]
The value of \(k\) is
\[
k=\begin{cases}
n/3,&n\equiv0,3\pmod6,\\
(n-2)/3,&n\equiv2,5\pmod6,\\
(n+2)/3,&n\equiv1,4\pmod6.
\end{cases}
\]
Label old vertices by their degrees, which are distinct by induction.

#### Case 1: \(n\equiv0,3\pmod6\)

Here \(D_{n-1}=\{1,\ldots,n-1\}\) and \(D_n=\{1,\ldots,n\}\). The old vertices with degrees
\[
k,k+1,\ldots,n-1
\]
number \(n-k=2k\). Let \(F\) be any perfect matching on these \(2k\) vertices. Every listed old degree increases by 1 and the new vertex has degree \(k\), giving exactly \(D_n\).

#### Case 2: \(n\equiv2,5\pmod6\)

Now
\[
D_{n-1}=\{1,\ldots,n-3,n-1,n\},
\qquad D_n=\{1,\ldots,n\}.
\]
The old vertices with degrees
\[
k,k+1,\ldots,n-3
\]
number \(n-2-k=2k\). Take \(F\) to be a perfect matching on these vertices. They increase by 1, the two high degrees \(n-1,n\) are unchanged, and \(x\) has degree \(k\). Again the final degree set is exactly \(D_n\).

#### Case 3: \(n\equiv1,4\pmod6\)

Here \(D_{n-1}=\{1,\ldots,n-1\}\) and
\[
D_n=\{1,\ldots,n-2,n,n+1\}.
\]
Let \(A\) be the old vertices whose degrees are
\[
k,k+1,\ldots,n-3.
\]
Then \(|A|=2k-4\). Let \(u,w\) be the old vertices of degrees \(n-2,n-1\). Choose distinct \(a,b\in A\), which is possible because the first case here is \(n=7\), where \(k=3\). Put into \(F\) the three-edge path
\[
a-u-w-b
\]
and a perfect matching on \(A\setminus\{a,b\}\). Thus \(F\) has
\[
3+(k-3)=k
\]
edges; every vertex of \(A\) has \(F\)-degree 1 and \(u,w\) have \(F\)-degree 2. Consequently the old degrees \(k,\ldots,n-3\) become \(k+1,\ldots,n-2\), while \(n-2,n-1\) become \(n,n+1\), and \(x\) has degree \(k\). This is exactly \(D_n\).

The induction is complete. All degrees in \(D_n\) are positive and distinct, and their sum is \(3M_n\), so the lower bound is attained for every \(n\ge6\).

## Relation to prior literature

Gyárfás, Jacobson, Kinch, Lehel and Schelp introduced and studied irregular uniform hypergraphs in 1992. They proved that irregular \(r\)-uniform hypergraphs exist for \(r\ge3\) and \(n\ge r+3\). Their smallest nontrivial example is a 3-uniform hypergraph on six vertices with seven edges, and they note that their general inductive construction can be altered to remove its possible isolated vertex. The checked section does not optimize the number of edges under the isolate-free requirement.

Behrens et al. (2013) study general \(k\)-graphic degree sequences, giving sufficient conditions and edge-exchange results. Li and Miklós (2023/2025) give constructive realizability conditions for dense irregular 3-uniform degree sequences. Those degree-sequence results provide broader context but concern substantially different regimes from the sparse degree sets used here.

Searches for the exact minimum-size problem, the formula \(\lceil n(n+1)/6\rceil\), the degree sets \(\{1,\ldots,n\}\) and \(\{1,\ldots,n-2,n,n+1\}\), and synonymous irregular/uniform-hypergraph formulations did not locate an equivalent theorem in the checked literature. Originality is therefore claimed only to the best of our knowledge.

## Verification

`artifacts/verify_irregular_3graph.py` implements the recursive construction and checks simplicity, edge count, positivity, pairwise distinctness, degree sums, and the stated target degree sets. The supplied output records successful checks for every \(6\le n\le200\). This finite verification supports the construction but is not used in place of the proof.

## Limitations

- The theorem is specifically about **isolate-free** irregular simple 3-uniform hypergraphs. It does not claim the same minimum when isolated vertices are allowed.
- The result determines the minimum number of edges and gives explicit extremal degree sets and constructions; it does not classify all minimum-size realizations up to isomorphism.
- Originality is to the best of our knowledge. Older or poorly indexed work on 3-graphic sequences, irregular set systems, or sparse hypergraph degree sequences could contain an equivalent statement under different terminology.
- The result is for rank exactly 3. The analogous sharp minimum-size question for general \(r\)-uniform isolate-free irregular hypergraphs is not settled here.

## References

1. A. Gyárfás, M. S. Jacobson, L. Kinch, J. Lehel, R. H. Schelp, *Irregularity Strength of Uniform Hypergraphs*, Journal of Combinatorial Mathematics and Combinatorial Computing 11 (1992), 161–172. https://users.renyi.hu/~gyarfas/Cikkek/61_GyarfasJacobsonKinchLehelSchelp_IrregularityStrengthOfUniformHypergraphs.pdf
2. S. Behrens, C. Erbes, M. Ferrara, S. G. Hartke, B. Reiniger, H. Spinoza, C. Tomlinson, *New Results on Degree Sequences of Uniform Hypergraphs*, Electronic Journal of Combinatorics 20(4) (2013), P14. https://doi.org/10.37236/3414
3. R. Li, I. Miklós, *Dense, irregular, yet always graphic 3-uniform hypergraph degree sequences*, arXiv:2312.00555; later published in Discrete Mathematics. https://arxiv.org/abs/2312.00555
