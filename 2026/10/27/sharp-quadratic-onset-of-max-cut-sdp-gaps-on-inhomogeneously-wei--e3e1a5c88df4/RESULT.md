# Sharp quadratic onset of Max-Cut SDP gaps on inhomogeneously weighted odd cycles

## Finding
Fix any even integer \(k\ge 2\) and positive path-edge weights \(b_1,\ldots,b_k\). Add a closing edge of weight \(w>0\) to form the odd cycle \(C_{k+1}\). Let \(\mathrm{MC}(w)\) be the integer maximum-cut value and \(\mathrm{SDP}(w)\) the standard unit-vector semidefinite relaxation, with edge contribution \(c_{ij}(1-\langle u_i,u_j\rangle)/2\). Define
\[
S=\sum_{j=1}^k b_j^{-1},\qquad T=\sum_{j=1}^k b_j^{-3},\qquad D=S^3-T>0,\qquad w_c=S^{-1}.
\]
Then for \(0<w\le w_c\), \(\mathrm{SDP}(w)=\mathrm{MC}(w)=\sum_j b_j\). For \(w\downarrow w_c\) from above,
\[
\boxed{\ \mathrm{SDP}(w)-\mathrm{MC}(w)=\frac{3S^4}{4(S^3-T)}(w-w_c)^2+O((w-w_c)^3).\ }
\]
In particular, \(\mathrm{SDP}(w)>\mathrm{MC}(w)\) for all sufficiently small \(w-w_c>0\). Every optimal vector configuration immediately above \(w_c\), up to orthogonal transformations, has path-edge deviations \(\delta_j\) obeying
\[
\delta_j=\frac{S}{b_j}\sqrt{\frac{6(w-w_c)}{D}}+O((w-w_c)^{3/2}).
\]
At fixed \(S\), the sharp quadratic coefficient is minimized uniquely by equal path weights and is unbounded as one reciprocal weight approaches \(S\) while the others approach zero.

## Assumptions and scope
Vertices are \(0,1,\ldots,k\), path edges \(\{j-1,j\}\) of weights \(b_j\) for \(1\le j\le k\), closing edge \(\{0,k\}\) of weight \(w\). The integer optimum is the largest cut weight over labels in \(\{-1,1\}\); the relaxation replaces labels by unit Euclidean vectors in arbitrary finite dimension. All weights are strictly positive, \(k\) is even, and the asserted expansion is for fixed \(k,b_1,\ldots,b_k\) as \(w\to w_c^+\). The asymptotic remainder may depend on these fixed parameters. This is a local theorem, not a classification for all large \(w\).

## Proof
**1. Critical exactness and localization.** Put \(v_j=(-1)^j u_j\). Since \(k\) is even, the gain over the cut that cuts all path edges and leaves the closing edge uncut is exactly
\[
F_w(v)=\frac14\left(w\|v_k-v_0\|^2-\sum_{j=1}^k b_j\|v_j-v_{j-1}\|^2\right).
\]
The weighted Cauchy--Schwarz inequality applied to \(v_k-v_0=\sum_j(v_j-v_{j-1})\) yields
\[
\|v_k-v_0\|^2\le S\sum_j b_j\|v_j-v_{j-1}\|^2.
\]
Therefore \(F_w\le0\) for \(w\le S^{-1}\). The unchanged cut attains zero gain, hence the integer and SDP optima coincide with \(\sum_j b_j\) there.

At \(w=w_c\), equality can hold only when all path increments are proportional, with the proportionality constants \(b_j^{-1}\). If a common proportionality vector were nonzero, \(v_0,v_1,v_2\) would be three distinct, consecutively ordered points of a line, all with Euclidean norm one, impossible. Hence all increments vanish. This is the unique critical Gram configuration, and compactness of the elliptope implies that optimizers at \(w\downarrow w_c^+\) converge to this configuration. Since \(w_c<\min_j b_j\), the integer maximum cut remains \(\sum_jb_j\) for all \(w\) in a sufficiently small two-sided neighborhood of \(w_c\): every cut of an odd cycle leaves an odd number of edges uncut, and here the uniquely cheapest edge is the closing one.

**2. Reduction to a single angle.** For any unit-vector path, let \(\Theta=\arccos\langle v_0,v_k\rangle\) and \(d_j=\arccos\langle v_{j-1},v_j\rangle\). Spherical triangle inequality gives \(L:=\sum_jd_j\ge\Theta\). Replacing the path by successive coplanar vectors on a shortest great-circle arc between the same endpoints with angles \(d'_j=d_j\Theta/L\) weakly lowers each positive path penalty \(b_j(1-\cos d_j)/2\) without changing the closing-edge reward; the case \(L=0\) is trivial. Thus a maximizer admits a planar monotone representative. At a positive near-critical maximizing angle \(\Theta\), strict convexity of \(1-\cos d\) for small \(d\) and the first-order condition in the constraint \(\sum_j d_j=\Theta\) give the unique path-cost minimizer
\[
b_j\sin\delta_j=\lambda,\qquad
\delta_j=\arcsin(\lambda/b_j),\qquad
\Theta(\lambda)=\sum_j\arcsin(\lambda/b_j).
\]
No \(\delta_j\) is zero when \(\Theta>0\), since transferring a small angle from a positive component to a zero component lowers the cost. Critical localization ensures all angles are small, so the displayed principal inverse-sine branch applies to every near-critical optimizer.

The gain at the reduced configuration is
\[
G_w(\lambda)=\tfrac12w(1-\cos\Theta(\lambda))
-\tfrac12\sum_jb_j(1-\cos\delta_j(\lambda)).
\]
Differentiating with respect to \(\Theta\) along the minimum-cost path gives \(dG_w/d\Theta=(w\sin\Theta-\lambda)/2\). A nonzero near-critical maximizer therefore solves \(w\sin\Theta(\lambda)=\lambda\).

**3. Nondegenerate branch and sharp coefficient.** Taylor expansion at \(\lambda=0\) yields
\[
\Theta(\lambda)=S\lambda+\frac{T}{6}\lambda^3+O(\lambda^5),\qquad
\sin\Theta(\lambda)=S\lambda-\frac{D}{6}\lambda^3+O(\lambda^5).
\]
The strict positivity \(D>0\) follows because \(S^3>(\sum_j b_j^{-3})\) for at least two positive reciprocal weights. Writing \(\varepsilon=w-w_c>0\), the stationarity equation divided by \(\lambda\) has a unique small positive solution, by the implicit function theorem in \(\lambda^2\), with
\[
\lambda^2=\frac{6S^2}{D}\varepsilon+O(\varepsilon^2).
\]
The derivative of \(G_w\) with respect to \(\Theta\) changes from positive to negative at this root. It is therefore the local maximizing branch; the compactness localization from Step 1 makes it global for all sufficiently small \(\varepsilon>0\). The expansion for every \(\delta_j\) follows immediately.

By the envelope formula for the optimized SDP value (or by direct differentiation of the reduced branch),
\[
\frac{d\,\mathrm{SDP}}{dw}
=\tfrac12(1-\cos\Theta(\lambda(w)))
=\frac{3S^4}{2D}\varepsilon+O(\varepsilon^2).
\]
Meanwhile \(\mathrm{MC}(w)=\sum_jb_j\) in this neighborhood and \(\mathrm{SDP}(w_c)=\mathrm{MC}(w_c)\). Integration from \(w_c\) gives the quadratic gap and its cubic remainder.

**4. Effect of heterogeneity.** With \(x_j=b_j^{-1}>0\), the convexity inequality \(\sum_jx_j^3\ge S^3/k^2\) has equality precisely for \(x_1=\cdots=x_k\). Hence
\[
\frac{3S^4}{4(S^3-T)}\ge \frac{3S}{4(1-k^{-2})},
\]
with equality precisely for equal path weights. Taking \(x_1\uparrow S\) and all other \(x_j\downarrow0\) at fixed sum \(S\) makes \(T\uparrow S^3\), so this curvature is unbounded across such fixed-threshold families.

## Verification
For \(k=2\) with \((b_1,b_2)=(1,1)\), the theorem gives \(w_c=1/2\) and coefficient \(2\), agreeing with the exact near-threshold triangle expression \(\mathrm{SDP}(w)=1+w+1/(4w)\). For \(k=4\) and \((b_1,b_2,b_3,b_4)=(1,2,3,4)\), exact arithmetic gives \(S=25/12\), \(T=2035/1728\), \(D=755/96\), \(w_c=12/25\), and coefficient \(78125/43488\). The accompanying standalone verification program evaluates the stationary equation by bisection for these and an equal-weight five-cycle; scaled gains converge numerically to the analytic coefficients. These tests check examples, not the theorem's arbitrary-weight proof.

## Relationship to prior work
The unit-vector Max-Cut SDP is the classical relaxation of Goemans--Williamson (1994 preliminary conference version; 1995 full article), equivalent to the Delorme--Poljak eigenvalue bound. Goemans--Williamson explicitly compute the unweighted five-cycle value in their Section 5; it does not give an inhomogeneous weight-dependent expansion at the boundary of SDP exactness. Delorme and Poljak treat weighted graphs and general spectral bounds; the accessible abstract does not resolve whether their full proofs imply the particular local curvature law here. Later work on strict complementarity analyzes normal-cone boundary behavior rather than the stated weight-specific SDP-gap coefficient. The theorem computes the first nonzero SDP-gap term and its inverse-cubic dependence on an arbitrary positive path-weight profile, including a sharp heterogeneity comparison.

## Limitations
The expansion holds only for fixed positive \(b_j\) immediately above \(w_c\), not uniformly as weights degenerate or for arbitrary large closing-edge weights. The minimizing rank-two representative is a consequence of cycle geometry, not a claim for arbitrary graphs. Full-text comparison with some potentially related spectral-bound literature remains incomplete; no exhaustive originality claim is asserted.

## References
1. C. Delorme and S. Poljak, *Laplacian eigenvalues and the maximum cut problem*, Mathematical Programming **62** (1993), 557--574, DOI: 10.1007/BF01585184.
2. M. X. Goemans and D. P. Williamson, *.879-approximation algorithms for MAX CUT and MAX 2SAT*, STOC 1994, 422--431, DOI: 10.1145/195058.195216; extended as *Improved approximation algorithms for maximum cut and satisfiability problems using semidefinite programming*, J. ACM **42** (1995), 1115--1145; full text: https://math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf.
3. M. K. de Carli Silva and L. Tunçel, *Strict Complementarity in MaxCut SDP*, arXiv:1806.01173 (2018), https://arxiv.org/abs/1806.01173.
4. A. Bhardwaj, *On the Complexity of Recognizing SDP Exactness for the Maximum Cut Problem*, arXiv:2609.03508 (2026), https://arxiv.org/html/2609.03508v1.
5. C. Delorme and S. Poljak, *The performance of an eigenvalue bound on the max-cut problem in some classes of graphs*, Discrete Mathematics **111** (1993), 145--156, DOI: 10.1016/0012-365X(93)90151-I.
