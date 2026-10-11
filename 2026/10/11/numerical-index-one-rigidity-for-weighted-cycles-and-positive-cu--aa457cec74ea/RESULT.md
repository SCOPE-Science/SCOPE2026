# Numerical-index-one rigidity for weighted cycles and positive cube sections

## Finding
Fix any integer \(m\ge4\) and arbitrary strictly positive real numbers \(w_1,\ldots,w_m\). Write \(W=\sum_{i=1}^{m}w_i\) and consider the real Banach space
\[
Y_w=\{u\in\mathbb R^m:\sum_{i=1}^{m}w_i u_i=0\},\qquad \|u\|=\max_i|u_i|.
\]
Its numerical index equals one **if and only if**
\[
\boxed{\ \mathfrak n(Y_w)=1\quad\Longleftrightarrow\quad
2\max_i w_i\ge W\quad\text{or}\quad
\big(m\text{ is even and }w_1=\cdots=w_m\big).\ }
\]
Let \(C_m(w)\) be the finite metric space formed from a simple cycle with consecutive positive edge lengths \(w_1,\ldots,w_m\), equipped with its shortest-path metric. For the real Lipschitz-free space, precisely the same dichotomy holds:
\[
\boxed{\ \mathfrak n(\mathcal F(C_m(w)))=1\quad\Longleftrightarrow\quad
2\max_i w_i\ge W\quad\text{or}\quad
\big(m\text{ is even and all }w_i\text{ are equal}\big).\ }
\]
In particular, among genuine weighted cycles satisfying \(2w_i<W\) for every edge, only the equal-edge even cycles have numerical index one. In the equal-edge even-cycle case, every sufficiently small nonuniform positive perturbation makes the numerical index strictly below one, despite preserving the cycle graph.

## Assumptions and scope
All spaces and numerical radii are over the real scalars, and all edge lengths are positive; the number of vertices is \(m\ge4\). Define
\[
\mathfrak n(X)=\inf_{\|T\|=1}v(T),\qquad
v(T)=\sup\{|x^*(Tx)|:x\in S_X,\ x^*\in S_{X^*},\ x^*(x)=1\}.
\]
The graph metric is the minimum total edge length among paths, so an edge longer than the complementary path may be metrically redundant. For a finite metric space, \(\mathcal F(M)^*=\operatorname{Lip}_0(M)\) isometrically. We invoke the finite-dimensional McGregor criterion: \(\mathfrak n(X)=1\) precisely when \(|f(x)|=1\) for **every** extreme \(x\in B_X\) and every extreme \(f\in B_{X^*}\).

## Proof
**1. Weighted cycle as a cube hyperplane.** Orient the edges cyclically, from \(v_i\) to \(v_{i+1}\), with indices modulo \(m\). For a real-valued function \(f\) vanishing at a fixed base vertex, put \(u_i=(f(v_{i+1})-f(v_i))/w_i\). Telescoping gives \(\sum_i w_i u_i=0\). Conversely, every vector satisfying that equation integrates uniquely to such an \(f\). The graph's shortest-path metric has the property
\[
\|f\|_{\mathrm{Lip}}=\max_i\frac{|f(v_{i+1})-f(v_i)|}{w_i}=\max_i|u_i|.
\]
For the upper bound, sum edge increments along a shortest path; the lower bound follows because each path edge connects two graph vertices whose distance does not exceed its assigned length. Thus \(\operatorname{Lip}_0(C_m(w))\cong Y_w\), and \(\mathcal F(C_m(w))\cong Y_w^*\). In finite dimensions \(\mathfrak n(X)=\mathfrak n(X^*)\): transpose is a norm-preserving bijection on all operators and preserves their numerical radii, since the same norming pairs are exchanged by biduality. The cycle assertion therefore reduces exactly to the hyperplane assertion.

**2. A metrically redundant edge.** Suppose \(2w_k\ge W\). Eliminating \(u_k\) gives
\[
u_k=-\frac{\sum_{j\ne k}w_j u_j}{w_k},\qquad
|u_k|\le\frac{W-w_k}{w_k}\max_{j\ne k}|u_j|\le\max_{j\ne k}|u_j|.
\]
The projection onto the other \(m-1\) coordinates is consequently a surjective linear isometry \(Y_w\cong\ell_\infty^{m-1}\). Hence \(\mathfrak n(Y_w)=1\). Geometrically, the long edge contributes no shorter route than its complementary path, and the free space is \(\ell_1^{m-1}\).

**3. Vertices and dual facets for genuine cycles.** Now assume \(2w_i<W\) for all \(i\). The unit ball of \(Y_w\) is \(Y_w\cap[-1,1]^m\). A vector in that section is a vertex exactly when at most one coordinate has modulus strictly below one: if two coordinates are free, a nonzero small perturbation supported on them preserves both the weighted hyperplane equation and all strict coordinate inequalities; if at least \(m-1\) coordinates are fixed to signs, the weighted equation determines the last one uniquely. The dual unit ball is
\[
B_{Y_w^*}=\operatorname{conv}\{\pm e_i^*|_{Y_w}:1\le i\le m\}.
\]
Furthermore, each positive restricted coordinate functional \(e_i^*|_{Y_w}\) is **exposed** in this dual ball. Indeed, the unit vector \(q\in Y_w\) given by \(q_i=1\) and \(q_j=-w_i/(W-w_i)\) for \(j\ne i\) evaluates \(e_i^*\) to one and every other signed coordinate functional to an absolute value strictly below one. Consequently, failure of \(|u_i|=1\) at any cube-section vertex \(u\) implies \(\mathfrak n(Y_w)<1\) by McGregor's criterion.

**4. Equal weights.** If all weights are equal and \(m\) is even, fix \(m-1\) vertex coordinates to signs. Their sum is an odd integer, so the remaining coordinate, which negates this sum, can lie in \([-1,1]\) only if it is \(1\) or \(-1\). Thus every vertex has **all** coordinates of modulus one. All dual extreme points belong to the signed restricted coordinate family above; McGregor gives \(\mathfrak n(Y_w)=1\). If all weights are equal and \(m\) is odd, fix among the other \(m-1\) coordinates half to \(1\) and half to \(-1\), leaving \(u_i=0\). This vector is a vertex, while \(e_i^*|_{Y_w}\) is an exposed dual point. Therefore \(\mathfrak n(Y_w)<1\).

**5. Unequal weights.** Assume the weights are not all equal and all \(2w_i<W\). Choose \(i\) with maximal weight \(a=w_i\). Consider the remaining weights. First assign alternating signs to all those **equal** to \(a\), leaving signed partial sum either \(0\) or \(a\). At least one remaining weight \(b\) is strictly smaller than \(a\). Give \(b\) the opposite sign if the current sum is \(a\), and either sign if it is zero: the new absolute sum is strictly less than \(a\). Process every further smaller weight \(c<a\), each time choosing its sign opposite the current partial sum (arbitrarily if zero). The update of the absolute partial sum from \(r<a\) is \(|r-c|<a\). In the end, the signed sum \(S\) of all weights other than \(a\) satisfies \(|S|<a\). Fix their coordinates to their chosen signs and put \(u_i=-S/a\). Then \(u\in Y_w\cap[-1,1]^m\) is a vertex with \(|u_i|<1\). The exposed dual coordinate functional from step 3 yields a strict McGregor obstruction and \(\mathfrak n(Y_w)<1\). This exhausts all cases and proves the classification.

## Verification
The proof is finite-dimensional and applies to every admissible real weight vector, not just rational ones. The accompanying stand-alone Python 3 checker `verify.py` enumerates cube-section vertices in exact rational arithmetic for every weight vector with \(m=4,5,6\) and individual integer weights in \(\{1,2,3\}\). It checks the complete McGregor vertex/dual-coordinate criterion against the stated alternative. Its replay output is:

`VERIFY_OK rational_weight_vectors=1053 cube_vertices=42302 dimensions=4..6 weights=1..3`

These finitely many computations corroborate the combinatorial argument; the result for all dimensions and positive real weights follows only from the analytic proof.

## Relationship to prior work
Cobollo, Guirao and Montesinos (2023) compute the numerical index of every two-dimensional real Lipschitz-free space, covering weighted **triangles** (three-point metric spaces); this result is expressly restricted to cycles on at least four vertices. The published equal-edge cycle parity computation establishes the numerical index of unit-edge cycles, and the published graph bipartiteness criterion applies to **unit-length** graph metrics. Neither statement implies the classification over every positive weight vector: in particular an even cycle ceases to have index one under any nonuniform genuine weighting. Aliaga (2021) provides the extremal framework for finite compact metric free spaces; McGregor's classical finite-dimensional extreme-point criterion supplies the numerical-index test. Sain, Paul, Bhunia and Bag (2018) give a general polyhedral bound and selected three-dimensional calculations but do not derive this positive-normal hyperplane rigidity classification. The weighted-cycle isometry literature addresses a different invariant. The conclusion is a complete qualitative phase diagram rather than an exact formula for the numerical index below one.

## Limitations
Only real scalars, finite simple cycles with at least four vertices, and strictly positive edge lengths are addressed. If the dichotomy fails, the theorem proves \(\mathfrak n<1\) but does not compute its exact value. No quantitative stability gap uniform over weights is claimed: the numerical index may approach one as nonuniform weights approach equality. A full comparison against every unindexed equivalent formulation in transportation-cost or polyhedral geometry literature is not established; the identified relevant full texts and published special cases were examined.

## References
1. Ch. Cobollo, A. J. Guirao, V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1 (first public 2023-04-25), https://arxiv.org/html/2304.13183v1.
2. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219v2 (first public 2021-02-01), https://arxiv.org/html/2102.01219v2.
3. C. M. McGregor, *Finite-Dimensional Normed Linear Spaces with Numerical Index 1*, J. London Math. Soc. (1971), DOI 10.1112/jlms/s2-3.4.717.
4. D. Sain, K. Paul, P. Bhunia, S. Bag, *On the numerical index of polyhedral Banach spaces*, arXiv:1809.04778v2, https://arxiv.org/html/1809.04778v2.
5. S. Pal, S. Roy, D. Sain, *A characterization of Banach spaces with numerical index one*, arXiv:2604.03690v1 (2026), https://arxiv.org/html/2604.03690v1, Theorem 1.1 and Corollary 2.12 (a fully accessible proof of McGregor's criterion).
6. M. Cúth, M. Doucha, T. Titkos, *Isometries of Lipschitz-free Banach spaces*, J. London Math. Soc. 110 (2024), e70000, DOI 10.1112/jlms.70000.
7. *Numerical-index parity law for Lipschitz-free spaces over cycles*, publicly available mathematical result (2026), with exactly unit edge lengths.
8. *Bipartiteness exactly characterizes numerical index one for finite graph metrics*, publicly available mathematical result (2026), for unit-edge graph metrics.
