# A sharp inverse-index law for distant zero flips of a bandlimited sinc profile

## Finding

Fix \(B>0\) and \(y>0\). Define the entire function
\[
f_{B,y}(z)=\frac{\sin(\pi B(z-iy))}{\pi(z-iy)},
\]
with the removable value at \(z=iy\), and let \(a_n=n/B+iy\) for integers \(n\ge1\). With the Fourier convention \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i t\xi}\,dt\),
\[
\widehat f_{B,y}(\xi)=e^{2\pi y\xi}\mathbf 1_{[-B/2,B/2]}(\xi),
\]
so \(f_{B,y}\in PW_{B/2}\) and \(f_{B,y}(a_n)=0\). Let \(\mathfrak F_a\) be the standard zero-flipping operation
\[
(\mathfrak F_a f)(t)=\frac{1-t/\bar a}{1-t/a}e^{t/\bar a-t/a}f(t),\qquad t\in\mathbb R.
\]
Then
\[
\boxed{\lim_{n\to\infty}n^2\inf_{|c|=1}\|\mathfrak F_{a_n}f_{B,y}-cf_{B,y}\|_2^2
=\frac{2B^2y}{\pi}\left(2\cosh(2\pi By)-e^{-2\pi By}\right).}
\]
The coefficient is positive for every fixed \(B,y>0\). Thus the phase-optimized distance is asymptotic to a nonzero constant times \(n^{-1}\), with an explicit leading coefficient.

## Assumptions and scope

The parameters \(B\) and \(y\) are fixed positive real numbers, and \(n\) tends to infinity through positive integers. The zero-flip is performed at a genuine zero \(a_n\), so \(\mathfrak F_{a_n}f_{B,y}\) remains in the same Paley–Wiener class. The result concerns this single canonical bandlimited profile. It does not assert a uniform limit in \(B\) or \(y\), a statement at \(y=0\), or a sharp estimate for all functions in \(PW_{B/2}\).

## Proof

Write \(x=n/B\), \(a=x+iy\), and
\[
w(t)=|f_{B,y}(t)|^2=\frac{\sin^2(\pi Bt)+\sinh^2(\pi By)}{\pi^2(t^2+y^2)}.
\]
The multiplier \(m_x(t)=(1-t/\bar a)(1-t/a)^{-1}e^{t/\bar a-t/a}\) has unit modulus on the real axis. Set \(R_x(t)=\frac{a}{\bar a}\frac{\bar a-t}{a-t}\). Direct algebra gives
\[
R_x(t)-1=\frac{-2iyt}{\bar a(a-t)},\qquad m_x(t)=R_x(t)e^{2iyt/(x^2+y^2)}.
\]
The raw squared distance is \(Q_x=\int_{\mathbb R}|m_x(t)-1|^2w(t)\,dt\).

There are two contributions at order \(x^{-2}\). First, in the boundary layer \(t=x+s\) with fixed \(s\), one has
\[
m_x(x+s)\longrightarrow\frac{s+iy}{s-iy},\qquad
x^2w(x+s)\longrightarrow\frac{\sin^2(\pi Bs)+\sinh^2(\pi By)}{\pi^2}.
\]
Consequently the contribution from this layer, after first taking \(x\to\infty\) and then enlarging the layer, is
\[
\frac{4y^2}{\pi^2}\int_{\mathbb R}\frac{\sin^2(\pi Bs)+\sinh^2(\pi By)}{s^2+y^2}\,ds
=\frac{2y}{\pi}\left(\cosh(2\pi By)-e^{-2\pi By}\right),
\]
using \(\int_{\mathbb R}(s^2+y^2)^{-1}ds=\pi/y\) and \(\int_{\mathbb R}\cos(2\pi Bs)(s^2+y^2)^{-1}ds=(\pi/y)e^{-2\pi By}\).

Second, away from that layer the rational factor contributes \(o(x^{-2})\) to \(Q_x\). For the exponential factor, rescale \(t=x^2u\). On compact intervals bounded away from \(u=0\), the oscillatory numerator in \(w(x^2u)\) averages to \(\tfrac12+\sinh^2(\pi By)=\tfrac12\cosh(2\pi By)\). The resulting contribution is
\[
\frac{\cosh(2\pi By)}{2\pi^2}\int_{\mathbb R}\frac{|e^{2iyu}-1|^2}{u^2}\,du
=\frac{2y}{\pi}\cosh(2\pi By),
\]
where \(\int_{\mathbb R}|e^{-iku}-1|^2u^{-2}du=2\pi|k|\). The omitted region \(|u|<\varepsilon\) is bounded by \(O(\varepsilon)\) after multiplying by \(x^2\), and the tails \(|u|>U\) by \(O(U^{-1})\). The identity for \(R_x-1\) above bounds the rational-factor remainder outside the boundary layer; the layer tail is \(O(R^{-1})\) when \(|s|>R\). These estimates justify the two-scale decomposition and yield
\[
\lim_{n\to\infty}x^2Q_x=\frac{2y}{\pi}\left(2\cosh(2\pi By)-e^{-2\pi By}\right).
\]

Finally, put \(I_x=\int_{\mathbb R}m_x(t)w(t)\,dt\) and \(N=\|f_{B,y}\|_2^2=\sinh(2\pi By)/(2\pi y)>0\). Then \(Q_x=2(N-\operatorname{Re}I_x)\), whereas the phase-optimized squared distance is \(2(N-|I_x|)\). Splitting the integral at \(|t-x|=R\), \(|t|=x/2\), and \(|t|=x^2\), the displayed bounds on \(R_x-1\) and the exponential multiplier give \(\operatorname{Im}I_x=O(\log x/x^2)\). Hence
\[
Q_x-2(N-|I_x|)=2(|I_x|-\operatorname{Re}I_x)=O((\log x)^2/x^4)=o(x^{-2}).
\]
The phase optimization therefore leaves the leading coefficient unchanged. Since \(x=n/B\), multiplying the limit by \(B^2\) gives the stated formula. No numerical experiment is used as a proof.

## Verification

The Fourier representation follows by integrating \(e^{2\pi y\xi}e^{2\pi i\xi z}\) over \([-B/2,B/2]\). The zero locations and the zero-flip multiplier are explicit. The two leading contributions are the rational-factor boundary layer near \(t=n/B\) and the exponential-factor scale \(t\asymp n^2/B^2\); the proof bounds the remaining regions and then removes the cutoffs. The global-phase correction is lower order. The result is an asymptotic theorem for fixed parameters, not a finite-index identity.

## Relationship to prior work

Jaming, Kellay, and Perez study zero-flipping in the Paley–Wiener class, give the multiplier formula, and prove general stability/instability estimates. Their results motivate the phase-optimized distance used here. The statement above is a different, explicit high-index asymptotic for the particular shifted-sinc profile: it identifies the exact leading constant when the real parts of its zeros tend to infinity while the imaginary part stays fixed. It does not claim a general asymptotic for arbitrary bandlimited signals.

## Limitations

The proof holds for fixed \(B>0\) and \(y>0\). It does not establish uniformity as \(y\downarrow0\), cover nonuniformly spaced zeros, or improve the general stability bounds for every member of a Paley–Wiener space. The asymptotic coefficient depends on the chosen profile and zero-flip normalization. An independent mathematical audit has not been performed.

## References

1. P. Jaming, K. Kellay, and R. Perez III, “On the effect of zero-flipping on the stability of the phase retrieval problem in the Paley–Wiener class,” arXiv:2103.05937 (first public version: 10 March 2021), especially the zero-flipping definition and stability estimates in Section 3. https://arxiv.org/abs/2103.05937
2. P. Jaming, K. Kellay, and R. Perez III, published version, *Monatshefte für Mathematik* 198 (2022), 757–776. https://doi.org/10.1007/s00605-022-01716-y
