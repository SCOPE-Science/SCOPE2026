# A cosine-integral boundary for the second harmonic of odd-cycle distance powers

## Finding

Let \(N=2m+1\ge5\) be odd and equip the cyclic group \(\mathbb Z/N\mathbb Z\) with its graph distance \(d_N(j,k)=\min(|j-k|,N-|j-k|)\). The real Fourier multiplier of the powered distance matrix on the frequency-two character is
\[
 F_N(s)=2\sum_{r=1}^{m}r^s\cos(4\pi r/N),\qquad s\ge0.
\]
There is exactly one \(\sigma_N\in(1,2)\) such that \(F_N(\sigma_N)=0\). Moreover \(F_N(s)<0\) for \(0\le s<\sigma_N\), and \(F_N(s)>0\) for \(s>\sigma_N\). Its asymptotic transition scale is
\[
 \lim_{\substack{N\to\infty\\N\ \mathrm{odd}}}N^2(\sigma_N-1)
 =\frac{2\pi^2}{\gamma+\log(2\pi)-\operatorname{Ci}(2\pi)}
 =8.0976273568665367\ldots.
\]
Consequently the powered cyclic distance is not conditionally negative definite at any \(s>\sigma_N\), and \(\exp(-t d_N(j,k)^s)\) fails positive definiteness for all sufficiently small \(t>0\). In particular, the supremal negative-type exponent \(\wp(C_N)\) obeys \(\wp(C_N)\le\sigma_N\), and
\[
 \limsup_{\substack{N\to\infty\\N\ \mathrm{odd}}}
 N^2(\wp(C_N)-1)
 \le\frac{2\pi^2}{\gamma+\log(2\pi)-\operatorname{Ci}(2\pi)}.
\]
The root is exactly \(\sigma_5=\log_2((3+\sqrt5)/2)\).

## Assumptions and scope

All cyclic distances are shortest path lengths measured in unit edges. The diagonal of each powered distance matrix is zero for every \(s\ge0\), including \(s=0\). For \(r\ge1\) use the ordinary real power \(r^s\). Fourier multipliers are unnormalized character sums, and the frequency-two character is \(j\mapsto\exp(4\pi i j/N)\). The claims hold simultaneously for every odd integer \(N\ge5\). The statement concerns this single, canonically specified Fourier sector; it does not identify the first failing sector among *all* nontrivial frequencies.

## Proof

The character eigenvalue is the displayed multiplier because the distance matrix is real symmetric and circulant. Geometric differentiation of \(\sum_{r=1}^{m}z^r\), evaluated at \(z=\exp(4\pi i/N)\), yields the three exact identities
\[
 F_N(0)=-1,\qquad
 F_N(1)=-\frac1{4\cos^2(\pi/N)},\qquad
 F_N(2)=\frac{N\cos(2\pi/N)}{2\sin^2(2\pi/N)}.
\]
Thus the multiplier is negative at exponents zero and one, and positive at exponent two. For \(N=5,7\), the ordered coefficients \(2\cos(4\pi r/N)\), indexed by increasing \(r\), have exactly one sign change (negative to positive). For every odd \(N\ge9\), they have exactly two sign changes (positive, negative, positive); none is zero, since odd \(N\) cannot satisfy \(4r/N\equiv1/2\pmod1\). The generalized Descartes rule for an exponential polynomial \(\sum_r a_r\exp(s\log r)\) gives at most as many real zeros, counted with multiplicity, as sign changes of the nonzero ordered coefficients. For completeness, divide by the smallest exponential to obtain a function \(g\) with finite nonzero limit \(a_1\) at negative infinity. Its derivative is an exponential sum whose ordered signs are those of \(a_2,\ldots,a_m\). By induction its zeros number at most the sign changes in that tail. If \(a_1a_2<0\), Rolle's theorem gives at most one more zero of \(g\). If \(a_1a_2>0\), the initial derivative points away from zero, so any first zero of \(g\) requires a preceding derivative zero; then Rolle between successive zeros gives at most as many zeros as the derivative. Multiplicities are included by the usual generalized Rolle count. This proves exactly the sign-change bound. When \(N\ge9\), the limit as \(s\to-\infty\) is \(2\cos(4\pi/N)>0\); since \(F_N(0)=-1\), there is one negative root and, because \(F_N(1)<0<F_N(2)\), one root between one and two. The two-root upper bound proves they are the only real roots and both simple. For \(N=5,7\), the one-sign-change bound gives the same uniqueness on the nonnegative axis. The claimed signs follow by continuity and the signs at one and two.

For the asymptotic constant, differentiate at one:
\[
 F_N'(1)=2\sum_{r=1}^{m}r\log r\cos(4\pi r/N).
\]
Splitting \(\log r=\log N+\log(r/N)\), using the exact bounded value of \(F_N(1)\), and passing to a Riemann sum for the continuous function \(x\log x\cos(4\pi x)\) (taken zero at \(x=0\)) gives
\[
 \lim_{N\to\infty,\,N\text{ odd}}\frac{F_N'(1)}{N^2}
 =2\int_0^{1/2}x\log x\cos(4\pi x)\,dx
 =\frac{\gamma+\log(2\pi)-\operatorname{Ci}(2\pi)}{8\pi^2}=:L>0.
\]
Here \(\operatorname{Ci}(z)=\gamma+\log z+\int_0^z(\cos u-1)\,du/u\) for positive \(z\), and integration by parts yields the integral identity. Positivity follows also from \(\gamma+\log(2\pi)-\operatorname{Ci}(2\pi)=\int_0^{2\pi}(1-\cos u)\,du/u>0\).

Fix \(c>0\). Uniformly for \(1\le s\le1+c/N^2\), one has \(|F_N''(s)|=O(N^2\log^2N)\), simply by bounding the defining finite sum. Taylor's formula and \(F_N(1)\to-1/4\) therefore give
\[
 F_N(1+c/N^2)=-\frac14+cL+o(1).
\]
Bracketing the unique root with constants \(c\) on either side of \(1/(4L)\) proves the asserted limit. For \(N=5\), directly solve its two-term exponential sum to obtain \(2^{\sigma_5}=(3+\sqrt5)/2\).

Finally, the frequency-two real cosine vector has zero coordinate sum, while the quadratic form of the powered distance matrix equals \(F_N(s)\) times its positive squared norm. Therefore \(F_N(s)>0\) disproves conditional negative definiteness. Its exponential-kernel Fourier multiplier has value zero at \(t=0\) and derivative \(-F_N(s)<0\), proving negativity for all sufficiently small \(t>0\). These are genuine finite-group Fourier witnesses, not numerical inferences.

## Verification

The self-contained `checker.py` recalculates the exact low-exponent Fourier identities numerically at a collection of odd sizes, brackets each root by bisection, and examines the scaled transition. It separately checks a negative quadratic-form witness above the root. These finite checks support transcription, normalization, and arithmetic; the infinite-family assertions and asymptotic limit are proved analytically above.

## Relationship to prior work

Wolf, *On the gap of finite metric spaces of p-negative type* (arXiv:1008.0964v1, 2010), calculates the strict one-negative-type gap for cycle graphs; this supplies the motivation for determining how fast superunit obstructions approach one as odd cycle size grows. Sanchez, *On the supremal p-negative type of a finite metric space* (arXiv:1108.0451v1, 2011), supplies general determinant criteria for finite metric spaces, and Murugan, *Generalized roundness of vertex transitive graphs* (arXiv:1112.5657v1, 2011), studies vertex-transitive negative-type calculations. The present statement isolates the second cyclic Fourier character, proves its unique transition for every odd size, and identifies the cosine-integral asymptotic coefficient; it is not an assertion that the entire spectrum crosses at that character.

## Limitations

The bound on \(\wp(C_N)\) is an **upper bound**, not an equality claim for arbitrary \(N\). A different Fourier sector might fail sooner; no assertion about the complete positive-definiteness range of \(\exp(-t d_N^s)\) is made when \(s\le\sigma_N\). The root is described implicitly except at \(N=5\). The literature comparison is bounded, and independent mathematical validation has not been performed.

## References

- R. Wolf, *On the gap of finite metric spaces of p-negative type*, arXiv:1008.0964v1, first public 2010-08-05; https://arxiv.org/html/1008.0964v1 .
- S. Sanchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, first public 2011-08-02; https://arxiv.org/abs/1108.0451 .
- M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1, first public 2011-12-23; https://arxiv.org/abs/1112.5657 .
