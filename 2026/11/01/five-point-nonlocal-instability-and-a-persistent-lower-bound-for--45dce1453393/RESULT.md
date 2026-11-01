# Five-point nonlocal instability and a persistent lower bound for convex least-squares projection

## Finding
For each integer \(n\ge2\), let \(\mathcal C_n\subset\mathbb R^n\) be the cone of sequences with nonnegative second differences at equally spaced sites, and let \(Q_n\) be the *Euclidean* nearest-point projector onto \(\mathcal C_n\). Measure perturbations and outputs with the coordinate maximum norm, and write
\[
L_n=\sup_{y\ne z}\frac{\|Q_n(y)-Q_n(z)\|_\infty}{\|y-z\|_\infty}.
\]
The first four values are exact:
\[
\boxed{L_2=1,\quad L_3=\frac43,\quad L_4=\frac75,\quad L_5=\frac{11}{7}.}
\]
At five sites the unique local active-constraint pattern giving \(11/7\) is *separated curvature saturation*: the first and third second differences are zero, while the middle one is strictly positive. The maximizing output coordinate is the middle site. Every pattern with adjacent active second differences has local maximum norm at most \(7/5\).

Moreover, \(L_{n+1}\ge L_n\) for every \(n\ge2\), and an explicit alternating-curvature family gives the nontrivial asymptotic lower bound
\[
\boxed{\liminf_{n\to\infty} L_n\ge 1+\frac1{\sqrt2}.}
\]
This last bound is not asserted to be the optimal limit.

## Assumptions and scope
The underlying space is real \(\mathbb R^n\), the data-fit objective is the unweighted squared Euclidean error, and the feasible cone is
\[
\mathcal C_n=\{x:\ x_i-2x_{i+1}+x_{i+2}\ge0\quad(1\le i\le n-2)\}.
\]
There are no endpoint, sign, or monotonicity constraints on the fitted values. The maximum norm enters only the *two-input Lipschitz quotient*, not the least-squares optimization. The metric projection is unique. The first four values and the five-point maximizing-face claim are exact and global; the asymptotic assertion is a constructive lower bound, not an exact formula for larger \(n\).

## Proof
**1. Active-face formula and completeness.** Let \(D_n\) denote the \((n-2)\)-by-\(n\) second-difference matrix, with row \(i\) having entries \((1,-2,1)\) in columns \(i,i+1,i+2\). Its rows are independent. For each subset \(A\subseteq\{1,\ldots,n-2\}\), write \(B_A\) for the submatrix of active rows and
\[
H_A=I-B_A^T(B_AB_A^T)^{-1}B_A,
\]
with \(H_\varnothing=I\). It is the orthogonal projector onto the linear space where the selected second differences vanish.

On any open region where precisely the constraints in \(A\) are active and the associated positive Karush–Kuhn–Tucker multipliers are strict, \(Q_n(y)=H_Ay\). Every subset \(A\) occurs on a nonempty open region: by surjectivity of \(D_n\), choose \(x\) with second differences zero on \(A\) and one off \(A\), choose all active multipliers strictly positive, and set \(y=x-B_A^T\lambda\). The Euclidean projection optimality condition holds, and its active pattern persists under small perturbations. Since the polyhedral projector is continuous and piecewise linear with these finitely many local matrices, dividing the segment between any two data vectors at cell boundaries proves
\[
\boxed{L_n=\max_{A\subseteq\{1,\ldots,n-2\}}\|H_A\|_{\infty\to\infty}}
=\max_A\max_i\sum_j |(H_A)_{ij}|.
\]
The opposite inequality follows from the full-dimensional realization of each face and a sign perturbation of one maximizing row. The segment argument remains valid if a segment lies on cell boundaries, by approximation through generic segments and continuity.

**2. Exhaustive exact calculation through five sites.** For \(n=2\) there are no inequalities. For \(n=3\), the only nontrivial active matrix has maximum absolute row sum \(4/3\). For \(n=4\), the subsets of its two second differences have maxima \(1\), \(4/3\), \(4/3\), and \(7/5\). At \(n=5\), labeling the three curvature constraints \(1,2,3\), the complete eight-face computation is:

| Active set \(A\) | Absolute row sums of \(H_A\), in site order |
| --- | --- |
| \(\varnothing\) | \(1,1,1,1,1\) |
| \(\{1\}\) | \(4/3,1,4/3,1,1\) |
| \(\{2\}\) | \(1,4/3,1,4/3,1\) |
| \(\{3\}\) | \(1,1,4/3,1,4/3\) |
| \(\{1,2\}\) | \(7/5,1,1,7/5,1\) |
| \(\{1,3\}\) | \(7/5,39/35,11/7,39/35,7/5\) |
| \(\{2,3\}\) | \(1,7/5,1,1,7/5\) |
| \(\{1,2,3\}\) | \(7/5,1,1,1,7/5\) |

For the uniquely maximizing face \(A=\{1,3\}\), direct inversion gives
\[
H_A=\frac1{35}\begin{pmatrix}
29&12&-5&-2&1\\
12&11&10&4&-2\\
-5&10&25&10&-5\\
-2&4&10&11&12\\
1&-2&-5&12&29
\end{pmatrix}.
\]
Its middle absolute row sum is exactly \(55/35=11/7\). No other active set or output row attains it.

**3. An attained finite two-input witness.** Take
\[
 y=(-1,2,-2,3,1),\quad h=(-1,1,1,1,-1),\quad \varepsilon=\frac1{10}.
\]
The two exact Euclidean convex regressions are
\[
Q_5(y)=(0,0,0,1,2),\quad
Q_5(y+\varepsilon h)=\left(-\frac1{14},\frac3{70},\frac{11}{70},\frac{73}{70},\frac{27}{14}\right).
\]
For the first regression, the three second differences are \((0,1,0)\), and both active multipliers equal \(1\). For the second, they are \((0,27/35,0)\), and both active multipliers equal \(36/35\). Thus both projected vectors satisfy the primal and dual optimality conditions. Their difference is \(({-5},3,11,3,{-5})/70\), whereas the input difference has maximum norm \(1/10\). The quotient is \(11/7\).

**4. Persistence with sample size.** For any active subset \(A\) on \(n\) sites, regard the same constraints as a subset on \(n+1\) sites, leaving the new rightmost curvature constraint inactive. The corresponding orthogonal projector is \(H_A\oplus[1]\). Every such face remains realizable by Step 1, so \(L_{n+1}\ge L_n\). In particular the five-point obstruction persists for every \(n\ge5\).

**5. Alternating-curvature lower bound.** For \(m\ge2\), work on \(2m+1\) sites with the selected curvature constraints \(1,3,5,\ldots,2m-1\). Write \(B_m\) for their row matrix and \(S_m=I-B_m^T(B_mB_m^T)^{-1}B_m\). The Gram matrix \(G_m=B_mB_m^T\) has diagonal \(6\), immediate off-diagonals \(1\), and all remaining entries zero. Let \(t_0=1,t_1=6,t_{k+1}=6t_k-t_{k-1}\). Standard elimination, or direct multiplication, gives for zero-based \(0\le i\le j<m\)
\[
(G_m^{-1})_{ij}=(-1)^{i+j}\frac{t_i t_{m-j-1}}{t_m},\qquad
 t_k=\frac{(3+2\sqrt2)^{k+1}-(3-2\sqrt2)^{k+1}}{4\sqrt2}.
\]
Set \(\alpha=3-2\sqrt2\in(0,1)\) and \(c=1/(4\sqrt2)\). As both indices recede from the ends while their difference stays fixed, the inverse converges to the doubly infinite tridiagonal Green matrix \(g_{i-j}=c(-\alpha)^{|i-j|}\). The explicit continuant formula also yields a uniform geometric bound \(C\alpha^{|i-j|}\), allowing termwise convergence of absolute row sums by dominated convergence.

Consider a row of \(S_m\) at an even-positioned coordinate in zero-based indexing, with its distance from both ends tending to infinity. In the infinite Green-kernel limit the corresponding column of \(B_m\) is \(e_{-1}+e_0\), while odd-coordinate columns are \(-2e_j\). Put \(v_j=g_j+g_{j+1}\). Then \(\sum_{j\in\mathbb Z}|v_j|=2c\), because on either side of the midpoint \(|v_j|=c(1-\alpha)\alpha^{\text{distance}}\). The projected row entries on odd coordinates are \(2v_j\), whose absolute sum is \(4c=1/\sqrt2\). On even coordinates the entries are \(\mathbf1_{\{j=0\}}-(v_{j-1}+v_j)\); their absolute sum is
\[
1-2c(1-\alpha)+2\sum_{k\ge1}c(1-\alpha)^2\alpha^{k-1}=1.
\]
Thus these finite active-face rows have norms converging to \(1+1/\sqrt2\). They are legitimate local derivatives of the convex least-squares projector by Step 1. Consequently \(\liminf_{m\to\infty}L_{2m+1}\ge1+1/\sqrt2\), and Step 4 extends this lower bound to the full sequence \(n\to\infty\).

## Verification
Run `python3 verify_convex5.py`. The self-contained exact-rational checker reconstructs every active-face matrix for \(2\le n\le5\), computes all their absolute row sums, proves the unique five-point maximizing face by exhaustive rational comparison, verifies the stated finite-input primal/dual certificates, tests the embedding identity, and checks the alternating tridiagonal inverse for a range of sizes. The checker reports **420 exact-rational assertions passed**. Its finite experiments independently test algebraic identities but are not substituted for the arguments in Steps 1, 4, or 5.

## Relationship to prior work
Meyer (2008, arXiv:0811.1705v1, especially §2 and Proposition 1) develops cone projections for shape-restricted regression splines and describes their facewise linear least-squares structure. This provides methodological context for Step 1 but does not state the five-point maximum-norm Lipschitz value, the separated-curvature extremizer, or the alternating-curvature lower bound. Chen and Wellner (arXiv:1411.4626v1) study rates and limit distributions in convex least-squares estimation, including linear regions, rather than deterministic two-input maximum-norm sensitivity. Yang and Barber (arXiv:1706.01852v1) characterize contraction of *isotonic* (first-difference) regression under suitable norms; the cone here imposes second-difference inequalities, and the slope-coordinate change is not an isometry for the Euclidean least-squares objective or the input maximum norm.

## Limitations
The sharp constant \(11/7\) is established only for five equally spaced unweighted observations. The general lower bound \(1+1/\sqrt2\) need not be the true limiting Lipschitz constant; no upper bound of that size is claimed. Unequal design spacings, observation weights, and other shape constraints are not classified. Earlier unindexed exact finite-dimensional convex-regression sensitivity calculations are a priority risk. The results have not been independently audited.

## References
1. M. C. Meyer, *Inference using shape-restricted regression splines*, Annals of Applied Statistics 2 (2008), 1013–1033; original public preprint arXiv:0811.1705v1, 2008-11-11. https://arxiv.org/abs/0811.1705
2. Y. Chen and J. A. Wellner, *On convex least squares estimation when the truth is linear*, arXiv:1411.4626v1, 2014-11-17; Electronic Journal of Statistics 10 (2016), 171–209. https://arxiv.org/abs/1411.4626
3. F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852v1, 2017-06-06; Electronic Journal of Statistics 13 (2019). https://arxiv.org/abs/1706.01852
