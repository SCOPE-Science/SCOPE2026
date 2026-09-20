# Review: Semifinite-gap Floquet selection in the trigonometric Nosé–Hoover orbit

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The starting normal variational equation is stated explicitly in arXiv:2609.19958v1. The change of variable \(\tau=(z_0-bt)/2\) gives
\[
X''-4\alpha\sin2\tau\,X'+\nu X=0,
\quad
\alpha=\frac{a}{2b},\quad \nu=\frac4{b^2}.
\]
The periodic gauge \(\psi=e^{\alpha\cos2\tau}X\) gives exactly
\[
-\psi''-(4\alpha\cos2\tau+2\alpha^2\cos4\tau)\psi
=(\nu-2\alpha^2)\psi,
\]
which is the \(s=1\) Whittaker–Hill operator in the convention of Hemery–Veselov. Since the gauge has period \(\pi\), Floquet stability is preserved. Abel's identity independently gives unit determinant of the transverse monodromy.

The gap-selection statement follows directly from the cited Whittaker–Hill theorem: for \(s=1=2m+1\) with \(m=0\), all even gaps are closed. The principal anti-periodic characteristic values were checked by degenerate perturbation theory and symbolic substitution. Numerical integration of the original transverse system gives reciprocal multipliers and places the first \(b=1/2\) trace crossing at \(a=1.590316803016\ldots\). The numerical threshold is explicitly labeled numerical and is not used as a proof of the spectral theorem.

Adversarial checks considered sign conventions, the reversal of the \(\tau\) direction over one physical period, and the periodic gauge. Direction reversal inverts the monodromy, but because its determinant is one the multiplier set and stability classification are unchanged. Sign changes of \(a/b\) are related by the half-period symmetry of the Whittaker–Hill potential.

## Originality

**PASS, to the best of our knowledge.** The source paper derives the normal variational equation and transforms it to a double-confluent Heun equation for differential-Galois purposes, but the inspected full text contains no Floquet or Whittaker–Hill analysis. The source reports a central regular regime and a transition near \(a\simeq1.6\) for \(b=1/2\) without identifying the anti-periodic monodromy crossing.

The Whittaker–Hill equation, semifinite-gap property, and gap-closing theorem are classical prior art and are expressly excluded from the novelty claim. Hemery–Veselov, following Magnus–Winkler and Djakov–Mityagin, state the relevant theorem in full. Searches using the exact arXiv identifier, title, author names, "Floquet", "Whittaker-Hill", "periodic orbit stability", and the numerical threshold did not locate a source-specific prior statement of this reduction or its consequences. The current SCOPE archive was also checked by source identifier and equivalent terminology without finding overlap.

Residual originality risk remains because older parametrically damped oscillator literature contains many Hill-equation reductions, and an unindexed note could conceivably specialize the same classical spectral theorem to this newly introduced trigonometric Nosé–Hoover model. No concrete prior coverage of this source-specific identification was found.

## Value

**PASS.** The result turns a variational equation used only as a non-integrability certificate into an exact stability problem with classical spectral structure. It provides: (i) an exact band/gap criterion for the central orbit over the full parameter plane; (ii) an exact reciprocal-multiplier constraint; (iii) a non-generic parity selection rule suppressing every weak-coupling periodic instability tongue; (iv) explicit leading boundaries and growth rate for the principal anti-periodic tongue; and (v) a quantitative local explanation of the source paper's independently observed transition near \(a\simeq1.6\) at \(b=1/2\).

## Limitations

The analysis is restricted to the exact central orbit and linear transverse stability. It does not establish nonlinear stability, KAM persistence, attracting behavior, global bifurcations, or the mechanism of chaos away from that orbit. The finite-coupling \(b=1/2\) crossing is numerical. Originality is assessed to the best of our knowledge rather than as an exhaustive guarantee.
