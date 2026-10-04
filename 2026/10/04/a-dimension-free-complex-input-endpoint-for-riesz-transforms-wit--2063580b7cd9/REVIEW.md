# Review of A dimension-free complex-input endpoint for Riesz transforms with constant drift

## Correctness

PASS. The primary theorem gives
\[
\|R_v f\|_{L^{1,\infty}(\mu_v;\mathbb R^n)}
\le2\|f\|_1
\]
for real-valued data. For a complex vector \(z=a+ib\), the squared norm of
\[
\operatorname{Re}(e^{-i\theta}z)
\]
is a two-dimensional quadratic form with eigenvalues \(\lambda\) and \(1-\lambda\). When \(c\le2^{-1/2}\), direct diagonalization proves that the set of phases for which the real projection exceeds \(c|z|\) has measure at least \(4\arccos c\). Applying the real theorem to every rotated real part of the input and integrating in the phase gives
\[
\|R_v^{\mathbb C}f\|_{1,\infty}
\le
\frac{2}{c\arccos c}\|f\|_1.
\]
The exact scalar identity
\[
\int_0^{2\pi}
|\operatorname{Re}(e^{-i\theta}w)|\,d\theta
=
4|w|
\]
accounts for the input norm. The unique optimizer satisfies
\[
\theta\tan\theta=1
\]
with \(c=\cos\theta\), yielding the displayed constant.

## Originality

PASS. The motivating paper was inspected in full and explicitly restricts its endpoint theorem to real-valued data. Its obstacle construction is positivity-based, while the complex weighted \(L^2\) identity is separately recorded. The Euclidean predecessor was also inspected in full: its proof uses positive and negative parts and does not supply the constant-drift complex result. Earlier drift work is recorded by the motivating source as lacking a dimension-independent constant.

Targeted searches using the source identifier together with complex-valued input, complexification, rotational realification, dimension-free weak type, and constant drift found no covering statement. General real/complex operator-norm literature is a residual comparison risk because complexification constants are a classical topic, but no inspected source gave this weak-\(L^1\), Hilbert-target constant or the drift-Riesz consequence.

## Value

PASS. Complex scalars are the standard setting for Fourier and spectral harmonic analysis, yet the new endpoint theorem is stated only for real data because its obstacle mechanism is ordered. A separate real/imaginary argument preserves dimension independence but loses the constant from \(2\) to \(4\). The rotation argument gives a strictly better explicit universal constant and isolates a reusable geometric mechanism for complexifying Hilbert-valued weak-\(L^1\) estimates without coordinate losses.

Same-model review: passed. Independent audit: not yet performed.
