# Sharp adjacency–Dirac distances on cross-polytope graphs

## Finding
For each integer \(r\geq3\), let \(G_r\) be the one-skeleton of the \(r\)-dimensional cross-polytope. Thus \(G_r=K_{2,2,\ldots,2}\), the complete graph on \(2r\) vertices with one perfect matching deleted; call the two ends of a deleted edge *antipodes*. Use the unweighted adjacency matrix \(D_r\) as Dirac operator and the operator norm in the Connes distance of real diagonal potentials.

There are exactly two nonzero distance classes. Antipodal vertices have
\[
 d_r^{\mathrm{opp}}=\frac1{\sqrt{r-1}}.
\]
For vertices in different matching pairs (which are graph-adjacent), put
\[
 \begin{aligned}
 A_r(a)&=r-1+(a+\tfrac12)^2,\\
 B_r(a)&=2a^2+2(r-1)a+\tfrac12,\\
 E_r(a)&=(4r-3)a^2+a+\tfrac14,\\
 F_r(a)&=\frac{A_r(a)+E_r(a)+\sqrt{(A_r(a)-E_r(a))^2+4B_r(a)^2}}{2}.
 \end{aligned}
\]
The exact adjacent-vertex distance is
\[
 d_r^{\mathrm{adj}}=\bigl(F_r(a_r)\bigr)^{-1/2},
 \qquad a_r=\mathop{\mathrm{argmin}}_{a\in\mathbb R}F_r(a).
\]
The minimizer \(a_r\) is unique, lies strictly between \(-1/2\) and \(0\), and can equivalently be found as the unique zero of \(F'_r(a)\). This is an exact one-variable algebraic characterization, not merely a numerical prescription. In every dimension,
\[
 0<d_r^{\mathrm{adj}}<d_r^{\mathrm{opp}}.
\]
The large-dimensional transition is sharp:
\[
 \begin{aligned}
 a_r&=-\frac{3}{8r}+O(r^{-2}),\\
 F_r(a_r)&=r-\frac34-\frac{5}{16r}+O(r^{-2}),\\
 d_r^{\mathrm{adj}}&=r^{-1/2}\left(1+\frac{3}{8r}+\frac{47}{128r^2}+O(r^{-3})\right),\\
 d_r^{\mathrm{opp}}-d_r^{\mathrm{adj}}&=\frac1{8r^{3/2}}+\frac1{128r^{5/2}}+O(r^{-7/2}).
 \end{aligned}
\]
In particular, the shortest-path distinction (length one versus length two) shrinks to a spectral-distance gap of order \(r^{-3/2}\), and its leading coefficient is exactly \(1/8\).

## Assumptions and scope
On \(\mathbb C^{2r}\), with the standard Euclidean norm, let \(D_r=(d_{ij})\) be the real symmetric adjacency matrix with \(d_{ij}=1\) when vertices belong to different antipodal pairs, and \(0\) otherwise. For real \(f:V(G_r)\to\mathbb R\), let \(M_f=\operatorname{diag}(f)\). The distance is
\[
 d_r(x,y)=\sup\bigl\{|f(x)-f(y)|:\ \|[D_r,M_f]\|_{2\to2}\leq1\bigr\}.
\]
The usual self-adjoint-element formulation of the finite spectral-triple distance suffices: self-adjoint diagonal matrices are precisely the real-valued potentials. Distances are nonnegative and symmetric. The theorem has no edge weights, no additional Dirac blocks, and assumes the integer \(r\geq3\). The dimension-two case is the four-cycle and is not included in the new classification.

## Proof
**1. Normalize and average without losing optimality.** For fixed distinct \(x,y\), the desired reciprocal distance is the minimum commutator norm over all real potentials satisfying \(f(x)-f(y)=1\). Translation of \(f\) by constants does not change the commutator. The automorphism group of \(G_r\) permutes all antipodal pairs and independently flips their endpoints. Conjugating by its permutation matrices preserves the commutator norm. Since the norm is convex in \(f\), averaging over automorphisms that fix the prescribed pair can only decrease that norm. When the pair is swapped by an automorphism \(\sigma\), the transformed potential \(-f\circ\sigma\) preserves the prescribed difference; averaging with it forces antisymmetry. This proves that the symmetrized normal forms below attain the global minima over all potentials, not just restricted subfamilies.

**2. Opposite vertices.** Fix \(x,y\) as an antipodal pair. The combined average makes \(f(x)=1/2\), \(f(y)=-1/2\), and all other \(2r-2\) entries zero. The skew matrix \([D_r,M_f]\) has rank two and operator norm \(\sqrt{r-1}\): on the span of the difference of the first pair and the normalized sum of the remaining vertices it acts as a two-dimensional skew rotation with coefficient \(\sqrt{(2r-2)/2}\). Hence \(d_r^{\mathrm{opp}}=(r-1)^{-1/2}\).

**3. Adjacent vertices and the exact Gram matrix.** Fix \(x,y\) in different antipodal pairs and name their antipodes \(x',y'\). Symmetry averaging reduces the potentials, in the order \(x,x',y,y'\), to \((1/2,a,-1/2,-a)\), with zero value on all other vertices. The commutator vanishes on vectors supported on the remaining vertices whose coordinates sum to zero. Its only nontrivial action is therefore on the five-dimensional space spanned by the four named coordinate vectors and the normalized sum of the other \(2r-4\) coordinates. Under the involution swapping the two named pairs, the skew commutator exchanges a three-dimensional even subspace and a two-dimensional odd subspace. Its off-diagonal rectangular block is, up to signs and orthogonal changes of basis,
\[
 C_r(a)=\begin{pmatrix}
 1&a+\frac12\\
 a+\frac12&2a\\
 \sqrt{r-2}&2a\sqrt{r-2}
 \end{pmatrix}.
\]
Its squared operator norm is the larger eigenvalue of the \(2\times2\) Gram matrix
\[
 C_r(a)^*C_r(a)=\begin{pmatrix}A_r(a)&B_r(a)\\B_r(a)&E_r(a)\end{pmatrix}.
\]
The quadratic formula gives exactly \(F_r(a)\). Thus the symmetrized minimization equals the unrestricted distance, and the stated algebraic characterization follows.

**4. Unique minimizer, range and strict class separation.** Write \(C_r(a)=C_r(0)+aC'_r\). The matrix \(C'_r\) has full column rank, as is already evident from its first two rows \((0,1)\) and \((1,2)\). For every unit vector \(v\in\mathbb R^2\), the function \(a\mapsto\|C_r(a)v\|_2^2\) has second derivative \(2\|C'_rv\|_2^2\) bounded strictly below by a positive constant independent of \(v\). Their pointwise maximum, \(F_r(a)\), is therefore strongly convex. Its two Gram eigenvalues never coincide for \(r\ge3\): coincidence would force \(A_r=E_r\) and \(B_r=0\), but the resultant in \(a\) is \(-16r(r-2)(r-1)^2\ne0\). Consequently \(F_r\) is differentiable with a unique global minimizer. Direct differentiation gives \(F'_r(-1/2)=6-4r<0\) and \(F'_r(0)=1+2(r-1)/\sqrt{(r-1)^2+1}>0\); hence \(-1/2<a_r<0\). Moreover \(F_r(a)\ge A_r(a)=r-1+(a+1/2)^2\). Equality with \(r-1\) would require \(a=-1/2\), but there \(B_r(a)=2-r\ne0\), so \(F_r(a)>r-1\) for all \(a\). Taking reciprocals proves \(d_r^{\mathrm{adj}}<d_r^{\mathrm{opp}}\).

**5. Sharp asymptotics.** Put \(a=k/r\) for bounded real \(k\). The large diagonal of the Gram matrix is \(A_r=r-3/4+k/r+O(r^{-2})\), while \(B_r=2k+1/2+O(r^{-1})\) and \(E_r=1/4+O(r^{-1})\). The larger eigenvalue, uniformly with its first derivative for bounded \(k\), is
\[
 F_r(k/r)=r-\frac34+\frac{4k^2+3k+\frac14}{r}+O(r^{-2}).
\]
For sufficiently large \(r\), differentiating this uniform expansion at \(k=-1\) and \(k=0\) gives opposite signs, so the unique minimizer lies in \([-1/r,0]\). On that interval the limiting quadratic is uniquely minimized at \(k=-3/8\), and the uniform derivative remainder gives \(ra_r=-3/8+O(r^{-1})\). Substitution yields \(F_r(a_r)=r-3/4-5/(16r)+O(r^{-2})\). The binomial expansion of \(F_r(a_r)^{-1/2}\) gives the adjacent-distance terms. Finally expand \((r-1)^{-1/2}\) and subtract; the first two gap coefficients are \(1/8\) and \(1/128\), as claimed. All error terms are for integer \(r\to\infty\).

## Verification
The accompanying `verify.py` is a standalone Python 3 standard-library checker. Run `python3 verify.py`. It reconstructs full skew commutators for dimensions \(2r\), computes their largest squared singular value by symmetric Jacobi diagonalization, compares them against \(F_r\) over a range of rational trial parameters, checks the antipodal matrix, verifies the minimizer derivative and strict separation, and performs large-dimension asymptotic diagnostics. The supplied test returned `CHECK_OK 219 finite comparisons, dimension/asymptotic diagnostics`. The analytic symmetry reduction, strong-convexity argument and asymptotic error estimates—not these finite tests—are the proofs for every integer dimension.

## Relationship to prior work
Clare, Li, Poon and Swartz (arXiv:2409.04146, first submitted September 6, 2024) formulate adjacency-based noncommutative graph distances and give a complete path-graph treatment, including Birkhoff–James methods. Their graph-general reduction tools do not state the cross-polytope/cocktail-party classification. Besnard (arXiv:2105.09056) proves general inequalities and graph-pruning results; these yield bounds rather than the exact two-class formulas and the \(r^{-3/2}\) gap. The earlier exact treatment of complete bipartite graphs applies to \(K_{2,2}\) at \(r=2\), which is explicitly excluded; for \(r\ge3\), these graphs contain triangles and are not bipartite. The numerical norm reduction here uses the special signed-pair symmetry and does not assert a formula for arbitrary multipartite graphs.

## Limitations
No independent expert or formal-machine audit has been performed. The adjacent distance has an exact uniquely attained algebraic one-variable characterization, not a general elementary radical expression in \(r\). Nothing here addresses arbitrary part sizes, nonunit weights, unrelated spectral triples, or all-pairs distances for other graph families. Failure to locate a prior equivalent formula does not establish publication-level novelty; alternative operator-norm/minimax formulations remain a residual literature risk.

## References
1. P. Clare, C.-K. Li, E. Poon, E. Swartz, *Noncommutative Distances on Graphs: An Explicit Approach via Birkhoff-James Orthogonality*, arXiv:2409.04146v1 (September 6, 2024), https://arxiv.org/abs/2409.04146.
2. F. Besnard, *Estimating noncommutative distances on graphs*, arXiv:2105.09056v1 (May 19, 2021), https://arxiv.org/abs/2105.09056.
