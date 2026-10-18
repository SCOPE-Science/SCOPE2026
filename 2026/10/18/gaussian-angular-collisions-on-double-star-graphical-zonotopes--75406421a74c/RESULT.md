# Gaussian angular collisions on double-star graphical zonotopes

## Finding

Let \(T_{p,q}\) be the tree with two adjacent hubs, \(p\) leaves attached to the first hub and \(q\) leaves attached to the second, where \(p,q\ge 1\). Form its centered Euclidean graphical zonotope \(Z_{p,q}\), and choose two independent isotropic Gaussian linear objective directions in its intrinsic affine span. Let \(C_{p,q}\) denote the probability that the unique maximizing vertex is the same for both objectives.

Put
\[
I_{i,j}^{p,q}=\sum_{h=0}^{p-i}(-1)^h\binom{p-i}{h}\frac{(i+j+h+1)!\,(q-j)!}{(i+h+1)\,(i+q+h+2)!},
\quad 0\le i\le p,\quad 0\le j\le q.
\]
Then the exact finite-dimensional collision law is
\[
\boxed{C_{p,q}=2\sum_{i=0}^{p}\sum_{j=0}^{q}\binom pi\binom qj\left(I_{i,j}^{p,q}\right)^2.}
\]
In particular all the collision probabilities are rational numbers, despite being probabilities of intersections of Euclidean normal cones.

Define the reference one-hub star probability
\[
S_s=\frac{1}{(s+1)^2}\sum_{j=0}^{s}\binom{s}{j}^{-1}.
\]
For any sequence of integers \(p,q\to\infty\) with \(p/(p+q)\to\theta\in[0,1]\), one has
\[
\boxed{p^2q^2C_{p,q}\longrightarrow4\bigl(1-\theta(1-\theta)\bigr),}\qquad
\boxed{\frac{C_{p,q}}{S_pS_q}\longrightarrow1-\theta(1-\theta).}
\]
The latter limiting ratio is minimized uniquely at \(\theta=1/2\), where it is \(3/4\); the limit is \(1\) at either endpoint. In particular \(C_{m,m}\sim 3/m^4\). The tree graphical zonotope has \(2^{p+q+1}\) vertices, so for the balanced family the reciprocal collision probability is asymptotic to \(m^4/3\), in striking contrast with the exponential combinatorial vertex count.

## Assumptions and scope

The vertices of \(T_{p,q}\) are the hubs \(A,B\), leaves \(A_1,\dots,A_p\) adjacent only to \(A\), and leaves \(B_1,\dots,B_q\) adjacent only to \(B\). In \(\mathbb R^{p+q+2}\), equipped with its usual inner product, define
\[
Z_{p,q}=\sum_{\{r,s\}\in E(T_{p,q})}\left[-\frac{e_r-e_s}{2},\frac{e_r-e_s}{2}\right]\subset\mathbf1^\perp.
\]
The edge generators are linearly independent, since the graph is a tree; thus \(Z_{p,q}\) is a full-dimensional parallelotope in \(\mathbf1^\perp\), with \(2^{p+q+1}\) vertices. A standard Gaussian on \(\mathbf1^\perp\) defines an isotropic objective direction; the maximizer is unique almost surely. An independent second Gaussian has the same law. The collision probability is the sum of squared spherical normal-cone proportions over all vertices. All statements concern these canonical Euclidean generators, not an arbitrary affine image or the different symmetric edge polytope \(\operatorname{conv}\{\pm(e_r-e_s)\}\).

## Proof

**1. Reduction to independent coordinate ranks.** Each edge segment is maximized at its endpoint determined by the sign of the inner product of the objective with \(e_r-e_s\). Because the edge generators of a tree are linearly independent, different edge sign choices determine different vertices, and no generic sign pattern is excluded. Write a Gaussian objective in \(\mathbf1^\perp\) as the orthogonal projection of an \(N=p+q+2\)-vector of independent standard Gaussian coordinates. Projection subtracts a common scalar and therefore leaves every edge comparison unchanged. The probability integral transform, applied simultaneously to the coordinates of each objective, replaces them by independent uniform random variables on \([0,1]\), without changing their pairwise comparisons. The two objectives are independent, including their corresponding coordinate arrays.

**2. Conditioning on the hubs.** Denote the two objective values at hub \(A\) by \(u,u'\) and at hub \(B\) by \(v,v'\). Conditional on these four values, a leaf adjacent to \(A\) has matching edge signs for the two objectives precisely when its two independent uniform values lie both below the corresponding hub values, or both above. This has conditional probability
\[
a(u,u')=uu'+(1-u)(1-u')=1-u-u'+2uu'.
\]
The analogous probability for a leaf adjacent to \(B\) is \(a(v,v')\). All leaf-edge events are conditionally independent. The central edge has matching signs precisely when \((u-v)(u'-v')>0\). Hence
\[
C_{p,q}=\int_{[0,1]^4}\mathbf1_{\{(u-v)(u'-v')>0\}}a(u,u')^p a(v,v')^q\,du\,du'\,dv\,dv'.
\tag{1}
\]
The two regions \(\{u<v,u'<v'\}\) and \(\{u>v,u'>v'\}\) have equal integrals under simultaneous reflection \((u,u',v,v')\mapsto(1-u,1-u',1-v,1-v')\). Expand
\[
a(u,u')^p=\sum_{i=0}^{p}\binom pi u^i(1-u)^{p-i}{u'}^i(1-u')^{p-i}.
\]
For the region \(u<v,u'<v'\), the integrals factor into two copies of
\[
I_{i,j}^{p,q}=\int_{0<u<v<1}u^i(1-u)^{p-i}v^j(1-v)^{q-j}\,du\,dv.
\]
Expanding \((1-u)^{p-i}\) and integrating first in \(u\), then using an integer-parameter beta integral, gives
\[
I_{i,j}^{p,q}=\sum_{h=0}^{p-i}(-1)^h\binom{p-i}{h}\frac{(i+j+h+1)!\,(q-j)!}{(i+h+1)(i+q+h+2)!}.
\]
Substituting into (1) proves the finite double sum, including its factor \(2\).

**3. One-hub normalization.** With \(s\) leaves and no central edge, the collision probability is
\[
S_s=\int_{[0,1]^2}a(x,y)^s\,dx\,dy
=\sum_{j=0}^{s}\binom sj\left(\frac{j!(s-j)!}{(s+1)!}\right)^2
=\frac1{(s+1)^2}\sum_{j=0}^{s}\binom sj^{-1}.
\]
The two endpoint terms of the last sum equal \(2\). For \(s\ge4\), the remaining terms are bounded by \(2/s+(s-3)/\binom s2\), which tends to zero. Therefore \(s^2S_s\to2\).

**4. Corner limits for the weighted hub pairs.** Define a probability measure \(\mu_s\) on \([0,1]^2\) with density \(a(x,y)^s/S_s\). The function \(a\) reaches its maximum \(1\) at precisely the two corners \((0,0)\) and \((1,1)\). Outside any fixed neighborhoods of those corners its maximum is strictly smaller than \(1\), so the \(\mu_s\)-mass there tends to zero exponentially relative to \(S_s\asymp s^{-2}\). Reflection \((x,y)\mapsto(1-x,1-y)\) makes the two corner masses equal. Near \((0,0)\), change variables \((x,y)=(X/s,Y/s)\); for fixed \(X,Y\ge0\),
\[
a(X/s,Y/s)^s\longrightarrow e^{-X-Y}.
\]
For \(x,y\le\delta<1/2\), the bound \(a(x,y)\le\exp(-(1-\delta)(x+y))\) dominates the rescaled integrals. Dominated convergence thus gives independent unit-exponential coordinates \((X,Y)\) conditional on the zero corner. Reflection gives the same independent exponential deficit coordinates near the one corner. Therefore \(\mu_s\) asymptotically consists of equal masses at two corner types, each carrying an independent pair of exponential local coordinates on scale \(1/s\).

**5. Coupling the hubs and finishing the asymptotic.** Dividing (1) by \(S_pS_q\) shows that the ratio is the probability of central-edge sign agreement for independent hub pairs \((u,u')\sim\mu_p\) and \((v,v')\sim\mu_q\). Their corner types are independent asymptotic fair coin flips. If the two hubs occupy opposite corners, the central-edge signs agree with probability tending to \(1\). If both occupy the zero corner, their first-coordinate values converge after rescaling to independent \(X/p\) and \(Y/q\) with \(X,Y\) unit exponentials. As \(p/(p+q)\to\theta\),
\[
\Pr\{X/p<Y/q\}\longrightarrow\theta.
\]
The second objective gives an independent such comparison, so agreement of the two central-edge signs has limiting probability \(\theta^2+(1-\theta)^2\). The same value holds at the one corner, by reflection. These conclusions remain valid for \(\theta=0,1\) because strict exponential comparisons have zero tie probability and one of the two scales becomes negligible. Averaging over the four equally likely corner-type combinations gives
\[
\frac{C_{p,q}}{S_pS_q}\longrightarrow
\frac12+\frac12\bigl(\theta^2+(1-\theta)^2\bigr)
=1-\theta(1-\theta).
\]
Together with \(p^2S_p\to2\) and \(q^2S_q\to2\), this proves both stated limits. The elementary quadratic \(1-\theta(1-\theta)\) has unique minimum \(3/4\) at \(\theta=1/2\), proving the asserted sharp balance effect.

## Verification

The standalone `CHECK.py` uses only the Python standard library. It implements the exact factorial sum with rational arithmetic and independently enumerates all rank permutations on small double-star trees to compute the sum of squared orientation-class probabilities. It also checks the one-hub formula and several exact rational values. Run `python CHECK.py` to reproduce its output. This finite computation tests the exact finite formula in sample cases; the all-parameter statements and limits are justified by the proof above, not by numerical extrapolation.

## Relationship to prior work

Padrol, Pilaud and Poullot develop the deformation theory, graphical fans, and combinatorics of graphical zonotopes, providing the lead geometric setting; their results concern deformation cones rather than the squared Gaussian normal-cone weights in the present double-star family. Stinson, Gleich and Constantine establish the general correspondence between randomized Gaussian zonotope-vertex selection and normal-cone probabilities; that general algorithmic principle is used here, not claimed anew. Mallows and Shepp studied the same-up/down comparison phenomenon on a **path** (equivalently path-tree orientation agreements); this covers the path-special cases and motivates excluding a standalone path collision result, but it does not state the present two-hub asymptotic in the available inspected material. The one-hub star identity is included only as a benchmark and is not asserted to be a novel separate result. Results about bistar **symmetric edge polytopes** concern a different convex body. The new scope is the exact two-hub collision law and its sharp asymptotic central-edge coupling factor.

## Limitations

The asymptotic requires \(p\to\infty\) and \(q\to\infty\); it does not supply a uniform finite-size remainder or a result when one leaf count stays fixed. It concerns ordinary isotropic Euclidean Gaussian objectives and the unweighted coordinate-root realization; an arbitrary affine transformation changes normal-cone probabilities. The finite sum does not claim a uniformly efficient large-parameter evaluation algorithm. Published literature may contain an unindexed equivalent formulation under random tree orderings, linear extensions or cone-angle Rényi entropy. Independent mathematical validation is not asserted.

## References

1. A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first posted 2021-11-24; *Discrete & Computational Geometry* 73 (2025), 447–465. https://arxiv.org/abs/2111.12422
2. K. Stinson, D. F. Gleich, P. G. Constantine, *A randomized algorithm for enumerating zonotope vertices*, arXiv:1602.06620 (2016). https://arxiv.org/abs/1602.06620
3. C. L. Mallows, L. A. Shepp, *Enumerating pairs of permutations with the same up-down form*, *Discrete Mathematics* 54 (1985), 301–311. https://dblp.org/rec/journals/dm/MallowsS85
