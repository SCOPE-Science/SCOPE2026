# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked at the endpoint cases \(s=0\), \(s=r_d\), and \(u=0\), as well as for the open parameter ranges.

For \(s>0\), with \(\nu=(d-1)/2\) and
\[
g_s(t)=(2\pi)^\nu s^{-\nu}t^\nu J_\nu(st),
\]
standard Bessel recurrences give
\[
g_s''(t)
=(2\pi)^\nu s^{1-\nu}t^{\nu-1}
\bigl((2\nu-1)J_{\nu-1}(st)-stJ_\nu(st)\bigr).
\]
Thus the least positive zero \(r_d\) of the displayed Bessel combination makes the slice kernel convex for every \(0\le s\le r_d\). The endpoint conditions \(q_s(1)=q_s'(1)=0\) hold because \(d-1\ge2\). Extension by zero is therefore convex and \(C^1\).

For a compactly supported nonnegative convex kernel \(q\), \(w=-q'\) is nonnegative and nonincreasing. Pairing adjacent positive and negative half-periods in the sine transform gives
\[
\int_0^\infty w(x)\sin(ux)\,dx>0
\]
for every \(u>0\); integration by parts then gives strict positivity of the cosine transform. This supplies a direct proof of the Pólya-type positivity criterion used here, so no unstated regularity theorem is needed.

Existence of \(r_d\) follows from the positive small-\(z\) expansion of the Bessel combination and its negative value at \(j_{\nu-1,1}\), using standard zero interlacing \(j_{\nu-1,1}<j_{\nu,1}\).

The dimension-three fixed-pair certification is deliberately independent of floating-point numerics. The alternating Bessel series gives \(r_3>5/4\), while the elementary half-integer formula gives \(j_{3/2,1}<23/5\). Consequently
\[
A_3<2\left(\frac{23/5}{5/4}\right)^3=99.672064<100.
\]
The displayed decimal values of \(r_3\) and \(A_3\) are informational only and are not used in the proof.

## Originality

The closest source inspected in full was Gómez-Serrano–Levitin–Platt–Polterovich, arXiv:2609.10517. Its Section 2 proves existence of a dimension-dependent strip \(0\le s\le\sigma_d\), and Remark 2.4 explains how constants could be extracted from that proof but explicitly does not record them. The following remark reports non-rigorous \(\alpha=100\) values and leaves rigorous fixed-pair certification to future work by two-variable interval arithmetic. The paper does not invoke the convex-kernel Fourier-positivity route used here; searches within the accessible text found no occurrence of Tuck's criterion.

Tuck (2006) proves the general fact that suitable convex functions have positive cosine transforms. That classical theorem covers the harmonic-analysis mechanism but does not identify the bipyramid slice kernel, the Bessel combination \(H_\nu\), the strip radius \(r_d\), or the geometric threshold \(A_d\).

Targeted searches used the source title and arXiv identifier together with terms including "Pólya", "Bessel", "bipyramid", "explicit sigma", "zero-free strip", and the dimension-three combination \(J_0(z)-zJ_1(z)\). No prior source was located that states the Bessel-root strip, the resulting all-dimensional threshold, or the analytic \((100,3)\) certification. Searches of the current SCOPE archive by the same mathematical objects and synonymous phrases also found no overlap.

Residual originality risk is non-negligible because arXiv:2609.10517 was submitted on 9 September 2026; very recent parallel work may not yet be indexed.

## Value

The result turns a qualitative compactness-based strip into a simple explicit structural strip controlled by one Bessel zero. It produces a closed sufficient threshold in every dimension and resolves a concrete fixed-parameter certification left open in the motivating paper, without requiring a two-dimensional interval computation. The dimension-three example is certified by elementary rational inequalities, so its counterexample status does not depend on the displayed numerical approximations.

The result does not locate the actual first Fourier zero and does not claim the threshold is optimal. The convexity mechanism can cease beyond \(r_d\) while the cosine transform remains positive, so \(r_d\) should be viewed as an explicit certificate radius rather than an exact spectral boundary.
