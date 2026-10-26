# A Fibonacci staircase and sharp fourth-root radius barrier for positive lattice diffusion stencils

## Finding

Let \(s=(\sqrt5-1)/2\) and consider the positive-definite planar diffusion family
\[
 A_\varepsilon=\begin{pmatrix}1+\varepsilon&s\\s&s^2+\varepsilon\end{pmatrix},\qquad\varepsilon>0.
\]
For a stencil of integer grid offsets whose coordinate magnitudes do not exceed an integer \(R\ge1\), exact second-moment consistency with a **nonnegative symmetric, translation-invariant** discrete diffusion operator is possible if and only if \(\varepsilon\ge\varepsilon_R\), where the threshold is constant on successive Fibonacci intervals. With \(F_0=0,F_1=1,F_{n+2}=F_{n+1}+F_n\), for the unique \(n\ge2\) with \(F_n\le R<F_{n+1}\),
\[
 \boxed{\varepsilon_R=\frac{s^{2n-1}}{F_{n-1}(F_n+F_{n-2})}.}
\]
The sharp scaled accumulation endpoints are distinct:
\[
 \boxed{\liminf_{R\to\infty}R^4\varepsilon_R=\frac1{5s^2(1+s^2)}},\qquad
 \boxed{\limsup_{R\to\infty}R^4\varepsilon_R=\frac1{5s^6(1+s^2)}}.
\]
Consequently, the smallest admissible stencil radius at anisotropy noise \(\varepsilon\downarrow0\) grows on the order \(\varepsilon^{-1/4}\), but the fourth-power normalized thresholds have no single asymptotic constant. The exact plateau effect is a property of lattice-aligned nonnegative moment matching, not a restriction on off-grid or interpolatory probabilistic schemes.

## Assumptions and scope

For \(R\in\mathbb N\), let \(\mathcal Z_R=\{(a,b)\in\mathbb Z^2\setminus\{(0,0)\}:\max(|a|,|b|)\le R\}\). Select one representative \(\mathcal Z_R^+\) of every opposite pair. A legal stencil has finite nonnegative weights \(w_z\ge0\) and
\[
 L_hu(x)=\frac{1}{2h^2}\sum_{z\in\mathcal Z_R^+}w_z\,[u(x+hz)+u(x-hz)-2u(x)],\qquad h>0.
\]
The Taylor leading term is \(\frac12\operatorname{tr}(A_\varepsilon D^2u)\) precisely when \(\sum_z w_z zz^\mathsf T=A_\varepsilon\). This is the exact moment-matching notion of consistency used here; no boundary treatment, truncation-error optimization, or time-integration stability is asserted. We allow zero weights. We constrain **both absolute lattice coordinates** by \(R\), and all shifts land on the same Cartesian grid.

## Proof

**1. Farey neighbors.** Let \(\ell_R\) and \(r_R\) be respectively the largest rational below \(s\) and the smallest rational above \(s\), among reduced fractions \(p/q\) with \(0\le p\le q\le R\). The Fibonacci ratios \(F_{n-2}/F_{n-1}\) and \(F_{n-1}/F_n\) straddle \(s\), because
\[
 F_{k-1}-sF_k=(-1)^k s^k,
\]
which follows by induction from \(s^2+s=1\). Consecutive Fibonacci ratios are Farey adjacent, since their numerator-denominator cross-determinant has absolute value one. Any rational strictly between them must have reduced denominator at least the sum of their denominators, \(F_{n-1}+F_n=F_{n+1}\). Thus, whenever \(F_n\le R<F_{n+1}\),
\[
 \{\ell_R,r_R\}=\{F_{n-2}/F_{n-1},F_{n-1}/F_n\}.
\]
This also covers \(R=1\), by \(n=2\).

**2. Exact convex-cone separation.** For every \(z=(a,b)\in\mathcal Z_R\),
\[
 (b-\ell_Ra)(b-r_Ra)\ge0.
\]
Indeed, if \(a\ne0\) and the product were negative, the reduced slope \(b/a\) would lie strictly between the two adjacent fractions and have a denominator at most \(R\); if \(a=0\), the product is \(b^2\). A legal nonnegative decomposition of \(A_\varepsilon\) therefore forces
\[
 0\le (A_\varepsilon)_{22}-(\ell_R+r_R)(A_\varepsilon)_{12}+\ell_Rr_R(A_\varepsilon)_{11}
 =\varepsilon(1+\ell_Rr_R)-(s-\ell_R)(r_R-s).
\]
It follows that
\[
 \varepsilon\ge\widehat\varepsilon_R:=\frac{(s-\ell_R)(r_R-s)}{1+\ell_Rr_R}.
\]
To prove sufficiency at equality, set \(t=s/(1+\widehat\varepsilon_R)\). The elementary inequality \(\ell_R<t<r_R\) holds (the left one follows from \(\ell_R(r_R-s)<1+\ell_Rr_R\); the right from \(t<s<r_R\)). Let \(u=(q_\ell,p_\ell)\), \(v=(q_r,p_r)\) be the primitive lattice directions of slopes \(\ell_R=p_\ell/q_\ell\) and \(r_R=p_r/q_r\). These lie in \(\mathcal Z_R\). Put
\[
 \theta=\frac{r_R-t}{r_R-\ell_R},\quad
 w_u=\frac{(1+\widehat\varepsilon_R)\theta}{q_\ell^2},\quad
 w_v=\frac{(1+\widehat\varepsilon_R)(1-\theta)}{q_r^2}.
\]
Both weights are positive. Direct multiplication matches the first row of \(A_{\widehat\varepsilon_R}\); its second diagonal entry matches because both side vectors make the separating functional zero. Hence \(A_{\widehat\varepsilon_R}=w_uuu^\mathsf T+w_vvv^\mathsf T\). For \(\varepsilon>\widehat\varepsilon_R\), add \(\varepsilon-\widehat\varepsilon_R\) times each of the two axis-direction rank-one matrices. This proves necessity and sufficiency for every \(R\ge1\) and \(\varepsilon>0\).

**3. Explicit Fibonacci threshold.** The two distances from \(s\) to the adjacent ratios are \(s^{n-1}/F_{n-1}\) and \(s^n/F_n\), in either order. The rational denominator \(1+\ell_Rr_R\) is \((F_{n-1}F_n+F_{n-2}F_{n-1})/(F_{n-1}F_n)\). Substitution yields precisely
\[
 \widehat\varepsilon_R=\frac{s^{2n-1}}{F_{n-1}(F_n+F_{n-2})}=\varepsilon_R.
\]
No intermediate radius can change the neighbors, so the threshold is constant throughout each half-open Fibonacci interval.

**4. Sharp asymptotic endpoints.** Binet's formula gives \(F_n\sim s^{-n}/\sqrt5\) as \(n\to\infty\). Consequently,
\[
 F_n^4\varepsilon_{F_n}\longrightarrow c_-:=\frac1{5s^2(1+s^2)}.
\]
Inside \(F_n\le R<F_{n+1}\), \(R^4\varepsilon_R\) strictly increases with \(R\); at \(R=F_{n+1}-1\), it tends instead to \(c_+:=c_-/s^4\). As the Fibonacci intervals partition all sufficiently large integers, these are the global liminf and limsup. Both are positive and finite, establishing the \(\varepsilon^{-1/4}\) order for the least permitted radius. The eigenvalues of \(A_\varepsilon\) are \(1+s^2+\varepsilon\) and \(\varepsilon\), so this is also a fourth-root condition-number barrier as the condition number diverges.

## Verification

The bundled `CHECK.py` is executable with Python 3 and SymPy, and `CHECK_OUTPUT.txt` records its actual output. It independently enumerates all rational slopes and all allowed integer directions for every \(1\le R\le89\), verifies the Fibonacci bracketing and exact threshold in \(\mathbb Q(\sqrt5)\), constructs the boundary stencil and matches all covariance entries, and verifies the separating inequality on every enumerated direction. Over 970,000 exact algebraic or integer assertions passed. Numeric approximations are provided only as diagnostics. The proof above, not finite enumeration, establishes the assertions for unbounded \(R\).

## Relationship to prior work

The anisotropic-diffusion and positivity-preserving discretization literature establishes the necessity of wider stencils and supplies existence and construction methods; see Ngo--Huang (2015), Fehrenbach--Mirebeau (2013), Bonnans--Bonnet--Mirebeau (2021, 2025), and Xu--Li--Yue (2026). In particular the 2021 work reports *optimally compact* two-dimensional stencils, so a general pointwise minimal-stencil characterization is not claimed here. The specific assertion is the exact golden-slope Fibonacci plateau sequence and its distinct fourth-power liminf and limsup under the stated coordinatewise lattice-radius constraint. An optimal-stencil algorithm or qualitative radius bound does not by itself state these arithmetic asymptotics. The 2026 probabilistic method permits off-grid or interpolatory constructions, outside the present lattice-alignment restriction.

## Limitations

The calculation is for a fixed, homogeneous, planar covariance family and a symmetric positive linear stencil with grid-aligned integer offsets. It neither prohibits non-grid-aligned positive schemes nor asserts boundary-value convergence rates, optimal computational complexity, or general coefficient-dependent stencil bounds. While multiple closely related sources were inspected, an equivalent specialized Fibonacci asymptotic might be implicit in older lattice-reduction literature; the full 2021 and 2025 Bonnans--Bonnet--Mirebeau texts were not accessible through the attempted lawful sources. Independent scientific priority verification is outstanding.

## References

- H. Xu, K. Li, X. Yue, *A Non-compact Positivity-Preserving Numerical Scheme for Elliptic Differential Equations Based on Mathematical Expectation* (2026), arXiv:2604.02797, https://arxiv.org/abs/2604.02797 .
- C. Ngo and W. Huang, *Monotone finite difference schemes for anisotropic diffusion problems via nonnegative directional splittings* (2015), arXiv:1503.08177, https://arxiv.org/abs/1503.08177 .
- J. F. Bonnans, G. Bonnet, J.-M. Mirebeau, *Second order monotone finite differences discretization of linear anisotropic differential operators* (2021), doi:10.1090/mcom/3671 .
- J. Fehrenbach and J.-M. Mirebeau, *Sparse Non-Negative Stencils for Anisotropic Diffusion* (2013), arXiv:1301.3925 .
- J. F. Bonnans, G. Bonnet, J.-M. Mirebeau, *Monotone Discretization of Anisotropic Differential Operators Using Voronoi's First Reduction* (2025), doi:10.1007/s00365-023-09672-y .
