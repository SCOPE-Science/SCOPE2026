# Complete spectral–Frobenius region for cubic moments of minimal-state isotropic laws

## Finding

For an integer \(d\ge2\), let \(X\) be a real random vector with exactly \(m=d+1\) distinct atoms \(v_1,\ldots,v_m\), strictly positive masses \(p_1,\ldots,p_m\), and normalization
\[
\mathbb EX=0,\qquad \mathbb E(XX^\top)=I_d.
\]
Set \(q=\min_i p_i\), let \(T=\mathbb E[X^{\otimes3}]\), and measure its cubic spectral and Hilbert–Schmidt norms by
\[
K=\max_{\|a\|_2=1}|T[a,a,a]|,\qquad
H^2=\sum_{a,b,c=1}^{d}T_{abc}^2.
\]
Then \(0<q\le 1/(d+1)\), and the **exact** spectral norm is
\[
\boxed{K=\frac{1-2q}{\sqrt{q(1-q)}}.}\tag{1}
\]
Every unit maximizer is a positive or negative multiple of an atom \(v_i\) with \(p_i=q\). Thus the smallest atom mass is exactly recoverable from the cubic spectral norm:
\[
\boxed{q=\frac12\left(1-\frac{K}{\sqrt{K^2+4}}\right).}\tag{2}
\]
The precise feasible range of the **other** cubic norm, conditional on this fixed spectral norm, is
\[
\boxed{
\frac1q+\frac{d^2}{1-q}-3d-1
\ \le\ H^2\ \le\
\frac d q+\frac1{1-dq}-3d-1.}
\tag{3}
\]
Every value in this closed interval occurs for a law satisfying the hypotheses and having the same \(K\). The lower equality profile is, up to relabeling,
\[
\left(q,\frac{1-q}{d},\ldots,\frac{1-q}{d}\right),
\]
and the upper equality profile is
\[
\left(1-dq,q,\ldots,q\right).
\]
When \(q<1/(d+1)\), these are the unique equality probability profiles up to relabeling. All atomic realizations with a prescribed probability profile are orthogonally equivalent.

In particular, over all such finite-state laws,
\[
K\ge\frac{d-1}{\sqrt d},\qquad H^2\ge d(d-1),
\]
with simultaneous equality **exactly** for the uniform regular isotropic simplex. The squared tensor norm also has the exact probability-divergence decomposition
\[
\boxed{H^2=d(d-1)+(d+1)^2\chi^2(U_{d+1}\Vert p),}\tag{4}
\]
where \(U_{d+1}\) is the uniform probability vector and
\(\chi^2(U_{d+1}\Vert p)=\sum_i((d+1)^{-1}-p_i)^2/p_i\).

For fixed \(d\), as \(q\downarrow0\), the ratio of the upper and lower attainable **squared** tensor energies tends to \(d\), despite their identical worst-direction cubic coefficient. Thus the norm pair distinguishes concentrated from distributed third-order bias at the same sharp directional obstruction.

## Assumptions and scope

All vector spaces and tensors are real. The support has exactly \(d+1\) atoms, probabilities are strictly positive, and covariance is precisely the identity. These conditions also make the one-step scalar predictable representation property automatic: the constant function and \(d\) coordinate functions constitute an orthonormal basis for all scalar functions on the support. No ordering or geometric restrictions beyond the stated normalization are imposed. For \(d=1\), the uniform two-point law has vanishing third moment, so the positive barrier and the nontrivial interval statement are explicitly restricted to \(d\ge2\).

The claim concerns the symmetric third-moment tensor. It does not assert optimality for higher moments, non-isotropic increments, or state-dependent/time-inhomogeneous schemes. Equation (3) is an *attainable region*, not an inequality between two opposing objective functions: both norms are minimized by the regular simplex.

## Proof

**Step 1: complete-support geometry.** Form the \(d\)-by-\(m\) matrix \(V\) with columns \(\sqrt{p_i}v_i\), and the vector \(u=(\sqrt{p_1},\ldots,\sqrt{p_m})^\top\). Centering and isotropy give \(Vu=0\) and \(VV^\top=I_d\). Since \(V\) has rank \(d=m-1\), its row-space projector is
\[
V^\top V=I_m-uu^\top.
\]
Taking matrix entries yields
\[
\|v_i\|^2=\frac1{p_i}-1,\qquad v_i\cdot v_j=-1\quad(i\ne j).
\tag{5}
\]
Conversely, for every positive probability vector \(p\), complete the unit vector \(u\) to an orthogonal \(m\)-by-\(m\) matrix with first row \(u^\top\). Dividing its remaining \(d\) row entries in column \(i\) by \(\sqrt{p_i}\) constructs an admissible atomic law. Two choices differ by an orthogonal transformation of \(\mathbb R^d\). Thus there are no hidden constraints on \(p\).

**Step 2: exactly optimize the cubic spectral norm.** Because the functions \(1,X_1,\ldots,X_d\) are an orthonormal basis of \(L^2(p)\), the map \(a\mapsto (a\cdot v_i)_i\) is an isometric bijection from \(\mathbb R^d\) onto the weighted mean-zero hyperplane. Consequently,
\[
K=\max\left\{\left|\sum_i p_i z_i^3\right|:\ \sum_i p_i z_i=0,\ \sum_i p_i z_i^2=1\right\}.
\tag{6}
\]
The constraint set is compact and smooth: the gradients of the two constraints are linearly independent there, because a variance-one vector \(z\) is not constant. At a constrained extremum, Lagrange multipliers satisfy
\[
3z_i^2=\lambda+2\mu z_i\qquad\text{for every }i.
\]
Thus there are exactly two distinct values of \(z_i\). Let the upper value have total mass \(P\in(0,1)\); solving the zero-mean/unit-variance equations gives the upper value \(\sqrt{(1-P)/P}\), the lower value \(-\sqrt{P/(1-P)}\), and the cubic moment
\[
b(P)=\frac{1-2P}{\sqrt{P(1-P)}}.
\]
Each of the two nonempty groups contains an atom, so \(P\ge q\) and \(1-P\ge q\). The function \(b\) is strictly decreasing and satisfies \(b(1-P)=-b(P)\); hence \(|b(P)|\le b(q)\), with equality exactly when a group is a singleton of mass \(q\). Such a profile is achieved by the standardized centered indicator of any minimum-mass atom. Its vector realization is \(a=\pm v_i/\|v_i\|\), by (5). This proves (1), the stated spectral maximizers, and the inversion (2). Because \(q\le1/m\) with equality exactly when all masses are uniform, the sharp global lower bound for \(K\) follows, including its equality case.

**Step 3: exact Hilbert–Schmidt identity.** The full scalar function space has the orthonormal basis \(1,X_1,\ldots,X_d\). Expanding the centered quadratic monomial yields
\[
X_aX_b-\delta_{ab}=\sum_{c=1}^{d}T_{abc}X_c.
\]
Taking squared \(L^2\) norms and summing over \(a,b\) gives
\[
H^2=\sum_{a,b}\mathbb E[(X_aX_b-\delta_{ab})^2]
=\mathbb E\|X\|^4-d.
\tag{7}
\]
Insert \(\|v_i\|^2=p_i^{-1}-1\) from (5):
\[
H^2=\sum_i p_i(p_i^{-1}-1)^2-d
=\sum_i\frac1{p_i}-3m+2.
\tag{8}
\]
Expanding the stated Pearson divergence gives
\[
m^2\chi^2(U_m\Vert p)=\sum_i\frac1{p_i}-m^2.
\]
With \(m=d+1\), equations (7)–(8) yield (4), including sharp nonnegative stability and the uniform equality case.

**Step 4: complete conditional range.** Fix \(q\in(0,1/m]\); (1) fixes \(K\). After relabeling \(p_1=q\), the remaining \(d\) masses range over the compact convex polytope
\[
p_2,\ldots,p_m\ge q,\qquad \sum_{i=2}^{m}p_i=1-q.
\]
By strict convexity of \(x\mapsto1/x\) and Jensen's inequality, the minimum of \(\sum_{i=2}^{m}1/p_i\) occurs precisely when all remaining masses equal \((1-q)/d\), producing the lower endpoint in (3). A convex function attains its maximum over a polytope at a vertex; every vertex has \(d-1\) of the remaining masses equal to \(q\), and the last equal to \(1-dq\). Strict convexity shows that all global maximizers lie at these vertices, producing the upper endpoint. Both equality cases are admissible by Step 1. The straight line between a minimizing and maximizing probability profile on this same face retains \(p_1=q\) and all other masses at least \(q\). Continuity of (8) on this line realizes *every* intermediate energy. This proves the full range, not only its endpoints.

**Step 5: Brownian weak-Fourier interpretation.** Take iid copies \(X_1,X_2,\ldots\), a fixed \(\tau>0\), \(h=\tau/N\), and \(S_N=\sqrt h\sum_{j=1}^{N}X_j\). For each unit \(a\), a third-order characteristic-function expansion, uniform over the unit sphere because the support is finite, gives
\[
\mathbb E\exp(i a\cdot S_N)
=e^{-\tau/2}\left(1-i\frac{\tau\sqrt h}{6}T[a,a,a]+O(h)\right).
\]
Therefore, if \(B_\tau\) is standard \(d\)-dimensional Brownian motion,
\[
\boxed{\lim_{N\to\infty}\frac1{\sqrt{\tau/N}}\sup_{\|a\|=1}
\left|\mathbb E\sin(a\cdot S_N)-\mathbb E\sin(a\cdot B_\tau)\right|
=\frac{\tau e^{-\tau/2}}6K.}\tag{9}
\]
Combining (9) with (1) and (3) quantifies the common worst-direction Fourier error shared by laws whose *total* cubic-tensor energies can range over a complete, dimension-dependent interval. This application uses the **same fixed increment law at every step**; it makes no barrier claim for alternating increments.

## Verification

Run `python3 verify.py` with Python 3 and NumPy installed. Its exact-rational checks compare the Gram contraction \(\sum_{ij}p_ip_j(v_i\cdot v_j)^3\) with equations (4) and (8), the weighted Gram projector identities, all two-level partition stationary values on the sampled supports, Jensen/vertex endpoints, and interior interpolations. A dense directional numerical grid in dimension two and characteristic-function evaluations check the interpretation of (1) and (9). The executed program reported **49,319 passing exact-rational or deterministic numerical checks**. The proof of all-dimensional statements is Steps 1–5; a finite computation cannot certify those quantifiers.

For an exact small-dimensional witness, take \(d=2\), \(q=1/4\). The profiles \((1/4,3/8,3/8)\) and \((1/4,1/4,1/2)\) both have \(K=2/\sqrt3\), yet their squared tensor norms are respectively \(7/3\) and \(3\). Thus identical worst-direction bias does not determine aggregate third-order energy.

## Relationship to prior work

Tanaka's arXiv:2610.20880v1 establishes that exact finite-state scalar predictable representation in \(d\ge2\) forces some nonzero cubic direction (Theorem 8.3), and explains the associated qualitative square-root weak-Fourier error (Corollary 8.5). The sharp spectral coefficient and the complete conditional interval of squared tensor energies in (3) are not stated there.

Attal, Deschamps, and Pellegrini, arXiv:1312.3731, Proposition 2.3 and Proposition 2.7, develop the obtuse-system geometry and its cubic structure tensor. The support identities and quadratic expansions in Steps 1 and 3 are consequences of that established algebra. Their inspected tensor-characterization sections do not supply the two-norm feasible-region classification (1)–(4).

The published result *Endpoint masses determine the exact skewness range of a discrete law* gives sharp one-dimensional skewness extrema for fixed ordered masses with **distinct** projected support values. This genuinely covers the scalar skewness optimization underlying Step 2 after allowing tied projection values in the closure. We do **not** assert Step 2 on its own as an original discovery. The subject of the present classification is instead the exact **joint** range of cubic tensor spectral and Hilbert–Schmidt norms of minimal-state isotropic vector laws at fixed maximal directional skewness; that prior scalar statement neither defines nor constrains the other tensor norm. The proof includes the scalar calculation for self-containment and explicitly acknowledges its coverage.

The full joint statement combines finite-state geometry, the spectral interpretation, a tensor-energy identity, and a sharp fixed-spectral-energy feasible-region calculation. No inspected source contains a stronger theorem that determines this whole feasible region or its two sharply distinct extremizer profiles. Novelty is assessed for this combined result, not for any cited or elementary component separately.

## Limitations

This is a self-review, not independent verification. Older treatments of obtuse-variable tensor norms or joint skewness/fourth-moment optimization may contain equivalent feasible-region formulas under different nomenclature; the literature search is targeted rather than exhaustive. The extremal spectral mass formula is a covered scalar optimization ingredient, explicitly credited above.

The theorem requires exactly \(d+1\) atoms, all with positive weights, an identity covariance, and a real support. If support is larger than \(d+1\), the linear-coordinate predictable representation property fails and equation (7) need not hold. The Brownian Fourier interpretation is asymptotic and uses iid increments of one fixed law; it is not a uniform finite-step bound or an assertion about general BSDE convergence.

## References

1. A. Tanaka, *Third-moment cancellation and predictable representation in finite-state BSDE approximation*, arXiv:2610.20880v1, first public 2026-10-14. In particular §§7–8, Theorem 8.3 and Corollary 8.5. https://arxiv.org/abs/2610.20880
2. S. Attal, J. Deschamps, C. Pellegrini, *Complex Obtuse Random Walks and their Continuous-Time Limits*, arXiv:1312.3731v2, in particular §§2.2–2.4 and §3. https://arxiv.org/abs/1312.3731
3. *Endpoint masses determine the exact skewness range of a discrete law*, published mathematical record (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-endpoint-masses-determine-the-exact-skewness-range-of-a-discrete--4f6817ccede3
