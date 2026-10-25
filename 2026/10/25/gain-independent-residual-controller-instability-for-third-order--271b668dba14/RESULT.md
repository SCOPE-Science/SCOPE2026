# Gain-independent residual-controller instability for third-order Runge–Kutta

## Finding

For the classical third-order three-stage explicit Runge–Kutta stability polynomial \(R(z)=1+z+z^2/2+z^3/6\), consider a third-order Hermite endpoint reconstruction on the complex scalar equation \(u'=\lambda u\), with \(\operatorname{Re}\lambda<0\). Use its scaled residual \(L^p\) estimator for any \(1\le p<\infty\) to drive a positive-gain integral (I-type) step-size controller with a smooth, increasing limiter. There exists a single point \(z_\star=-1+i\sqrt{w}\) on the absolute-stability boundary, where \(w>3\) uniquely solves \(w(w-3)^2=32\), such that for **every** finite \(p\), every controller exponent \(\beta>0\), and every smooth limiter \(\kappa\) with \(\kappa(1)=1\) and \(\kappa'(1)>0\), the amplitude/step-size feedback fixed point is linearly unstable. The Jacobian determinant is strictly larger than one. The same conclusion holds on a nonempty open arc of the left-half-plane absolute-stability boundary around \(z_\star\), and on its conjugate arc.

This is a gain-independent nonstabilizability result for the stated I-type feedback family, **not** a statement about PI/PID controllers, step rejection, or integration errors on a finite time interval.

## Assumptions and scope

Fix \(h>0\), \(\lambda\in\mathbb C\) with \(\operatorname{Re}\lambda<0\), and \(z=h\lambda\ne0\). Let \(u_{n+1}=R(z)u_n\). The degree-three Hermite polynomial \(\widehat u\) on \([0,h]\) interpolates \(u_n,u_{n+1}\) and their endpoint derivatives \(\lambda u_n,\lambda u_{n+1}\). Its residual is \(\widehat u'-\lambda\widehat u\). For \(1\le p<\infty\) define the normalized estimator

\[
E_p=h^{1-1/p}\|\widehat u'-\lambda\widehat u\|_{L^p(0,h)}
=\frac{|\lambda|^4|u_n|h^4}{6}
\left(\int_0^1[v(1-v)|2-v-vz|]^p\,dv\right)^{1/p}.
\]

Let \(\tau>0\) be an absolute tolerance. The controller proposes \(h_{n+1}=h_n\kappa((\tau/E_p)^{\beta/4})\), with arbitrary \(\beta>0\) and a positive, differentiable limiter \(\kappa\) satisfying \(\kappa(1)=1\), \(\kappa'(1)>0\). The identity limiter is included. The analysis assumes this unrejected one-step update map and exact arithmetic. At a point with \(|R(z)|=1\), selecting the initial amplitude to satisfy \(E_p=\tau\) defines a fixed point of the two-dimensional logarithmic amplitude/step-size map (the complex phase need not be fixed).

## Proof

Write \(v=t/h\). Substituting the four Hermite endpoint data and differentiating gives the exact identity

\[
h(\widehat u'-\lambda\widehat u)
=-\frac{u_n z^4}{6}\,v(v-1)(vz+v-2).
\]

Taking absolute values and converting the \(L^p\) norm proves the estimator formula above. Define the logarithmic coordinates \(\eta_n=\log|u_n|\), \(\chi_n=\log h_n\). At the amplitude/step-size fixed point, introduce

\[
\mu(z)=\operatorname{Re}\frac{zR'(z)}{R(z)},\qquad
\nu_p(z)=\left.\frac{\partial\log E_p}{\partial\chi}\right|_{\eta,\lambda\;\mathrm{fixed}}.
\]

Set \(A=2-v>0\), \(B=-vz\), and \(Q=A+B\). For \(0<v<1\), \(\operatorname{Re}z<0\) implies \(\operatorname{Re}B>0\), so

\[
0<d(v,z):=\operatorname{Re}\frac{B}{Q}
=1-\frac{A\operatorname{Re}Q}{|Q|^2}<1.
\]

Differentiate the positive integral defining \(E_p\). If \(g(v,z)=v(1-v)|Q|\), then

\[
\nu_p(z)=4+
\frac{\int_0^1 g(v,z)^p d(v,z)\,dv}
{\int_0^1g(v,z)^p\,dv};
\qquad 4<\nu_p(z)<5
\]

for all finite \(p\ge1\) and all \(\operatorname{Re}z<0\). The inequalities are strict because the weight is positive in the open interval.

For \(z=-1+iy\), with \(w=y^2\), direct polynomial substitution gives

\[
R(z)=\frac13+\frac{iy(3-w)}6,\quad R'(z)=\frac{1-w}{2},\quad
|R(z)|^2-1=\frac{w(w-3)^2-32}{36}.
\]

The polynomial \(f(w)=w(w-3)^2-32\) is strictly increasing for \(w>3\), because \(f'(w)=3(w-3)(w-1)>0\). It has a unique root \(w_\star>3\), and exact rational evaluations yield \(f(53/10)=-3963/1000<0\), \(f(11/2)=19/8>0\). Thus \(53/10<w_\star<11/2\), and \(z_\star=-1+i\sqrt{w_\star}\) is on \(|R|=1\) in the strictly stable continuous-time half-plane. Moreover, since \(|R(z_\star)|=1\),

\[
\mu(z_\star)=\operatorname{Re}\bigl(z_\star R'(z_\star)\overline{R(z_\star)}\bigr)
=\frac{(w_\star-1)^2(w_\star-2)}{12}.
\]

This expression is strictly increasing in \(w>3\); the lower enclosure gives

\[
\mu(z_\star)=\frac{(w_\star-1)^2(w_\star-2)}{12}
>\frac{(53/10-1)^2(53/10-2)}{12}
=5+\frac{339}{4000}>5>\nu_p(z_\star).
\]

At \(E_p=\tau\), the Jacobian for \((\eta,\chi)\) is

\[
J=\begin{pmatrix}1&\mu(z_\star)\\
-c/4&1-c\nu_p(z_\star)/4\end{pmatrix},
\qquad c=\beta\kappa'(1)>0,
\]

and therefore

\[
\det J=1+\frac c4\bigl(\mu(z_\star)-\nu_p(z_\star)\bigr)>1.
\]

Two eigenvalues whose product has modulus greater than one cannot both be in the closed unit disk: the fixed point is linearly unstable for every permitted \(p,\beta,\kappa\). Finally, continuity of \(\mu(z)\) near \(z_\star\) and the strict inequality \(\mu(z_\star)>5\) provide a surrounding open arc of the absolute-stability boundary inside \(\operatorname{Re}z<0\) where \(\mu(z)>5>\nu_p(z)\). Conjugation gives the reflected arc. This completes the claimed common instability witness.

## Verification

The standalone script `verify.py` uses exact rational polynomial arithmetic to verify the stability-polynomial identities, the rational root enclosure, and the exact lower bound above. It additionally checks the logarithmic residual sensitivities and Jacobian determinants at \(p=1,2,4\) for illustrative positive controller exponents; those finite checks are consistency tests, not the proof for all \(p\) and \(\beta\). Run `python3 verify.py` in the same directory. It prints `VERIFY_OK` on success.

For independent comparison with the analytic \(L^2\) source formula, direct integration gives

\[
\int_0^1 v^2(1-v)^2 |2-v-vz|^2\,dv
=\frac{8+|z|^2-5\operatorname{Re}z}{105}.
\]

## Relationship to prior work

Ranocha and Giesselmann (2023) introduce the relevant residual-based step-size controllers, their Hermite reconstructions, and the I-controller Jacobian. Their third-order complex-linear illustrations numerically exhibit instability for a particular controller gain, and they derive the special \(L^2\) residual formula; these facts are not new here. The contribution isolated here is a single **rigorously located stability-boundary arc** where **every positive I-controller gain**, **every finite residual \(L^p\) norm**, and **every smooth limiter with positive derivative at its operating point** fail simultaneously. This supplements, rather than replaces, the existing numerical/controller analysis. Earlier RK error-estimator and PI/PID-gain studies use different estimators or more complicated memory-based controllers and do not directly imply this uniform three-way obstruction.

## Limitations

This is a local linear stability result for a scalar complex test equation and an unrejected I-type controller based on central cubic-Hermite residuals. It does not address the behavior of PI/PID/history-dependent controllers, nonlinear limiters with zero operating-point slope, accepted-step rejection algorithms, or nonlinear ODEs. It does not show all controller initial states diverge and does not bound global finite-horizon discretization errors. The open arc need not be a maximal instability set. Generalization to other residual reconstructions or polynomial degrees remains unproved. Literature-completeness remains a scholarly risk.

## References

1. H. Ranocha and J. Giesselmann, *Stability of step size control based on a posteriori error estimates*, initial public preprint 2023-07-24, arXiv:2307.12677, https://arxiv.org/abs/2307.12677 . In particular, the central cubic-Hermite residual and the I-controller stability analysis.
2. H. Ranocha, L. Dalcin, M. Parsani, and D. I. Ketcheson, *Optimized Runge-Kutta Methods with Automatic Step Size Control for Compressible CFD*, arXiv:2104.06836, https://arxiv.org/abs/2104.06836 . Background on error-based controller-gain stability and optimization.
