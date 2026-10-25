# One-area Fourier-ambiguity ovals and their collapse under Gaussian amplitude imbalance

## Finding

For a real two-Gaussian pulse with equal component amplitudes, every connected component of its real delay–Doppler ambiguity zero set is a smooth strictly convex closed oval, and **the area enclosed by each oval is exactly one** in delay–cycles-frequency coordinates, irrespective of component separation and Gaussian width. Unequal positive amplitudes replace each oval by precisely two isolated, regular complex zeros of opposite local topological index. The theorem below gives the entire zero set in both cases, not merely a small-displacement approximation.

Fix \(a>0\), \(\sigma>0\), and \(r>0\). Put
\[
g(t)=\exp\!\left(-\frac{(t-a)^2}{2\sigma^2}\right)+r\exp\!\left(-\frac{(t+a)^2}{2\sigma^2}\right),
\quad A(T,\nu)=\int_{\mathbb R}g(t+T/2)g(t-T/2)e^{-2\pi i\nu t}\,dt.
\]
With \(c=e^{-a^2/\sigma^2}\in(0,1)\), \(u=aT/\sigma^2\), and \(\phi=2\pi a\nu\), the exact identity is
\[
A(T,\nu)=\sqrt\pi\,\sigma\,e^{-T^2/(4\sigma^2)-\pi^2\sigma^2\nu^2}
\left(e^{-i\phi}+r^2e^{i\phi}+2rc\cosh u\right).
\tag{1}
\]

**Balanced case \(r=1\).** For every \(k\in\mathbb Z\), let \(\nu_k=(2k+1)/(2a)\), \(U=\operatorname{arcosh}(1/c)\), and \(v=2\pi a(\nu-\nu_k)\). The complete real zero set is the disjoint union of the curves
\[
\Gamma_k=\left\{(T,\nu): |u|\le U,\quad
v=\pm\arccos(c\cosh u)\right\}.
\tag{2}
\]
Each \(\Gamma_k\) is an analytic simple closed strictly convex curve, and its bounded interior \(\Omega_k\) satisfies
\[
\boxed{\ \operatorname{area}_{dT\,d\nu}(\Omega_k)=1\quad\text{for every }k\in\mathbb Z.\ }
\tag{3}
\]
No other real zeros exist.

**Imbalanced case \(r\ne1\).** The complete zero set consists of the isolated points
\[
\boxed{\quad
\nu=\frac{2k+1}{2a},\qquad
T=\pm\frac{\sigma^2}{a}\operatorname{arcosh}\!\left(
\frac{e^{a^2/\sigma^2}}2(r+r^{-1})\right),
\quad k\in\mathbb Z.
\quad}
\tag{4}
\]
Every zero is regular as a map \((T,\nu)\mapsto(\operatorname{Re}A,\operatorname{Im}A)\) and has local winding index \(+1\) or \(-1\). The two zeros on the same Doppler line have opposite indices. In the limit \(r\to1\) they approach the two extreme-delay tips of the corresponding balanced oval.

## Assumptions and scope

The Fourier phase uses **cycles per unit time**: the kernel is \(e^{-2\pi i\nu t}\), not \(e^{-i\nu t}\). Delay \(T\) and frequency \(\nu\) are both real, and area means Euclidean Lebesgue area in the \((T,\nu)\)-plane. With angular frequency \(\omega=2\pi\nu\), the same enclosed area is \(2\pi\), not one. The Gaussian components have the same variance, zero relative phase and strictly positive amplitudes. Multiplication of \(g\) by any nonzero constant only rescales the ambiguity function and does not change its zeros.

## Proof

**1. Gaussian identity.** Expand \(g(t+T/2)g(t-T/2)\) into its four pairs of displaced Gaussians. Completing the square in each term and using
\[
\int_{\mathbb R}e^{-t^2/\sigma^2}e^{-2\pi i\nu t}\,dt
=\sqrt\pi\,\sigma e^{-\pi^2\sigma^2\nu^2}
\]
yields the same strictly positive prefactor in all four terms. The two like-center terms give \(e^{-i\phi}+r^2e^{i\phi}\); the cross-center terms give \(2rc\cosh u\). This proves (1), including at zero frequency and zero delay. There is no unproved interchange of an infinite sum with an integral.

**2. Complete balanced zero classification.** At \(r=1\), the bracket in (1) is \(2(\cos\phi+c\cosh u)\). Since \(c\cosh u>0\), a zero requires \(\cos\phi<0\). Write \(\phi=(2k+1)\pi+v\). Then \(\cos v=c\cosh u\). In particular \(c\cosh u\le1\), equivalent to \(|u|\le U\), and \(|v|\le\arccos c<\pi/2\). This establishes (2) and exhausts all real zeros. Because distinct odd multiples of \(\pi\) are separated by \(2\pi\) in \(\phi\), these ovals are pairwise disjoint.

Set \(b(u)=\arccos(c\cosh u)\) on \((-U,U)\). Differentiation gives
\[
b''(u)=-\frac{c\cosh u}{\sqrt{1-c^2\cosh^2u}}
-\frac{c^3\cosh u\sinh^2u}{(1-c^2\cosh^2u)^{3/2}}<0.
\]
Thus the region \(\{|u|\le U,\ |v|\le b(u)\}\) is strictly convex. To check the two tips and analyticity rather than relying on a graph with a vertical tangent, use the implicit equation \(\cos v-c\cosh u=0\). Its gradient \((-c\sinh u,-\sin v)\) is never zero on this level set: the only simultaneous candidate \((0,0)\) would require \(c=1\), excluded by \(a>0\). The oval is therefore a regular analytic Jordan curve. Strict convexity also holds at its tips: on the level set, the Hessian of \(\cos v-c\cosh u\) is exactly \(-c\cosh u\) times the identity matrix, so its normal curvature is nonzero at every boundary point.

**3. Exact area.** In \((u,v)\)-coordinates the enclosed area is \(4I(c)\), where
\[
I(c)=\int_0^{\operatorname{arcosh}(1/c)}\arccos(c\cosh u)\,du.
\]
The integrand vanishes at the moving upper endpoint; differentiation under the integral is permitted because the square-root endpoint singularity is integrable for every \(0<c<1\). Thus
\[
I'(c)=-\int_0^{\operatorname{arcosh}(1/c)}
\frac{\cosh u}{\sqrt{1-c^2\cosh^2u}}\,du
=-\frac1c\int_0^{\sqrt{1-c^2}}
\frac{dy}{\sqrt{1-c^2-y^2}}=-\frac\pi{2c},
\]
where \(y=c\sinh u\). Since \(I(c)\to0\) as \(c\uparrow1\), integration gives \(I(c)=\frac\pi2\log(1/c)\). Therefore the \((u,v)\)-area is \(2\pi\log(1/c)=2\pi a^2/\sigma^2\). As \(dT\,d\nu=(\sigma^2/(2\pi a^2))\,du\,dv\), the product is exactly one. This proves (3) without a numerical area approximation.

**4. Complete imbalanced zeros and indices.** For any \(r>0\), the bracket of (1) has
\[
R=(1+r^2)\cos\phi+2rc\cosh u,
\qquad H=(r^2-1)\sin\phi.
\]
For \(r\ne1\), \(H=0\) forces \(\phi\in\pi\mathbb Z\). At even multiples of \(\pi\), \(R>0\); at odd multiples, \(R=0\) is equivalent to
\[
\cosh u=\frac{r+r^{-1}}{2c}>1.
\]
There are precisely two real solutions, as displayed in (4), and no other zeros. In the coordinate orientation \((T,\nu)\), the Jacobian determinant for \((R,H)\) at any zero is
\[
J=-\frac{4\pi rca^2}{\sigma^2}(r^2-1)\sinh u\ne0.
\]
The positive prefactor of (1) multiplies this determinant by its positive square at a zero; therefore the zeros are regular and their local winding indices are \(\operatorname{sgn}J\). The two signs of \(u\) give opposite indices. Finally, as \(r\to1\), \((r+r^{-1})/2\to1\), so the solutions tend to \(u=\pm U\), the two balanced-oval tips. All quantifiers and boundary cases covered by the stated strictly positive parameter ranges have been included.

## Verification

The standalone \(checker.py\) can be run with Python, NumPy and SciPy. It independently evaluates eight ambiguity integrals by adaptive real-line quadrature and compares them with (1), numerically integrates seven balanced oval areas, verifies 24 isolated-zero locations using direct quadrature and the exact Jacobian signs, and tests nearby nonzeros. It exits successfully and produces the supplied \(checker_output.txt\). The largest observed absolute discrepancy in the eight generic integrals was \(1.043\times10^{-15}\); the largest discrepancy from unit area was \(3.331\times10^{-15}\). These are finite numerical consistency checks only; the all-parameter and all-index conclusions follow from the analytical proof above.

## Relationship to prior work

Zambrano and Ozorio de Almeida, *Blind spots between quantum states* (arXiv:0905.1900, first posted 2009-05-12), study zeros of coherent-state translation overlaps; their Sections 3–4 give the connection to the chord function, parity symmetry, and the coherent-state decomposition. They emphasize the **short-displacement** regime and state that unequal coefficients eliminate cat-state blind spots. The present full-plane Gaussian formula resolves the distinction in scope: for positive unequal coefficients it gives exact but remote nonzero-delay zeros at (4), which are exponentially suppressed in the large-separation regime considered in the earlier approximation. The paper does not give the enclosed-area identity (3) or the complete full-plane two-parameter classification. That textual difference merits specialist review rather than an assumption that the prior article was examining identical global quantifiers.

Zambrano and Ozorio de Almeida, *Semiclassical theory for small displacements* (arXiv:1003.1877, 2010), focuses on local/semiclassical chord behavior, not this exact unit-area law. Gröchenig, Jaming and Malinnikova, *Zeros of the Wigner distribution and the short-time Fourier transform* (arXiv:1811.03937; subsequently published 2019), define the same ambiguity normalization and study nonvanishing, including individual Gaussian pairs, but their inspected analysis does not provide the two-Gaussian equal/unequal amplitude geometric phase transition or exact area identity. The Gaussian integral and phase-space conventions are standard; novelty is asserted only for the complete combined classification and the parameter-independent oval area, subject to independent literature review.

## Limitations

The theorem concerns exactly two **real, equal-width, equal-phase** Gaussian packets with strictly positive real relative amplitude. It does not treat unequal widths, complex amplitude phases, Gaussian chirps or general coherent-state multiplets. The invariant area is in delay–cycles-frequency coordinates; changing frequency units changes its numerical value. For unequal amplitudes, the isolated zeros often lie in exponentially small tails, so this is an exact mathematical statement, not a claim of readily observable radar nulls. A previously unindexed analytic treatment of two-coherent-state ambiguity zeros may contain some of these consequences; searches do not certify publication priority. No external or independent proof audit has been performed.

## References

1. E. Zambrano and A. M. Ozorio de Almeida, *Blind spots between quantum states*, arXiv:0905.1900 (initial version 2009-05-12), especially Sections 2–4 and the discussion of coefficient symmetry. https://arxiv.org/pdf/0905.1900
2. E. Zambrano and A. M. Ozorio de Almeida, *Semiclassical theory for small displacements*, arXiv:1003.1877 (initial version 2010-03-09). https://arxiv.org/pdf/1003.1877
3. K. Gröchenig, P. Jaming and E. Malinnikova, *Zeros of the Wigner distribution and the short-time Fourier transform*, arXiv:1811.03937; *Rev. Mat. Complut.* 33 (2020), 723–744. https://doi.org/10.1007/s13163-019-00335-w
