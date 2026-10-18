# Spatial compound-Poisson posterior law for asymmetric telegraph killing

## Finding
For a telegraph particle alternating between velocities \(+u\) and \(-v\), with \(u,v>0\), equal velocity-switching rate \(b>0\), independent exponential termination rate \(a>0\), and equiprobable initial velocities, the **termination time conditioned on its terminal displacement** possesses an exact convolution decomposition. The increments of the conditional time law as the magnitude of the observed displacement increases are a deterministic ballistic delay plus a common compound-Poisson subordinator, even when \(u\ne v\).

Write \(T\) for termination time and \(X=\int_0^T V_t\,dt\) for terminal displacement. Put \(H=u+v\), \(K=uv\), \(d=u-v\), \(\eta=2b\sqrt K/H\), and \(\Delta(q)=\sqrt{(q+b)^2-\eta^2}\). For \(\sigma\in\{+1,-1\}\), define \(c_+=u\), \(c_-=v\) and
\[
 A_\sigma(q)=\frac1{2c_\sigma}+\frac H{4K}\left(\frac{q+b}{\Delta(q)}-1\right)+\frac b{H\Delta(q)},\qquad
 \zeta_\sigma(q)=\frac{H\Delta(q)-\sigma d(q+b)}{2K}.
\]
Let \(I_j\) denote the modified Bessel function of the first kind. Define a nonnegative \(U_\sigma\) by its atom and density:
\[
 \Pr(U_\sigma=0)=\frac{1}{2c_\sigma A_\sigma(a)},\qquad
 \frac{\Pr(U_\sigma\in dt)}{dt}=\frac{e^{-(a+b)t}}{A_\sigma(a)}\left(\frac{H\eta}{4K}I_1(\eta t)+\frac bH I_0(\eta t)\right),\quad t>0.
\]
Independently, let \((J_r)_{r\ge0}\) be a compound-Poisson subordinator with Lévy measure per unit \(r\)
\[
 \nu(dt)=\frac{H\eta}{2K}\frac{e^{-(a+b)t}I_1(\eta t)}t\,dt,\qquad t>0.
\]
Then, for every \(r>0\), the following holds for the continuous version of the regular conditional laws:
\[
 \boxed{\mathcal L(T\mid X=\sigma r)=\mathcal L\left(U_\sigma+\frac r{c_\sigma}+J_r\right).}
\]
In particular, for \(0<r_1<r_2\) on either fixed side of the origin, the conditional law at \(r_2\) is the conditional law at \(r_1\) convolved with an independent \((r_2-r_1)/c_\sigma+J_{r_2-r_1}\). Thus the conditional termination time is strictly increasing in the usual stochastic order with terminal distance **on each ray**. Its conditional mean and variance are exactly affine in \(r\):
\[
 \begin{aligned}
 \mathbb E[T\mid X=\sigma r]&=-\frac{A_\sigma'(a)}{A_\sigma(a)}+r\left[\frac1{c_\sigma}+\frac H{2K}\left(\frac{a+b}{\Delta(a)}-1\right)\right],\\
 \operatorname{Var}(T\mid X=\sigma r)&=(\log A_\sigma)''(a)+\frac{rH\eta^2}{2K\Delta(a)^3}.
 \end{aligned}
\]
The continuous density of the posterior time starts after the ballistic lower limit \(r/c_\sigma\); it also has an atom there, of mass
\[
 \frac{1}{2c_\sigma A_\sigma(a)}\exp\left[-\frac{rH}{2K}\big((a+b)-\Delta(a)\big)\right].
\]

## Assumptions and scope
Take \(u,v,a,b\) arbitrary strictly positive real numbers. The velocity switches between \(+u\) and \(-v\) at events of an independent homogeneous Poisson process of rate \(b\). Its initial sign is \(+\) or \(-\), each with probability \(1/2\). Independently, an exponential clock of rate \(a\) stops the motion; observe its terminal position and infer the elapsed clock time. The model also describes direction changes marked for killing with probability \(p\in(0,1)\) at homogeneous rate \(\lambda>0\), on setting \(a=\lambda p\) and \(b=\lambda(1-p)\). The original motivation is the position/time law in arXiv:2610.15094; the genuinely asymmetric regime \(u\ne v\) is included and is the principal domain of the present result. All conditional statements refer to regular conditional distributions given the continuously distributed terminal position; the displayed version is defined for all \(r>0\).

## Proof
**1. Fourier-Laplace resolvent.** For \(q>0\) and real \(k\), let \(Y_t\) be the freely moving telegraph position before killing. Its velocity-state Fourier generator is
\[
 M(k)=\begin{pmatrix}ik u-b&b\\b&-ikv-b\end{pmatrix}.
\]
A two-by-two inversion, averaged over the two initial states, yields
\[
 \int_0^\infty e^{-qt}\mathbb E(e^{ikY_t})\,dt
 =\frac{q+2b-ikd/2}{q(q+2b)-ikd(q+b)+Kk^2}.
\]
Let \(f_s(x)\,dx=\mathbb E[e^{-sT};X\in dx]\) for \(s\ge0\). Independence and exponentiality of termination give the Fourier transform of \(f_s\) as \(a\) times this expression with \(q=a+s\). Factor the quadratic denominator as
\[
 K(\zeta_+(q)-ik)(\zeta_-(q)+ik),\quad
 \zeta_+(q)\zeta_-(q)=q(q+2b)/K,\quad
 \zeta_+(q)-\zeta_-(q)=-d(q+b)/K.
\]
Both \(\zeta_\pm(q)\) are strictly positive for \(q>0\). Partial fractions and bilateral Fourier inversion yield
\[
 f_s(\sigma r)=a A_\sigma(a+s)e^{-r\zeta_\sigma(a+s)},\qquad \sigma\in\{+,-\},\ r>0.
\]
Consequently the conditional Laplace transform is exactly
\[
 \mathbb E[e^{-sT}\mid X=\sigma r]=
 \frac{A_\sigma(a+s)}{A_\sigma(a)}
 \exp\left[-r\big(\zeta_\sigma(a+s)-\zeta_\sigma(a)\big)\right].\tag{1}
\]

**2. The base factor is a probability transform.** For \(z>\eta\), the standard Bessel-Laplace identities are
\[
 \int_0^\infty e^{-zt}I_0(\eta t)\,dt=(z^2-\eta^2)^{-1/2},\quad
 \int_0^\infty e^{-zt}\eta I_1(\eta t)\,dt=z(z^2-\eta^2)^{-1/2}-1.
\]
Since \(a+b>\eta\) (indeed \(\eta\le b<a+b\)), these give
\[
 A_\sigma(q)=\frac1{2c_\sigma}+\int_0^\infty e^{-(q+b)t}
 \left[\frac{H\eta}{4K}I_1(\eta t)+\frac bH I_0(\eta t)\right]dt.
\]
Thus \(A_\sigma(a+s)/A_\sigma(a)\) is exactly the Laplace transform of the stated \(U_\sigma\). The base law is normalized and nonnegative; it has a positive atom at zero.

**3. The spatial factor is a drift-plus-compound-Poisson transform.** Differentiate the exponent:
\[
 \zeta_\sigma'(q)=\frac1{c_\sigma}+\frac H{2K}\left(\frac{q+b}{\Delta(q)}-1\right)
 =\frac1{c_\sigma}+\frac H{2K}\int_0^\infty e^{-(q+b)t}\eta I_1(\eta t)\,dt.
\]
Integrating from \(q=a\) to \(a+s\) and applying Tonelli gives
\[
 \zeta_\sigma(a+s)-\zeta_\sigma(a)
 =\frac s{c_\sigma}+\int_0^\infty(1-e^{-st})\,\nu(dt).
\]
The measure \(\nu\) is nonnegative. The Bessel expansion at zero and its large-argument exponential bound show it has finite total mass. More explicitly,
\[
 \nu((0,\infty))=\frac H{2K}\big(a+b-\Delta(a)\big)>0.
\]
Hence the spatial factor in (1) is the Laplace transform of \(r/c_\sigma+J_r\), with \(J\) a compound-Poisson subordinator. Combining this with the independent base factor proves the theorem.

**4. Consequences.** Stationary independent increments of \(J\) give the convolution identity, including strict stochastic ordering because the added ballistic delay is positive. The zero-jump event together with the atom of \(U_\sigma\) gives the stated ballistic atom. Differentiating the logarithm of (1) at \(s=0\) gives the affine conditional mean and variance, using
\(\zeta_\sigma''(a)=-H\eta^2/(2K\Delta(a)^3)\). All moments exist, as the conditional transforms are analytic near zero.

## Verification
A standalone script `verify.py` computes the exact two-state Fourier resolvent and compares it with independent integration of the established fixed-time asymmetric telegraph Bessel density and the ballistic contribution. It tests both terminal-position signs and multiple Laplace parameters in several asymmetric parameter regimes. Numerical quadrature is corroboration; the full infinite-family assertion follows from the resolvent, Bessel identities, positivity and Lévy–Khintchine calculation above.

## Relationship to prior work
Orsingher and Marchione (2026, arXiv:2610.15094v1) established the symmetric-speed killed-telegraph terminal-position distribution and joint time/position law, including the singular ballistic component; these are not newly claimed here. Ratanov (2021, arXiv:2102.04905v1, §1) gave fixed-time Bessel densities for general asymmetric telegraph motions. Cinque (2022, arXiv:2202.01904v1, §2) studied conditional distributions given initial velocity and switch counts. Their fixed-time kernels are compatible with this calculation and can be integrated against an exponential clock; the present separately identified contribution is the **explicit spatial compound-Poisson posterior factorization with a common Lévy jump kernel and side-dependent base laws**, yielding exact stochastic order and affine posterior moment laws across a continuum of terminal positions. It is not asserted that the classical resolvent or Bessel identities are new.

## Limitations
The result assumes positive, constant switching and killing rates, exponential killing independent of the velocity chain, initially equiprobable signs, and two velocities of opposite signs. It does not classify arbitrary velocity-dependent termination, nonexponential stopping laws, or higher-dimensional random flights. Historical coverage by a general Markov-additive Wiener–Hopf decomposition remains a priority risk; independent scientific validation has not been performed.

## References
1. E. Orsingher and M. M. Marchione, *Killing random motions with finite velocity*, arXiv:2610.15094v1, first submitted 2026-10-10, Sections 2–4, especially Equation (48). https://arxiv.org/html/2610.15094v1
2. N. Ratanov, *On telegraph processes, their first passage times and running extrema*, arXiv:2102.04905v1 (2021), Section 1, Equations (1.4)–(1.7). https://arxiv.org/html/2102.04905v1
3. F. Cinque, *A Note on the Conditional Probabilities of the Telegraph Process*, arXiv:2202.01904v1 (2022), Section 2. https://arxiv.org/html/2202.01904v1
