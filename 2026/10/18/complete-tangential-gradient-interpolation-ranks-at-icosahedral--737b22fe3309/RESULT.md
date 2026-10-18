# Complete tangential-gradient interpolation ranks at icosahedral vertices

## Finding

Let \(V\) be the twelve vertices of a regular icosahedron inscribed in the unit sphere \(S^2\). For every integer \(\ell\ge0\), let \(\mathcal H_\ell\) denote the \((2\ell+1)\)-dimensional complex space of scalar spherical harmonics of **exactly** degree \(\ell\). For \(f\in\mathcal H_\ell\), record the intrinsic tangent gradient at every vertex. The interpolation map is
\[
T_\ell:f\longmapsto (\nabla_{S^2}f(v))_{v\in V}.
\]
Its rank is exactly
\[
(\operatorname{rank}T_0,\ldots,\operatorname{rank}T_{14})
=(0,3,5,4,9,8,12,12,9,12,12,12,12,12,9),
\]
and \(\operatorname{rank}T_\ell=12\) for every integer \(\ell\ge15\).
In particular, full interpolation occurs at degrees \(6\) and \(7\), fails again at degree \(8\), is restored at degrees \(9\) through \(13\), fails at **degree \(14\)** with precisely three independent compatibility conditions, and then holds for every degree from \(15\) onward. The rank-deficient degrees are exactly \(0,1,2,3,4,5,8,14\), with ranks as stated.

## Assumptions and scope

Set \(\varphi=(1+\sqrt5)/2\) and \(L=1+\varphi^2\). Six representatives of the antipodal vertex pairs are the following vectors divided by \(\sqrt L\):
\[
\begin{aligned}
q_1&=(0,1,\varphi),&q_2&=(0,1,-\varphi),\\
q_3&=(1,\varphi,0),&q_4&=(1,-\varphi,0),\\
q_5&=(\varphi,0,1),&q_6&=(\varphi,0,-1).
\end{aligned}
\]
Write \(x_i=q_i/\sqrt L\). For each vertex pair choose any orthonormal tangent basis at \(x_i\). The intrinsic gradients obey the antipodal parity
\[
\nabla_{S^2}f(-x_i)=(-1)^{\ell+1}\nabla_{S^2}f(x_i),
\]
where ambient tangent vectors at antipodes are compared in \(\mathbb R^3\). Thus the original twenty-four scalar tangent coordinates have an intrinsic twelve-dimensional parity-compatible target. All ranks below refer to this full original map, equivalently to the map to these twelve independent coordinates. No sampling of harmonic values is included; no degrees are mixed.

## Proof

**1. Differentiated addition kernel.** Fix an orthonormal harmonic basis \(Y_{\ell m}\) and use the addition theorem
\[
\sum_{m=-\ell}^{\ell}Y_{\ell m}(x)\overline{Y_{\ell m}(y)}=\frac{2\ell+1}{4\pi}P_\ell(x\cdot y),
\]
where \(P_\ell\) is the ordinary Legendre polynomial with \(P_\ell(1)=1\). Differentiate once in each tangent argument. After discarding the common positive scalar, the Gram matrix of the twelve gradient evaluations has entries, for tangent directions \(u\in T_{x_i}S^2\), \(v\in T_{x_j}S^2\),
\[
G_\ell[(i,u),(j,v)]=P_\ell'(t)(u\cdot v)+P_\ell''(t)(u\cdot x_j)(v\cdot x_i),\qquad t=x_i\cdot x_j.
\]
Its matrix rank is \(\operatorname{rank}T_\ell\). For \(i=j\), the block is \(d_\ell I_2\), where \(d_\ell=\ell(\ell+1)/2\); for \(i\ne j\), \(t=\pm1/\sqrt5\). This formula fixes all signs and normalizations.

**2. Exact low-degree ranks.** Use tangent directions along the coordinate axis missing from each \(q_i\), together with its cross product with \(q_i\). These two directions are perpendicular and nonzero; their normalization changes no rank. The first executable appendix constructs the preceding Gram matrix in the exact field \(\mathbb Q(\sqrt5)\), generates \(P_\ell\) by the Legendre recurrence, and performs exact Gaussian elimination for every \(0\le\ell\le14\). Its resulting ranks, in increasing degree, are
\[
(0,3,5,4,9,8,12,12,9,12,12,12,12,12,9).
\]
All rational and quadratic-field entries are represented by exact fractions; no finite-precision determinant sign test is used.

**3. Exact certificate for the intermediate degrees.** The second executable appendix reduces the same algebraic formulas modulo \(10009\), over \(\mathbb F_{10009}\), using \(\sqrt5\mapsto4070\), which satisfies \(4070^2\equiv5\pmod{10009}\). Here \(10009\) is prime and every recurrence denominator through degree \(99\) is invertible. For every integer \(15\le\ell\le99\), Gaussian elimination gives rank \(12\) over that finite field. Every denominator required to construct these matrices is invertible modulo \(10009\). Thus a nonzero twelve-by-twelve determinant after reduction **forces** that exact determinant to be nonzero in \(\mathbb Q(\sqrt5)\); this is a valid characteristic-zero nonvanishing certificate, not probabilistic numeric experimentation. The program also confirms the low-degree ranks modulo the same prime, though their exact values come from Step 2.

**4. All degrees from \(100\) onward.** Normalize tangent frames to make the diagonal blocks equal to \(d_\ell I_2\). For every off-diagonal block at \(t=\pm1/\sqrt5\), its operator norm is bounded by
\[
|P_\ell'(t)|+(1-t^2)|P_\ell''(t)|
\le 2|P_\ell'(t)|+\ell(\ell+1)|P_\ell(t)|,
\]
using the Legendre differential equation and \(2|t|<1\). Bernstein's Legendre estimate
\[
(\sin\theta)^{1/2}|P_n(\cos\theta)|<\sqrt{\frac2\pi}\,n^{-1/2}
\]
shows \(|P_n(\pm1/\sqrt5)|<9/100\) for all integers \(n\ge99\), since \(\sin\theta=2/\sqrt5\), \(\pi>3\), and \(\sqrt5<9/4\). The recurrence identity
\[
(1-t^2)P_\ell'(t)=\ell(P_{\ell-1}(t)-tP_\ell(t))
\]
then yields \(|P_\ell'(t)|<27\ell/160\) for \(\ell\ge100\). Thus any off-diagonal two-by-two block has norm less than
\[
\frac{27\ell}{80}+\frac{9\ell(\ell+1)}{100}.
\]
There are five off-diagonal blocks in each row. Their combined norm bound is therefore less than
\[
\frac{27\ell}{16}+\frac{9\ell(\ell+1)}{20}
<\frac{\ell(\ell+1)}2=d_\ell,
\qquad \ell\ge100.
\]
Strict block diagonal dominance of the Hermitian Gram matrix yields positive definiteness, so its rank is twelve for all \(\ell\ge100\). Combining Steps 2–4 completes the all-degree classification.

## Verification

Run both self-contained Python 3 programs in the same directory:

```bash
python3 icosa_exact.py
python3 icosa_checker.py
```

The first checks every degree through fourteen by exact \(\mathbb Q(\sqrt5)\) arithmetic; the second checks nonvanishing for every degree from fifteen through ninety-nine by finite-field algebra over a specified prime. Both printed the expected rank sequence and completed successfully when the mathematical claim was reviewed. The proof of the infinite tail uses the stated Bernstein inequality and strict block diagonal dominance, not extrapolation from the finite checks. The code contains no fetched data and needs only the Python standard library.

## Relationship to prior work

General formulas for differentiation of spherical harmonics and related tensor gradients are treated by Weniger [1]; the scalar addition kernel employed here is classical. Hitchin [2] analyzes degree-three harmonic cubics and the vertex geometry of regular icosahedra, not the all-degree twelve-observation tangent-gradient rank. Plattner and Simons [3] develop vector spherical harmonics and spatial concentration on the sphere; their setting is regional vector-field concentration rather than the discrete exact-degree derivative sampling map. Cohan's 1958 icosahedral symmetry-harmonic calculations [5] are particularly relevant background, including decompositions through degree fourteen; the available abstract does not determine whether an equivalent tangent-gradient rank table is contained in the inaccessible full article. The proof of the analytic tail uses the classical Legendre Bernstein estimate documented by Gautschi and Giordano [4].

Earlier scalar **value** sampling classifications on fifteen icosidodecahedral antipodal lines or ten dodecahedral axes share exceptional degrees eight and fourteen, but they concern different sampling sets and zeroth-order functionals. Their statements alone do not imply the present rank of tangential **derivatives** at six antipodal icosahedral lines. The similarities are a residual priority risk; this manuscript does not claim an independent publication-priority determination.

## Limitations

The classification is restricted to a regular icosahedron, intrinsic first derivatives, and individual spherical-harmonic degrees. It does not classify simultaneous value-and-gradient jets, arbitrary Platonic vertex configurations, vector-harmonic interpolation, or stability/condition numbers. Exact finite-field nonvanishing is a proof certificate only because the matrix entries have the explicit algebraic characteristic-zero lift specified above. The analysis does not establish independent priority over all older symmetry-harmonic tables; in particular [5] remained inaccessible in full text.

## References

[1] E. J. Weniger, *The Spherical Tensor Gradient Operator*, arXiv:math-ph/0505018, first posted 2005-05-06. https://arxiv.org/abs/math-ph/0505018

[2] N. Hitchin, *Spherical harmonics and the icosahedron*, arXiv:0706.0088, first posted 2007-06-01. https://arxiv.org/abs/0706.0088

[3] A. Plattner and F. Simons, *Spatiospectral concentration of vector fields on a sphere*, arXiv:1306.3201, first posted 2013-06-13. https://arxiv.org/abs/1306.3201

[4] W. Gautschi and C. Giordano, *Luigi Gatteschi's work on asymptotics of special functions and their zeros*, Numer. Algorithms 49 (2008), Section 5.3, Bernstein inequality (56). https://www.cs.purdue.edu/homes/wxg/selected_works/section_12/189.pdf

[5] N. V. Cohan, *The spherical harmonics with the symmetry of the icosahedral group*, Math. Proc. Cambridge Philos. Soc. 54 (1958), 28–38. https://doi.org/10.1017/S0305004100033156
