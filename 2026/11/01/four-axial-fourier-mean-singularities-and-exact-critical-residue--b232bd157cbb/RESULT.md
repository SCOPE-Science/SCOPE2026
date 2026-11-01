# Four axial Fourier-mean singularities and exact critical residues of planar Fermat balls

## Finding
For each even integer \(q\ge 2\), define the planar Fermat ball
\[
K_q=\{(x,y)\in\mathbb R^2:x^q+y^q\le 1\},\qquad
v_q=\operatorname{area}(K_q)=\frac{4\Gamma(1+1/q)^2}{\Gamma(1+2/q)}.
\]
Use the Fourier convention \(\widehat{\mathbf1_K}(\xi)=\int_K e^{-i\langle x,\xi\rangle}\,dx\). For any \(p>0\) and unit \(u\), define the possibly infinite Fourier-mean radial function as in Langharst--Manui--Zvavitch:
\[
\rho_{F_pK_q}(u)^p=\frac p{v_q}\int_0^\infty|\widehat{\mathbf1_{K_q}}(ru)|^2r^{p-1}\,dr.
\]
Write \(p_q=2+2/q\), and \(\mathcal A=\{(\pm1,0),(0,\pm1)\}\). Then the *complete directional integrability classification* is:

1. For \(0<p<p_q\), the radial integral is finite in every direction, uniformly bounded in the direction, and \(F_pK_q\) is a compact star body.
2. When \(q\ge4\) and \(p_q\le p<3\), the radial integral diverges exactly on \(\mathcal A\); it is finite for every \(u\notin\mathcal A\).
3. For \(p\ge3\), the integral diverges in every direction. When \(q=2\), \(p_q=3\), so the intermediate regime is empty.

In particular the Fourier index (the sharp uniform squared-Fourier-decay exponent) is exactly \(p(K_q)=2+2/q\). At each axial direction the critical blow-up has the **exact** normalization
\[
\boxed{\lim_{p\uparrow p_q}(p_q-p)\rho_{F_pK_q}(e_1)^p
=4\left(1+\frac1q\right)q^{2/q}\Gamma\left(1+\frac2q\right).}
\]
The same holds at the other three axes. The right-hand side is \(12\) at \(q=2\), \(5\sqrt\pi\) at \(q=4\), and tends to \(4\) as even \(q\to\infty\). The last limit equals the directly computed residue of the square \([-1,1]^2\), but does **not** assert uniformity in \(q\) and \(p\).

## Assumptions and scope
The family consists of full-dimensional centrally symmetric convex disks with an *even integer* exponent \(q\ge2\). This assumption makes the boundaries real analytic and ensures contact orders are exactly \(q\) at the four axial support points and two elsewhere. All constants and asymptotics use the unnormalized Fourier transform given above. For \(p\ge p_q\), the formula defines an extended-valued radial function rather than a compact star body; no assertion about the Euclidean area of such an unbounded set is made.

## Proof
**1. Uniform Fourier decay.** For a unit direction \(u\) and \(r\ge1\), the divergence theorem expresses \(\widehat{\mathbf1_{K_q}}(ru)\) as \(i/r\) times the boundary oscillatory integral of \((u\cdot\nu(x))e^{-ir u\cdot x}\), where \(\nu\) is the outward normal. Near an axis endpoint \((1,0)\), write the boundary as \(x=f(y)=(1-y^q)^{1/q}\). On a sufficiently small fixed neighborhood \(f^{(q)}\) is nonzero, since \(f(y)=1-y^q/q+O(y^{2q})\). If \(|u_1|\ge1/2\), the phase \(u_1f(y)+u_2y\) has a uniformly nonvanishing \(q\)th derivative, so the order-\(q\) van der Corput bound is \(O_q(r^{-1/q})\). If \(|u_1|<1/2\), then \(|u_2|\ge\sqrt3/2\), and, after shrinking the patch, the first derivative is bounded away from zero; one integration by parts gives \(O_q(r^{-1})\). The other three axes are identical. On the remaining compact boundary arcs, curvature is uniformly positive. There, the first or second phase derivative is uniformly nonzero on finitely many appropriately chosen subarcs, yielding \(O_q(r^{-1/2})\). Amplitudes have uniformly bounded smooth norms, and the finite patch counts can be chosen independently of \(u\). Thus for a constant depending only on \(q\),
\[
\sup_{|u|=1}|\widehat{\mathbf1_{K_q}}(ru)|\le C_q r^{-1-1/q}.
\]
For \(q=2\) the positive-curvature estimate alone gives the same exponent. The integral near \(r=0\) is bounded by \(v_q^2r^{p-1}\), and the displayed large-radius bound proves uniform finiteness and continuity of \(\rho_{F_pK_q}\) for \(0<p<p_q\) by dominated convergence. Its positive minimum follows from continuity and nonzero low-frequency Fourier mass.

**2. Exact axial oscillation.** Integration in the transverse coordinate gives
\[
\widehat{\mathbf1_{K_q}}(re_1)=2\int_{-1}^1(1-|x|^q)^{1/q}e^{-irx}\,dx.
\]
At \(x=1-t\), the integrand amplitude is \(2q^{1/q}t^{1/q}(1+O_q(t))\). Watson's endpoint lemma, applied with smooth cutoffs at both endpoints and repeated integration by parts away from them, yields
\[
\widehat{\mathbf1_{K_q}}(re_1)
=A_q r^{-1-1/q}\cos\left(r-\frac\pi2(1+1/q)\right)
+O_q(r^{-2-1/q}),\quad
A_q=4q^{1/q}\Gamma(1+1/q)>0.
\]
Hence \(\limsup_{r\to\infty}r^{1+1/q}|\widehat{\mathbf1_{K_q}}(re_1)|=A_q\). This proves sharpness of the uniform exponent and divergence of the axial integral for every \(p\ge p_q\): the positive mean of the squared cosine prevents cancellation, including at the logarithmic endpoint.

**3. Nonaxial behavior.** Fix \(u\) with both coordinates nonzero. The two boundary points with normal \(\pm u\) are nonaxial and have strictly positive curvature \(\kappa_q(u)\); the other parts of the boundary contribute superpolynomially after localization. The classical one-dimensional nondegenerate stationary-phase formula and the same divergence-theorem normalization give
\[
\widehat{\mathbf1_{K_q}}(ru)
=\frac{2\sqrt{2\pi}}{\sqrt{\kappa_q(u)}}r^{-3/2}
\cos\bigl(rh_{K_q}(u)-3\pi/4\bigr)+O_{q,u}(r^{-5/2}).
\]
Here \(h_{K_q}(u)>0\) is its support function. Consequently the radial integral is finite when \(p<3\), and diverges when \(p\ge3\). This completes the directional trichotomy.

**4. Residue.** The area is the beta integral \(v_q=4\Gamma(1+1/q)^2/\Gamma(1+2/q)\). Squaring the axial expansion gives a leading \(A_q^2r^{-p_q}\cos^2(r-\pi p_q/4)\), with an integrable error uniformly for \(p\) near \(p_q\) from below. Setting \(\delta=p_q-p\), the nonoscillatory part of \(\cos^2\) contributes \(A_q^2/(2\delta)\) to \(\int_1^\infty r^{p-1}|\widehat{\mathbf1_{K_q}}(re_1)|^2dr\); the oscillatory part remains bounded by Dirichlet's test. Multiplication by \(p/v_q\) yields
\[
\frac{p_qA_q^2}{2v_q}=4(1+1/q)q^{2/q}\Gamma(1+2/q).
\]
As a crosscheck, \(q=2\) gives the standard Bessel-disk value \(12\). For the square, \(\widehat{\mathbf1_{[-1,1]^2}}(re_1)=4\sin r/r\), its area is \(4\), and the corresponding residue as \(p\uparrow2\) is \(4\).

## Verification
Run `python verify_fermat_fourier.py` (Python 3 with SciPy) to check the beta-area normalization, the axial endpoint coefficient by independent oscillatory quadrature at several frequencies, the disk Bessel identity, algebraic residue reductions, and the circle-to-square endpoint values. These finite diagnostics do not prove the uniform oscillatory-integral bounds, the directional statement, or asymptotic exactness for infinitely many exponents; those follow from the analytic arguments above.

## Relationship to prior work
Langharst, Manui, and Zvavitch introduced \(F_pK\), its Fourier index, and the disk/cube endpoint estimates. Their full arXiv paper gives the general formula and proves the square's loss of compactness at \(p=2\), but does not tabulate the even-exponent Fermat-disk directional classification or the gamma-valued axial critical residue. The finite-type Fourier decay machinery is classical: Bruna--Nagel--Wainger's estimates and Greenblatt's generalizations give more general bounds, but not the displayed special-function blow-up formula for Fourier-mean bodies. Brandolini--Colzani--Travaglini and Beretti study different averaged or discrepancy quantities. Thus the decay mechanism is **not** claimed as newly discovered. The contribution is the exact three-regime Fourier-mean classification and critical residue throughout this natural analytic family, with an explicit Euclidean-disk-to-square limit.

## Limitations
The result is restricted to planar even-exponent Fermat balls. It does not settle the general Fourier-index upper bound or injectivity/open fixed-point questions for Fourier-mean bodies. The residue is only for axial directions. Older finite-type Fourier literature could encode equivalent sharp decay estimates, and an unindexed integral calculation could predate the residue; independent priority assessment is outstanding. No independent mathematical validation has been performed.

## References
1. D. Langharst, A. Manui, A. Zvavitch, *On the Fourier Mean Bodies of a Convex Body*, arXiv:2601.20117, first public 2026-01-27, v2 2026-06-30, https://arxiv.org/html/2601.20117.
2. M. Greenblatt, *Convexity, Fourier transforms, and lattice point discrepancy*, arXiv:2402.16636, originally 2024-02-26; https://arxiv.org/abs/2402.16636. Discusses the classical finite-line-type estimates of Bruna, Nagel, and Wainger.
3. L. Brandolini, L. Colzani, G. Travaglini, *Irregularities of distribution and Fourier transforms of multi-dimensional convex bodies*, arXiv:2503.00973, 2025-03-02; https://arxiv.org/abs/2503.00973.
4. T. Beretti, *The Fourier transform of planar convex bodies and discrepancy over intervals of rotations*, arXiv:2408.15412, 2024-08-27; https://arxiv.org/abs/2408.15412.
5. Classical tools: the van der Corput oscillatory-integral lemma, Watson's endpoint lemma, and one-dimensional stationary phase (used in the precise forms described in the proof).
