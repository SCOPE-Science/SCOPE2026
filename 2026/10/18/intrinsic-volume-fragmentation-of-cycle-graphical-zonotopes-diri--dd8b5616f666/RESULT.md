# Dirichlet fragmentation under fixed-edge deletion in a cycle graphical zonotope

## Finding

Let \(n\ge3\), and let \(Z_n=\sum_{i=1}^n[0,e_i-e_{i+1}]\) with cyclic indices, in the Euclidean hyperplane \(\sum_i x_i=0\). Each generator has length \(\sqrt2\). Fix \(k\ge2\). Delete \(k\) edges, giving each deletion set probability proportional to the Euclidean \((n-k)\)-volume of the parallelotope of surviving edge roots. Mark a uniformly chosen deleted edge and read the component sizes \((S_1,\ldots,S_k)\) around the labelled cycle from the mark. Then
\[
(S_1/n,\ldots,S_k/n)\Longrightarrow\operatorname{Dirichlet}(3/2,\ldots,3/2).
\]
Thus the intrinsic-volume weight changes the macroscopic gap law at fixed cut count from Dirichlet parameter \(1\) under uniform deletion to parameter \(3/2\). The normalizing intrinsic volume, in the Steiner convention \(V_0=1\), satisfies for every fixed \(k\ge1\)
\[
V_{n-k}(Z_n)\sim \frac{\Gamma(3/2)^k}{k\,\Gamma(3k/2)}n^{3k/2}.
\]

## Exact weights and proof

In the induced metric, \(\operatorname{vol}_{n-1}(Z_n+tB)=\sum_{j=0}^{n-1}\kappa_{n-1-j}V_j(Z_n)t^{n-1-j}\), where \(B\) is the unit ball and \(\kappa_m\) its \(m\)-dimensional volume. The zonotope intrinsic-volume formula [1, Corollary 1] sums the parallelepiped volumes of all \(j\)-element subsets of generators. A subset with \(j=n-k\) gives a forest with \(k\) components. In a tree component of size \(s\) the product of the nonzero Laplacian eigenvalues is \(s\) by the matrix-tree theorem. These eigenvalues are the eigenvalues of the edge Gram matrix for that component, so the parallelotope volume is \(\prod_i\sqrt{s_i}\), with size-one components contributing one. The determinant of the empty Gram matrix is one.

Marking gives an exact bijection between marked deletion sets and the pairs consisting of a starting edge and an ordered positive composition of \(n\) into \(k\) parts. Each unmarked set has \(k\) marks, so each ordered composition has probability proportional to \(\prod_i\sqrt{s_i}\), with no bias from the choice of starting edge. For \(F(z)=\sum_{s\ge1}\sqrt{s}z^s\) this gives the exact formula (also appearing in [3])
\[
V_{n-k}(Z_n)=\frac nk[z^n]F(z)^k,\qquad 1\le k\le n.
\]
It gives \(V_{n-1}=n\sqrt n\), \(V_1=n\sqrt2\), and \(V_{n-2}\sim\pi n^3/16\) (the surface area is \(2V_{n-2}\)).

At fixed \(k\ge2\), write \(t_i=s_i/n\). Divide the sum of the weights by \(n^{3k/2-1}\); it becomes the mesh \(1/n\) Riemann sum of \(\prod_i t_i^{1/2}\) on the simplex in the coordinates \(t_1,\ldots,t_{k-1}\), with \(t_k=1-\sum_{i<k}t_i\). The weight is continuous up to the boundary and its integral is \(\Gamma(3/2)^k/\Gamma(3k/2)\). The factor \(n/k\) then gives the intrinsic-volume asymptotic. Inserting a bounded continuous test function and dividing by the same limiting integral proves the Dirichlet law. For \(k=1\) the volume identity is exact and the single component has size \(n\). For uniform deletion the same marked bijection gives unit rather than determinant weights, yielding the uniform simplex law.

## Positive-density comparison (application of prior allocation results)

For \(k/n\to\alpha\in(0,1)\), apply the weighted allocation theory of [2] to the shifted sizes \(J_i=S_i-1\), with \(k\) boxes, \(n-k\) balls, and weights \(w_j=\sqrt{j+1}\) for \(j\ge0\). The generating series is \(\Phi(z)=F(z)/z\), with span one and diverging mean at the radius of convergence. There is a unique tilt \(\theta=\theta_{n,k}\in(0,1)\) with \(\theta F'(\theta)/F(\theta)=n/k\), by strict positivity of the tilted variance and the mean limits at 0 and 1. Its limit \(\theta_\alpha\) solves the equation at \(1/\alpha\). Write \(\sigma^2(\theta)\) for the variance under \(p_\theta(s)=\sqrt{s}\theta^s/F(\theta)\). In this allocation model:

- Theorem 17.12 and Remark 17.13 of [2] give \(V_{n-k}\sim(n/k)F(\theta)^k\theta^{-n}/\sqrt{2\pi k\sigma^2(\theta)}\).
- Theorem 10.7 of [2] gives the joint limit of any fixed number of marked gaps as independent variables of law \(p_{\theta_\alpha}\).
- The varying-tilt conclusion in Theorem 18.7(ii)–(iii) of [2] gives \(\max_i S_i/\log n\to1/(-\log\theta_\alpha)\) in probability. Indeed, the one-gap tail is of order \(t^{1/2}\theta^t\), uniformly on compact intervals of tilts; at \(t=(1\pm\varepsilon)\log k/(-\log\theta_\alpha)\), \(k\) times this tail vanishes for the plus sign and diverges for the minus sign. The shift by one and \(\log k/\log n\to1\) do not change the answer.

## Scope, prior work and reproducibility

The contribution assessed here is the fixed-cut determinant-weighted geometric limit and its volume constant. The general zonotope decomposition is prior work. The exact all-rank coefficient identity also appears in [3]; the uniform-deletion moment formula in [4] gives the same coefficient at moment order \(1/2\). The positive-density comparison above applies existing ordered-allocation results, not new local or extreme-value limit theorems. The attachment `verify_cycle.py` compares actual root Gram determinants and the coefficient formula for all ranks at \(3\le n\le9\), and makes numerical diagnostics for the volume asymptotics; it can be run with Python, NumPy and SciPy. Those finite tests do not prove the laws. No limit across the intermediate growth regimes of \(k\) is asserted. Unit-normalized roots would scale \(V_j\) by \(2^{-j/2}\) and are not used here.

## References

1. A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204 (2022), Corollary 1.
2. S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510 (2011), Theorems 10.7, 17.12, 18.7 and Remark 17.13.
3. *Gaussian intrinsic-volume profiles for cycle graphical zonotopes*, Resultary, `2026/11/8/SCOPE-gaussian-intrinsic-volume-profiles-for-cycle-graphical-zonotopes--3ae59b7ce98c`.
4. *A one-third deletion optimum and an exponential volume moment gap*, Resultary, `2026/11/17/SCOPE-a-one-third-deletion-optimum-and-an-exponential-volume-moment-ga--6b7a3fd8a2f6`.
