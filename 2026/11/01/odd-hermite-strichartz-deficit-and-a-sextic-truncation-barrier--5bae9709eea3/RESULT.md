# Odd-Hermite Strichartz deficit and a sextic truncation barrier

## Finding

For the one-dimensional free Schrödinger propagator \(U(t)=e^{it\partial_x^2}\), set
\[
\mathcal S(f)=\frac{\|U(t)f\|_{L_t^8(\mathbb R;L_x^4(\mathbb R))}^{8}}{\|f\|_{L^2(\mathbb R)}^8},\qquad f\ne0.
\]
Let \(h_n\) be the real \(L^2\)-normalized physicists' Hermite functions defined below. The following is a linked sharp finite-band result, not a bound for all odd data.

**Exact first-two-mode theorem.** For every \((a,b)\in\mathbb C^2\setminus\{(0,0)\}\), let \(f=ah_1+bh_3\) and \(s=|b|^2/(|a|^2+|b|^2)\). Then, independently of the relative coefficient phase,
\[
\boxed{\mathcal S(f)=\frac{3}{262144}\bigl(12288-11520s^2+8960s^3-2525s^4\bigr).}
\]
In particular \(\mathcal S(f)\le9/64\), with equality exactly when \(b=0\). The following fourth-order stability inequality has the **largest possible uniform coefficient**:
\[
\boxed{\mathcal S(f)\le\frac9{64}-\frac{15255}{262144}\,s^2.}
\]
Equality in this stability inequality holds exactly when \(s=0\) or \(s=1\). Near \(h_1\), the exact local deficit coefficient is \(135/1024\):
\[
\frac9{64}-\mathcal S(h_1+\varepsilon h_3)
=\frac{135}{1024}|\varepsilon|^4+O(|\varepsilon|^6).
\]

**First transverse three-mode correction.** For each fixed \(\lambda\in\mathbb C\) and real \(\varepsilon\), define the unit vector
\[
f_{\varepsilon,\lambda}
=\frac{h_1+\varepsilon h_3+\lambda\varepsilon^2 h_5}
{(1+\varepsilon^2+|\lambda|^2\varepsilon^4)^{1/2}}.
\]
The optimal cancellation of its fourth-order deficit is unique:
\[
\boxed{\mathcal S(f_{\varepsilon,\lambda})
=\frac9{64}-\frac{81}{512}\left|\lambda-\frac{\sqrt{30}}6\right|^2\varepsilon^4
+O_\lambda(\varepsilon^6).}
\]
At the unique cancellation parameter \(\lambda_0=\sqrt{30}/6\), the first nonzero deficit instead has **strictly positive sixth-order coefficient**:
\[
\boxed{\mathcal S(f_{\varepsilon,\lambda_0})
=\frac9{64}-\frac{525}{4096}\varepsilon^6+O(\varepsilon^8).}
\]
Thus the first two odd Hermite modes have a sharp quartic deficit, while the natural second-order correction in the next odd mode cancels that term but cannot remove the sextic loss along this specified curve.

## Assumptions and scope

Use Lebesgue measure on the spatial and temporal real lines, the unscaled Laplacian \(\partial_x^2\), and
\[
h_n(x)=\frac{H_n(x)e^{-x^2/2}}{\pi^{1/4}\sqrt{2^n n!}},
\qquad H_n(x)=(-1)^n e^{x^2}\frac{d^n}{dx^n}e^{-x^2}.
\]
All parameters in the first theorem may be complex. In the asymptotic theorem \(\varepsilon\) is real, \(\lambda\) is fixed complex, and the implied constants may depend on it. The results concern only the displayed finite-dimensional odd Hermite families. No global odd-data sharp Strichartz constant is asserted.

## Proof

**1. The exact lens identity.** Set \(\theta=\arctan(2t)\), \(-\pi/2<\theta<\pi/2\), and \(\mathsf H=-\partial_x^2+x^2\). The standard lens transform, with spatial Jacobian included, gives
\[
\int_{\mathbb R}\!\left(\int_{\mathbb R}|e^{it\partial_x^2}f(x)|^4dx\right)^2dt
=\frac12\int_{-\pi/2}^{\pi/2}\!\left(\int_{\mathbb R}|e^{-i\theta\mathsf H/2}f(x)|^4dx\right)^2d\theta.
\]
Since \(\mathsf Hh_n=(2n+1)h_n\), the relative phases of \(h_1,h_3,h_5\) are \(1,e^{-2i\theta},e^{-4i\theta}\). Thus \(z=e^{-2i\theta}\) ranges over exactly one full unit circle, and the right side is \(\pi/2\) times the constant Fourier coefficient of the square of the spatial fourth moment. This is an equality, not an asymptotic approximation.

**2. Explicit first-two-mode moments.** Direct Gaussian integration gives
\[
\begin{array}{c|ccccc}
&\int h_1^4&\int h_3^4&\int h_1^2h_3^2&\int h_1^3h_3&\int h_1h_3^3\\ \hline
\text{value}&\dfrac{3\sqrt2}{8\sqrt\pi}&\dfrac{147\sqrt2}{512\sqrt\pi}&\dfrac{11\sqrt2}{64\sqrt\pi}&-\dfrac{\sqrt3}{16\sqrt\pi}&\dfrac{3\sqrt3}{128\sqrt\pi}
\end{array}
\]
Write \(A,B,C,D,E\) for these five numbers in order, put \(u=1-s\), and remove the irrelevant common phase of \(a\). For \(\alpha=\sqrt u\), \(\beta=\sqrt s\), the fourth spatial moment of \(\alpha h_1+\beta e^{i\phi}h_3\) is
\[
I(\phi)=U+V\cos\phi+W\cos(2\phi),
\quad U=u^2A+s^2B+4usC,
\quad V=4\sqrt{us}(uD+sE),\quad W=2usC.
\]
The temporal mean of \(I^2\) is \(U^2+(V^2+W^2)/2\). Inserting the exact five moments yields the displayed polynomial. Its derivative is
\[
\frac{d\mathcal S}{ds}
=-\frac{15s}{65536}(505s^2-1344s+1152).
\]
The quadratic is strictly positive on \(\mathbb R\) because its discriminant is \(-520704\). Thus \(\mathcal S\) is strictly decreasing for \(0<s\le1\). Furthermore,
\[
\frac{9/64-\mathcal S}{s^2}
=\frac3{262144}(11520-8960s+2525s^2)
\]
is strictly decreasing on \([0,1]\), and its value at \(s=1\) is \(15255/262144\). This proves the equality cases and sharp uniform fourth-order stability coefficient. Its limit at \(s=0\) is \(135/1024\), giving the local expansion.

**3. Three-mode normal form and sextic coefficient.** Substitute \(h_1+\varepsilon zh_3+\lambda\varepsilon^2z^2h_5\) into the spatial fourth moment, square the result, and select the constant \(z\)-Fourier coefficient. Every coefficient is a finite Gaussian moment. The sole integration rule needed is
\[
\int_{\mathbb R}x^{2m}e^{-2x^2}\,dx
=\sqrt{\frac\pi2}\frac{(2m-1)!!}{4^m},\qquad m\ge0,
\]
with \((-1)!!=1\). Divide by \((1+\varepsilon^2+|\lambda|^2\varepsilon^4)^4\). Exact coefficient extraction gives
\[
[\varepsilon^0]\mathcal S=\frac9{64},\quad
[\varepsilon^2]\mathcal S=0,\quad
[\varepsilon^4]\mathcal S=-\frac{81}{512}\left|\lambda-\frac{\sqrt{30}}6\right|^2.
\]
At the unique zero of the fourth coefficient,
\[
[\varepsilon^6]\mathcal S=-\frac{525}{4096},\qquad
[\varepsilon^8]\mathcal S=\frac{105}{1048576}.
\]
The coefficient identities follow by elementary polynomial multiplication using the stated moment rule; an independent executable symbolic expansion is supplied in `CHECK.py`. For fixed \(\lambda\), the entire expression is a rational function of \(\varepsilon\) with denominator positive near zero. The temporal Fourier symmetry makes it even in real \(\varepsilon\), so the stated remainder orders follow. The unique quartic cancellation agrees with the second-order \(h_5\) coefficient on the unitary dilation orbit through \(h_1\), which is why a fourth-order normal form has a flat symmetry direction.

## Verification

Execute `python CHECK.py` with Python 3 and SymPy. The code uses the exact Gaussian moment formula above, performs phase-harmonic convolution through order eight, and checks exact identities over rational numbers and radicals; no approximate integration enters the certificates. Independent Gauss–Hermite spatial and periodic phase quadrature at several small real \(\varepsilon\) also agrees with the sextic coefficient; that supplementary numerical test is not used as proof.

## Relationship to prior work

Gonçalves (2017), especially Theorem 1, supplies the general Hermite/lens-transform representation; that underlying method is not claimed as new. Gonçalves and Zagier (2021) determine the parity-restricted sharp *\(L^6_{t,x}\)* constant, and identify the mixed \(L_t^8L_x^4\) parity-projected operator as harder to diagonalize. Suzuki (October 22, 2026) proves an optimal sharpening for **even** initial data, not the odd family here. Gonçalves, Negro and Oliveira e Silva (September 10, 2026) determine Gaussian-centered stability, not this odd-centered finite-band normal form. The present claim is the explicit sharp nonlinear two-mode profile and the optimized quartic-to-sextic three-mode transition, not a new lens identity or a solution of the unrestricted odd problem.

## Limitations

The exact maximum is proved only on \(\operatorname{span}_{\mathbb C}\{h_1,h_3\}\). The three-mode assertion is local along the parameterized paths and does **not** establish a global maximum on \(\operatorname{span}\{h_1,h_3,h_5\}\). In particular, the unrestricted sharp \(L_t^8L_x^4\) constant for all odd initial data is not proved. A general all-data Hermite formula predates this result; its possible interpretation as implicit coverage is an originality risk despite the absence of a located statement of the optimized local coefficients. No independent verification has been performed.

## References

1. Soichiro Suzuki, *A sharpened \(L_t^8L_x^4\)-Strichartz estimate for even initial data*, arXiv:2610.31543v1 (2026-10-22), https://arxiv.org/abs/2610.31543.
2. Felipe Gonçalves, Giuseppe Negro, Diogo Oliveira e Silva, *Gaussians Do Not Always Maximize Mixed-Norm Strichartz Inequalities for the Schrödinger Equation*, arXiv:2609.11644v1 (2026-09-10), https://arxiv.org/abs/2609.11644.
3. Felipe Gonçalves and Don Zagier, *Strichartz estimates with broken symmetries*, Rev. Mat. Iberoam. 38 (2022), 1709–1722, https://doi.org/10.4171/RMI/1322 (first public 2021).
4. Felipe Gonçalves, *Orthogonal Polynomials and Sharp Estimates for the Schrödinger Equation*, arXiv:1702.08510 (2017), https://arxiv.org/abs/1702.08510.
