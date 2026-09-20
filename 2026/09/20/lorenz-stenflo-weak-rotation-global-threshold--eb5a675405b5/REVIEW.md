# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**  The central calculation was checked in two algebraically separate forms.

First, with
\[
s=(\sigma^2-k^2)/3,\qquad 0\le k<\sigma,
\]
the stated matrix \(P\) has
\[
P_{11}>0,\qquad
\det P=
\frac{(\sigma-k)^2(2\sigma-k)}
{3\sigma^2(2\sigma+k)}>0,
\]
so the storage is genuinely positive definite throughout the claimed range \(0<s\le\sigma^2/3\).

Second, direct symbolic expansion gives exactly
\[
M y^2-xy-\dot S-\frac12\psi^2=0.
\]
Combining this with
\[
\frac12\frac d{dt}(y^2+z^2)=\rho xy-y^2-\beta z^2
\]
gives the displayed Lyapunov identity without an inequality or discarded term.

The marginal case was stress-tested separately because ordinary linearization is inconclusive there.  At \(\rho=1+s/\sigma^2\), a trajectory remaining in the zero-dissipation set has \(z\equiv0\), hence \(xy\equiv0\).  Continuity and the \(y\)-equation exclude \(x\ne0\) on any interval.  With \(x\equiv0\), every nonzero solution of the remaining linear equations grows backward, so no nonzero complete bounded trajectory can lie in a compact Lyapunov level set.  Thus the largest invariant subset relevant to LaSalle is the origin.  This closes the equality case without assuming exponential decay.

For \(\rho>1+s/\sigma^2\), the constant term of the \((x,y,v)\) characteristic polynomial is negative, forcing a positive real eigenvalue.  The converse instability therefore does not depend on numerical evidence.

The frequency-domain calculation was also differentiated explicitly: the maximum of \(\Re H(i\omega)\) is at zero frequency exactly when \(s\le\sigma^2/3\), matching the parameter range in which the explicit storage reaches the pitchfork threshold.

## Originality

**PASS, to the best of our knowledge.**  The local pitchfork boundary is not new and is explicitly credited to the established Lorenz–Stenflo bifurcation literature.  Searches were made for the classical system under Lorenz–Stenflo/Stenflo terminology together with global asymptotic stability, Lyapunov, passivity, energy stability, center/stability boundary, and equivalent parameter formulations.

The strongest directly relevant prior results found were:

- Xavier–Rech (2010): local fixed-point stability and precise pitchfork/Hopf locations, with numerical parameter-space dynamics.
- Wang–Li–Hu (2010) and later bound papers: ultimate/solution bounds.
- Zhang–Xiao (2019): global boundedness and families of globally attractive sets.
- Uyaroğlu–Emiroğlu (2015): passivity-based stabilization and synchronization after adding control.
- Huang–Li–Niu–Xie (2023): symbolic local stability conditions and zero-Hopf bifurcation.
- Ovsyannikov–Rademacher–Welter–Lu (2023): large-Rayleigh periodic-attractor and transport theory, including a Lorenz–Stenflo extension.
- Naser–Abdel Aal–Gumah (2026): global stability statements for different nonautonomous generalized/high-order Lorenz models.

No inspected source stated the exact weak-rotation global if-and-only-if threshold for the unforced classical four-dimensional system, the explicit storage identity in the result, or global asymptotic stability at the nonhyperbolic pitchfork boundary.

Two sources remain material residual risks.  The full 2023 symbolic-stability chapter was not available, although its accessible abstract describes local stability and zero-Hopf results.  The full 2026 SeMA paper was also not available; its abstract concerns nonautonomous extended Lorenz-84 and high-order Lorenz–Stenflo systems rather than the classical four-dimensional autonomous equations.  These limitations prevent an absolute novelty claim, so originality is stated only to the best of our knowledge.

## Value

**PASS.**  The result joins two pieces that were previously separated in the accessible literature: the known local static bifurcation threshold and global nonlinear attraction.  In the explicit weak-rotation regime it turns a local boundary into an exact global one and settles the delicate equality case, where the origin has a zero eigenvalue.  The storage factorization also identifies a structural reason for the restriction \(s\le\sigma^2/3\): below that threshold the dominant real gain is static, while above it a nonzero-frequency resonance becomes the passivity bottleneck.  This gives both a sharp theorem in a nontrivial parameter regime and a mechanism indicating what must be overcome to extend it.

## Scientific limitations

The theorem does not classify strong rotation \(s>\sigma^2/3\), does not describe the post-pitchfork attractor structure, and applies only to the deterministic autonomous classical Lorenz–Stenflo equations with positive parameters.  It should not be transferred without proof to controlled, fractional, stochastic, modified, or high-order variants.
