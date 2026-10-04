# Same-model review

## Correctness

**PASS.** The fixed-decomposition qubit feedback formula is
\[
F_{\mathrm{corr}}=\frac12+\frac12\sum_k|\det B_k|.
\]
Every finite Kraus representation of a rank-two channel is an isometric remixing of a minimal pair. Takagi diagonalization of the determinant quadratic form gives
\[
\det B_k=s_1x_k^2+s_2y_k^2
\]
for orthonormal coefficient columns. Triangle and reverse-triangle inequalities give the exact bounds \(s_1\pm s_2\), explicit two-outcome unitary remixings attain both, and a continuous two-outcome path attains every intermediate value. The Takagi singular values are invariant under minimal-Kraus unitary basis changes.

## Originality

**PASS, narrowly scoped.** Gregoratti--Werner solve optimal recovery for a fixed observed decomposition. Uhlmann develops determinant/concurrence geometry for rank-two channels. Memarzadeh--Cafaro--Mancini investigate environment-measurement choice specifically for amplitude damping, proving two-outcome invariance and reporting three/four-outcome numerical evidence. The inspected sources do not state the full attainable fidelity interval for every rank-two qubit channel or the iff criterion \(s_2=0\).

Targeted semantic searches for rank-two qubit channels, Kraus determinants, environment measurements, Takagi singular values, and optimal feedback did not locate an equivalent theorem. Residual overlap risk remains because determinant quadratic forms are standard in rank-two concurrence theory.

## Value

**PASS.** The result solves the environment-measurement design problem for a broad natural channel class using two intrinsic numbers. It gives exact best and worst measurements, shows that two outcomes already realize the whole range, and classifies exactly when measurement choice is irrelevant. It converts the amplitude-damping special case into a structural theorem and provides dephasing as a contrasting channel with a nontrivial full interval.

Same-model review: passed. Independent audit: not yet performed.
