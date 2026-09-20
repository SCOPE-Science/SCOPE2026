# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** For a symmetric matrix, one GMRES(1) step has
\(\alpha=(e^TA^3e)/(e^TA^4e)\). In an orthonormal eigenbasis this implies the
exact moment constraint \(\sum_iw_i z_i^3(1-z_i)=0\) for
\(z_i=\alpha\lambda_i\). The scalar certificate
\[
\frac43-(1-z)^2-12z^3(1-z)=\frac{(6z^2-3z-1)^2}{3}\ge0
\]
then proves the \(4/3\) squared-error bound with no hidden spectral assumption.
The equality conditions force active scaled eigenvalues to the two roots of
\(6z^2-3z-1\); the stated positive weight satisfies the moment constraint and
therefore attains equality.

The two-cycle was checked algebraically. The equality witness has step lengths
\(1,-2\); the quadratic root relation gives
\((1+2\lambda)(1-\lambda)=2/3\) on both eigenspaces, so the error direction returns
after two steps. The residual ratios on the two alternating steps are both
\(\sqrt{2/3}\). The definite-matrix monotonicity claim follows from the displayed
nonnegative double-sum representation of \(m_1m_4-m_2m_3\). The absence of a
nontrivial absolute-condition-number safety threshold follows from the exact
2-by-2 formula and its positive derivative at the stagnating weight. The
nonsymmetric upper-triangular family directly gives unbounded solution-error
amplification, so the symmetry limitation is genuine.

A deterministic NumPy check reproduced all exact constants to floating-point
accuracy and found no violation in 5,000 random symmetric tests. Numerical
checks support but do not replace the proof.

## Originality

**PASS, to the best of our knowledge.** The checked literature clearly distinguishes
residual minimization from solution-error control. Weiss (1994) gives the broad
qualitative warning that decreasing residuals can accompany increasing errors.
Meurant (2011) develops formulas and estimates for GMRES/FOM solution-error norms.
Saad (2000) analyzes minimum-residual convergence bounds. Most importantly, the
accessible theorem-level 2025 analysis of MRI/GMRES(1) by He studies one-step,
q-linear and root convergence of the residual; it gives worst-case factor one for
symmetric indefinite systems but does not formulate the Euclidean solution-error
bound proved here.

Searches covered GMRES(1), minimal residual iteration/MRI, Orthomin(1), minimum
residual and minimal discrepancy terminology, restarted GMRES with restart one,
symmetric indefinite systems, Euclidean solution error, one-step error amplification,
error monotonicity, and exact/synonymous searches for \(2/\sqrt3\), \(4/3\),
\(\sqrt{33}\), and the equality spectrum. No source located the dimension-free
\(2/\sqrt3\) solution-error barrier, its equality classification, or the exact
alternating equality cycle.

Residual originality risk is material. The complete theorem-level contents of
Fridman's short 1963 minimum-error note and Saad's 2000 article were not fully
available, and the broad Weiss (1994) and Meurant (2011) papers could contain an
equivalent inequality under different notation. This uncertainty is explicitly
retained; inaccessible literature is not treated as evidence of absence.

## Value

**PASS.** Residual minimization guarantees monotonic residuals but does not generally
control solution-error transients. For symmetric systems the result supplies a
sharp, scale-free and condition-number-free per-cycle cap on that mismatch. The
explicit two-cycle shows that the sharp error spike can recur indefinitely while
the residual contracts on every step, making the phenomenon more structural than a
single exceptional initialization. The definite/indefinite dichotomy, the lack of
any nontrivial absolute-condition-number monotonicity threshold, and the
nonsymmetric unbounded contrast delimit exactly which part of the bound comes from
self-adjoint structure.

## Scientific limitations

The result is for exact arithmetic, real symmetric nonsingular matrices and
unpreconditioned GMRES(1)/MRI in the ordinary Euclidean norm. It is not a per-step
statement about full MINRES or full GMRES after the first Krylov direction, and it
does not cover arbitrary left/right preconditioning, variable preconditioners,
finite-precision loss of orthogonality, or nonsymmetric matrices. The universal
bound is local to one restart-one cycle and does not assert global convergence of
MRI on symmetric indefinite systems. Broad historical minimum-residual and
minimum-error literature leaves residual prior-coverage risk. Independent audit has
not been performed.
