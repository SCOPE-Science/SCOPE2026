# Exact convex geometry and three-site generation of diagonal joint \(q\)-numerical ranges

## Finding
Let \(m\ge2\), let \(\Omega\) be any nonempty compact Hausdorff space, and let \(F:\Omega\to\mathcal B(\mathbb C^m)\) be a norm-continuous family with a single orthonormal basis in which every \(F(s)\) is diagonal. Write its continuous diagonal functions as \(f_1,\ldots,f_m\in C(\Omega)\). For every complex \(q\) with \(|q|\le1\), its joint \(q\)-numerical range is exactly
\[
\mathcal W_q(F)=\left\{\sum_{j=1}^{m}\alpha_j f_j:\ \sum_{j=1}^{m}\alpha_j=q,\quad\sum_{j=1}^{m}|\alpha_j|\le1\right\}.
\]
In particular, the range is compact and convex (in the complex Banach space \(C(\Omega)\), considered as a real locally convex space).

The coefficient body \(K_q\) in this formula has the following *complete extreme-point classification*:

* For \(|q|=1\), its extreme points are exactly \(q e_j\), for \(1\le j\le m\).
* For \(|q|<1\), an admissible coefficient vector \(\alpha\) is extreme if and only if \(\sum_j|\alpha_j|=1\) and the complex unit phases \(\alpha_j/|\alpha_j|\) on its nonzero support are affinely independent when regarded as points of \(\mathbb R^2\). Such an extreme vector has precisely two or three nonzero coordinates; for three coordinates, pairwise distinct phases suffice.

Consequently, whenever \(m\ge3\),
\[
\mathcal W_q(F)=\operatorname{conv}\left(\bigcup_{\substack{J\subset\{1,\ldots,m\}\\ |J|=3}}\mathcal W_q(F|_{\mathbb C^J})\right).
\]
The number three is sharp for every \(|q|<1\): there is a three-dimensional commuting normal projection tuple whose joint \(q\)-numerical range is not the convex hull of its two-dimensional coordinate-compression ranges. For \(|q|=1\), one spectral coordinate already generates the full range by convexification.

## Assumptions and scope
We use the Hilbert inner product linear in its first entry: \(\langle x,y\rangle=\sum_j x_j\overline{y_j}\). The pair constraint is \(\|x\|=\|y\|=1\) and \(\langle x,y\rangle=q\). The map \(s\mapsto F(s)\) is continuous in operator norm, each operator is simultaneously diagonal in a *fixed* common orthonormal basis (not merely pointwise diagonalizable), and \(m\) is finite and at least two. The compressed family \(F|_{\mathbb C^J}\) is the same diagonal family restricted to the coordinate subspace indexed by \(J\); its joint range is defined with unit vectors in that subspace, so \(|J|\ge2\). No assertion is made for arbitrary nonnormal, nonsimultaneously diagonalizable, or infinite-dimensional families.

## Proof
**1. Necessity of the coefficient constraints.** For every allowed pair \((x,y)\), set \(\alpha_j=x_j\overline{y_j}\). Then \(\sum_j\alpha_j=\langle x,y\rangle=q\) and, by Cauchy--Schwarz, \(\sum_j|\alpha_j|\le\|x\|\|y\|=1\). The simultaneous diagonalization yields \(\langle F(s)x,y\rangle=\sum_j\alpha_j f_j(s)\) for every \(s\in\Omega\).

**2. Sufficiency, including every boundary case.** Conversely, suppose \(\alpha\in\mathbb C^m\), \(\sum\alpha_j=q\), and \(S:=\sum|\alpha_j|\le1\). We construct unit vectors satisfying \(x_j\overline{y_j}=\alpha_j\). If \(S=0\), take two different standard basis vectors for \(x,y\); necessarily \(q=0\). If \(S=1\), take \(x_j=\sqrt{|\alpha_j|}\) and \(y_j=\overline{\alpha_j}/\sqrt{|\alpha_j|}\) on the support, and zero elsewhere. Both norms are one. If \(0<S<1\) and the support is a singleton \(\{k\}\), choose \(\ell\ne k\), set \(x_k=|\alpha_k|\), \(x_\ell=\sqrt{1-|\alpha_k|^2}\), \(y_k=\overline{\alpha_k}/|\alpha_k|\), \(y_\ell=0\), and zero elsewhere. Finally, if \(0<S<1\) and at least two coordinates are nonzero, let \(t^{(0)}_j=|\alpha_j|/S\). On the positive-support probability simplex, \(\Phi(t)=\sum_{\alpha_j\ne0}|\alpha_j|^2/t_j\) is continuous, with \(\Phi(t^{(0)})=S^2<1\). Along a path toward the vertex supported at any one nonzero coordinate, \(\Phi(t)\to+\infty\). Hence the intermediate value theorem supplies positive \(t_j\) with \(\sum t_j=1\) and \(\Phi(t)=1\). Put \(x_j=\sqrt{t_j}\), \(y_j=\overline{\alpha_j}/\sqrt{t_j}\) on that support and zero elsewhere. Now \(\|x\|=\|y\|=1\) and the desired coordinate products hold. These cases cover every admissible \(\alpha\), proving the exact range formula. Its right-hand coefficient body is compact and convex, as is its image under the continuous linear map \(\alpha\mapsto\sum\alpha_j f_j\).

**3. Extreme points.** If \(|q|=1\), the inequalities \(1=|\sum\alpha_j|\le\sum|\alpha_j|\le1\) force all nonzero coefficients to have phase \(q\), so \(K_q=q\{t_j\ge0,\ \sum t_j=1\}\). Its vertices are \(q e_j\). Assume now \(|q|<1\). Any \(\alpha\) with \(\sum|\alpha_j|<1\) is not extreme: since \(m\ge2\), a sufficiently small nonzero perturbation \(\pm\varepsilon(e_1-e_2)\) preserves \(\sum\alpha_j=q\) and stays inside the \(\ell_1\) ball.

Let \(\sum|\alpha_j|=1\), let \(J=\{j:\alpha_j\ne0\}\), and put \(u_j=\alpha_j/|\alpha_j|\). If \(\alpha=(\beta+\gamma)/2\) with \(\beta,\gamma\in K_q\), equality in the triangle inequality and in the norm bound forces \(\beta_j= b_j u_j\), \(\gamma_j=c_j u_j\), with \(b_j,c_j\ge0\) for \(j\in J\), and both coefficients zero off \(J\). The difference is \(\beta-\gamma=(t_j u_j)_{j\in J}\) for real \(t_j\), subject to \(\sum_{J}t_j=0\) and \(\sum_{J}t_j u_j=0\). Conversely, any nonzero real solution to these three real homogeneous linear constraints, multiplied by sufficiently small positive \(\varepsilon\), gives two distinct feasible vectors \(\alpha\pm\varepsilon(t_j u_j)\). Thus \(\alpha\) is extreme exactly when the column vectors \((1,\Re u_j,\Im u_j)\), \(j\in J\), are linearly independent over \(\mathbb R\), i.e. when the phase points are affinely independent in the plane. There can be no more than three. Three distinct points on a circle are noncollinear; one-point support cannot occur when \(|q|<1\), and two-point boundary support necessarily has distinct phases.

**4. Three-site reduction and sharpness.** A compact convex body in a finite-dimensional real vector space is the convex hull of its extreme points. Every extreme coefficient vector of \(K_q\) has support at most three, and any such vector can be realized by an allowed unit pair within some three-coordinate subspace, by Step 2. This proves the three-site formula after applying the linear coefficient-to-function map.

For sharpness, take \(\Omega=\{1,2,3\}\) and \(F(s)=e_s e_s^*\) on \(\mathbb C^3\). Then \(\mathcal W_q(F)=K_q\) itself. For \(r=|q|<1\), choose a unit complex \(\zeta\) with \(q=r\zeta\) when \(r>0\), and \(\zeta=1\) otherwise. With \(\omega=e^{2\pi i/3}\), let
\[
\alpha=\frac{\zeta}{3}\bigl(1+2r,\ (1-r)\omega,\ (1-r)\omega^2\bigr).
\]
Its coefficient sum is \(q\), its \(\ell_1\) norm is one, and its three nonzero phases are distinct. Step 3 makes \(\alpha\) extreme. Since it uses all three coordinates, it cannot lie in the convex hull of feasible coefficient vectors supported on at most two coordinates: any such representation by two-site points would contradict extremality. This gives a sharp witness for every \(|q|<1\).

## Verification
The entire proof is finite-dimensional analysis and covers every integer \(m\ge2\), every \(q\) with \(|q|\le1\), and every continuous simultaneously diagonal family over an arbitrary compact Hausdorff space. The attached standalone numerical checker samples feasible coefficient factorizations, confirms the constructive sufficiency algorithm, verifies the exact sharpness family and tests the real phase-rank criterion. It does not certify the infinite parameter ranges; Steps 1--4 supply the proof.

## Relationship to prior work
Azadi (2026, arXiv:2610.32504) introduced the continuous-operator-valued joint \(q\)-range, proved total boundedness and finite-dimensional compactness, and gave a realization theorem for \(|q|=1\). Its proof contains the necessary coefficient \(\ell_1\) inequality for a particular diagonal realization; it does not establish the general coefficient *sufficiency*, convexity for simultaneously diagonal families at \(|q|<1\), a full extreme-point classification, or sharp universal three-site generation. Feki--Patra--Rani--Taki (arXiv:2410.03669) proved general joint-range inequalities and convexity for commuting tuples in dimension two; their examples establish possible nonconvexity without the simultaneous diagonal assumption, but they do not give the all-dimension normal classification here. Chien--Nakazato (2005) established a three-eigenvalue reduction for the *scalar* \(q\)-numerical range of certain normal operators; scalar image projections do not by themselves describe the entire simultaneous function-valued range, its coefficient extreme points, or their sharpness. Earlier \(q\)-numerical-range work on normal matrices is relevant but not identified with the exact present theorem.

## Limitations
This is a structural classification for finite-dimensional *simultaneously diagonal* families. The phase independence test describes the coefficient body, not necessarily the extreme points of its potentially noninjective image in \(C(\Omega)\). A three-site reduction is a convex-hull statement; individual range values need not lie in a single three-dimensional compression. The q-range may be nonconvex outside the stated class. Equivalence through more general results on constrained complex \(\ell_1\) sections or classical scalar normal \(q\)-ranges is a remaining publication-priority risk. No independent mathematical validation is asserted.

## References
1. A. Azadi, *Joint q-Numerical Ranges of Continuous Operator-Valued Functions*, arXiv:2610.32504v1 (first publicly available 2026-10-23), https://arxiv.org/abs/2610.32504.
2. K. Feki, A. Patra, J. Rani, Z. Taki, *Joint q-Numerical Ranges of Operators in Hilbert and Semi-Hilbert Spaces*, arXiv:2410.03669 (initially public 2024-09-12), https://arxiv.org/abs/2410.03669.
3. M.-T. Chien and H. Nakazato, *The q-numerical ranges of normal operators*, Linear and Multilinear Algebra 53 (2005), 393--416, https://doi.org/10.1080/03081080500156888.
4. C.-K. Li, *q-numerical ranges of normal and convex matrices*, Linear and Multilinear Algebra 43 (1998), 377--384, https://doi.org/10.1080/03081089808818538.
