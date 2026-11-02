# Sharp Lipschitz spread of length-two double brooms and its three-to-one branching transition

## Finding

Let \(B_{m,n}\), for integers \(m,n\ge2\), be the unit-edge tree formed from a three-vertex path \(a-b-c\) by adding \(m\) private leaves adjacent to \(a\) and \(n\) private leaves adjacent to \(c\). **All three path vertices and all leaves belong to the metric space**, with the graph shortest-path metric and uniform vertex probability. Set \(N=m+n+3\), \(H=\max\{m,n\}\), \(L=\min\{m,n\}\), and \(S=m+n\). The exact graph spread, or sharp squared real Lipschitz--Poincaré constant, is
\[
\mathcal V_{m,n}=\max_{\operatorname{Lip}(f)\le1}\frac1N\sum_{v\in B_{m,n}}(f(v)-\bar f)^2,
\qquad \bar f=N^{-1}\sum_v f(v).
\]
It satisfies, for **every** such pair of integers,
\[
\boxed{N^2\mathcal V_{m,n}=\begin{cases}
16mn+14(m+n)+6,&H\le3L+3,\\
N(H+9L+5)-\mathbf1_{2\mid S},&H\ge3L+4.
\end{cases}}
\tag{1}
\]
Every maximizing function saturates every tree edge and is monotone along the central three-vertex path, up to global sign; its leaf values and all possible multiplicities are explicitly classified below.

For fixed \(S=m+n\ge4\), transferring one leaf from the larger endpoint branch to the smaller one **strictly increases** spread whenever their sizes differ by at least two. Thus the balanced allocation uniquely maximizes spread among such length-two double brooms, and \((2,S-2)\) minimizes it, up to interchanging endpoints.

If \(L\to\infty\) and \(H/L\to\rho\in[1,\infty)\), then
\[
\boxed{\lim\mathcal V_{m,n}=\begin{cases}
\dfrac{16\rho}{(1+\rho)^2},&1\le\rho\le3,\\[4pt]
\dfrac{\rho+9}{\rho+1},&\rho\ge3.
\end{cases}}
\tag{2}
\]
This limiting profile is \(C^1\) but not \(C^2\) at the sharp ratio \(\rho=3\); the one-sided second derivatives are \(1/8\) and \(1/4\). In the contrasting regime where \(L\) stays fixed and \(H\to\infty\), the spread tends to \(1\).

## Assumptions and scope

All edges have length one. The Lipschitz condition is equivalent to \(|f(x)-f(y)|\le1\) for each graph edge. Real-valued functions and uniform point masses are essential. This is not the length-one double-star graph with adjacent hubs: the central spine here contains a **third vertex**; indeed, the tree diameter equals four rather than three.

To state **all** equality cases, translate and, if necessary, globally negate \(f\) so that its three path values are \(f(a)=0\), \(f(b)=1\), \(f(c)=2\). Let \(k\) be the number of leaves adjacent to \(a\) with value \(+1\), while its other \(m-k\) leaves have value \(-1\). Let \(\ell\) be the number of leaves adjacent to \(c\) with value \(3\), while its remaining \(n-\ell\) leaves have value \(1\).

* When \(n\le3m+3\) and \(m\le3n+3\), precisely \((k,\ell)=(0,n)\) is optimal.
* When \(n>3m+3\), precisely \(k=0\) and the integer(s) \(\ell\) closest to \((3m+n+3)/2\) are optimal.
* When \(m>3n+3\), precisely \(\ell=n\) and the integer(s) \(k+n\) closest to \((m-n-3)/2\) are optimal.

These are all maximizing count pairs. Each admissible choice of which labeled leaves realize those values gives a maximizer. The second and third cases have two nearest integers exactly when \(m+n\) is even. At \(H=3L+4\), the full-extreme leaf assignment and a split assignment tie; for \(H\ge3L+5\), every maximizer splits the larger leaf class.

## Proof

**1. Strict edge saturation.** After anchoring \(f(a)=0\), the collection of 1-Lipschitz functions is linearly parameterized by the independent edge increments in the cube \([-1,1]^{m+n+2}\), since a tree has no cycle constraints. Centered variance is a *strictly positive definite quadratic form* in these increments: vanishing variance forces a constant function and hence all anchored increments zero. A strictly convex function on a cube cannot achieve its maximum at a point with any interior coordinate, because replacing that coordinate by one of its two endpoints increases the value. Hence **every** maximizer saturates every edge, including the central spine.

**2. The middle vertex cannot be a turning point.** Suppose, after translation and possible negation, that the spine values instead are \(0,1,0\). All vertices on the left side (\(a\) and its leaves) have values in \([-1,1]\), while all vertices on the right side (\(c\) and its leaves) also have values in \([-1,1]\). Reflect the entire right-side subtree around level \(1\): replace its values \(x\) by \(2-x\), leaving the middle vertex and left side unchanged. Every edge still has increment of absolute value one. Pairwise distances **within** either side are unchanged; pairs involving the middle vertex preserve their absolute value differences. For any left-side value \(y\le1\) and right-side value \(x\le1\), the change in their squared difference is
\[
(2-x-y)^2-(x-y)^2=4(1-x)(1-y)\ge0.
\]
It is strictly positive for the pair of end hubs, where \(x=y=0\). The exact identity
\[
\operatorname{Var}(f)=\frac1{N^2}\sum_{u<v}(f(u)-f(v))^2
\]
then shows that the reflection **strictly increases** variance. The other folded sign pattern is equivalent by global negation, so no maximum folds at the middle vertex. Thus the normalized spine is necessarily \(0,1,2\).

**3. Integer quadratic optimization and the parity defect.** In the canonical orientation and notation above,
\[
\sum_v f(v)=3-m+n+2(k+\ell),\qquad
\sum_v f(v)^2=m+n+5+8\ell.
\]
Consequently the variance numerator is
\[
F(k,\ell)=N(m+n+5+8\ell)-[3-m+n+2(k+\ell)]^2.
\tag{3}
\]
For a fixed integer \(j=k+\ell\), this is strictly increasing in \(\ell\). Therefore any maximizing pair has \(\ell=\min\{j,n\}\) and \(k=\max\{0,j-n\}\). Writing \(j\in\{0,\ldots,m+n\}\), two concave quadratic arcs remain:
\[
F_j=\begin{cases}
N(n+9m+5)-4\bigl(j-\frac{3m+n+3}{2}\bigr)^2,&0\le j\le n,\\[4pt]
N(m+9n+5)-4\bigl(j-\frac{m-n-3}{2}\bigr)^2,&n\le j\le m+n.
\end{cases}
\tag{4}
\]
Both formulas coincide at \(j=n\). The real vertices of these parabolas straddle the junction when and only when \(n\le3m+3\) and \(m\le3n+3\); the unique maximizing integer is then \(j=n\). Substituting into (3) gives \(16mn+14(m+n)+6\).

When \(n>3m+3\), the first vertex \((3m+n+3)/2\) lies strictly inside its interval and the second parabola decreases from the junction. Its nearest integer(s) are the global maximizers. The square penalty is \(0\) when \(m+n\) is odd and \(1\) when \(m+n\) is even. The opposite imbalance uses the second vertex \((m-n-3)/2\) and yields the symmetric value \(N(m+9n+5)-\mathbf1_{2\mid m+n}\). These observations prove (1) and every equality case; the integer parity is **not** recovered from continuous optimization alone.

**4. Strict leaf balancing.** Fix \(S=m+n\) and \(N=S+3\). Replace \((H,L)\) by \((H-1,L+1)\) with \(H\ge L+2\). When both pairs lie in the first branch of (1), the numerator increases by \(16(H-L-1)>0\). When both lie in the second, it increases by exactly \(8N>0\), since \(S\) and hence its parity are fixed. The only crossovers from the second to the first branch occur at \(H=3L+d\) with \(d\in\{4,5,6,7\}\); direct substitution gives respective positive increases \(32L+48\), \(32L+60\), \(32L+72\), and \(32L+80\). Iteration proves strict balancing and the endpoint extrema at a fixed leaf budget.

**5. Asymptotic phase transition.** Divide the two numerators in (1) by \(N^2\). Terms of lower order, including the bounded parity correction, vanish as \(L\to\infty\) with finite ratio \(H/L\to\rho\). The two branches yield (2), agreeing in value and first derivative \(-1/2\) at \(\rho=3\). Their second derivatives have limits \(1/8\) and \(1/4\), establishing the claimed \(C^1\)-but-not-\(C^2\) phase boundary. For fixed \(L\), the second numerator is \(N(H+9L+5)-O(1)\), whose normalization tends to one.

## Verification

Run `python3 verify_double_broom.py` (Python 3 standard library; no dependencies). The code enumerates all signed edge increments for the complete small-parameter range \(2\le m,n\le6\), independently compares folded and straight spine patterns, and checks the sharp formula by exact rational arithmetic. It also checks the full integer optimizer profiles for 784 leaf-size pairs, strictly ordered spread across 147 fixed leaf budgets, transition ties and numerical asymptotics. The final printed marker is `ALL_DOUBLE_BROOM_SPREAD_CHECKS_OK`. These finite tests supplement, but never substitute for, the universal proof in Steps 1--5.

## Relationship to prior work

Alon, Boppana and Spencer (1998) defined graph spread and its product-concentration significance and established generic integral extremizers, but did not evaluate this three-spine-vertex two-broom family. Addario-Berry, Janson and McDiarmid (2009) studied spread of random graph ensembles rather than these deterministic diameter-four trees. Yancey (2017) studied graph spread and structural properties of tree hair extremizers, including some special trees with long paths, but his statements do not compute the present exact numerator or its 3:1 transition.

A closer distinct prior calculation, *Sharp Euclidean inballs and contact-facet transitions for bistar symmetric edge polytopes* (2026), gives the exact polar Euclidean inradius, and therefore the equivalent Lipschitz variance, for **double stars with two adjacent hubs** (diameter three). It already covers the diameter-three 2:1 transition and is **not** claimed here. The present graph has three spine vertices and diameter four; its novel strict reflection step excludes the folded spine configuration, its critical ratio is \(3:1\), its parity depends on the total number of leaves, and its sharp numerator and balancing increments differ. In particular its formula cannot be obtained as an implied special case of the diameter-three theorem by simply changing a parameter: subdivision adds a sampled vertex and modifies all cross-branch path distances. The existence of a generic integral-extremizer principle is also acknowledged as prior art.

Equivalent rephrasings of the present diameter-four case in otherwise unindexed mathematical literature are a residual originality risk. The absence of a database match is not itself a proof of novelty.

## Limitations

The theorem assumes two leaf-bearing endpoints of a central path with **exactly two central edges**, with equal vertex masses and unit edge lengths. It does not claim the corresponding formula for longer central paths, arbitrary weighted brooms, or other variance exponents. The balance theorem concerns only this fixed family, not all finite trees. Independent mathematical validation has not been performed.

## References

1. N. Alon, R. Boppana, J. Spencer, *An Asymptotic Isoperimetric Inequality*, Geometric and Functional Analysis **8** (1998), pp. 411--436; especially §1.1 and Theorem 2.1. Original paper: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf.
2. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, first public version arXiv:0902.1156v1, 6 February 2009. https://arxiv.org/abs/0902.1156.
3. M. P. Yancey, *Probabilistic and Geometrical Applications to Graph Theory*, arXiv:1705.09725v1, 26 May 2017; especially Sections 1 and 2.5. https://arxiv.org/abs/1705.09725.
4. *Sharp Euclidean inballs and contact-facet transitions for bistar symmetric edge polytopes*, public research result (2026); the complete published statement and proof address diameter-three two-hub trees.
