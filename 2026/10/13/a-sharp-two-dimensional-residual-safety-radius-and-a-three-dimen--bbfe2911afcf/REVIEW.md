# Self-review

## Correctness
PASS. The Newton–Schulz residual satisfies
\[
E_{k+1}=E_k^2
\]
exactly. In dimension two, unitary Schur triangularization reduces the Frobenius comparison to three scalar terms. Spectral radius at most \(1/2\) forces each term to be nonexpansive; a repeated-eigenvalue Jordan family proves sharpness above \(1/2\).

In dimension three, the two-edge nilpotent shift has zero spectral radius, squares to a single entry of size \(M^2\), and fourth power zero. This gives unbounded first-step amplification and exact second-step termination. Taking \(A=I\) and \(X_0=I-E_0\) realizes the residual sequence in an actual matrix-inversion problem. The packaged checker replays representative exact identities.

## Originality
PASS with stated residual risks. The Newton–Schulz formula, residual squaring, spectral-radius convergence criterion, and generic nonnormal transient growth are prior work and are excluded from the originality claim.

The closest full inversion source was inspected around its convergence and residual discussion; targeted searches found no Frobenius, nonnormal, transient, nilpotent, or minimal-dimension classification. Published-record searches likewise returned broader normal spectral-filter and generic power-transient results rather than the Newton–Schulz theorem stated here.

The main residual risk is older nonnormal matrix-power literature or an inaccessible inversion paper containing the same small-dimensional observation in different terminology.

## Value
PASS. Spectral-radius convergence is strictly weaker than norm contraction, and Newton–Schulz residuals are routinely monitored as inverse-quality diagnostics. The result provides an exact boundary in dimension two and proves that dimension three already allows arbitrarily misleading first-step residual behavior even for a perfectly conditioned target and an iteration that terminates exactly one step later.

## Closest literature and limitations
The closest inspected literature gives the classical Newton–Schulz inverse recurrence and spectral-radius convergence condition, along with broader Newton–Schulz matrix-iteration analysis. The universal \(2\times2\) result is Frobenius-specific, practical scaled initializations may avoid the obstruction, and floating-point behavior is outside scope.

Self-review: passed. Independent audit: not yet performed.
