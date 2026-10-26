# Two-frequency recovery of depth and flexural rigidity from hydroelastic dispersion

## Finding

**Exact two-frequency inverse theorem.** Fix known fluid density \(\rho>0\), gravity \(g>0\), and two distinct measured wavenumbers \(0<k_1<k_2\). In the linear, inviscid, incompressible, irrotational finite-depth water-wave model with a homogeneous, thin, *massless* elastic sheet of constant positive bending rigidity \(\mathcal D\), the angular frequency satisfies
\[
\omega(k)^2=\left(gk+\frac{\mathcal D}{\rho}k^5\right)\tanh(kh),\qquad h>0,\quad \mathcal D>0.
\]
Write the dimensionless wavenumber ratio and measured frequencies as
\[
q=\frac{k_2}{k_1}>1,\qquad U=\frac{\omega(k_1)^2}{gk_1}>0,\qquad V=\frac{\omega(k_2)^2}{gk_2}>0.
\]
Then **there is exactly one** pair \((h,\mathcal D)\in(0,\infty)^2\) producing the two measurements **if and only if**
\[
\boxed{\quad L_q(U)<V<q^5U,\quad}
\]
where
\[
L_q(U)=\begin{cases}
\tanh\!\big(q\operatorname{arctanh}U\big),&0<U<1,\\
1+q^4(U-1),&U\ge1.
\end{cases}
\]
The inequalities are strict. They give the exact set of physically realizable two-frequency data for this model, not merely a local inverse or a sufficient condition. In particular, no two distinct positive depths and positive sheet rigidities can generate the same pair of measured frequencies at the prescribed wavenumbers.

## Assumptions and scope

The water has constant known \(\rho\), known \(g\), a level impermeable bottom at depth \(h\), and a flat homogeneous thin elastic cover with bending rigidity \(\mathcal D\). Linear small-amplitude harmonic waves have real positive wavenumbers. Plate inertia, pre-stress, viscosity, currents, and wave attenuation are omitted. These assumptions are the standard Euler–Bernoulli thin-sheet linearization: the forward dispersion formula is established in the flexural-gravity literature, including Milewski–Wang (2013), equation (2), after nondimensionalization. The theorem assumes *both wavenumbers and both angular frequencies* are measured and belong to the same homogeneous region. It does not assume that ice thickness or elastic modulus is separately recoverable from their product defining bending rigidity.

Define
\[
t=k_1h>0,\qquad b=\frac{\mathcal D\,k_1^4}{\rho g}>0.
\]
The data equations are exactly
\[
U=(1+b)\tanh t,\qquad V=(1+q^4b)\tanh(qt).
\]

## Proof

**Step 1: Eliminate the bending parameter and find its full admissible interval.** Fix arbitrary \(q>1\) and \(U>0\). The first data equation gives
\[
b_U(t)=U\coth t-1.
\]
It is strictly decreasing since \(b_U'(t)=-U\operatorname{csch}^2t<0\). The requirement \(b_U(t)>0\) is equivalent to
\[
0<t<T_U,\quad T_U=\begin{cases}\operatorname{arctanh}U,&0<U<1,\\ +\infty,&U\ge1.\end{cases}
\]
(The case \(U=1\) admits every finite \(t>0\), with \(b_U(t)\downarrow0\) only at infinite depth.) The remaining data equation becomes a scalar equation
\[
V=G_U(t):=\big[1+q^4b_U(t)\big]\tanh(qt),\qquad t\in(0,T_U).
\]

**Step 2: Global strict monotonicity.** From \(U=(1+b_U(t))\tanh t\), we have
\[
b_U'(t)=-\frac{2(1+b_U(t))}{\sinh(2t)}.
\]
Using \(\operatorname{sech}^2z/\tanh z=2/\sinh(2z)\), differentiate to obtain the exact identity
\[
G_U'(t)=2q^4\tanh(qt)\left[
\frac{1+q^4b_U(t)}{q^3\sinh(2qt)}-
\frac{1+b_U(t)}{\sinh(2t)}\right].
\]
For every \(t>0\), strict convexity of \(\sinh\) on the positive half-line gives \(\sinh(2qt)>q\sinh(2t)\). Also \(1+q^4b<q^4(1+b)\) for every \(q>1\), \(b>0\). Therefore
\[
\frac{1+q^4b}{q^3\sinh(2qt)}
<\frac{1+q^4b}{q^4\sinh(2t)}
<\frac{1+b}{\sinh(2t)}.
\]
Every factor outside the square brackets is positive; hence \(G_U'(t)<0\) throughout the **entire** admissible interval. Thus each admissible \(V\) can correspond to at most one depth, and the recovered bending parameter is then uniquely fixed.

**Step 3: Sharp endpoint values and surjectivity.** As \(t\downarrow0\), \(b_U(t)=U/t-1+O(t)\) and \(\tanh(qt)=qt+O(t^3)\). Therefore
\[
\lim_{t\downarrow0}G_U(t)=q^5U.
\]
If \(0<U<1\), then \(T_U=\operatorname{arctanh}U\), \(b_U(t)\downarrow0\), giving
\[
\lim_{t\uparrow T_U}G_U(t)=\tanh\!\big(q\operatorname{arctanh}U\big).
\]
If \(U\ge1\), then \(t\uparrow\infty\) and \(b_U(t)\to U-1\), giving
\[
\lim_{t\to\infty}G_U(t)=1+q^4(U-1).
\]
By continuity and strict decrease, \(G_U\) maps \((0,T_U)\) bijectively onto exactly the open interval between those respective limits. This proves the necessary and sufficient inequalities and global uniqueness. No boundary value occurs with both \(h\) and \(\mathcal D\) finite and strictly positive.

**Step 4: Explicit reconstruction.** For data passing the strict inequalities, solve the one-dimensional monotone equation \(G_U(t)=V\) by bracketing. Recover
\[
\boxed{h=t/k_1,\qquad \mathcal D=\frac{\rho g}{k_1^4}\big(U\coth t-1\big).}
\]
The Jacobian of the forward map in \((t,b)\) is strictly positive: along fixed \(U\), \(G_U'(t)=-J/\tanh t<0\). Thus the reconstruction is locally smooth in the interior, but this does **not** imply a uniform conditioning bound near the boundary.

## Verification

A self-contained numerical checker (`checker.py`) evaluates all three components separately: the two forward data equations, the strict analytic admissibility inequalities, and the inverse computed by a bracketed scalar root solver. It checks 120 interior combinations of \(q\), \(t\), and \(b\), additionally evaluating the Jacobian orientation. With \(q=2\), \(t=0.8\), and \(b=0.4\), the data are \(U\approx0.929651478375\), \(V\approx6.82034730261\), and the inverse reconstructs the original parameters to numerical precision. These finite tests are ancillary checks; the proof above establishes the assertion for all positive parameters.

Run `python checker.py` with Python 3, SciPy and the standard-library `math` module. No raw field data are claimed, and the checker cannot certify physical adequacy of the idealized massless-plate model.

## Relationship to prior work

Milewski and Wang, *Three Dimensional Flexural–Gravity Waves* (2013), explicitly derive the same massless thin-sheet forward dispersion relation, with \(c^2=(1/k+k^3)\tanh(kH)\) after scaling, and study phase-speed minima and wavepacket modulation, not simultaneous recovery of depth and rigidity from two measured Fourier modes. Guyenne and Părău, *Finite-depth effects on solitary waves in a floating ice sheet* (2014), analyze nonlinear finite-depth dynamics, stability and the two wave-speed scales but do not give the global exact inverse-data image above. Marchenko, Morozov and Muzylev, *Measurements of sea-ice flexural stiffness by pressure characteristics of flexural-gravity waves* (2013), solve a different inverse measurement design involving pressure-sensor amplitude ratios and assess estimation error; this is relevant prior inverse work, not an assertion that inverse estimation itself is new. Voermans et al., *Estimating sea ice properties from wave observations in sea ice* (2023), use field-wave inversions including plate mass and separate unknown ice constitutive parameters, unlike the exact two-unknown massless-sheet setting here. More elaborate models can have materially different identifiability.

The present statement supplies **one global injectivity theorem and a necessary-and-sufficient two-measurement realizability region** for the specified massless-sheet dispersion law. Its monotonic scalar reduction is an exact consequence of that previously known forward law. Similar algebra can occur in gravity–capillary dispersion; the conclusion is not a claim of a new physical dispersion equation, nor of generic inverse-wave uniqueness under arbitrary constitutive laws.

## Limitations

The inversion is exact only for noise-free data and the stated ideal massless, unstressed sheet model. When the two measured wavenumbers nearly coincide or the water is effectively infinitely deep, inversion can become severely ill-conditioned despite uniqueness. The theorem recovers bending rigidity \(\mathcal D\), not ice thickness and Young's modulus separately. Ice inertia, compressive stress, currents, dissipation and finite floes invalidate the two-parameter formula without modification. The result supplies a mathematical realizability test and no error bars for finite-precision measurements. Priority may still be affected by specialized inverse-dispersion literature not captured in the inspected sources; this statement is not independently audited.

## References

1. P. A. Milewski and Z. Wang, *Three Dimensional Flexural–Gravity Waves*, Studies in Applied Mathematics **131** (2013), 135–148. DOI: 10.1111/sapm.12005. Author manuscript: https://purehost.bath.ac.uk/ws/portalfiles/portal/10790497/2DFGWangMilewskiStudies2013.pdf . (First published online 2013-02-13.)
2. P. Guyenne and E. I. Părău, *Finite-depth effects on solitary waves in a floating ice sheet*, Journal of Fluids and Structures **49** (2014), 242–262. DOI: 10.1016/j.jfluidstructs.2014.04.015.
3. A. Marchenko, E. Morozov and S. Muzylev, *Measurements of sea-ice flexural stiffness by pressure characteristics of flexural-gravity waves*, Annals of Glaciology **54** (2013), 51–60. DOI: 10.3189/2013AoG64A075.
4. J. J. Voermans et al., *Estimating sea ice properties from wave observations in sea ice*, arXiv:2305.06490 (2023), https://arxiv.org/abs/2305.06490 .
