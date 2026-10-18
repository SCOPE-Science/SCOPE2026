# Sharp balance law for Mahler products of complete-bipartite transportation spaces

## Finding
For integers \(p,q\ge1\), put \(N=p+q\) and \(d=N-1\). Give the vertex set of \(K_{p,q}\) its unit-edge shortest-path metric. Let \(P_{p,q}\) denote the unit ball of its real Lipschitz-free space and \(Q_{p,q}=P_{p,q}^{\circ}\) its dual Lipschitz ball. Use the dual coordinate system in which one potential in the first part is fixed to zero and all other potentials are free; volumes below refer to this coordinate system and its dual, so their product is intrinsic.

Define
\[
H_{p,q}=\sum_{k=0}^{\min(p-1,q-1)}\binom{p-1}{k}\binom{q-1}{k}\frac{\binom{2k}{k}}{4^k}.
\]
The exact individual volumes are
\[
\operatorname{vol}_d(P_{p,q})=\frac{2^d}{d!}H_{p,q},\qquad
\operatorname{vol}_d(Q_{p,q})=\frac{2^d p!q!}{d!}.
\]
Thus the Mahler product, normalized by the Hanner-polytope benchmark, is
\[
R(p,q):=\frac{d!\,\operatorname{vol}_d(P_{p,q})\operatorname{vol}_d(Q_{p,q})}{4^d}
=\frac{N}{\binom Np}H_{p,q}.
\]

**Sharp fixed-size balance law.** For each fixed \(N\ge6\), the product is strictly larger when an unbalanced partition with \(2\le p\le q-2\) is replaced by \((p+1,q-1)\). It equals the Hanner benchmark if and only if \(\min(p,q)\le2\); it exceeds that value whenever both parts have at least three vertices. Consequently the unique maximizing unordered bipartition is \(\{\lfloor N/2\rfloor,\lceil N/2\rceil\}\), and the minimizing unordered bipartitions are precisely those with smaller part one or two. For \(N\le5\), every bipartition has the same Hanner-benchmark product.

For fixed \(p\ge1\), a further exact asymptotic is
\[
\lim_{q\to\infty}R(p,q)=p\frac{\binom{2p-2}{p-1}}{4^{p-1}},
\]
whose value grows as \(\sqrt{p/\pi}\) when \(p\to\infty\) *after taking the fixed-\(p\) limit*. The previously published bipartite symmetric-edge Ehrhart formula supplies the primal-volume formula; the new result here is the dual-volume evaluation together with the sharp strict balancing and equality classification for their product.

## Assumptions and scope
All parameters are integers at least one. The graph metric has cross-part distance one and within-part distance two (except when a part is a singleton). The polytope is \(P_{p,q}=\operatorname{conv}\{\pm(e_a-e_b):a\in A,b\in B\}\) in the zero-sum hyperplane. The dual unit ball consists of functions \(f\) satisfying \(|f(a)-f(b)|\le1\) on every edge. One vertex of \(A\) is anchored to zero. The primal volume uses the linear-dual basis, not an unrelated Euclidean orthonormal basis, ensuring that the product is basis independent. All integrations have ordinary Lebesgue measure in these chosen coordinates.

## Proof
**1. Exact dual volume.** Fix \(f(a_0)=0\) for one vertex of the first part. Write \(u\) for the remaining \(p-1\) first-part potentials and \(v\) for the \(q\) second-part potentials. The constraints are \(|u_i-v_j|\le1\), along with \(|v_j|\le1\), for every \(i,j\). If the span of all \(p\) first-part potentials is \(r\), then \(0\le r\le2\), and the admissible interval for each \(v_j\) has length \(2-r\). For \(p\ge2\), the push-forward of anchored Lebesgue measure by the range \(r\) has density \(p(p-1)r^{p-2}\): the measure of anchored \((p-1)\)-tuples of range at most \(r\) is \(p r^{p-1}\), by partitioning according to which coordinate is minimal or maximal. Hence the beta integral gives
\[
\operatorname{vol}_d(Q_{p,q})=p(p-1)\int_0^2 r^{p-2}(2-r)^q\,dr
=\frac{2^d p!q!}{d!}.
\]
For \(p=1\), the ball is exactly \([-1,1]^q\), with the same volume formula.

**2. Primal volume with an independent slice check.** The lattice volume formula for symmetric edge polytopes of \(K_{p,q}\) is the specialization at one of Higashitani–Jochemko–Michałek's explicit \(h^*\)-polynomial (reference [2]): for \(d=p+q-1\), their formula is
\[
h^*(z)=\sum_{k=0}^{\min(p-1,q-1)}\binom{2k}{k}\binom{p-1}{k}\binom{q-1}{k}z^k(1+z)^{d-2k}.
\]
Its value at \(z=1\) is the normalized lattice volume \(d!\operatorname{vol}_d(P_{p,q})=2^dH_{p,q}\). Thus this volume itself is already established in that paper and is not claimed as a new result.

A second direct integral confirms the coordinate normalization without Ehrhart theory. Slice the zero-sum molecule ball at the total first-part mass \(t\in[-1,1]\). Setting \(\lambda=(1+t)/2\) and \(\mu=(1-t)/2\), the slice is affinely \((\lambda\Delta_{p-1}-\mu\Delta_{p-1})\times(\mu\Delta_{q-1}-\lambda\Delta_{q-1})\). For the standard simplex \(\Delta_r\), splitting by the signs of its coordinates gives
\[
\operatorname{vol}_r(\lambda\Delta_r-\mu\Delta_r)=\frac1{r!}\sum_{i=0}^r\binom ri^2\lambda^i\mu^{r-i}.
\]
Integrating the product across \(t\in[-1,1]\) yields an exact independent finite expression
\[
\operatorname{vol}_d(P_{p,q})=
\frac{2}{(p-1)!(q-1)!d!}
\sum_{i=0}^{p-1}\sum_{j=0}^{q-1}\binom{p-1}{i}^{\!2}\binom{q-1}{j}^{\!2}(i+j)!(d-1-i-j)!.
\]
The two formulas agree by the cited Ehrhart theorem; `verify.py` also confirms their equality by exact arithmetic across many independent cases. This calculation is a normalization check, not a substitute for the general published \(h^*\) identity.

**3. A positive-weight single-crossing lemma.** Put \(w_k=\binom{2k}{k}/4^k\) and \(s_k=(k+1)w_k\). The sequence is nondecreasing: \(s_0=s_1=1\), and
\[
\frac{s_{k+1}}{s_k}=1+\frac{k}{2(k+1)^2}>1\quad(k\ge1).
\]
The beta/Vandermonde identity
\[
\sum_{k\ge0}\frac{\binom{p-1}{k}\binom{q-1}{k}}{k+1}=\frac{\binom{p+q}{p}}{p+q}
\]
shows that replacing every \(w_k\) in \(H_{p,q}\) by \(1/(k+1)\) gives normalized Mahler ratio exactly one. Because \(s_k=1\) only for \(k=0,1\), this proves \(R(p,q)=1\) if \(\min(p,q)\le2\), and \(R(p,q)>1\) otherwise.

Now fix \(2\le p\le q-2\), and put \(N=p+q\). Compare the normalized products for the adjacent splits \((p,q)\) and \((p+1,q-1)\). Define, for \(0\le k\le p\),
\[
D_k=(p+1)\binom pk\binom{q-2}k-q\binom{p-1}k\binom{q-1}k,
\]
with out-of-range binomial coefficients equal to zero. The preceding Vandermonde identity gives \(\sum_kD_k/(k+1)=0\). For \(k<p\), direct cancellation gives
\[
D_k=\binom{p-1}k\binom{q-2}k
\frac{(q-p-1)\bigl(kN-p(q-1)\bigr)}{(p-k)(q-1-k)}.
\]
The factor outside the last numerator is nonnegative, so these coefficients switch sign at most once, from nonpositive to nonnegative, as \(k\) grows; moreover \(D_0<0\), while \(D_p>0\). Therefore a strictly larger weight \(s_k\) on a positive tail than on a negative initial block gives
\[
\sum_{k=0}^p w_kD_k
=\sum_{k=0}^p \frac{D_k}{k+1}s_k>0.
\]
Strictness follows because some positive coefficient has index at least two, where \(s_k>1=s_0\). Finally, direct common-denominator algebra gives
\[
R(p+1,q-1)-R(p,q)=\frac{N}{q\binom Np}\sum_{k=0}^p w_kD_k>0.
\]
This proves the entire strict balancing law, including every tie/equality case.

**4. One-sided asymptotic.** For fixed \(p\), \(H_{p,q}\) is a polynomial of degree \(p-1\) in \(q\), with leading coefficient \(w_{p-1}/(p-1)!\). Also \(\binom{p+q}{p}\sim q^p/p!\). Hence \(R(p,q)\to p w_{p-1}\). The central binomial asymptotic gives the stated second-order growth in \(p\).

## Verification
The standalone standard-library program `verify.py` checks exact equality of the two primal-volume formulas and the product normalization for all \(1\le p,q\le9\): 81 exact cases. It checks strict balancing and the sign-change certificate in 64 integer cases with total sizes through 20. When NumPy and SciPy are installed, eight additional cases independently reconstruct primal convex hulls and dual halfspace-intersection polytopes and compare their numeric volumes with the exact fractions. All three groups passed before packaging. These finite checks test the proof and coordinate conventions; they are not an infinite-family proof.

Some normalized exact values at \(N=8\): \(R(1,7)=R(2,6)=1\), \(R(3,5)=29/28\), and \(R(4,4)=21/20\). At \(N=6\), the balanced split has \(R(3,3)=81/80\).

## Relationship to prior work
The primal symmetric-edge volume is **not new**: Higashitani–Jochemko–Michałek [2] explicitly determined its full Ehrhart \(h^*\)-polynomial. Alexander–Fradelizi–García-Lirola–Zvavitch [3] initiated a systematic analysis of Mahler products of finite Lipschitz-free spaces and characterized the relevant Hanner configurations, including the thin bipartite spiderweb case. Aliaga–Guirao [1] supplies the Banach-space extreme-molecule context. This result concerns the *combined polar-primal Mahler product* as the bipartition changes at fixed dimension, including strict maximizers and exact equality classes. The cited works establish important ingredients and low-dimensional equalities but do not state or prove this balancing comparison. D’Alì–Delucchi–Michałek [4] provides related symmetric-edge and duality background. A separately published signed-chain-polytope volume result for the graph formed by adjoining a universal vertex to \(K_{p,q}\) concerns a different rooted graph and a different polytope; its imbalance theorem does not imply the present intrinsic Mahler balancing theorem.

## Limitations
The optimizing statement is restricted to the complete-bipartite **unweighted graph metrics** at a fixed number of vertices; it is not a global maximization over all finite metric spaces. Only the joint Mahler product and the new polar formula are claimed as contributions; the primal volume was previously known. The proof does not classify arbitrary weighted bipartite graphs, other graph families or nonsymmetric metric deformations. The originality assessment relies on accessible primary literature and targeted mathematical-record searches and does not exclude an equivalent unindexed treatment. Independent scientific audit has not been conducted.

## References
[1] R. J. Aliaga and A. J. Guirao, On the preserved extremal structure of Lipschitz-free spaces, arXiv:1705.09579v1, 2017-05-26, https://arxiv.org/abs/1705.09579 (MSC 46B20).

[2] A. Higashitani, K. Jochemko and M. Michałek, Arithmetic Aspects of Symmetric Edge Polytopes, arXiv:1807.07678v1, 2018-07-20, https://arxiv.org/pdf/1807.07678 (Theorem 4.1; opening theorem on p. 2).

[3] M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, Geometry and volume product of finite dimensional Lipschitz-free spaces, arXiv:1911.10642, first publicly posted 2019-11-24, https://arxiv.org/pdf/1911.10642 (Sections 3, 5).

[4] A. D’Alì, E. Delucchi and M. Michałek, Many Faces of Symmetric Edge Polytopes, arXiv:1910.05193, https://arxiv.org/abs/1910.05193.
