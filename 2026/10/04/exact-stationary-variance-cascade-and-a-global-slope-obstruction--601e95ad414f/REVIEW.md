# Same-model review

## Correctness
PASS. Arbitrary antiderivative tests in each mRNA and protein coordinate give
\[
\mathbb E[R(p_{j_i})\mid m_i]=m_i,
\qquad
\mathbb E[m_i\mid p_i]=p_i.
\]
The residuals are exactly the coordinate speeds, producing two variance differences equal to nonnegative mean-square speeds. If either defect is zero, coordinate constancy propagates around the strictly monotone cyclic repression loop and forces equilibrium support. For a non-equilibrium stationary state, all three protein variances are positive and satisfy
\[
V_i<L^2V_{j_i},
\]
so multiplication around the cycle forces
\[
L>1.
\]
The Hill-slope maximization is elementary and the \(h=2\) specialization was replayed exactly.

Risk: the result is restricted to compactly supported invariant measures in the nonnegative concentration orthant.

## Originality
PASS. Complete same-object mathematical sources from 2006, 2015, 2018, and the open generalized-repressilator manuscript were inspected at statement and implication level. They address equilibrium stability, Hopf bifurcation, limit cycles, heteroclinic dynamics, and generalized kinetic laws, but targeted searches did not reveal the accepted invariant-measure conditional regressions or variance cascade. Direct and equivalent indexed searches likewise found no same-object statement implying the result.

Risk: general cyclic-feedback small-gain theory may contain conceptually related slope criteria, and the short residual identities could have appeared incidentally under different terminology.

## Value
PASS. The theorem matches the biological architecture of the repressilator: transcription drive, mRNA, and protein form successive dynamical stages. It quantifies the variance dissipated at each stage exactly by mean-square coordinate speed and yields a model-wide necessary condition for non-equilibrium stationary oscillation. This is a reusable stationary diagnostic and a structural recurrence obstruction, not a restatement of the known equilibrium or Hopf calculation.

Same-model review: passed. Independent audit: not yet performed.
