# An eighth-order passive absorption window from three nonuniform lossy lattice sites

## Finding
Consider a lossless semi-infinite nearest-neighbor tight-binding lead with hopping \(J>0\), connected through hopping \(J_0>0\) to a terminal chain of exactly three sites. Neighboring terminal sites have hopping \(J\); their on-site energies are \(-i\gamma_j/2\), with \(\gamma_j>0\). Let \(r(k)\) denote the stationary reflection amplitude for an incident plane wave at \(0<k<\pi\), with incident energy \(E=-2J\cos k\). There exist strictly positive \(\gamma_1,\gamma_2,\gamma_3,J_0\) such that \(r(k)\) has a zero of **exact multiplicity four** at \(k=\pi/2\). More precisely, with \(a=\gamma_1/(2J)\), \(b=\gamma_2/(2J)\), \(c=\gamma_3/(2J)\), \(t=(J_0/J)^2\), one choice lies in the certified intervals

\[
\begin{aligned}
|a-0.436411176971509|&\le 10^{-7},\\
|b-0.825078162539108|&\le 10^{-7},\\
|c-1.940513159446698|&\le 10^{-7},\\
t&=(abc+a+c)/(bc+1)>0.
\end{aligned}
\]

At this exact algebraic parameter point,
\[
1-|r(\pi/2+\delta)|^2=1-C\delta^8+o(\delta^8), \qquad C\in(0.1036,0.1038).
\]
The order-eight *reflection probability* deficit is not a statement that all frequencies are perfectly absorbed. It is a sharp local statement: \(|r(k)|^2\) vanishes to order exactly eight near the central momentum. No uniqueness or global optimization over all passive designs is asserted.

## Assumptions and scope
The lossless lead consists of sites \(j\le0\), whose hopping is \(-J\). Terminal sites are \(1,2,3\), with hopping \(-J\) between them, link \(0\leftrightarrow1\) of strength \(-J_0\), and no site \(4\). The terminal diagonal is \(-i\gamma_j/2\); no gain, nonreciprocal hopping, or interactions occur. All positive parameters are independent of energy. Define the normalized energy \(e=-2\cos k\), the ratio \(t=(J_0/J)^2\), and
\[
g(e)=\left[e+ia-\frac{1}{e+ib-\dfrac1{e+ic}}\right]^{-1}.
\]
Because every terminal site has positive loss, the tridiagonal resolvent exists for real \(e\). The incoming and reflected amplitudes are normalized so that
\[
r(k)=-\frac{t g(-2\cos k)+e^{ik}}{t g(-2\cos k)+e^{-ik}}.
\]
This is a one-lead scattering problem: with no propagating terminal output, reflection plus absorption accounts for the incident flux.

## Proof
Set \(k=\pi/2+x\) and \(N(x)=t g(2\sin x)+i e^{ix}\); note \(i e^{ix}=e^{i(\pi/2+x)}\). Write \(g_m=g^{(m)}(0)\). The conditions \(N(0)=N'(0)=N''(0)=N'''(0)=0\) are respectively
\[
tg_0=-i,\quad 2tg_1=1,\quad 4tg_2=i,\quad 8tg_3-2tg_1=-1.
\]
The terminal continued fraction evaluates to
\[
g(0)=-i\frac{bc+1}{abc+a+c},\qquad t=\frac{abc+a+c}{bc+1}.
\]
Substitution into the other three conditions gives the real rational system
\[
F_1=2t g'(0)-1=0,\quad F_2=[4tg''(0)-i]/i=0,\quad F_3=8tg'''(0)-2tg'(0)+1=0,
\]
where \(t\) is replaced by the displayed rational expression. Each \(F_j(a,b,c)\) is rational with real coefficients and denominators nonzero throughout the positive octant.

Here is a reproducible **existence proof, not a numerical-root assumption**. Let \(z_0\) be the rational three-vector with decimal coordinates shown in the Finding, let \(B=\{z:\|z-z_0\|_\infty\le10^{-7}\}\), and choose the constant rational matrix
\[
A=\begin{pmatrix}
-3.79000745&1.04762005&0.07647238\\
-2.13141533&0.91395119&0.08720546\\
-1.51817375&0.74179254&0.10102913
\end{pmatrix}.
\]
The attached executable `certify.py` differentiates the exact rational \(F\) symbolically, then evaluates its Jacobian \(DF(B)\) and the value \(F(z_0)\) using outward-rounded interval arithmetic. It verifies
\[
\|I-A DF(B)\|_\infty<0.0002,\qquad
\|AF(z_0)\|_\infty<10^{-11}.
\]
Thus \(T(z)=z-AF(z)\) is a contraction on \(B\) and maps \(B\) strictly into itself, since \(10^{-11}+0.0002\cdot10^{-7}<10^{-7}\). Banach's theorem produces exactly one root of \(F\) in \(B\). All coordinates and \(t\) are strictly positive. The certificate bounds the fourth derivative of the numerator at this root by
\[
-15.46< N^{(4)}(0)/i<-15.45.
\]
The reflection denominator at the center is \(-2i\), hence nonzero. Taylor's theorem proves the zero has multiplicity **exactly four** and the reflection probability obeys
\[
|r(\pi/2+x)|^2=Cx^8+o(x^8),\quad C=|N^{(4)}(0)|^2/(4(4!)^2).
\]
The certified derivative interval and sharper point estimates imply \(0.1036<C<0.1038\); the leading numerical estimate is \(C\approx0.10365594\). The narrower interval is validated by the same interval certificate and direct interval evaluation of the derivative bounds.

## Verification
Run `python certify.py` with Python 3, SymPy and mpmath. The program symbolically reconstructs the continued fraction and three real stationarity equations; it certifies strict contraction inside the specified rational box and excludes a fifth-order numerator zero by an interval bound on the fourth derivative. The script prints the measured Jacobian defect and residual as further reproducibility details. The check uses interval inclusion and a mathematical contraction theorem; floating-point root searches alone are not used to infer existence. Direct numerical checks of the scattering amplitudes are supplementary and not part of the existence proof.

## Relationship to prior work
Mercado-Gutiérrez et al., arXiv:2608.06189v1, derive the momentum-resolved reflection for a three-site **uniform-loss** terminal and discuss parameter matching for strong absorption. The present result allows three independently tuned site losses and proves positive parameter existence for a **fourth-order amplitude zero**, an eighth-order reflection-probability law, with a rigorous local certificate. Longhi, *Algebraic Absorption in Non-Hermitian Photonic Lattices* (2026), derives an exact transfer-matrix scattering expression even for arbitrary sitewise losses and studies CPA and power decay, including numerical uniform three-site examples. That general transfer representation is acknowledged: it gives a method to calculate reflection for fixed parameters, but does not establish existence of this fourfold zero under strict passivity. High-order coherent perfect absorption is known in other geometries, including giant-atom devices and exceptional-point photonics; high-order reflection suppression *per se* is not claimed as new. The proposed contribution is the certified strictly passive three-site lattice design and order-eight local law.

## Limitations
This is an existence result in an exactly specified discrete scattering geometry, not a classification or proof of maximal multiplicity. The interval root is not a simple closed form. The result addresses stationary monochromatic amplitudes and narrowband wave packets, not finite-chain transients, noise sensitivity under parameter drift, or optimality under fabrication constraints. Published general transfer formulas and broader CPA design literature remain a priority risk for originality; literature searches cannot certify global novelty. Independent validation has not been performed.

## References
1. E. D. Mercado-Gutiérrez et al., *Quantum transport in a non-Hermitian 1D synthetic lattice: from quantum Zeno reflection to near-perfect absorption*, arXiv:2608.06189v1, first public 2026-08-06. https://arxiv.org/abs/2608.06189
2. S. Longhi, *Algebraic Absorption in Non-Hermitian Photonic Lattices*, Photonics **13** (2026), 574, doi:10.3390/photonics13060574, https://doi.org/10.3390/photonics13060574
3. M. Li et al., *Giant-Atom-Induced High-Order Output Zeros in a Coupled-Cavity Array*, arXiv:2609.21560, https://arxiv.org/abs/2609.21560
4. W. R. Sweeney et al., *Perfectly absorbing exceptional points and chiral absorbers*, arXiv:1807.08805, https://arxiv.org/abs/1807.08805
