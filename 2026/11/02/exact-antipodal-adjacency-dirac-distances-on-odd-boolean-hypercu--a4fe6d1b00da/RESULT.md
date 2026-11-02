# Exact antipodal adjacency-Dirac distances on odd Boolean hypercubes

## Finding
For each odd integer \(n=2m+1\geq1\), take the unweighted Boolean hypercube \(Q_n\) with vertices \(\{0,1\}^n\). Equip its diagonal function algebra with the adjacency-matrix Dirac operator \(D\). The exact Connes distance between antipodal vertices is
\[
 d_D(0^n,1^n)=\sum_{j=0}^{m}\frac1{\sqrt{(2j+1)(2m-2j+1)}}. \tag{1}
\]
Set \(N=(n+1)/2=m+1\). As \(N\to\infty\),
\[
 d_D(0^n,1^n)=\frac{\pi}{2}+\frac{\zeta(1/2,1/2)}{\sqrt N}+O(N^{-3/2}),
 \qquad \zeta(1/2,1/2)=(\sqrt2-1)\zeta(1/2)<0. \tag{2}
\]
In particular, antipodal spectral distance converges to \(\pi/2\) although ordinary shortest-path distance equals \(n\). Both statements concern only odd dimensions.

## Assumptions and scope
Vertices are subsets of \(\{1,\ldots,n\}\), with unit-weight edges joining subsets differing in exactly one coordinate. The real symmetric operator \(D\) is the \(2^n\)-by-\(2^n\) adjacency matrix on \(\mathbb C^{2^n}\), and functions act as real diagonal matrices. Precisely,
\[
 d_D(x,y)=\sup\{|f(x)-f(y)|:f:V(Q_n)\to\mathbb R,\ \|[D,\operatorname{diag}f]\|_{2\to2}\leq1\}.
\]
No auxiliary spinor factor, graph Laplacian, or shortest-path spectral metric is used. The claim holds for every odd \(n\geq1\), including \(n=1\). Formula (2) uses the standard Hurwitz zeta function and its analytic continuation at \(1/2\).

## Proof
**Step 1: exact radial reduction.** The group of permutations of the \(n\) coordinates fixes both antipodal endpoints and preserves \(D\). Replacing any admissible \(f\) by its group average leaves its endpoint difference unchanged and cannot increase the commutator norm, by convexity and unitary invariance. Therefore the supremum can be restricted to \(f(S)=g_{|S|}\). Write \(h_k=g_{k+1}-g_k\) for \(0\leq k<n\). We may bound the signed endpoint difference by \(\sum_k|h_k|\); for the converse take nonnegative increments. Since all edges join successive levels, first multiply the real skew-symmetric commutator by \(i\) (preserving its norm), then conjugate this Hermitian matrix by suitable diagonal unitary phases depending only on the Hamming level. This produces the nonnegative real symmetric weighted adjacency with weights \(|h_k|\) along every level-\(k\) edge. Thus the commutator norm is its Perron eigenvalue. A Perron maximizer can be averaged over coordinate permutations while remaining nonzero and maximal, so the top eigenvalue occurs in the subspace spanned by normalized indicator vectors of each Hamming level. The corresponding \((n+1)\)-by-\((n+1)\) symmetric Jacobi matrix \(J(h)\) has zero diagonal and edge weights
\[
 J(h)_{k,k+1}=J(h)_{k+1,k}=w_kh_k,
 \quad w_k=\sqrt{(k+1)(n-k)},\quad h_k\geq0. \tag{3}
\]
Consequently
\[
 d_D(0^n,1^n)=\max\{\textstyle\sum_{k=0}^{n-1}h_k:h_k\geq0,\ \|J(h)\|\leq1\}. \tag{4}
\]
The maximum exists because every \(h_k\leq1/w_k\) under the matrix-norm constraint.

**Step 2: matching lower certificate.** Let \(n=2m+1\) and set
\[
 L=\sum_{j=0}^{m}w_{2j}^{-1},\qquad h^*_{2j}=w_{2j}^{-1},\quad h^*_{2j+1}=0.
\]
The matrix \(J(h^*)\) is the direct sum of \(m+1\) symmetric two-by-two exchanges with off-diagonal entry \(1\). Hence \(\|J(h^*)\|=1\) and its objective in (4) equals \(L\). This proves \(d_D\geq L\) and constructs an attaining diagonal potential (start at \(g_0=0\) and sum the increments).

**Step 3: global sharp upper certificate.** Define a unit vector \(u\in\mathbb R^{n+1}\) by
\[
 u_{2j}=u_{2j+1}=(2Lw_{2j})^{-1/2}\qquad(0\leq j\leq m).
\]
Normalization holds because \(\sum_j2(2Lw_{2j})^{-1}=1\). For every nonnegative \(h\), the coefficient of \(h_{2j}\) in \(u^{\mathsf T}J(h)u\) is exactly \(1/L\). The coefficient of \(h_{2j+1}\), for \(0\leq j<m\), is
\[
 \frac{w_{2j+1}}{L\sqrt{w_{2j}w_{2j+2}}}\geq \frac1L.
\]
Indeed, \(w_k^2=(k+1)(n-k)\) and the sequence \((w_k)\) is strictly log-concave, since its two positive linear factors are log-concave; hence \(w_k^2>w_{k-1}w_{k+1}\) for interior indices. As \(u\) is a unit vector,
\[
 \|J(h)\|\geq u^{\mathsf T}J(h)u\geq L^{-1}\sum_kh_k.
\]
Every admissible point in (4) has objective at most \(L\), completing the exact formula (1). The argument also proves feasibility and optimality uniformly in all odd dimensions, without finite-dimensional enumeration.

**Step 4: sharp asymptotic.** With \(N=m+1\), equation (1) becomes
\[
 L=\frac1{2N}\sum_{j=0}^{N-1}F\!\left(\frac{j+1/2}{N}\right),\qquad
 F(x)=\frac1{\sqrt{x(1-x)}}.
\]
Write \(F(x)=x^{-1/2}+(1-x)^{-1/2}+G(x)\). The function \(G\) extends continuously to the endpoints; near each endpoint it equals a constant plus an \(O(\sqrt{\text{distance}})\) term, and its second derivative is bounded by a constant times \(x^{-3/2}+(1-x)^{-3/2}\). Splitting the midpoint rule into its two endpoint cells and interior cells and applying the midpoint remainder bound to each interior cell gives a total quadrature error \(O(N^{-3/2})\) for \(G\). The singular part contributes
\[
 \frac1{\sqrt N}\sum_{j=0}^{N-1}(j+1/2)^{-1/2}
 =2+\frac{\zeta(1/2,1/2)}{\sqrt N}+O(N^{-2}),
\]
by the Hurwitz-zeta tail formula (equivalently midpoint Euler--Maclaurin). Finally \(\int_0^1F(x)\,dx=\pi\) and \(\int_0^1[x^{-1/2}+(1-x)^{-1/2}]\,dx=4\). Dividing by two yields (2).

## Verification
A standalone reproducibility script, `checker.py`, requires Python 3 and NumPy and is run as `python3 checker.py`. It reconstructs the full adjacency commutator and its radial Jacobi compression for odd dimensions \(1,3,5,7\), compares operator norms for randomized signed level increments, checks the proposed primal and dual certificates, and tests numerical asymptotic residuals through dimension \(3999\). On the checked environment it passed 170 assertions. These finite tests are **not** a proof of the all-dimensional statements; Steps 1--4 establish those statements.

For example, \(d_D(0^3,1^3)=2/\sqrt3\), and \(d_D(0^5,1^5)=2/\sqrt5+1/3\). The first few values increase toward \(\pi/2\).

## Relationship to prior work
Besnard, *Estimating noncommutative distances on graphs* (arXiv:2105.09056v1, 2021), establishes general bounds and reductions for adjacency-Dirac graph distances; these do not evaluate the odd hypercube antipodal distance. Clare, Li, Poon, and Swartz, *Noncommutative distances on graphs: An explicit approach via Birkhoff-James orthogonality* (arXiv:2409.04146v1, 2024), obtain a complete **implicit** viable-vector characterization for every weighted tridiagonal path (Theorem 3.10). That theorem applies after our radial reduction; the present statement does **not** claim to invent weighted-path reduction or generic matrix duality. The nontrivial contribution is an all-dimensional, explicit odd-hypercube value, an extremizer and uniform dual witness for the binomial radial weights, and a sharp zeta-corrected asymptotic not supplied by the cited general characterization. Swartz, *Effect of edge deletion on noncommutative distances on graphs* (arXiv:2610.07718v1, 2026), addresses related graph-distance questions but not this family. An equivalent explicit solution embedded in a more general path or noncommutative metric theorem is a remaining priority risk.

## Limitations
The dimension must be odd. No even-dimensional formula, distances for nonantipodal vertices, nonunit edge weights, or unrelated Dirac operators follow here. The finite numerical checks are supplementary, and independent mathematical validation has not been performed. The cited 2024 weighted-path theorem provides implicit general coverage of the reduced optimization and therefore is particularly relevant when assessing the originality of the *explicit* formula.

## References
1. F. Besnard, *Estimating noncommutative distances on graphs*, arXiv:2105.09056v1, first posted 2021-05-19, https://arxiv.org/html/2105.09056.
2. P. Clare, C.-K. Li, E. Poon, E. Swartz, *Noncommutative distances on graphs: An explicit approach via Birkhoff-James orthogonality*, arXiv:2409.04146v1, first posted 2024-09-06, https://arxiv.org/html/2409.04146v1.
3. E. Swartz, *Effect of edge deletion on noncommutative distances on graphs*, arXiv:2610.07718v1, first posted 2026-10-06, https://arxiv.org/html/2610.07718v1.
4. Hurwitz zeta Euler--Maclaurin expansion, standard midpoint summation identity; used only for asymptotic formula (2).
