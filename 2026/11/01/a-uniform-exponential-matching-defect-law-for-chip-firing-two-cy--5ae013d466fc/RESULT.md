# A uniform exponential matching-defect law for chip-firing two-cycles

## Finding

Let \(G_{N,k}\) be the graph obtained from the simple complete graph \(K_N\) by removing any specified matching of \(k\) edges. Let \(Q_{N,k}\) be the number of distinct primitive temporal two-cycle orbits of the **ordinary synchronous degree-threshold parallel chip-firing map** on \(G_{N,k}\), with nonnegative integer chip numbers and each two-configuration orbit counted once. For all integers \(N\ge4\), \(0\le k\le\lfloor N/2\rfloor\), the counts satisfy an exact finite binomial sum stated below, and the following *uniform* asymptotic law holds as \(N\to\infty\):

\[
\boxed{\sup_{0\le k\le\lfloor N/2\rfloor}\left|\frac{Q_{N,k}}{Q_{N,0}}-\exp\!\left(-\frac{2k}{N}\right)\right|=O(N^{-1}).}
\]

The constant implicit in the error is absolute, independent of \(k\). Thus, for any matching sequence with \(k/N\to\theta\in[0,1/2]\), the orbit-count ratio tends to \(e^{-2\theta}\). For a deleted perfect matching (even \(N\)), the ratio tends to \(e^{-1}\), despite removing only \(N/2\) of the \(\binom N2\) original edges. This is a ratio of **numbers of primitive periodic orbits**, not a probability that a randomly chosen chip configuration has period two.

To state the exact count, put \(r=N-2k\). For integers \(0\le s\le k\), \(0\le p\le k-s\), \(0\le t\le r\), define \(a=s+2p+t\), \(b=N-a\). Then

\[
\boxed{
Q_{N,k}=\frac12\sum_{s=0}^{k}\sum_{p=0}^{k-s}\sum_{t=0}^{r}
\mathbf1_{\{1\le a\le N-1\}}
\binom{k}{s}2^s\binom{k-s}{p}\binom rt
 b^{a-s}a^{b-s}\big((a-1)(b-1)\big)^s.}
\]

A zero exponent means an empty product, including when its base is zero. In particular,

\[
Q_{N,0}=\frac12\sum_{a=1}^{N-1}\binom Na (N-a)^a a^{N-a}.
\]

For example, when \(N=6\), the counts for \(k=0,1,2,3\) respectively are \(11160,7440,5020,3400\). For \(N=8\) they are \(4059328,3044496,2289168,1724744,1301832\) for \(k=0,1,2,3,4\), respectively.

## Assumptions and scope

The graph is finite, simple, undirected, connected, and labelled; \(N\ge4\) and \(k\) deleted edges are pairwise vertex-disjoint. For every vertex \(v\), let \(d_v\) be its graph degree and \(x_v\in\mathbb Z_{\ge0}\) its chip number. In each synchronous update, a vertex fires exactly when \(x_v\ge d_v\), sending one chip to each neighbor. Thus

\[
(Fx)_v=x_v-d_v\mathbf1_{\{x_v\ge d_v\}}
+\sum_{u\sim v}\mathbf1_{\{x_u\ge d_u\}}.
\]

The number \(Q_{N,k}\) counts distinct orbits \(\{x,Fx\}\) satisfying \(F^2x=x\) and \(Fx\ne x\). No assertion is made about the lengths of other possible periods, the transient time of arbitrary initial states, or attraction-basin sizes. Because the number of chip configurations is infinite without a conserved-total restriction, the asserted finite count pertains only to the primitive two-cycles, whose chip ranges are proved finite below.

## Proof

**1. Exactly one firing per vertex in a primitive two-cycle.** Suppose \(x\ne Fx\) but \(F^2x=x\). The two-step change is the negative graph Laplacian applied to the vector \(f\) of each vertex's number of firings in these two updates. Hence \(Lf=0\). The graph is connected, so \(f\) is constant, and each entry lies in \(\{0,1,2\}\). If this constant is zero, all vertices wait at both steps, leaving the configuration unchanged; if it is two, every vertex fires at both steps, again leaving it unchanged. Therefore the constant is one. The firing vertices at the first update form one shore \(A\) of a nontrivial cut \(A\sqcup B\); at the second update exactly \(B\) fires.

For \(v\in V\), write \(c_v(A)\) for its number of neighbors across the cut. If \(v\in A\), its first-step chip loss equals \(c_v\), so the two firing inequalities require \(d_v\le x_v\le d_v+c_v-1\). If \(v\in B\), its first-step chip gain is \(c_v\), so the inequalities require \(d_v-c_v\le x_v\le d_v-1\). Thus the cut supports exactly \(\prod_v c_v\) labelled first-phase configurations when every \(c_v\ge1\), and none otherwise. Each such configuration returns after the next synchronous update, since the second firing phase exchanges the two shores. Every primitive two-cycle is counted twice, once from each temporal phase. Consequently

\[
Q(G)=\frac12\sum_{\varnothing\ne A\subsetneq V(G)}\prod_{v\in V(G)} c_v(A).
\]

This general cut identity is a counting mechanism, not the asymptotic contribution asserted above.

**2. Matchings give the exact sum.** Fix a shore \(A\) with \(a\) vertices and complement \(B\) of size \(b\). Let \(s\) be the number of deleted matching edges separated by the cut. For the \(s\) separated pairs, both endpoints lose one cross-cut neighbor; all other vertices retain their complete-graph cross degrees. Hence

\[
\prod_vc_v(A)=b^{a-s}a^{b-s}((a-1)(b-1))^s.
\]

To select the cut, choose the \(s\) separated deleted pairs and which endpoint of each is in \(A\); next choose \(p\) of the remaining deleted pairs wholly inside \(A\); finally choose \(t\) of the \(r=N-2k\) unmatched vertices inside \(A\). Their numbers are respectively \(\binom ks2^s\), \(\binom{k-s}p\), and \(\binom rt\). The condition \(a=s+2p+t\) gives precisely the displayed formula, including correct zero weights for a shore with an isolated cross-cut vertex.

**3. Weighted cut measure.** For the complete graph let \(W_N(A)=b^a a^b\) for nontrivial shores, and use the probability measure on these shores with mass proportional to \(W_N(A)\). Let \(S(A)\) be the number of deleted matching edges separated by \(A\). The exact cut identity yields

\[
\frac{Q_{N,k}}{Q_{N,0}}=\mathbb E_N\!\left[\left(1-\frac1a\right)^{S(A)}\left(1-\frac1b\right)^{S(A)}\right].
\]

The expression is defined as the cross-degree ratio; if \(a=1\) or \(b=1\), the actual product (which is zero when a deleted matching edge crosses that shore) is used. When \(S=0\), each factor is interpreted as one.

The cut size concentrates exponentially about half the vertices. Indeed, writing \(u=a/N\) and \(H(u)=-u\log u-(1-u)\log(1-u)\), the bound \(\binom Na\le e^{NH(u)}\) gives

\[
\binom Na b^a a^b \le N^N e^{N g(u)},\qquad
g(u)=(2u-1)\log\frac{1-u}{u}.
\]

For \(u\notin[1/4,3/4]\), \(g(u)\le-\frac12\log3\). A central binomial term is at least \(N^N/(4(N+1))\), including odd \(N\). Therefore, for the weighted measure,

\[
\Pr_N\left(\min(a,b)<N/4\right)
\le4N(N+1)3^{-N/2}.
\]

**4. Uniform conditional moment estimate.** Conditional on \(a\), the shore \(A\) is a uniformly random \(a\)-element subset. For a fixed deleted matching edge and two distinct such edges, respectively, the split probabilities are

\[
p_1=\frac{2ab}{N(N-1)},\qquad
p_2=\frac{4a(a-1)b(b-1)}{N(N-1)(N-2)(N-3)}.
\]

Consequently \(\mathbb E[S\mid a]=kp_1\). For \(a,b\ge N/4\),

\[
p_2-p_1^2=O(N^{-1}),\qquad
\operatorname{Var}(S\mid a)=O(k+k^2/N)=O(N),
\]

uniformly for \(0\le k\le N/2\). Put \(Y=S(1/a+1/b)\). The cancellation

\[
\boxed{\mathbb E[Y\mid a]=\frac{2k}{N-1}}
\]

is exact and independent of the cut size. Moreover, \(\operatorname{Var}(Y\mid a)=O(N^{-1})\) uniformly on the central range. Since \(e^{-y}\) has second derivative at most one for \(y\ge0\), Taylor's theorem gives

\[
\mathbb E[e^{-Y}\mid a]=e^{-2k/(N-1)}+O(N^{-1}).
\]

For the original multiplier, use \(0\le-\log(1-z)-z\le2z^2\) for \(0\le z\le1/2\). On the same central range (for sufficiently large \(N\)),

\[
0\le -S\log[(1-1/a)(1-1/b)]-Y=O(N^{-1}),
\]

uniformly because \(S\le k\le N/2\). The exponential function is 1-Lipschitz on the nonpositive real axis, so this changes the conditional expectation by only \(O(N^{-1})\). Averaging over central shores and using the exponentially small tail establishes

\[
\frac{Q_{N,k}}{Q_{N,0}}=e^{-2k/(N-1)}+O(N^{-1})
=e^{-2k/N}+O(N^{-1}),
\]

with one absolute error constant for all admissible \(k\). This proves the claimed uniform law.

## Verification

The standalone `verify_counts.py` evaluates the exact triple sum with integer arithmetic, independently enumerates the weighted cuts, and constructs each two-step phase configuration from its cut-degree intervals. It checks all \(N=3,4,5,6\) by three routes, extends the cut-enumeration comparison through \(N=10\), with every admissible matching size, and compares the predicted ratios with \(e^{-2k/N}\) at \(N=10,20,40,80,120\). The supplementary \(N=3\) calculation is a verification case, outside the theorem's stated domain.

The independent `verify_direct.cpp` enumerates *all* labelled chip configurations in the sufficient region \(0\le x_v<2d_v\) for those same small graphs, using the vertex-neighbor chip-firing rule directly. It tested 2,375,520 configurations and obtained exactly the same counts. This finite computation is not substituted for the proof for unbounded \(N\); the arbitrary-size claim follows from the cut identity and the uniform probability estimate.

To reproduce, use `python3 verify_counts.py` and `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct`. Captured outputs are supplied as `counts_output.txt` and `direct_output.txt`.

## Relationship to prior work

The general parallel chip-firing dynamics, periodic firing patterns, and complete-graph activity regimes have established foundations in the papers listed below. Jiang's 2010 work proves possible period results for complete bipartite and multipartite graphs; Jiang, Scully, and Zhang characterize possible firing patterns. Levine's complete-graph paper uses a self-loop-inclusive convention for its main circle-map results, unlike the ordinary loopless degree-threshold convention used here. The general two-cycle cut parametrization and exact mass-resolved complete-graph orbit counts are known and are not claimed as new. A separate previously established asymptotic result for bounded-degree deletions from complete bipartite graphs gives a different exponential parameter and an arcsine phase-size law. Its graph class excludes the present complete graphs; its estimates do not imply the complete-graph matching-defect constant or the uniform order-inverse-size bound here.

The **new assessed quantitative statement** is the uniform ratio law \(e^{-2k/N}+O(N^{-1})\) for deleting arbitrary matchings, together with its exact finite-sum realization. It is not implied by identifying which periods occur or by the existence of a middle activity regime. A general cut enumeration can be specialized to obtain the finite sum, but does not by itself supply the weighted-cut concentration and uniform asymptotic analysis.

## Limitations

The theorem concerns only primitive period-two orbits and ordinary synchronous, nonnegative, integer degree-threshold chip firing on the specified graph family. It does not classify all periodic orbits or the attraction probabilities under any distribution on initial chip states. The error term is an absolute, uniform order bound, not a sharp first correction. The originality comparison was conducted against identifiable literature and accessible previous statements; unindexed equivalent results remain possible. The computational checks cover finite sizes only.

## References

1. Lionel Levine, *Parallel chip-firing on the complete graph: Devil's staircase and Poincaré rotation number*, arXiv:0811.2800 (first posted 2008-11-17), https://arxiv.org/abs/0811.2800.
2. Tian-Yi Jiang, *On the period lengths of the parallel chip-firing game*, arXiv:1003.0943 (first posted 2010-03-04), https://arxiv.org/abs/1003.0943.
3. Tian-Yi Jiang, Ziv Scully, Yan X. Zhang, *Motors and impossible firing patterns in the parallel chip-firing game*, arXiv:1211.6786 (first posted 2012-11-29), https://arxiv.org/abs/1211.6786.
4. Javier Bitar and Eric Goles, *Parallel chip firing games on graphs*, Theoretical Computer Science 92 (1992), 291–300, https://doi.org/10.1016/0304-3975(92)90316-8 (background model; publication abstract checked).
