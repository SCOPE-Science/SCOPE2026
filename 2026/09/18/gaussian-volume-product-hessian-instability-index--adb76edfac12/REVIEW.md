# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**  The calculation uses the standard smooth support-function parametrization
\[
x_h(u)=h(u)u+\nabla_Sh(u),\qquad
dS_K=\det(\nabla_S^2h+hI)\,d\omega,
\]
together with the Gaussian first-variation formula already used in the motivating paper.  Differentiating at \(h\equiv1\) gives
\[
A''(0)=a_\sigma\left[-\|\nabla_Sf\|_2^2+
\left(n-1-\sigma^{-2}\right)\|f\|_2^2\right].
\]
The polar calculation is independent and exact from \(\rho_{K_t^\circ}=1/(1+tf)\), giving
\[
B''(0)=a_\sigma\left(n+1-\sigma^{-2}\right)\|f\|_2^2.
\]
The product rule then produces the stated quadratic form, including the mean-square correction from \(2A'(0)B'(0)\).

As an internal consistency check, substituting a degree-one harmonic reproduces exactly the translated-ball coefficient
\[
n+1-\frac{2}{\sigma^2}
\]
computed in Proposition 5.1 of Artstein-Avidan--Fradelizi--Wyczesany.  Degree two gives \(-2/\sigma^2\), and the spherical Laplacian eigenvalues make every higher mode more negative.  The constant mode is strictly negative because
\[
\frac{e^{-1/(2\sigma^2)}}{\int_0^1e^{-r^2/(2\sigma^2)}r^{n-1}\,dr}
=
n-\frac1{\sigma^2}
\frac{\int_0^1e^{-r^2/(2\sigma^2)}r^{n+1}\,dr}
{\int_0^1e^{-r^2/(2\sigma^2)}r^{n-1}\,dr}
>
n-\frac1{\sigma^2}.
\]
No empirical computation is used in place of the proof.

## Originality

**PASS, to the best of our knowledge.**  The motivating preprint arXiv:2609.18472 was inspected in full where relevant.  It computes the second-order translated-ball perturbation and uses it to prove non-optimality for \(\sigma^2>2/(n+1)\), but it does not state or compute the Hessian for arbitrary support-function perturbations, does not diagonalize it by spherical harmonics, and does not identify its full positive index or nullspace.

Targeted literature searches combined the phrases and equivalent formulations “Gaussian volume product”, “Gaussian Blaschke-Santaló”, “second variation”, “Hessian”, “spherical harmonics”, “Morse index”, “local stability”, and “translation mode”.  No prior result matching the displayed full Hessian or the exact index statement was located.  Adjacent literature on classical volume products, Gaussian Minkowski problems and functional Blaschke-Santaló inequalities was also considered, but no stronger theorem implying this spectral calculation was found.  A current-archive search found no SCOPE record on this Gaussian volume-product Hessian.

The main residual risk is the recency of arXiv:2609.18472: closely related work may not yet be indexed.  No especially plausible inaccessible source was identified that asserts the same theorem.

## Value

**PASS.**  The result resolves the local quadratic stability question completely.  It shows that the instability exhibited by translations is not merely one witness: it exhausts the entire positive spectrum.  In the open global gap \(1/n<\sigma^2<2/(n+1)\), the ball remains strictly stable to second order in every smooth support-function direction, sharply separating the unresolved global problem from local bifurcation at quadratic order.  At the transition, the nullspace is identified exactly.

## Limitations

The theorem is infinitesimal.  It does not prove a uniform infinite-dimensional nonlinear local maximum, does not settle the global gap in dimensions \(n\ge3\), and does not determine the higher-order behavior of the translation modes at the critical parameter.  It is stated for smooth support-function perturbations.  The motivating preprint is very recent, so unindexed parallel work remains possible.
