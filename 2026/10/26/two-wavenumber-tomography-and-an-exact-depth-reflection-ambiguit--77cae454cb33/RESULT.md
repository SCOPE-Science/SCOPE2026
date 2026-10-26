# Two-wavenumber tomography and an exact depth-reflection ambiguity for two-layer gravity waves

## Finding
Consider the two positive gravity-wave frequencies (surface and internal branches) at each of two distinct wavenumbers in a finite-depth, two-layer fluid. Both branch frequencies at one wavenumber determine total depth exactly, irrespective of the unknown density contrast and partition of depth. Both branches at two distinct wavenumbers determine the total depth, the density ratio, and the absolute depth difference uniquely; they cannot distinguish which layer has which of the two depths. This ambiguity is exact at all wavenumbers. The following inequalities give a necessary-and-sufficient spectral realizability test, not merely a local inverse result.

Write \(\lambda_-(k)<\lambda_+(k)\) for the two squared frequencies normalized by \(gk\). For each \(k>0\), define
\[
H_k=\frac{\operatorname{arctanh}\lambda_-(k)+\operatorname{arctanh}\lambda_+(k)}{k},\qquad
q_k=\frac{\lambda_-(k)\lambda_+(k)}{1+\lambda_-(k)\lambda_+(k)}.
\]
For observations at \(0<k_1<k_2\), they are realizable by this model if and only if (i) each pair satisfies \(0<\lambda_-<\lambda_+<1\); (ii) \(H_{k_1}=H_{k_2}=:H>0\); (iii) putting
\[
F_k(z)=1-\frac{\cosh(kz)}{\cosh(kH)},\quad
R_0=\frac{1-\operatorname{sech}(k_2H)}{1-\operatorname{sech}(k_1H)},\quad
R_*=\frac{k_2\tanh(k_2H)}{k_1\tanh(k_1H)},
\]
one has \(R_0\le q_{k_2}/q_{k_1}<R_*\); and (iv) for the unique \(z\in[0,H)\) solving \(F_{k_2}(z)/F_{k_1}(z)=q_{k_2}/q_{k_1}\), one has \(0<2q_{k_1}/F_{k_1}(z)<1\).

For realizable data, the unique density ratio is \(\beta=1-2q_{k_1}/F_{k_1}(z)\), and the two admissible ordered depth pairs are
\[
(h_u,h_\ell)=\left(\frac{H+z}{2},\frac{H-z}{2}\right)
\quad\text{or}\quad
(h_u,h_\ell)=\left(\frac{H-z}{2},\frac{H+z}{2}\right).
\]
The pairs coincide when \(z=0\). For an individual wavenumber with realizable observations, there is instead a continuous one-parameter family of positive depths and contrasts, so two distinct wavenumbers are minimal for identifying these spectral invariants.

## Assumptions and scope
The fluid is linearized about rest, inviscid, incompressible, and irrotational in each homogeneous layer, with known gravity \(g>0\), a flat rigid bottom, an unconstrained free upper surface, a movable internal interface, no capillarity and no ambient shear. The upper and lower densities obey \(0<\rho_u<\rho_\ell\), with \(\beta=\rho_u/\rho_\ell\in(0,1)\). Both physical layer depths are strictly positive. Frequencies are exact positive angular frequencies; their wavenumbers are known and distinct. No information about wave eigenfunctions, surface/interface amplitude ratios, phases, or forced-wave amplitudes is assumed. The conclusion is a noiseless identification theorem, not a stability or statistical estimation assertion.

## Proof
**Forward quadratic and admissible branches.** The standard linear dispersion equation (Alam, Liu and Yue, equation (2.7), after undoing nondimensionalization) reads
\[
[AB+\beta]\lambda^2-(A+B)\lambda+1-\beta=0,\quad
A=\coth(kh_u),\quad B=\coth(kh_\ell),\quad
\lambda=\omega^2/(gk).
\]
Here \(A,B>1\). Its discriminant equals \((A-B)^2+4\beta(AB-1+\beta)>0\), so the roots are real and distinct. Their sum and product are positive. The polynomial at \(\lambda=1\) is \((A-1)(B-1)>0\), while the product is \((1-\beta)/(AB+\beta)<1\); consequently both roots lie strictly between zero and one.

**The depth sum rule.** Write \(p=\lambda_-\lambda_+\) and \(s=\lambda_-+\lambda_+\). Vieta gives \(p=(1-\beta)/(AB+\beta)\), \(s=(A+B)/(AB+\beta)\), and hence
\[
\frac{s}{1+p}=\frac{A+B}{AB+1}=\tanh(k(h_u+h_\ell)).
\]
Because both roots lie in \((0,1)\), the hyperbolic addition law implies
\[
\operatorname{arctanh}\lambda_-+\operatorname{arctanh}\lambda_+=k(h_u+h_\ell).
\]
This proves the sum rule without knowing the density ratio.

**A product invariant.** Define \(H=h_u+h_\ell\) and \(z=|h_u-h_\ell|\). From Vieta and the hyperbolic product identity,
\[
q_k=\frac{p}{1+p}=\frac{1-\beta}{AB+1}
=\frac{1-\beta}{2}\left(1-\frac{\cosh(kz)}{\cosh(kH)}\right)
=\frac{1-\beta}{2}F_k(z).
\]
This identity is symmetric in the two depths, explaining the all-wavenumber reflection ambiguity.

**Sharp monotonic ratio.** For fixed \(H>0\), \(0<k_1<k_2\), and \(0<z<H\), set \(R(z)=F_{k_2}(z)/F_{k_1}(z)\). The positive logarithmic decay magnitude is
\[
G(k,z)=-\partial_z\log F_k(z)
=\frac{k\sinh(kz)}{\cosh(kH)-\cosh(kz)}
=\frac{k}{2}\left[\coth\left(\frac{k(H-z)}2\right)-\coth\left(\frac{k(H+z)}2\right)\right].
\]
Let \(u=(H-z)/2>0\) and \(v=(H+z)/2>u\). Direct differentiation yields
\[
\partial_k G(k,z)=\frac12[\psi(ku)-\psi(kv)]<0,
\quad\psi(t)=\coth t-t\operatorname{csch}^2t.
\]
Indeed \(\psi'(t)=2\operatorname{csch}^2t\,[t\coth t-1]>0\) for every \(t>0\), since \(t>\tanh t\). Thus
\[
\partial_z\log R(z)=G(k_1,z)-G(k_2,z)>0.
\]
Continuity extends strict injectivity to \([0,H)\). At \(z=0\), direct evaluation gives \(R(0)=R_0\); since \(F_k(z)\sim k\tanh(kH)(H-z)\) as \(z\uparrow H\), the right endpoint is \(R_*\). The range is exactly \([R_0,R_*)\).

**Necessity and sufficiency.** Every physical model produces the four stated conditions by the preceding identities. Conversely, let four candidate frequencies satisfy (i)--(iv). Their common total depth \(H\), the strictly invertible ratio \(R(z)\), and \(\beta=1-2q_{k_1}/F_{k_1}(z)\) construct positive physical parameters. At each observed wavenumber, the constructed forward quadratic has the measured product \(p=q/(1-q)\). Its sum is fixed by the independently matching depth identity, because \(s/(1+p)=\tanh(kH)\). Consequently its unordered pair of roots is precisely the measured pair. Every physical parameter triple giving these data has this same \(H,z,\beta\), and only the ordering of the two depths is unidentifiable. The complete dispersion curves are equal under depth interchange because the quadratic depends on \(A,B\) only through their sum and product.

**Minimality.** At one wavenumber, physical observations determine \(H\) and \(q>0\). The function \(F_k\) decreases continuously and strictly from \(F_k(0)>2q\) to zero on \([0,H)\). Let the unique \(z_{\max}\in(0,H)\) solve \(F_k(z_{\max})=2q\). Every \(0\le z<z_{\max}\), together with \(\beta(z)=1-2q/F_k(z)\), realizes the same unordered frequency pair, giving a nontrivial continuum of admissible models. Thus one wavenumber cannot identify the density ratio or layer-depth separation.

## Verification
The accompanying standalone `checker.py` uses the forward quadratic independently of the inverse identities, computes both branches, and reconstructs parameters from both branches at two wavenumbers. It checks 600 deterministic pseudorandom positive-parameter combinations, plus exactly symmetric and reflected-depth cases. All tests passed. The numerical experiment is a reproducibility and algebra check; the infinite-domain strict monotonicity and global inverse statements follow from the proof, not sampling.

## Relationship to prior work
Alam, Liu and Yue (2009) provide the finite-depth two-layer forward dispersion equation used as a starting premise. Their primary paper develops Green functions, forced wave fields, and wave components; it does not state or prove this precise two-wavenumber realizability classification. Avital and Miloh (1994, 1998/1999) investigate inverse density stratification from ship-wake geometric observations rather than the specified four exact surface/internal eigenfrequencies. Their complete texts could not be compared here; this is a priority limitation, not proof of novelty. Choi and Camassa (1996) and other two-fluid theories treat forward waves and asymptotic regimes; they do not imply the quantified uniqueness theorem merely from sharing the dispersion relation. The new content claimed here is the exact depth sum, sharp monotone two-wavenumber inverse and realizability bounds as a combined theorem, including the unavoidable spectral reflection ambiguity; the forward dispersion equation is not claimed as new.

## Limitations
The inference is for noiseless, fully measured branches of the specified linear homogeneous model. It cannot recover an absolute density scale, cannot distinguish upper/lower depth assignment without eigenmode or amplitude information, and may be ill-conditioned near symmetric depths or extreme stratification/long-wave limits. Surface tension, weak shear, density gradients within layers, varying bathymetry and finite-precision measurements are outside scope. No independent external audit or experimental identification is claimed. An inaccessible prior inverse-ship-wave paper leaves residual research-priority uncertainty.

## References
1. M.-R. Alam, Y. Liu, D. K. P. Yue, *Waves due to an oscillating and translating disturbance in a two-layer density-stratified fluid*, Journal of Engineering Mathematics 65, 179–200 (2009), DOI 10.1007/s10665-009-9303-1, first published June 27, 2009. Full lawful author-hosted manuscript: https://taflab.berkeley.edu/wp-content/uploads/2014/01/2009-Waves_JEM_AlamLiuYue.pdf, equation (2.7).
2. E. Avital and T. Miloh, *On the determination of density profiles in stratified seas from kinematical patterns of ship-induced internal waves*, Journal of Ship Research 38, 308–318 (1994), DOI 10.5957/jsr.1994.38.4.308.
3. E. Avital and T. Miloh, *On an inverse problem of ship-induced internal waves*, Ocean Engineering 26, 99–110 (1998/1999), DOI 10.1016/S0029-8018(97)10033-6; full text inaccessible in this review.
4. W. Choi and R. Camassa, *Weakly-nonlinear internal waves in a two-fluid system*, Journal of Fluid Mechanics 313, 83–103 (1996), DOI 10.1017/S0022112096002133.
