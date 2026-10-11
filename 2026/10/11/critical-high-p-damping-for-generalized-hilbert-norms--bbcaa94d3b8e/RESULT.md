# Critical high-\(p\) damping for generalized Hilbert norms

## Finding

Fix
\[
\alpha>-1.
\]
In the exact-norm regime
\[
p\ge 2(\alpha+2),
\qquad
b\ge0,
\]
the generalized Hilbert operator on the weighted Bergman space
\[
A_\alpha^p
\]
has norm
\[
N_{\alpha,p}(b)
=
\|\mathcal H_b\|_{A_\alpha^p\to A_\alpha^p}
=
B\!\left(x,b+1-x\right),
\qquad
x=\frac{\alpha+2}{p}.
\]

As
\[
p\to\infty,
\]
the following expansion is uniform over all
\[
b\ge0:
\]
\[
\log\!\left(xN_{\alpha,p}(b)\right)
=
-x\bigl(\gamma+\psi(b+1)\bigr)
+
O(x^2).
\]
Here
\[
\psi
\]
is the digamma function and
\[
\gamma
\]
is Euler's constant. The implied constant is absolute and does not depend on
\[
b.
\]

Therefore, for any parameter choice
\[
b=b_p\ge0,
\]
if
\[
\tau_p
=
\frac{\alpha+2}{p}
\bigl(\gamma+\psi(b_p+1)\bigr)
\longrightarrow
\tau\in[0,\infty],
\]
then
\[
\frac{\alpha+2}{p}
N_{\alpha,p}(b_p)
\longrightarrow
e^{-\tau},
\]
where
\[
e^{-\infty}=0.
\]

For the important exponential scaling
\[
\log b_p=cp+o(p),
\qquad
c\ge0,
\]
this becomes
\[
N_{\alpha,p}(b_p)
\sim
\frac{p}{\alpha+2}
e^{-c(\alpha+2)}.
\]

There is also an exact scale at which the norm ceases to grow. If
\[
\log b_p
=
\frac{p}{\alpha+2}
\bigl(\log p+s+o(1)\bigr)
\]
for a fixed real number
\[
s,
\]
then
\[
N_{\alpha,p}(b_p)
\longrightarrow
\frac{e^{-s}}{\alpha+2}.
\]
If the logarithm of
\[
b_p
\]
exceeds this critical scale by
\[
\omega(p),
\]
then
\[
N_{\alpha,p}(b_p)\to0.
\]
If it lies below the critical scale by
\[
\omega(p),
\]
then
\[
N_{\alpha,p}(b_p)\to\infty.
\]

Thus the generalized parameter
\[
b
\]
does not alter the leading high-\(p\) blow-up when it is subexponential in
\[
p.
\]
It changes the leading constant on the exponential scale and fully offsets the high-\(p\) growth only at the superexponential scale
\[
b_p
\asymp
p^{\,p/(\alpha+2)}
\]
up to exponential-in-\(p\) factors.

## Assumptions and scope

The source defines the generalized Hilbert operator
\[
\mathcal H_b
\]
for
\[
b\ge0
\]
and proves, for every
\[
\alpha>-1
\]
and
\[
p\ge2(\alpha+2),
\]
the exact norm identity
\[
\|\mathcal H_b\|_{A_\alpha^p\to A_\alpha^p}
=
B\!\left(
\frac{\alpha+2}{p},
b+1-\frac{\alpha+2}{p}
\right).
\]

The present result analyzes that source-proved exact regime. It does not enlarge the unresolved parameter region in which the beta-function formula itself is not yet known to equal the operator norm.

The weight convention is the source convention
\[
dA_\alpha(z)
=
(\alpha+1)(1-|z|^2)^\alpha\,dA(z).
\]

The asymptotics keep
\[
\alpha
\]
fixed. The generalized parameter
\[
b=b_p
\]
may vary arbitrarily with
\[
p,
\]
including superexponential growth.

## Proof

Put
\[
x=\frac{\alpha+2}{p}.
\]
In the exact-norm range,
\[
0<x\le\frac12.
\]
Using the beta-gamma identity,
\[
xN_{\alpha,p}(b)
=
x
\frac{\Gamma(x)\Gamma(b+1-x)}
{\Gamma(b+1)}
=
\Gamma(1+x)
\frac{\Gamma(b+1-x)}
{\Gamma(b+1)}.
\]
Hence
\[
\log\!\left(xN_{\alpha,p}(b)\right)
=
\log\Gamma(1+x)
+
\log\Gamma(b+1-x)
-
\log\Gamma(b+1).
\]

Taylor expansion at
\[
1
\]
gives
\[
\log\Gamma(1+x)
=
-\gamma x+O(x^2)
\]
uniformly for
\[
0\le x\le\frac12.
\]

For the second gamma difference, Taylor's theorem gives
\[
\log\Gamma(b+1-x)
-
\log\Gamma(b+1)
=
-x\psi(b+1)
+
\frac{x^2}{2}
\psi_1(b+1-\theta x)
\]
for some
\[
0<\theta<1,
\]
where
\[
\psi_1
\]
is the trigamma function. Since
\[
b+1-\theta x\ge\frac12
\]
and
\[
\psi_1
\]
is positive and decreasing on the positive real axis,
\[
0<
\psi_1(b+1-\theta x)
\le
\psi_1(1/2)
=
\frac{\pi^2}{2}.
\]
Thus the remainder is
\[
O(x^2)
\]
with an absolute constant independent of
\[
b.
\]
Combining the two expansions proves
\[
\log\!\left(xN_{\alpha,p}(b)\right)
=
-x\bigl(\gamma+\psi(b+1)\bigr)
+
O(x^2).
\]

Because
\[
\psi
\]
is increasing and
\[
\psi(1)=-\gamma,
\]
the quantity
\[
\gamma+\psi(b+1)
\]
is nonnegative for every
\[
b\ge0.
\]
If
\[
\tau_p
=
x\bigl(\gamma+\psi(b_p+1)\bigr)
\to\tau,
\]
then
\[
x^2\to0,
\]
so exponentiation yields
\[
xN_{\alpha,p}(b_p)
\to
e^{-\tau}.
\]

Now suppose
\[
b_p\to\infty.
\]
The standard digamma asymptotic
\[
\psi(b+1)=\log b+O(1/b)
\]
gives
\[
\tau_p
=
\frac{\alpha+2}{p}\log b_p+o(1)
\]
whenever
\[
\log b_p=O(p\log p).
\]
In particular, if
\[
\log b_p=cp+o(p),
\]
then
\[
\tau_p\to c(\alpha+2),
\]
and therefore
\[
N_{\alpha,p}(b_p)
\sim
\frac{p}{\alpha+2}
e^{-c(\alpha+2)}.
\]

For the finite-norm transition, assume
\[
\log b_p
=
\frac{p}{\alpha+2}
\bigl(\log p+s+o(1)\bigr).
\]
Then
\[
\tau_p
=
\log p+s+o(1),
\]
so
\[
\frac{\alpha+2}{p}
N_{\alpha,p}(b_p)
=
p^{-1}e^{-s+o(1)}.
\]
Multiplication by
\[
p/(\alpha+2)
\]
gives
\[
N_{\alpha,p}(b_p)
\to
\frac{e^{-s}}{\alpha+2}.
\]

More generally, write
\[
\log b_p
=
\frac{p}{\alpha+2}
\bigl(\log p+s_p\bigr).
\]
The same calculation gives
\[
N_{\alpha,p}(b_p)
=
\frac{e^{-s_p+o(1)}}{\alpha+2}.
\]
Thus
\[
s_p\to+\infty
\]
forces the norm to zero, whereas
\[
s_p\to-\infty
\]
forces it to infinity. This proves the complete critical-scale trichotomy.

## Verification

The proof uses the exact norm identity only inside the source-proved range
\[
p\ge2(\alpha+2).
\]

The key uniformity point is the lower bound
\[
b+1-\theta x\ge1/2.
\]
It makes the trigamma remainder uniformly bounded even when
\[
b=b_p
\]
depends arbitrarily on
\[
p.
\]
Thus no hidden bounded-\(b\) assumption enters the high-\(p\) expansion.

The normalization
\[
xN_{\alpha,p}(b)
\]
was checked directly from
\[
x\Gamma(x)=\Gamma(1+x).
\]
For
\[
b=0,
\]
the source formula reduces to
\[
B(x,1-x)=\frac{\pi}{\sin(\pi x)},
\]
and the uniform expansion reduces consistently to
\[
x\frac{\pi}{\sin(\pi x)}
=
1+O(x^2).
\]

For fixed
\[
b,
\]
the formula also yields
\[
N_{\alpha,p}(b)
=
\frac{p}{\alpha+2}
-
\bigl(\gamma+\psi(b+1)\bigr)
+
O_\alpha(p^{-1}),
\]
which provides an independent check of the leading scale.

Numerical evaluations of the exact beta function were used only to check representative parameter choices. No finite computation or numerical extrapolation is used to prove the uniform asymptotic or the critical scale.

## Relationship to prior work

Li, Li, Pan, Wulan, and Zhou prove the exact beta-function norm on a substantial parameter range and emphasize that the generalized parameter
\[
b
\]
changes the operator structurally rather than serving as a cosmetic reparametrization. Their paper does not analyze simultaneous high-\(p\), high-\(b\) limits or identify a scale at which the generalized parameter compensates for high-\(p\) norm growth.

Earlier work on generalized Hilbert operators on Bergman spaces establishes boundedness conditions and upper norm estimates, while work on classical Hilbert matrix operators determines exact or essential norms in fixed-parameter settings. Those results do not provide the uniform two-parameter expansion above.

The special-function ingredients themselves are classical: beta-gamma identities, digamma asymptotics, and complete-monotonicity phenomena for gamma ratios are well known. The new content here is the operator-theoretic uniformization over all
\[
b\ge0
\]
and the resulting critical damping law for the exact weighted-Bergman operator norm.

Targeted searches under the source identifier, exact beta norm, high-\(p\)/high-\(b\) scaling, digamma formulations, and the critical
\[
p^{\,p/(\alpha+2)}
\]
scale did not locate an implication-equivalent operator-norm result.

## Limitations

The result does not address parameter values for which the exact beta-function norm formula remains open.

The critical-scale theorem fixes
\[
\alpha.
\]
A simultaneous limit in which
\[
\alpha
\]
also varies would require separate uniform control.

The statement concerns operator norms, not spectra, essential norms, compactness, or extremizing functions.

The special-function expansion is uniform in
\[
b,
\]
but its operator interpretation depends on the cited exact-norm theorem.

## References

1. D. Li, S. Li, W. Pan, H. Wulan, and M. Zhou, *Norm of the generalized Hilbert operator on weighted Bergman spaces*, arXiv:2609.04833v1, first posted 4 September 2026.
2. S. Bhuyan and S. Naik, *Generalized Hilbert operator on Bergman spaces*, Korean Journal of Mathematics 33 (2025), 7--19, DOI: 10.11568/kjm.2025.33.1.7.
3. M. Lindström, S. Miihkinen, and D. Norrbo, *Exact essential norm of generalized Hilbert matrix operators on classical analytic function spaces*, arXiv:2201.09591; published 2022.
