# Sharp sixth Fourier moment and phase rigidity for the hexagonal root aperture

## Finding
Let
\[
\mathcal H=\{(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)\}\subset\mathbb Z^2.
\]
For six **arbitrary complex** coefficients \(c_\nu\), define
\[
P(z,w)=\sum_{\nu=(a,b)\in\mathcal H}c_\nu z^a w^b,
\qquad M=\sum_{\nu\in\mathcal H}|c_\nu|^2.
\]
With normalized Haar measure on \(\mathbb T^2\), the exact sharp sixth-moment inequality is
\[
\boxed{\ \int_{\mathbb T^2}|P|^6\,dm\le\frac{85}{9}M^3.\ }
\]
The constant is attained. **Every nonzero equality case**, with no extra exceptional families, is exactly
\[
\boxed{c_{(a,b)}=\lambda\,\eta^a\xi^b\quad((a,b)\in\mathcal H),
\qquad \lambda\in\mathbb C\setminus\{0\},\quad |\eta|=|\xi|=1.}
\]
Thus the projective equality family is a two-torus, not the larger three-torus permitted by the fourth-moment antipodal-product condition.

The identical sharp inequality and continuous phase classification hold when the integral is replaced by the **normalized \(N\times N\) Fourier-grid average** for every integer \(N\ge7\). The nonaliasing cutoff is sharp for this stable constant: when \(N=6\), the flat coefficients give average \(2046\) instead of the continuous value \(2040\), so the sharp sixth-power ratio strictly exceeds \(85/9\).

## Assumptions and scope
All six coefficient positions are distinct. Coefficients may be zero; only the nonzero equality cases are classified. Haar measure and finite-grid counting measure are normalized to total mass one, while \(M\) is an unnormalized sum of six squares. For the grid, evaluate \(P\) at all pairs of \(N\)-th roots of unity using the displayed integer exponents; \(N\ge7\). The maximizing phases \(\eta,\xi\) need **not** be \(N\)-th roots of unity, even on the finite grids. This is a sharp \(\ell^2\to L^6\) inequality for this single six-frequency aperture, not a claim about arbitrary six-point supports or other exponents.

## Proof
**1. Triple-convolution identity.** Write \(S=\mathcal H\), extend \(c\) by zero to \(\mathbb Z^2\), and put \(C=c*c*c\). Orthogonality gives
\[
\int_{\mathbb T^2}|P|^6\,dm=\sum_{h\in\mathbb Z^2}|C(h)|^2.
\tag{1}
\]
The triangle inequality on every convolution fiber shows that replacing \(c_\nu\) by \(|c_\nu|\) cannot decrease (1). Consequently it suffices first to maximize over nonnegative coefficients; equality for complex coefficients requires alignment of the triple products in **each** nonempty sum fiber.

**2. Antipodal balancing.** Let \(a_\nu=|c_\nu|\) and
\[
b_\nu=\left(\frac{a_\nu^2+a_{-\nu}^2}{2}\right)^{1/2}.
\]
This symmetrization preserves \(\sum a_\nu^2=M\). Define the nonnegative autocorrelation \(R_h(a)=\sum_\nu a_\nu a_{\nu+h}\). Cauchy--Schwarz applied to the two vectors \((a_\nu,a_{-\nu})\) and \((a_{\nu+h},a_{-\nu-h})\) yields
\[
2b_\nu b_{\nu+h}\ge a_\nu a_{\nu+h}+a_{-\nu}a_{-\nu-h}.
\]
Summing and changing variables proves \(R_h(b)\ge R_h(a)\) for **every** \(h\), with \(R_0(b)=R_0(a)=M\). Since
\[
\int|P_a|^6\,dm
=\sum_{h_1+h_2+h_3=0}R_{h_1}(a)R_{h_2}(a)R_{h_3}(a),
\tag{2}
\]
balancing cannot decrease the sixth moment. If any antipodal magnitudes differ, the strict pairwise root-mean-square inequality gives \(\sum b_\nu>\sum a_\nu\), hence
\(\sum_h R_h(b)=(\sum b_\nu)^2>(\sum a_\nu)^2=\sum_hR_h(a)\). Some nonzero shift is therefore strictly improved. Its \((h,-h,0)\) term in (2) increases strictly because \(R_0=M>0\). **Every nonzero maximizer must therefore have equal magnitudes at antipodal sites.** This independently establishes the symmetrization premise used below.

**3. Exact balanced polynomial.** Set \(v_1=(1,0)\), \(v_2=(0,1)\), \(v_3=(-1,1)\) and let the nonnegative antipodally balanced coefficients at \(\pm v_1,\pm v_2,\pm v_3\) be \(x,y,z\). Enumerating the ordered triple-sum fibers in (1) gives the exact identity
\[
F(x,y,z)=20(x^6+y^6+z^6)
+180\!\sum_{i\ne j}x_i^4x_j^2
+900x^2y^2z^2,
\tag{3}
\]
where \((x_1,x_2,x_3)=(x,y,z)\). In terms of \(X=x^2,Y=y^2,Z=z^2\), \(s=X+Y+Z\), \(e_2=XY+XZ+YZ\), and \(e_3=XYZ\), this simplifies to
\[
\boxed{F=20s^3+120s e_2+420e_3.}
\tag{4}
\]
The 216 ordered triples have exactly 37 distinct sum fibers, with multiplicity histogram \(\{1:6,3:12,6:12,12:1,15:6\}\). The coefficient polynomial (3), including all coefficients, follows from finite exact enumeration, independently reproduced by the packaged standalone checker; the finite combinatorial identity is not a stand-in for an infinite search.

**4. Sharp optimization.** For \(X,Y,Z\ge0\),
\[
e_2\le\frac{s^2}{3},\qquad e_3\le\frac{s^3}{27},
\]
with both equalities, for \(s>0\), if and only if \(X=Y=Z=s/3\). Since \(M=2s\), (4) gives
\[
F\le\left(20+40+\frac{420}{27}\right)s^3
=\frac{680}{9}s^3=\frac{85}{9}M^3.
\]
This is strict unless the six original coefficient magnitudes are identical, by steps 2 and 4. At \(x=y=z=1\), one has \(F=2040\), \(M=6\), and \(2040/6^3=85/9\). Thus the bound and its normalization are exact.

**5. Complete phase classification.** Let \(c_\nu\) be a nonzero equality case. All six magnitudes are the same positive number. Since equality in the complex majorant from step 1 is required separately in every triple-sum fiber, for each \(j\in\{1,2,3\}\) the three products associated with
\(v_j=v_j+v_i-v_i\) for \(i=1,2,3\) have the same phase. Cancelling the nonzero factor \(c_{v_j}\) gives
\[
c_{v_1}c_{-v_1}=c_{v_2}c_{-v_2}=c_{v_3}c_{-v_3}=:\tau\ne0.
\tag{5}
\]
Choose a square root \(\lambda^2=\tau\) and set \(c_{v_i}=\lambda\eta_i\), \(c_{-v_i}=\lambda\eta_i^{-1}\). All \(|\eta_i|=1\). In the zero triple-sum fiber, the two distinct unordered zero sums are
\[
v_1+v_3-v_2=0,\qquad -v_1-v_3+v_2=0.
\]
Alignment of their two triple products forces
\[
\left(\frac{\eta_1\eta_3}{\eta_2}\right)^2=1.
\]
If this ratio equals \(-1\), replacing the chosen square root \(\lambda\) by \(-\lambda\) replaces every \(\eta_i\) by \(-\eta_i\) and makes the ratio \(+1\). Therefore \(\eta_2=\eta_1\eta_3\). Because \(v_1,v_3\) form an integer-lattice basis and \(v_2=v_1+v_3\), there are \(\eta,\xi\in\mathbb T\) such that \(c_{(a,b)}=\lambda\eta^a\xi^b\) on all six sites. Conversely every such coefficient family has uniform magnitude and every triple-product in a fixed fiber equals \(\lambda^3\eta^{h_1}\xi^{h_2}\); it achieves equality in every step. After quotient by common nonzero scalar, \((\eta,\xi)\) is an unrestricted two-torus, proving the classification.

**6. Discrete grids and the sharp nonaliasing threshold.** Every triple sum lies in \([-3,3]^2\). Reduction modulo \(N\) is injective on this box for every \(N\ge7\). Hence the convolution identity (1), its exact fiber table, the optimal constant, and all equality conditions remain unchanged on \((\mathbb Z/N\mathbb Z)^2\). For \(N=6\), direct aggregation of the **explicit finite** sum fibers for flat coefficients gives \(2046\), establishing that the stable \(85/9\) ratio already fails at the immediately preceding grid size; this is a boundary witness, not a claim to classify the smaller-grid norm.

## Verification
The embedded `checker.py` uses only Python's standard library. It constructs all 216 ordered triple sums and their 37 integer fibers, computes the complete degree-six symbolic coefficient polynomial by exact integer combinatorics, independently checks equations (3)–(4), and verifies \(2040/216=85/9\). It also checks 350 bounded Gaussian-integer coefficient arrays, 216 balanced integer triples, representative complex character-phase maximizers, normalized finite Fourier-grid averages for sizes \(7,8,9\), and the \(N=6\) boundary witness. The embedded `checker_output.txt` records a completed `VERIFY_OK` run. None of the finite samples is used to assert global optimality: that follows from the balancing inequality, the exact polynomial identity, and the elementary symmetric-polynomial bounds.

## Relationship to prior work
Ciccone and Gonçalves (2022, arXiv:2208.09441) develop sharp sixth-power Fourier extension under arithmetic restrictions on frequency support. Their operator is Fourier extension from the Euclidean unit circle into \(\mathbb R^2\), with Bessel-weighted analysis and a \(P(3)\) support condition, whereas the present problem is Fourier synthesis from six integer-lattice characters on a compact two-torus. The hexagonal root spectrum has a non-cancellation triple relation \(v_1+v_3-v_2=0\); its phase geometry and exact \(85/9\) constant are not covered by the cited circle theorem.

The published *Reflection root-mean-square majorization of every even Fourier moment* proves a general necessary antipodal-modulus symmetry but does not calculate this six-mode \(L^6\) constant or the final triangle-induced phase rigidity; step 2 above independently verifies the needed argument. The published *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture* treats the **different** total-degree-two simplex frequency support, rather than the centrally symmetric hexagonal root orbit. The published small-field anisotropic sphere phase classification identifies an antipodal-product phase torus at the **fourth** moment; it cannot imply the present **sixth**-moment suppression of noncharacter phases because the triple-sum relations differ. The present sixth-moment classification specifically resolves this difference between pair-sum and triple-sum phase constraints.

## Limitations
The theorem concerns the exact six-site root orbit, normalized sixth moments, and square cyclic grids of order at least seven. It does not determine the optimal constant or optimizer set for smaller grids, other planar apertures, non-even exponents, or weighted norms. An older trigonometric-polynomial or lattice-walk table could contain the unweighted moment \(2040\), but such a scalar enumeration would not by itself imply the unrestricted complex-coefficient sharp norm and equality classification. The originality comparison is best-knowledge, not an independent exhaustive priority determination; no independent external audit has been performed.

## References
1. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441v1, first public 2022-08-19, https://arxiv.org/abs/2208.09441; primary Mathematics Subject Classification 42B10.
2. A. Mudgal, *Additive energies on spheres*, arXiv:2105.06925v1, first public 2021-05-14, https://arxiv.org/abs/2105.06925; large finite lattice spheres rather than the single six-vertex hexagonal Fourier norm.
3. *Reflection root-mean-square majorization of every even Fourier moment*, publicly accessible mathematical research record (2026), identifier ce42dcffc673.
4. *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture*, publicly accessible mathematical research record (2026), identifier bea9cf2ed885.
5. *Small-field phase dichotomy for anisotropic sphere extremizers*, publicly accessible mathematical research record (2026), identifier 973050ba74a9.
