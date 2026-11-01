# A sharp two-phase amplitude bound for integer diffusion on complete bipartite graphs

## Finding

For integers \(a,b\ge 2\), the synchronous integer diffusion game on the labelled complete bipartite graph \(K_{a,b}\) has the following exact orbit-amplitude law. If \(x\in\mathbb Z^{a+b}\) belongs to a primitive two-cycle \(x\mapsto y\mapsto x\), define its **two-phase amplitude** by
\[
\mathcal A(x,y)=\max_{v\in V,\ t\in\{0,1\}}x_v^{(t)}-\min_{v\in V,\ t\in\{0,1\}}x_v^{(t)},\qquad x^{(0)}=x,\quad x^{(1)}=y.
\]
Then
\[
\boxed{\ \max_{\text{primitive two-cycles of }K_{a,b}}\mathcal A=a+b+\max(a,b)-2.\ }
\]
The maximum is attained by an explicit two-cycle for every pair \(a,b\ge2\). Thus, after the unique uniform integer translation that sets the minimum across both phases to zero, **all** primitive two-cycle states fit in the integer alphabet \(\{0,1,\ldots,a+b+\max(a,b)-2\}\), and no smaller universal alphabet suffices. This is a sharp finite-state cutoff for enumerating recurrent configurations up to uniform translation, not an estimate for a transient orbit's amplitude.

## Assumptions and scope

Let \(L\) and \(R\) be disjoint, labelled vertex sets with \(|L|=a\), \(|R|=b\); all edges join \(L\) to \(R\). An integer state \(z\in\mathbb Z^{L\cup R}\) evolves by the parallel rule
\[
(Fz)_v=z_v+\sum_{w\sim v}\operatorname{sgn}(z_w-z_v),\qquad\operatorname{sgn}(m)=\begin{cases}-1&m<0,\\0&m=0,\\1&m>0.\end{cases}
\]
A primitive two-cycle is a pair \(x\ne y=Fx\) with \(Fy=x\). The amplitude ranges over both distinct states, all vertices, and all integer labels; it is invariant under simultaneous uniform translation and interchange of the two phases. The theorem assumes \(a,b\ge2\). Stars with a singleton shore are not included in the sharp formula; their different amplitude classification belongs to the known separate star case.

## Proof

**1. Edge-reversal lemma.** For a finite simple graph and a primitive two-cycle \(x\mapsto y\mapsto x\), orient each edge \(uv\) arbitrarily and write \(s_{uv}(z)=\operatorname{sgn}(z_u-z_v)\). Let \(B\) be the corresponding signed vertex-edge incidence matrix (tail \(+1\), head \(-1\)). Since the update rule is \(Fz=z-Bs(z)\),
\[
B(s(x)+s(y))=0.
\]
Taking the dot product with \(x+y\) gives
\[
0=\sum_{uv\in E}[(x_u-x_v)+(y_u-y_v)]\,[s_{uv}(x)+s_{uv}(y)].
\]
Every summand is nonnegative. It is strictly positive unless the two signs add to zero: if their sum is positive (respectively negative), both nonzero contributing differences have positive (respectively negative) sign. Consequently \(s_{uv}(x)+s_{uv}(y)=0\) for every edge. In each primitive two-cycle every edge either stays tied at both phases or reverses its strict direction at each step. The lemma is proved here for completeness; the general period-at-most-two literature supplies related edge-sign potential methods.

**2. Universal cross-shore bound.** Put \(H=a+b-1\). For an edge \(uv\), the vertex changes in one step have absolute values at most their degrees, whose sum is \(a+b\). If an integer edge gap of magnitude \(d>0\) reverses strictly, the old and new gaps have opposite sign and both magnitude at least one, so \(d+1\le a+b\). If the edge stays tied, its gap is zero. Thus at each phase
\[
|x_u-x_v|\le H,\qquad |y_u-y_v|\le H\qquad(u\in L,\ v\in R).
\]

**3. Uniform two-phase upper bound.** Translate the whole orbit so its minimum across both phases is zero. Interchange the phases if necessary, and suppose first that the minimum is \(x_i=0\) at a vertex \(i\in L\). All entries of \(x\) and \(y\) are then nonnegative. Every \(j\in R\) obeys \(0\le x_j\le H\) by Step 2. The update at \(i\) gives \(0\le y_i\le b\), since all \(x_j\ge0\). For \(j\in R\) with \(x_j=0\), edge reversal forces \(y_j=y_i\le b\); for \(x_j>0\), it forces \(y_j<y_i\le b\). Hence every right-shore value in both phases is at most \(H\), because \(H\ge b\).

Now take any \(k\in L\). If \(x_k<H\), its update is at most \(x_k+b\le H+b-1\). If \(x_k=H\), at least one right-shore neighbor has value at most \(x_k\), so not all \(b\) summands in its update are \(+1\); therefore \(y_k\le H+b-1\) again. In these two cases \(x_k\le H\le H+b-1\). If instead \(x_k>H\), then \(x_k\) is strictly larger than every right-shore value. It loses exactly \(b\) chips, so \(y_k=x_k-b\), and every incident edge reverses to \(y_k<y_j\le b\). Thus \(y_k\le b-1\) and \(x_k\le2b-1\le H+b-1\) (the last inequality uses \(a\ge1\)). Therefore all coordinates of both phases lie in \([0,H+b-1]\).

If the minimum occurs instead in \(R\), swap the shore names in the argument and obtain the bound \(H+a-1\). Combining the two cases yields
\[
\mathcal A(x,y)\le H+\max(a,b)-1=a+b+\max(a,b)-2.
\]
This argument uses no assumption about which vertices attain the maximum, and includes ties and negative initial labels (removed by the harmless uniform translation).

**4. Explicit sharp construction.** By symmetry suppose \(2\le a\le b\), so the maximum vertex degree is \(b\). Give \(a-1\) left vertices value \(0\), one remaining left vertex value \(H-1=a+b-2\), and all \(b\) right vertices value \(H=a+b-1\). Every left label is strictly below every right label. One update adds \(b\) to each left label and subtracts \(a\) from each right label; hence the new left labels are \(b\) and \(H+b-1\), while every right label is \(b-1\). Their inequalities are now strictly reversed, so the second update returns to the original configuration. The two configurations are distinct. The minimum across both phases is \(0\), while the maximum is \(H+b-1\), proving equality. If \(a>b\), interchange the shores in this construction. The theorem follows.

## Verification

The accompanying standalone `verify_diffusion_range.py` recomputes the integer update without symbolic algebra, tests the edge-reversal property and sharp constructions for \(169\) size pairs with \(2\le a,b\le14\), and independently enumerates sorted-shore candidates in an alphabet larger than the predicted cutoff for \((a,b)=(2,2),(2,3),(2,4),(3,3),(3,4)\). These finite searches checked \(261,938\) normalized sorted candidates and found \(1,113\) qualifying primitive two-phase representatives, none exceeding the predicted amplitude and at least one attaining it in each case. The program prints `BIPARTITE_DIFFUSION_WIDTH_ALL_CHECKS_PASSED` on success; its recorded output is included. Exhaustive checking within a finite alphabet does **not** establish the theorem for unbounded integer states or all sizes; Steps 1--4 provide that proof.

## Relationship to prior work

Duffy, Lidbetter, Messinger and Nowakowski introduced this integer diffusion game and proved eventual periodicity on complete bipartite graphs, with bounds depending on the initial configuration. Their discussion of stars and homogeneous-part initial conditions does not state an exact initial-condition-independent amplitude across primitive two-cycle phases. Long and Narayanan later established eventual period one or two for every finite graph by a potential argument. This broader period theorem gives the permissible lengths but does not specify the sharp \(K_{a,b}\) amplitude above. Carlotti and Herrman proved a universal sufficient *initial* chip balance for nonnegativity; that is a different quantity and does not imply this optimal recurrent-orbit range. The present calculation isolates the sharp translation-normalized range on bicliques with two nonsingleton shores.

## Limitations

The result does not classify the number of two-cycle orbits at any conserved chip total, their basins, or their convergence times. It is not a bound on arbitrarily large transient amplitudes. It does not claim a new general period-two theorem, a new edge-sign potential method, or the already studied star case. No independent mathematical audit has been performed, and historical equivalence in literature not identified by the source comparisons remains possible.

## References

1. C. Duffy, T. F. Lidbetter, M. E. Messinger, and R. J. Nowakowski, *A Variation on Chip-Firing: the diffusion game*, arXiv:1609.05792 (first publicly posted 2016-09-19), especially Section 2.3 and Section 3.2. https://arxiv.org/abs/1609.05792
2. J. Long and B. Narayanan, *Diffusion on graphs is eventually periodic*, arXiv:1704.04295 (first publicly posted 2017-04-13), particularly the potential proof in Section 2. https://arxiv.org/abs/1704.04295
3. A. Carlotti and R. Herrman, *Uniform Bounds for Non-negativity of the Diffusion Game*, arXiv:1805.05932 (first publicly posted 2018-05-15), Theorems 1--2. https://arxiv.org/abs/1805.05932
