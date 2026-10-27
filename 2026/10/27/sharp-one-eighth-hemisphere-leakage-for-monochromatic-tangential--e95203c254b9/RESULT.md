# Sharp one-eighth hemisphere leakage for monochromatic tangential spherical harmonics

## Finding

Let \(H=\{(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta):0\le\theta<\pi/2\}\subset S^2\).
For each integer \(\ell\ge1\), consider the complex tangential vector-harmonic space
\[
\mathcal T_\ell=
\operatorname{span}_{\mathbb C}\left\{
\frac{\nabla_SY_{\ell m}}{\sqrt{\ell(\ell+1)}},
\frac{J\nabla_SY_{\ell m}}{\sqrt{\ell(\ell+1)}}:
-\ell\le m\le\ell
\right\},
\]
where \(Y_{\ell m}\) are ordinary surface-area \(L^2\)-orthonormal scalar spherical harmonics and \(J\) rotates tangent vectors by \(90^\circ\) with the outward orientation. Let \(C_\ell\) be hemisphere energy concentration (compression of multiplication by \(\mathbf1_H\) to \(\mathcal T_\ell\)).

**Sharp all-degree claim.** Every \(F\in\mathcal T_\ell\) satisfies
\[
\frac18\|F\|_{L^2(S^2)}^2
\le \|F\|_{L^2(H)}^2
\le\frac78\|F\|_{L^2(S^2)}^2.
\]
The constants are optimal simultaneously across all \(\ell\ge1\). Either equality can occur only for \(\ell=1\), in the two-real-dimensional eigenspace of the corresponding polarization and orders \(\lvert m\rvert=1\). In particular, every nonzero monochromatic tangential field leaves at least \(1/8\) of its energy outside a hemisphere.

**Exact degree-by-degree extremum.** Writing \(c_j=4^{-j}\binom{2j}{j}\), the largest and smallest concentration eigenvalues in degree \(\ell\) are
\[
\lambda^\pm_\ell=\frac12\pm
\frac{2\ell+1}{2(\ell+1)}c_\ell.
\]
The maximum decreases strictly with \(\ell\), and
\[
\lambda^+_\ell=\frac12+\frac{1+o(1)}{\sqrt{\pi\ell}}
\quad(\ell\to\infty).
\]
The optimizing azimuthal orders in each fixed degree are uniquely \(\lvert m\rvert=\ell\).

**Complete spectrum.** Each order \(m\) gives a two-dimensional poloidal-toroidal block with eigenvalues
\[
\frac12\pm\mu_{\ell,\lvert m\rvert},\qquad
\mu_{\ell,m}=
\begin{cases}
\displaystyle\frac{m(2\ell+1)}{2\ell(\ell+1)}
c_{(\ell+m)/2}c_{(\ell-m)/2},&
m\ge1,\ \ell+m\text{ even},\\[2mm]
0,&m=0\ \text{or }\ell+m\text{ odd}.
\end{cases}
\]
Thus each \(m>0\) positive gap has order-pair multiplicity two when counted with its negative order; all remaining block eigenvalues equal \(1/2\). The complex dimension is \(2(2\ell+1)\).

## Assumptions and scope

The surface measure is the ordinary area element \(d\omega=\sin\theta\,d\theta\,d\phi\); the scalar harmonics satisfy \(\int_{S^2}|Y_{\ell m}|^2\,d\omega=1\).
The polarization \(\nabla_S\) is the intrinsic gradient and \(J\) the quarter-turn of the tangent plane. The inner product of complex vector fields is \(F\cdot\overline{G}\), integrated against \(d\omega\).

All results concern the **single exact-degree space** \(\mathcal T_\ell\), not sums over several degrees and not the normal/radial vector-harmonic sector. Any fixed hemisphere is equivalent to \(H\) by rotation. The real-valued subspace obeys the same bounds and achieves them. The equality eigenspaces have complex dimension two, and real dimension two when restricted to real vector fields.

## Proof

**1. Orthogonal basis and hemisphere blocks.** Put
\[
E_{\ell m}=\nabla_SY_{\ell m}/\sqrt{\ell(\ell+1)},\qquad
B_{\ell m}=J\nabla_SY_{\ell m}/\sqrt{\ell(\ell+1)}.
\]
By integration by parts and orthogonality, \(\{E_{\ell m},B_{\ell m}\}_{m=-\ell}^{\ell}\) is a complete orthonormal basis of \(\mathcal T_\ell\). The scalar phases are \(Y_{\ell m}(\theta,\phi)=f_{\ell m}(\theta)e^{im\phi}\), with \(f_{\ell m}\) real up to the conventional constant phase.

Because longitude integration kills cross-order terms, \(C_\ell\) is a direct sum over \(m\) of \(2\times2\) blocks. Reflection \(\theta\mapsto\pi-\theta\) preserves \(|\nabla_SY_{\ell m}|^2\), so each diagonal hemispherical energy is exactly \(1/2\).

**2. Cross-polarization boundary identity.** In the frame \((e_\theta,e_\phi)\),
\[
\nabla_SY=(\partial_\theta Y)e_\theta+
\frac{\partial_\phi Y}{\sin\theta}e_\phi,\qquad
J(e_\theta)=e_\phi,\quad J(e_\phi)=-e_\theta.
\]
For \(m>0\), direct multiplication and integration yield
\[
\int_H E_{\ell m}\cdot\overline{B_{\ell m}}\,d\omega
=\frac{2\pi i m}{\ell(\ell+1)}
\bigl(f_{\ell m}(\pi/2)^2-f_{\ell m}(0)^2\bigr)
=\frac{2\pi i m}{\ell(\ell+1)}f_{\ell m}(\pi/2)^2,
\]
since \(Y_{\ell m}\) vanishes at the north pole for \(m>0\).
The sign reverses for \(m<0\), and the cross term vanishes for \(m=0\).
Hence each block has diagonal \(1/2\) and purely imaginary off-diagonal entries with absolute value
\(\mu_{\ell,m}=2\pi m|Y_{\ell m}(\pi/2,0)|^2/[\ell(\ell+1)]\).
Its eigenvalues are \(1/2\pm\mu_{\ell,m}\). This identity and the block construction are also compatible with the general cap matrices in Plattner–Simons (2014, equations (69)–(76)); their existence is not claimed as new here.

**3. Exact central-binomial formula.** With Condon–Shortley associated Legendre functions,
\[
Y_{\ell m}=
\sqrt{\frac{2\ell+1}{4\pi}
\frac{(\ell-m)!}{(\ell+m)!}}\,
P_\ell^m(\cos\theta)e^{im\phi}.
\]
If \(\ell+m\) is odd then \(P_\ell^m(0)=0\).
Otherwise, writing \(a=(\ell+m)/2\), \(b=(\ell-m)/2\),
\[
P_\ell^m(0)=(-1)^a\frac{(2a-1)!!}{(2b)!!},
\qquad
2\pi|Y_{\ell m}(\pi/2,0)|^2
=\frac{2\ell+1}{2}c_ac_b.
\]
Substitution gives the claimed rational spectrum. These formulas include all endpoint cases \(m=0\) and \(m=\ell\).

**4. Sharp azimuthal ordering.** Fix \(\ell\). Along the nonzero-parity orders \(m=\ell,\ell-2,\ldots\), replacing \(m\ge3\) by \(m-2\) means replacing \((a,b)\) by \((a-1,b+1)\). The product ratio is
\[
\frac{c_{a-1}c_{b+1}}{c_ac_b}
=\frac{2a(2b+1)}{(2a-1)(2b+2)}
=1-\frac{2(m-1)}{(2a-1)(2b+2)}<1.
\]
The additional factor \(m-2\) in \(\mu_{\ell,m-2}\) is smaller than \(m\); when \(m=2\), the next value is zero. Wrong-parity orders and \(m=0\) also have zero gap. Thus \(\lvert m\rvert=\ell\) is the unique maximizing absolute azimuthal order.

**5. All-degree sharpness and equality.** For \(\lvert m\rvert=\ell\), \(a=\ell,b=0\), hence
\[
M_\ell=\max_m\mu_{\ell,\lvert m\rvert}
=\frac{2\ell+1}{2(\ell+1)}c_\ell.
\]
Using \(c_{\ell+1}/c_\ell=(2\ell+1)/(2\ell+2)\) gives
\[
\frac{M_{\ell+1}}{M_\ell}
=\frac{2\ell+3}{2\ell+4}<1,\qquad M_1=\frac38.
\]
Therefore the entire concentration spectrum lies in \([1/8,7/8]\); equality requires \(\ell=1\) and \(\lvert m\rvert=1\), with the eigenpolarization selected accordingly. More explicitly, for \(m\in\{-1,1\}\), the normalized upper extremizers are
\[
F^{+}_{m}=(E_{1m}+i\,\operatorname{sgn}(m)B_{1m})/\sqrt2,
\]
and replacing \(+i\) by \(-i\) gives the lower extremizers. Taking conjugate-compatible combinations of the \(m=\pm1\) doublet produces real-valued extremizers. Finally \(c_\ell\sim(\pi\ell)^{-1/2}\) by Stirling's formula, proving the displayed asymptotic.

## Verification

The standalone `checker.py` uses exact integer central-binomial coefficients and rational arithmetic to verify the spectral identities and order/degree inequalities in the first ten degrees. Independently, it evaluates normalized associated Legendre functions at the equator and numerically integrates the cross-polarization term through a separate Simpson quadrature of \(f_{\ell m}\partial_\theta f_{\ell m}\). It checks 30 nonzero modes, with maximum equatorial discrepancy \(5.551\times10^{-17}\) and maximum quadrature discrepancy \(1.196\times10^{-13}\), as recorded in `checker_output.txt`. Run `python checker.py` with Python 3 and no third-party dependencies. These finite checks do not certify the all-degree result; steps 1–5 are the proof.

## Relationship to prior work

Plattner and Simons, *Spatiospectral concentration of vector fields on a sphere* (arXiv:1306.3201v1; first public 2013-06-13), derive tangential vector Slepian concentration matrices for arbitrary spherical caps. In particular, their equations (69)–(76), inspected in the openly readable full-text presentation, imply the **unoptimized per-order** hemispherical block formula after specialization. The present asserted advance is **not** that block formula: it is the exact azimuthal ordering for each degree, the sharp all-degree \(1/8\) leakage constant, strict monotonicity in the degree, and classification of the attaining vector fields.

Jahn and Bokor, *Revisiting the concentration problem of vector fields within a spherical cap: a commuting differential operator solution* (arXiv:1302.5261v1; first public 2013-02-21), reduce general tangential vector cap concentration to a scalar method. Their complete text was not obtained during this assessment, and the possible presence of an equivalent globally optimized special case is a residual priority risk. Michel, Plattner, and Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator* (arXiv:2103.14650; 2021), give general spin-weighted cap matrices but do not state the sharp all-degree monochromatic constant in the inspected sections.

The general Slepian eigenproblem and Legendre boundary formulas are prior methods, not claims of new theory. The originality claim is limited to their optimized, sharp combination across **all single degrees**, with the stated historical qualification.

## Limitations

The estimate fails as a uniform bound when arbitrary mixtures of many spherical-harmonic degrees are allowed: such spaces can approximate highly hemisphere-localized fields. No general cap-aperture bound, vector-tensor extension, or other surface is asserted. A full-text historical comparison with Jahn–Bokor and independent specialist priority review remain outstanding. Numerical quadrature is only a finite cross-check and not an infinite proof.

## References

1. K. Jahn, N. Bokor, *Revisiting the concentration problem of vector fields within a spherical cap: a commuting differential operator solution*, arXiv:1302.5261v1 (2013-02-21), https://arxiv.org/abs/1302.5261.
2. A. Plattner, F. J. Simons, *Spatiospectral concentration of vector fields on a sphere*, arXiv:1306.3201v1 (2013-06-13), https://arxiv.org/abs/1306.3201; Appl. Comput. Harmon. Anal. 36 (2014), 1–22, particularly equations (69)–(76).
3. V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (2021-03-26), https://arxiv.org/abs/2103.14650.
