# Review

## Correctness

PASS. The AggMo quadratic dynamics decouple exactly along Hessian eigenvectors. For each scalar mode, the characteristic equation is
\[
z-1+\frac{s z}{K}\sum_i\frac{1}{z-\beta_i}=0.
\]
The root at \(z=1\) moves into the unit disk for small positive \(s\). A direct phase calculation shows that no nonreal point on the unit circle can solve the characteristic equation for real positive \(s\). The only possible crossing is \(z=-1\), which occurs exactly at
\[
s_\star=\frac{2K}{\sum_i(1+\beta_i)^{-1}}.
\]
The exact sign of \((-1)^{K+1}P_s(-1)\) then rules out Schur stability for every larger \(s\). Modal monotonicity in \(s=\gamma\lambda\) gives the full SPD condition \(0<\gamma L<s_\star\).

Risk: this is an outer stability theorem, not a formula for the optimal interior spectral radius.

## Originality

PASS. The defining AggMo paper was inspected in full. It derives the exact quadratic state matrix and uses direct eigenvalue computation for convergence-rate plots; its open-questions section explicitly proposes closed-form spectral analysis of the reduced modal block as future work. The inspected QHM paper later relates extended AggMo to QHM and compares their damping behavior, but does not state the harmonic-mean Schur boundary for the original equal-weight multi-buffer update.

Focused database and literature searches for AggMo, quadratic Schur stability, unit-circle crossings, harmonic-mean damping formulas, and exact learning-rate ceilings found only adjacent stability results for other momentum and splitting methods. No inspected source implied the complete claim.

## Value

PASS. The source paper's central motivation is that heterogeneous damping suppresses oscillations while retaining aggressive momentum. The exact boundary clarifies what that mechanism can and cannot do: the absolute quadratic stepsize ceiling is twice the harmonic mean of \(1+\beta_i\), so it always lies between the individual single-buffer ceilings. This separates passive damping's genuine interior spectral benefit from any mistaken interpretation that aggregation enlarges the outer Schur region. The formula also gives immediate safety constants for the paper's default damping vectors and asymptotic \(K\)-families.

Same-model review: passed. Independent audit: not yet performed.
