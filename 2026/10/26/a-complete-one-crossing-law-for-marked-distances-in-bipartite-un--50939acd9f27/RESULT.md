# A complete one-crossing law for marked distances in bipartite uniform spanning trees

## Finding

Fix an integer \(N\geq4\). For each integer \(a\in\{2,\ldots,N-1\}\), choose uniformly a labeled spanning tree of the complete bipartite graph \(K_{a,N-a}\), and fix two distinct labeled vertices in its part of size \(a\). Let \(D_a\) be their tree distance. This is a family of separate random variables on separate finite probability spaces, compared only through their laws.

For any \(\lceil N/2\rceil\leq u<v\leq N-1\), define
\[
H_N(u,v)=uv-2(N-1)(u+v-N).
\]
Then the **complete stochastic-order trichotomy** is as follows.

1. If \(H_N(u,v)\leq0\), then \(D_v\leq_{\mathrm{st}}D_u\): every upper tail of \(D_v\) is at most the corresponding tail of \(D_u\).
2. If \(H_N(u,v)>0\), \(N=2m\), \(u=m\), and \(v=m+1\), then \(D_v\geq_{\mathrm{st}}D_u\). The two distributions have the same support and, for \(m\geq3\), the inequality at every nontrivial tail is strict.
3. In all remaining cases with \(H_N(u,v)>0\), neither law stochastically dominates the other. At distance threshold four, \(D_v\) has the larger upper tail; at a larger threshold \(D_u\) has the larger upper tail. As the threshold increases, the sign of the difference \(\Pr(D_v\geq2k)-\Pr(D_u\geq2k)\) can switch from positive to negative **at most once** (zeros allowed at the switch).

The first possible incomparable pair occurs at \(N=11\), \(u=6\), \(v=7\), with exact contrasts
\[
\Pr(D_7\geq4)-\Pr(D_6\geq4)=\frac1{420},\qquad
\Pr(D_6\geq6)-\Pr(D_7\geq6)=\frac{17}{2450}.
\]
There are no incomparable pairs for \(4\leq N\leq10\).

A macroscopic phase boundary follows. If \(x\in(1/2,2/3)\) is fixed, comparing \(u_N=\lceil N/2\rceil\) with \(v_N=\lfloor xN\rfloor\) gives incomparable distance laws for all sufficiently large \(N\). For fixed \(x\in(2/3,1)\), the balanced-side law eventually stochastically dominates the \(v_N\) law. No assertion is made at \(x=2/3\).

## Assumptions and scope

All edges have unit weight; the spanning tree is sampled **uniformly**, not as a minimum spanning tree. The two marked vertices always belong to the size-\(a\) part, including after changing the part sizes. They are distinct, and the same total number of vertices \(N\) is used throughout. The comparison parameter satisfies \(\lceil N/2\rceil\leq u<v\leq N-1\): the marked part is at least as large as its complement. Stochastic order means \(X\leq_{\mathrm{st}}Y\) if \(\Pr(X\geq t)\leq\Pr(Y\geq t)\) for every real \(t\). The distances are positive even integers.

For a nonnegative integer \(r\), write \((z)_{\underline r}=z(z-1)\cdots(z-r+1)\), with \((z)_{\underline0}=1\). Put \(b=N-a\) and
\[
S_k(a)=\Pr(D_a\geq2k).
\]
The elementary path-count consequence of the published spanning-tree inclusion formula is
\[
S_k(a)=\frac{(a-2)_{\underline{k-1}}(b-1)_{\underline{k-1}}}{(ab)^{k-1}}
\quad (1\leq k\leq\min(a-1,b)),
\]
with \(S_k(a)=0\) for \(k>\min(a-1,b)\). The exact path counts and this tail formula are **not claimed as new**; the contribution is the complete comparison law and its sharp incomparability threshold.

## Proof

**1. Exact tails from the established tree-inclusion formula.** Ge--Dong [1, Theorem 1.4] gives, for a fixed tree subgraph occupying \(s\) vertices in the first part and \(t\) in the second, the probability it is contained in a uniform spanning tree of \(K_{a,b}\):
\[
\Pr(F\subseteq T)=\frac{sb+ta-st}{a^t b^s}.
\]
This is also a specialization of Dong--Ge [2, Theorem 4]. A simple path of length \(2k\) between two marked first-part vertices uses \(k+1\) vertices of that part and \(k\) of the other part. There are exactly \((a-2)_{\underline{k-1}}(b)_{\underline k}\) such paths: first order the \(k-1\) intermediate first-part vertices and then the \(k\) opposite-part vertices. Every spanning tree contains exactly one connecting path between the marked vertices, so the path-events are disjoint. Consequently, for \(1\leq k\leq\min(a-1,b)\),
\[
\Pr(D_a=2k)=
\frac{(a-2)_{\underline{k-1}}(b)_{\underline k}\big((k+1)b+ka-k(k+1)\big)}{a^k b^{k+1}}.
\]
Direct division and subtraction show that this is \(S_k(a)-S_{k+1}(a)\) for the displayed product \(S_k\). Since \(S_1=1\) and the upper support endpoint vanishes, the mass formula telescopes and proves the stated survival probabilities.

**2. Single-crossing factor identity.** For \(j\geq1\), put
\[
f_j(a)=\frac{(a-j-1)(N-a-j)}{a(N-a)},\qquad S_{j+1}(a)=S_j(a)f_j(a)
\]
whenever both factors are positive, extending with zero at the support boundary. For \(\lceil N/2\rceil\leq u<v\leq N-1\), algebra gives the exact identity
\[
f_j(v)-f_j(u)=
\frac{(v-u)\big[uv-(u+v-N)(j+1)(N-j)\big]}
{uv(N-u)(N-v)}.
\]
Here \(u+v-N>0\). Over the common positive-factor indices \(1\leq j\leq N-v-1\), the product \((j+1)(N-j)\) is strictly increasing, so the bracket is strictly decreasing in \(j\). At \(j=1\) the bracket equals \(H_N(u,v)\).

If \(H_N(u,v)\leq0\), every common ratio factor for \(v\) is no larger than that for \(u\), and the shorter support of \(D_v\) cannot reverse the inequality. Hence \(S_k(v)\leq S_k(u)\) for all \(k\).

If \(H_N(u,v)>0\), then \(S_2(v)>S_2(u)\). On common positive support, the ratio \(S_k(v)/S_k(u)\) starts at one and has successive multipliers \(f_j(v)/f_j(u)\), which are \(\geq1\) until at most one index, then \(\leq1\) thereafter. Hence the ratio is unimodal: relative to one it can change sign only from above to below. The same conclusion extends when \(S_k(v)\) first becomes zero.

**3. Equal-support exception and inevitable crossing otherwise.** For \(u\geq\lceil N/2\rceil\), the largest possible \(k\) with \(S_k(u)>0\) is \(\min(u-1,N-u)\). The smaller-part sizes imply \(D_v\) has strictly shorter positive-tail support than \(D_u\), except when \(N=2m\), \(u=m\), and \(v=m+1\); these have equal positive-tail support. In that exceptional pair, \(u+v-N=1\). For every common positive factor \(1\leq j\leq m-2\),
\[
uv-(u+v-N)(j+1)(N-j)
\geq m(m+1)-(m-1)(m+2)=2>0.
\]
Therefore the exceptional pair has \(S_k(v)\geq S_k(u)\) for all \(k\), with strict inequalities at nontrivial thresholds when \(m\geq3\). All other pairs with \(H_N(u,v)>0\) have \(S_2(v)>S_2(u)\) but \(S_{N-v+1}(v)=0<S_{N-v+1}(u)\), giving incomparability and the one-crossing assertion.

**4. Sharp first order and asymptotic phase boundary.** For fixed \(N\), \(H_N(u,v)\) is strictly decreasing in either coordinate over the stated parameter domain, since the difference upon increasing \(u\) is \(v-2(N-1)<0\) (and symmetrically). For \(N=2m+1\), its maximum at the nearest pair \((m+1,m+2)\) equals \(m^2-5m+2\), nonpositive for \(m\leq4\), positive for \(m\geq5\). For \(N=2m\), excluding the equal-support exception, the largest \(H_N\) occurs at \((m,m+2)\), where it equals \(m^2-6m+4\), nonpositive for \(m\leq5\), positive for \(m\geq6\). Thus the first incomparable case has \(N=11\); the two fractions follow by direct substitution into \(S_2\) and \(S_3\). Finally, for the parameters in the finding, divide \(H_N(u_N,v_N)\) by \(N^2\) and pass to the limit:
\[
\lim_{N\to\infty}\frac{H_N(u_N,v_N)}{N^2}=1-\frac{3x}{2}.
\]
Its strict sign on either side of \(2/3\), together with the trichotomy, establishes the phase boundary. This completes the proof.

## Verification

The standalone pure-Python script `check_exact.py` uses `fractions.Fraction`, not floating-point arithmetic. It independently enumerates labeled bipartite spanning trees by edge subsets and graph connectivity for small orders, checks the path-mass and tail formulas, tests the factor identity and the full trichotomy over all \(4\leq N\leq60\), and reproduces the sharp \(N=11\) fractions. A direct execution passed 89,613 exact assertions. Its finite enumeration is corroboration; the unbounded assertions are justified by the algebraic proof above. Run using `python3 check_exact.py` with the standard library only.

## Relationship to prior work

Ge and Dong [1] establish the inclusion count for a prescribed tree, including the paths used in Step 1; Dong and Ge [2] give a more general prescribed-forest inclusion count. These already imply the exact path-distance probability mass function and survival product after enumeration, so neither expression is presented as novel. Archer and Shalev [3] prove Brownian-continuum-tree scaling for uniform spanning trees of dense graphs, with a complete-bipartite illustration; this is about macroscopic limits rather than the exact finite part-imbalance stochastic-order trichotomy here. Earlier published mathematical-result records about vertex degree versus distance on *Cayley* trees, and opposite-part *degree* distributions on bipartite uniform spanning trees, concern other random quantities and do not imply the stated tail-comparison classification.

The new assertion is precisely the global trichotomy, the at-most-one tail crossing, the sharp first incomparable order, and the macroscopic imbalance boundary, not the input enumeration. A previously unnoticed published stochastic-comparison theorem may nonetheless contain this conclusion; that historical priority remains open.

## Limitations

The comparison only treats marked vertices in the larger/equal part, a fixed total \(N\), and uniform spanning trees of complete bipartite graphs. It is not a comparison of rescaled Brownian limits, arbitrary bipartite host graphs, or vertex pairs in opposite parts. The result does not assert a signed comparison of *all* moments for incomparable cases, nor a boundary classification at \(x=2/3\). Independent external validation has not been performed, and historical priority is uncertain.

## References

[1] Jun Ge and Fengming Dong, *Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs*, arXiv:1904.07766, first posted 2019-04-16; especially Theorem 1.4 and Section 4. https://arxiv.org/abs/1904.07766

[2] Fengming Dong and Jun Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294, first posted 2021-03-09; especially Theorem 4 and its proof. https://arxiv.org/abs/2103.05294

[3] Eleanor Archer and Matan Shalev, *The GHP scaling limit of uniform spanning trees of dense graphs*, arXiv:2301.00461, first posted 2023-01-01; especially its introduction, principal scaling theorem, and complete-bipartite illustration. https://arxiv.org/abs/2301.00461
