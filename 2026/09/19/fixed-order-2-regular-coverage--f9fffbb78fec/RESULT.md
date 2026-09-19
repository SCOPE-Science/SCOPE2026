# Exact fixed-order 2-regular coverage in regular graphs

## Result

For a finite graph \(G\), let \(f_2(G)\) be the largest number of vertices covered by a 2-regular subgraph of \(G\). For integers \(r\ge2\) and admissible \(n\) (that is, \(n\ge r+1\) and \(rn\) is even), define
\[
M_r(n)=\min\{f_2(G): G\text{ is a simple }r\text{-regular graph on }n\text{ vertices}\}.
\]

Then
\[
M_r(n)=n \qquad (r\text{ even}),
\]
and for every odd \(r\ge3\) (hence every admissible \(n\) is even),
\[
\boxed{
M_r(n)=n-\max\left\{0,\left\lfloor
\frac{n-2(r+2)}{r^2-3}
\right\rfloor\right\}.
}
\]
Moreover, for every admissible \((r,n)\), the minimum is attained by a connected simple \(r\)-regular graph.

Equivalently, for odd \(r\ge3\) and \(t\ge1\), the smallest order of a simple \(r\)-regular graph whose every 2-regular subgraph omits at least \(t\) vertices is exactly
\[
\boxed{N_r(t)=(r^2-3)t+2(r+2).}
\]
In particular, the first possible order of an odd-regular graph with no spanning 2-factor in this extremal scale is
\[
N_r(1)=(r+1)^2.
\]

For \(r=3\), the formula reduces to the exact cubic result of Choi, Kim, Kostochka, Park, and West:
\[
M_3(n)=\min\left\{n,\left\lceil\frac{5(n+2)}6\right\rceil\right\}.
\]
Thus the new content is the every-order sharpness for general odd \(r\), especially \(r\ge5\), together with a uniform interpolation construction.

## Proof

For even \(r\), Petersen's 2-factor theorem gives a spanning 2-factor in every \(r\)-regular graph, so \(M_r(n)=n\).

Now let \(r\ge3\) be odd. The proof of Theorem 4.1 in Sivashankar's *Nearly Spanning Regular Subgraphs* combines a cut-edge bound with a 2-regular-subgraph lemma to give the following finite-order consequence for every connected simple \(r\)-regular graph \(G\) of order \(n\):
\[
n-f_2(G)
\le
\max\left\{0,\left\lfloor
\frac{n-2(r+2)}{r^2-3}
\right\rfloor\right\}.
\tag{1}
\]
For completeness, the numerical mechanism behind (1) is as follows. If \(c\) is the number of cut-edges, the 2-regular-subgraph estimate used there gives
\[
n-f_2(G)\le \left\lfloor\frac{c-1}{r-1}\right\rfloor
\quad(c>0),
\]
while a bridgeless odd-regular graph has a spanning 2-factor. The sharp O--West cut-edge inequality then implies that having \(c\ge (r-1)t+1\) forces
\[
n\ge (r^2-3)t+2(r+2).
\]
This is exactly (1).

The same bound holds for disconnected simple \(r\)-regular graphs. Indeed, apply (1) to each connected component. Every component with positive omission \(d_i\) has order at least
\[
2(r+2)+(r^2-3)d_i.
\]
If at least one such component exists, summing these inequalities gives
\[
n\ge 2(r+2)+(r^2-3)\sum_i d_i,
\]
which yields (1) for the whole graph. Components with zero omission contribute nothing to the deficiency.

It remains to show equality at every admissible order. Put
\[
a=r^2-3,
\qquad C=2(r+2),
\qquad
t=\max\left\{0,\left\lfloor\frac{n-C}{a}\right\rfloor\right\}.
\]

If \(t=0\), write \(r=2d+1\). On \(\mathbb Z_n\), join every vertex to its translates by
\[
\pm1,\ldots,\pm d,\quad n/2.
\]
Because \(n\ge r+1\), these are distinct neighbours. The resulting connected simple graph is \(r\)-regular and contains the Hamilton cycle formed by the \(\pm1\) edges, so \(f_2=n\).

Assume \(t\ge1\). We first need a one-deficient block.

### One-deficient block lemma

For every odd \(r\ge3\) and every odd \(N\ge r+2\), there exists a simple graph \(B_{r,N}\) on \(N\) vertices with a distinguished vertex \(v\) such that

- \(d(v)=r-1\);
- every other vertex has degree \(r\); and
- \(B_{r,N}\) contains a spanning Hamilton cycle (hence a spanning 2-factor).

To construct it, take a Walecki Hamilton decomposition of \(K_N\). Let \(d=(r-1)/2\). The union of \(d\) Hamilton cycles is an \((r-1)\)-regular spanning graph \(H\). Take one further edge-disjoint Hamilton cycle \(C\). Delete \(v\) from \(C\); the remaining path has even order, so alternate edges form a perfect matching of \(V(K_N)\setminus\{v\}\). Adding that matching to \(H\) raises every degree except \(d(v)\) by one. One of the Hamilton cycles in \(H\) is the required spanning 2-factor.

### Sharp construction

Take a path on \(t\) core vertices (a single vertex when \(t=1\)). At each core vertex, attach enough one-deficient blocks by a single bridge so that the core vertex has total degree \(r\). If its degree inside the core path is \(q\in\{0,1,2\}\), attach \(r-q\) blocks there. The total number of blocks is
\[
(r-2)t+2.
\]
All core-path edges and all attachment edges are bridges.

Initially give every block order \(r+2\). The total order is then
\[
t+((r-2)t+2)(r+2)
=(r^2-3)t+2(r+2)=at+C.
\]
Since \(t=\lfloor(n-C)/a\rfloor\), the excess
\[
e=n-(at+C)
\]
satisfies \(0\le e<a\). Both \(n\) and \(at+C\) are even, so \(e\) is even. Enlarge one block from order \(r+2\) to order \(r+2+e\), which remains odd; the block lemma applies. Leave all other blocks at order \(r+2\).

The resulting graph is connected, simple, \(r\)-regular, and has exactly \(n\) vertices. No bridge lies in a cycle, so none of the \(t\) core vertices can belong to a 2-regular subgraph. Hence
\[
f_2(G)\le n-t.
\]
On the other hand, the union of one spanning Hamilton cycle from each attached block is a 2-regular subgraph covering every non-core vertex, so
\[
f_2(G)=n-t.
\]
Together with (1), this proves the formula.

## Relation to prior work

Sivashankar (2026) proves the sharp asymptotic value
\[
\delta_2(r)=\frac1{r^2-3}
\]
for every odd \(r\ge3\). The finite-order upper inequality used above is already contained in the proof of that theorem, and the paper gives sharp constructions at the arithmetic progression
\[
n=(r^2-3)t+2(r+2).
\]
The contribution here is not that inequality or those endpoint examples: it is the proof that the same floor bound is attained at **every admissible order**, using variable-order one-deficient Walecki blocks. This converts the asymptotic result into an exact fixed-order extremal function.

The case \(r=3\) is already completely known from Choi--Kim--Kostochka--Park--West (2019). The present formula specializes exactly to their result. Older work of O and West gives the sharp cut-edge inequality used in the finite-order upper bound, while van den Heuvel and Toft (2026) survey and sharpen structural results on 2-factors in regular graphs.

## Verification

`artifacts/verify_constructions.py` is a standalone standard-library Python verifier. It explicitly constructs the Walecki blocks and the connected extremal graphs, then checks simplicity, regularity, connectivity, the predicted bridge count, and an explicit 2-regular subgraph on exactly \(n-t\) vertices. It also checks arithmetic agreement with the known cubic formula. The recorded output is in `artifacts/verification.txt`.

The computation is supporting evidence only; the theorem is proved above.

## Originality and limitations

The originality assessment is **to the best of our knowledge**. Searches were made for exact fixed-order versions of the largest-2-regular-subgraph problem, odd-regular 2-factor deficiency, cut-edge formulations, and equivalent regular-factor terminology. The recent Sivashankar preprint and the exact cubic paper were examined specifically to separate their claims from the every-order statement here.

The main residual risk is that the interpolation may be implicit in older factor literature under a different formulation, or may appear in a very recent update or parallel work. In particular, the finite-order upper bound itself is not new, and the cubic specialization is not new. No claim is made that the threshold \((r+1)^2\) in isolation was previously unknown; the originality claim is the full exact fixed-order law for general odd degree and its all-orders sharp construction.

## References

1. V. Sivashankar, *Nearly Spanning Regular Subgraphs*, arXiv:2609.19777 (2026), https://arxiv.org/abs/2609.19777.
2. I. Choi, R. Kim, A. V. Kostochka, B. Park, and D. B. West, *Largest 2-Regular Subgraphs in 3-Regular Graphs*, Graphs and Combinatorics 35 (2019), 805--813, https://doi.org/10.1007/s00373-019-02021-6; arXiv:1903.08795.
3. S. O and D. B. West, *Balloons, Cut-Edges, Matchings, and Total Domination in Regular Graphs of Odd Degree*, Journal of Graph Theory 64 (2010), 116--131, https://doi.org/10.1002/jgt.20443.
4. J. van den Heuvel and B. Toft, *2-Factors in Graphs*, Electronic Journal of Combinatorics 33 (2026), P2.40, https://doi.org/10.37236/14739.
