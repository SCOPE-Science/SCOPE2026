# The exact limiting Gibbs overshoot for Krawtchouk interpolation of the sign function

## Finding
Let \(F_{2M}\) denote the symmetric Krawtchouk Fourier interpolation of the sign function at the \(2M+1\) integer nodes \(-M,-M+1,\ldots,M\), with \(\operatorname{sgn}(0)=0\). As established in the cited paper, the Fourier polynomial is the unique odd polynomial of degree at most \(2M-1\) with those values.

**Theorem.** As integers \(M\to\infty\), \(F_{2M}\) converges locally uniformly on \(\mathbb C\) to an entire odd function \(F\). For real \(x>0\),
\[
F(x)=1-\frac{\sin(\pi x)}{\pi}H(x),\qquad
H(x)=\int_0^1\frac{t^{x-1}(1-t)}{1+t}\,dt
=\psi\!\left(\frac{x+1}{2}\right)-\psi\!\left(\frac{x}{2}\right)-\frac1x.
\]
Here \(\psi\) denotes the digamma function. The **global real maximum** of the *limiting function* is uniquely attained at \(\xi\in(1,2)\) satisfying
\[
\pi\cot(\pi\xi)+\frac{H'(\xi)}{H(\xi)}=0.
\]
The exact limiting first-overshoot constant is
\[
\Gamma=1-\frac{\sin(\pi\xi)}{\pi}H(\xi)
\approx1.065783888266448099,\qquad
\xi\approx1.376991769203938866.
\]
In particular, \(\lim_{M\to\infty}\max_{1\le x\le2}F_{2M}(x)=\Gamma\). The above statement does **not** claim convergence of maxima on the expanding intervals \([-M,M]\).

## Assumptions and scope
Take integer \(M\ge1\). At each integer \(j\in[-M,M]\) prescribe the value \(\operatorname{sgn}(j)\). The Fourier expansion in any of the paper's shifted Krawtchouk bases agrees with the unique interpolating polynomial; the source proves this for the discrete measure and the full basis. In this theorem the infinite-degree limit is at a fixed complex point or uniformly on each fixed compact subset of \(\mathbb C\); no uniformity is asserted over unbounded \(x\).

## Proof
**1. Exact finite interpolation.** Put
\[
P_M(z)=\prod_{j=1}^M\left(1-\frac{z^2}{j^2}\right),\qquad
b_{M,k}=\frac{(M!)^2}{(M+k)!(M-k)!}\quad(1\le k\le M).
\]
Paired Lagrange cardinal terms at nodes \(k\) and \(-k\), whose values are \(1\) and \(-1\), respectively, give the exact polynomial identity
\[
F_{2M}(z)=2zP_M(z)\sum_{k=1}^M
\frac{(-1)^k b_{M,k}k}{z^2-k^2}.
\]
The apparent poles are removable because \(P_M(k)=0\). For example, \(M=1\) gives \(F_2(z)=z\), verifying the sign and factor. At integer nodes the formula has exactly the required interpolating values.

**2. Uniform convergence.** Euler's sine product gives \(P_M(z)\to P(z)=\sin(\pi z)/(\pi z)\) locally uniformly. For each fixed \(k\), \(b_{M,k}\to1\) as \(M\to\infty\). To control the remaining summands, for any compact disk \(|z|\le R\) and \(k>2R+2\), expand
\[
\frac{k}{z^2-k^2}=-\frac1k+O_R(k^{-3}).
\]
The sequence \(b_{M,k}/k\), extended as zero for \(k>M\), is nonincreasing in \(k\) because \(b_{M,k+1}/b_{M,k}=(M-k)/(M+k+1)\). The alternating-series bound and the absolutely convergent \(O_R(k^{-3})\) tail show uniformly in \(M\) that the tail from \(k=K\) is \(O_R(K^{-1})\). Consequently, away from the integers,
\[
F_{2M}(z)\longrightarrow
F(z)=\frac{2\sin(\pi z)}{\pi}
\sum_{k=1}^{\infty}\frac{(-1)^k k}{z^2-k^2}.
\]
The limit is entire: the same expression is the locally uniformly convergent paired cardinal series
\[
F(z)=\sum_{k=1}^{\infty}\bigl[\operatorname{sinc}(z-k)-\operatorname{sinc}(z+k)\bigr],
\quad \operatorname{sinc}(z)=\frac{\sin(\pi z)}{\pi z},
\]
whose apparent poles are removable. Around each integer, the differences \(F_{2M}-F\) are holomorphic; convergence on a small surrounding circle and the maximum-modulus principle extend the convergence uniformly to the enclosed disk. Hence the convergence is locally uniform on all of \(\mathbb C\).

**3. Positive-real profile.** The classical cardinal partition of unity, derivable from the partial-fraction formula for \(\pi\csc(\pi z)\), is \(\sum_{k\in\mathbb Z}\operatorname{sinc}(x-k)=1\), with symmetric summation. Rearranging the paired cardinal series yields for \(x>0\)
\[
F(x)=1-\frac{\sin(\pi x)}{\pi}
\left[\frac1x+2\sum_{j=1}^\infty\frac{(-1)^j}{x+j}\right].
\]
The bracket is \(H(x)=\sum_{j\ge0}(-1)^j/[(x+j)(x+j+1)]\). Integrating the geometric series \(1/(1+t)=\sum_{j\ge0}(-t)^j\) on \((0,1)\) gives the displayed positive integral representation. The digamma expression follows from the standard alternating harmonic sum. In particular \(H(x)>0\), \(H'(x)<0\), and \(F\) agrees with \(\operatorname{sgn}\) at integer nodes.

**4. Sharp first lobe and uniqueness.** For \(x>0\), \(0<H(x)<1/x\). Thus \(F(x)>0\) (also when \(\sin(\pi x)>0\)); moreover \(F(x)>1\) exactly when \(\sin(\pi x)<0\), namely on the intervals \((2j+1,2j+2)\), \(j\ge0\). If \(x\in(2j+1,2j+2)\) with \(j\ge1\), then \(y=x-2j\in(1,2)\) has the same sine and \(H(y)>H(x)\); hence \(F(y)>F(x)\). Oddness excludes a larger positive value on the negative real axis. Therefore the global real maximum lies in \((1,2)\).

On this interval maximize \(G(x)=-\sin(\pi x)H(x)>0\). The bounds
\[
H(x)\ge\frac1{2x(x+1)},\qquad
0\le H''(x)\le\frac2{x^3}
\]
follow directly from \(\tfrac12(1-t)\le(1-t)/(1+t)\le1\) and elementary beta integrals. Thus, for \(x\ge1\),
\[
(\log H)''=\frac{H''}{H}-\left(\frac{H'}H\right)^2
\le\frac{4(x+1)}{x^2}\le8<\pi^2.
\]
Since \((\log[-\sin(\pi x)])''=-\pi^2\csc^2(\pi x)\le-\pi^2\), the function \(\log G\) is strictly concave on \((1,2)\). It tends to \(-\infty\) at both ends, and therefore has a unique maximizer. Differentiation gives the stated stationary equation. Finally, locally uniform convergence implies uniform convergence on \([1,2]\), hence convergence of the first-lobe maxima to \(\Gamma\).

## Verification
All steps are analytic: exact Lagrange weights, uniformly controlled alternating-series tails, Euler's sine product, elementary beta integrals, and a strict global logarithmic-concavity bound. The standalone Python checker evaluates finite Lagrange representations, compares them with the limiting profile, and numerically confirms the unique critical point. No finite calculation is used as proof of local uniform convergence or global uniqueness.

## Relationship to prior work
Cullinan and Young, *The Gibbs phenomenon for the Krawtchouk polynomials* (arXiv:2603.05408v1, first public 2026-03-05), proved that the finite Krawtchouk expansion is precisely the sign-interpolating polynomial (Proposition 6), computed the limiting derivative at zero (Theorem 4), and supplied numerical first-overshoot values near \(1.066\). Their page 4 expressly notes that they did not prove an exact limiting Gibbs constant. The present theorem identifies the entire locally uniform limit, derives the explicit positive-integral profile, and proves its unique sharp global real overshoot. Classical cardinal-sine interpolation and the digamma alternating sum are used as established identities; they are not claimed as new.

## Limitations
The constant \(\Gamma\) is the **global maximum of the limiting entire function** and the limit of finite maxima over the **fixed first lobe** \([1,2]\). This theorem alone does not prove that the global maxima of the finite-degree interpolants over their growing intervals \([-M,M]\) converge to \(\Gamma\), nor give rates uniform in growing spatial windows. Numerical decimals are approximations; the implicit integral/root characterization is exact.

## References
- J. Cullinan and E. Young, *The Gibbs phenomenon for the Krawtchouk polynomials*, arXiv:2603.05408v1 (first available 2026-03-05), Proposition 6, Section 2, Theorem 4, pages 4–6, and numerical overshoot table, https://arxiv.org/abs/2603.05408.
- Classical Euler sine product and Mittag–Leffler partial fraction for \(\pi\csc(\pi z)\); identities used in the proof.
