# Scalar-field parity in Euclidean distortion of cycle transportation spaces

## Finding
Let \(C_n\) be the unit-edge cycle with its shortest-path metric, for every integer \(n\ge3\). Over the indicated scalar field, let \(\mathcal F_{\mathbb K}(C_n)\) be its finite-dimensional Lipschitz-free (transportation-cost) space, defined as the canonical predual of complex- or real-valued Lipschitz functions vanishing at one vertex. With multiplicative Banach–Mazur distance and complex-linear maps in the complex case,
\[
 d_{\mathrm{BM}}\bigl(\mathcal F_{\mathbb R}(C_n),\ell_2^{n-1}(\mathbb R)\bigr)^2=
 \begin{cases}
 n-1,&n\text{ even},\\[2pt]
 \dfrac{(n-1)^2}{n},&n\text{ odd},
 \end{cases}
\]
whereas
\[
 d_{\mathrm{BM}}\bigl(\mathcal F_{\mathbb C}(C_n),\ell_2^{n-1}(\mathbb C)\bigr)^2=n-1
 \quad(n\ge3).
\]
Thus in every even dimension of the cycle, the real space attains the dimensional upper bound \(\sqrt{n-1}\), while in every odd cycle it falls strictly below that bound; over the complex scalars every cycle attains it. At odd cycle lengths the complex-to-real distortion ratio is exactly \(\sqrt{n/(n-1)}\).

## Assumptions and scope
The unit-edge cycle has labeled vertices \(v_0,\dots,v_{n-1}\), with adjacency read modulo \(n\); the metric is the shortest-path graph metric. For \(\mathbb K\in\{\mathbb R,\mathbb C\}\), the space \(\operatorname{Lip}_0(C_n;\mathbb K)\) consists of functions \(f:C_n\to\mathbb K\) satisfying \(f(v_0)=0\), with norm \(\max_{0\le i<n}|f(v_i)-f(v_{i+1})|\). Define its finite-dimensional Banach dual, taken over \(\mathbb K\), as \(\mathcal F_{\mathbb K}(C_n)\). This agrees with the usual finite-point Lipschitz-free definition by evaluation functionals.

For normed \(\mathbb K\)-spaces \(X,Y\) of equal finite dimension, use \(d_{\mathrm{BM}}(X,Y)=\inf_T\|T\|\|T^{-1}\|\), where \(T\) ranges over invertible \(\mathbb K\)-linear maps. Complex distances do not permit conjugate-linear maps. The statement does not concern weighted edges, arbitrary finite graphs, or nonlinear distortion.

## Proof
**1. The cycle is a zero-sum cube section in dual coordinates.** Write \(b_i=f(v_i)-f(v_{i+1})\). Telescoping yields \(\sum_i b_i=0\). Conversely, every such vector integrates uniquely to a base-point-zero function on the cycle. The graph metric and the triangle inequality ensure that edge differences give the full Lipschitz norm, so
\[
 \operatorname{Lip}_0(C_n;\mathbb K)\cong H_n^{\mathbb K}
 :=\left\{b\in\mathbb K^n:\sum_{i=1}^n b_i=0\right\},\qquad
 \|b\|=\max_i|b_i|.
\]
By finite-dimensional duality and the invariance of multiplicative Banach–Mazur distance under taking duals when the comparison space is Hilbertian, it suffices to determine the Euclidean distance of \(H_n^{\mathbb K}\).

**2. Permutation symmetry rules out improving the coordinate Hilbert norm by any ellipsoid.** Let \(N(b)=\|b\|_\infty\). Every Euclidean comparison on the \((n-1)\)-dimensional space \(H_n^{\mathbb K}\) is a positive-definite real quadratic form when \(\mathbb K=\mathbb R\), or a positive-definite Hermitian quadratic form when \(\mathbb K=\mathbb C\). After rescaling, the distortion is the smallest \(D\) for which such a form \(Q\) satisfies
\[
 N(b)^2\le Q(b)\le D^2N(b)^2\quad\text{for all }b\in H_n^{\mathbb K}.
\]
All coordinate permutations preserve both \(H_n^{\mathbb K}\) and \(N\). Averaging any admissible \(Q\) over the symmetric group preserves these two linear inequalities and positivity. An invariant real symmetric or complex Hermitian matrix has one constant diagonal entry and one constant off-diagonal entry; on the zero-sum hyperplane the off-diagonal all-ones part vanishes. Hence the averaged form equals \(c\sum_i|b_i|^2\) for some \(c>0\). Consequently no nonstandard Euclidean position can improve on the restricted coordinate \(\ell_2\) norm, and
\[
 d_{\mathrm{BM}}\bigl(H_n^{\mathbb K},\ell_2^{n-1}(\mathbb K)\bigr)^2
 =\frac{M_n^{\mathbb K}}{m_n^{\mathbb K}},\qquad
 M_n^{\mathbb K}=\max_{N(b)=1}\sum_i|b_i|^2,\quad
 m_n^{\mathbb K}=\min_{N(b)=1}\sum_i|b_i|^2.
\]
This averaging argument covers every invertible real or complex linear change of coordinates, not merely diagonal changes.

**3. The common minimum.** When \(N(b)=1\), choose an index with \(|b_i|=1\). By the zero-sum constraint and Cauchy–Schwarz,
\[
 \sum_{j\ne i}|b_j|^2\ge\frac{|\sum_{j\ne i}b_j|^2}{n-1}=\frac1{n-1}.
\]
Equality is attained at \(b=(1,-1/(n-1),\ldots,-1/(n-1))\); it is valid over either scalar field. Therefore
\[
 m_n^{\mathbb R}=m_n^{\mathbb C}=\frac n{n-1}.
\]

**4. The real maximum and its parity.** The convex function \(b\mapsto\sum_i b_i^2\) achieves a maximum over \(H_n^{\mathbb R}\cap[-1,1]^n\) at a vertex. At least \(n-1\) coordinate bounds must be active at every vertex: if two coordinates were strictly interior, one could perturb them in opposite directions. If \(n\) is even, cancellation of the sum forces all \(n\) coordinates to be signs, with equal numbers of positive and negative signs; each has square sum \(n\). If \(n\) is odd, one coordinate must be zero and the other \(n-1\) coordinates comprise equally many positive and negative signs, with square sum \(n-1\). These patterns exist for every stated \(n\), and so
\[
 M_n^{\mathbb R}=\begin{cases}n,&n\text{ even},\\n-1,&n\text{ odd}.\end{cases}
\]

**5. The complex maximum.** The bound \(\sum_i|b_i|^2\le n\) follows immediately from \(N(b)\le1\). Let \(\zeta=\exp(2\pi\mathrm i/n)\). The vector \((1,\zeta,\ldots,\zeta^{n-1})\) has zero sum and all coordinates of modulus one, so \(M_n^{\mathbb C}=n\). The geometric-series identity is exact for every integer \(n\ge3\).

Substituting the minima and maxima into the exact averaged-ellipsoid formula proves both statements and their scalar-field comparison. \(\square\)

## Verification
A standard-library script, `verify_cycle_hilbert.py`, enumerates **all** real cube-section vertices in dimensions \(3\le n\le11\) with exact integer arithmetic, checks the derived parity maxima, computes the exact rational minimum witnesses and distortion formulas, and separately checks the complex roots-of-unity examples numerically. Execute `python verify_cycle_hilbert.py`; the output ends in `CYCLE_HYPERPLANE_CHECK_OK`. This finite replay tests the combinatorial and normalization formulas, not the unrestricted all-dimensional argument; that argument is in the proof above.

## Relationship to prior work
Godard's tree-metric theorem (arXiv:0904.3178) identifies isometric \(L_1\)-type behavior for tree-derived Lipschitz-free spaces. Alexander, Fradelizi, García-Lirola and Zvavitch (arXiv:1911.10642, especially Sections 3–4) describe finite Lipschitz-free polytopes, the cycle-space quotient model, and the special four-cycle cube. Ostrovska and Ostrovskii (arXiv:2112.02689, Section 1) prove the quotient-over-cycle-space representation. These structural results justify the natural model but do not state the entire sharp Euclidean-distance profile above.

A separately published computation of the numerical index of real cycle transportation spaces uses the **same** zero-sum cube-section model and already supplies the real parity classification of its vertices. That vertex classification is therefore prior work, not a new assertion here. Its numerical-index formula is a different invariant and gives neither the all-dimensional optimal Euclidean ellipsoid nor the complex-scalar distance. The present result combines the scalar-field comparison with the exact all-dimensional Hilbert-distance calculation; the real four-cycle case is familiar and is not claimed as individually new.

## Limitations
All cycle edges must have equal length, and the result is for finite cycles and linear distances to Hilbert space. The real vertex description and graph quotient identification were available in earlier literature. The proof does not determine Hilbert distances of cycles with arbitrary edge weights or uniqueness of every optimal ellipsoid. A classical unindexed treatment of zero-sum hyperplane sections could contain an equivalent distance formula; bibliographic searches do not rule this out. The independent mathematical audit has not been performed.

## References
1. A. Godard, “Tree metrics and their Lipschitz-free spaces,” arXiv:0904.3178v1 (first public preprint 2009-04-21), *Proc. Amer. Math. Soc.* 138 (2010), 4311–4320.
2. M. Alexander, M. Fradelizi, L. C. García-Lirola, and A. Zvavitch, “Geometry and volume product of finite dimensional Lipschitz-free spaces,” arXiv:1911.10642 (first public preprint 2019-11-24), *J. Funct. Anal.* 280 (2021), 108849.
3. S. Ostrovska and M. I. Ostrovskii, “Isometric structure of transportation cost spaces on finite metric spaces,” arXiv:2112.02689 (first public preprint 2021-12-05).
4. “Numerical-index parity law for Lipschitz-free spaces over cycles,” public published-finding corpus record `06885f9d5f05`, available in the publicly indexed findings (2026). The zero-sum cube vertices are taken as known there; the record studies numerical index, not Euclidean Banach–Mazur distance.
