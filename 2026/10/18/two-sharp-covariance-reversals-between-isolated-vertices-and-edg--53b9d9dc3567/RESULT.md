# Two sharp covariance reversals between isolated vertices and edges in circular random geometric graphs

## Finding

Fix any integer \(n\ge2\). Choose \(n\) labeled, independent uniformly distributed positions on the unit circle \(\mathbb R/\mathbb Z\). Put an edge between two vertices precisely when their shorter circular distance is at most \(r\), where \(0<r<1/2\). Let \(I\) count isolated vertices and let \(E\) count all graph edges.

Write \(L=1-2r\) and
\[
q(r)=\begin{cases}
\dfrac{2r}{L}-\dfrac{r^2}{L^2},&0<r\le1/3,\\[4pt]
1,&1/3\le r<1/2.
\end{cases}
\]
The following exact identity holds for every stated \(n\) and \(r\):
\[
\boxed{\operatorname{Cov}(I,E)=\binom n2 L^{n-1}\bigl((n-2)q(r)-2nr\bigr).}\tag{1}
\]
It has a complete sign classification:

* For \(2\le n\le5\), the covariance is strictly **negative** for all \(0<r<1/2\).
* For \(n\ge6\), let
\[
 r_-(n)=\frac{3n+10-\sqrt{9n^2-68n+100}}{16n},\qquad
 r_+(n)=\frac{n-2}{2n}.
\]
Then the covariance is strictly **positive** precisely when \(r_-(n)<r<r_+(n)\), vanishes precisely at \(r=r_-(n)\) and \(r=r_+(n)\), and is strictly negative for all other \(0<r<1/2\). At the first admissible positive size, \(n=6\), the positive interval is exactly \((1/4,1/3)\); in particular
\[
\operatorname{Cov}(I,E)\big|_{n=6,r=3/10}=\frac{72}{3125}>0.
\]
The asymptotic endpoints are \(r_-(n)\sim4/(3n)\) and \(r_+(n)=1/2-1/n\).

## Assumptions and scope

The model is the **binomial** (fixed-vertex-count), hard-cutoff, one-dimensional periodic random geometric graph. Positions are independent and uniform on the unit circle, repeated positions being a null event. The graph is simple and undirected; at the distance-equality boundary the edge convention makes no difference to probabilities. The theorem covers every finite integer \(n\ge2\) and every real \(r\in(0,1/2)\); no sparse scaling, large-size approximation or assumption of independently sampled edges is made. The random variables \(I\) and \(E\) are counts on **the same sampled geometric graph**.

## Proof

**Conditional concentration of points.** By rotation invariance, fix a marked vertex at position zero. It is isolated if and only if each of the remaining \(n-1\) points lies in the complement of its radius-\(r\) neighbourhood. That complement is one connected arc of length \(L=1-2r\). Therefore, the isolation probability is \(L^{n-1}\), and conditional on isolation, the remaining positions are independent and uniform on that length-\(L\) arc.

**Exact conditional edge probability.** Given two independently uniform points on that arc, let \(S\in[0,L]\) be their ordinary (unwrapped) separation. Its density is \(2(L-s)/L^2\). Because \(s\le L=1-2r<1-r\), a pair of points in the complement cannot be circular neighbours via the other direction around the circle: their shorter circular distance is at most \(r\) if and only if \(S\le r\). Thus if \(r<L\), their conditional edge probability is
\[
\int_0^r\frac{2(L-s)}{L^2}\,ds=\frac{2r}{L}-\frac{r^2}{L^2};
\]
if \(r\ge L\), this probability is one. The transition \(r=L\) occurs exactly at \(r=1/3\). This proves the formula for \(q(r)\).

**Mixed moment.** All edges incident to an isolated marked vertex are absent. Conditional on that event, linearity of expectation gives \(\mathbb E[E\mid \text{marked vertex isolated}]=\binom{n-1}{2}q(r)\). Unconditionally, two independent uniform circular points are within distance \(r\) with probability \(2r\), and therefore \(\mathbb E E=\binom n2(2r)\). Expanding \(I\) into the sum of vertex-isolation indicators yields
\[
\operatorname{Cov}(I,E)=nL^{n-1}\left[\binom{n-1}{2}q(r)-\binom n2(2r)\right],
\]
which is exactly (1).

**Sign and the sharp size threshold.** Since the prefactor in (1) is strictly positive, the sign is that of
\[
B_n(r)=(n-2)q(r)-2nr=n(q(r)-2r)-2q(r).
\]
For \(r\le1/3\), one has \(q(r)-2r=r^2(3-8r)/L^2>0\); for \(r\ge1/3\), one has \(q(r)-2r=L>0\). Thus \(B_n(r)\) is strictly increasing as a function of integer \(n\), for each fixed radius. When \(r\le1/3\),
\[
B_5(r)=\frac{r}{L^2}(-40r^2+25r-4)<0,
\]
since the quadratic has negative discriminant \(25^2-4\cdot40\cdot4=-15\) and negative leading coefficient. When \(r\ge1/3\), \(B_5(r)=5L-2\le-1/3<0\). The monotonicity in \(n\) proves negativity for every \(2\le n\le5\).

For \(n\ge6\) and \(r\le1/3\), the exact identity
\[
B_n(r)=\frac{r}{L^2}\left[-8nr^2+(3n+10)r-4\right]
\]
reduces the sign to a concave quadratic with discriminant \(9n^2-68n+100>0\). Its smaller zero is \(r_-(n)\); the other zero equals \(1/3\) at \(n=6\) and lies strictly above \(1/3\) at \(n>6\), because the quadratic at \(r=1/3\) equals \((n-6)/9\). For \(r\ge1/3\), \(B_n(r)=n(1-2r)-2\), whose unique zero is \(r_+(n)=(n-2)/(2n)\). These formulas fit continuously at \(r=1/3\), and yield exactly the two reversals claimed above, with no other roots. Substituting \(n=6,r=3/10\) into (1) gives \(72/3125\). A first-order expansion of the quadratic root gives \(r_-(n)\sim4/(3n)\), while the displayed \(r_+(n)\) is already exact. This completes the proof.

## Verification

The standalone standard-library program `verify.py` independently checks two rational versions of (1) and their signs over \(n=2,\dots,34\) and nine representative rational radii, exact zeros of the upper boundary, and the positive six-vertex witness. It additionally enumerates complete graphs on small discrete circular grids and checks the covariance against an independently evaluated triple-point count; finer-grid checks compare this separate discretization with the continuum formula. All 653 checks pass. These finite checks are supplementary: the unrestricted theorem follows from the preceding integral and algebra, not extrapolation from enumeration.

## Relationship to prior work

Last, Nestmann and Schulte (arXiv:1808.01203, posted 2018-08-03) study second-order **Poisson** random-connection-model component counts and normal approximations in Euclidean space. Their objects are components rather than the full edge count, and their principal covariance results are in a growing-window regime, not the finite binomial circle or the present two sign boundaries.

Badiu and Coon (arXiv:2107.13495, posted 2021-07-28) study structures and entropy of one-dimensional random geometric graphs on an **interval**, with different graph statistics; their results do not imply a fixed-size circular isolation/edge covariance sign phase diagram.

Wilsher, Dettmann and Ganesh (arXiv:2202.08044, posted 2022-02-16) study isolated-node count limits for **soft** random geometric graphs with periodic boundaries. Their theorem assumes a connection function whose squared integral is strictly smaller than its integral; they explicitly observe that the hard-cutoff model fails that assumption. Their theorem does not supply the claimed finite-size joint moment or sign reversals.

The conditioning argument uses familiar occupancy and elementary geometric-probability ideas. The assertion of new content is limited to their resulting sharp all-size covariance phase diagram and the first positive-size threshold, not generic graph definitions or isolation expectations. Relevant historical literature may contain an equivalent mixed-moment identity; a search failure alone does not establish priority.

## Limitations

The theorem concerns one-dimensional *periodic*, **fixed-\(n\)** hard random geometric graphs with uniformly sampled points. It does not claim corresponding sign laws for line intervals with boundaries, soft random connections, Poisson sample sizes, nonuniform spatial densities, higher dimensions or other graph statistics. All statements are unconditional expectations/covariances; no assertion of independence or of a distributional limit is made. Historical novelty is assessed against identified literature, not certified by an independent exhaustive priority audit.

## References

1. G. Last, F. Nestmann, M. Schulte, *The random connection model and functions of edge-marked Poisson processes: second order properties and normal approximation*, arXiv:1808.01203 (first public version 2018-08-03).
2. M.-A. Badiu, J. P. Coon, *Structural Complexity of One-Dimensional Random Geometric Graphs*, arXiv:2107.13495 (first public version 2021-07-28).
3. M. Wilsher, C. Dettmann, A. Ganesh, *The Distribution of the Number of Isolated Nodes in the 1-Dimensional Soft Random Geometric Graph*, arXiv:2202.08044 (first public version 2022-02-16).
