# Exact two-jet Lu Qi-Keng phase for the canonical ξ-Bergman Gram kernel

## Finding

Let
\[
\mathbb H=\{z\in\mathbb C:\operatorname{Im}z>0\},
\]
and let \(B_\xi\) be the canonical Gram kernel obtained from the differential sequence \(\xi\) by the Riesz-family construction of Gehlawat--Jain--Sarkar.

Assume that \(\xi\) is nonzero and supported in
\[
\{0,1\},
\]
so
\[
\xi=(\xi_0,\xi_1,0,\ldots).
\]
Then the zero-free phase of \(B_\xi\) on
\[
\mathbb H\times\mathbb H
\]
is completely classified.

If
\[
\xi_0=0,
\]
then \(B_\xi\) is zero-free. If
\[
\xi_0\ne0,
\]
then
\[
B_\xi(z,w)\ne0
\quad\text{for every }z,w\in\mathbb H
\]
if and only if
\[
\operatorname{Im}\!\left(\frac{\xi_1}{\xi_0}\right)\ge0.
\]
Thus the first genuinely mixed differential functional already has a sharp phase boundary: the lower half of the projective coefficient plane produces kernel zeros, while the closed upper half is zero-free.

## Assumptions and scope

The result uses the canonical positive-definite Gram kernel itself. For a sequence supported in
\[
\{0,1\},
\]
write
\[
R_\xi(\cdot,w)
=
\xi_0K^{(0,0)}(\cdot,w)
+
\xi_1K^{(0,1)}(\cdot,w),
\]
and
\[
B_\xi(z,w)
=
\langle R_\xi(\cdot,w),R_\xi(\cdot,z)\rangle_{A^2(\mathbb H)}.
\]
Here the Bergman-space inner product is linear in the first argument. The complex conjugations in the coefficient formula below are therefore fixed by the Gram definition, rather than inferred from a displayed coefficient expansion.

The classification concerns the zero set of \(B_\xi\) on
\[
\mathbb H\times\mathbb H.
\]
It does not address higher support
\[
\{0,1,\ldots,N\}
\]
with
\[
N\ge2,
\]
where the auxiliary polynomial has higher degree and its half-plane stability problem is genuinely different.

The result also does not require an identification of the diagonal of \(B_\xi\) with a separately normalized extremal quantity for arbitrary complex coefficient sequences.

## Proof

The classical Bergman kernel of the upper half-plane is
\[
K_{\mathbb H}(z,w)
=
-\frac1{\pi(z-\overline w)^2}.
\]
Put
\[
u=z-\overline w.
\]
Direct differentiation gives
\[
K^{(m,n)}_{\mathbb H}(z,w)
=
\frac{(-1)^{m+1}(m+n+1)!}{\pi u^{m+n+2}}.
\]

Expanding the Gram product yields
\[
B_\xi(z,w)
=
\sum_{m,n=0}^1
\frac{\overline{\xi_m}\xi_n}{m!n!}
K^{(m,n)}_{\mathbb H}(z,w).
\]
Therefore, with
\[
t=\frac1u,
\]
we have
\[
B_\xi(z,w)
=
-\frac1{\pi u^2}F_\xi(t),
\]
where
\[
F_\xi(t)
=
|\xi_0|^2
+2(\overline{\xi_0}\xi_1-\overline{\xi_1}\xi_0)t
-6|\xi_1|^2t^2.
\]

First suppose
\[
\xi_0=0.
\]
Because \(\xi\) is nonzero,
\[
\xi_1\ne0,
\]
and
\[
F_\xi(t)=-6|\xi_1|^2t^2.
\]
The value
\[
t=0
\]
is not obtained from finite
\[
z,w\in\mathbb H,
\]
so the kernel is zero-free.

Now suppose
\[
\xi_0\ne0
\]
and write
\[
a=\frac{\xi_1}{\xi_0}=x+iy.
\]
Then
\[
\frac{F_\xi(t)}{|\xi_0|^2}
=
1+4iyt-6(x^2+y^2)t^2.
\]
If
\[
a=0,
\]
this is the constant function
\[
1,
\]
so the kernel is zero-free.

Assume
\[
a\ne0.
\]
The two roots are
\[
t_\pm
=
\frac{2iy\pm\sqrt2\sqrt{3x^2+y^2}}{6(x^2+y^2)}.
\]
The square-root term is real, hence
\[
\operatorname{Im}t_\pm
=
\frac{y}{3(x^2+y^2)}.
\]
Thus both roots lie in the lower half-plane exactly when
\[
y<0,
\]
both lie on the real axis when
\[
y=0,
\]
and both lie in the upper half-plane when
\[
y>0.
\]

It remains only to identify the attainable \(t\)-region. If
\[
z,w\in\mathbb H,
\]
then
\[
\operatorname{Im}(z-\overline w)
=
\operatorname{Im}z+\operatorname{Im}w
>0,
\]
so
\[
t=(z-\overline w)^{-1}
\]
lies in the lower half-plane.

Conversely, take any lower-half-plane value
\[
t_*.
\]
Then
\[
u_*=1/t_*
\]
lies in the upper half-plane. Writing
\[
u_*=p+iq,
\qquad q>0,
\]
choose
\[
z=\frac p2+i\frac q2,
\qquad
w=-\frac p2+i\frac q2.
\]
Then
\[
z,w\in\mathbb H
\]
and
\[
z-\overline w=u_*.
\]
Hence the map
\[
(z,w)\longmapsto (z-\overline w)^{-1}
\]
is onto the lower half-plane.

The prefactor
\[
-1/(\pi u^2)
\]
never vanishes. Therefore \(B_\xi\) has a zero in
\[
\mathbb H\times\mathbb H
\]
exactly when \(F_\xi\) has a zero in the lower half-plane, which occurs exactly when
\[
\operatorname{Im}(\xi_1/\xi_0)<0.
\]
This proves the classification.

## Verification

The coefficient formula was reconstructed directly from the Gram definition and the derivative formula for
\[
K_{\mathbb H}(z,w),
\]
including the conjugation forced by the Hilbert-space inner product.

The root calculation is exact. The discriminant of
\[
1+4iyt-6(x^2+y^2)t^2
\]
is real and strictly positive whenever
\[
a\ne0,
\]
so the two displayed roots are distinct and their imaginary parts have exactly the sign of
\[
y.
\]

The geometric range of
\[
t=(z-\overline w)^{-1}
\]
was checked in both directions, not merely by inclusion. This is what turns the root-location calculation into an if-and-only-if kernel-zero statement.

The primary preprint was inspected at the Gram-kernel definition, its derivative representation, the upper-half-plane reduction to an entire factor, the definition of the corresponding Lu Qi-Keng property, and the two special zero-free families proved there. Its Lu Qi-Keng theorem treats the single-index sequences and the factorial sequence; it does not classify the mixed two-coefficient family considered here.

No numerical sampling is used in the proof.

## Relationship to prior work

Gehlawat, Jain, and Sarkar introduce the canonical positive-definite Gram kernel associated with the differential-functional construction and reduce its upper-half-plane zero problem to the location of zeros of an auxiliary entire function. Their proved Lu Qi-Keng examples are the single-index sequences and the factorial sequence.

The earlier work of Bao, Guan, and collaborators develops the extremal \(\xi\)-Bergman and \(p\)-Bergman theories, but its stated scope concerns extremal, regularity, singularity-exponent, and higher-order kernel questions rather than the two-variable upper-half-plane zero set of the new Gram kernel.

The present result solves the smallest mixed finite-support case completely. The invariant coefficient is the projective ratio
\[
\xi_1/\xi_0,
\]
and the phase boundary is the real axis in that parameter plane. Multiplying the whole sequence by a nonzero complex scalar leaves the ratio unchanged and multiplies the Gram kernel by a nonzero positive scalar, so the classification is genuinely projective rather than a normalization artifact.

Targeted searches for two-coefficient \(\xi\)-Bergman sequences, first-derivative mixtures, half-plane root stability, and the ratio
\[
\xi_1/\xi_0
\]
did not locate an implication-equivalent published statement.

## Limitations

Only support in
\[
\{0,1\}
\]
is classified. The next finite-support case leads to a higher-degree stability problem and is not claimed here.

The statement is about the canonical Gram kernel \(B_\xi\) defined by the Riesz-family construction. It deliberately avoids relying on any additional diagonal-identification convention for arbitrary complex sequences.

The literature on this particular canonical two-variable kernel is very recent, so an unindexed independent observation of the same quadratic phase diagram remains possible.

## References

1. S. Gehlawat, A. Jain, and A. D. Sarkar, *A Canonical Positive Definite Kernel Associated with the \(\xi\)-Bergman Kernel*, arXiv:2608.13193v1, 2026.
2. S. Bao, Q. Guan, and X. Sun, *On the \(p\)-Bergman kernel with respect to a functional \(\xi\)*, arXiv:2510.13144v1, 2025.
3. S. Bao, Q. Guan, and Z. Yuan, *A Note on \(\xi\)-Bergman Kernels*, Frontiers of Mathematics 20 (2025), 481--506, DOI: 10.1007/s11464-023-0021-1.
