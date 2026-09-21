# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was re-derived from normalized ball and sphere means. The key identity for a homogeneous polynomial \(Q\) of degree \(d\),
\[
A(Q,0,r)=\frac{n}{n+d}r^d\langle Q\rangle,
\]
was checked directly by radial integration.

The potentially delicate sign step is valid: if \(\Delta P_k\) is the first nonzero Taylor term of the nonnegative function \(\Delta v\), then \(\Delta P_k\ge0\) pointwise. Since it is not identically zero, its spherical average is positive, and
\[
\langle\Delta P_k\rangle=k(k+n-2)\langle P_k\rangle
\]
forces \(\langle P_k\rangle>0\).

Two asymptotic regimes were checked separately. If a nonharmonic Taylor term occurs at degree \(k<2m\), nonlinear exponential terms have not yet appeared and the leading coefficient is
\[
-\frac{pk}{n+k}\langle P_k\rangle<0.
\]
If all degrees below \(2m\) are harmonic, expansion through degree \(2m\) gives
\[
-\frac{2mp}{n+2m}\langle P_{2m}\rangle
+\frac p2\left(\frac{pn}{n+2m}-1\right)\langle P_m^2\rangle.
\]
The first term is nonpositive and the second is strictly negative for \(p<1+2m/n\). No cross-term of degree at most \(2m\) is missing: because \(m\) is the first positive Taylor degree, the only quadratic exponential contribution at degree \(2m\) is \(P_m^2/2\), and all higher exponential powers have degree \(>2m\).

As a consistency check, the \(m=1\) coefficient simplifies to
\[
-\frac{p((n+2-np)|\nabla v|^2+2\Delta v)}{2n(n+2)},
\]
matching Mochizuki's second-order computation. The sharpness example \(v=H_m\), with \(H_m\) a nonzero homogeneous harmonic polynomial, changes sign exactly at \(p=1+2m/n\) at leading order.

The statement deliberately assumes positivity near the point; zeros are not covered.

## Originality

PASS, to the best of our knowledge.

Mochizuki (2005) was inspected in full at the introduction, main theorem and Section 3 remarks. It explicitly calls the range \(1<p<(n+2)/n\) open, proves local validity under \(\Delta u(a)>0\), and proves that the closure of the bad-point set has no interior. No finite-order Taylor criterion or infinite-flatness obstruction is stated there.

Ekonen–Kinnunen–Marola–Sbordone (2009) was inspected at Theorem 2.3 and its references. Their global positive result has exponent \(n/(n-1)\). By \(L^p\)-mean monotonicity it covers all smaller exponents, but for \(n\ge3\) it does not reach the upper interval
\[
\frac{n}{n-1}<p<\frac{n+2}{n}.
\]
Their paper cites Mochizuki's 2005 paper, so this comparison is material rather than merely bibliographic.

Targeted searches covered the exact Mochizuki title, source terminology, `logarithmically subharmonic`, `real-analytic`, `finite jet`, `flat to infinite order`, `Pizzetti`, `volume mean`, `spherical mean`, and Beckenbach–Radó formulations. No prior statement equivalent to the finite-order threshold or the conclusion that a smooth bad positive point must be infinitely flat in \(\log u\) was located.

Residual risk remains because higher-order Pizzetti and spherical-mean expansions are classical and an equivalent observation may have been recorded under different terminology or in literature not indexed by these searches.

## Value

PASS.

The result turns Mochizuki's local intermediate-range question into a sharply constrained smooth problem. It completely removes bad positive points for real-analytic log-subharmonic functions and shows that any \(C^\infty\) counterexample must exploit infinite-order flatness. The stronger threshold \(1+2m/n\) records how the local admissible exponent improves with the first nonconstant jet, and harmonic homogeneous germs show that threshold is sharp away from its endpoint.

This is not merely the already-known global exponent \(n/(n-1)\): for \(n\ge3\) it reaches the entire remaining upper part of the original intermediate interval locally at every finite-order point.

## Limitations

- The theorem is local.
- Positivity near the point is required; zeros are not analyzed.
- Infinite-order-flat \(C^\infty\) germs remain unresolved.
- The endpoint \(p=1+2m/n\) remains undecided in general.
- The literature search is targeted rather than exhaustive, and equivalent prior coverage under higher-order mean-value/Pizzetti terminology remains possible.
- Independent audit has not been performed.
