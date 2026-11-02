# Exact equilibrium census and sharp pinning fold on a three-site cubic Nagumo ring

## Finding
Consider three cyclic sites with continuous-time nearest-neighbor coupling
\[
\dot x_i=x_i-x_i^3+d(x_{i-1}-2x_i+x_{i+1}),\qquad i\in\mathbb Z/3\mathbb Z,\quad d\ge0.
\]
There is exactly one critical coupling \(d_*\in(0,1/3)\) satisfying
\[
108d_*^4-36d_*^2+12d_*-1=0,\qquad d_*\approx0.1350681582114225.
\]
The **complete real equilibrium census**, including unstable equilibria, is
\[
\begin{array}{c|ccccc}
\text{coupling}&d=0&0<d<d_*&d=d_*&d_*<d<1/3&d\ge1/3\\\hline
\text{distinct equilibria}&27&27&21&15&3\\
\text{exponentially attracting equilibria}&8&8&2&2&2
\end{array}.
\]
At \(d=d_*\), six distinct nonhomogeneous equilibria are ordinary saddle-node folds and the six pinned nonhomogeneous sinks have just disappeared. For \(d\ge1/3\), only the three homogeneous equilibria remain. At \(d=0\), the count of eight sinks follows from independent scalar cubic components.

## Assumptions and scope
All coordinates are real; site indices are cyclic modulo three. A stationary state is a real \(x\in\mathbb R^3\) with all three right-hand sides zero, and distinct states are counted with their site labels. Local exponential attraction means every eigenvalue of the real symmetric Jacobian is strictly negative. The parameter \(d\) is the diffusion coefficient in the displayed, **normalized** cubic \(x-x^3\), not the coefficient in \(u(1-u)(u-1/2)\). Under \(x=2u-1\), with a positive rescaling of physical time, the coefficients are related by \(d=4d_{\mathrm{Nagumo}}\) for the latter cubic.

## Proof
**1. Every equilibrium falls into one of three exhaustive forms.** Write \(S=x_0+x_1+x_2\). Since the two neighbors of a site are exactly the other two sites, the equilibrium equations become
\[
x_i^3-(1-3d)x_i-dS=0\qquad (i=0,1,2).
\]
Consequently, the three coordinates are roots of **the same depressed cubic** \(p(t)=t^3-(1-3d)t-dS\). Either they are all equal; all distinct; or exactly two equal.

All-equal coordinates are \((h,h,h)\) with \(h\in\{-1,0,1\}\). Their Jacobian spectra are \(\{1-3h^2,1-3h^2-3d,1-3h^2-3d\}\). Both outer homogeneous equilibria are sinks at every \(d\ge0\), whereas the homogeneous zero is unstable since its uniform eigenvalue equals \(1\).

If all three coordinates are distinct, they are the three real roots of \(p\), hence their sum is zero, forcing \(S=0\) and
\[
\{x_0,x_1,x_2\}=\{-\sqrt{1-3d},0,\sqrt{1-3d}\}.
\]
These give six labeled equilibria exactly when \(0\le d<1/3\), with genuine distinctness only for \(d<1/3\). For \(d>0\), at such a state the Jacobian has the eigenvector corresponding to exchanging the outer amplitudes, with eigenvalue \(-2+6d\), while its complementary two-dimensional block has determinant \(-2(1-3d)^2<0\). All six are therefore saddles throughout \(0<d<1/3\). At \(d=1/3\) all six collapse into the homogeneous origin.

**2. The repeated-coordinate branches admit an exact rational parametrization.** After a permutation let \((x_0,x_1,x_2)=(u,v,v)\) with \(u\ne v\). Subtracting the two distinct equilibrium equations yields \(u^2+uv+v^2=1-3d\). The case \(v=0\) gives \(u=0\) and is excluded by \(u\ne v\), so set \(r=u/v\). The remaining scalar equation then gives
\[
d=D(r)=-\frac{r(r+1)}{r^3+2},\qquad v^2=\frac{r+2}{r^3+2},\qquad u=rv.
\]
The simultaneous conditions \(d>0\), \(v^2>0\), and \(r\ne1\) reduce **exactly** to the two disjoint real intervals \(r<-2\) and \(-1<r<0\). Every allowed \(r\) supplies two signs of \(v\) and three choices of the exceptional site, hence six labeled states per distinct \(r\).

Differentiation gives
\[
D'(r)=\frac{P(r)}{(r^3+2)^2},\quad P(r)=r^4+2r^3-4r-2.
\]
For \(r<-2\), writing \(r=-s\), \(s>2\), gives \(P(-s)=s^3(s-2)+4s-2>0\). Thus \(D\) strictly increases from \(0\) to \(1/3\) as \(r\) increases from \(-\infty\) to \(-2\), giving one repeated-coordinate branch parameter for every \(0<d<1/3\).

On \(-1<r<0\), the derivative \(P'(r)=4r^3+6r^2-4<0\): indeed \(r^2(2r+3)\le1\) there, so \(P'(r)=2r^2(2r+3)-4\le-2\). Since \(P(-1)=1\) and \(P(0)=-2\), there is a unique \(r_*\in(-1,0)\) with \(P(r_*)=0\), and \(D\) rises from zero to a strict positive maximum \(d_*=D(r_*)\) before falling back to zero. Thus this interval supplies two parameters for \(0<d<d_*\), one for \(d=d_*\), and none above. Eliminating \(r\) between \(P(r)=0\) and \(d=D(r)\) produces
\[
108d^4-36d^2+12d-1=0.
\]
This quartic has exactly one zero in \((0,1/3)\): its derivative is \(12(36d^3-6d+1)\), and the cubic in parentheses has minimum \(1-2\sqrt2/3>0\) on the nonnegative real axis. Its endpoint values have opposite signs, and the root is the just-constructed maximum.

**3. All repeated-coordinate stability indices are exact.** At \((u,v,v)\) the antisymmetric mode \((0,1,-1)\) has eigenvalue
\[
\lambda_A=\frac{(r-1)(r+2)^2}{r^3+2}.
\]
The remaining symmetric two-dimensional restriction, using coordinates \((u,v)\), has matrix
\[
B=\begin{pmatrix}1-3u^2-2d&2d\\d&1-3v^2-d\end{pmatrix}
\]
with exact trace and determinant
\[
\operatorname{tr}B=-\frac{r^3+3r^2+2}{r^3+2},\qquad
\det B=-\frac{2(r-1)(r+2)P(r)}{(r^3+2)^2}.
\]
For \(r<-2\), \(\lambda_A>0\), hence all six associated states are unstable. For \(-1<r<r_*\), \(\lambda_A<0\), \(\operatorname{tr}B<0\), and \(\det B>0\), so all three eigenvalues are negative and the six states are sinks. For \(r_*<r<0\), \(\det B<0\), so they are saddles. At \(r=r_*\), precisely one eigenvalue vanishes; the other two are strictly negative. Because \(D''(r_*)=P'(r_*)/(r_*^3+2)^2<0\), and the branch parametrization is regular with \(v\ne0\), each of the six coalescences is a nondegenerate saddle-node fold.

**4. Count without omissions.** For \(0<d<d_*\): three homogeneous, six all-distinct, six repeated-coordinate from \(r<-2\), and twelve from two \(-1<r<0\) roots give \(3+6+6+12=27\), with \(2+6=8\) sinks. At \(d=d_*\), replace twelve by six, giving 21 states and two sinks. Above \(d_*\) and below \(1/3\), only \(3+6+6=15\) states remain, with two sinks. At \(d\ge1/3\), only the three homogeneous states remain, with two sinks. At \(d=0\) there are independently \(3^3=27\) equilibria and \(2^3=8\) sinks. The cubic-root trichotomy proves exhaustion for all real coordinates, not just for coordinates in a preferred physical interval.

## Verification
Run the accompanying standalone \`verify.py\` with Python 3 and SymPy. It checks the exact branch identities, the Jacobian invariant formulas, the elimination polynomial, rational root brackets, and representative stability signatures. Its finite sample checks are supplemental; the preceding sign and root arguments prove the all-parameter classification. The script prints a PASS line and rationally bracketed values of the fold parameter and coupling.

## Relationship to prior work
Hesoun, Stehlík and Volek (2026) prove a three-symbol coding of bounded stationary Nagumo sequences in a **sufficiently small** diffusion regime; their theorem does not give this exact three-site global coupling census. Hupkes, Morelli, Stehlík and Švígler (2019) enumerate periodic solution classes and establish the weak-diffusion \(3^n\)/\(2^n\) counts. Švígler (2021) studies qualitative existence regions and word symmetries, including the three-letter case; its inspected manuscript gives no exact value \(d_*\), complete all-coupling 3-ring census, or stability-index partition as stated here. The finite-graph Allen–Cahn treatment by van Gennip and collaborators (2014) establishes the broader graph framework and bifurcation phenomena, not this explicit three-node cubic threshold. These antecedents motivate the natural finite-ring test and provide its limiting checks.

## Limitations
This is a complete equilibrium and local linear stability classification only for the normalized symmetric cubic and a three-site **periodic** ring. It does not claim global attraction, attraction basin volumes, nonstationary dynamics, exact thresholds for longer rings, or the pinning threshold for fronts on the infinite lattice. The source-based originality assessment is provisional: the complete 2017 study of Nagumo stationary states on graphs and a 2021 paper on Fiedler-vector bifurcations were not available in full through the consulted lawful channels. Their abstracts do not state this exact theorem, but uninspected special examples could warrant a closer priority check.

## References
- J. Hesoun, P. Stehlík, J. Volek, *Characterization of spatial topological chaos for bistable lattice equation*, arXiv:2609.25868v1 (first public 2026-09-22), https://arxiv.org/abs/2609.25868.
- H. J. Hupkes, L. Morelli, P. Stehlík, V. Švígler, *Counting and ordering periodic stationary solutions of lattice Nagumo equations*, arXiv:1905.06107 (2019), https://pub.math.leidenuniv.nl/~hupkeshj/lyndon.pdf.
- V. Švígler, *Periodic stationary solutions of the Nagumo lattice differential equation: existence regions and their number*, Electronic Journal of Qualitative Theory of Differential Equations 2021, no. 23, https://doi.org/10.14232/ejqtde.2021.1.23.
- Y. van Gennip et al., *Mean curvature, threshold dynamics, and phase field theory on finite graphs*, arXiv:1307.0045 (2014).
- P. Stehlík, *Exponential number of stationary solutions for Nagumo equations on graphs*, J. Math. Anal. Appl. 455 (2017), 1749–1764, https://doi.org/10.1016/j.jmaa.2017.06.075 (full text inaccessible in this review).
- P. Stehlík, V. Švígler, J. Volek, *Bifurcations in Nagumo Equations on Graphs and Fiedler Vectors*, J. Dyn. Differ. Equ. 35 (2023), 2397–2412, https://doi.org/10.1007/s10884-021-10101-6 (full text inaccessible in this review).
