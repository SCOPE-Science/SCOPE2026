# Conditional endpoint-degree dependence along paths in bipartite uniform spanning trees

## Finding

Let \(a,b\ge2\), let \(T\) be uniformly sampled from the spanning trees of the complete bipartite graph \(K_{a,b}\), and fix vertices \(u\) and \(v\) in opposite parts, of sizes \(a\) and \(b\), respectively. Write \(\Delta\) for their distance in \(T\), and \(D_u,D_v\) for their degrees. For \(1\le t\le\min(a,b)\) set
\[
C_t=t(a+b-t),\qquad R_t=b-t,\qquad L_t=a-t.
\]
Every possible distance is odd, and its exact law is
\[
\Pr(\Delta=2t-1)=\frac{(a-1)_{t-1}(b-1)_{t-1}C_t}{(ab)^t},
\]
where \((x)_j=x(x-1)\cdots(x-j+1)\), with \((x)_0=1\).

The **complete bivariate conditional degree law** is specified by its polynomial probability-generating function. Put \(h=(z-1)/a\), \(k=(w-1)/b\), and define \(F_j(s)=(1+s)^j\) for nonnegative integers \(j\). Then
\[
\begin{aligned}
&\mathbb E[z^{D_u-1}w^{D_v-1}\mid\Delta=2t-1]\\
&=F_{R_t}(h)F_{L_t}(k)
+\frac{(a-t)R_t}{C_t}hF_{R_t-1}(h)F_{L_t}(k)\\
&\quad+\frac{(b-t)L_t}{C_t}kF_{R_t}(h)F_{L_t-1}(k)
-\frac{R_tL_t}{C_t}hkF_{R_t-1}(h)F_{L_t-1}(k).
\end{aligned}
\]
Any term with a zero multiplicative factor \(R_t\) or \(L_t\) is omitted; thus no negative-index power is ever required. The formula is valid also at \(t=\min(a,b)\).

The conditional covariance has the particularly simple form
\[
\boxed{\operatorname{Cov}(D_u,D_v\mid \Delta=2t-1)
=-\frac{(a-t)(b-t)}{t^2(a+b-t)^2}.}
\]
It is strictly negative when \(t<\min(a,b)\), and exactly zero at the maximal possible distance, when at least one endpoint is forced to be a leaf.

The one-point marginals admit independent-summand representations. When \(t<b\),
\[
D_u\mid(\Delta=2t-1)\ \overset{d}=\ 1+\operatorname{Bin}\!\left(b-t-1,\frac1a\right)
+\operatorname{Bernoulli}\!\left(\frac b{C_t}\right),
\]
with independent summands; when \(t=b\), \(D_u=1\) almost surely. For \(D_v\), exchange \(a\) and \(b\). In both parts, these conditional degree distributions **decrease strictly in first-order stochastic order** at every increase from \(t\) to \(t+1\) within the attainable range. In particular \(\operatorname{Cov}(D_u,\Delta)<0\) and \(\operatorname{Cov}(D_v,\Delta)<0\).

## Assumptions and scope

The host graph is the unweighted simple graph \(K_{a,b}\); every spanning tree is equally likely. The marked vertices are fixed and lie in different bipartition classes. Degrees count edges in the random spanning tree, not in the host graph. All random variables are finite, and \(a,b\ge2\) are arbitrary integers. In the probability-generating polynomial, the convention for absent terms at the boundary is part of the statement.

The stochastic statement refers to each marginal conditional law separately, not to a coordinatewise stochastic ordering of the bivariate vector of endpoint degrees. Negative conditional covariance does not assert independence or general negative association of the entire degree vector.

## Proof

**1. Fixed path extension count.** A standard exact spanning-tree extension formula for a connected prescribed tree \(H\subseteq K_{a,b}\), containing \(s\) vertices from the first part and \(q\) from the second, is
\[
\#\{T:H\subseteq T\}=(sb+qa-sq)a^{b-q-1}b^{a-s-1}.
\tag{1}
\]
This is Theorem 1.4 of Ge and Dong, which also follows directly by contracting \(H\) and applying the matrix-tree theorem. Formula (1) remains valid at the boundary when the expression is interpreted through the equivalent normalized ratio below. The total number of trees is \(a^{b-1}b^{a-1}\).

Fix one simple path \(P\) from \(u\) to \(v\) of length \(2t-1\). Such a path contains exactly \(t\) vertices from each side; by (1),
\[
\Pr(P\subseteq T)=\frac{C_t}{(ab)^t}.
\tag{2}
\]
There are \((a-1)_{t-1}(b-1)_{t-1}\) such paths. The events that different paths are contained in a spanning tree are disjoint, because every tree has a unique \(u\)-to-\(v\) path. Multiplying (2) by their count proves the distance formula. Every admissible length has positive mass.

**2. Mixed inclusion moments.** Condition on this particular path \(P\). It leaves \(R_t=b-t\) possible new edges at \(u\), to right-side vertices outside \(P\), and \(L_t=a-t\) possible new edges at \(v\), to left-side vertices outside \(P\). Let \(X=D_u-1\) and \(Y=D_v-1\). Select any \(j\) distinct eligible edges at \(u\) and \(\ell\) distinct eligible edges at \(v\). Their union with \(P\) is a tree with \(t+\ell\) left-side vertices and \(t+j\) right-side vertices. Dividing the corresponding count (1) by the count for \(P\) gives the conditional inclusion probability
\[
\frac1{a^j b^\ell}
\left(1+\frac{j(a-t)+\ell(b-t)-j\ell}{C_t}\right).
\tag{3}
\]
Therefore, for all \(0\le j\le R_t\) and \(0\le\ell\le L_t\),
\[
\mathbb E[(X)_j(Y)_\ell\mid P]
=\frac{(R_t)_j(L_t)_\ell}{a^j b^\ell}
\left(1+\frac{j(a-t)+\ell(b-t)-j\ell}{C_t}\right).
\tag{4}
\]
These exact moments determine the full bivariate generating polynomial. Expanding \(z^X=(1+z-1)^X\) and \(w^Y=(1+w-1)^Y\) in factorial moments and summing the four terms of (4) yields the displayed generating function. Its parameters depend only on \(a,b,t\), not on the intermediate path labels, so the same law holds after conditioning only on \(\Delta=2t-1\).

**3. Covariance and margins.** Taking \(j,\ell\in\{0,1\}\) in (4), and writing \(C=C_t\), \(R=R_t\), \(L=L_t\), gives
\[
\mathbb EX=\frac Ra\left(1+\frac{a-t}{C}\right),\quad
\mathbb EY=\frac Lb\left(1+\frac{b-t}{C}\right),
\]
\[
\mathbb E[XY]=\frac{RL}{ab}\left(1+\frac{a-t+b-t-1}{C}\right).
\]
Hence
\[
\begin{aligned}
\operatorname{Cov}(X,Y)
&=-\frac{RL}{ab}\left(\frac1C+\frac{(a-t)(b-t)}{C^2}\right)\\
&=-\frac{RL}{C^2},
\end{aligned}
\]
because \(C+(a-t)(b-t)=ab\). Since degrees differ from \(X,Y\) by constants, this proves the covariance identity and its exact strictness boundary.

Setting \(w=1\) in the generating function and using the same identity gives, when \(R\ge1\),
\[
\mathbb E[z^X\mid\Delta=2t-1]
=\left(1+\frac{z-1}{a}\right)^{R-1}
\left(1+\frac bC(z-1)\right).
\tag{5}
\]
For \(t<b\), the Bernoulli parameter \(b/C\) lies in \((0,1)\). Formula (5) proves the stated independent-binomial-plus-Bernoulli representation. If \(t=b\), then \(R=0\) and \(X=0\). The result for \(v\) follows by exchanging the two parts.

**4. Strict stochastic regression.** As \(t\) grows through \(1,\ldots,\min(a,b)\), the number \(C_t=t(a+b-t)\) increases strictly: \(C_{t+1}-C_t=a+b-2t-1>0\) whenever \(t<\min(a,b)\). Thus the Bernoulli success probability \(b/C_t\) decreases strictly, while the binomial trial count \(b-t-1\) drops by one wherever it remains nonnegative. A coupling using shared independent uniforms orders successive conditional degrees almost surely, with strict inequality with positive probability. If the next index has \(t+1=b\), the degree at \(u\) is deterministically one and the previous conditional degree exceeds one with positive probability. The argument for \(v\) is identical. Since all possible distances have positive mass, covariance with the strictly increasing distance is strictly negative by the independent-copy identity for monotone regression.

## Verification

The accompanying standalone Python program `verification/check.py` enumerates all spanning trees of \(K_{a,b}\) for \(2\le a,b\le5\) with \(ab\le20\), using edge-subset enumeration and a union-find cycle rejection; this is independent of formula (1). It checks the count \(a^{b-1}b^{a-1}\), the exact distance law, every mixed factorial moment in (4) within its available ranges, every conditional covariance, and every successive conditional upper-tail comparison in both bipartition classes. The saved verifier passed 574 exact rational comparisons. These finite checks supplement, but do not replace, the unrestricted proof above.

## Relationship to prior work

Pemantle's 2004 account develops finite uniform spanning trees, transfer-impedance formulas, and degree laws, motivating the question of how local degree distributions respond to a global distance constraint. Ge and Dong's Theorem 1.4 (2019 preprint; 2020 journal paper) provides the exact *fixed-tree inclusion count* (1). Its count is a proof input, not a new result here. The contribution studied here is the extracted **two-endpoint conditional law**, its exact conditional covariance, and the resulting strict degree-versus-distance stochastic regression for a two-class host graph.

A published formula for uniform Cayley trees already gives a one-endpoint binomial-plus-Bernoulli degree law conditional on distance; it neither treats bipartite host graphs nor specifies the two-endpoint covariance established here. The present finding is not an independence theorem: its negative conditional covariance measures the remaining dependence after separation is fixed.

## Limitations

This theorem concerns complete bipartite host graphs with *uniform* spanning-tree weights and marked endpoints in opposite classes. It does not assert the same distribution for general bipartite graphs, weighted spanning trees, or endpoints in the same class. The earlier fixed-tree inclusion formula is strong enough to recover finite-degree distributions by further combinatorial algebra; that derivability is an explicit originality risk. The detailed two-endpoint conditional identity and strict regression have not received independent publication-priority verification.

## References

1. R. Pemantle, “Uniform random spanning trees,” arXiv:math/0404099v1, publicly posted 2004-04-05, https://arxiv.org/abs/math/0404099.
2. J. Ge and F. Dong, “Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs,” arXiv:1904.07766v1 (2019-04-16); *Discrete Applied Mathematics* 283 (2020), 542–554, https://arxiv.org/abs/1904.07766, DOI 10.1016/j.dam.2020.02.002.
3. “Exact negative regression between endpoint degree and distance in a uniform Cayley tree,” publicly accessible research record, 2026-10-04, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-negative-regression-between-endpoint-degree-and-distance-i--d9ddfb06a9ae.
