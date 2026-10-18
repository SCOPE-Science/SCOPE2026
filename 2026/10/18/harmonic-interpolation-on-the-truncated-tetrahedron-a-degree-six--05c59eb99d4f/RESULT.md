# Harmonic interpolation on the truncated tetrahedron: a degree-six cycle obstruction

## Finding
Let \(v_0=(1,1,1)\), \(v_1=(1,-1,-1)\), \(v_2=(-1,1,-1)\), and \(v_3=(-1,-1,1)\). On the unit sphere \(S^2\), let
\[
 X=\{x_{ij}=(2v_i+v_j)/\sqrt{11}:0\le i,j\le3,\ i\ne j\}.
\]
These are the twelve vertices of the uniformly truncated regular tetrahedron. For each integer \(\ell\ge0\), evaluate the **single exact degree** complex spherical-harmonic space \(\mathcal H_\ell(S^2)\) at the twelve labelled points, obtaining \(E_\ell:\mathcal H_\ell\to\mathbb C^{12}\). Its complete rank law is
\[
\bigl(\operatorname{rank}E_0,\ldots,\operatorname{rank}E_6\bigr)
=(1,3,5,7,9,11,9),\qquad
\operatorname{rank}E_\ell=12\quad(\ell\ge7).
\]
The failure at degree six is a genuine rank reversal: the harmonic source has dimension thirteen, but its sample image has dimension nine. A data array \(y=(y_{ij})_{i\ne j}\) belongs to \(\operatorname{im}E_6\) **if and only if** the antisymmetric edge differences have zero circulation around every tetrahedral triangle:
\[
 (y_{ij}-y_{ji})+(y_{jk}-y_{kj})+(y_{ki}-y_{ik})=0
 \quad\text{for all distinct }i,j,k.
\]
There are exactly three independent conditions. At degree five the sole condition is \(\sum_{i\ne j}y_{ij}=0\). Degree seven is both the first and the permanent degree of arbitrary interpolation.

More explicitly, write
\[
p=P_\ell(7/11),\qquad q=P_\ell(-5/11),\qquad
r=P_\ell(-1/11),\qquad s=P_\ell(-9/11),
\]
where \(P_\ell\) is the Legendre polynomial normalized by \(P_\ell(1)=1\). Divide the twelve-by-twelve reproducing-kernel Gram matrix by \(2\ell+1\). Its spectrum is exactly the union of the following blocks:
\[
\begin{aligned}
\lambda_{\mathrm{const}}&=1+3p+2q+4r+2s &&\text{(multiplicity 1)},\\
\lambda_{\mathrm{sym}}&=1-q-2r+2s &&\text{(multiplicity 2)},\\
\lambda_{\mathrm{cycle}}&=1-2p-q+2r &&\text{(multiplicity 3)},
\end{aligned}
\]
together with the two eigenvalues of
\[
M_\ell=\begin{pmatrix}
1+2p-q-r-s&r-s\\
p-q+r-s&1-p+2q-r-s
\end{pmatrix},
\]
each repeated three times. The matrix displayed is in a nonorthogonal, but nonsingular, basis; its eigenvalues are real and nonnegative because this is a self-adjoint Gram operator. These formulas also give a blockwise pseudoinverse in every degree.

## Assumptions and scope
The sphere has probability-normalized surface measure. Accordingly, for an orthonormal harmonic basis the reproducing kernel is \(K_\ell(u,v)=(2\ell+1)P_\ell(u\cdot v)\). Sampling uses all twelve **distinct ordered-edge labels** \((i,j)\), each once, with the ordinary Euclidean norm on \(\mathbb C^{12}\). No parity reduction or union of harmonic degrees is imposed. All rank statements are over \(\mathbb C\), for every integer \(\ell\ge0\). The normalization is fixed by the coordinates and the addition theorem; multiplying the Gram matrix by a positive scalar does not affect rank.

## Proof
**Geometry.** The integer tetrahedral vertices satisfy \(v_i\cdot v_i=3\) and \(v_i\cdot v_j=-1\) for \(i\ne j\); thus \(\|2v_i+v_j\|^2=11\). Fix an ordered edge \((i,j)\). Its eleven other vertices have dot products \(7/11,-5/11,-1/11,-9/11\) with multiplicities respectively \(3,2,4,2\). More precisely, the \(7/11\) entries comprise two edges with the same source and the reverse edge; the \(-5/11\) entries share the target; the \(-1/11\) entries form the four remaining adjacent ordered-edge chains; and the \(-9/11\) entries use the two complementary vertices. By the addition theorem, the normalized Gram matrix is \(A_\ell=(P_\ell(x_{ij}\cdot x_{kl}))\).

**Invariant decomposition.** Regard a sample vector as an array \(f_{ij}\), with row sums \(R_i=\sum_{j\ne i}f_{ij}\), column sums \(C_i=\sum_{j\ne i}f_{ji}\), and grand sum \(S=\sum_{i\ne j}f_{ij}\). Directly summing the five inner-product classes gives
\[
\begin{split}
(A_\ell f)_{ij}={}&(1-p-q+s)f_{ij}+(p-2r+s)f_{ji}\\
&+(p-s)R_i+(q-s)C_j+(r-s)(R_j+C_i)+sS.
\end{split}
\]
The twelve-dimensional ordered-edge space splits orthogonally as: constants (dimension one); symmetric arrays with zero row sums (dimension two); antisymmetric arrays with zero row sums (dimension three); and the span of arrays \(f_{ij}=a_i\) and \(f_{ij}=a_j\), for \(\sum_i a_i=0\) (dimension six). The first three spaces give the three scalar eigenvalues shown in the Finding. On the last space, a source-coordinate array and a target-coordinate array transform by \(M_\ell\), identically on three independent choices of \(a\). All twelve dimensions are accounted for, proving the spectral decomposition.

**Exceptional degrees.** Use \(P_0(t)=1\), \(P_1(t)=t\), and
\[
 (n+1)P_{n+1}(t)=(2n+1)tP_n(t)-nP_{n-1}(t).
\]
Substitution into the scalar blocks and the determinant and trace of \(M_\ell\) gives ranks \(1,3,5,7,9,11,9\) for \(\ell=0,1,2,3,4,5,6\). In degree five only the constant scalar block is zero. In degree six only the antisymmetric zero-row-sum block is zero; for instance its eigenvalue is exactly \(1-2P_6(7/11)-P_6(-5/11)+2P_6(-1/11)=0\), whereas the constant and symmetric eigenvalues equal \(384/14641\) and \(5376/14641\), and \(\det M_6=7965941760/2357947691>0\). Orthogonality to antisymmetric zero-divergence flows is precisely the stated cycle-circulation condition: on the complete tetrahedral graph, the orthogonal complement of the cycle space is the gradient space \(a_i-a_j\). All constraints and their stated independence follow.

**All later degrees.** For every \(7\le\ell\le575\), the attached exact rational checker evaluates the four Legendre values by the displayed recurrence and verifies \(\lambda_{\mathrm{const}}>0\), \(\lambda_{\mathrm{sym}}>0\), \(\lambda_{\mathrm{cycle}}>0\), \(\operatorname{tr}M_\ell>0\), and \(\det M_\ell>0\). All comparisons use Python's exact rational arithmetic, not floating-point tolerances. Together with real eigenvalues, they imply positive definiteness. This is a finite exhaustive check of **all 569 integers** in that specified interval, with complete code included.

For \(\ell\ge576\), one can instead prove positivity without computation. The elementary Laplace representation for \(-1<t<1\) gives
\[
P_\ell(t)=\frac1\pi\int_0^\pi
 \bigl(t+i\sqrt{1-t^2}\cos\theta\bigr)^\ell\,d\theta.
\]
Taking absolute values, using \(1-u\le e^{-u}\), and the concavity inequality \(\sin\theta\ge2\theta/\pi\) on \([0,\pi/2]\), followed by a Gaussian integral, yields
\[
 |P_\ell(t)|\le\sqrt{\frac{\pi}{2\ell(1-t^2)}}.
\]
Every off-diagonal dot product has \(|t|\le9/11\), so the sum of the eleven off-diagonal absolute values in any row is at most
\[
 11\sqrt{\frac{121\pi}{80\ell}}
 <\sqrt{\frac{322102}{560\ell}}<1\qquad(\ell\ge576),
\]
where only \(\pi<22/7\) is used. The real symmetric matrix \(A_\ell\), with unit diagonal, is therefore strictly diagonally dominant and positive definite. Combining this with the finite interval proves full rank for every \(\ell\ge7\).

**Interpolation formula.** For any \(\ell\ge7\) and \(y\in\mathbb C^{12}\), define \(G_\ell=(2\ell+1)A_\ell\). The unique minimum-\(L^2\)-norm interpolating harmonic is
\[
 f_y(u)=\sum_{i\ne j}(G_\ell^{-1}y)_{ij}\,K_\ell(u,x_{ij}),
 \qquad \|f_y\|_{L^2}^2=y^*G_\ell^{-1}y.
\]
This is the standard reproducing-kernel projection formula and does not claim uniqueness among all interpolating harmonics.

## Verification
Run `python3 check_exact.py` with standard Python 3 and no external packages. It reconstructs all twelve integer vertex triples, confirms all geometric dot classes, performs exact rational Legendre recurrence checks for the 569 degrees \(7\) through \(575\), directly row-reduces the full rational Gram matrix at all degrees \(0\) through \(12\), and asserts the seven exceptional rank values. An independent exact cycle vector computation confirms annihilation at degree six but not at degrees five or seven. The bound for all degrees at least 576 is proved above, not inferred from the checker.

## Relationship to prior work
Bannai, Okuda, and Tagami (2013) develop harmonic-index spherical designs and the same normalized Gegenbauer/Legendre reproducing kernels; their principal results concern existence and lower bounds for vanishing **constant-sum** harmonic moments, not the ordered-edge cycle obstruction or complete single-degree sample-image classification here. Khalid, Kennedy, and McEwen (2014) analyze optimal-dimensionality spherical-harmonic transforms using latitude rings for whole bandlimits; neither the Archimedean vertex orbit nor its degree-six rank reversal is their sampling design. Fritz (2009, thesis submission date) constructs algebraic surfaces with singularities at the *same truncated-tetrahedral vertex coordinates*, including an ordinary degree-six polynomial; such a singular algebraic surface is not a homogeneous harmonic sampling operator and does not imply its Gram nullity. The geometry, the exact-degree hypothesis, and the statement-to-statement distinction matter here. The finite polyhedral point coordinates are classical; the novelty claim concerns the all-degree harmonic ranks, three-dimensional cycle obstruction, and sharp permanent degree.

## Limitations
This is a single exact-degree interpolation result for one fixed, uniformly truncated tetrahedral orbit, not a general theorem for arbitrary truncation parameters, arbitrary twelve-point sets, or simultaneous multi-degree reconstruction. The exact finite interval is checked by transparent reproducible rational code, rather than by a short closed-form positivity identity valid for every one of its degrees. The normalized minimum-norm formula does not assert sharp condition-number bounds. Possible implicit equivalents in older tetrahedral invariant-theory or numerical-harmonic tables remain a literature-priority risk; no independent mathematical audit or priority certification is claimed.

## References
1. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101v1, first posted 2013-08-23, https://arxiv.org/abs/1308.5101.
2. Z. Khalid, R. A. Kennedy, J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661v1, first posted 2014-03-19, https://arxiv.org/abs/1403.4661.
3. A. Fritz, *Platonic stars: Construction of algebraic curves and surfaces with prescribed symmetries and singularities*, diploma thesis submitted 2009-12-11, §3.2.2, https://homepage.univie.ac.at/herwig.hauser/Publications/diplom_fritz.pdf (submission date is not asserted to be first online release).
4. E. W. Weisstein, *Truncated Tetrahedron*, MathWorld, https://mathworld.wolfram.com/TruncatedTetrahedron.html (coordinate and polyhedral context only).
