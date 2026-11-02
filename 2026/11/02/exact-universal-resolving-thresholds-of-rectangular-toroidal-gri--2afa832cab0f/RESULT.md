# Exact universal resolving thresholds of rectangular toroidal grids

## Finding

Let \(C_q\) be the simple cycle of order \(q\ge3\). For every pair of integers \(m,n\ge3\), define the rectangular toroidal grid \(T_{m,n}=C_m\square C_n\). Its *metric-dimension threshold* \(\dim_{\mathrm{th}}(G)\) is the smallest integer \(k\) such that every \(k\)-element subset of \(V(G)\) is a resolving set; a set resolves if the distances to its vertices distinguish every two vertices of the graph.

Write \(E(m,n)\) for the maximum cardinality of an equidistance bisector of two distinct vertices of \(T_{m,n}\). Then

\[
\dim_{\mathrm{th}}(T_{m,n})=1+E(m,n),
\]

where the complete closed form is

\[
E(m,n)=\begin{cases}
mn/2,&m,n\text{ both even};\\
(m-1)(n-1)/2+1,&m,n\text{ both odd};\\
2n,&m=4,\ n\text{ odd};\\
2m,&n=4,\ m\text{ odd};\\
m(n-1)/2,&m\ge6\text{ even},\ n\text{ odd};\\
n(m-1)/2,&n\ge6\text{ even},\ m\text{ odd}.
\end{cases}
\]

This classification includes the exact exceptional behavior of four-vertex cycle factors. Whenever neither exceptional line applies, the maximum is attained by the bisector of vertices differing by one step in *both* cycle coordinates. For \(m=4\) and odd \(n\), a pair displaced by two steps in the first coordinate and zero steps in the second attains the larger exceptional maximum (and symmetrically if \(n=4\)).

## Assumptions and scope

All graphs are finite, simple, undirected, connected and unweighted. Cyclic coordinate arithmetic is modulo its respective cycle length. For a pair \(u\ne v\), its bisector is \(B(u,v)=\{z:d(z,u)=d(z,v)\}\). The theorem concerns the *universal* resolving threshold, not the minimum metric dimension and not the equidistant dimension of distance-equalizer sets. Both dimensions \(m,n\) can vary independently and include all cases from three onward.

## Proof

**1. Reduction to largest bisectors.** A subset \(S\) fails to resolve a graph precisely if some distinct \(u,v\) have equal distances from every \(s\in S\), i.e., \(S\subseteq B(u,v)\). Thus the largest size of a nonresolving subset is \(\max_{u\ne v}|B(u,v)|\), proving \(\dim_{\mathrm{th}}(G)=1+\max_{u\ne v}|B(u,v)|\). This general reduction is elementary and is not claimed as new.

**2. One-cycle difference histograms.** Write \(\rho_N(x)=\min(x\bmod N,(-x)\bmod N)\). For an integer shift \(a\) in the range \(1\le a\le\lfloor N/2\rfloor\), put

\[
H_N^a(t)=\left|\left\{x\in\mathbb Z/N\mathbb Z:\rho_N(x)-\rho_N(x-a)=t\right\}\right|.
\]

A direct traversal of the two monotone arcs of the cycle yields the following *complete*, not merely bounded, histograms.

If \(N=2h+1\), then \(H_N^a(-a)=H_N^a(a)=h-a+1\), and \(H_N^a(t)=1\) for every integer \(-a<t<a\); all other values vanish. In particular, the histogram for \(a=1\) has nonzero values \(h,h,1\) at \(t=-1,1,0\), respectively.

If \(N=2h\), then \(H_N^a(-a)=H_N^a(a)=h-a+1\), and \(H_N^a(t)=2\) at each integer \(-a<t<a\) having \(t\equiv a\pmod2\); all other values vanish. In particular, the histogram for \(a=1\) has nonzero values \(h,h\) at \(t=-1,1\).

These formulas include the antipodal shift \(a=N/2\) in an even cycle and the three-cycle boundary. Their totals are \(N\), as required.

**3. A sharp rearrangement bound for pairs that move in both coordinates.** In either parity, the descending rearrangement of \(H_N^a\) is majorized by the descending rearrangement of \(H_N^1\). For an even cycle, the entries of every histogram are bounded by \(h\) and sum to \(2h\), while the \(a=1\) histogram is \((h,h,0,\ldots)\). For an odd cycle, every histogram has at least three positive entries, all entries are at most \(h\), and the sum is \(2h+1\); hence its largest entry is at most \(h\), its two largest sum to at most \(2h\), and its descending rearrangement is majorized by \((h,h,1,0,\ldots)\). These are all the defining partial-sum inequalities for majorization.

Translation and reflection let us take a vertex pair to have displacement \((a,b)\) with \(0\le a\le\lfloor m/2\rfloor\) and \(0\le b\le\lfloor n/2\rfloor\). Cartesian graph distance is the sum of cycle distances. If \(a,b>0\), therefore,

\[
|B((0,0),(a,b))|=\sum_{t\in\mathbb Z}H_m^a(t)H_n^b(-t).
\]

The rearrangement inequality and the preceding two majorizations bound this inner product by the inner product of the descending sequences for \(H_m^1\) and \(H_n^1\). Since both shift-one histograms are supported at \(t=\pm1\), and possibly at \(t=0\), *their original supports already align the largest entries*. Consequently the upper bound is attained at \((a,b)=(1,1)\). Its exact value is

\[
B_{11}(m,n)=\begin{cases}
mn/2,&m,n\text{ even},\\
(m-1)(n-1)/2+1,&m,n\text{ odd},\\
m(n-1)/2,&m\text{ even},\ n\text{ odd},\\
n(m-1)/2,&m\text{ odd},\ n\text{ even}.
\end{cases}
\]

**4. Axis displacements.** If \(a>0\) and \(b=0\), then the bisector count is exactly \(nH_m^a(0)\). The histogram formulas show \(H_N^a(0)=1\) for odd \(N\), and \(H_N^a(0)=2\) for even \(N\) with even \(a\), and zero otherwise. Because every even cycle has a two-step shift, the greatest count among pairs moving *only* in the first coordinate is \(n\) for odd \(m\), and \(2n\) for even \(m\). In the other coordinate it is \(m\) for odd \(n\), and \(2m\) for even \(n\). This treats all nonzero displacements not covered in Step 3.

**5. Comparison and sharpness.** If both orders are odd, \(B_{11}(m,n)\ge\max(m,n)\) because each order is at least three. If both are even, \(B_{11}(m,n)=mn/2\ge2\max(m,n)\) because each order is at least four. For even \(m\ge6\) and odd \(n\ge3\), \(m(n-1)/2\ge2n\) (equivalently, \(m(n-1)\ge4n\)) and \(m(n-1)/2\ge m\); the transposed case is identical. Finally, for \(m=4\) and odd \(n\), \(B_{11}(m,n)=2(n-1)<2n\) and \(2n\ge m\), so an axis displacement \((2,0)\) is strictly extremal; likewise after transposition. The maxima are all attained by the stated displacements, completing the formula for \(E(m,n)\) and thus for the threshold. \(\square\)

## Verification

A self-contained Python standard-library script, `verify_toroidal_threshold.py`, checks the theorem in two different ways. It evaluates every nonzero translation displacement and its exact one-cycle histogram convolution for all \(3\le m,n\le40\) (1,444 graph parameters), and independently rebuilds graph adjacency, performs breadth-first searches from every vertex, and evaluates every vertex-pair bisector for all \(3\le m,n\le10\) (64 graph parameters). Execution of the delivered source yields `VERIFY_OK 1444 full offset-pair histogram cases; 64 independent BFS all-vertex-pair cases`. Finite checks corroborate but do not replace Steps 1–5, which prove the all-parameter result.

## Relationship to prior work

Korivand, Khashyarmanesh and Tavakoli introduced the metric-dimension-threshold terminology and general bisector bound in 2022. Their paper's explicit examples and classification results do not evaluate the largest bisector on a Cartesian product of two cycles. Cáceres and collaborators study the *minimum* size of a resolving set in Cartesian products, including cycle products; this different extremization does not determine a worst-case universal threshold. Gispert-Fernández, Rodríguez-Velázquez and Yero study distance-*equalizer* sets and a different equidistant dimension, including cycle prisms, rather than the largest bisector and universal resolvability of two-cycle products. The present contribution is the explicit all-parity largest-bisector classification and resulting universal threshold, not the general reduction from bisectors to the threshold.

## Limitations

The theorem applies to the ordinary Cartesian product \(C_m\square C_n\) and standard graph distance, with both orders at least three. It does not address weighted, twisted or higher-dimensional tori, or the counts of *all* maximizing displacement types. No claim of independent publication-priority certification is made; literature indexing can be incomplete. Computational checks extend to the finite ranges specified above only.

## References

- M. Korivand, K. Khashyarmanesh and M. Tavakoli, *Metric Dimension Threshold of Graphs*, Journal of Mathematics (first publicly available 2022-09-14), DOI: 10.1155/2022/1838719. Full text: https://onlinelibrary.wiley.com/doi/10.1155/2022/1838719.
- J. Cáceres, C. Hernando, M. Mora, I. M. Pelayo, M. L. Puertas, C. Seara and D. R. Wood, *On the Metric Dimension of Cartesian Products of Graphs*, arXiv:math/0507527 (first posted 2005-07-26), subsequently SIAM Journal on Discrete Mathematics 21 (2007), 423–441; DOI: 10.1137/050641867. Open full text: https://arxiv.org/pdf/math/0507527.
- A. Gispert-Fernández, J. A. Rodríguez-Velázquez and I. G. Yero, *Equidistant Dimension of Cartesian Product Graphs*, Bulletin of the Malaysian Mathematical Sciences Society 49 (2026), article 101; DOI: 10.1007/s40840-026-02088-4. Full text: https://link.springer.com/article/10.1007/s40840-026-02088-4.
