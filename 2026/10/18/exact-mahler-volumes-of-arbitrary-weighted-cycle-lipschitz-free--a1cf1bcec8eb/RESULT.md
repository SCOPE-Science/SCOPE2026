# Exact Mahler volumes of arbitrary weighted-cycle Lipschitz-free spaces

## Finding
Let \(n\ge3\) and give the edges of a cycle on \(n\) labeled vertices arbitrary strictly positive lengths \(a_1,\ldots,a_n\). Let \(M_a\) be its shortest-path metric and let \(B_a\) be the unit ball of the real Lipschitz-free Banach space \(\mathcal F(M_a)\). Write \(d=n-1\), \(A=\sum_{i=1}^n a_i\), and \(a(S)=\sum_{i\in S}a_i\). Define
\[
H_i(a)=\sum_{\sigma\in\{-1,1\}^{[n]\setminus\{i\}}}\!\left(\mathbf1_{\left|\sum_{j\ne i}\sigma_j a_j\right|<a_i}+\frac12\mathbf1_{\left|\sum_{j\ne i}\sigma_j a_j\right|=a_i}\right).
\]
In rooted evaluation coordinates and their dual coordinates, the two exact volumes are
\[
\boxed{\operatorname{vol}_d(B_a)=\frac{\sum_{i=1}^n a_i H_i(a)}{d!\prod_{i=1}^n a_i}},\qquad
\boxed{\operatorname{vol}_d(B_a^\circ)=\frac1{d!}\sum_{S\subseteq[n]}(-1)^{|S|}\bigl(A-2a(S)\bigr)_+^d}.
\]
Here \(x_+=\max(x,0)\). Their product gives the Mahler volume product for **every** positive choice of cycle lengths, including resonant choices with equally weighted half-perimeter subsets and lengths making an edge metrically redundant. No genericity hypothesis is required. Since the two volumes scale reciprocally and are symmetric in the edge-length multiset, so is the product.

For unit edge lengths the formulas specialize to
\[
\operatorname{vol}_d(B_a)=\frac{n}{(n-1)!}\binom{n-1}{\lfloor(n-1)/2\rfloor},\qquad
\operatorname{vol}_d(B_a^\circ)=\frac1{(n-1)!}\sum_{k=0}^{\lfloor n/2\rfloor}(-1)^k\binom nk(n-2k)^{n-1}.
\]
The normalized unit-cycle product has the asymptotic limit
\[
\boxed{\lim_{n\to\infty}\frac{(n-1)!}{4^{n-1}}\operatorname{vol}_{n-1}(B_a)\operatorname{vol}_{n-1}(B_a^\circ)=\frac{2\sqrt3}{\pi}}.
\]
The edge-metric realization, combinatorial facet classification, and general definition of the Mahler product are previously known. The finding is the exact combined *metric-dependent volume evaluation* and the resulting asymptotic.

## Assumptions and scope
The cycle has \(n\ge3\) edges and \(n\) vertices. Each \(a_i>0\). Its metric is defined by minimizing weighted path length; in particular a length exceeding the sum of the others simply makes its edge redundant. Root one vertex and identify the zero-sum measure space with \(\mathbb R^{n-1}\) via its coordinates at the remaining vertices. The dual coordinate vector records Lipschitz function values at those vertices with root value zero. These dual pairing coordinates are essential: the separately reported volumes are coordinate volumes, not Euclidean hyperplane volumes in \(\mathbb R^n\), while their product is invariant under any linear coordinate change.

## Proof
**1. Rooted edge vectors.** Orient the cycle and set \(v_i=(e_i-e_{i+1})/a_i\), interpreting the root coordinate vector as zero, with cyclic indices. The nonzero vectors \(v_i\) span \(\mathbb R^d\), satisfy the unique linear relation \(\sum_i a_i v_i=0\), and every \(d\)-subset forms a basis of determinant magnitude \(\prod_{j\ne i}a_j^{-1}\), since deleting any cycle edge leaves a spanning tree with unimodular reduced incidence matrix. By the shortest-path decomposition of every elementary transportation molecule, \(B_a=\operatorname{conv}\{\pm v_i:1\le i\le n\}\), even if some edge is redundant.

**2. Primal volume for generic weights.** Temporarily assume \(\sum_i\epsilon_i a_i\ne0\) for every sign vector \(\epsilon\in\{-1,1\}^n\). A facet of this centrally symmetric polytope has at most one of each antipodal pair and at most \(d\) signed edge vectors, because a supporting functional cannot saturate all \(n\) pairs without violating the nonvanishing signed cycle relation. Every facet consequently consists of exactly \(d\) vertices, obtained by omitting one index \(i\) and prescribing signs \(\sigma_j\) for the remaining indices. The uniquely determined supporting functional takes value \(-\sum_{j\ne i}\sigma_j a_j/a_i\) on \(v_i\). The signed simplex is a facet exactly when the absolute value is strictly below one. Its cone from zero has volume \(\bigl(d!\prod_{j\ne i}a_j\bigr)^{-1}\). These cones have pairwise disjoint interiors and cover \(B_a\). Summing gives the first boxed formula without the equality contributions.

**3. All resonances.** Both the convex hull and its volume vary continuously with positive weights. Perturb the length vector by a small centered continuous random vector. For every equality \(\left|\sum_{j\ne i}\sigma_j a_j\right|=a_i\), the strict-facet indicator for the perturbed vector has limiting expectation \(1/2\), since the defining nonzero linear functional has a symmetric perturbation. For non-equalities the indicator is locally constant. Average the generic-volume identity and take the limit, using finiteness of the sums and continuity of the determinant factors. This yields the half-weight rule at *simultaneous* resonances as well; there is no assumption that only one sign relation vanishes.

**4. Polar volume.** For a rooted potential \(f\) write successive oriented edge increments \(u_i=f(i)-f(i-1)\), with \(u_n=-\sum_{i<n}u_i\). The map from rooted potential coordinates to \((u_1,\ldots,u_d)\) is triangular with determinant one. The polar is the sliced box \(\{|u_i|\le a_i\ (i<n),\ |\sum_{i<n}u_i|\le a_n\}\). The corresponding integral is the convolution at zero of the \(n\) interval indicators \(\mathbf1_{[-a_i,a_i]}\). Shift the intervals to \([0,2a_i]\). Inclusion-exclusion for the volume of \(\{y_i\ge0,\sum_i y_i\le z\}\), differentiated at \(z=A\), gives precisely \(d!^{-1}\sum_{S}(-1)^{|S|}(A-2a(S))_+^d\). Boundary values are obtained by continuity. This proves the second boxed formula and hence the exact product.

**5. Unit cycles and the limit.** For all lengths one, when \(n\) is odd only balanced zero sums contribute to the strict primal count. When \(n\) is even the balanced sign sums have magnitude one and each contributes one half. In either parity \(H_i=\binom{n-1}{\lfloor(n-1)/2\rfloor}\). The polar formula groups subsets by cardinality. Let \(Z_1,\ldots,Z_n\) be independent uniform variables on \([-1,1]\), and let \(p_n\) denote the density of their sum. The polar volume equals \(2^n p_n(0)\). Fourier inversion with characteristic function \(\sin t/t\), or the local central limit theorem, gives \(p_n(0)\sim\sqrt{3/(2\pi n)}\). The central binomial estimate \(\binom{n-1}{\lfloor(n-1)/2\rfloor}\sim 2^{n-1}\sqrt{2/(\pi n)}\) then yields \(2\sqrt3/\pi\) after normalizing by the standard cross-polytope product \(4^{n-1}/(n-1)!\).

## Verification
The included `check_cycle.py` forms both primal and polar vertex sets for eleven rational configurations with three through six vertices; triangulations are computed with SciPy, and each simplex determinant is evaluated as an exact rational. It checks the two boxed volume formulas against the two independently formed hulls, including uniform edge lengths, generic rational weights, and resonant weights. Every specified check passed. These are finite corroborations, not substitutes for the all-dimensional proof; triangulation combinatorics are supplied by floating-point Qhull, so the script is not itself an exact infinite-dimensional certificate.

For representative inputs: the unit triangle gives primal and polar areas \(3\) and \(3\); the unit four-cycle gives volumes \(2\) and \(16/3\); weights \((2/3,3/4,5/4,4/3)\) give volumes \(8/3\) and \(341/81\). The reproducer prints the tested values and asserts exact equality of rational determinants with the analytic formulas.

## Relationship to prior work
Aliaga and Pernecká (arXiv:1810.11278, first posted 26 October 2018, primary MSC 46B20) established the extreme-molecule characterization of finite Lipschitz-free balls. Jevtić, Timotijević and Živaljević (arXiv:1812.00397, first posted 2 December 2018) identified the boundary complexes of generic weighted-cycle Kantorovich–Rubinstein polytopes with short-set Bier spheres. Their classification implies the generic facet sign criterion but does not evaluate either volume or the Mahler product. Alexander, Fradelizi, García-Lirola and Zvavitch (arXiv:1911.10642, first posted 24 November 2019) analyzed volume products of finite Lipschitz-free balls, including the equilateral metric and extremal inequalities; their treatment of cycles establishes a minimum bound and a four-point equality characterization, not the arbitrary weighted-cycle volume formula or unit-cycle asymptotic. The new evaluation combines facet-determinant geometry with a box-slice spline calculation. Its symmetry under reordering lengths is consistent with previously known combinatorial symmetry and is not presented as a newly discovered ordering invariance.

## Limitations
The result concerns finite **real** Lipschitz-free spaces on single weighted cycles, with shortest-path metrics. The formulas are finite exponential-size sums, not a claim of polynomial-time evaluation when input lengths have unrestricted encoding. No general Mahler conjecture for arbitrary finite metric spaces or arbitrary graph families is proved. The full weighted-cycle result has not undergone independent mathematical review; equivalent results in unindexed literature remain a residual bibliographic possibility.

## References
1. R. J. Aliaga and E. Pernecká, *Supports and extreme points in Lipschitz-free spaces*, arXiv:1810.11278 (2018), https://arxiv.org/abs/1810.11278.
2. F. D. Jevtić, M. Timotijević and R. T. Živaljević, *Polytopal Bier spheres and Kantorovich-Rubinstein polytopes of weighted cycles*, arXiv:1812.00397 (2018), https://arxiv.org/abs/1812.00397.
3. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (2019), https://arxiv.org/abs/1911.10642.
