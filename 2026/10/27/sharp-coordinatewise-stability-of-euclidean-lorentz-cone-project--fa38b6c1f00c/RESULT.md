# Sharp coordinatewise stability of Euclidean Lorentz-cone projection

## Finding
Let \(d\ge1\) be an integer, \(K_d=\{(s,x)\in\mathbb R\times\mathbb R^d:s\ge\|x\|_2\}\), and let \(\Pi_d\) denote the **Euclidean** nearest-point map onto \(K_d\). Measure errors by the coordinatewise norm \(\|(s,x)\|_\infty=\max\{|s|,|x_1|,\ldots,|x_d|\}\), rather than by the Euclidean metric defining \(\Pi_d\). Define its global sharp modulus by
\[
\mathcal L_d=\sup_{z\ne w}\frac{\|\Pi_d(z)-\Pi_d(w)\|_\infty}{\|z-w\|_\infty}.
\]
For \(d=2,3,4\), let \(a_d\) be the **unique** root in \((1/2,1/\sqrt2)\) of
\[
1-2a+\sqrt{d-1}\frac{1-2a^2}{\sqrt{1-a^2}}=0.
\]
Then the exact sharp constant has a dimension-five transition:
\[
\boxed{\mathcal L_d=
\begin{cases}
1,&d=1,\\
1+\tfrac12\bigl(a_d-a_d^2+\sqrt{d-1}\,a_d\sqrt{1-a_d^2}\bigr),&2\le d\le4,\\
\tfrac12(1+\sqrt d),&d\ge5.
\end{cases}}
\]
Numerically the exceptional constants are \(\mathcal L_2\approx1.361178997925\), \(\mathcal L_3\approx1.463035638121\), and \(\mathcal L_4\approx1.541623172494\). In dimensions two through four, the most sensitive **output** is a spatial coordinate; for every dimension at least five, it is the distinguished scalar coordinate. All constants are sharp as suprema of two-point Lipschitz quotients, approached by explicitly specified first differences.

## Assumptions and scope
All dimensions and scalars are real, \(d\ge1\), and the target is the standard, *unscaled* Lorentz (second-order) cone. The projection minimizes Euclidean squared distance; only its perturbations are measured in \(\ell_\infty\). Theorem makes no statement about projections minimizing \(\ell_\infty\) distance, weighted coordinate norms, or general cones. For \(z=(s,x)\), write \(r=\|x\|_2\). The standard, explicitly verified projection formula is
\[
\Pi_d(s,x)=\begin{cases}
(s,x),&s\ge r,\\
(0,0),&s\le-r,\\
\tfrac{s+r}{2}\bigl(1,x/r\bigr),&-r<s<r.
\end{cases}
\]
The third case has \(r>0\); definitions agree continuously at its two boundaries.

## Proof
**1. Kernel of the sharp sensitivity calculation.** On the smooth intermediate region write \(u=x/r\), so \(\|u\|_2=1\), and \(t=s/r\in(-1,1)\). Differentiation of the displayed projection formula, using \(\mathrm d r=u^{\mathsf T}\mathrm d x\) and \(\mathrm d u=(I-uu^{\mathsf T})\mathrm d x/r\), gives the full Jacobian
\[
D\Pi_d=\frac12\begin{pmatrix}
1&u^{\mathsf T}\\
u&(1+t)I-tuu^{\mathsf T}
\end{pmatrix}.
\]
Elsewhere the derivatives are respectively \(I\) and \(0\). The induced \(\ell_\infty\) matrix norm is its largest absolute row sum. The distinguished scalar row has sharp supremum
\[
\sup_{\|u\|_2=1}\frac{1+\|u\|_1}{2}=\frac{1+\sqrt d}{2},
\]
with equality precisely when all magnitudes \(|u_j|\) equal \(1/\sqrt d\).

**2. Spatial rows.** Fix spatial row \(i\) and set \(a=|u_i|\), \(S=\sum_{j\ne i}|u_j|\). Its diagonal entry is nonnegative for every \(-1<t<1\), because \(1+t(1-a^2)\ge a^2\ge0\). Its absolute row sum is therefore
\[
R_i(t,u)=\frac12\bigl[a+1+t(1-a^2)+|t|aS\bigr].
\]
This piecewise-affine function attains its supremum as \(t\uparrow1\): the \(t=1\) endpoint dominates both \(t=0\) and \(t=-1\). By Cauchy--Schwarz, \(S\le\sqrt{(d-1)(1-a^2)}\), with equality realizable whenever the other \(d-1\) coordinate magnitudes agree. Thus for every \(d\ge2\), the exact spatial-row supremum is
\[
V_d=1+\frac12\max_{0\le a\le1}g_d(a),\qquad
g_d(a)=a-a^2+\sqrt{d-1}\,a\sqrt{1-a^2}.
\]
The maximizer is unique: on \((0,1)\),
\[
g_d''(a)=-2+\sqrt{d-1}\,\frac{a(2a^2-3)}{(1-a^2)^{3/2}}<0.
\]
Moreover \(g_d'(1/2)>0\) and \(g_d'(1/\sqrt2)<0\), so this maximizer is exactly the uniquely defined \(a_d\in(1/2,1/\sqrt2)\). This definition is valid for every \(d\ge2\), though the spatial branch wins only when \(d\le4\).

**3. Proving the exact transition.** Comparing \(V_d\) against the scalar branch amounts to comparing \(g_d(a)\) with \(\sqrt d-1\). For \(2\le d\le4\), the test \(a=1/\sqrt2\) gives
\[
g_d(1/\sqrt2)=1/\sqrt2-1/2+\sqrt{d-1}/2>\sqrt d-1.
\]
Hence the spatial branch wins strictly. At \(d=5\), put \(b=\sqrt{1-a^2}\). Since \(a+b\le\sqrt2\),
\[
g_5(a)=a-a^2+2ab\le(1+2\sqrt2)a-3a^2
\le\frac{(1+2\sqrt2)^2}{12}=\frac{9+4\sqrt2}{12}<\frac{11}{9}<\sqrt5-1.
\]
For every fixed \(a\in[0,1]\), extend the dimension variable continuously to \(d\ge5\) and differentiate:
\[
\frac{\partial}{\partial d}\bigl(g_d(a)-\sqrt d+1\bigr)
=\frac{a\sqrt{1-a^2}}{2\sqrt{d-1}}-\frac1{2\sqrt d}
\le\frac1{4\sqrt{d-1}}-\frac1{2\sqrt d}<0.
\]
So \(g_d(a)<\sqrt d-1\) for every integer \(d\ge5\), proving strict scalar-row dominance. For \(d=1\), the cone is a right-angle planar wedge, its two nontrivial linear projection pieces have maximum row sum one, and \(\mathcal L_1=1\).

**4. Passing from local derivatives to the global sharp norm.** The projection is continuous and piecewise smooth. Along a straight input segment, region boundaries solve \(s^2=\|x\|_2^2\) together with signs; unless the quadratic identity holds throughout, there are finitely many crossings. On any segment contained in a boundary surface, the projection acts identically (positive boundary) or vanishes (negative boundary). Split an arbitrary segment at crossings and integrate the smooth Jacobian on each open subsegment. Every segment therefore obeys the largest row-sum bound obtained above. Conversely, at any smooth intermediate point every induced Jacobian norm is a limit of two-point Lipschitz quotients; for \(t\uparrow1\) take those points inside the intermediate region before passing to the limit. This proves global sharpness and the asserted maximizing output classes. For \(d\ge5\), choose \(t=0\) and \(u_j=1/\sqrt d\) to realize the scalar-row supremum locally; for \(d=2,3,4\), use \(|u_i|=a_d\), the other magnitudes \(\sqrt{(1-a_d^2)/(d-1)}\), and \(t\uparrow1\).

## Verification
Run the self-contained, standard-library program `verify_lorentz.py`. It directly evaluates the Euclidean cone projector and its full Jacobian, bisects the unique scalar stationary equation, compares the exact branch inequalities in dimensions \(1\) through \(32\), checks sampled spatial rows, and compares analytical Jacobians with first differences. Its deterministic run produced `VERIFIED 5461 finite assertions; max-dimensional test d=32`. These finite tests corroborate calculations but **do not prove** the universal result; the proof is analytical. In particular, sharp constants are global suprema and need not arise from a pair of distinct points attaining the quotient.

## Relationship to prior work
Kong, Tunçel, and Xiu derive the generalized Jacobian for projection onto symmetric cones, which includes Lorentz cones. This supplies broad differentiability background but does not state, or imply without additional row-sum maximization, the coordinatewise Lipschitz constants or the dimension-five change of extremizing output. Németh and Zhang study Euclidean order-isotonicity for extended Lorentz cones and convergence of associated algorithms, rather than sharp cross-norm perturbation constants. A published result on planar \(\ell_p\)-metric projection onto circular cones measures both minimization and sensitivity in \(\ell_p\), and a published ball-clipping result studies a different target (the Euclidean ball), even though its equal-weight constant coincides with the present high-dimensional scalar branch. Neither comparison supplies the exceptional spatial branches for the Lorentz cone. The familiar Hilbert-space nonexpansivity theorem concerns Euclidean sensitivity, whereas this result concerns coordinatewise sensitivity.

## Limitations
The result is finite-dimensional, unweighted, and real, and requires the standard cone aperture. It does not determine sensitivity for weighted coordinate norms, arbitrary cone apertures, non-Euclidean metric projections, or products of cones. An exhaustive historical priority claim would require a wider independent literature audit; generalized-Jacobian machinery can conceal an equivalent special case. The indicated source date is the verified first arXiv version of the motivating literature, not a claimed first-public date for the present finding.

## References
1. S. Z. Németh and G. Zhang, *Extended Lorentz cones and mixed complementarity problems*, arXiv:1405.7835v1 (first public version 2014-05-30), https://arxiv.org/abs/1405.7835 ; https://arxiv.org/html/1405.7835v2 .
2. L. Kong, L. Tunçel, and N. Xiu, *Clarke generalized Jacobian of the projection onto symmetric cones*, *Set-Valued and Variational Analysis* 17 (2009), 135–151, DOI: 10.1007/s11228-009-0113-4; lawful manuscript https://www.math.uwaterloo.ca/~ltuncel/publications/CGJ-SVVA2.pdf (dated June 26, 2008, revised April 14, 2009).
3. *Exact planar stability and nonexpansivity rigidity for \(\ell_p\) projections onto scaled Lorentz cones*, publicly released mathematical record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-planar-stability-and-nonexpansivity-rigidity-for-ell-p-pro--fbfc40872e9c .
4. *Sharp weighted coordinate sensitivity of Euclidean-ball clipping*, publicly released mathematical record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-weighted-coordinate-sensitivity-of-euclidean-ball-clipping--78696bf157c3 .
5. *Sharp Lipschitz constants and nonexpansivity for every planar \(\ell_p\) cone*, publicly released mathematical record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-lipschitz-constants-and-nonexpansivity-for-every-planar-el--8dad3ac9984d .
