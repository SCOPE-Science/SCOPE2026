# Parity-controlled inball rigidity in matched-pair Lipschitz-free spaces

## Finding

Fix an integer \(k\ge2\) and a parameter \(0<t<1\). Equip \(2k\) points, grouped into \(k\) disjoint pairs, with distance \(t\) within each pair and distance \(1\) between different pairs. Let \(P_{k,t}\) be the real Lipschitz-free unit ball in the canonical zero-sum Euclidean space
\[
H=\{z\in\mathbb R^{2k}:\sum_{a=1}^{2k}z_a=0\},\qquad \langle z,w\rangle=\sum_a z_aw_a.
\]
Write \(r_{k,t}\) for its largest Euclidean inball radius and \(\mathcal C_{k,t}\) for the complete set of centers of balls of this radius contained in \(P_{k,t}\). The following determines the radius, all contacting facets at the origin-centered ball, and the affine dimension of \(\mathcal C_{k,t}\).

For even \(k\),
\[
r_{k,t}=\sqrt{\frac2k},\qquad
\#\{\text{contact facets}\}=\binom{k}{k/2},\qquad
\dim\operatorname{aff}\mathcal C_{k,t}=k.
\]
For odd \(k\ge3\), put
\[
t_k=\frac{2k-2}{2k-1},\qquad
C_0=\frac1{2k},\qquad C_1=t(1-t)+\frac{(1-t)^2}{2k}.
\]
Then
\[
r_{k,t}=\left(\frac{k}{2}-\min\{C_0,C_1\}\right)^{-1/2}.
\]
The optimal-center dimension equals \(k\) for \(t<t_k\) and equals \(0\) for \(t\ge t_k\); in the latter regime the origin is the unique optimal center. The numbers of facets touching the centered maximal ball are, respectively,
\[
\begin{array}{c|c}
0<t<t_k&2\binom{k}{(k-1)/2}\\
t=t_k&2\binom{k}{(k-1)/2}+2(k+1)\binom{k}{(k+1)/2}\\
t_k<t<1&2(k+1)\binom{k}{(k+1)/2}.
\end{array}
\]
In particular, the same fixed combinatorial type of dual Lipschitz polytope undergoes a genuine interior transition from a \(k\)-dimensional family of optimal ball centers to a unique center, only when the number of pairs is odd.

## Assumptions and scope

The metric is an ultrametric: the only distances are \(t\) on the matching and \(1\) elsewhere. Its free-space unit ball is
\[
P_{k,t}=\operatorname{conv}\left\{\frac{e_a-e_b}{d(a,b)}:a\ne b\right\}\subset H.
\]
The polar Lipschitz ball \(Q_{k,t}=P_{k,t}^{\circ}\) is the polytope of centered real functions \(f\in H\) satisfying \(|f_a-f_b|\le d(a,b)\). A *contact facet* is a facet whose supporting hyperplane has Euclidean distance \(r_{k,t}\) from the origin. The full optimal-center set is not assumed a singleton. The affine dimension is taken in \(H\).

## Proof

**1. A product-hexagon representation.** Every 1-Lipschitz function on this metric has oscillation at most \(1\), since all pairwise distances are at most \(1\). Subtract its minimum, so all values lie in \([0,1]\). Conversely, any values in \([0,1]\) with paired differences at most \(t\) automatically satisfy every cross-pair Lipschitz inequality. Therefore, if \(\pi\) subtracts the coordinate mean,
\[
Q_{k,t}=\pi(K_t^k),\qquad
K_t=\{(x,y)\in[0,1]^2:|x-y|\le t\}.
\]
The six vertices of the planar hexagon \(K_t\) are
\[
(0,0),\ (1,1),\ (0,t),\ (t,0),\ (1-t,1),\ (1,1-t).
\]
The function \(\|\pi f\|_2^2\) is convex; hence its maximum on this product is attained at a product vertex. Moreover, strict convexity in \(H\) shows that every maximizing centered function is a vertex of \(Q_{k,t}\), and hence determines a contact facet of \(P_{k,t}\).

**2. An exact imbalance penalty.** Label the pairs \(i=1,\ldots,k\). Represent each of their six states by a sign \(s_i\in\{-1,+1\}\), indicating the lower or upper group, and a flag \(\varepsilon_i\in\{0,1\}\), indicating whether it is split. The midpoint of the pair is \((1+s_i(1-t\varepsilon_i))/2\); its two members differ by \(t\varepsilon_i\). Let
\[
E=\sum_i\varepsilon_i,\quad
W=\sum_i s_i(1-t\varepsilon_i).
\]
Subtracting the global mean and evaluating both within-pair and between-pair sums gives the identity
\[
\|\pi f\|_2^2=\frac{k}{2}-\left[t(1-t)E+\frac{W^2}{2k}\right].\tag{1}
\]
Thus maximum norm is equivalent to minimizing the nonnegative bracketed penalty.

**3. The sharp two-pattern principle.** If \(k\) is even, choose \(E=0\) and exactly half of the signs positive. Then \(W=0\), the penalty vanishes, and every split state has strictly positive penalty because \(0<t<1\). This proves the even formula and identifies all its maximizers.

Assume \(k\ge3\) is odd. When \(E=0\), the integer \(W=\sum_i s_i\) is odd; the least possible penalty is \(C_0=1/(2k)\), attained exactly at \(|W|=1\). When \(E=1\), the least possible \(|W|\) is \(1-t\), attained when the unique split pair belongs to the majority sign. This gives \(C_1=t(1-t)+(1-t)^2/(2k)\).

No configuration with \(E\ge2\) improves either candidate. For \(t\ge1/(2k+1)\), its penalty is at least \(2t(1-t)\), which is at least \(C_1\), because \(2kt\ge1-t\). Equality cannot occur in this comparison: at strict inequality of the parameter bound it is immediate; at its endpoint the odd integer \(\sum_i s_i\) cannot be canceled by \(t\sum_i s_i\varepsilon_i\), whose absolute value is less than \(1\).

For \(0<t<1/(2k+1)\), put \(S=\sum_i s_i\), a nonzero odd integer. Since \(E\le k\),
\[
|W|\ge |S|-tE\ge1-tE>0.
\]
The penalty minus \(C_0\) is therefore at least
\[
\frac{Et}{2k}\left[(2k-2)-(2k-E)t\right]>0,
\]
where the last inequality follows from \(E\ge2\), \(k\ge3\), and \(t<1\). Hence the two patterns are exhaustive. Direct subtraction gives
\[
C_1-C_0=\frac{t}{2k}\left[(2k-2)-(2k-1)t\right],
\]
so the unique interior transition is \(t=t_k\). Formula (1) proves the stated radius because the largest centered Euclidean ball in the polar-dual \(P_{k,t}\) has radius \((\max_{f\in Q_{k,t}}\|f\|_2)^{-1}\).

**4. Contact counts.** With even \(k\), the maximizers have \(k/2\) upper constant pairs and \(k/2\) lower constant pairs, giving \(\binom{k}{k/2}\) distinct centered potentials. With odd \(k\), unsplit maximizers choose a majority group of size \((k+1)/2\) with either sign, hence \(2\binom{k}{(k-1)/2}\) choices. In the split regime, choose a sign of the majority, choose its \((k+1)/2\) group positions, select one majority pair to split, and orient its split endpoints in two ways. The count is \(2(k+1)\binom{k}{(k+1)/2}\). At equality of the two penalties the contact sets are disjoint and both occur.

**5. Dimension of every optimal-center locus.** Let \(\mathcal N\) be the set of centered contact normals. Because \(P_{k,t}\) is centrally symmetric, a radius-\(r_{k,t}\) Euclidean ball centered at \(c\in H\) lies inside it precisely when
\[
|\langle c,f\rangle|+r_{k,t}\|f\|_2\le1
\]
for all vertices \(f\) of \(Q_{k,t}\). Every contacting normal satisfies \(\langle c,f\rangle=0\). Conversely, in the subspace perpendicular to all contact normals, all remaining finitely many facet inequalities have positive slack at the origin, so a relative neighborhood of the origin consists of optimal centers. Consequently,
\[
\dim\operatorname{aff}\mathcal C_{k,t}
=(2k-1)-\dim\operatorname{span}\mathcal N.\tag{2}
\]
Decompose \(H=U\oplus V\), where \(U\) consists of vectors constant on each matched pair and with zero total sum (dimension \(k-1\)), and \(V\) consists of independent opposite fluctuations inside each pair (dimension \(k\)). All unsplit contact normals lie in \(U\). Their orbit under permutations of the \(k\) pairs spans \(U\): swapping a high and a low pair generates a pair-block difference, and permutations generate every such difference. Thus (2) yields optimal-center dimension \(k\) in the even case and in the odd unsplit-only regime.

In the odd split regime, every pair can be the unique split pair in a contact pattern. Reversing its orientation while keeping all other states fixed produces its antisymmetric coordinate direction, so the contact span contains \(V\). The pair-mean part of a split contact normal is nonconstant; permuting the pairs shows that these projected normals span \(U\) as well. Thus \(\mathcal N\) spans all of \(H\), and the origin is the unique optimal center. At the transition point split contacts are already present, so the same conclusion holds.

## Verification

The standalone standard-library script `matched_metric_check.py` enumerates all six states independently per pair, computes exact rational centered squared norms, checks the analytic maxima and contact counts, and computes the exact rank of the contacting-normal matrix. It passed \(23\) parameter configurations: five rational parameters for each \(k=2,3,4,5\), both exact transition parameters for \(k=3,5\), and an additional six-pair case. Contact-normal rank was checked for the first \(22\) configurations. Run with `python matched_metric_check.py`.

These are finite checks only. The proof for all integers \(k\ge2\) and all real \(0<t<1\) is the product-hexagon identity, exact penalty inequality, and contact-rank argument above.

## Relationship to prior work

Alexander, Fradelizi, García-Lirola, and Zvavitch establish the polar description, the canonical finite metric geometry, and general extremal considerations for Lipschitz-free unit balls [1]. A published classification of dual extreme Lipschitz potentials for independently shortened disjoint pairs gives an exact facet count independent of the short lengths [2]. That classification concerns *which facets exist*; it does not determine the Euclidean distances of their supporting hyperplanes or the geometry of all maximum-ball centers. The present theorem supplies those quantitative invariants for the uniform perfect-matching specialization and identifies an interior rigidity transition invisible to the known facet count.

Results for complete multipartite graph metrics concern a different regime of same-part distances (greater than one, rather than shorter than one). General equilateral metric radii describe the endpoint \(t=1\), not the interior phase \(t_k\). The theorem neither claims the preexisting facet enumeration nor addresses Mahler volume products.

## Limitations

The Euclidean realization is the canonical zero-sum coordinate space; the inradius is not invariant under arbitrary linear changes of coordinates. Every pair has the same short length \(t\); unequal short lengths, unmatched points, the degenerate coincidence limit \(t=0\), and the equilateral endpoint \(t=1\) are excluded. The result does not describe the full shape, rather than only the affine dimension, of nonunique optimal-center sets. The finite checker cannot replace the infinite-family proof. Independent external verification has not been performed.

## References

1. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (initial public version 2019-11-24), https://arxiv.org/abs/1911.10642.
2. *Facet enumeration for equilateral metrics with independently shortened pairs* (public mathematical research record, 2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-facet-enumeration-for-equilateral-metrics-with-independently-sho--3bd6d7048744.
