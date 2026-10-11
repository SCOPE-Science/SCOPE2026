# Exact numerical index \(14/17\) for a singly shortened six-cycle
## Finding
Let \(M=\{v_0,v_1,v_2,v_3,v_4,v_5\}\) be the weighted six-cycle, with cyclically consecutive edge lengths \(1,2,2,2,2,2\), and shortest-path distance. For its five-dimensional **real** Lipschitz-free Banach space \(X=\mathcal F(M)\),
\[
n(X)=\frac{14}{17}.
\]
The constant is sharp: a concrete nonzero operator has \(\|T\|/v(T)=17/14\). This determines a natural weighted-even-cycle test case in which the numerical index is strictly below \(1\), in contrast to the unit-edge even-cycle family.

## Assumptions and scope
All spaces and operators are real. The vertices are distinct, edges carry the stated positive lengths, and distances are shortest-path distances. The normalization of the numerical index is
\[
n(X)=\inf_{\|T\|=1}v(T),\qquad
v(T)=\sup\{|f(Tx)|:\|x\|=\|f\|=f(x)=1\}.
\]
The free space has basis \(\delta(v_1),\ldots,\delta(v_5)\), with \(\delta(v_0)=0\). We use that basis for every operator matrix and finite certificate. Only this specific metric is claimed; no interpolation law for arbitrary weighted cycles is asserted.

## Proof
**1. Dual description and exhaustive vertices.** A Lipschitz function \(f(v_0)=0\) is represented by five coordinates \(f(v_1),\ldots,f(v_5)\). Write cyclic edge differences \(d_i=f(v_{i+1})-f(v_i)\), where \(v_6=v_0\). The dual unit ball is precisely
\[
\left\{f:\sum_{i=0}^{5}d_i=0,\quad |d_i|\le w_i\ (0\le i\le5)\right\},
\quad (w_0,w_1,w_2,w_3,w_4,w_5)=(1,2,2,2,2,2).
\]
All vertex-to-vertex Lipschitz inequalities follow by summation along shortest paths, so no extra inequalities occur. This is a five-dimensional section of a six-dimensional box. Every vertex has at least five saturated edge inequalities: if at most four were active, there would be a nonzero zero-sum perturbation supported on unsaturated coordinates. Conversely, any feasible solution obtained by fixing five distinct edge differences to signed edge lengths is a vertex. The exact enumeration in the companion certificate, verified independently from these rules by `c6_verify_exact.py`, yields **60** distinct dual vertices, listed in `c6_exact_certificate.json` as five-dimensional evaluation vectors.

**2. Primal vertices.** Write
\[
u_i=\frac{\delta(v_i)-\delta(v_{i+1})}{w_i},\qquad 0\le i\le5.
\]
The primal unit ball is \(\operatorname{conv}\{\pm u_i:0\le i\le5\}\): every normalized point-pair molecule decomposes as a convex combination of signed edge molecules along a shortest path. Each edge length is strictly shorter than the complementary five-edge path, so each signed edge molecule is exposed: a zero-sum edge-difference vector that saturates this edge and has strict inequalities on the other five exposes it. Thus the **12** displayed molecules are precisely the primal vertices. The certificate stores their coordinates as exact rational pairs.

**3. Finite tensor reduction.** For a primal vertex \(u\) and a dual vertex \(f\), let \(C(f,u)\) be the row-major vectorization of the rank-one matrix with entries \(f_i u_j\). For an operator \(T\), the dot product of the tensor with its row-major matrix is \(f(Tu)\). The operator norm satisfies
\[
\|T\|=\max_{u,f}|f(Tu)|.
\]
The numerical radius satisfies the same maximum restricted to the norming contacts \(f(u)=1\). Indeed, for an arbitrary norming pair, decompose the primal point into vertices in the exposed face defined by its functional; then decompose that functional into extreme points of the corresponding dual exposed face. Convexity twice does not decrease the maximum absolute evaluation. This is the finite-dimensional extreme-pair formula, also stated as equation (1) in Cobollo--Guirao--Montesinos [1]. Exact enumeration produces **360** distinct norm tensors and **150** distinct norming-contact tensors.

**4. Universal upper comparison.** The certificate contains, for each of the 360 norm tensors \(C\), an explicit identity
\[
C=\sum_{j=1}^{150}a_jB_j,\qquad
\sum_{j=1}^{150}|a_j|\le\frac{17}{14},
\]
where \(B_j\) ranges over the 150 contact tensors. All coefficients are exact rationals; each identity uses at most five nonzero summands. The standalone checker re-enumerates both tensor collections from the weighted metric and tests every coordinate of all 360 identities with rational arithmetic. It also verifies that the maximal coefficient total is exactly \(17/14\). Thus for every real operator,
\[
\|T\|=\max_C|C\cdot T|\le\frac{17}{14}\max_B|B\cdot T|
=\frac{17}{14}v(T),
\]
so \(n(X)\ge14/17\).

**5. Attaining operator.** In the declared ordered basis, take the rational operator
\[
T=\begin{pmatrix}
1&8/7&32/49&0&0\\
0&-1/7&0&0&0\\
0&0&25/49&-8/49&0\\
0&4/7&20/49&53/49&4/49\\
0&0&0&0&41/49
\end{pmatrix}.
\]
The checker directly evaluates the 150 contact tensors and 360 norm tensors at this matrix, obtaining **exactly** \(v(T)=1\) and \(\|T\|=17/14\). In particular the witness is nonzero and gives the reverse inequality \(n(X)\le14/17\). Combining the two bounds proves the claim.

## Verification
The two required, self-contained artifacts are `c6_exact_certificate.json` and `c6_verify_exact.py`. With Python 3 (standard library only), run `python3 c6_verify_exact.py c6_exact_certificate.json`. It rederives both polytope vertex sets by exhaustive finite combinatorics, regenerates both tensor sets, checks all 360 rational linear combinations and their coefficient bounds, and checks the sharp witness. Expected output begins `PASS: 60 dual extreme points, 12 primal extreme points` and ends `numerical index 14/17`. All operations used for acceptance of the certificate are exact integer or rational computations; finite enumeration is exhaustive because the complete vertex description is proved above.

## Relationship to prior work
Cobollo, Guirao and Montesinos [1] provide the exact numerical index for three-point metric spaces (two-dimensional free spaces) and the finite-dimensional extreme-pair formula used above; neither determines this five-dimensional six-point metric. Existing published results for unit-edge graph metrics show numerical index \(1\) for even unit cycles and characterize numerical index \(1\) for unweighted bipartite graph metrics [2,3]. Those statements assume **unit** edges and do not imply the result for lengths \(1,2,2,2,2,2\). A separate exact short-edge four-cycle result [4] concerns a three-dimensional space, and does not determine this five-dimensional index. The present value is a benchmark for the first one-edge deformation of the smallest higher even cycle.

## Limitations
The theorem is restricted to real scalars, six vertices and the specific ratio of one unit edge to five edges of length two. The certificate is a finite exact proof only because the complete reduction to 60/12 vertices and 150/360 tensors is proved; it does not establish a formula for arbitrary edge weights, longer cycles, or complex spaces. A general polyhedral numerical-index algorithm exists, so the contribution is the new exact invariant, not a new computational principle. Although relevant published sources and indexed findings were compared, exact equivalent computations in other literature cannot be excluded without further independent review.

## References
[1] Ch. Cobollo, A. J. Guirao and V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1, first posted 2023-04-25, Sections 1 and 5, https://arxiv.org/html/2304.13183v1.

[2] *Numerical-index parity law for Lipschitz-free spaces over cycles*, published mathematical record, 2026. The result concerns **unit-edge cycles only**.

[3] *Bipartiteness exactly characterizes numerical index one for finite graph metrics*, published mathematical record, 2026. The result concerns **unit-edge graph metrics only**.

[4] *Exact numerical index along the short-edge four-cycle deformation*, existing mathematical finding. The domain has four vertices, unlike the present six-vertex metric.
