# The unique rotational-diffusion onset of reentrant kurtosis in a trapped chirality-switching swimmer

## Finding

Consider a planar active Brownian swimmer in an isotropic harmonic trap of relaxation rate \(\kappa>0\). Its angular drift switches between \(\pm\omega\) at symmetric rate \(\gamma>0\) and there is angular Brownian diffusion of strength \(D\ge0\), with no translational Brownian diffusion. Write \(d=D/\kappa\), \(g=\gamma/\kappa\), and \(u=(\omega/\kappa)^2\). In the regime \(0<g<1/4\), there is exactly one critical diffusivity \(d_c(g)>1\) for the onset of reentrance of stationary Cartesian excess kurtosis as \(u\) increases. Below \(d_c(g)\) the excess is always negative. At \(d_c(g)\) it touches zero at a single positive \(u_c\). Above \(d_c(g)\) there are exactly two positive zeros, between which the excess is positive and outside which it is negative.

The onset curve \(d_c(g)\) is real analytic and **strictly decreasing** on \((0,1/4)\). Put
\[
 c=1-4g,\quad a=1+d+2g,\quad
 Q(d,g)=10d^2-(7g+2)d-14g^2-27g-10,
 \quad S(d,g)=(7d+3)(d+2g+3)(2d+g+1).
\]
The unique critical diffusivity is the solution of \(Q=2\sqrt{cS}\). Define
\[
 d_\star=\frac{15+\sqrt{11505}}{80},\qquad S_\star=S(d_\star,1/4),\qquad a_\star=1+d_\star+1/2.
\]
As \(g\uparrow1/4\), the two-zero onset approaches the quarter-rate boundary with the scalings
\[
 d_c(g)=d_\star+\frac{2\sqrt{S_\star}}{\partial_d Q(d_\star,1/4)}\sqrt{1-4g}+O(1-4g),
 \qquad
 u_c(g)\sim\frac{a_\star\sqrt{S_\star}}{\sqrt{1-4g}}.
\]
Thus the threshold in diffusivity stays finite but the angular speed at which the two zeros meet diverges as \((1-4g)^{-1/4}\) in trap-rate units.

## Model and kurtosis identity

In trap-rate time and with length scaled by propulsion speed divided by the trap rate, \(z\in\mathbb C\) obeys \(dz=(-z+e^{i\theta})\,dt\), \(d\theta=\sqrt{u}\,\sigma\,dt+\sqrt{2d}\,dW\), where the independent symmetric telegraph process \(\sigma\) has jump rate \(g\). The stationary rotationally invariant law is given by the stable position convolution of a two-sided stationary angular process; \(|z|\le1\). Its second radial moment is positive. For Cartesian excess \(\mathcal K=\mathbb E[(\operatorname{Re}z)^4]/\mathbb E[(\operatorname{Re}z)^2]^2-3\), the stationary moment identity reads
\[
 \mathcal K=-\frac{3(a^2 S-aQu+cu^2)}{2a^2 L_2 L_3},\quad
 L_2=u+d^2+2dg+6d+6g+9,\quad L_3=u+4d^2+2dg+4d+g+1.
\]
To recover the identity, let \(M^{(b)}_{pq}=\mathbb E[z^p\bar z^{q} e^{i(q-p)\theta}\sigma^b]\), \(b=0,1\), and put \(k=q-p\), \(n=p+q+dk^2\). The stationary generator gives, for \(p+q>0\),
\[
 (n+2bg)M^{(b)}_{pq}-ik\sqrt{u}\,M^{(1-b)}_{pq}
 =p M^{(b)}_{p-1,q}+q M^{(b)}_{p,q-1}.
\]
Omit negative indices, with \(M_{00}^{(0)}=1\) and \(M_{00}^{(1)}=0\). The determinant \(n(n+2g)+k^2u\) is positive. Iterating through total degree four gives \(M_{11}^{(0)}=a/((1+d)a+u)\) and \(M_{22}^{(0)}/(M_{11}^{(0)})^2=2-(a^2 S-aQu+cu^2)/(a^2 L_2L_3)\). Rotational averaging gives \(\mathcal K=\tfrac32M_{22}^{(0)}/(M_{11}^{(0)})^2-3\).

## Proof of the onset curve

The denominator of \(\mathcal K\) is positive. For \(c>0\), the numerator's quadratic \(a^2S-aQu+cu^2\) has a negative interval on \(u>0\) exactly when \(Q>0\) and \(Q^2>4cS\). Equality with \(Q>0\) gives a double zero. Thus the sign of \(\Phi(d,g)=Q-2\sqrt{cS}\) distinguishes the three cases in the finding.

For fixed \(g\), \(Q\) has precisely one positive zero \(d_0\), with \(d_0>1\) since \(Q(1,g)<0\). For \(d>d_0\) one has \(d\partial_d Q-2Q=(7g+2)d+2(14g^2+27g+10)>0\), whereas \(d\partial_d\log S<3\) because each of the three factors is affine with positive intercept. Consequently \(\partial_d\log(Q/\sqrt S)>1/(2d)\). The ratio goes from zero to infinity (its leading behavior is \((10/\sqrt{14})\sqrt d\)). Hence it meets \(2\sqrt c\) once. At that point \(\Phi_d=\sqrt S\partial_d(Q/\sqrt S)>0\), giving a real analytic graph by the implicit function theorem.

To order that graph with respect to \(g\), at every \(d\ge1\) one has \(S_g/S=2/(d+2g+3)+1/(2d+g+1)\le5/6\). Thus
\[
 \Phi_g=-(7d+28g+27)+(4-cS_g/S)\sqrt{S/c}
 \ge -(7d+28g+27)+\frac{19}{6}\sqrt{S(d,0)}(1+2g),
\]
where \((1-4g)^{-1/2}\ge1+2g\). The ratio \(S(d,0)/(7d+27)^2\) strictly increases: its logarithmic derivative is \(7/(7d+3)+1/(d+3)+2/(2d+1)-14/(7d+27)>0\) since the first and third positive terms each exceed \(7/(7d+27)\). At \(d=1\), \((19/6)\sqrt{S(1,0)}=(19/6)\sqrt{120}>34\). Hence the lower bound on \(\Phi_g\) is strictly larger than \(-(7d+28g+27)+(7d+27)(1+2g)\), which is nonnegative. Therefore \(d_c'(g)=-\Phi_g/\Phi_d<0\).

For the endpoint set \(\varepsilon=\sqrt{1-4g}\), so \(g=(1-\varepsilon^2)/4\). At \(\varepsilon=0\), the onset equation becomes \(Q(d,1/4)=0\) with positive root \(d_\star\), where \(Q_d>0\). Its analytic solution near this point has first derivative \(2\sqrt{S_\star}/Q_d\); uniqueness for small positive \(\varepsilon\) identifies it with the onset curve. At the double root \(u_c=a Q/(2c)=a\sqrt{S/c}\), giving the stated divergence. At fixed subcritical \(g\), the two roots genuinely split at onset: with \(R=Q^2-4cS\), one has \(R_d(d_c,g)=2Q(d_c,g)\Phi_d(d_c,g)>0\), and
\[
 u_\pm(d,g)=u_c(g)\ \pm\ \frac{a(d_c,g)}{2c}\sqrt{R_d(d_c,g)}\sqrt{d-d_c}+O(d-d_c).
\]
Further above threshold, for fixed \(g\), their sum and product and the leading terms of \(Q,S\) give \(u_-\sim(7/5)d^2\) and \(u_+\sim(10/c)d^3\).

## Verification and relation to prior work

The accompanying `verify.py` checks the rational radial moments and excess formula with SymPy, as well as finite sign examples. The graph of critical diffusivities and its endpoint and splitting laws are established by the inequalities and implicit differentiation above, not by those finite examples.

The [one-quarter chirality-flip boundary](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-universal-one-quarter-chirality-flip-boundary-for-stationary-k--7bd960c68958) gives the equivalent fourth-cumulant polynomial and the complete pointwise quadratic sign conditions, even in the presence of independent translational diffusion. No novelty is claimed here for that polynomial, the flip-rate boundary, or the discriminant test. The onset result resolves how the test depends on the rotational diffusivity and orders its boundary with the switching rate, including the singular approach to the quarter-rate boundary. This is distinct from free angular-velocity reversal (Das and Basu, arXiv:2301.11194), trapped propulsion-direction reversal (Santra, Basu and Sabhapandit, arXiv:2107.12640), and trapped fixed angular drift (Pattanayak et al., arXiv:2509.03448).
