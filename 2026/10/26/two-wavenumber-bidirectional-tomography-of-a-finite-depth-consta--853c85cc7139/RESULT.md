# Two-wavenumber bidirectional tomography of a finite-depth constant-shear gravity–capillary layer

## Finding

Four positive directional phase-speed measurements at just two distinct wavenumbers determine **four independent unknown physical coefficients**—finite depth, positive constant shear, positive restoring acceleration, and positive surface tension—uniquely. The exact set of physically realizable quadruples is given by three sharp open inequalities. One wavenumber always leaves a two-parameter family of indistinguishable layers. The inverse depth map loses conditioning at both the zero-depth and infinite-depth edges, with sharp algebraic and exponential laws, respectively.

Fix known \(0<k_1<k_2\) and liquid density \(\rho>0\). At wavenumber \(k_i\), let \(u_i\) and \(d_i\) be the positive magnitudes of the upstream and downstream intrinsic phase velocities, respectively, measured relative to the independently known velocity of the undisturbed free surface. Put
\[
\delta_i=u_i-d_i,\quad p_i=u_id_i,\quad
R=\frac{k_1\delta_1}{k_2\delta_2}.
\]
The four measurements correspond to **one and only one** combination \((h,S,g,\sigma)\in(0,\infty)^4\) if and only if
\[
u_i>d_i>0\quad(i=1,2),\qquad \frac{k_1}{k_2}<R<1,
\]
and, defining \(h\) by the unique solution
\[
R=\frac{\tanh(k_1h)}{\tanh(k_2h)}
\]
and \(Y_i=k_ip_i/\tanh(k_ih)\), if and only if also
\[
\boxed{\quad Y_1<Y_2<\frac{k_2^2}{k_1^2}Y_1.\quad}
\]
The exact inverse is
\[
\boxed{S=\frac{k_1\delta_1}{\tanh(k_1h)},\qquad
\frac{\sigma}{\rho}=\frac{Y_2-Y_1}{k_2^2-k_1^2},\qquad
g=\frac{k_2^2Y_1-k_1^2Y_2}{k_2^2-k_1^2}.}
\]
All feasibility inequalities are strict because all four unknown coefficients must be positive and the depth finite.

## Assumptions and scope

Consider an inviscid, incompressible, two-dimensional linearization about a plane free surface with a horizontal impermeable bed at depth \(h>0\). The stationary background velocity is \(U(z)=U_0+Sz\), for \(-h\le z\le0\), with \(S>0\). The background surface advection \(U_0\) is **known and subtracted** before measuring the two intrinsic speed magnitudes in opposite propagation directions. Horizontal slip at the bed is allowed; there is no extra constraint \(U(-h)=0\). The effective gravity is an independent parameter, for example in a variable-acceleration laboratory or a setting with an uncertain normal restoring field. The liquid density \(\rho\) and prescribed positive wavenumbers \(k_1<k_2\) are known. The effective gravitational acceleration \(g>0\), physical surface tension \(\sigma>0\), depth \(h>0\), and shear \(S>0\) are unknown. Both opposing wave branches are assumed distinguishable. The conclusions are for exact linear dispersion data; no nonlinear or noisy-observation model is assumed.

For \(k>0\), the classical constant-vorticity gravity–capillary dispersion branches [1, Eqs. (33)–(34)] are
\[
\begin{aligned}
u(k)&=\sqrt{\left(\frac gk+\frac{\sigma k}{\rho}\right)\tanh(kh)+\frac{S^2\tanh^2(kh)}{4k^2}}+\frac{S\tanh(kh)}{2k},\\
d(k)&=\sqrt{\left(\frac gk+\frac{\sigma k}{\rho}\right)\tanh(kh)+\frac{S^2\tanh^2(kh)}{4k^2}}-\frac{S\tanh(kh)}{2k}.
\end{aligned}
\]
These formulas specify the entire forward model; the uniqueness, sharp feasibility, one-wavenumber nonidentifiability, and depth-conditioning statements concern its inverse map.

## Proof

**Step 1: separate the directional and symmetric data.** Writing \(t(k)=\tanh(kh)\), direct subtraction and multiplication of the two forward branches yield exactly
\[
\delta(k)=u(k)-d(k)=\frac{St(k)}k,
\qquad
p(k)=u(k)d(k)=\left(\frac gk+\frac{\sigma k}{\rho}\right)t(k).
\]
Both quantities are strictly positive. Consequently, any admissible measurements satisfy \(u_i>d_i>0\) and
\[
R=\frac{\tanh(k_1h)}{\tanh(k_2h)}.
\]

**Step 2: sharp invertibility of the depth ratio.** Let \(F(h)=\tanh(k_1h)/\tanh(k_2h)\). Differentiation gives
\[
\frac{F'(h)}{F(h)}=\frac{2k_1}{\sinh(2k_1h)}-\frac{2k_2}{\sinh(2k_2h)}>0.
\]
For fixed \(h>0\), the function \(k\mapsto k/\sinh(2kh)\) is strictly decreasing because \(z\cosh z-\sinh z>0\) for \(z>0\), the latter following by differentiation from zero. As \(h\downarrow0\), \(F(h)\to k_1/k_2\); as \(h\to\infty\), \(F(h)\to1\). Thus \(F\) is a continuous, strictly increasing bijection from \((0,\infty)\) onto \((k_1/k_2,1)\). The ratio inequality is necessary and sufficient for a unique finite positive depth.

**Step 3: positivity and reconstruction.** With \(h\) fixed, the first identity determines a unique \(S=k_1\delta_1/\tanh(k_1h)>0\). The product identity gives
\[
Y_i=\frac{k_ip_i}{\tanh(k_ih)}=g+\frac\sigma\rho k_i^2.
\]
This two-by-two system has the unique solution in the finding. Its surface-tension coefficient is positive precisely when \(Y_2>Y_1\); its gravitational coefficient is positive precisely when \(k_2^2Y_1>k_1^2Y_2\). These are exactly the final strict feasibility inequalities. This proves necessity.

For sufficiency, reconstruct all parameters from any data satisfying the three conditions. The generated forward pair at each wavenumber has exactly the same positive difference \(\delta_i\) and positive product \(p_i\). A pair \((u,d)\) of positive numbers is uniquely determined by these two statistics: \(u=(\sqrt{\delta^2+4p}+\delta)/2\) and \(d=(\sqrt{\delta^2+4p}-\delta)/2\). Therefore the forward model reproduces the original four speeds exactly, proving sufficiency and global uniqueness.

**Step 4: necessity of using two wavenumbers.** At any single \(k>0\) and observed \(u>d>0\), let \(h\) vary through any positive interval; set \(S=k(u-d)/\tanh(kh)\). For each such \(h\), choose any
\[
0<g<\frac{kud}{\tanh(kh)}
\]
and define \(\sigma=\rho\left[kud/\tanh(kh)-g\right]/k^2>0\). This gives a two-dimensional open family of physically positive, exactly indistinguishable layers. Two distinct wavenumbers are therefore minimal for identification of this four-parameter family from bidirectional phase speeds.

**Step 5: sharp endpoint conditioning.** Elementary Taylor and exponential expansions give
\[
F(h)=\frac{k_1}{k_2}\left(1+\frac{k_2^2-k_1^2}{3}h^2+O(h^4)\right),\qquad h\downarrow0,
\]
\[
F'(h)\sim\frac{2k_1(k_2^2-k_1^2)}{3k_2}h\quad(h\downarrow0),
\qquad
F'(h)\sim 4k_1e^{-2k_1h}\quad(h\to\infty).
\]
Hence the exact inverse condition factor \(\lvert dh/dR\rvert\) obeys
\[
\boxed{\quad \left|\frac{dh}{dR}\right|\sim\frac{3k_2}{2k_1(k_2^2-k_1^2)h}\ (h\downarrow0),\qquad
\left|\frac{dh}{dR}\right|\sim\frac{e^{2k_1h}}{4k_1}\ (h\to\infty).\quad}
\]
These are deterministic local sensitivities to perturbations of the depth statistic \(R\); they do not assert a statistical error bound for noisy measured velocities.

## Verification

A standard-library Python checker, `checker.py`, separately evaluates the forward dispersion formula, its difference/product identities, exact inverse, sharp feasibility rejection, and the shallow/deep endpoint asymptotics. With its deterministic random seed, it performs 12,028 finite checks and prints `PASS`. In particular the two directional modes are evaluated from the square-root dispersion, not reconstructed from the inverse identities alone. Execute with `python3 checker.py` from the folder containing this document and the checker. The global claims are proved analytically above; no finite test substitutes for the monotonicity or global sufficiency proofs.

As one consistent synthetic data point, choose \(k_1=0.8\), \(k_2=2.1\), \(h=1.4\), \(S=0.7\), \(g=9.81\), \(\rho=1000\), and \(\sigma=0.18\). The branches give approximately \((u_1,d_1)=(3.51997511,2.81335231)\) and \((u_2,d_2)=(2.32750429,1.99602895)\). The inverse reconstructs all four positive parameters.

## Relationship to prior work

Ellingsen and Brevik [1] derive the full two-direction uniform-vorticity finite-depth dispersion, including capillarity, in their equations (33)–(35). The present result **uses that existing forward law** and does not claim a new wave dispersion relation. Its separate assertion is a global four-parameter inverse theorem, minimal-wavenumber obstruction, exact data-feasibility criterion, and two endpoint condition laws. The cited forward source discusses upstream/downstream speeds, wave stopping, and deep/shallow regimes, but does not establish the four-parameter reciprocal-data bijection or its strict measured-data feasibility region in the material inspected.

De Boeck [2] proves global bifurcation of finite-depth constant-vorticity nonlinear steady waves, rather than identification of these linear coefficients from reciprocal dispersion data. Barbieri and collaborators [3] study nonlinear Stokes-wave bifurcation and linear phase-speed geometry, not the four-observable joint inverse classification. Two-layer inverse tomography and one-direction hydroelastic phase-speed identification address different physical forward systems; those results do not furnish the shear difference/product separation above. An unlocated equivalent result in historical wave-dispersion inversion literature remains a priority risk; the present mathematical claims should not be interpreted as externally established historical firsts.

## Limitations

The surface reference current \(U_0\), density, and two exact distinct wavenumbers must be known. The sign convention fixes strictly positive \(S\); reversed shear orientation can be handled only after reversing branch labels. Zero-shear data have \(\delta_i=0\), so this particular four-parameter parametrization cannot infer the signed zero shear via the ratio. The exact ends \(h=0\) and \(h=\infty\) are excluded, as are \(g=0\) and \(\sigma=0\). The local sensitivity laws demonstrate ill-conditioning in those limits, not failure of noiseless uniqueness at finite positive depth. Experimental feasibility, calibration error, finite-sample statistical precision, wave breaking, viscosity, and nonlinear corrections are not treated. Historical exclusivity has not been independently certified.

## References

[1] S. Å. Ellingsen and I. Brevik, “How linear surface waves are affected by a current with constant vorticity,” arXiv:1311.1073v1, first public November 5, 2013. https://arxiv.org/abs/1311.1073 . Equations (33)–(35), §§2–5 and conclusions inspected.

[2] P. de Boeck, “Global bifurcation for steady finite-depth capillary-gravity waves with constant vorticity,” arXiv:1404.5608v1, first public April 22, 2014. https://arxiv.org/abs/1404.5608 . Introduction and free-boundary/bifurcation statements inspected.

[3] T. Barbieri, M. Berti, A. Maspero, and M. Mazzucchelli, “Bifurcation of gravity-capillary Stokes waves with constant vorticity,” arXiv:2501.14353, January 24, 2025. https://arxiv.org/abs/2501.14353 . Dispersion and phase-speed structure compared for potentially stronger coverage.
