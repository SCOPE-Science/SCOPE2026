# Sharp attainable fourth-cumulant range at optimal diffusion for chiral tumblers

## Finding and assumptions

Consider a planar particle propelled at speed \(v>0\), with circle-valued orientation
\[
\Theta_t=\Theta_0+\Omega t+\sqrt{2D}\,W_t+\sum_{j=1}^{N_t}\eta_j\pmod{2\pi}.
\]
Here \(\Omega>D>0\), \(\Theta_0\) is uniform, \(W\) is standard Brownian motion, \(N\) is a homogeneous Poisson process of rate \(\lambda\), and the independent tumble increments have a common symmetric circle law \(\nu\); all sources of randomness are independent. Put \(c_j=\int\cos(j\eta)\,\nu(d\eta)\) and assume \(c_1<1\). At the rate \(\lambda_*=(\Omega-D)/(1-c_1)\) that maximizes per-coordinate long-time diffusivity, the **sharp attainable interval** of longitudinal fourth cumulant rates is
\[
-\frac{3v^4}{\Omega(16D^2+4\Omega^2)}\ \le\ K_4(\nu)\ <\ -\frac{3v^4}{20\Omega^3},\qquad
K_4(\nu)=\lim_{T\to\infty}\frac{\kappa_4(v\int_0^T\cos\Theta_s\,ds)}{T}.
\]
The minimum occurs exactly for laws supported on \(\{0,\pi\}\) with positive mass at \(\pi\). Every interior value is attained by \(\tfrac12(\delta_\varphi+\delta_{-\varphi})\) for a suitable \(\varphi\in(0,\pi)\); the unattainable supremum is approached as \(\varphi\downarrow0\) and the associated optimizing rates diverge. The ratio of the maximum absolute rate to its infimum is \(5\Omega^2/(4D^2+\Omega^2)\in(1,5)\).

The contribution is the attainable interval, endpoint laws and quantitative spread over **all** symmetric turn laws. The diffusivity optimizer is known from Olsen and Löwen (arXiv:2405.14326). The optimized pointwise fourth-cumulant formula and its negativity are known from *Diffusion-optimal symmetric tumbles enforce negative fourth cumulant* (Resultary d952c0bfcbf8); neither is claimed as new here.

## Proof

Put \(A=D+\lambda(1-c_1)\) and \(B=4D+\lambda(1-c_2)\). Symmetry of the jump law makes the Fourier generator eigenvalues \(-\mu_n\), where \(\mu_n=Dn^2+\lambda(1-c_n)-in\Omega\). The first-harmonic correlation of the centered longitudinal velocity is \((v^2/2)e^{-As}\cos(\Omega s)\) at lag \(s\ge0\). Twice its integral gives variance rate \(v^2 A/(A^2+\Omega^2)\); half that rate is per-coordinate diffusivity. Since \(A\) increases from \(D\) to infinity, differentiation yields the unique optimum \(A=\Omega\) and diffusivity \(v^2/(4\Omega)\).

For clarity about normalization, recover the known cumulant formula by tilting the angular generator by \(kv\cos\theta\). At \(k=0\), the simple constant eigenvalue is separated in real part from the other Fourier modes by at least \(D\). The tilted operator is an elliptic circle generator with bounded convolution and multiplication perturbations. For sufficiently small complex \(k\), bounded analytic perturbation preserves a simple eigenvalue \(\Lambda(k)\) near zero and separates the remaining spectrum to its left. The Feynman–Kac expectation for a uniform start is \(e^{T\Lambda(k)}(a(k)+O(e^{-\gamma T}))\) in a smaller neighborhood, with \(a(0)=1\), analytic \(a\), and \(\gamma>0\). This follows by separating the spectral projection near zero from the exponentially decaying complement of the analytic semigroup. Thus derivatives of the logarithm divided by \(T\) converge to the derivatives of \(\Lambda\) at zero by Cauchy's integral formula. Rotation by \(\pi\) makes \(\Lambda\) even.

Write \(r_j=\mu_j^{-1}\) for \(j=\pm1,\pm2\) and normalize the tilted eigenfunction to have mean one. Its first-order coefficients at \(\pm1\) are \(vr_j/2\), the second-order coefficients at \(\pm2\) are \(v^2 r_j r_{2j}/4\) for \(j=\pm1\), and its second-order constant coefficient is zero. Projecting onto the constant gives the quadratic eigenvalue coefficient \(a_2=v^2(r_1+r_{-1})/4\). At cubic order the coefficients on \(j=\pm1\) are \(v^3r_j^2r_{2j}/8-a_2vr_j^2/2\). Project once more onto the constant to get the quartic coefficient
\[
a_4=\frac{v^4}{16}\left[r_1^2r_2+r_{-1}^2r_{-2}-(r_1+r_{-1})(r_1^2+r_{-1}^2)\right].
\]
No higher harmonics can enter this coefficient because tilting moves by only one Fourier index at a time. At \(A=\Omega\), \(r_{\pm1}=(1\pm i)/(2\Omega)\), so \(r_1^2+r_{-1}^2=0\). With \(r_2=(B-2i\Omega)^{-1}\) this gives \(K_4=24a_4=-3v^4/[\Omega(B^2+4\Omega^2)]\).

The law-space optimization is separate. At \(\lambda=\lambda_*\),
\[
B_*=4D+(\Omega-D)\frac{1-c_2}{1-c_1},\qquad
\frac{1-c_2}{1-c_1}=2\int(1+\cos\eta)\,\frac{1-\cos\eta}{1-c_1}\,\nu(d\eta).
\]
The weighted measure is a probability measure with no mass at zero angle. The ratio is therefore in \([0,4)\); it vanishes exactly when the weighted measure is concentrated at \(\pi\), equivalent to the stated support and positive-mass condition on \(\nu\). For the symmetric fixed-angle pair the ratio equals \(2(1+\cos\varphi)\), realizing the whole half-open interval as \(\varphi\) runs from \(\pi\) toward zero. Thus the exact interval for \(B_*\) is \([4D,4\Omega)\). The known pointwise rate is strictly increasing in \(B_*>0\); evaluating at the two edges and dividing their absolute magnitudes yields the sharp interval and ratio. In the fixed-angle limit \(\varphi\downarrow0\), \(1-c_1=1-\cos\varphi\to0\), so \(\lambda_*\to\infty\).

## Examples, verification and scope

At \((D,\Omega,v)=(1,3,2)\), the half-turn, symmetric quarter-turn and symmetric \(\pi/3\) laws have respective optimizing rates \(1,2,4\) and \(B_*\) values \(4,8,10\). Their fourth cumulant rates are \(-4/13,-4/25,-2/17\); their common per-coordinate diffusivity is \(1/3\). The unchanged `verify.py` checks the pointwise formula by symbolic simplification, rational examples and finite tilted-Fourier spectra; the sharp law-space conclusion follows from the exact weighted-measure proof, not finite sampling.

The result concerns long-time longitudinal cumulants, not the sign of a finite-time fourth cumulant. Adding independent translational Brownian motion leaves the fourth cumulant unchanged. No claim is made for nonsymmetric laws, fixed-rate law optimization, correlated tumbles or interacting particles.

## Relationship to prior work

In addition to the exact pointwise precedent credited above, fourth-moment methods in Villa-Torrealba et al. (arXiv:2002.02872), Britton et al. (arXiv:2608.23519) and Pattanayak et al. (arXiv:2404.09650) concern related angular or displacement processes. The fixed-persistence envelope recorded in Resultary 0a534892a5b1 concerns Poisson angular jumps without continuous angular diffusion or intrinsic angular drift. No absolute priority is claimed.
